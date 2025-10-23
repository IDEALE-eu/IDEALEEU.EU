"""
PostgreSQL with pgvector adapter.
"""

from typing import List, Dict, Any, Optional
import uuid
from sqlalchemy import create_engine, Column, String, Text, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from .base import VectorStoreAdapter


Base = declarative_base()


class PgVectorAdapter(VectorStoreAdapter):
    """
    Adapter for PostgreSQL with pgvector extension.
    
    Requires pgvector extension to be installed in the database.
    """
    
    def __init__(self, connection_url: str):
        """
        Initialize pgvector adapter.
        
        Args:
            connection_url: PostgreSQL connection URL
        """
        self.engine = create_engine(connection_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
        # Ensure pgvector extension is enabled
        with self.engine.connect() as conn:
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            conn.commit()
    
    async def create_collection(
        self,
        collection_name: str,
        dimension: int,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Create a new table for vector storage."""
        # Sanitize collection name
        safe_name = collection_name.replace("-", "_").replace(".", "_")
        
        with self.engine.connect() as conn:
            # Create table
            conn.execute(text(f"""
                CREATE TABLE IF NOT EXISTS {safe_name} (
                    id VARCHAR(100) PRIMARY KEY,
                    text TEXT NOT NULL,
                    embedding vector({dimension}),
                    metadata JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            
            # Create index for vector similarity search
            conn.execute(text(f"""
                CREATE INDEX IF NOT EXISTS {safe_name}_embedding_idx 
                ON {safe_name} 
                USING hnsw (embedding vector_cosine_ops)
                WITH (m = 16, ef_construction = 200)
            """))
            
            conn.commit()
    
    async def delete_collection(self, collection_name: str):
        """Delete a collection table."""
        safe_name = collection_name.replace("-", "_").replace(".", "_")
        
        with self.engine.connect() as conn:
            conn.execute(text(f"DROP TABLE IF EXISTS {safe_name}"))
            conn.commit()
    
    async def insert(
        self,
        collection_name: str,
        vectors: List[List[float]],
        texts: List[str],
        metadata: List[Dict[str, Any]],
        ids: Optional[List[str]] = None
    ):
        """Insert vectors into collection."""
        safe_name = collection_name.replace("-", "_").replace(".", "_")
        
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in vectors]
        
        with self.engine.connect() as conn:
            for i, (vec, txt, meta, vec_id) in enumerate(zip(vectors, texts, metadata, ids)):
                # Convert vector to string format for pgvector
                vec_str = "[" + ",".join(str(x) for x in vec) + "]"
                
                conn.execute(
                    text(f"""
                        INSERT INTO {safe_name} (id, text, embedding, metadata)
                        VALUES (:id, :text, :embedding::vector, :metadata::jsonb)
                        ON CONFLICT (id) DO UPDATE
                        SET text = EXCLUDED.text,
                            embedding = EXCLUDED.embedding,
                            metadata = EXCLUDED.metadata
                    """),
                    {
                        "id": vec_id,
                        "text": txt,
                        "embedding": vec_str,
                        "metadata": str(meta)
                    }
                )
            
            conn.commit()
    
    async def search(
        self,
        collection_name: str,
        query_vector: List[float],
        top_k: int = 10,
        score_threshold: Optional[float] = None
    ) -> List[Dict[str, Any]]:
        """Search for similar vectors using cosine similarity."""
        safe_name = collection_name.replace("-", "_").replace(".", "_")
        vec_str = "[" + ",".join(str(x) for x in query_vector) + "]"
        
        query = f"""
            SELECT 
                id,
                text,
                metadata,
                1 - (embedding <=> :query_vector::vector) as score
            FROM {safe_name}
            ORDER BY embedding <=> :query_vector::vector
            LIMIT :top_k
        """
        
        with self.engine.connect() as conn:
            result = conn.execute(
                text(query),
                {"query_vector": vec_str, "top_k": top_k}
            )
            
            results = []
            for row in result:
                score = float(row[3])
                
                # Apply score threshold if specified
                if score_threshold and score < score_threshold:
                    continue
                
                results.append({
                    "id": row[0],
                    "text": row[1],
                    "metadata": row[2] if row[2] else {},
                    "score": score
                })
            
            return results
    
    async def delete(self, collection_name: str, ids: List[str]):
        """Delete vectors by ID."""
        safe_name = collection_name.replace("-", "_").replace(".", "_")
        
        with self.engine.connect() as conn:
            for vec_id in ids:
                conn.execute(
                    text(f"DELETE FROM {safe_name} WHERE id = :id"),
                    {"id": vec_id}
                )
            conn.commit()
    
    async def get_stats(self, collection_name: str) -> Dict[str, Any]:
        """Get collection statistics."""
        safe_name = collection_name.replace("-", "_").replace(".", "_")
        
        with self.engine.connect() as conn:
            result = conn.execute(
                text(f"SELECT COUNT(*) FROM {safe_name}")
            )
            count = result.fetchone()[0]
            
            return {
                "collection_name": collection_name,
                "vector_count": count
            }
