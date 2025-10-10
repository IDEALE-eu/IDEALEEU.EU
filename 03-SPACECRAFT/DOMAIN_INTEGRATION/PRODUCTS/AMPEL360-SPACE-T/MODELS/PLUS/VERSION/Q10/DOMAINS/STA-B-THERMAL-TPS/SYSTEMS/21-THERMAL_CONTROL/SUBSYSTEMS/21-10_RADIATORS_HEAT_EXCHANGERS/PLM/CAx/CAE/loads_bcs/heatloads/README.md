# HEATLOADS — Heat Dissipation Tables

## Purpose
Component power dissipation data and heat load definitions for thermal analysis.

## Contents
- Component heat dissipation tables
- Power vs operational mode
- Time-dependent load profiles
- Duty cycle definitions
- Heat load uncertainties and margins

## File Organization
- One file per component or subsystem
- Include operational mode definitions
- Document load allocation methodology
- Store supporting calculations

## Naming Convention
```
21-10-CAE_heatloads_<component>_<mode>__r<NN>__<STATUS>.{csv|xlsx}
```

Example: `21-10-CAE_heatloads_electronics_nominal__r02__REL.csv`

## Data Requirements
- Component identification
- Nominal power dissipation (W)
- Operational mode definitions
- Uncertainty factors
- Source and date of data

## Typical Heat Sources
- Electronics boxes
- Reaction wheels
- Solar array drive electronics
- Battery charge/discharge
- Propulsion components

## Table Format
```
Component ID | Mode | Power (W) | Uncertainty (%) | Notes
-------------|------|-----------|-----------------|-------
COMP-001     | NOM  | 25.0      | ±10%            | ...
```

## Guidelines
- Reference power budget documentation
- Document worst-case assumptions
- Include margin policy
- Maintain traceability to requirements

---

**Last Updated**: 2025-10-10
