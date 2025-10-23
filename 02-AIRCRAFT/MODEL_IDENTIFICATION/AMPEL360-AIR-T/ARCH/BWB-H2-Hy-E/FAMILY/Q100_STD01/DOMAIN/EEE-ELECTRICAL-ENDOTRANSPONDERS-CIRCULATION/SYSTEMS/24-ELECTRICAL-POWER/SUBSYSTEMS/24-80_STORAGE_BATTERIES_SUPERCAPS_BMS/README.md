# Subsystem: 24-80_STORAGE_BATTERIES_SUPERCAPS_BMS

## Description

Energy Storage Systems - Batteries, Supercapacitors, Battery Management System (BMS)

This subsystem (24-80) is dedicated to energy storage components, distinct from subsystem 24-40 which handles energy distribution.

**Contents**:
- CO₂ Endocircular Battery System (dry ice battery)
- Battery Management Systems
- Supercapacitors
- Energy storage control systems

## PLM Structure

This subsystem contains engineering artifacts organized by CAx discipline:

### Engineering BOM

See [PLM/EBOM_LINKS.md](./PLM/EBOM_LINKS.md) for BOM references.

### CAx Directories

- [CAD/](./PLM/CAx/CAD/) - Computer-Aided Design (3D models, drawings, **design specifications**)
- [CAE/](./PLM/CAx/CAE/) - Computer-Aided Engineering (FEA, analysis, **simulations**)
- [CAO/](./PLM/CAx/CAO/) - Computer-Aided Optimization (design optimization)
- [CAM/](./PLM/CAx/CAM/) - Computer-Aided Manufacturing (NC programming, tooling)
- [CAI/](./PLM/CAx/CAI/) - Computer-Aided Installation (installation procedures, **industrial applications**)
- [CAV/](./PLM/CAx/CAV/) - Computer-Aided Validation (test models, validation data)
- [CAP/](./PLM/CAx/CAP/) - Computer-Aided Process planning
- [CAS/](./PLM/CAx/CAS/) - Computer-Aided Services (**S1000D technical publication workflows only**)
- [CMP/](./PLM/CAx/CMP/) - Configuration Management Program (**ECNs/ECOs, baselines, quality KPIs**)

## Directory Structure

```
24-80_STORAGE_BATTERIES_SUPERCAPS_BMS/
├─ README.md (this file)
└─ PLM/
   ├─ EBOM_LINKS.md
   └─ CAx/
      ├─ CAD/  ← Design specifications (CO2_BATTERY_TECHNICAL_DOCS.md)
      ├─ CAE/  ← Simulations (co2_battery_endocircular.py, tests)
      ├─ CAI/  ← Industrial applications (co2_battery_examples.py)
      ├─ CAO/
      ├─ CAM/
      ├─ CAP/
      ├─ CAS/  ← S1000D workflows only
      ├─ CAV/
      └─ CMP/  ← Configuration management
```

## Contents

### CO₂ Endocircular Battery System

A closed-loop CO₂-based energy storage system for aircraft applications.

- **Design Specs** (CAD): Complete technical documentation
- **Simulations** (CAE): Core thermodynamic models and tests
- **Applications** (CAI): Industrial use cases and examples

See individual CAx directories for detailed information.

## Note on Taxonomy

Per IDEALE-EU engineering taxonomy:
- **CAS** is reserved exclusively for S1000D technical publication workflows
- **CMP** is for configuration management (ECNs/ECOs, baselines, quality control)
- General technical documentation belongs in **CAD** (design specifications)

---

**Last Updated**: 2025-10-23
