# COORDINATE_SYSTEMS — Coordinate System Definitions

## Purpose

This directory contains coordinate system definitions used for the top-level assembly positioning and component alignment.

## Contents

### Coordinate System Types
- **Global aircraft frame (GAF)**: Master aircraft coordinate system
- **Local assembly frames**: Center body local coordinate systems
- **Interface frames**: Coordinate systems at system interfaces
- **Manufacturing frames**: Tooling and fixture coordinate systems

## Coordinate System Convention

Per ATA Chapter 06:
- **X-axis**: Positive forward (nose to tail)
- **Y-axis**: Positive right (pilot's perspective)
- **Z-axis**: Positive up (perpendicular to X-Y plane)

### Station References
- **FS (Fuselage Station)**: X-direction measurements
- **WL (Water Line)**: Z-direction measurements
- **BL (Butt Line)**: Y-direction measurements

## File Format

Coordinate systems may be stored as:
- Native CAD features (CATIA axis systems, NX CSYS)
- Text files with transformation matrices
- CSV files with origin and orientation data

## Naming Convention

```
53-10_CSYS_<name>_<version>.<ext>
```

Examples:
- `53-10_CSYS_CENTER-BODY-ORIGIN_v01.txt`
- `53-10_CSYS_WING-INTERFACE_v01.csv`

## Documentation

Each coordinate system should document:
- **Origin location**: X, Y, Z coordinates in GAF
- **Orientation**: Rotation angles or direction cosines
- **Purpose**: Intended use and reference
- **Traceability**: Parent coordinate system

## Related References

- **Dimensions & Stations**: [`../../../../../../../06-DIMENSIONS-STATIONS/`](../../../../../../../06-DIMENSIONS-STATIONS/)
- **Interface Control**: [`../../DOCS/INTERFACE_CONTROL/`](../../DOCS/INTERFACE_CONTROL/)
