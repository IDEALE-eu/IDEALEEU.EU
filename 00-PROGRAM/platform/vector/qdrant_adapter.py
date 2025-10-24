"""
Qdrant vector database adapter.
"""

from typing import List, Dict, Any, Optional
import uuid
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from .base import VectorStoreAdapter


class QdrantAdapter(VectorStoreAdapter):
    """
    Adapter for Qdrant vector database.
    """
    
    def __init__(self, host: str = "localhost", port: int = 6333):
        """
        Initialize Qdrant adapter.
        
        Args:
            host: Qdrant server host
            port: Qdrant server port
        """
        self.client = QdrantClient(host=host, port=port)
    
    async def create_collection(
        self,
        collection_name: str,
        dimension: int,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Create a new Qdrant collection."""
        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=dimension,
                distance=Distance.COSINE
            )
        )
    
    async def delete_collection(self, collection_name: str):
        """Delete a Qdrant collection."""
        self.client.delete_collection(collection_name=collection_name)
    
    async def insert(
        self,
        collection_name: str,
        vectors: List[List[float]],
        texts: List[str],
        metadata: List[Dict[str, Any]],
        ids: Optional[List[str]] = None
    ):
        """Insert vectors into Qdrant collection."""
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in vectors]
        
        points = []
        for vec_id, vector, text, meta in zip(ids, vectors, texts, metadata):
            payload = {
                "text": text,
                **meta
            }
            
            points.append(
                PointStruct(
                    id=vec_id,
                    vector=vector,
                    payload=payload
                )
            )
        
        self.client.upsert(
            collection_name=collection_name,
            points=points
        )
    
    async def search(
        self,
        collection_name: str,
        query_vector: List[float],
        top_k: int = 10,
        score_threshold: Optional[float] = None
    ) -> List[Dict[str, Any]]:
        """Search for similar vectors in Qdrant."""
        search_result = self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=top_k,
            score_threshold=score_threshold
        )
        
        results = []
        for hit in search_result:
            payload = hit.payload
            text = payload.pop("text", "")
            
            results.append({
                "id": str(hit.id),
                "text": text,
                "metadata": payload,
                "score": hit.score
            })
        
        return results
    
    async def delete(self, collection_name: str, ids: List[str]):
        """Delete vectors by ID from Qdrant."""
        self.client.delete(
            collection_name=collection_name,
            points_selector=ids
        )
    
    async def get_stats(self, collection_name: str) -> Dict[str, Any]:
        """Get Qdrant collection statistics."""
        info = self.client.get_collection(collection_name=collection_name)
        
        return {
            "collection_name": collection_name,
            "vector_count": info.points_count,
            "dimension": info.config.params.vectors.size
        }
