# PROPERTIES — Material and Surface Properties

## Purpose
This directory contains material thermophysical properties, coating optical properties, and fluid properties for thermal analysis.

## Subdirectories

### [materials/](materials/) — Material Properties
Thermophysical properties:
- Thermal conductivity k(T)
- Specific heat c_p(T)
- Density ρ(T)
- Coefficient of thermal expansion (CTE)
- Emissivity (if applicable)

**Format**: CSV/XLSX tables with temperature-dependent data

### [coatings/](coatings/) — Coating Optical Properties
Surface coating properties:
- Solar absorptance α
- Infrared emissivity ε
- Temperature dependence
- Angle dependence
- Degradation factors (EOL)

**Format**: Property tables, test data, vendor specifications

### [fluids/](fluids/) — Fluid Properties
Heat transfer fluid properties:
- Dynamic viscosity µ(T)
- Density ρ(T)
- Thermal conductivity k(T)
- Specific heat c_p(T)
- Two-phase properties (if applicable)

**Format**: Property tables for loop fluids, refrigerants

## File Organization
- One file per material or coating type
- Include temperature-dependent data
- Document test data sources
- Store vendor specifications

## Naming Convention
```
21-10-CAE_<type>_<material_name>__r<NN>__<STATUS>.{csv|xlsx}
```

Example: `21-10-CAE_materials_aluminum_6061__r01__REL.csv`

## Guidelines
- Reference standard databases (MMPDS, vendor data)
- Include temperature range applicability
- Document uncertainties
- Maintain traceability to test data

---

**Last Updated**: 2025-10-10
