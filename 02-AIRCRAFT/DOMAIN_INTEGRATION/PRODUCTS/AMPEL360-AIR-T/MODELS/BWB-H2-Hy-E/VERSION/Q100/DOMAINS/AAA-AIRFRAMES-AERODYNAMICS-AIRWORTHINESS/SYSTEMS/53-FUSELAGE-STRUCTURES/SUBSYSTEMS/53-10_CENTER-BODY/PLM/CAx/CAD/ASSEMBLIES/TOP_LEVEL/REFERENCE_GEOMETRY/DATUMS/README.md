# DATUMS — Datum Features

## Purpose

This directory contains datum feature definitions per ASME Y14.5 and ISO 1101 standards for geometric dimensioning and tolerancing (GD&T).

## Contents

### Datum Types
- **Primary datums**: Highest precedence geometric references
- **Secondary datums**: Second-level references
- **Tertiary datums**: Third-level references
- **Datum features**: Physical features used as datums
- **Datum reference frames**: Complete 3-2-1 datum systems

## Datum Framework

### Datum Reference Frame (DRF)
A DRF establishes a coordinate system using three mutually perpendicular planes:
- **Primary datum**: Establishes first constraint (typically a plane)
- **Secondary datum**: Establishes second constraint (typically a line or plane)
- **Tertiary datum**: Establishes third constraint (typically a point or plane)

### Center Body Datums
- **Datum A**: Horizontal reference plane (typically WL reference)
- **Datum B**: Vertical centerline plane (BL 0)
- **Datum C**: Transverse plane at specific FS

## Standards Compliance

Follow:
- **ASME Y14.5-2018**: Dimensioning and tolerancing
- **ISO 1101:2017**: Geometrical tolerancing
- **ATA iSpec 2200**: Technical documentation

## File Format

Datums may be documented as:
- CAD datum features in assembly models
- Engineering drawings with datum callouts
- Datum definition documents (PDF, text)

## Naming Convention

```
53-10_DATUM_<identifier>_<version>.<ext>
```

Examples:
- `53-10_DATUM_A_DEFINITION_v01.pdf`
- `53-10_DATUM_B_CENTERLINE_v01.txt`
- `53-10_DATUM_FRAME_ABC_v01.pdf`

## Documentation

Each datum should specify:
- **Datum identifier**: Letter designation (A, B, C, etc.)
- **Datum feature**: Physical feature or theoretical plane
- **Tolerance**: Datum feature tolerance if applicable
- **Material condition**: RFS, MMC, or LMC modifier
- **Purpose**: Manufacturing, assembly, or inspection reference

## Related References

- **Planes**: [`../PLANES/`](../PLANES/) — Reference plane definitions
- **Coordinate Systems**: [`../COORDINATE_SYSTEMS/`](../COORDINATE_SYSTEMS/) — Coordinate frame references
- **Interface Control**: [`../../DOCS/INTERFACE_CONTROL/`](../../DOCS/INTERFACE_CONTROL/) — Interface datum requirements
