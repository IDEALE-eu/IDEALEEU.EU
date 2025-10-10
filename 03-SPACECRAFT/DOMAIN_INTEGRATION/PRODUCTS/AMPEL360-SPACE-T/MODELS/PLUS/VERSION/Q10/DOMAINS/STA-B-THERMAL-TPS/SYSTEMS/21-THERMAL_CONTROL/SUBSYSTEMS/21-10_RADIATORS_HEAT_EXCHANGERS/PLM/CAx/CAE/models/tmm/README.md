# TMM — Thermal Mathematical Models

## Purpose
Thermal network models for conductive and radiative heat transfer analysis of radiators and heat exchangers.

## Contents
- Node-based thermal models
- Thermal resistances and capacitances
- Radiation view factors and optical properties
- Contact conductance definitions
- Multi-layer insulation (MLI) models
- Thermal interface material (TIM) modeling

## File Organization
- Use descriptive filenames indicating component and configuration
- Include revision/version in filename
- Store supporting documentation alongside models
- Reference material properties and boundary conditions

## Naming Convention
```
21-10-CAE_tmm_<component>__r<NN>__<STATUS>.{ext}
```

Example: `21-10-CAE_tmm_radiator_panel__r03__REL.tmm`

## Model Requirements
- Document node numbering scheme
- Include mesh convergence study
- Validate contact conductance assumptions
- Reference material property sources
- Document radiation coupling methodology

## Standards
- Follow thermal modeling best practices per ECSS-E-ST-31C
- Ensure model-to-hardware traceability
- Maintain validation against test data

---

**Last Updated**: 2025-10-10
