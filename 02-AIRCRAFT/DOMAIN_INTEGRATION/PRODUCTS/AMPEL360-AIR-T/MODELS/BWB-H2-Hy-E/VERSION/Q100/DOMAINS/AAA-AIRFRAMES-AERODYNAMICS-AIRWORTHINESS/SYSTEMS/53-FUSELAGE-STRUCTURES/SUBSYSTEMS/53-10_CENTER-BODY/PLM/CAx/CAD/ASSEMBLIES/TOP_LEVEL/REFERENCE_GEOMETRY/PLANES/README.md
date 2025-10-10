# PLANES — Reference Planes

## Purpose

This directory contains reference plane definitions used for modeling, assembly, and manufacturing reference.

## Contents

### Plane Types
- **Datum planes**: Primary, secondary, and tertiary datums
- **Construction planes**: Modeling and sketching references
- **Symmetry planes**: Aircraft centerline and other symmetry
- **Section planes**: Cross-section references

## Standard Planes

### Primary Aircraft Planes
- **X-Y Plane (WL 0)**: Horizontal reference at waterline zero
- **X-Z Plane (BL 0)**: Vertical centerline plane
- **Y-Z Plane**: Transverse planes at fuselage stations

### Center Body Planes
- **Forward bulkhead plane**: Front interface datum
- **Aft bulkhead plane**: Rear interface datum
- **Floor planes**: Cabin floor reference surfaces
- **Wing attachment planes**: Wing-to-body interface datums

## File Format

Reference planes may be stored as:
- Native CAD plane features
- Geometric definition files (point-normal form)
- Equation-based plane definitions

## Naming Convention

```
53-10_PLANE_<name>_<version>.<ext>
```

Examples:
- `53-10_PLANE_CENTERLINE_v01.txt`
- `53-10_PLANE_FWD-BULKHEAD_v01.csv`
- `53-10_PLANE_FLOOR-LEVEL-1_v01.dat`

## Documentation

Each plane should specify:
- **Position**: Point on the plane (X, Y, Z)
- **Orientation**: Normal vector or three points
- **Type**: Datum, construction, symmetry, etc.
- **Purpose**: Intended use and reference

## Related References

- **Datums**: [`../DATUMS/`](../DATUMS/) — Datum feature specifications
- **Coordinate Systems**: [`../COORDINATE_SYSTEMS/`](../COORDINATE_SYSTEMS/) — Related coordinate frames
