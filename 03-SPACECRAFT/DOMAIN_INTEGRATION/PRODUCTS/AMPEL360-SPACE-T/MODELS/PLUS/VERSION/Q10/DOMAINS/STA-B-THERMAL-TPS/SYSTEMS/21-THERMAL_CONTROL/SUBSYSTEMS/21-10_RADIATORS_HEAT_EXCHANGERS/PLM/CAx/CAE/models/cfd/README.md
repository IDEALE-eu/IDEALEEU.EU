# CFD — Computational Fluid Dynamics

## Purpose
Fluid flow and heat transfer models for loop heat exchangers (LPHX), coldplates, and thermal fluid loops.

## Contents
- LPHX hydraulic models
- Coldplate channel flow analysis
- Pressure drop calculations
- Two-phase flow modeling
- Heat transfer coefficient prediction
- Flow distribution analysis

## File Organization
- Use descriptive filenames indicating component and flow regime
- Include revision/version in filename
- Store mesh quality reports
- Document solver settings and convergence criteria

## Naming Convention
```
21-10-CAE_cfd_<component>_<condition>__r<NN>__<STATUS>.{ext}
```

Example: `21-10-CAE_cfd_lphx_nominal_flow__r01__RVW.cas`

## Model Requirements
- Document mesh independence study
- Validate turbulence model selection
- Include fluid property temperature dependencies
- Document boundary conditions (inlet/outlet)
- Reference experimental correlation data

## Analysis Types
- Single-phase liquid flow
- Two-phase flow (if applicable)
- Conjugate heat transfer
- Pressure drop prediction
- Flow uniformity assessment

## Standards
- Follow CFD best practices
- Maintain validation against test data
- Document numerical convergence criteria

---

**Last Updated**: 2025-10-10
