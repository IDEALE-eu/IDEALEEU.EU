# Maximum Deflection Objective

## Objective ID
`max_deflection`

## Type
Minimize

## Description
Maximum structural deflection under design load cases. Lower deflection indicates higher stiffness.

## Evaluation Method
CAE-based displacement analysis from FEA

## Load Cases Evaluated
- LC1: Cabin pressurization (0.062 MPa)
- LC2: Symmetric pull-up (2.5g)
- LC3: Combined pressure + maneuver (0.062 MPa + 2.0g)

## Formula
```
max_deflection = max(|displacement_vector|) across all nodes and load cases
```

## Target Value
< cb_length / 500 (geometric constraint)

## Weight in Multi-Objective
0.4 (secondary to mass)

## Units
mm

## Implementation
- Run static FEA for all load cases
- Extract displacement magnitudes for all nodes
- Return maximum value across all cases
- Store per-load-case results for analysis

## Traceability
- **Requirement**: REQ-53-10-005 - Structural stiffness
- **Test**: TEST-53-10-005 - Deflection measurement

## Notes
- Critical for passenger comfort (floor deflection)
- Affects door/window alignment
- Trade-off with mass objective
- May need penalty function if exceeds L/500

---
**Created**: 2025-10-09
**Status**: Active
