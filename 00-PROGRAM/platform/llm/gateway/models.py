"""
Database models for LLM Gateway.
"""

from datetime import datetime
from typing import Optional
from sqlalchemy import Column, String, Integer, DateTime, Text, JSON, Boolean, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class ChatRequest(Base):
    """Audit log for chat requests."""
    
    __tablename__ = "chat_requests"
    
    id = Column(String(36), primary_key=True)
    tenant_id = Column(String(100), nullable=False, index=True)
    project_id = Column(String(100), nullable=False, index=True)
    user_id = Column(String(100), nullable=False, index=True)
    
    model = Column(String(100), nullable=False)
    provider = Column(String(50), nullable=False)
    
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    
    # Request metadata
    system_prompt = Column(Text, nullable=True)
    temperature = Column(String(10), nullable=True)
    max_tokens = Column(Integer, nullable=True)
    tools_used = Column(JSON, nullable=True)
    
    # Response metadata
    completion_tokens = Column(Integer, nullable=True)
    prompt_tokens = Column(Integer, nullable=True)
    total_tokens = Column(Integer, nullable=True)
    latency_ms = Column(Integer, nullable=True)
    
    # Audit
    guardrails_passed = Column(Boolean, default=True)
    guardrails_violations = Column(JSON, nullable=True)
    cost_usd = Column(String(20), nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Indexes for efficient querying
    __table_args__ = (
        Index("idx_tenant_project", "tenant_id", "project_id"),
        Index("idx_created_at", "created_at"),
    )


class EmbeddingRequest(Base):
    """Audit log for embedding requests."""
    
    __tablename__ = "embedding_requests"
    
    id = Column(String(36), primary_key=True)
    tenant_id = Column(String(100), nullable=False, index=True)
    project_id = Column(String(100), nullable=False, index=True)
    user_id = Column(String(100), nullable=False, index=True)
    
    model = Column(String(100), nullable=False)
    provider = Column(String(50), nullable=False)
    
    text = Column(Text, nullable=False)
    embedding_dimensions = Column(Integer, nullable=True)
    
    tokens = Column(Integer, nullable=True)
    latency_ms = Column(Integer, nullable=True)
    cost_usd = Column(String(20), nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    __table_args__ = (
        Index("idx_tenant_project_emb", "tenant_id", "project_id"),
        Index("idx_created_at_emb", "created_at"),
    )


class TenantConfig(Base):
    """Tenant-specific configuration."""
    
    __tablename__ = "tenant_configs"
    
    id = Column(String(36), primary_key=True)
    tenant_id = Column(String(100), nullable=False, unique=True, index=True)
    
    # Quotas
    max_requests_per_day = Column(Integer, default=1000)
    max_tokens_per_request = Column(Integer, default=4096)
    
    # Allowed models
    allowed_models = Column(JSON, nullable=False)  # List of allowed model names
    
    # Features
    rag_enabled = Column(Boolean, default=True)
    guardrails_enabled = Column(Boolean, default=True)
    audit_enabled = Column(Boolean, default=True)
    
    # Encryption
    kms_key_id = Column(String(200), nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)


class Context(Base):
    """Knowledge base contexts for RAG."""
    
    __tablename__ = "contexts"
    
    id = Column(String(36), primary_key=True)
    tenant_id = Column(String(100), nullable=False, index=True)
    project_id = Column(String(100), nullable=False, index=True)
    
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    
    # Vector store reference
    vector_store_id = Column(String(100), nullable=True)
    collection_name = Column(String(200), nullable=True)
    
    # Metadata
    document_count = Column(Integer, default=0)
    last_sync_at = Column(DateTime(timezone=True), nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    
    __table_args__ = (
        Index("idx_tenant_project_ctx", "tenant_id", "project_id"),
    )
