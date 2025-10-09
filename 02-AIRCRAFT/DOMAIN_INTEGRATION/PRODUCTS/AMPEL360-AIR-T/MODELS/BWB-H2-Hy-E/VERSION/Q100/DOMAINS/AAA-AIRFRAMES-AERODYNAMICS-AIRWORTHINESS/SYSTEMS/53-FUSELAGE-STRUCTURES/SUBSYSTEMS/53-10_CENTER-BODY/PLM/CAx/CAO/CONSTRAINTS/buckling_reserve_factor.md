# Buckling Reserve Factor Constraint

## Constraint ID
`buckling_reserve_factor`

## Type
Inequality (≥)

## Description
Linear buckling reserve factor must be greater than 1.1 for all critical panels and load cases.

## Limit
```
RF_buckling ≥ 1.1
```

Where RF = P_critical / P_applied

## Evaluation Method
Linear buckling eigenvalue analysis (CAE)

## Load Cases Evaluated
- LC1: Cabin pressurization (compression in frames)
- LC2: Symmetric pull-up (skin compression zones)
- LC3: Combined loading (critical combined state)

## Constraint Function
```python
def evaluate(design):
    eigenvalues = run_buckling_analysis(design)
    min_rf = min(eigenvalues)  # First (lowest) eigenvalue
    constraint_value = 1.1 - min_rf
    return constraint_value  # ≤ 0 is feasible
```

## Implementation
- Run linear buckling analysis (eigenvalue extraction)
- Extract first 5 eigenvalues (modes)
- Minimum eigenvalue is critical buckling load factor
- Compare against limit 1.1
- Return constraint violation

## Critical Zones
- Lower skin panels (compression in pull-up)
- Frame webs (shear buckling)
- Pressure bulkhead (out-of-plane pressure)
- Door/window cutout edges

## Penalty Function
```
penalty = max(0, constraint_value)² × 2000
```

## Design Guidance
If violated, consider:
- Increase skin thickness
- Reduce frame spacing
- Add local reinforcement
- Increase stiffener areas

## Traceability
- **Requirement**: REQ-53-10-001 - Structural integrity
- **Standard**: CS-25.305(a) - Stability
- **Test**: TEST-53-10-003 - Buckling test

## Notes
- Linear buckling only (conservative)
- Nonlinear post-buckling not considered in generative phase
- Factor 1.1 provides margin for:
  - Geometric imperfections
  - Load distribution uncertainty
  - Analysis linearization

---
**Created**: 2025-10-09
**Status**: Active
