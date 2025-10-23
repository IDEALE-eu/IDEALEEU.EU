"""
Tests for Evaluation Metrics.
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from metrics import EvaluationMetrics
from golden_sets import GoldenSetManager, GoldenExample


class TestEvaluationMetrics:
    """Test evaluation metrics."""
    
    def test_exact_match_positive(self):
        """Test exact match with matching strings."""
        score = EvaluationMetrics.exact_match("hello world", "hello world")
        assert score == 1.0
    
    def test_exact_match_negative(self):
        """Test exact match with different strings."""
        score = EvaluationMetrics.exact_match("hello world", "goodbye world")
        assert score == 0.0
    
    def test_exact_match_case_insensitive(self):
        """Test exact match is case insensitive."""
        score = EvaluationMetrics.exact_match("Hello World", "hello world")
        assert score == 1.0
    
    def test_exact_match_whitespace_normalized(self):
        """Test exact match normalizes whitespace."""
        score = EvaluationMetrics.exact_match("hello  world", "hello world")
        assert score == 1.0
    
    def test_f1_score_perfect(self):
        """Test F1 score with identical strings."""
        score = EvaluationMetrics.f1_score("hello world", "hello world")
        assert score == 1.0
    
    def test_f1_score_partial(self):
        """Test F1 score with partial overlap."""
        score = EvaluationMetrics.f1_score("hello world", "hello there")
        assert score > 0.0
        assert score < 1.0
    
    def test_f1_score_no_overlap(self):
        """Test F1 score with no overlap."""
        score = EvaluationMetrics.f1_score("hello", "goodbye")
        assert score == 0.0
    
    def test_groundedness_score_fully_grounded(self):
        """Test groundedness when prediction is fully in context."""
        prediction = "The aircraft wingspan is 35 meters"
        context = "Technical specs: The aircraft wingspan is 35 meters and height is 12 meters"
        
        result = EvaluationMetrics.groundedness_score(prediction, context)
        
        assert result["score"] > 0.7
        assert result["is_grounded"] is True
    
    def test_groundedness_score_not_grounded(self):
        """Test groundedness when prediction is not in context."""
        prediction = "The aircraft uses nuclear propulsion"
        context = "The aircraft uses hydrogen fuel cells for propulsion"
        
        result = EvaluationMetrics.groundedness_score(prediction, context, threshold=0.7)
        
        # Should have some overlap but not be fully grounded
        assert result["score"] > 0.0
    
    def test_latency_stats(self):
        """Test latency statistics calculation."""
        latencies = [100, 150, 200, 250, 300, 350, 400]
        
        stats = EvaluationMetrics.calculate_latency_stats(latencies)
        
        assert stats["min"] == 100
        assert stats["max"] == 400
        assert stats["mean"] > 0
        assert stats["p50"] > 0
        assert stats["p95"] > 0
    
    def test_latency_stats_empty(self):
        """Test latency stats with empty list."""
        stats = EvaluationMetrics.calculate_latency_stats([])
        
        assert stats["min"] == 0.0
        assert stats["max"] == 0.0
        assert stats["mean"] == 0.0
    
    def test_cost_stats(self):
        """Test cost statistics calculation."""
        costs = ["0.001", "0.002", "0.003", "0.004"]
        
        stats = EvaluationMetrics.calculate_cost_stats(costs)
        
        assert stats["total"] == 0.010
        assert stats["mean"] == 0.0025
        assert stats["min"] == 0.001
        assert stats["max"] == 0.004


class TestGoldenSetManager:
    """Test golden set management."""
    
    def test_create_golden_set(self):
        """Test creating a golden set."""
        manager = GoldenSetManager()
        
        examples = [
            GoldenExample(
                id="ex1",
                query="What is the wingspan?",
                reference_answer="35 meters"
            ),
            GoldenExample(
                id="ex2",
                query="What is the propulsion?",
                reference_answer="Hydrogen fuel cells"
            )
        ]
        
        manager.create_golden_set("test_set", examples)
        
        retrieved = manager.get_golden_set("test_set")
        assert len(retrieved) == 2
        assert retrieved[0].id == "ex1"
    
    def test_add_example(self):
        """Test adding example to golden set."""
        manager = GoldenSetManager()
        manager.create_golden_set("test_set", [])
        
        example = GoldenExample(
            id="ex1",
            query="Test query",
            reference_answer="Test answer"
        )
        
        manager.add_example("test_set", example)
        
        retrieved = manager.get_golden_set("test_set")
        assert len(retrieved) == 1
        assert retrieved[0].id == "ex1"
    
    def test_get_nonexistent_set(self):
        """Test getting non-existent golden set."""
        manager = GoldenSetManager()
        result = manager.get_golden_set("nonexistent")
        assert result == []
