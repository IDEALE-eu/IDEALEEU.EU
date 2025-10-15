# QS Framework - Quantum Superposition for Decision Management

[![Status](https://img.shields.io/badge/status-canonical-green.svg)](docs/QS_SPEC.md)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](docs/QS_SPEC.md)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)

Implementation of the Quantum Superposition (QS) technical specification v2.0 for managing pre-optimized configuration candidates before criteria collapse.

## Overview

**QS (Quantum Superposition)** is a framework for managing decision-making under uncertainty in aerospace engineering and other complex domains. It provides:

- **Pre-decision candidate management**: Curate and maintain a field of viable configuration options
- **Cryptographic integrity**: Merkle trees ensure immutability and tamper-evidence
- **Criteria-based collapse**: Apply stakeholder criteria to select optimal solutions
- **Validation and learning**: Compare predictions to actual outcomes for continuous improvement
- **Full traceability**: Integration with UTCS (Universal Traceability and Configuration System)

## Key Concepts

### TFA Flow: QS → FWD → UE → FE → CB → QB

1. **QS (Quantum Superposition)**: Generate candidate field with predictions
2. **FWD (Future/Waves Dynamics)**: Distribute to stakeholders
3. **UE (Unit Element)**: Apply physics and feasibility filters
4. **FE (Federation Entanglement)**: Enforce governance and multi-party policies
5. **CB (Classical Bit)**: Collapse to select optimal candidate
6. **QB (Qubit)**: Execute, measure, and feed back for learning

## Quick Start

### Installation

```bash
# Add to your Python path
export PYTHONPATH="${PYTHONPATH}:/path/to/00-PROGRAM/QS_FRAMEWORK/src"
```

### Basic Usage

```python
from qs_framework import QSAPI

# Initialize API
api = QSAPI()

# Create QS field
qs_field = api.create(
    design_space={"variables": [...], "ranges": {...}},
    evidence={"historical_data": [...], "simulations": [...]},
    constraints={"C_0": {...}, "phi_0": {...}}
)

# Freeze before decision
merkle_root = api.freeze(qs_field)

# Apply criteria and collapse
criteria = {
    "evaluation_method": "weighted_sum",
    "weights": {"performance": 0.5, "cost": 0.3, "risk": 0.2}
}
x_star, collapse_record = api.collapse(qs_field, criteria)

# Validate predictions
validation = api.validate(qs_field, x_star, actual_performance={...})
```

## Structure

```
QS_FRAMEWORK/
├── src/                  # Source code
│   ├── __init__.py      # Package exports
│   ├── qs_field.py      # Candidate and QSField classes
│   ├── qs_api.py        # QSAPI lifecycle management
│   └── merkle.py        # Merkle tree integrity
├── tests/               # Unit tests
│   ├── test_qs_field.py
│   ├── test_qs_api.py
│   └── test_merkle.py
├── examples/            # Usage examples
│   ├── basic_usage.py
│   └── aircraft_wing.py
├── docs/                # Documentation
│   └── QS_SPEC.md      # Technical specification
└── README.md           # This file
```

## Features

### Core Capabilities

- **Candidate Management**: Create, version, and track configuration candidates
- **Merkle Tree Integrity**: Cryptographic proof of field completeness
- **Multi-Objective Optimization**: Pareto frontier extraction
- **Uncertainty Quantification**: Confidence intervals and risk metrics
- **Constraint Handling**: Hard constraints (C_0) and soft preferences (phi_0)
- **Criteria Collapse**: Flexible objective functions and decision methods
- **Validation Framework**: Compare predictions to actual outcomes
- **Learning Loop**: Feed validation results back for model improvement

### API Highlights

```python
# QSAPI methods
api.create(design_space, evidence, constraints)
api.update_evidence(qs_field, new_evidence)
api.freeze(qs_field)
api.collapse(qs_field, criteria)
api.validate(qs_field, x_star, actual_performance)

# QSField methods
qs_field.freeze()
qs_field.collapse(criteria)
qs_field.validate_integrity()
qs_field.get_pareto_frontier(objectives)
qs_field.compute_coverage_metrics()
```

## Examples

### Run Basic Example

```bash
cd examples
python basic_usage.py
```

### Run Tests

```bash
cd tests
python -m unittest discover
```

Or run individual test files:

```bash
python test_qs_field.py
python test_merkle.py
```

## Documentation

- **[QS_SPEC.md](docs/QS_SPEC.md)**: Complete technical specification with mathematical formalization
- **[examples/basic_usage.py](examples/basic_usage.py)**: Step-by-step workflow example
- Source code docstrings: Inline API documentation

## Operational Rules

1. **Keep N Large for Coverage**: Generate diverse candidates (target: N ≥ 20 for complex decisions)
2. **Separate Prior Scoring from Criteria**: Don't leak decision criteria into prediction function
3. **Freeze QS at Decision Time**: Compute Merkle root before collapse, never back-edit
4. **Re-Open QS Only on New Evidence**: Version fields (QS_0 → QS_1 → QS_2 → ...)

## Service Level Objectives (SLOs)

| Metric | Target |
|--------|--------|
| Time-to-Collapse | < 10 seconds |
| Regret | < 5% |
| Coverage | > 80% |
| Prediction Accuracy | RMSE < 10% |
| Hash Integrity | 100% |

## Standards Alignment

- **AS9100 Rev D**: Configuration management via immutable QS versions
- **ATA iSpec 2200**: QS field structure maps to data modules
- **S1000D CSDB**: Each candidate can be a data module with provenance
- **ISO 9001**: QS→CB validation = continuous improvement cycle

## Integration

### UTCS Traceability

Each candidate includes UTCS manifest:
- Context, content, cache, structure, style, sheet
- Full provenance chain
- Evidence references

### CAO Framework

Compatible with:
- `02-AIRCRAFT/.../PLM/CAx/CAO/`: Computer-Aided Optimization
- `QUANTUM_OA`: Quantum optimization solvers
- BREX compliance and S1000D anchors

## License

Apache-2.0

## References

- **Specification**: [docs/QS_SPEC.md](docs/QS_SPEC.md)
- **UTCS**: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`
- **Governance**: `00-PROGRAM/GOVERNANCE/`

---

**Status**: ✅ **CANONICAL - DO NOT MODIFY WITHOUT GOVERNANCE APPROVAL**

*QS = Quantum Superposition: A curated option space with proofs. CRITERIA collapse = decision act that selects one realization under audited rules.*
