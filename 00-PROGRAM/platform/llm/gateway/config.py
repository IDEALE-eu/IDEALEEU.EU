"""
Configuration management for LLM Gateway.
"""

from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Gateway configuration."""

    # Service
    service_name: str = "llm-gateway"
    environment: str = Field(default="dev", alias="IDEALE_ENV")
    log_level: str = Field(default="info", alias="IDEALE_LOG_LEVEL")
    
    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_prefix: str = "/llm"
    
    # Database
    database_url: str = Field(
        default="postgresql://ideale:changeme@localhost:5432/ideale_llm",
        alias="IDEALE_DB_URL"
    )
    
    # Security
    jwt_secret_key: str = Field(default="change-me-in-production", alias="JWT_SIGNING_KEY")
    jwt_algorithm: str = "HS256"
    jwt_expiration_seconds: int = 3600
    
    # KMS
    kms_provider: str = Field(default="local", alias="KMS_PROVIDER")  # local, aws, azure, gcp
    aws_kms_key_id: Optional[str] = Field(default=None, alias="AWS_KMS_KEY_ID")
    azure_key_vault_url: Optional[str] = Field(default=None, alias="AZURE_KEY_VAULT_URL")
    gcp_kms_key_name: Optional[str] = Field(default=None, alias="GCP_KMS_KEY_NAME")
    
    # LLM Providers
    openai_api_key: Optional[str] = Field(default=None, alias="OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = Field(default=None, alias="ANTHROPIC_API_KEY")
    azure_openai_endpoint: Optional[str] = Field(default=None, alias="AZURE_OPENAI_ENDPOINT")
    azure_openai_api_key: Optional[str] = Field(default=None, alias="AZURE_OPENAI_API_KEY")
    
    # Rate limiting
    rate_limit_enabled: bool = True
    rate_limit_requests_per_minute: int = 60
    
    # Audit
    audit_log_enabled: bool = True
    audit_retention_days: int = 90
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
