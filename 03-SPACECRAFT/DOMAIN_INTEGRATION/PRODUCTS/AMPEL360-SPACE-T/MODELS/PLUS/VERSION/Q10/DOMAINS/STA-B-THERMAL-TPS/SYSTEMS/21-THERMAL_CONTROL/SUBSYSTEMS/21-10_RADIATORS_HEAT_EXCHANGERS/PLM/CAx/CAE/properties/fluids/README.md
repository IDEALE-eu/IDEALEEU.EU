# FLUIDS — Fluid Thermophysical Properties

## Purpose
Heat transfer fluid properties for loop heat exchangers (LPHX), coldplates, and thermal control loops.

## Contents
- Dynamic viscosity µ(T) [Pa·s]
- Kinematic viscosity ν(T) [m²/s]
- Density ρ(T) [kg/m³]
- Thermal conductivity k(T) [W/m·K]
- Specific heat c_p(T) [J/kg·K]
- Prandtl number Pr(T)
- Two-phase properties (if applicable)

## File Organization
- One file per fluid type
- Include temperature-dependent data
- Document source (vendor, database)
- Store supporting test reports

## Naming Convention
```
21-10-CAE_fluids_<fluid_name>__r<NN>__<STATUS>.{csv|xlsx}
```

Example: `21-10-CAE_fluids_ammonia__r01__REL.csv`

## Data Requirements
- Fluid identification and specification
- Temperature range (operating limits)
- Property values at multiple temperatures
- Source reference (vendor, NIST, Refprop)
- Pressure dependency (if significant)

## Common Fluids
- **Water/Glycol**: Propylene glycol, ethylene glycol mixtures
- **Refrigerants**: Ammonia (R717), R134a, R404A
- **Dielectrics**: HFE-7000, FC-72, Novec fluids
- **Hydrocarbons**: Alkanes, synthetic oils
- **Cryogens**: Liquid nitrogen, liquid helium

## Property Table Format
```
Temperature (°C) | ρ (kg/m³) | c_p (J/kg·K) | k (W/m·K) | µ (Pa·s)
-----------------|-----------|--------------|-----------|----------
-20              | 1030      | 3800         | 0.45      | 0.0089
+25              | 1000      | 4180         | 0.60      | 0.0010
+80              | 970       | 4190         | 0.67      | 0.0004
```

## Two-Phase Properties
- Saturation pressure P_sat(T)
- Enthalpy of vaporization h_fg(T)
- Surface tension σ(T)
- Quality (vapor fraction)

## Guidelines
- Reference fluid specification (ASHRAE, vendor)
- Include safety and compatibility data
- Document operating pressure range
- Maintain uncertainty quantification

---

**Last Updated**: 2025-10-10
