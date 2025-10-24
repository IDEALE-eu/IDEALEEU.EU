"""
RAG retrieval service.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class RetrievalResult:
    """Result from document retrieval."""
    chunk_id: str
    document_id: str
    text: str
    score: float
    metadata: Dict[str, Any]


class RAGRetriever:
    """
    Retrieval service for RAG.
    
    Retrieves relevant document chunks based on query.
    """
    
    def __init__(self, vector_store, embedding_service):
        """
        Initialize retriever.
        
        Args:
            vector_store: Vector database adapter
            embedding_service: Embedding generation service
        """
        self.vector_store = vector_store
        self.embedding_service = embedding_service
    
    async def retrieve(
        self,
        query: str,
        context_id: str,
        top_k: int = 5,
        score_threshold: float = 0.7
    ) -> List[RetrievalResult]:
        """
        Retrieve relevant document chunks.
        
        Args:
            query: Search query
            context_id: Context/collection to search in
            top_k: Number of results to return
            score_threshold: Minimum similarity score
        
        Returns:
            List of RetrievalResult objects
        """
        # Generate query embedding
        query_result = await self.embedding_service.generate_embeddings(
            texts=[query],
            normalize=True
        )
        query_embedding = query_result["embeddings"][0]
        
        # Search vector store
        results = await self.vector_store.search(
            collection_name=context_id,
            query_vector=query_embedding,
            top_k=top_k,
            score_threshold=score_threshold
        )
        
        # Convert to RetrievalResult
        retrieval_results = []
        for result in results:
            retrieval_results.append(
                RetrievalResult(
                    chunk_id=result["id"],
                    document_id=result["metadata"].get("document_id", "unknown"),
                    text=result["text"],
                    score=result["score"],
                    metadata=result["metadata"]
                )
            )
        
        return retrieval_results
    
    def format_context(self, results: List[RetrievalResult]) -> str:
        """
        Format retrieval results into context for LLM.
        
        Args:
            results: List of retrieval results
        
        Returns:
            Formatted context string
        """
        if not results:
            return ""
        
        context_parts = ["# Retrieved Context\n"]
        
        for i, result in enumerate(results, 1):
            context_parts.append(f"\n## Chunk {i} (score: {result.score:.3f})\n")
            context_parts.append(result.text)
            context_parts.append("\n")
        
        return "\n".join(context_parts)
    
    async def retrieve_and_format(
        self,
        query: str,
        context_id: str,
        top_k: int = 5,
        score_threshold: float = 0.7
    ) -> Dict[str, Any]:
        """
        Retrieve and format context in one call.
        
        Returns:
            {
                "context": str,
                "results": List[RetrievalResult],
                "num_chunks": int
            }
        """
        results = await self.retrieve(
            query=query,
            context_id=context_id,
            top_k=top_k,
            score_threshold=score_threshold
        )
        
        formatted_context = self.format_context(results)
        
        return {
            "context": formatted_context,
            "results": results,
            "num_chunks": len(results)
        }
