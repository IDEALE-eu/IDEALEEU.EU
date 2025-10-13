# FASTENER_MAPS — Fastener Specifications and Installation Maps

## Purpose

Comprehensive fastener installation documentation including part numbers, torque specifications, and installation procedures for all joints in the CENTER-BODY subsystem.

## Content Types

- **Fastener Installation Maps** — Visual fastener location and type
- **Bills of Fasteners** — Complete parts lists with quantities
- **Torque Specifications** — Installation torque requirements
- **Installation Procedures** — Assembly sequences and methods

## File Formats

- `.pdf` — Installation drawings and procedures
- `.csv` — Fastener bills of materials
- `.xlsx` — Torque specification matrices
- `.step` — 3D fastener installation models

## Naming Convention

```
FastenerMap_{joint_id}_{type}_v{version}.{ext}
```

Examples:
- `FastenerMap_J-001_wing_joint_install_v001.pdf`
- `FastenerMap_J-015_BOM_v002.csv`
- `FastenerMap_J-020_torque_spec_v001.xlsx`

## Cross-References

- [Parent: MOUNTING](../README.md)
- [Hole Patterns](../HOLE_PATTERNS/README.md)
- [Hardpoints](../HARDPOINTS/README.md)
- [Load Paths](../LOAD_PATHS/README.md)
- [Interface Definitions](../../INTERFACES/)

## Fastener BOM Format

```csv
fastener_id,part_number,description,material,diameter,grip_length,qty,torque_Nm,installation_notes
F-001,NAS6204-12,Bolt Hi-Lok,A286,1/4",12mm,24,8.5±0.5,Dry installation
F-002,NAS1149F0832P,Washer,Steel,1/4",-,24,-,Under bolt head
F-003,HL70-4-12,Collar Hi-Lok,A286,1/4",12mm,24,Pull-up,Install wet
```

## Fastener Type Classifications

| Type | Application | Torque Method | Typical Use |
|------|-------------|---------------|-------------|
| **Hi-Lok** | Shear joints | Pull-up or torque | Primary structure |
| **Hi-Lite** | Tension joints | Torque | Secondary structure |
| **NAS Bolt** | General purpose | Torque wrench | Non-critical joints |
| **Lockbolt** | High-shear | Hydraulic pull | High-load joints |
| **Rivet** | Permanent | Shop head | Skin attachments |

## Torque Specifications

Standard torque requirements:
- **Dry installation**: As per fastener specification
- **Wet installation**: +10% over dry torque
- **Lubricated**: Specify lubricant type
- **Prevailing torque**: Check initial break-away

## Installation Requirements

Critical fastener installation steps:
1. **Hole inspection** — Verify diameter, countersink, cleanliness
2. **Sealant application** — If required (wet installation)
3. **Fastener insertion** — Correct orientation, washer placement
4. **Torque application** — Per specification, calibrated tools
5. **Inspection** — Visual and torque verification
6. **Documentation** — Record actual torque values

## Sealant Application

Sealant requirements by joint type:
- **Fuel tank interfaces**: PR-1422 (Class A)
- **Pressure boundary**: PR-1440 (Class B)
- **Weather sealing**: PR-1776 (Class C)
- **Non-sealing**: Dry installation

## Validation Requirements

- Torque wrench calibration verification
- First fastener torque audit (every shift)
- Random torque checks (10% sampling)
- Visual inspection (100% of installations)
- Shimming and fit-up verification

## Special Installation Notes

**Critical Fasteners**: 
- 100% torque inspection
- Witness by QA inspector
- Documentation of each fastener

**High-Load Fasteners**:
- Pre-torque pattern specified
- Final torque in sequence
- Load distribution analysis

## Change Control

Fastener specification changes require:
- Structural engineering approval
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Part number cross-reference documentation
- Training if installation method changes
- [Hole Patterns](../HOLE_PATTERNS/README.md) compatibility check
