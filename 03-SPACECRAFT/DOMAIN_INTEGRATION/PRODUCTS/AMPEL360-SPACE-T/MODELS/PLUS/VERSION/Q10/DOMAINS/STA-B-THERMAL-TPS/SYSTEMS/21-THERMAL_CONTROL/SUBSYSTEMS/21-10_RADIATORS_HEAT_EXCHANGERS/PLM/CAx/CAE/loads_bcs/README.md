# LOADS_BCS — Loads and Boundary Conditions

## Purpose
This directory contains thermal loads, environmental definitions, and interface boundary conditions for analysis.

## Subdirectories

### [heatloads/](heatloads/) — Heat Dissipation Tables
Component power dissipation data:
- Heat loads vs operational mode
- Power dissipation tables (W)
- Time-dependent load profiles
- Uncertainty factors

**Format**: CSV/XLSX tables, load profile definitions

### [environments/](environments/) — Thermal Environments
Orbital and environmental parameters:
- Solar flux and albedo
- Earth IR heating
- Beta angle definitions
- Seasonal variations
- Sink temperatures

**Format**: Environment definition files, parametric tables

### [interfaces/](interfaces/) — Interface Definitions
Thermal interface properties:
- TIM thermal conductivity k(T)
- Contact conductance h(T, P)
- Clamp and mount definitions
- Interface areas and gaps
- Bondline thicknesses

**Format**: Interface property tables, contact definitions

## File Organization
- Use descriptive filenames
- Include source and date of data
- Document uncertainties and margins
- Reference requirements and specifications

## Naming Convention
```
21-10-CAE_<type>_<description>__r<NN>__<STATUS>.{csv|xlsx}
```

Example: `21-10-CAE_heatloads_nominal_ops__r01__REL.csv`

## Guidelines
- Maintain traceability to source data
- Document worst-case assumptions
- Include uncertainty quantification
- Version control all load definitions

---

**Last Updated**: 2025-10-10
