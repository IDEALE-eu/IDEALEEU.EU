# THERMAL_BALANCE — Thermal Balance Cases

## Purpose
Steady-state orbital thermal analysis cases for radiators and heat exchangers under various environmental conditions.

## Contents
- Hot case analysis (maximum heat load, high solar flux)
- Cold case analysis (minimum heat load, eclipse)
- Worst-case hot/cold combinations
- Beta angle parametric sweeps
- Seasonal variation analysis
- Sun-pointing and inertial attitudes

## File Organization
- One subdirectory per case or beta angle
- Include case description and objectives
- Store boundary conditions and environments
- Document margin analysis

## Naming Convention
```
21-10-CAE_thermal_balance_<condition>__r<NN>__<STATUS>/
```

Example: `21-10-CAE_thermal_balance_hot_case__r02__REL/`

## Case Requirements
- Define solar flux and albedo
- Specify IR environmental heating
- Document heat dissipation levels
- Include sink temperature assumptions
- Reference thermal coating properties

## Analysis Outputs
- Component temperature predictions
- Heater power requirements
- Thermal margin assessment
- Interface temperature verification
- Radiator performance validation

## Standards
- Follow ECSS-E-ST-31C thermal analysis guidelines
- Verify compliance with thermal requirements
- Document worst-case environments

---

**Last Updated**: 2025-10-10
