# Getting Started with QS Framework

Quick start guide for using the Quantum Superposition Framework v2.0.

## Installation

The QS Framework is a standalone Python package located at:
```
00-PROGRAM/QS_FRAMEWORK/
```

Add to your Python path:
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/00-PROGRAM/QS_FRAMEWORK/src"
```

Or import directly in your code:
```python
import sys
sys.path.insert(0, '/path/to/00-PROGRAM/QS_FRAMEWORK/src')
```

## 5-Minute Quick Start

### 1. Import the API

```python
from qs_api import QSAPI

api = QSAPI()
```

### 2. Define Your Problem

```python
# Design space
design_space = {
    "variables": ["wingspan", "chord", "thickness"],
    "ranges": {"wingspan": (10, 20), "chord": (1, 3)},
    "num_candidates": 30,
}

# Evidence data
evidence = {
    "simulations": {"cfd_results": [...]},
    "tests": {"wind_tunnel_data": [...]},
}

# Constraints
constraints = {
    "C_0": {"max_weight": 1500, "min_performance": 0.8},
    "phi_0": {"prefer_low_cost": True},
}
```

### 3. Create QS Field

```python
qs_field = api.create(design_space, evidence, constraints)
print(f"Generated {len(qs_field.candidates)} candidates")
```

### 4. Freeze and Collapse

```python
# Freeze field
merkle_root = api.freeze(qs_field)

# Define decision criteria
criteria = {
    "evaluation_method": "weighted_sum",
    "weights": {"performance": 0.5, "cost": 0.3, "risk": 0.2},
}

# Select optimal candidate
x_star, collapse_record = api.collapse(qs_field, criteria)
print(f"Selected: {x_star.id}")
```

### 5. Validate Predictions

```python
# After implementation
actual_performance = {
    "weight_kg": 1285.0,
    "cost_usd": 485000.0,
}

validation = api.validate(qs_field, x_star, actual_performance)
print(f"Accuracy: {validation['metrics']['prediction_accuracy']:.1f}%")
```

## Common Use Cases

### Aerospace Design Trade Study

See `examples/aircraft_wing.py` for a complete aircraft wing design example with:
- Multi-objective optimization
- Pareto frontier analysis
- Realistic aerospace constraints
- Multiple decision scenarios

### Pareto Frontier Analysis

```python
# Extract non-dominated candidates
pareto_candidates = qs_field.get_pareto_frontier([
    "performance",
    "cost",
    "risk"
])

print(f"Found {len(pareto_candidates)} Pareto optimal candidates")
```

### Coverage Analysis

```python
metrics = qs_field.compute_coverage_metrics()
print(f"Coverage ratio: {metrics['coverage_ratio']:.1%}")
print(f"Feasible: {metrics['feasible_candidates']} / {metrics['total_candidates']}")
```

### Field Versioning

```python
# Create initial field
qs_v1 = api.create(design_space, evidence_v1, constraints)

# Update with new evidence
new_evidence = {"new_tests": {...}}
qs_v2 = api.update_evidence(qs_v1, new_evidence)
```

### Custom Candidate Generation

```python
def my_generator(design_space, evidence, constraints):
    candidates = []
    # Your custom logic here
    # - Use optimization algorithms
    # - Interface with CAD/CAE tools
    # - Load from databases
    return candidates

qs_field = api.create(
    design_space,
    evidence,
    constraints,
    candidate_generator=my_generator
)
```

## Key Concepts

### TFA Flow: QS → FWD → UE → FE → CB → QB

1. **QS (Quantum Superposition)**: Generate candidate field
2. **FWD (Future/Waves Dynamics)**: Distribute to stakeholders
3. **UE (Unit Element)**: Apply physics validation
4. **FE (Federation Entanglement)**: Enforce governance
5. **CB (Classical Bit)**: Collapse to select optimal
6. **QB (Qubit)**: Execute and validate predictions

### Immutability

- Once frozen, QS field cannot be modified
- Merkle tree provides cryptographic proof
- All changes create new versioned field
- Complete audit trail maintained

### Decision Criteria

Criteria are separate from candidate generation:
- Prevents bias in prediction
- Allows criteria to change without regenerating candidates
- Supports "what-if" analysis with same QS field

## Next Steps

1. **Run Examples**
   ```bash
   cd examples
   python basic_usage.py
   python aircraft_wing.py
   ```

2. **Read Documentation**
   - `docs/QS_SPEC.md` - Complete technical specification
   - `docs/API_REFERENCE.md` - Detailed API documentation

3. **Run Tests**
   ```bash
   cd tests
   python -m unittest discover
   ```

4. **Integrate with Your Workflow**
   - Adapt design_space to your problem
   - Connect to your CAD/CAE tools
   - Define domain-specific constraints
   - Customize candidate generation

## Troubleshooting

### Import Errors

Ensure src directory is in Python path:
```python
import sys
sys.path.insert(0, '/path/to/QS_FRAMEWORK/src')
```

### ValueError: QS must be frozen before collapse

Always freeze before collapse:
```python
api.freeze(qs_field)  # Must call this first
api.collapse(qs_field, criteria)  # Then collapse
```

### ValueError: QS is already frozen

Cannot freeze twice. Create new version instead:
```python
qs_v2 = api.update_evidence(qs_v1, new_evidence)
api.freeze(qs_v2)
```

## Support

- **Documentation**: `docs/` directory
- **Examples**: `examples/` directory
- **Tests**: `tests/` directory
- **Issues**: Open issue on GitHub repository

## Related Components

- **UTCS**: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`
- **CAO Framework**: `02-AIRCRAFT/.../PLM/CAx/CAO/`
- **Governance**: `00-PROGRAM/GOVERNANCE/`

---

**Version**: 2.0.0  
**Status**: Production Ready  
**Last Updated**: 2025-10-15
