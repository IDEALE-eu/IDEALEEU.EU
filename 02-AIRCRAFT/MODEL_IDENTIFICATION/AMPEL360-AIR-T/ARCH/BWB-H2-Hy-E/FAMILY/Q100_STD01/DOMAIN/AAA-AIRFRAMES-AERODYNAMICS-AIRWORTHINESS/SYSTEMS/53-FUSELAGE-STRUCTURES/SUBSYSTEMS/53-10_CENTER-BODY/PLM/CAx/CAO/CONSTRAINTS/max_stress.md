# Maximum Stress Constraint

## Constraint ID
`max_stress`

## Type
Inequality (≤)

## Description
Von Mises stress must remain below material yield strength divided by safety factor across all elements and load cases.

## Limit
```
σ_VM ≤ σ_yield / 1.5
```

For AL 2024-T3: σ_VM ≤ 345 / 1.5 = 230 MPa

## Evaluation Method
CAE-based stress analysis from FEA

## Load Cases Evaluated
- LC1: Cabin pressurization (0.062 MPa)
- LC2: Symmetric pull-up (2.5g)
- LC3: Combined pressure + maneuver (0.062 MPa + 2.0g)

## Constraint Function
```python
def evaluate(design):
    stress_max = get_max_von_mises_stress(design)
    material_yield = get_material_yield(design.material)
    constraint_value = stress_max - (material_yield / 1.5)
    return constraint_value  # ≤ 0 is feasible
```

## Implementation
- Run static FEA for all load cases
- Extract Von Mises stress for all elements
- Find maximum stress across all cases
- Compare against allowable
- Return constraint violation (positive = violation)

## Penalty Function
For generative phase, use quadratic penalty:
```
penalty = max(0, constraint_value)² × 1000
```

## Traceability
- **Requirement**: REQ-53-10-001 - Structural integrity
- **Standard**: CS-25.305 - Strength and deformation
- **Test**: TEST-53-10-001 - Ultimate load test

## Notes
- Safety factor 1.5 on yield accounts for:
  - Static strength requirement
  - Material variability
  - Analysis uncertainty
- Does not address fatigue (separate analysis)
- Critical regions: window/door cutouts, pressure bulkhead

---
**Created**: 2025-10-09
**Status**: Active
