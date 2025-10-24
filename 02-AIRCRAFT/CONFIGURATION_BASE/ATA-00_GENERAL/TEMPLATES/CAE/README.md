# CAE — Computer-Aided Engineering Template

## Purpose

This directory contains the template structure for Computer-Aided Engineering (CAE) artifacts including Computational Fluid Dynamics (CFD), Finite Element Analysis (FEA), and multi-physics coupling simulations.

## Scope

- CFD analyses (OpenFOAM, ANSYS Fluent, etc.)
- FEA analyses (Abaqus, ANSYS Mechanical, etc.)
- Coupled simulations (preCICE, FMU co-simulation)
- Validation and verification data
- Quality assurance and regression testing

## Owners

- **Engineering Lead**: [Name]
- **CAE Lead**: [Name]
- **Approver**: [Name]
- **Contact**: cae-team@example.com

## Solver Versions

| Solver | Version | Notes |
|--------|---------|-------|
| OpenFOAM | v10 | Primary CFD solver |
| ANSYS Fluent | 2024R1 | Commercial CFD |
| Abaqus | 2023 | Primary FEA solver |
| preCICE | v3.0 | Multi-physics coupling |

## Directory Structure

```
CAE/
├─ README.md                    # This file
├─ META.json                    # Ownership and contact info
├─ TEMPLATE_METADATA.yaml       # Metadata template for cases
├─ SCRIPTS/                     # Orchestration and CI scripts
├─ CFD/                         # CFD analyses
├─ FEA/                         # FEA analyses
├─ COUPLING/                    # Multi-physics coupling
├─ DATA/                        # Experimental and baseline data
├─ QA/                          # Quality assurance
├─ VALIDATION/                  # Validation reports
└─ DOCS/                        # Detailed documentation
```

## Quick Start

1. **Copy this template** to your subsystem's CAE directory
2. **Update META.json** with your team information
3. **Create a new case** in CFD/cases/ or FEA/cases/
4. **Copy TEMPLATE_METADATA.yaml** to your case directory and fill it out
5. **Run smoke tests** using SCRIPTS/ci_smoke.sh
6. **Document results** in baseline/metrics.json

## CI Integration

The CI system automatically runs:
- Metadata validation via `SCRIPTS/check_metadata.py`
- Smoke tests from `CFD/cases/*/smoke/` and `FEA/cases/*/smoke/`
- Regression comparison against `DATA/regression_baselines/`

CI runs must complete in < 10 minutes on standard runners.

## File Management

### Git LFS

Use Git LFS for:
- All mesh files (.msh, .unv, etc.)
- Solver binary outputs (field data, results databases)
- Native CAD/FEA files (.CATPart, .prt, .odb, etc.)

### Neutral Formats

Maintain neutral formats alongside native files:
- STEP for geometry
- Nastran bulk data for meshes
- CSV/JSON for results

## Standards and Guidelines

1. **Naming Convention**: `{CASE_ID}_{DESCRIPTION}_{REV}.{ext}`
2. **Traceability**: Link to UTCS URIs in metadata
3. **Documentation**: Document numerical schemes and models in DOCS/
4. **Determinism**: Keep smoke cases deterministic (seed RNGs)
5. **Baselines**: All baselines require metrics.json with standard keys

## Required Metrics Keys

Every `baseline/metrics.json` must include:
- `mass` (kg or appropriate unit)
- `energy_kwh` (kWh)
- `peak_temp_C` (°C)
- `mass_flow_kg_s` (kg/s)
- `runtime_s` (seconds)

## Support

For questions or issues:
- Email: cae-team@example.com
- Documentation: See DOCS/ for detailed guides
- Examples: See CFD/cases/tank_solidification/ and FEA/cases/static_stress/

---

**Template Version:** 1.0  
**Last Updated:** 2025-10-23  
**Maintained by:** CAE Template Working Group
