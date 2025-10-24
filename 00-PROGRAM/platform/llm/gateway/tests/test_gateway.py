"""
Tests for LLM Gateway.
"""

import pytest
from unittest.mock import Mock, AsyncMock, patch
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from providers import OpenAIProvider, AnthropicProvider, ProviderFactory
from security import SecurityManager, TenantIsolation, AuditLogger
from schemas import ChatMessage, ChatRequest


class TestProviders:
    """Test LLM provider implementations."""
    
    @pytest.mark.asyncio
    async def test_openai_provider_initialization(self):
        """Test OpenAI provider can be initialized."""
        provider = OpenAIProvider(api_key="test-key")
        assert provider.api_key == "test-key"
        assert provider.base_url == "https://api.openai.com/v1"
    
    @pytest.mark.asyncio
    async def test_anthropic_provider_initialization(self):
        """Test Anthropic provider can be initialized."""
        provider = AnthropicProvider(api_key="test-key")
        assert provider.api_key == "test-key"
        assert provider.base_url == "https://api.anthropic.com/v1"
    
    def test_provider_factory_create_openai(self):
        """Test factory can create OpenAI provider."""
        provider = ProviderFactory.create_provider("openai", api_key="test")
        assert isinstance(provider, OpenAIProvider)
    
    def test_provider_factory_create_anthropic(self):
        """Test factory can create Anthropic provider."""
        provider = ProviderFactory.create_provider("anthropic", api_key="test")
        assert isinstance(provider, AnthropicProvider)
    
    def test_provider_factory_unknown_provider(self):
        """Test factory raises error for unknown provider."""
        with pytest.raises(ValueError, match="Unknown provider"):
            ProviderFactory.create_provider("unknown", api_key="test")


class TestSecurity:
    """Test security components."""
    
    def test_security_manager_create_token(self):
        """Test JWT token creation."""
        manager = SecurityManager(secret_key="test-secret")
        token = manager.create_access_token({"user_id": "test", "tenant_id": "t1"})
        assert isinstance(token, str)
        assert len(token) > 0
    
    def test_security_manager_verify_token(self):
        """Test JWT token verification."""
        manager = SecurityManager(secret_key="test-secret")
        token = manager.create_access_token({"user_id": "test", "tenant_id": "t1"})
        payload = manager.verify_token(token)
        assert payload is not None
        assert payload["user_id"] == "test"
        assert payload["tenant_id"] == "t1"
    
    def test_security_manager_verify_invalid_token(self):
        """Test invalid token returns None."""
        manager = SecurityManager(secret_key="test-secret")
        payload = manager.verify_token("invalid-token")
        assert payload is None
    
    def test_tenant_isolation_valid_access(self):
        """Test tenant isolation allows valid access."""
        result = TenantIsolation.validate_tenant_access(
            token_tenant_id="tenant1",
            request_tenant_id="tenant1",
            token_project_id="project1",
            request_project_id="project1"
        )
        assert result is True
    
    def test_tenant_isolation_invalid_tenant(self):
        """Test tenant isolation blocks different tenant."""
        result = TenantIsolation.validate_tenant_access(
            token_tenant_id="tenant1",
            request_tenant_id="tenant2"
        )
        assert result is False
    
    def test_tenant_isolation_invalid_project(self):
        """Test tenant isolation blocks different project."""
        result = TenantIsolation.validate_tenant_access(
            token_tenant_id="tenant1",
            request_tenant_id="tenant1",
            token_project_id="project1",
            request_project_id="project2"
        )
        assert result is False
    
    def test_tenant_isolation_namespace(self):
        """Test namespace generation."""
        namespace = TenantIsolation.get_namespace("tenant1", "project1")
        assert namespace == "tenant1/project1"
    
    @pytest.mark.asyncio
    async def test_audit_logger(self):
        """Test audit logging."""
        logger = AuditLogger(enabled=True)
        # Should not raise exception
        await logger.log_request(
            request_id="req1",
            tenant_id="t1",
            project_id="p1",
            user_id="u1",
            action="test",
            details={}
        )


class TestSchemas:
    """Test API schemas."""
    
    def test_chat_message_validation(self):
        """Test ChatMessage validation."""
        msg = ChatMessage(role="user", content="Hello")
        assert msg.role == "user"
        assert msg.content == "Hello"
    
    def test_chat_request_validation(self):
        """Test ChatRequest validation."""
        request = ChatRequest(
            messages=[ChatMessage(role="user", content="Hello")],
            model="gpt-4",
            tenant_id="t1",
            project_id="p1"
        )
        assert len(request.messages) == 1
        assert request.model == "gpt-4"
        assert request.temperature == 0.7  # default
    
    def test_chat_request_custom_temperature(self):
        """Test ChatRequest with custom temperature."""
        request = ChatRequest(
            messages=[ChatMessage(role="user", content="Hello")],
            model="gpt-4",
            temperature=0.5,
            tenant_id="t1",
            project_id="p1"
        )
        assert request.temperature == 0.5
