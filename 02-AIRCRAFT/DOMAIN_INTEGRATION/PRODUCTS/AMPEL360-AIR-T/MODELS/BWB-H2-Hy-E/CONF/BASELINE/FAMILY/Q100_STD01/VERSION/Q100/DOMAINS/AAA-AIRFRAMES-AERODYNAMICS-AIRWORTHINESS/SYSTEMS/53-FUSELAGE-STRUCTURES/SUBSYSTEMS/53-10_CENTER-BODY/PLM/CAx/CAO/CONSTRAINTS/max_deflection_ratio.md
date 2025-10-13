# Maximum Deflection Ratio Constraint

## Constraint ID
`max_deflection_ratio`

## Type
Inequality (≤)

## Description
Maximum structural deflection must not exceed span/500 to ensure structural stiffness and maintain clearances.

## Limit
```
δ_max ≤ L / 500
```

For typical center body length ~8000 mm: δ_max ≤ 16 mm

## Evaluation Method
CAE-based displacement analysis from FEA (same as deflection objective)

## Load Cases Evaluated
- LC1: Cabin pressurization
- LC2: Symmetric pull-up
- LC3: Combined loading

## Constraint Function
```python
def evaluate(design):
    deflection_max = get_max_deflection(design)
    cb_length = design.parameters['cb_length']
    limit = cb_length / 500.0
    constraint_value = deflection_max - limit
    return constraint_value  # ≤ 0 is feasible
```

## Implementation
- Use results from deflection objective calculation
- No additional CAE runs required
- Compare against geometric limit
- Return constraint violation

## Rationale
The L/500 criterion ensures:
1. **Structural stiffness** - Prevents excessive flexibility
2. **Door/window operation** - Maintains alignment
3. **System clearances** - Avoids interference with systems
4. **Passenger comfort** - Floor deflection acceptable

## Penalty Function
```
penalty = max(0, constraint_value)² × 1500
```

## Traceability
- **Requirement**: REQ-53-10-005 - Structural stiffness
- **Standard**: Industry practice (L/500 for fuselage structures)
- **Test**: TEST-53-10-005 - Deflection verification

## Notes
- More restrictive than pure strength requirements
- May drive design in low-mass regions
- Can be relaxed in local zones if justified
- Floor beam deflection often most critical

---
**Created**: 2025-10-09
**Status**: Active
