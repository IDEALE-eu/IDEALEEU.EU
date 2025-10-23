"""
Embedding generation service.
"""

from typing import List, Dict, Any, Optional
import numpy as np


class EmbeddingService:
    """
    Service for generating text embeddings.
    
    Supports multiple embedding models and providers.
    """
    
    def __init__(self, default_model: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.default_model = default_model
        self.models = {}
    
    def load_model(self, model_name: str):
        """Load an embedding model."""
        if model_name in self.models:
            return self.models[model_name]
        
        # For local models (sentence-transformers)
        if model_name.startswith("sentence-transformers/"):
            from sentence_transformers import SentenceTransformer
            model = SentenceTransformer(model_name.replace("sentence-transformers/", ""))
            self.models[model_name] = model
            return model
        
        # For API-based models, return a placeholder
        return None
    
    async def generate_embeddings(
        self,
        texts: List[str],
        model: str = None,
        normalize: bool = True
    ) -> Dict[str, Any]:
        """
        Generate embeddings for a list of texts.
        
        Args:
            texts: List of text strings to embed
            model: Model to use (defaults to self.default_model)
            normalize: Whether to L2-normalize the embeddings
        
        Returns:
            {
                "embeddings": List[List[float]],
                "model": str,
                "dimensions": int
            }
        """
        model_name = model or self.default_model
        
        # Load model
        embedding_model = self.load_model(model_name)
        
        if embedding_model is None:
            raise ValueError(f"Model {model_name} not available")
        
        # Generate embeddings
        embeddings = embedding_model.encode(
            texts,
            normalize_embeddings=normalize,
            show_progress_bar=False
        )
        
        # Convert to list
        embeddings_list = embeddings.tolist()
        
        return {
            "embeddings": embeddings_list,
            "model": model_name,
            "dimensions": len(embeddings_list[0]) if embeddings_list else 0
        }
    
    async def compute_similarity(
        self,
        embedding1: List[float],
        embedding2: List[float]
    ) -> float:
        """
        Compute cosine similarity between two embeddings.
        
        Returns:
            Similarity score between -1 and 1
        """
        vec1 = np.array(embedding1)
        vec2 = np.array(embedding2)
        
        # Cosine similarity
        similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        
        return float(similarity)
    
    async def batch_similarity(
        self,
        query_embedding: List[float],
        candidate_embeddings: List[List[float]]
    ) -> List[float]:
        """
        Compute similarity between a query and multiple candidates.
        
        Returns:
            List of similarity scores
        """
        query = np.array(query_embedding)
        candidates = np.array(candidate_embeddings)
        
        # Compute dot products
        similarities = np.dot(candidates, query)
        
        # Normalize if vectors aren't already normalized
        query_norm = np.linalg.norm(query)
        candidate_norms = np.linalg.norm(candidates, axis=1)
        
        similarities = similarities / (query_norm * candidate_norms)
        
        return similarities.tolist()
