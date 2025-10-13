# 56-60 SCRATCH_PANES_SHADES_BLINDS — Windows (BWB-H2-Hy-E, Q100)

**Purpose**: Removable protective panes, window shades, and blinds for passenger and crew windows.

## Scope
- Cockpit removable scratch panes (outer protective layer)
- Passenger window shades and blinds
- Mounting mechanisms and tracks
- Manual and powered actuation (if applicable)
- Light control and heat rejection
- Aesthetic appearance and cabin integration

## Key Requirements
- **Scratch panes**: Easy removal/replacement, optical clarity, scratch resistance
- **Shades/blinds**: Smooth operation, reliable retention, aesthetic appearance
- **Mounting**: Secure attachment, no rattling or vibration
- **Materials**: Fire resistance, low toxicity, UV stability
- **Maintenance**: Easy inspection and replacement
- **Weight**: Minimize weight while meeting functional requirements

## Interfaces
- **25 Cabin Interior** — Integration with interior trim and aesthetics
- **56-30 Cabin Windows** — Shade/blind mounting provisions

## Deliverables
- Scratch pane and shade assembly drawings (CAD)
- Material specifications (CAV)
- Installation procedures (CAI)
- Manufacturing specifications (CAM)
- Replacement procedures (CAS)

## PLM Structure

This subsystem contains engineering artifacts organized by CAx discipline in the [PLM/CAx/](./PLM/CAx/) directory.

### Engineering BOM
See [PLM/EBOM_LINKS.md](./PLM/EBOM_LINKS.md) for Bill of Materials references.

## Directory Structure

```
56-60_SCRATCH_PANES_SHADES_BLINDS/
├─ README.md (this file)
└─ PLM/
   ├─ EBOM_LINKS.md
   └─ CAx/
      ├─ CAD/  — Assembly drawings
      ├─ CAE/  — Analysis (if applicable)
      ├─ CAO/  — Design optimization
      ├─ CAI/  — Installation procedures
      ├─ CAM/  — Manufacturing specifications
      ├─ CAV/  — Material testing, validation
      ├─ CAP/  — Production procedures
      ├─ CAS/  — Replacement procedures
      └─ CMP/  — Materials processing
```

## Configuration Management
- Changes via ECR/ECO per `00-PROGRAM/CONFIG_MGMT/`

## References
- Parent system: [56-WINDOWS](../../README.md)
- Standards: [56-00_STANDARDS_GENERAL](../56-00_STANDARDS_GENERAL/README.md)
