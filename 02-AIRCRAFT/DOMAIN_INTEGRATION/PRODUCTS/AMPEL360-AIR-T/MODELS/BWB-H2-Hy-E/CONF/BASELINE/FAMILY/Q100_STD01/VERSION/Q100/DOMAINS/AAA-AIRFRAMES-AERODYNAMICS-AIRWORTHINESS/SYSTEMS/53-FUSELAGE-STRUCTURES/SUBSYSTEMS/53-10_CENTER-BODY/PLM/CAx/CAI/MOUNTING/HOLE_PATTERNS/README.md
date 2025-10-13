# HOLE_PATTERNS — Fastener Hole Patterns and Drilling Templates

## Purpose

Detailed fastener hole pattern definitions for all joints and attachments in the CENTER-BODY subsystem.

## Content Types

- **Hole Pattern Drawings** — Dimensioned fastener layouts
- **Drilling Templates** — Manufacturing aids
- **Hole Schedules** — Size, type, tolerance tables
- **Countersink Specifications** — Depth and angle requirements

## File Formats

- `.pdf` — Pattern drawings and specifications
- `.dxf` / `.dwg` — 2D hole pattern geometry
- `.csv` — Hole schedule tables
- `.step` — 3D hole pattern models
- `.nc` / `.apt` — CNC drilling programs

## Naming Convention

```
HolePattern_{joint_id}_{type}_v{version}.{ext}
```

Examples:
- `HolePattern_J-001_wing_joint_v001.pdf`
- `HolePattern_J-015_floor_beam_v002.dxf`
- `HolePattern_J-020_bulkhead_schedule_v001.csv`

## Cross-References

- [Parent: MOUNTING](../README.md)
- [Fastener Maps](../FASTENER_MAPS/README.md)
- [Hardpoints](../HARDPOINTS/README.md)
- [Tolerances](../../TOLERANCES/)
- [Interface Definitions](../../INTERFACES/)

## Hole Schedule Format

```csv
hole_id,x_coord,y_coord,diameter,tolerance,type,countersink,treatment
H-001,100.0,50.0,6.35,±0.05,Through,100°×10.5mm,None
H-002,110.0,50.0,6.35,±0.05,Through,100°×10.5mm,None
H-003,120.0,50.0,8.00,±0.05,Through,None,Bushing
```

## Hole Type Classifications

| Type | Description | Typical Use |
|------|-------------|-------------|
| **Through** | Complete penetration | Standard fasteners |
| **Blind** | Partial depth | One-sided access |
| **Countersunk** | Flush head recess | Aerodynamic surfaces |
| **Counterbored** | Non-flush recess | Internal structure |
| **Bushingd** | Metal insert | High-load interfaces |

## Tolerancing Requirements

Standard hole tolerances per manufacturing method:
- **Drilled holes**: ±0.05mm
- **Reamed holes**: ±0.025mm
- **Close tolerance**: ±0.013mm
- **Interference fit**: -0.000/+0.025mm

## Drilling Sequence

Critical joints require documented drilling sequence:
1. Pilot holes (undersized)
2. Match drilling (to final size)
3. Deburring and cleaning
4. Inspection (CMM or optical)
5. Surface treatment (if required)
6. Final inspection

## Validation Requirements

- Pattern dimensioning per ASME Y14.5
- Hole-to-edge distance verification (minimum 2D)
- Hole-to-hole spacing verification (minimum 3D)
- Countersink depth measurement
- Surface finish verification

## Manufacturing Notes

- All critical hole patterns require production templates
- First article inspection (FAI) required
- Drilling sequence must prevent interference
- Tool access verification required
- Chip evacuation provisions documented

## Change Control

Hole pattern changes require:
- Manufacturing engineering review
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Template updates
- Operator training if process changes
- [Fastener Maps](../FASTENER_MAPS/README.md) update
