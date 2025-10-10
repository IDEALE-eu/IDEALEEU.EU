# MODELS — Analysis Models

## Purpose
This directory contains thermal, structural, and fluid analysis models for radiators, heat exchangers, coldplates, and TIMs.

## Subdirectories

### [tmm/](tmm/) — Thermal Mathematical Models
Thermal network models (conductive/radiative):
- Node-based thermal models
- Thermal resistances and capacitances
- Radiation view factors
- Contact conductance models
- MLI modeling
- Thermal interfaces

**Format**: TMM solver files, network diagrams, coupling definitions

### [fem/](fem/) — Finite Element Models
Structural analysis models:
- Flatness and stiffness analysis
- Mechanical loads (launch, operational)
- Thermal distortion
- Mount and interface stresses
- Bolt preload and joint modeling

**Format**: FEM solver decks (Nastran, ANSYS, Abaqus), mesh files

### [cfd/](cfd/) — Computational Fluid Dynamics
Flow and pressure drop models:
- Loop heat exchanger (LPHX) hydraulics
- Coldplate channel flow
- Pressure drop calculations
- Two-phase flow modeling
- Heat transfer coefficients

**Format**: CFD solver files (ANSYS Fluent, Star-CCM+), mesh files

## Model Organization
```
<model_name>/
  ├─ README.md (description, assumptions, validation)
  ├─ model_files/ (native solver formats)
  ├─ geometry/ (CAD references)
  └─ validation/ (test correlation data)
```

## Guidelines
- Document all modeling assumptions
- Maintain model-to-hardware traceability
- Version control all model changes
- Include material property references
- Archive validation evidence
- Link to test correlation data

---

**Last Updated**: 2025-10-10
