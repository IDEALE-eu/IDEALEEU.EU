# Optimized Reference Designs - Export Location

## Purpose
Store STEP files of selected optimized designs from Pareto front for detailed review and analysis.

## Naming Convention
```
Q100_CB_OPT_[DESIGN_ID]_[CHARACTERISTIC].stp

Examples:
- Q100_CB_OPT_001_MIN_MASS.stp
- Q100_CB_OPT_002_MIN_DEFLECTION.stp
- Q100_CB_OPT_003_BALANCED.stp
- Q100_CB_OPT_004_INTERMEDIATE_A.stp
- Q100_CB_OPT_005_INTERMEDIATE_B.stp
```

## Selection Strategy

From the Pareto front, select **5 reference designs** that span the trade-off space:

1. **MIN_MASS** - Minimum structural mass design
   - Lightest feasible solution
   - May have higher deflection
   - Optimized for fuel efficiency

2. **MIN_DEFLECTION** - Maximum stiffness design
   - Lowest deflection under loads
   - May have higher mass
   - Optimized for structural stiffness

3. **BALANCED** - Balanced compromise
   - Middle of Pareto curve
   - Good balance of mass and stiffness
   - Often practical choice

4. **INTERMEDIATE_A** - Between MIN_MASS and BALANCED
   - Explores lower-mass region
   - Alternative mass-focused design

5. **INTERMEDIATE_B** - Between BALANCED and MIN_DEFLECTION
   - Explores higher-stiffness region
   - Alternative stiffness-focused design

## Export Process

### Automated Export
The driver script (`SCRIPTS/DRIVERS/driver.py`) will automatically:
1. Identify 5 designs from Pareto front
2. Regenerate CAD for each design
3. Export to STEP format
4. Store in this directory

### Manual Export
If needed, manually export selected designs:
```python
from export_design import export_design_to_step

# Load Pareto front
pareto = load_pareto_front('RESULTS/PARETO/q100_cb_pareto.csv')

# Select designs
designs = select_reference_designs(pareto, n=5)

# Export each
for i, design in enumerate(designs):
    filename = f"Q100_CB_OPT_{i+1:03d}_{design.characteristic}.stp"
    export_design_to_step(design, filename)
```

## Design Documentation

Each exported STEP file should be accompanied by:
- Design parameters (CSV or JSON)
- Performance metrics (mass, deflection, constraints)
- Pareto rank and crowding distance
- Export date and study ID

Example: `Q100_CB_OPT_001_MIN_MASS_metadata.json`
```json
{
  "design_id": "Q100_CB_OPT_001",
  "characteristic": "MIN_MASS",
  "study": "study_001",
  "pareto_rank": 1,
  "objectives": {
    "mass": 3050.0,
    "deflection": 18.2
  },
  "constraints": {
    "max_stress": 215.0,
    "buckling_rf": 1.15,
    "deflection_ratio": 0.95
  },
  "parameters": {
    "cb_length": 7800.0,
    "cb_width": 11500.0,
    "skin_thickness": 2.2,
    "..."
  },
  "exported": "2025-10-09T15:30:00Z"
}
```

## Quality Checks

Before accepting exported designs:
1. **Geometry validation** - No self-intersections or invalid topology
2. **Constraint satisfaction** - All constraints met (g ≤ 0)
3. **STEP file integrity** - Opens in target CAD system
4. **Traceability** - Linked to optimization run and Pareto front

## Next Steps

After export:
1. **Review in CAD** - Visual inspection, dimensional checks
2. **Detailed FEA** - Refined mesh, additional load cases
3. **Manufacturing review** - Assess producibility
4. **Cost estimation** - Detailed cost analysis
5. **Down-selection** - Choose final design for development

## File Management

- Keep STEP files under version control (Git LFS recommended)
- Maintain metadata alongside each STEP file
- Archive superseded designs in `ARCHIVE/` subdirectory
- Document rationale for final design selection

---

**Status**: Ready for exports  
**Updated**: 2025-10-09
