# MATERIALS — Material Thermophysical Properties

## Purpose
Material thermophysical properties for thermal and structural analysis.

## Contents
- Thermal conductivity k(T) [W/m·K]
- Specific heat c_p(T) [J/kg·K]
- Density ρ(T) [kg/m³]
- Coefficient of thermal expansion CTE(T) [1/K]
- Emissivity ε(T) (for uncoated surfaces)

## File Organization
- One file per material or alloy
- Include temperature-dependent data
- Document source (standard, test, vendor)
- Store supporting test reports

## Naming Convention
```
21-10-CAE_materials_<material_name>__r<NN>__<STATUS>.{csv|xlsx}
```

Example: `21-10-CAE_materials_aluminum_6061_t6__r01__REL.csv`

## Data Requirements
- Material identification and specification
- Temperature range (min/max)
- Property values at multiple temperatures
- Source reference (MMPDS, vendor, test)
- Uncertainty or tolerance

## Common Materials
- **Aluminum alloys**: 6061, 7075, 2024
- **Composites**: Carbon fiber, graphite epoxy
- **Stainless steel**: 304, 316
- **Copper alloys**: Pure copper, C10100
- **Titanium**: Ti-6Al-4V
- **Insulators**: MLI, foam, ceramic

## Property Table Format
```
Temperature (°C) | k (W/m·K) | c_p (J/kg·K) | ρ (kg/m³) | CTE (1/K)
-----------------|-----------|--------------|-----------|----------
-100             | 180       | 850          | 2700      | 21e-6
+25              | 170       | 900          | 2700      | 23e-6
+100             | 165       | 950          | 2700      | 24e-6
```

## Guidelines
- Reference material specifications (MMPDS, ASTM)
- Include lot-specific data if available
- Document test temperature range
- Maintain uncertainty quantification

---

**Last Updated**: 2025-10-10
