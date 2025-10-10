# DATUMS_COORDS — Datums and Coordinate Systems

## Purpose

This directory contains definitions of coordinate systems, datum references, and measurement frameworks used for interface control and dimensional management.

## Contents

### [COORDINATE_SYSTEMS/](./COORDINATE_SYSTEMS/)
Master coordinate system definitions including:
- Aircraft body coordinate system (BCS)
- Local subsystem coordinate systems
- Interface-specific coordinate frames
- Transformation matrices between systems
- Origin definitions and axis orientations

### [DATUM_REFERENCES/](./DATUM_REFERENCES/)
Datum reference definitions including:
- Primary datums (A, B, C)
- Secondary and tertiary datums
- Datum targets and features
- Measurement reference points
- Tooling ball locations

## File Types

- `.pdf` — Coordinate system drawings and specifications
- `.csv` — Coordinate transformation tables
- `.step` — 3D reference geometry with coordinate frames
- `.json` — Machine-readable coordinate definitions
- `.xlsx` — Datum reference tables

## Naming Convention

```
{type}_{description}_v{version}.{ext}
```

Examples:
- `CS_AIRCRAFT-BCS_v001.pdf`
- `CS_53-10-LOCAL_v002.step`
- `DATUM_PRIMARY-A_v001.pdf`
- `DATUM_TOOLING-BALLS_v001.csv`

## Usage Guidelines

### Coordinate System Selection
1. Use aircraft BCS as primary reference
2. Define local systems when needed for manufacturing or assembly
3. Document all transformations
4. Maintain consistency across interfaces

### Datum Definition
1. Select stable, accessible features
2. Follow GD&T standards (ASME Y14.5)
3. Define datum order of precedence
4. Document measurement procedures

## Cross-References

- [Interface Control Documents](../ICD/)
- [Tolerances and GD&T](../TOLERANCES_GDT/)
- [Assembly References](../../REFERENCES/)
- [Installation Documentation](../../INSTALLATION/)

## Standards

- **ASME Y14.5-2018**: Dimensioning and Tolerancing
- **ISO 1101**: Geometrical tolerancing
- **ISO 5459**: Geometrical tolerancing - Datums and datum systems
- **AIA NAS 3000**: National Aerospace Standard for coordinate systems
