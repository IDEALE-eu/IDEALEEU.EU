# Pareto Front Results - Q100 Center Body

## Purpose
Store Pareto-optimal solutions from multi-objective optimization studies.

## Contents
This directory will contain:

### Primary Results
- `q100_cb_pareto.csv` - Pareto front from study_001
  - Columns: design variables, objectives, constraints
  - Each row is a non-dominated solution
  
### Analysis Files
- `pareto_comparison_*.csv` - Comparison across multiple studies
- `selected_designs.csv` - Subset of designs selected for detailed analysis

## Pareto Front Format

```csv
# Design Variables (18)
cb_length,cb_width,cb_height,skin_thickness,frame_spacing,frame_web_thickness,
frame_cap_area,stringer_spacing,stringer_area,bulkhead_thickness,
cabin_pressure,design_load_factor,floor_beam_height,floor_beam_web_thickness,
keel_beam_height,keel_beam_thickness,window_frame_reinforcement,
door_cutout_reinforcement,
# Objectives (2)
structural_mass,max_deflection,
# Constraints (3)
max_stress_violation,buckling_rf_violation,deflection_ratio_violation
```

## Interpretation

### Trade-off Curve
The Pareto front shows the trade-off between:
- **Mass** (minimize) - Lower is better for fuel efficiency
- **Deflection** (minimize) - Lower indicates higher stiffness

No single "best" design exists - each Pareto point is optimal given different weight preferences.

### Selecting Designs
Consider:
1. **Mass-optimal**: Lightest feasible design (may have higher deflection)
2. **Stiffness-optimal**: Lowest deflection (may have higher mass)
3. **Balanced**: Middle of Pareto front
4. **Margin**: Designs with constraint margins
5. **Manufacturing**: Ease of production

### Next Steps
From Pareto front:
1. Select 5 reference designs spanning the front
2. Export to STEP for detailed review
3. Perform additional detailed analysis
4. Manufacturing assessment
5. Cost analysis
6. Final down-selection

## Validation
All Pareto solutions must:
- Satisfy all constraints (g ≤ 0)
- Be non-dominated (no other solution better in all objectives)
- Be reproducible from configuration + seed

## References
- Problem definition: `PROBLEMS/q100_cb.md`
- Optimization run: `RUNS/study_001/`
- STEP exports: `CAD/EXPORTS/STEP/ASSEMBLIES/TOP_LEVEL/`

---
**Updated**: 2025-10-09  
**Status**: Ready for results
