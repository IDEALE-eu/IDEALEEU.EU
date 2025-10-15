"""
QS Field Data Structures

Core data structures for Quantum Superposition fields and candidates.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any, Tuple
import hashlib
import json
from datetime import datetime

# Import merkle module - handle both package and standalone imports
try:
    from .merkle import compute_merkle_root
except ImportError:
    import merkle
    compute_merkle_root = merkle.compute_merkle_root


def _compute_hash(data: Dict) -> str:
    """Compute SHA-256 hash of data dictionary."""
    json_str = json.dumps(data, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(json_str.encode()).hexdigest()


@dataclass
class Candidate:
    """
    A single candidate configuration in the QS field.
    
    Attributes:
        id: Unique identifier for this candidate
        configuration: Design parameters and settings
        utcs_manifest: UTCS traceability metadata
        score_vector: Multi-objective scores (performance, cost, risk, etc.)
        uncertainty: Uncertainty quantification (sigma, confidence intervals)
        bounds: Parameter bounds (lower, upper) for each metric
        constraints_satisfied: Boolean flags for hard constraints
        provenance: Generation metadata and evidence references
        hash: SHA-256 hash of this candidate
    """
    id: str
    configuration: Dict[str, Any]
    utcs_manifest: Dict[str, Any]
    score_vector: Dict[str, float]
    uncertainty: Dict[str, float]
    bounds: Dict[str, Tuple[float, float]]
    constraints_satisfied: Dict[str, bool]
    provenance: Dict[str, Any]
    hash: str = field(default="", init=False)
    
    def __post_init__(self):
        """Compute hash after initialization."""
        self._compute_hash()
    
    def _compute_hash(self):
        """Compute/recompute hash for this candidate."""
        data = {
            "id": self.id,
            "configuration": self.configuration,
            "utcs_manifest": self.utcs_manifest,
            "score_vector": self.score_vector,
            "uncertainty": self.uncertainty,
            "bounds": self.bounds,
            "constraints_satisfied": self.constraints_satisfied,
            "provenance": self.provenance,
        }
        self.hash = _compute_hash(data)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Candidate':
        """Create Candidate from dictionary."""
        # Remove hash if present - it will be recomputed
        data_copy = {k: v for k, v in data.items() if k != 'hash'}
        return cls(**data_copy)


@dataclass
class QSField:
    """
    Quantum Superposition Field - A curated option space with proofs.
    
    Represents the pre-collapse state containing all viable candidates
    with their predictions, constraints, and cryptographic integrity proofs.
    
    Attributes:
        version: QS field version identifier (e.g., "QS_2025_Q4_v1")
        candidates: List of all candidate configurations
        scores: Aggregate scores for each candidate
        bounds: Global bounds across all candidates per metric
        priors: Prior constraints and preferences (C_0, phi_0)
        constraints: Hard constraints that must be satisfied
        merkle_root: Cryptographic root hash of all candidates
        timestamp: ISO 8601 timestamp of field creation/freeze
        frozen: Whether this field is frozen (immutable)
        metadata: Additional metadata (problem description, etc.)
    """
    version: str
    candidates: List[Candidate]
    scores: List[float]
    bounds: Dict[str, List[Tuple[float, float]]]
    priors: Dict[str, Any]
    constraints: Dict[str, Any]
    merkle_root: str = ""
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    frozen: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def freeze(self) -> str:
        """
        Freeze QS field and compute Merkle root.
        
        Makes the field immutable and computes cryptographic proof of integrity.
        
        Returns:
            Merkle root hash
            
        Raises:
            ValueError: If field is already frozen
        """
        if self.frozen:
            raise ValueError("QS field is already frozen")
        
        hashes = [c.hash for c in self.candidates]
        self.merkle_root = compute_merkle_root(hashes)
        self.frozen = True
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        return self.merkle_root
    
    def collapse(self, criteria: Dict[str, Any]) -> Tuple[Candidate, Dict[str, Any]]:
        """
        Apply criteria K to select x* from frozen QS.
        
        Args:
            criteria: Decision criteria including objective function and constraints
            
        Returns:
            Tuple of (selected_candidate, collapse_record)
            
        Raises:
            ValueError: If QS is not frozen before collapse
        """
        if not self.frozen:
            raise ValueError("QS must be frozen before collapse")
        
        # Evaluate J_K(x) for each candidate
        scores_K = [self._evaluate_criteria(c, criteria) for c in self.candidates]
        
        # Select best candidate (minimize objective)
        idx_star = min(range(len(scores_K)), key=lambda i: scores_K[i])
        x_star = self.candidates[idx_star]
        
        # Record collapse event
        collapse_record = {
            "collapse_event": {
                "criteria": criteria,
                "objective_function": criteria.get("objective_function", "J_K(x)"),
                "constraints": criteria.get("constraints", []),
                "selected_candidate": x_star.id,
                "merkle_root_pre_collapse": self.merkle_root,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "decision_authority": criteria.get("decision_authority", "Unknown"),
                "qs_version": self.version,
                "cb_anchor": self._generate_cb_anchor(),
            },
            "post_collapse_state": {
                "x_star": x_star.to_dict(),
                "predicted_score": self.scores[idx_star] if idx_star < len(self.scores) else None,
                "predicted_bounds": x_star.bounds,
                "actual_performance": None,  # Filled after QB execution
                "delta": None,  # QS→CB validation after reality
            },
            "selection_scores": {
                "all_scores_K": scores_K,
                "selected_score_K": scores_K[idx_star],
                "original_scores": self.scores,
            }
        }
        
        # Compute collapse hash
        collapse_data = f"{self.merkle_root}|{json.dumps(criteria, sort_keys=True)}|{x_star.id}|{collapse_record['collapse_event']['timestamp']}"
        collapse_record["collapse_hash"] = hashlib.sha256(collapse_data.encode()).hexdigest()
        
        return x_star, collapse_record
    
    def _evaluate_criteria(self, candidate: Candidate, criteria: Dict[str, Any]) -> float:
        """
        Compute J_K(x) for given candidate under criteria K.
        
        Args:
            candidate: Candidate to evaluate
            criteria: Decision criteria
            
        Returns:
            Objective value (to be minimized)
        """
        # Extract evaluation method from criteria
        eval_method = criteria.get("evaluation_method", "weighted_sum")
        
        if eval_method == "weighted_sum":
            # Weighted sum of score vector components
            weights = criteria.get("weights", {})
            score = 0.0
            for key, value in candidate.score_vector.items():
                weight = weights.get(key, 1.0)
                score += weight * value
            
            # Add penalty for constraint violations
            penalty_weight = criteria.get("penalty_weight", 1000.0)
            for constraint_name, satisfied in candidate.constraints_satisfied.items():
                if not satisfied:
                    score += penalty_weight
            
            return score
        
        elif eval_method == "custom":
            # Use custom objective function provided in criteria
            objective_fn = criteria.get("objective_function_callable")
            if objective_fn and callable(objective_fn):
                return objective_fn(candidate)
            else:
                raise ValueError("Custom evaluation method requires objective_function_callable")
        
        else:
            raise ValueError(f"Unknown evaluation method: {eval_method}")
    
    def _generate_cb_anchor(self) -> str:
        """Generate Classical Bit anchor identifier."""
        timestamp = datetime.utcnow().strftime("%Y-%m-%d")
        return f"CB-{timestamp}-COLLAPSE-{self.version}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "version": self.version,
            "candidates": [c.to_dict() for c in self.candidates],
            "scores": self.scores,
            "bounds": self.bounds,
            "priors": self.priors,
            "constraints": self.constraints,
            "merkle_root": self.merkle_root,
            "timestamp": self.timestamp,
            "frozen": self.frozen,
            "metadata": self.metadata,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QSField':
        """Create QSField from dictionary."""
        candidates = [Candidate.from_dict(c) for c in data.pop("candidates", [])]
        return cls(candidates=candidates, **data)
    
    def validate_integrity(self) -> bool:
        """
        Validate Merkle root matches current candidates.
        
        Returns:
            True if integrity check passes, False otherwise
        """
        if not self.frozen:
            return True  # Unfrozen fields don't have integrity constraints
        
        hashes = [c.hash for c in self.candidates]
        computed_root = compute_merkle_root(hashes)
        return computed_root == self.merkle_root
    
    def get_pareto_frontier(self, objectives: List[str]) -> List[Candidate]:
        """
        Get Pareto-optimal candidates for specified objectives.
        
        Args:
            objectives: List of objective names from score_vector to consider
            
        Returns:
            List of non-dominated candidates
        """
        pareto_set = []
        
        for candidate in self.candidates:
            is_dominated = False
            for other in self.candidates:
                if candidate.id == other.id:
                    continue
                
                # Check if 'other' dominates 'candidate'
                dominates = True
                strictly_better_in_one = False
                
                for obj in objectives:
                    cand_score = candidate.score_vector.get(obj, float('inf'))
                    other_score = other.score_vector.get(obj, float('inf'))
                    
                    # Assuming minimization (lower is better)
                    if other_score > cand_score:
                        dominates = False
                        break
                    if other_score < cand_score:
                        strictly_better_in_one = True
                
                if dominates and strictly_better_in_one:
                    is_dominated = True
                    break
            
            if not is_dominated:
                pareto_set.append(candidate)
        
        return pareto_set
    
    def get_candidate_by_id(self, candidate_id: str) -> Optional[Candidate]:
        """Get candidate by ID."""
        for candidate in self.candidates:
            if candidate.id == candidate_id:
                return candidate
        return None
    
    def compute_coverage_metrics(self) -> Dict[str, float]:
        """
        Compute coverage metrics for the QS field.
        
        Returns:
            Dictionary with coverage statistics
        """
        if not self.candidates:
            return {
                "total_candidates": 0,
                "feasible_candidates": 0,
                "coverage_ratio": 0.0,
                "constraint_satisfaction_rate": 0.0,
            }
        
        feasible_count = sum(
            1 for c in self.candidates 
            if all(c.constraints_satisfied.values())
        )
        
        total_constraints = sum(
            len(c.constraints_satisfied) for c in self.candidates
        )
        satisfied_constraints = sum(
            sum(c.constraints_satisfied.values()) for c in self.candidates
        )
        
        return {
            "total_candidates": len(self.candidates),
            "feasible_candidates": feasible_count,
            "coverage_ratio": feasible_count / len(self.candidates),
            "constraint_satisfaction_rate": (
                satisfied_constraints / total_constraints 
                if total_constraints > 0 else 0.0
            ),
        }
