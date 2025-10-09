# COORDINATE_SYSTEMS — Local Coordinate System Definitions

## Purpose

This directory contains definitions and transformations for local coordinate systems used in the 53-10 CENTER-BODY subsystem integration.

## Content Types

- **Coordinate System Definitions** — Mathematical definitions of local frames
- **Transformation Matrices** — Conversion between local and global coordinate systems
- **Origin Specifications** — Reference point locations and orientations
- **Axis Alignment Data** — Angular relationships and rotation sequences

## File Formats

- `.yaml` / `.json` — Structured coordinate system definitions
- `.csv` — Tabular transformation matrices
- `.pdf` — Documentation and derivation notes

## Naming Convention

```
CS_{component}_{frame_name}_v{version}.{ext}
```

Examples:
- `CS_centerbody_local_v001.yaml`
- `CS_transform_global_to_local_v001.csv`

## Cross-References

- [Parent: MASTER_GEOMETRY](../README.md)
- [Global Datums: ATA-06-10](../../../../../../../06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-10_GLOBAL_DATUMS_COORDINATES/README.md)
- [CAI Root Documentation](../../README.md)

## Validation Requirements

All coordinate system definitions must:
- Reference the Global Aircraft Frame (GAF) from ATA-06
- Include transformation validation test cases
- Document rotation sequence (e.g., XYZ Euler, quaternions)
- Specify units (mm, degrees, radians)

## Change Control

Changes to coordinate systems require:
- ECR approval via [CHANGE_CONTROL/RFC](../../CHANGE_CONTROL/RFC/README.md)
- Validation against master geometry
- Update of dependent interface definitions
