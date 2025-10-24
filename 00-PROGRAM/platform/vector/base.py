"""
Abstract base class for vector store adapters.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class VectorStoreAdapter(ABC):
    """Abstract base class for vector database adapters."""
    
    @abstractmethod
    async def create_collection(
        self,
        collection_name: str,
        dimension: int,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Create a new collection/table."""
        pass
    
    @abstractmethod
    async def delete_collection(self, collection_name: str):
        """Delete a collection/table."""
        pass
    
    @abstractmethod
    async def insert(
        self,
        collection_name: str,
        vectors: List[List[float]],
        texts: List[str],
        metadata: List[Dict[str, Any]],
        ids: Optional[List[str]] = None
    ):
        """Insert vectors into collection."""
        pass
    
    @abstractmethod
    async def search(
        self,
        collection_name: str,
        query_vector: List[float],
        top_k: int = 10,
        score_threshold: Optional[float] = None
    ) -> List[Dict[str, Any]]:
        """
        Search for similar vectors.
        
        Returns:
            List of dicts with keys: id, score, text, metadata
        """
        pass
    
    @abstractmethod
    async def delete(self, collection_name: str, ids: List[str]):
        """Delete vectors by ID."""
        pass
    
    @abstractmethod
    async def get_stats(self, collection_name: str) -> Dict[str, Any]:
        """Get collection statistics."""
        pass
