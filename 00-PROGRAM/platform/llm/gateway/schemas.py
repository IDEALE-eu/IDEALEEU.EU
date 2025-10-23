"""
API schemas for LLM Gateway.
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


class ChatMessage(BaseModel):
    """A chat message."""
    role: str = Field(..., description="Message role: system, user, or assistant")
    content: str = Field(..., description="Message content")


class ChatRequest(BaseModel):
    """Request to chat endpoint."""
    
    messages: List[ChatMessage] = Field(..., description="Conversation messages")
    model: str = Field(..., description="Model to use (e.g., gpt-4, claude-3-opus)")
    
    # Optional parameters
    temperature: Optional[float] = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: Optional[int] = Field(default=None, ge=1, le=32000)
    top_p: Optional[float] = Field(default=1.0, ge=0.0, le=1.0)
    stream: bool = Field(default=False, description="Stream response")
    
    # Context for RAG
    context_ids: Optional[List[str]] = Field(default=None, description="Context IDs for RAG")
    
    # Tools (function calling)
    tools: Optional[List[Dict[str, Any]]] = Field(default=None)
    
    # Tenant/project info
    tenant_id: str = Field(..., description="Tenant identifier")
    project_id: str = Field(..., description="Project identifier")


class ChatResponse(BaseModel):
    """Response from chat endpoint."""
    
    id: str = Field(..., description="Request ID")
    model: str = Field(..., description="Model used")
    content: str = Field(..., description="Response content")
    
    # Usage stats
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    
    # Metadata
    latency_ms: int
    cost_usd: Optional[str] = None
    guardrails_passed: bool = True
    
    # RAG
    retrieved_contexts: Optional[List[Dict[str, Any]]] = None


class EmbedRequest(BaseModel):
    """Request to embed endpoint."""
    
    input: str | List[str] = Field(..., description="Text to embed")
    model: str = Field(default="text-embedding-ada-002", description="Embedding model")
    
    tenant_id: str = Field(..., description="Tenant identifier")
    project_id: str = Field(..., description="Project identifier")


class EmbedResponse(BaseModel):
    """Response from embed endpoint."""
    
    id: str = Field(..., description="Request ID")
    model: str = Field(..., description="Model used")
    embeddings: List[List[float]] = Field(..., description="Embedding vectors")
    
    # Usage
    tokens: int
    latency_ms: int
    cost_usd: Optional[str] = None


class KnowledgeSyncRequest(BaseModel):
    """Request to sync knowledge base."""
    
    context_id: str = Field(..., description="Context ID")
    source_type: str = Field(..., description="Source type: file, url, database")
    source_location: str = Field(..., description="Source location")
    
    # Options
    chunk_size: int = Field(default=512, ge=128, le=2048)
    chunk_overlap: int = Field(default=50, ge=0, le=512)
    
    tenant_id: str = Field(..., description="Tenant identifier")
    project_id: str = Field(..., description="Project identifier")


class KnowledgeSyncResponse(BaseModel):
    """Response from knowledge sync."""
    
    id: str = Field(..., description="Sync job ID")
    context_id: str
    status: str = Field(..., description="Status: pending, processing, completed, failed")
    documents_processed: int = 0
    chunks_created: int = 0


class ContextCreateRequest(BaseModel):
    """Request to create a new context."""
    
    name: str = Field(..., description="Context name")
    description: Optional[str] = None
    
    tenant_id: str = Field(..., description="Tenant identifier")
    project_id: str = Field(..., description="Project identifier")


class ContextResponse(BaseModel):
    """Response with context information."""
    
    id: str
    tenant_id: str
    project_id: str
    name: str
    description: Optional[str]
    
    document_count: int
    last_sync_at: Optional[datetime]
    created_at: datetime


class GuardrailsCheck(BaseModel):
    """Guardrails validation check."""
    
    check_name: str
    passed: bool
    severity: str  # info, warning, error
    message: Optional[str] = None


class GuardrailsResponse(BaseModel):
    """Response from guardrails validation."""
    
    passed: bool
    checks: List[GuardrailsCheck]
    modified_content: Optional[str] = None  # If content was sanitized
