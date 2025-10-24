# CFD — Computational Fluid Dynamics

## Purpose

This directory contains Computational Fluid Dynamics (CFD) analyses including:
- Flow simulations (internal and external)
- Heat transfer analyses
- Multi-phase flows
- Turbulence modeling
- Property data and material definitions

## Directory Structure

```
CFD/
├─ README.md                    # This file
├─ property_tables/             # Precomputed CoolProp/REFPROP tables
├─ cases/                       # Individual CFD cases
│  ├─ tank_solidification/      # Example: tank solidification analysis
│  │  ├─ case/                  # Full-resolution production case
│  │  ├─ smoke/                 # Coarse CI smoke test
│  │  └─ baseline/metrics.json  # Reference metrics
│  ├─ evaporator/               # Example: evaporator analysis
│  └─ expander/                 # Example: expander analysis
├─ meshes/                      # Shared mesh files and scripts
└─ baseline/                    # Canonical baselines and mesh independence studies
```

## Case Organization

Each case should have:
- **case/**: Full-resolution production setup
- **smoke/**: Fast, coarse version for CI (< 5 min runtime)
- **baseline/metrics.json**: Reference results with required metrics

## Mesh Management

### Mesh Files
- Store large meshes in Git LFS
- Document mesh generation scripts in meshes/
- Include mesh independence studies in baseline/

### Mesh Formats
- OpenFOAM: polyMesh directory
- ANSYS: .msh files
- Neutral: .unv, .cgns files

## Property Tables

Store precomputed property tables for:
- Refrigerants (CoolProp data)
- Real gas properties (REFPROP)
- Custom equations of state

Format: CSV or binary lookup tables

## Solver Configurations

### OpenFOAM
- controlDict: Time control and output
- fvSchemes: Numerical schemes
- fvSolution: Linear solvers and algorithms
- turbulenceProperties: Turbulence modeling

### ANSYS Fluent
- .jou files: Journal files for setup
- .cas/.dat: Case and data files

## Required Metrics

Every baseline/metrics.json must include:
```json
{
  "mass": 0.0,
  "energy_kwh": 0.0,
  "peak_temp_C": 0.0,
  "mass_flow_kg_s": 0.0,
  "runtime_s": 0.0
}
```

## Best Practices

1. **Naming**: Use descriptive case names with revision numbers
2. **Documentation**: Document assumptions, boundary conditions, and models
3. **Determinism**: Seed random number generators for reproducibility
4. **Validation**: Compare against experimental data when available
5. **Convergence**: Document convergence criteria and residuals

## Running Cases

```bash
# Run full case
cd cases/tank_solidification/case
./Allrun

# Run smoke test
cd cases/tank_solidification/smoke
./Allrun

# Post-process
python3 ../../../SCRIPTS/cfd_postprocess.py --case .
```

## References

- OpenFOAM User Guide: https://www.openfoam.com/documentation/
- Best Practices: See DOCS/CFD_README.md

---

**Last Updated:** 2025-10-23
