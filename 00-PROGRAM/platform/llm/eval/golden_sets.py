"""
Golden set management for evaluation.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
import json
from pathlib import Path


@dataclass
class GoldenExample:
    """A golden example for evaluation."""
    id: str
    query: str
    reference_answer: str
    context: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class GoldenSetManager:
    """
    Manage golden sets for LLM evaluation.
    """
    
    def __init__(self, storage_path: Optional[str] = None):
        """
        Initialize golden set manager.
        
        Args:
            storage_path: Path to store golden sets (optional)
        """
        self.storage_path = Path(storage_path) if storage_path else None
        self.golden_sets: Dict[str, List[GoldenExample]] = {}
    
    def create_golden_set(
        self,
        set_name: str,
        examples: List[GoldenExample]
    ):
        """
        Create a new golden set.
        
        Args:
            set_name: Name of the golden set
            examples: List of golden examples
        """
        self.golden_sets[set_name] = examples
    
    def add_example(
        self,
        set_name: str,
        example: GoldenExample
    ):
        """Add an example to a golden set."""
        if set_name not in self.golden_sets:
            self.golden_sets[set_name] = []
        
        self.golden_sets[set_name].append(example)
    
    def get_golden_set(self, set_name: str) -> List[GoldenExample]:
        """Retrieve a golden set."""
        return self.golden_sets.get(set_name, [])
    
    def save_golden_set(self, set_name: str):
        """Save a golden set to disk."""
        if not self.storage_path:
            raise ValueError("Storage path not configured")
        
        examples = self.golden_sets.get(set_name, [])
        
        self.storage_path.mkdir(parents=True, exist_ok=True)
        file_path = self.storage_path / f"{set_name}.json"
        
        # Convert to dict
        data = [asdict(ex) for ex in examples]
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_golden_set(self, set_name: str):
        """Load a golden set from disk."""
        if not self.storage_path:
            raise ValueError("Storage path not configured")
        
        file_path = self.storage_path / f"{set_name}.json"
        
        if not file_path.exists():
            raise FileNotFoundError(f"Golden set {set_name} not found")
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        examples = [GoldenExample(**item) for item in data]
        self.golden_sets[set_name] = examples
    
    def list_golden_sets(self) -> List[str]:
        """List available golden sets."""
        if not self.storage_path or not self.storage_path.exists():
            return list(self.golden_sets.keys())
        
        # List from disk
        json_files = self.storage_path.glob("*.json")
        return [f.stem for f in json_files]
