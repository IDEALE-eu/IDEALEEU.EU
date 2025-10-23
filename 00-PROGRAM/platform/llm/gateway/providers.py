"""
LLM Provider abstraction layer.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import time
import uuid


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    @abstractmethod
    async def chat(
        self,
        messages: List[Dict[str, str]],
        model: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Execute a chat completion.
        
        Returns:
            {
                "content": str,
                "prompt_tokens": int,
                "completion_tokens": int,
                "total_tokens": int,
            }
        """
        pass
    
    @abstractmethod
    async def embed(
        self,
        texts: List[str],
        model: str
    ) -> Dict[str, Any]:
        """
        Generate embeddings.
        
        Returns:
            {
                "embeddings": List[List[float]],
                "tokens": int
            }
        """
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI provider implementation."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1"
    
    async def chat(
        self,
        messages: List[Dict[str, str]],
        model: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Execute OpenAI chat completion."""
        import httpx
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
        
        if max_tokens:
            payload["max_tokens"] = max_tokens
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=60.0
            )
            response.raise_for_status()
            data = response.json()
        
        return {
            "content": data["choices"][0]["message"]["content"],
            "prompt_tokens": data["usage"]["prompt_tokens"],
            "completion_tokens": data["usage"]["completion_tokens"],
            "total_tokens": data["usage"]["total_tokens"],
        }
    
    async def embed(
        self,
        texts: List[str],
        model: str
    ) -> Dict[str, Any]:
        """Generate OpenAI embeddings."""
        import httpx
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "input": texts
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/embeddings",
                headers=headers,
                json=payload,
                timeout=60.0
            )
            response.raise_for_status()
            data = response.json()
        
        embeddings = [item["embedding"] for item in data["data"]]
        tokens = data["usage"]["total_tokens"]
        
        return {
            "embeddings": embeddings,
            "tokens": tokens
        }


class AnthropicProvider(LLMProvider):
    """Anthropic Claude provider implementation."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.anthropic.com/v1"
    
    async def chat(
        self,
        messages: List[Dict[str, str]],
        model: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Execute Anthropic chat completion."""
        import httpx
        
        # Convert messages format
        system_message = None
        formatted_messages = []
        
        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                formatted_messages.append(msg)
        
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": formatted_messages,
            "temperature": temperature,
            "max_tokens": max_tokens or 1024,
        }
        
        if system_message:
            payload["system"] = system_message
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/messages",
                headers=headers,
                json=payload,
                timeout=60.0
            )
            response.raise_for_status()
            data = response.json()
        
        return {
            "content": data["content"][0]["text"],
            "prompt_tokens": data["usage"]["input_tokens"],
            "completion_tokens": data["usage"]["output_tokens"],
            "total_tokens": data["usage"]["input_tokens"] + data["usage"]["output_tokens"],
        }
    
    async def embed(
        self,
        texts: List[str],
        model: str
    ) -> Dict[str, Any]:
        """Anthropic doesn't provide embeddings, fallback to OpenAI."""
        raise NotImplementedError("Anthropic does not provide embedding models")


class ProviderFactory:
    """Factory for creating LLM providers."""
    
    @staticmethod
    def create_provider(provider_name: str, **kwargs) -> LLMProvider:
        """Create a provider instance."""
        
        providers = {
            "openai": OpenAIProvider,
            "anthropic": AnthropicProvider,
        }
        
        provider_class = providers.get(provider_name.lower())
        if not provider_class:
            raise ValueError(f"Unknown provider: {provider_name}")
        
        return provider_class(**kwargs)
    
    @staticmethod
    def get_provider_for_model(model: str, config) -> LLMProvider:
        """Determine provider based on model name."""
        
        if model.startswith("gpt-") or model.startswith("text-embedding-"):
            if not config.openai_api_key:
                raise ValueError("OpenAI API key not configured")
            return OpenAIProvider(api_key=config.openai_api_key)
        
        elif model.startswith("claude-"):
            if not config.anthropic_api_key:
                raise ValueError("Anthropic API key not configured")
            return AnthropicProvider(api_key=config.anthropic_api_key)
        
        else:
            raise ValueError(f"Unknown model: {model}")
