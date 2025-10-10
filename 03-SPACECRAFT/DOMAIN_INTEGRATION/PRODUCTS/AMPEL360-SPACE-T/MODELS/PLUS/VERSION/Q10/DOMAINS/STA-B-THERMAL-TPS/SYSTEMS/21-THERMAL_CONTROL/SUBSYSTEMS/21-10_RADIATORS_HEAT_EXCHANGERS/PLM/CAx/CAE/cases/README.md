# CASES — Analysis Cases

## Purpose
This directory contains analysis case definitions for various operational and environmental conditions.

## Subdirectories

### [thermal_balance/](thermal_balance/) — Thermal Balance Cases
Steady-state orbital thermal analysis:
- Hot case (maximum heat load, high solar flux)
- Cold case (minimum heat load, eclipse)
- Worst-case hot/cold combinations
- Beta angle sweeps
- Seasonal variations

**Format**: Case definition files, boundary condition sets, configuration files

### [transient/](transient/) — Transient Analysis
Time-dependent thermal analysis:
- Operational mode transitions
- Eclipse entry/exit
- Survival heating profiles
- Power-on transients
- Thermal cycling

**Format**: Transient solver decks, time-dependent boundary conditions

### [tvac/](tvac/) — Thermal Vacuum Test Cases
TVAC chamber simulation cases:
- Test configuration matching
- Shroud temperature profiles
- Heat load simulation
- Correlation cases
- Test predictions

**Format**: TVAC-specific case files with CAV linkage

## Case Organization
```
<case_name>/
  ├─ README.md (objectives, assumptions)
  ├─ inputs/ (boundary conditions, loads)
  ├─ setup/ (case configuration)
  └─ documentation/ (analysis plan, success criteria)
```

## Guidelines
- Document case objectives and success criteria
- Reference applicable thermal requirements
- Include worst-case analysis rationale
- Maintain traceability to environments
- Link to correlation test data

---

**Last Updated**: 2025-10-10
