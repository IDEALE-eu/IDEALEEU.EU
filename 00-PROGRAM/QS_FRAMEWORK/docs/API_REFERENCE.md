# QS Framework API Reference

Complete API documentation for the QS Framework v2.0.

## Table of Contents

- [QSAPI Class](#qsapi-class)
- [QSField Class](#qsfield-class)
- [Candidate Class](#candidate-class)
- [Merkle Functions](#merkle-functions)
- [Data Structures](#data-structures)

---

## QSAPI Class

Main interface for QS field lifecycle management.

### Constructor

```python
QSAPI()
```

Creates a new QSAPI instance.

**Attributes:**
- `version` (str): API version ("2.0.0")
- `_field_history` (List[QSField]): History of created fields

### Methods

#### create()

```python
create(
    design_space: Dict[str, Any],
    evidence: Dict[str, Any],
    constraints: Dict[str, Any],
    *,
    version: str = None,
    metadata: Dict[str, Any] = None,
    candidate_generator: Optional[Callable] = None,
) -> QSField
```

Generate new QS field from design space, evidence, and constraints.

**Parameters:**
- `design_space`: Configuration space definition
  - `variables`: List of design variables
  - `ranges`: Min/max bounds for variables
  - `num_candidates`: Number of candidates to generate
- `evidence`: Training data for prediction function
  - Historical data, simulations, test results
- `constraints`: Hard and soft constraints
  - `C_0`: Hard constraints (dict)
  - `phi_0`: Soft preferences (dict)
- `version`: QS version identifier (optional, auto-generated)
- `metadata`: Additional metadata (optional)
- `candidate_generator`: Custom candidate generator function (optional)

**Returns:** QSField object with generated candidates

**Example:**
```python
api = QSAPI()
qs_field = api.create(
    design_space={"variables": [...], "ranges": {...}, "num_candidates": 30},
    evidence={"historical_data": [...], "cfd_results": [...]},
    constraints={"C_0": {"max_weight": 1300}, "phi_0": {"prefer_low_cost": True}}
)
```

#### update_evidence()

```python
update_evidence(
    qs_field: QSField,
    new_evidence: Dict[str, Any],
    *,
    regenerate: bool = True,
) -> QSField
```

Create new QS version with updated evidence.

**Parameters:**
- `qs_field`: Existing QS field (QS_k)
- `new_evidence`: New test data, simulations, etc.
- `regenerate`: Whether to regenerate candidates or just re-score

**Returns:** New QSField (QS_{k+1})

**Example:**
```python
new_evidence = {"wind_tunnel_results": [...]}
qs_field_v2 = api.update_evidence(qs_field_v1, new_evidence)
```

#### freeze()

```python
freeze(qs_field: QSField) -> str
```

Freeze QS field before decision.

**Parameters:**
- `qs_field`: QS field to freeze

**Returns:** Merkle root hash (str)

**Example:**
```python
merkle_root = api.freeze(qs_field)
print(f"Frozen with root: {merkle_root}")
```

#### collapse()

```python
collapse(
    qs_field: QSField,
    criteria: Dict[str, Any]
) -> Tuple[Candidate, Dict[str, Any]]
```

Apply decision criteria to select optimal candidate.

**Parameters:**
- `qs_field`: Frozen QS field
- `criteria`: Decision criteria
  - `evaluation_method`: "weighted_sum" or "custom"
  - `weights`: Weight dict for score components
  - `penalty_weight`: Penalty for constraint violations
  - `decision_authority`: Name of decision maker
  - `objective_function_callable`: Custom function (if method="custom")

**Returns:** Tuple of (selected_candidate, collapse_record)

**Example:**
```python
criteria = {
    "evaluation_method": "weighted_sum",
    "weights": {"performance": 0.5, "cost": 0.3, "risk": 0.2},
    "decision_authority": "CCB Chair",
}
x_star, collapse_record = api.collapse(qs_field, criteria)
```

#### validate()

```python
validate(
    qs_field: QSField,
    x_star: Candidate,
    actual_performance: Dict[str, float]
) -> Dict[str, Any]
```

Compare predictions to actual outcomes.

**Parameters:**
- `qs_field`: Original QS field
- `x_star`: Selected candidate
- `actual_performance`: Measured metrics after implementation

**Returns:** Validation report dict with:
- `deltas`: Predicted vs actual for each metric
- `bounds_violations`: Metrics outside predicted bounds
- `metrics`: RMSE, accuracy, bounds compliance
- `recommendation`: Suggested actions

**Example:**
```python
actual = {"weight_kg": 1285.0, "cost_usd": 485000.0}
validation = api.validate(qs_field, x_star, actual)
print(f"RMSE: {validation['metrics']['rmse_pct']:.2f}%")
```

#### export_field() / import_field()

```python
export_field(qs_field: QSField, filepath: str)
import_field(filepath: str) -> QSField
```

Save/load QS field to/from JSON file.

---

## QSField Class

Represents a Quantum Superposition field with candidates and cryptographic integrity.

### Constructor

```python
QSField(
    version: str,
    candidates: List[Candidate],
    scores: List[float],
    bounds: Dict[str, List[Tuple[float, float]]],
    priors: Dict[str, Any],
    constraints: Dict[str, Any],
    merkle_root: str = "",
    timestamp: str = auto_generated,
    frozen: bool = False,
    metadata: Dict[str, Any] = {}
)
```

### Attributes

- `version` (str): QS field version identifier
- `candidates` (List[Candidate]): All candidate configurations
- `scores` (List[float]): Aggregate scores
- `bounds` (Dict): Global bounds across all candidates
- `priors` (Dict): Prior constraints and preferences
- `constraints` (Dict): Hard constraints
- `merkle_root` (str): Cryptographic integrity hash
- `timestamp` (str): ISO 8601 timestamp
- `frozen` (bool): Immutability flag
- `metadata` (Dict): Additional metadata

### Methods

#### freeze()

```python
freeze() -> str
```

Freeze field and compute Merkle root.

**Returns:** Merkle root hash

**Raises:** ValueError if already frozen

#### collapse()

```python
collapse(criteria: Dict[str, Any]) -> Tuple[Candidate, Dict[str, Any]]
```

Apply criteria to select optimal candidate.

**Returns:** (selected_candidate, collapse_record)

**Raises:** ValueError if not frozen

#### validate_integrity()

```python
validate_integrity() -> bool
```

Verify Merkle root matches current candidates.

**Returns:** True if valid, False if tampered

#### get_pareto_frontier()

```python
get_pareto_frontier(objectives: List[str]) -> List[Candidate]
```

Extract Pareto-optimal candidates.

**Parameters:**
- `objectives`: List of objective names to consider

**Returns:** List of non-dominated candidates

**Example:**
```python
pareto_set = qs_field.get_pareto_frontier(["cost", "performance", "risk"])
```

#### compute_coverage_metrics()

```python
compute_coverage_metrics() -> Dict[str, float]
```

Compute coverage statistics.

**Returns:** Dict with:
- `total_candidates`: Total number
- `feasible_candidates`: Constraint-satisfied count
- `coverage_ratio`: Feasible/total ratio
- `constraint_satisfaction_rate`: Overall satisfaction rate

#### get_candidate_by_id()

```python
get_candidate_by_id(candidate_id: str) -> Optional[Candidate]
```

Retrieve candidate by ID.

#### to_dict() / from_dict()

```python
to_dict() -> Dict[str, Any]
from_dict(data: Dict[str, Any]) -> QSField
```

Serialization and deserialization.

---

## Candidate Class

Represents a single configuration candidate.

### Constructor

```python
Candidate(
    id: str,
    configuration: Dict[str, Any],
    utcs_manifest: Dict[str, Any],
    score_vector: Dict[str, float],
    uncertainty: Dict[str, float],
    bounds: Dict[str, Tuple[float, float]],
    constraints_satisfied: Dict[str, bool],
    provenance: Dict[str, Any],
    hash: str = auto_computed
)
```

### Attributes

- `id` (str): Unique identifier
- `configuration` (Dict): Design parameters
- `utcs_manifest` (Dict): UTCS traceability metadata
  - `context`: Context description
  - `content`: Content references
  - `cache`: Cached computations
  - `structure`: TFA/AAA/SI structure
  - `style`: Style standard (e.g., ISO_10303)
  - `sheet`: Requirements matrix reference
- `score_vector` (Dict[str, float]): Multi-objective scores
  - `performance`, `cost`, `risk`, `aggregate`, etc.
- `uncertainty` (Dict[str, float]): Uncertainty quantification
  - `sigma_*`: Standard deviations
  - `confidence_interval`: [lower, upper]
- `bounds` (Dict[str, Tuple]): Parameter bounds (lower, upper)
- `constraints_satisfied` (Dict[str, bool]): Constraint flags
- `provenance` (Dict): Generation metadata
  - `generated_by`, `timestamp`, `parent_design`, `evidence_refs`
- `hash` (str): SHA-256 hash (auto-computed)

### Methods

#### to_dict() / from_dict()

```python
to_dict() -> Dict[str, Any]
from_dict(data: Dict[str, Any]) -> Candidate
```

Serialization and deserialization.

---

## Merkle Functions

### compute_merkle_root()

```python
compute_merkle_root(hashes: List[str]) -> str
```

Compute Merkle tree root from list of hashes.

**Parameters:**
- `hashes`: List of SHA-256 hex digests

**Returns:** Merkle root hash

**Example:**
```python
hashes = [c.hash for c in candidates]
root = compute_merkle_root(hashes)
```

### verify_merkle_proof()

```python
verify_merkle_proof(leaf_hash: str, proof: List[str], root: str) -> bool
```

Verify Merkle proof for a leaf.

**Parameters:**
- `leaf_hash`: Hash to verify
- `proof`: List of sibling hashes
- `root`: Expected Merkle root

**Returns:** True if proof valid

---

## Data Structures

### Design Space

```python
{
    "description": str,
    "variables": List[str],
    "ranges": Dict[str, Tuple[float, float]],
    "num_candidates": int,
    "context": str
}
```

### Evidence

```python
{
    "source_name": {
        "description": str,
        "data_points": int,
        "reference": str
    },
    ...
}
```

### Constraints

```python
{
    "C_0": {  # Hard constraints
        "constraint_name": value,
        ...
    },
    "phi_0": {  # Soft preferences
        "preference_name": value,
        ...
    }
}
```

### Decision Criteria

```python
{
    "evaluation_method": "weighted_sum" | "custom",
    "weights": {
        "objective_name": float,
        ...
    },
    "penalty_weight": float,
    "decision_authority": str,
    "rationale": str,
    "objective_function_callable": Optional[Callable]
}
```

### Collapse Record

```python
{
    "collapse_event": {
        "criteria": Dict,
        "objective_function": str,
        "constraints": List,
        "selected_candidate": str,
        "merkle_root_pre_collapse": str,
        "timestamp": str,
        "decision_authority": str,
        "qs_version": str,
        "cb_anchor": str
    },
    "post_collapse_state": {
        "x_star": Dict,
        "predicted_score": float,
        "predicted_bounds": Dict,
        "actual_performance": Optional[Dict],
        "delta": Optional[Dict]
    },
    "selection_scores": {
        "all_scores_K": List[float],
        "selected_score_K": float,
        "original_scores": List[float]
    },
    "collapse_hash": str
}
```

### Validation Report

```python
{
    "qs_version": str,
    "candidate_id": str,
    "timestamp": str,
    "deltas": {
        "metric_name": {
            "predicted": float,
            "actual": float,
            "delta": float,
            "delta_pct": float
        },
        ...
    },
    "bounds_violations": {
        "metric_name": {
            "actual": float,
            "bounds": [float, float],
            "violation": "below" | "above"
        },
        ...
    },
    "metrics": {
        "rmse_pct": float,
        "within_bounds": bool,
        "prediction_accuracy": float
    },
    "recommendation": str
}
```

---

## Error Handling

### ValueError

Raised when:
- Trying to freeze an already frozen field
- Trying to collapse an unfrozen field
- Invalid evaluation method in criteria
- Custom evaluation without callable function

### TypeError

Raised when:
- Invalid parameter types
- Missing required parameters

---

## Best Practices

1. **Always freeze before collapse**: Ensures immutability
2. **Use meaningful IDs**: Makes tracking easier
3. **Document criteria rationale**: Helps with audits
4. **Validate predictions**: Feeds learning loop
5. **Version QS fields**: Maintains history
6. **Export important fields**: Backup and archival

---

## Examples

See [examples/basic_usage.py](../examples/basic_usage.py) for complete workflow example.

---

**Version**: 2.0.0  
**Status**: Canonical
