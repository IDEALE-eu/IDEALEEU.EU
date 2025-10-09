# HARDPOINTS — Structural Hardpoint Definitions and Load Capacities

## Purpose

Definitions of structural hardpoints in the CENTER-BODY subsystem, including attachment provisions for systems, equipment, and structural interfaces.

## Content Types

- **Hardpoint Specifications** — Location, geometry, load capacity
- **Load Envelope Definitions** — Allowable load combinations
- **Attachment Hardware Specifications** — Fitting details
- **Installation Procedures** — Torque specifications and sequences

## File Formats

- `.pdf` — Hardpoint specification sheets
- `.step` — 3D hardpoint geometry
- `.csv` — Hardpoint location tables
- `.xlsx` — Load capacity matrices

## Naming Convention

```
HP_{zone}_{identifier}_{type}_v{version}.{ext}
```

Examples:
- `HP_fwd_001_engine_mount_v001.pdf`
- `HP_center_005_equipment_rack_v002.csv`
- `HP_aft_010_stabilizer_attach_v001.step`

## Cross-References

- [Parent: MOUNTING](../README.md)
- [Load Paths](../LOAD_PATHS/README.md)
- [Fastener Maps](../FASTENER_MAPS/README.md)
- [Interface Definitions](../../INTERFACES/)
- [Master Geometry](../../MASTER_GEOMETRY/DATUMS/README.md)

## Hardpoint Classification

| Class | Description | Load Range | Usage |
|-------|-------------|------------|-------|
| **Primary** | Critical structural | >50 kN | Engine, wing, stabilizer |
| **Secondary** | Major equipment | 10-50 kN | HVAC packs, systems |
| **Tertiary** | Minor equipment | <10 kN | Avionics, brackets |

## Hardpoint Data Requirements

Each hardpoint must document:
- **Location**: X, Y, Z coordinates relative to GAF
- **Orientation**: Load direction vectors
- **Load Capacity**: Ultimate loads (all 6 DOF)
- **Interface Type**: Lug, clevis, bolt pattern, etc.
- **Material**: Structure and fitting materials
- **Surface Treatment**: Corrosion protection
- **Inspection Requirements**: NDI access and methods

## Load Capacity Format

```csv
hardpoint_id,location_x,location_y,location_z,Fx_ult,Fy_ult,Fz_ult,Mx_ult,My_ult,Mz_ult,material
HP_fwd_001,5000,0,1200,150000,50000,100000,20000,30000,15000,Ti-6Al-4V
```

## Validation Requirements

- Structural analysis for ultimate loads (1.5× limit)
- Fatigue life analysis (design service goal)
- Installation accessibility verification
- Corrosion compatibility assessment
- Temperature effects on load capacity

## Change Control

Hardpoint modifications require:
- Structural re-analysis and approval
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Notification to affected system owners
- Update to [INTERFACE_MATRIX](../../INTERFACE_MATRIX/README.md)
- Re-inspection if previously installed
