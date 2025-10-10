# Structural Mass Objective

## Objective ID
`structural_mass`

## Type
Minimize

## Description
Total structural mass of the center body including:
- Skin panels
- Frames
- Stringers
- Floor beams
- Keel beam
- Bulkheads
- Reinforcements (windows, doors)

## Evaluation Method
CAE-based mass calculation from FEA model

## Formula
```
structural_mass = Σ(element_volume × material_density)
```

## Target Value
< 3500 kg (based on Q100 requirements)

## Weight in Multi-Objective
0.6 (primary objective)

## Units
kg

## Implementation
- Extract element volumes from CAE model
- Apply material densities from material database
- Sum total mass
- Return scalar value

## Traceability
- **Requirement**: REQ-53-10-002 - Mass target
- **Test**: TEST-53-10-002 - Mass verification

## Notes
- Excludes secondary structures, fasteners, and non-structural items
- Includes structural margins per CS-25
- Conservative estimate acceptable in early generative phase

---
**Created**: 2025-10-09
**Status**: Active
