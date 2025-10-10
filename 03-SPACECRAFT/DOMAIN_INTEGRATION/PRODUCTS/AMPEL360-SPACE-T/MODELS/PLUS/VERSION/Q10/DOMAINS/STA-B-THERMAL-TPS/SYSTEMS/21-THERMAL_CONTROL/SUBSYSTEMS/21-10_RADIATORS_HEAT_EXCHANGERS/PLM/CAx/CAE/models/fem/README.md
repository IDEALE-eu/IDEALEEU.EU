# FEM — Finite Element Models

## Purpose
Structural analysis models for radiators, heat exchangers, and mounting hardware.

## Contents
- Flatness and stiffness analysis models
- Mechanical loads (launch, operational)
- Thermal distortion analysis
- Mount and interface stress analysis
- Bolt preload and joint modeling
- Modal analysis for dynamics

## File Organization
- Use descriptive filenames indicating component and load case
- Include revision/version in filename
- Store mesh quality reports
- Document element types and mesh density

## Naming Convention
```
21-10-CAE_fem_<component>_<loadcase>__r<NN>__<STATUS>.{ext}
```

Example: `21-10-CAE_fem_coldplate_launch__r02__REL.fem`

## Model Requirements
- Document mesh convergence study
- Validate element quality metrics
- Include material property temperature dependencies
- Document boundary conditions and loads
- Reference interface definitions

## Analysis Types
- Static structural analysis
- Thermal-structural coupling
- Modal and frequency response
- Contact and bolt preload
- Fatigue and life prediction

## Standards
- Follow structural modeling per ECSS-E-ST-32C
- Maintain positive margins of safety
- Document analysis assumptions

---

**Last Updated**: 2025-10-10
