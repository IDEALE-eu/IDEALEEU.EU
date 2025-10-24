"""
Evaluation metrics for LLM outputs.
"""

from typing import List, Dict, Any, Set
import re


class EvaluationMetrics:
    """
    Metrics for evaluating LLM performance.
    """
    
    @staticmethod
    def exact_match(prediction: str, reference: str) -> float:
        """
        Exact Match (EM) metric.
        
        Returns 1.0 if prediction exactly matches reference, 0.0 otherwise.
        """
        # Normalize whitespace
        pred_norm = " ".join(prediction.strip().split())
        ref_norm = " ".join(reference.strip().split())
        
        return 1.0 if pred_norm.lower() == ref_norm.lower() else 0.0
    
    @staticmethod
    def f1_score(prediction: str, reference: str) -> float:
        """
        Token-level F1 score.
        
        Computes F1 based on word overlap between prediction and reference.
        """
        # Tokenize
        pred_tokens = set(EvaluationMetrics._tokenize(prediction))
        ref_tokens = set(EvaluationMetrics._tokenize(reference))
        
        if not pred_tokens or not ref_tokens:
            return 0.0
        
        # Compute intersection
        common = pred_tokens & ref_tokens
        
        if not common:
            return 0.0
        
        # Precision and recall
        precision = len(common) / len(pred_tokens)
        recall = len(common) / len(ref_tokens)
        
        # F1
        f1 = 2 * (precision * recall) / (precision + recall)
        
        return f1
    
    @staticmethod
    def _tokenize(text: str) -> List[str]:
        """Simple tokenization."""
        # Convert to lowercase and split on non-alphanumeric
        tokens = re.findall(r'\w+', text.lower())
        return tokens
    
    @staticmethod
    def groundedness_score(
        prediction: str,
        context: str,
        threshold: float = 0.5
    ) -> Dict[str, Any]:
        """
        Measure how grounded the prediction is in the provided context.
        
        Returns a score indicating what fraction of prediction content
        can be attributed to the context.
        
        Args:
            prediction: LLM output
            context: Retrieved context/documents
            threshold: Overlap threshold for grounding
        
        Returns:
            {
                "score": float,  # 0.0 to 1.0
                "grounded_tokens": int,
                "total_tokens": int,
                "is_grounded": bool
            }
        """
        pred_tokens = set(EvaluationMetrics._tokenize(prediction))
        context_tokens = set(EvaluationMetrics._tokenize(context))
        
        if not pred_tokens:
            return {
                "score": 0.0,
                "grounded_tokens": 0,
                "total_tokens": 0,
                "is_grounded": False
            }
        
        # Count tokens in prediction that appear in context
        grounded = pred_tokens & context_tokens
        score = len(grounded) / len(pred_tokens)
        
        return {
            "score": score,
            "grounded_tokens": len(grounded),
            "total_tokens": len(pred_tokens),
            "is_grounded": score >= threshold
        }
    
    @staticmethod
    def calculate_latency_stats(latencies_ms: List[int]) -> Dict[str, float]:
        """
        Calculate latency statistics.
        
        Args:
            latencies_ms: List of latency measurements in milliseconds
        
        Returns:
            {
                "p50": float,
                "p95": float,
                "p99": float,
                "mean": float,
                "min": float,
                "max": float
            }
        """
        if not latencies_ms:
            return {
                "p50": 0.0,
                "p95": 0.0,
                "p99": 0.0,
                "mean": 0.0,
                "min": 0.0,
                "max": 0.0
            }
        
        sorted_latencies = sorted(latencies_ms)
        n = len(sorted_latencies)
        
        def percentile(p: float) -> float:
            idx = int(n * p)
            return float(sorted_latencies[min(idx, n - 1)])
        
        return {
            "p50": percentile(0.50),
            "p95": percentile(0.95),
            "p99": percentile(0.99),
            "mean": sum(latencies_ms) / n,
            "min": float(min(latencies_ms)),
            "max": float(max(latencies_ms))
        }
    
    @staticmethod
    def calculate_cost_stats(costs_usd: List[str]) -> Dict[str, float]:
        """
        Calculate cost statistics.
        
        Args:
            costs_usd: List of cost strings in USD
        
        Returns:
            {
                "total": float,
                "mean": float,
                "min": float,
                "max": float
            }
        """
        if not costs_usd:
            return {
                "total": 0.0,
                "mean": 0.0,
                "min": 0.0,
                "max": 0.0
            }
        
        costs = [float(c) for c in costs_usd]
        
        return {
            "total": sum(costs),
            "mean": sum(costs) / len(costs),
            "min": min(costs),
            "max": max(costs)
        }
