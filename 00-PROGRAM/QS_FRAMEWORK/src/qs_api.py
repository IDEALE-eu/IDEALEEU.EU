"""
QS API - Lifecycle Management Interface

API for managing Quantum Superposition field lifecycle including:
- QS field creation and generation
- Evidence updates and versioning
- Freezing and collapse operations
- Validation and compliance
"""

from typing import Dict, Any, List, Optional, Tuple, Callable
import random
import math
from datetime import datetime

# Import qs_field module - handle both package and standalone imports
try:
    from .qs_field import Candidate, QSField
except ImportError:
    import qs_field
    Candidate = qs_field.Candidate
    QSField = qs_field.QSField


class QSAPI:
    """
    API for QS field lifecycle management.
    
    Provides high-level interface for:
    - Creating new QS fields from design space and evidence
    - Updating fields with new evidence
    - Freezing fields before decision
    - Collapsing fields to select optimal candidate
    - Validating predictions against actual outcomes
    """
    
    def __init__(self):
        """Initialize QS API."""
        self.version = "2.0.0"
        self._field_history: List[QSField] = []
    
    def create(
        self,
        design_space: Dict[str, Any],
        evidence: Dict[str, Any],
        constraints: Dict[str, Any],
        *,
        version: str = None,
        metadata: Dict[str, Any] = None,
        candidate_generator: Optional[Callable] = None,
    ) -> QSField:
        """
        Generate new QS field.
        
        Args:
            design_space: X (configuration space definition)
            evidence: D (training data for f_pred)
            constraints: C_0 (hard), phi_0 (soft)
            version: QS version identifier (auto-generated if None)
            metadata: Additional metadata for the field
            candidate_generator: Custom generator function for candidates
        
        Returns:
            QSField with N candidates, scores, hashes
            
        Example:
            >>> api = QSAPI()
            >>> design_space = {"variables": [...], "ranges": [...]}
            >>> evidence = {"historical_data": [...], "simulations": [...]}
            >>> constraints = {"C_0": {...}, "phi_0": {...}}
            >>> qs_field = api.create(design_space, evidence, constraints)
        """
        if version is None:
            now = datetime.utcnow()
            quarter = (now.month - 1) // 3 + 1
            timestamp = f"{now.year}_Q{quarter}"
            version = f"QS_{timestamp}_v1"
        
        if metadata is None:
            metadata = {}
        
        # Generate candidates
        if candidate_generator:
            candidates = candidate_generator(design_space, evidence, constraints)
        else:
            candidates = self._default_candidate_generation(
                design_space, evidence, constraints
            )
        
        # Compute aggregate scores
        scores = [
            c.score_vector.get("aggregate", 0.0) 
            for c in candidates
        ]
        
        # Compute global bounds
        bounds = self._compute_global_bounds(candidates)
        
        # Create QS field
        qs_field = QSField(
            version=version,
            candidates=candidates,
            scores=scores,
            bounds=bounds,
            priors={
                "C_0": constraints.get("C_0", {}),
                "phi_0": constraints.get("phi_0", {}),
            },
            constraints=constraints,
            metadata=metadata,
        )
        
        self._field_history.append(qs_field)
        return qs_field
    
    def update_evidence(
        self,
        qs_field: QSField,
        new_evidence: Dict[str, Any],
        *,
        regenerate: bool = True,
    ) -> QSField:
        """
        Create new QS version with updated evidence.
        
        Args:
            qs_field: Existing QS_k
            new_evidence: New test data, simulations, etc.
            regenerate: Whether to regenerate candidates or just re-score
        
        Returns:
            QS_{k+1} with re-scored or regenerated candidates
            
        Example:
            >>> new_evidence = {"wind_tunnel_data": [...]}
            >>> qs_field_v2 = api.update_evidence(qs_field_v1, new_evidence)
        """
        # Parse version and increment
        version_parts = qs_field.version.split("_v")
        if len(version_parts) == 2:
            base_version = version_parts[0]
            current_num = int(version_parts[1])
            new_version = f"{base_version}_v{current_num + 1}"
        else:
            new_version = f"{qs_field.version}_v2"
        
        if regenerate:
            # Regenerate candidates with new evidence
            # For now, copy existing candidates and update scores
            candidates = [
                self._update_candidate_with_evidence(c, new_evidence)
                for c in qs_field.candidates
            ]
        else:
            # Just re-score existing candidates
            candidates = [
                self._rescore_candidate(c, new_evidence)
                for c in qs_field.candidates
            ]
        
        # Create new QS field
        new_qs_field = QSField(
            version=new_version,
            candidates=candidates,
            scores=[c.score_vector.get("aggregate", 0.0) for c in candidates],
            bounds=self._compute_global_bounds(candidates),
            priors=qs_field.priors,
            constraints=qs_field.constraints,
            metadata={
                **qs_field.metadata,
                "parent_version": qs_field.version,
                "evidence_update": new_evidence.get("description", "Updated evidence"),
            },
        )
        
        self._field_history.append(new_qs_field)
        return new_qs_field
    
    def freeze(self, qs_field: QSField) -> str:
        """
        Freeze QS field before decision.
        
        Args:
            qs_field: QS to freeze
        
        Returns:
            Merkle root H
            
        Example:
            >>> merkle_root = api.freeze(qs_field)
            >>> print(f"Frozen with root: {merkle_root}")
        """
        return qs_field.freeze()
    
    def collapse(
        self,
        qs_field: QSField,
        criteria: Dict[str, Any]
    ) -> Tuple[Candidate, Dict[str, Any]]:
        """
        Apply criteria K to select x* from frozen QS.
        
        Args:
            qs_field: Frozen QS field
            criteria: K (decision criteria and constraints)
        
        Returns:
            Tuple of (x_star, collapse_record)
            
        Example:
            >>> criteria = {
            ...     "evaluation_method": "weighted_sum",
            ...     "weights": {"performance": 0.5, "cost": 0.3, "risk": 0.2},
            ...     "decision_authority": "CCB_Chair_John_Doe",
            ... }
            >>> x_star, collapse_record = api.collapse(qs_field, criteria)
        """
        return qs_field.collapse(criteria)
    
    def validate(
        self,
        qs_field: QSField,
        x_star: Candidate,
        actual_performance: Dict[str, float]
    ) -> Dict[str, Any]:
        """
        Compare QS predictions to actual CB outcomes.
        
        Args:
            qs_field: Original QS field that produced x_star
            x_star: Selected candidate
            actual_performance: Measured outcomes after implementation
        
        Returns:
            Validation report with deltas and metrics
            
        Example:
            >>> actual = {
            ...     "weight_kg": 1285.0,
            ...     "cost_usd": 485000.0,
            ...     "lead_time_days": 195,
            ... }
            >>> validation = api.validate(qs_field, x_star, actual)
        """
        # Find the candidate in the field
        candidate_idx = None
        for idx, c in enumerate(qs_field.candidates):
            if c.id == x_star.id:
                candidate_idx = idx
                break
        
        if candidate_idx is None:
            raise ValueError(f"Candidate {x_star.id} not found in QS field")
        
        # Compute deltas
        deltas = {}
        for metric, actual_value in actual_performance.items():
            predicted_value = x_star.score_vector.get(metric)
            if predicted_value is not None:
                delta = actual_value - predicted_value
                delta_pct = (delta / predicted_value * 100) if predicted_value != 0 else 0.0
                deltas[metric] = {
                    "predicted": predicted_value,
                    "actual": actual_value,
                    "delta": delta,
                    "delta_pct": delta_pct,
                }
        
        # Check if actual values are within predicted bounds
        bounds_violations = {}
        for metric, actual_value in actual_performance.items():
            if metric in x_star.bounds:
                lower, upper = x_star.bounds[metric]
                if not (lower <= actual_value <= upper):
                    bounds_violations[metric] = {
                        "actual": actual_value,
                        "bounds": [lower, upper],
                        "violation": "below" if actual_value < lower else "above",
                    }
        
        # Compute RMSE across all metrics
        squared_errors = []
        for metric, delta_info in deltas.items():
            if "delta_pct" in delta_info:
                squared_errors.append(delta_info["delta_pct"] ** 2)
        
        rmse = math.sqrt(sum(squared_errors) / len(squared_errors)) if squared_errors else 0.0
        
        # Generate validation report
        validation_report = {
            "qs_version": qs_field.version,
            "candidate_id": x_star.id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "deltas": deltas,
            "bounds_violations": bounds_violations,
            "metrics": {
                "rmse_pct": rmse,
                "within_bounds": len(bounds_violations) == 0,
                "prediction_accuracy": 100.0 - rmse if rmse < 100 else 0.0,
            },
            "recommendation": self._generate_recommendation(rmse, bounds_violations),
        }
        
        return validation_report
    
    def _default_candidate_generation(
        self,
        design_space: Dict[str, Any],
        evidence: Dict[str, Any],
        constraints: Dict[str, Any],
    ) -> List[Candidate]:
        """
        Default candidate generation using sampling strategies.
        
        This is a placeholder implementation. In practice, this would use:
        - Genetic algorithms
        - Latin hypercube sampling
        - Multi-start optimization
        - Domain expert proposals
        """
        num_candidates = design_space.get("num_candidates", 20)
        candidates = []
        
        for i in range(num_candidates):
            candidate_id = f"x_{i+1}"
            
            # Generate random configuration (placeholder)
            configuration = {
                "param_1": random.uniform(0, 100),
                "param_2": random.uniform(0, 100),
                "param_3": random.choice(["A", "B", "C"]),
            }
            
            # UTCS manifest
            utcs_manifest = {
                "context": design_space.get("context", "Design trade study"),
                "content": {"config": configuration},
                "cache": {},
                "structure": "TFA/AAA/SI",
                "style": "ISO_10303",
                "sheet": "requirements_matrix.csv",
            }
            
            # Score vector (placeholder - should use f_pred from evidence)
            score_vector = {
                "performance": random.uniform(0.6, 0.95),
                "cost": random.uniform(0.5, 0.9),
                "risk": random.uniform(0.7, 0.98),
                "aggregate": random.uniform(0.6, 0.9),
            }
            
            # Uncertainty
            uncertainty = {
                "sigma_performance": random.uniform(0.02, 0.08),
                "sigma_cost": random.uniform(0.05, 0.15),
                "confidence_interval": [
                    score_vector["aggregate"] - 0.05,
                    score_vector["aggregate"] + 0.05,
                ],
            }
            
            # Bounds
            bounds = {
                "weight_kg": (
                    configuration["param_1"] * 10,
                    configuration["param_1"] * 15,
                ),
                "cost_usd": (
                    configuration["param_2"] * 5000,
                    configuration["param_2"] * 6000,
                ),
                "lead_time_days": (150, 250),
            }
            
            # Constraints
            constraints_satisfied = {
                "C0_safety": True,
                "C0_airworthiness": random.choice([True, True, True, False]),
                "phi0_manufacturability": score_vector["cost"] > 0.6,
            }
            
            # Provenance
            provenance = {
                "generated_by": "QSAPI_v2.0",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "parent_design": "baseline_v1.0",
                "evidence_refs": list(evidence.keys()),
            }
            
            candidate = Candidate(
                id=candidate_id,
                configuration=configuration,
                utcs_manifest=utcs_manifest,
                score_vector=score_vector,
                uncertainty=uncertainty,
                bounds=bounds,
                constraints_satisfied=constraints_satisfied,
                provenance=provenance,
            )
            
            candidates.append(candidate)
        
        return candidates
    
    def _compute_global_bounds(
        self,
        candidates: List[Candidate]
    ) -> Dict[str, List[Tuple[float, float]]]:
        """Compute global bounds across all candidates."""
        if not candidates:
            return {}
        
        # Collect all bound keys
        bound_keys = set()
        for c in candidates:
            bound_keys.update(c.bounds.keys())
        
        # Compute min/max across candidates
        global_bounds = {}
        for key in bound_keys:
            all_bounds = [c.bounds[key] for c in candidates if key in c.bounds]
            if all_bounds:
                global_bounds[key] = [
                    (min(b[0] for b in all_bounds), max(b[1] for b in all_bounds))
                ]
        
        return global_bounds
    
    def _update_candidate_with_evidence(
        self,
        candidate: Candidate,
        new_evidence: Dict[str, Any]
    ) -> Candidate:
        """Update candidate with new evidence."""
        # Create a new candidate with updated scores
        # This is a placeholder - should use actual prediction model
        updated_score_vector = {
            **candidate.score_vector,
            "aggregate": candidate.score_vector["aggregate"] * random.uniform(0.95, 1.05),
        }
        
        return Candidate(
            id=candidate.id,
            configuration=candidate.configuration,
            utcs_manifest={
                **candidate.utcs_manifest,
                "evidence_update": new_evidence.get("description", "Updated"),
            },
            score_vector=updated_score_vector,
            uncertainty=candidate.uncertainty,
            bounds=candidate.bounds,
            constraints_satisfied=candidate.constraints_satisfied,
            provenance={
                **candidate.provenance,
                "updated_timestamp": datetime.utcnow().isoformat() + "Z",
                "evidence_refs": [
                    *candidate.provenance.get("evidence_refs", []),
                    *list(new_evidence.keys()),
                ],
            },
        )
    
    def _rescore_candidate(
        self,
        candidate: Candidate,
        new_evidence: Dict[str, Any]
    ) -> Candidate:
        """Re-score candidate with new evidence without changing configuration."""
        return self._update_candidate_with_evidence(candidate, new_evidence)
    
    def _generate_recommendation(
        self,
        rmse: float,
        bounds_violations: Dict[str, Any]
    ) -> str:
        """Generate recommendation based on validation results."""
        if rmse < 5.0 and not bounds_violations:
            return "Excellent prediction accuracy. Model is performing well."
        elif rmse < 10.0 and not bounds_violations:
            return "Good prediction accuracy. Minor improvements possible."
        elif rmse < 15.0 or (bounds_violations and len(bounds_violations) <= 2):
            return "Moderate prediction accuracy. Consider model refinement."
        else:
            return "Poor prediction accuracy. Model requires significant refinement or retraining."
    
    def get_field_history(self) -> List[QSField]:
        """Get history of all QS fields created in this session."""
        return self._field_history.copy()
    
    def export_field(self, qs_field: QSField, filepath: str):
        """Export QS field to JSON file."""
        import json
        with open(filepath, 'w') as f:
            json.dump(qs_field.to_dict(), f, indent=2)
    
    def import_field(self, filepath: str) -> QSField:
        """Import QS field from JSON file."""
        import json
        with open(filepath, 'r') as f:
            data = json.load(f)
        return QSField.from_dict(data)
