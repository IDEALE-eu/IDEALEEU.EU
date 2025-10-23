# FEA — Finite Element Analysis

## Purpose

This directory contains Finite Element Analysis (FEA) cases including:
- Static stress analyses
- Transient thermal simulations
- Modal and vibration analyses
- Fatigue assessments
- Material property definitions

## Directory Structure

```
FEA/
├─ README.md                    # This file
├─ cases/                       # Individual FEA cases
│  ├─ static_stress/            # Example: static stress analysis
│  │  ├─ model/                 # Full-resolution production model
│  │  ├─ mesh/                  # Mesh files and scripts
│  │  ├─ smoke/                 # Coarse CI smoke test
│  │  └─ baseline/metrics.json  # Reference metrics
│  └─ transient_thermal/        # Example: transient thermal analysis
├─ materials/                   # Material property databases
└─ baseline/                    # Canonical baselines and convergence studies
```

## Case Organization

Each case should have:
- **model/**: Full-resolution production model
- **mesh/**: Mesh files, refinement zones, and generation scripts
- **smoke/**: Fast, coarse version for CI (< 5 min runtime)
- **baseline/metrics.json**: Reference results with required metrics

## Material Library

Store material properties in materials/:
- Mechanical properties (E, ν, ρ)
- Thermal properties (k, cp, α)
- Strength data (σy, σu, fatigue curves)
- Temperature-dependent data

Format: JSON, CSV, or solver-native formats

## Solver Configurations

### Abaqus
- .inp: Input file with model definition
- .odb: Output database (use LFS)
- .dat: Data file with results

### ANSYS Mechanical
- .db: Database files (use LFS)
- .inp: MAPDL input files
- .rst: Result files

### Nastran
- .bdf: Bulk data file
- .op2: Binary output (use LFS)

## Required Metrics

Every baseline/metrics.json must include:
```json
{
  "mass": 0.0,
  "energy_kwh": 0.0,
  "peak_temp_C": 0.0,
  "mass_flow_kg_s": 0.0,
  "runtime_s": 0.0,
  "max_stress_MPa": 0.0,
  "max_displacement_mm": 0.0
}
```

## Element Types

Document element choices:
- Linear vs. quadratic elements
- Shell, solid, or beam elements
- Integration schemes
- Element formulations

## Mesh Convergence

Perform mesh convergence studies:
1. Run same case with progressively finer meshes
2. Plot key metrics vs. element count
3. Document converged solution
4. Store results in baseline/

## Best Practices

1. **Units**: Always specify consistent unit system
2. **Boundary Conditions**: Document all BCs and assumptions
3. **Loads**: Describe load application and distribution
4. **Contact**: Document contact definitions and algorithms
5. **Validation**: Compare to analytical solutions when possible

## Running Cases

```bash
# Abaqus example
cd cases/static_stress/model
abaqus job=analysis input=model.inp

# Post-process
python3 ../../../SCRIPTS/export_metrics.py --case .
```

## Quality Checks

Before committing results:
- [ ] Mesh quality metrics acceptable
- [ ] Boundary conditions properly applied
- [ ] Results physically reasonable
- [ ] Convergence achieved
- [ ] Baseline metrics documented

## References

- Abaqus Documentation
- ANSYS Mechanical User Guide
- Best Practices: See DOCS/FEA_README.md

---

**Last Updated:** 2025-10-23
