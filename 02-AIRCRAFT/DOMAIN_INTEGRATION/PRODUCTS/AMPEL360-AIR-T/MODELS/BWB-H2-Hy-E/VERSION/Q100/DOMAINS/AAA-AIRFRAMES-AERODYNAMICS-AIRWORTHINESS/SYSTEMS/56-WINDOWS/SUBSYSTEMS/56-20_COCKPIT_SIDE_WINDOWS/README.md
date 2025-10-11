# 56-20 COCKPIT_SIDE_WINDOWS — Windows (BWB-H2-Hy-E, Q100)

**Purpose**: Cockpit side windows for lateral visibility, including glazing, mounting, sealing, and optional heating/anti-ice capability.

## Scope
- Left and right cockpit side windows
- Sliding or fixed window configurations
- Structural mounting and sealing
- Emergency egress capability (if applicable)
- Optional heating/anti-ice integration
- Mounting frames and gaskets

## Key Requirements
- **Visibility**: Side and downward visibility for pilots
- **Structural**: Withstand pressurization and operational loads
- **Optical**: Adequate clarity, minimal distortion
- **Emergency egress**: Quick opening mechanism (if designated egress window)
- **Sealing**: Pressure sealing, weather protection
- **Heating**: Optional anti-ice/defog (coordinated with ATA-30)

## Interfaces
- **24 Electrical** — Power for heating (if applicable)
- **30 Ice/Rain Protection** — Anti-ice coordination (if applicable)
- **53 Fuselage** — Mounting structure, cutouts
- **92 EWIS** — Wiring for heating elements (if applicable)

## Deliverables
- Side window assembly drawings (CAD)
- Structural analysis (pressure, emergency loads) (CAE)
- Installation procedures (CAI)
- Manufacturing specifications (CAM)
- Service procedures (CAS)

## PLM Structure

This subsystem contains engineering artifacts organized by CAx discipline in the [PLM/CAx/](./PLM/CAx/) directory.

### Engineering BOM
See [PLM/EBOM_LINKS.md](./PLM/EBOM_LINKS.md) for Bill of Materials references.

## Directory Structure

```
56-20_COCKPIT_SIDE_WINDOWS/
├─ README.md (this file)
└─ PLM/
   ├─ EBOM_LINKS.md
   └─ CAx/
      ├─ CAD/  — Assembly drawings, 3D models
      ├─ CAE/  — Structural analysis
      ├─ CAO/  — Design optimization
      ├─ CAI/  — Installation procedures
      ├─ CAM/  — Manufacturing specifications
      ├─ CAV/  — Validation and testing
      ├─ CAP/  — Production procedures
      ├─ CAS/  — Service and maintenance
      └─ CMP/  — Materials processing
```

## Configuration Management
- Changes via ECR/ECO per `00-PROGRAM/CONFIG_MGMT/`

## References
- Parent system: [56-WINDOWS](../../README.md)
- Standards: [56-00_STANDARDS_GENERAL](../56-00_STANDARDS_GENERAL/README.md)
