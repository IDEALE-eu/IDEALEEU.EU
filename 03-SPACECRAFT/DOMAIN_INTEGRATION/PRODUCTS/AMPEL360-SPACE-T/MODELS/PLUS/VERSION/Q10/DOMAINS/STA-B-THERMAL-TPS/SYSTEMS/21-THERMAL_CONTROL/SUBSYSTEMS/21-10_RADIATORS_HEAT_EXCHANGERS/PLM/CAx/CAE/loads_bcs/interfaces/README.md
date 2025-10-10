# INTERFACES — Interface Definitions

## Purpose
Thermal interface properties including TIMs, contact conductances, clamps, and mounting hardware.

## Contents
- Thermal interface material (TIM) conductivity k(T)
- Contact conductance h(T, P)
- Clamp and mount thermal definitions
- Interface areas and gap dimensions
- Bondline thicknesses
- Fastener thermal paths

## File Organization
- One file per interface type
- Include temperature-dependent properties
- Document test data sources
- Store vendor data sheets

## Naming Convention
```
21-10-CAE_interfaces_<type>_<material>__r<NN>__<STATUS>.{csv|xlsx}
```

Example: `21-10-CAE_interfaces_tim_gap_pad__r01__REL.csv`

## Data Requirements
- Interface identification
- Material or contact type
- Thermal conductivity k(T) or conductance h(T, P)
- Temperature range
- Pressure dependency (if applicable)
- Uncertainty factors

## Interface Types
- **TIMs**: Gap pads, phase change materials, thermal greases
- **Contact**: Metal-to-metal, bolted joints
- **Clamps**: C-clamps, mounting brackets
- **Fasteners**: Screws, bolts (thermal shorts)

## Property Format
```
Temperature (°C) | k (W/m·K) or h (W/m²·K) | Uncertainty (%)
-----------------|-------------------------|------------------
-50              | 3.0                     | ±15%
+25              | 3.2                     | ±15%
+100             | 3.5                     | ±15%
```

## Guidelines
- Reference vendor data sheets
- Include test correlation data
- Document application pressure
- Maintain margin/uncertainty quantification

---

**Last Updated**: 2025-10-10
