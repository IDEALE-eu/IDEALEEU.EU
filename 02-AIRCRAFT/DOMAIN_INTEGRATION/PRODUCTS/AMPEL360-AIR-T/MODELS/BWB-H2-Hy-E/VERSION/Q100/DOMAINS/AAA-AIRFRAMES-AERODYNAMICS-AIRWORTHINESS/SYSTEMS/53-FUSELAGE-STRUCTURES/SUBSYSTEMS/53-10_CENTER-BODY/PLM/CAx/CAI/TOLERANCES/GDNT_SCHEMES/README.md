# GDNT_SCHEMES — Geometric Dimensioning and Tolerancing Schemes

## Purpose

Geometric Dimensioning and Tolerancing (GD&T) schemes for the CENTER-BODY subsystem per ASME Y14.5 standards.

## Content Types

- **GD&T Callout Definitions** — Feature control frames
- **Datum Reference Frames** — DRF definitions and hierarchies
- **Tolerance Specifications** — Geometric tolerances by feature type
- **Inspection Methods** — CMM programs and procedures

## File Formats

- `.pdf` — GD&T drawings and specifications
- `.dxf` / `.dwg` — 2D tolerance drawings
- `.dmis` — CMM inspection programs
- `.csv` — Tolerance tables and schedules

## Naming Convention

```
GDNT_{component}_{feature_type}_v{version}.{ext}
```

Examples:
- `GDNT_centerbody_primary_datums_v001.pdf`
- `GDNT_bulkhead_flatness_spec_v002.csv`
- `GDNT_skin_panel_profile_v001.dxf`

## Cross-References

- [Parent: TOLERANCES](../README.md)
- [Stackup Analysis](../STACKUPS/README.md)
- [Master Geometry Datums](../../MASTER_GEOMETRY/DATUMS/README.md)
- [ATA-06 Tolerances](../../../../../../../06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-80_MEASUREMENT_TOLERANCES_GDT/README.md)

## GD&T Standard

All tolerancing per:
- **ASME Y14.5-2018** — Primary standard
- **ISO 1101** — International equivalent
- **AIA NAS 979** — Aerospace supplemental

## Datum Reference Frames

Primary DRF for CENTER-BODY:
```
| Datum | Feature | Degrees Constrained |
|-------|---------|---------------------|
| A | Fwd bulkhead face | 3 (translation Z, rotation X, Y) |
| B | Centerline keel | 2 (translation X, Y) |
| C | Side reference plane | 1 (rotation Z) |
```

## Tolerance Types and Applications

| GD&T Symbol | Control | Typical Application | Tolerance Range |
|-------------|---------|---------------------|-----------------|
| ⏥ (Flatness) | Surface form | Bulkhead faces | 0.5-2.0mm |
| ⌭ (Position) | Feature location | Hole patterns | 0.1-1.0mm |
| ∥ (Parallelism) | Orientation | Frame members | 0.3-1.5mm |
| ⊥ (Perpendicularity) | Orientation | Mounting faces | 0.2-1.0mm |
| ⌒ (Profile) | Surface | OML/IML surfaces | 0.5-3.0mm |
| ○ (Runout) | Rotation | Cylindrical features | 0.2-0.5mm |

## Tolerance Allocation Strategy

Tolerance allocation priorities:
1. **Critical interfaces** — Tightest tolerances (± 0.1mm)
2. **Structural joints** — Moderate tolerances (± 0.5mm)
3. **Secondary features** — Standard tolerances (± 1.0mm)
4. **Non-functional** — Relaxed tolerances (± 2.0mm)

## Material Condition Modifiers

- **MMC (Maximum Material Condition)**: Used for feature patterns (holes)
- **LMC (Least Material Condition)**: Used for thin-wall features
- **RFS (Regardless of Feature Size)**: Default, no modifier

## Inspection Requirements

All GD&T features require:
- CMM (Coordinate Measuring Machine) measurement
- Certified inspection per AS9102 First Article
- Documented measurement uncertainty
- Statistical process control (Cpk ≥ 1.33)

## CMM Programming Format

```dmis
DMISMN/'GDNT_INSPECTION_PROGRAM_v001'
UNITS/MM
DATUM/A,PLANE
DATUM/B,LINE
DATUM/C,PLANE
TOL/FLAT,0.5,DATUM A
TOL/POS,0.2@MMC,DATUM A,B,C
ENDMES
```

## Validation Requirements

- Design tolerance validation (capability studies)
- Manufacturing process capability analysis
- Supplier capability verification
- First article inspection (FAI) 100%
- Production sampling per AS9102

## Change Control

GD&T scheme changes require:
- Dimensional engineering approval
- Impact on manufacturing reviewed
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Updated inspection procedures
- [Stackup analysis](../STACKUPS/README.md) re-validation
