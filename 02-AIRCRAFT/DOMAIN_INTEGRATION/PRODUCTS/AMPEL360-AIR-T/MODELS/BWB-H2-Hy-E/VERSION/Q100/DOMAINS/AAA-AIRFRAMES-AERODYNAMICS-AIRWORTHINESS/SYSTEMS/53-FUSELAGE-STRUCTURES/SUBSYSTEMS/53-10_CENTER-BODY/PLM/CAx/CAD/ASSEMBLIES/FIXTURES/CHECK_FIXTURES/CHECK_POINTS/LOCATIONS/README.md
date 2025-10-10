# LOCATIONS — Check Point Locations

## Purpose

This directory contains specific location definitions for inspection check points on parts and assemblies.

## Contents

### Location Types
- **Dimensional check points**: Specific measurement locations
- **Feature locations**: Holes, slots, edges, surfaces
- **Interface check points**: Mating surface verification points
- **Critical feature locations**: Safety and function-critical points

## Naming Convention

Use the following pattern:
```
LOCATIONS_<part-id>_<check-type>_<version>.xlsx
```

Examples:
- `LOCATIONS_FRAME-F05_DIMENSIONAL_v01.xlsx`
- `LOCATIONS_WING-INTERFACE_FEATURES_v02.xlsx`
- `LOCATIONS_SKIN-PANEL-001_CRITICAL_v01.xlsx`

## Check Point Data

Each check point location should define:
- **Point ID**: Unique identifier
- **Coordinates**: Nominal X, Y, Z position
- **Feature type**: Hole, surface, edge, etc.
- **Characteristic**: Dimension, position, profile, etc.
- **Measurement method**: CMM, laser tracker, gauge
- **Tolerance**: See TOLERANCES directory
- **Drawing reference**: Source drawing and detail
- **Notes**: Special instructions

## File Format

### Spreadsheet Columns
| Point ID | Feature | X (mm) | Y (mm) | Z (mm) | Type | Method | Tolerance | Drawing | Notes |
|----------|---------|--------|--------|--------|------|--------|-----------|---------|-------|
| CP001    | Hole 1  | 100.0  | 200.0  | 50.0   | Dia  | CMM    | ±0.1      | DWG-001 | Critical |

## Coordinate System

All locations referenced to:
- Master coordinate system
- Datum reference frame (DRF)
- Aircraft coordinate system when applicable
- Clearly defined origin and orientation

## Inspection Frequency

Define for each check point:
- **100%**: Every part inspected
- **Sample**: Statistical sampling (e.g., 1 in 10)
- **First article**: Initial production only
- **Periodic**: At specified intervals
- **Witness**: Customer/inspector present

## Related Directories

- **Datums**: [`../DATUMS/`](../DATUMS/)
- **Tolerances**: [`../TOLERANCES/`](../TOLERANCES/)
- **CMM programs**: [`../../CMM/PROGRAMS/`](../../CMM/PROGRAMS/)
- **Laser tracker targets**: [`../../LASER_TRACKER/TARGETS/`](../../LASER_TRACKER/TARGETS/)
