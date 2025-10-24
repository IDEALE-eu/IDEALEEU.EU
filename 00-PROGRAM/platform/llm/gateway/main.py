"""
Main API application for LLM Gateway.
"""

import uuid
import time
from typing import Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, Header, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .config import settings
from .models import Base, ChatRequest as ChatRequestModel, EmbeddingRequest as EmbeddingRequestModel
from .schemas import (
    ChatRequest, ChatResponse,
    EmbedRequest, EmbedResponse,
    KnowledgeSyncRequest, KnowledgeSyncResponse,
    ContextCreateRequest, ContextResponse
)
from .providers import ProviderFactory
from .security import SecurityManager, TenantIsolation, AuditLogger, KMSManager


# Database setup
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Initialize security components
security_manager = SecurityManager(
    secret_key=settings.jwt_secret_key,
    algorithm=settings.jwt_algorithm
)
audit_logger = AuditLogger(enabled=settings.audit_log_enabled)
kms_manager = KMSManager(
    provider=settings.kms_provider,
    aws_kms_key_id=settings.aws_kms_key_id,
    azure_key_vault_url=settings.azure_key_vault_url,
    gcp_kms_key_name=settings.gcp_kms_key_name
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle management."""
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown


app = FastAPI(
    title="IDEALE-EU LLM Gateway",
    description="Multi-tenant LLM gateway with security and audit",
    version="0.1.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency injection
def get_db():
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(authorization: Optional[str] = Header(None)):
    """Extract and validate user from Authorization header."""
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )
    
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme"
            )
        
        payload = security_manager.verify_token(token)
        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )
        
        return payload
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header format"
        )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": settings.service_name,
        "version": "0.1.0"
    }


@app.post(f"{settings.api_prefix}/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    Chat completion endpoint.
    
    Supports multiple providers and models with tenant isolation.
    """
    # Validate tenant access
    if not TenantIsolation.validate_tenant_access(
        token_tenant_id=user.get("tenant_id"),
        request_tenant_id=request.tenant_id,
        token_project_id=user.get("project_id"),
        request_project_id=request.project_id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to requested tenant/project"
        )
    
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    try:
        # Get provider for model
        provider = ProviderFactory.get_provider_for_model(request.model, settings)
        
        # Convert messages
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        # Execute chat completion
        result = await provider.chat(
            messages=messages,
            model=request.model,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        latency_ms = int((time.time() - start_time) * 1000)
        
        # Calculate cost (simplified)
        cost_usd = _calculate_cost(request.model, result["total_tokens"])
        
        # Audit log
        await audit_logger.log_request(
            request_id=request_id,
            tenant_id=request.tenant_id,
            project_id=request.project_id,
            user_id=user.get("user_id", "unknown"),
            action="chat",
            details={
                "model": request.model,
                "tokens": result["total_tokens"]
            }
        )
        
        # Store in database
        chat_record = ChatRequestModel(
            id=request_id,
            tenant_id=request.tenant_id,
            project_id=request.project_id,
            user_id=user.get("user_id", "unknown"),
            model=request.model,
            provider=provider.__class__.__name__,
            prompt=messages[-1]["content"],
            response=result["content"],
            prompt_tokens=result["prompt_tokens"],
            completion_tokens=result["completion_tokens"],
            total_tokens=result["total_tokens"],
            latency_ms=latency_ms,
            cost_usd=cost_usd,
            guardrails_passed=True
        )
        db.add(chat_record)
        db.commit()
        
        return ChatResponse(
            id=request_id,
            model=request.model,
            content=result["content"],
            prompt_tokens=result["prompt_tokens"],
            completion_tokens=result["completion_tokens"],
            total_tokens=result["total_tokens"],
            latency_ms=latency_ms,
            cost_usd=cost_usd,
            guardrails_passed=True
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Chat completion failed: {str(e)}"
        )


@app.post(f"{settings.api_prefix}/embed", response_model=EmbedResponse)
async def embed(
    request: EmbedRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    Generate embeddings.
    """
    # Validate tenant access
    if not TenantIsolation.validate_tenant_access(
        token_tenant_id=user.get("tenant_id"),
        request_tenant_id=request.tenant_id,
        token_project_id=user.get("project_id"),
        request_project_id=request.project_id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to requested tenant/project"
        )
    
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    try:
        # Get provider for model
        provider = ProviderFactory.get_provider_for_model(request.model, settings)
        
        # Convert input to list
        texts = [request.input] if isinstance(request.input, str) else request.input
        
        # Generate embeddings
        result = await provider.embed(texts=texts, model=request.model)
        
        latency_ms = int((time.time() - start_time) * 1000)
        cost_usd = _calculate_embedding_cost(request.model, result["tokens"])
        
        # Audit log
        await audit_logger.log_request(
            request_id=request_id,
            tenant_id=request.tenant_id,
            project_id=request.project_id,
            user_id=user.get("user_id", "unknown"),
            action="embed",
            details={
                "model": request.model,
                "tokens": result["tokens"]
            }
        )
        
        # Store in database
        embed_record = EmbeddingRequestModel(
            id=request_id,
            tenant_id=request.tenant_id,
            project_id=request.project_id,
            user_id=user.get("user_id", "unknown"),
            model=request.model,
            provider=provider.__class__.__name__,
            text=texts[0] if len(texts) == 1 else f"{len(texts)} texts",
            embedding_dimensions=len(result["embeddings"][0]) if result["embeddings"] else 0,
            tokens=result["tokens"],
            latency_ms=latency_ms,
            cost_usd=cost_usd
        )
        db.add(embed_record)
        db.commit()
        
        return EmbedResponse(
            id=request_id,
            model=request.model,
            embeddings=result["embeddings"],
            tokens=result["tokens"],
            latency_ms=latency_ms,
            cost_usd=cost_usd
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Embedding generation failed: {str(e)}"
        )


@app.post("/knowledge/sync", response_model=KnowledgeSyncResponse)
async def sync_knowledge(
    request: KnowledgeSyncRequest,
    user: dict = Depends(get_current_user)
):
    """
    Sync knowledge base from source.
    
    This is a placeholder - full implementation would be in the RAG service.
    """
    # Validate tenant access
    if not TenantIsolation.validate_tenant_access(
        token_tenant_id=user.get("tenant_id"),
        request_tenant_id=request.tenant_id,
        token_project_id=user.get("project_id"),
        request_project_id=request.project_id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to requested tenant/project"
        )
    
    job_id = str(uuid.uuid4())
    
    # In a real implementation, this would trigger an async job
    return KnowledgeSyncResponse(
        id=job_id,
        context_id=request.context_id,
        status="pending",
        documents_processed=0,
        chunks_created=0
    )


@app.post("/contexts", response_model=ContextResponse)
async def create_context(
    request: ContextCreateRequest,
    user: dict = Depends(get_current_user)
):
    """
    Create a new knowledge context.
    """
    # Validate tenant access
    if not TenantIsolation.validate_tenant_access(
        token_tenant_id=user.get("tenant_id"),
        request_tenant_id=request.tenant_id,
        token_project_id=user.get("project_id"),
        request_project_id=request.project_id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to requested tenant/project"
        )
    
    context_id = str(uuid.uuid4())
    
    # In a real implementation, this would create the context in the database
    return ContextResponse(
        id=context_id,
        tenant_id=request.tenant_id,
        project_id=request.project_id,
        name=request.name,
        description=request.description,
        document_count=0,
        last_sync_at=None,
        created_at=datetime.utcnow()
    )


def _calculate_cost(model: str, tokens: int) -> str:
    """Calculate approximate cost in USD."""
    # Simplified cost calculation
    # In production, use actual pricing tables
    costs_per_1k = {
        "gpt-4": 0.03,
        "gpt-3.5-turbo": 0.002,
        "claude-3-opus": 0.015,
        "claude-3-sonnet": 0.003,
    }
    
    for model_prefix, cost in costs_per_1k.items():
        if model.startswith(model_prefix):
            return f"{(tokens / 1000) * cost:.6f}"
    
    return "0.000000"


def _calculate_embedding_cost(model: str, tokens: int) -> str:
    """Calculate embedding cost."""
    costs_per_1k = {
        "text-embedding-ada-002": 0.0001,
        "text-embedding-3-small": 0.00002,
        "text-embedding-3-large": 0.00013,
    }
    
    for model_name, cost in costs_per_1k.items():
        if model == model_name:
            return f"{(tokens / 1000) * cost:.6f}"
    
    return "0.000000"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)
