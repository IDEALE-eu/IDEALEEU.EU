"""
Document processing and chunking for RAG.
"""

from typing import List, Dict, Any, Optional
import re
from dataclasses import dataclass


@dataclass
class DocumentChunk:
    """A chunk of a document."""
    text: str
    metadata: Dict[str, Any]
    chunk_id: str
    document_id: str
    start_index: int
    end_index: int


class DocumentProcessor:
    """
    Process documents for RAG indexing.
    """
    
    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 50,
        separator: str = "\n\n"
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separator = separator
    
    def process_text(
        self,
        text: str,
        document_id: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> List[DocumentChunk]:
        """
        Process raw text into chunks.
        
        Args:
            text: Raw text content
            document_id: Unique document identifier
            metadata: Optional metadata to attach to chunks
        
        Returns:
            List of DocumentChunk objects
        """
        # Clean text
        text = self._clean_text(text)
        
        # Split into chunks
        chunks = self._split_text(text)
        
        # Create chunk objects
        document_chunks = []
        for i, chunk_text in enumerate(chunks):
            chunk = DocumentChunk(
                text=chunk_text,
                metadata=metadata or {},
                chunk_id=f"{document_id}_chunk_{i}",
                document_id=document_id,
                start_index=text.find(chunk_text),
                end_index=text.find(chunk_text) + len(chunk_text)
            )
            document_chunks.append(chunk)
        
        return document_chunks
    
    def process_pdf(self, file_path: str, document_id: str) -> List[DocumentChunk]:
        """Process a PDF file."""
        try:
            from pypdf import PdfReader
            
            reader = PdfReader(file_path)
            text = ""
            
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
            
            metadata = {
                "source_type": "pdf",
                "page_count": len(reader.pages),
                "file_path": file_path
            }
            
            return self.process_text(text, document_id, metadata)
        
        except ImportError:
            raise ImportError("pypdf is required for PDF processing")
    
    def process_markdown(self, text: str, document_id: str) -> List[DocumentChunk]:
        """Process markdown text."""
        # Extract headers for metadata
        headers = re.findall(r'^#+\s+(.+)$', text, re.MULTILINE)
        
        metadata = {
            "source_type": "markdown",
            "headers": headers
        }
        
        return self.process_text(text, document_id, metadata)
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text."""
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove control characters
        text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
        
        return text.strip()
    
    def _split_text(self, text: str) -> List[str]:
        """
        Split text into chunks with overlap.
        
        Uses a simple character-based splitting with overlap.
        """
        chunks = []
        start = 0
        text_length = len(text)
        
        while start < text_length:
            end = start + self.chunk_size
            
            # Try to break at sentence boundary
            if end < text_length:
                # Look for sentence ending
                sentence_end = text.rfind('.', start, end)
                if sentence_end > start:
                    end = sentence_end + 1
            
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            # Move start position with overlap
            start = end - self.chunk_overlap
        
        return chunks
    
    def estimate_tokens(self, text: str, model: str = "gpt-3.5-turbo") -> int:
        """
        Estimate token count for text.
        
        This is a simple approximation. For accurate counts, use tiktoken.
        """
        # Rough approximation: 1 token ≈ 4 characters
        return len(text) // 4
