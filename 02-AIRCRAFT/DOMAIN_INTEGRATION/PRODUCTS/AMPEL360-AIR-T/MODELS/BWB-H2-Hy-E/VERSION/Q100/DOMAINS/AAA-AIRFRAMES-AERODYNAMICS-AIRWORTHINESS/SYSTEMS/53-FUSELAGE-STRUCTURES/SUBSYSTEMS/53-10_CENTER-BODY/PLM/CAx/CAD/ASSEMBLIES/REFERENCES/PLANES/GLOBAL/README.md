# GLOBAL — Global Reference Planes

## Purpose

This directory contains CAD models of the primary global reference planes that define the aircraft coordinate system for the 53-10 Center Body. These planes establish the fundamental geometric reference framework.

## Contents

### XY/ — Horizontal Reference Plane
- **Description**: Primary horizontal plane (XY plane)
- **Definition**: Plane containing the X-axis (longitudinal) and Y-axis (lateral)
- **Normal Direction**: Z-axis (vertical, positive up)
- **Usage**: Waterline reference, horizontal cross-sections

### XZ/ — Vertical Longitudinal Plane
- **Description**: Primary vertical longitudinal plane (XZ plane)
- **Definition**: Plane containing the X-axis (longitudinal) and Z-axis (vertical)
- **Normal Direction**: Y-axis (lateral)
- **Usage**: Fuselage reference plane (FRP), symmetry plane, buttock line BL0

### YZ/ — Vertical Transverse Plane
- **Description**: Primary vertical transverse plane (YZ plane)
- **Definition**: Plane containing the Y-axis (lateral) and Z-axis (vertical)
- **Normal Direction**: X-axis (longitudinal)
- **Usage**: Station plane reference, frame cross-sections

## Aircraft Coordinate System

### Axis Definitions
- **X-axis**: Fuselage Station (FS), positive aft (rearward)
- **Y-axis**: Buttock Line (BL), positive right (starboard)
- **Z-axis**: Waterline (WL), positive up

### Origin
- Aircraft reference point (typically at nose or datum point)
- All global planes pass through or are referenced to this origin

## Usage Guidelines

### Design Applications
- Establish master coordinate system
- Define symmetry conditions
- Create sectional views
- Position components relative to aircraft axes

### Manufacturing Applications
- Tooling alignment
- Assembly jig setup
- Quality inspection reference
- Dimensional verification

### Analysis Applications
- Symmetry boundary conditions
- Load plane definitions
- Results visualization
- Model sectioning

## Naming Convention

Use the following pattern:
```
53-10_GLOBAL_PLANE_<plane-type>_<version>.<ext>
```

Examples:
- `53-10_GLOBAL_PLANE_XY_v01.CATPart`
- `53-10_GLOBAL_PLANE_XZ_SYMMETRY_v01.prt`
- `53-10_GLOBAL_PLANE_YZ_STATION_v01.sldprt`

## Standards Compliance

Follow:
- **ATA iSpec 2200**: Aircraft coordinate system conventions
- **ISO 1101**: Geometrical tolerancing
- **ASME Y14.5**: Datum reference frames

## Related Directories

- **Station planes**: [`../STATIONS/`](../STATIONS/)
- **Coordinate systems**: [`../../COORDINATE_SYSTEMS/`](../../COORDINATE_SYSTEMS/)
- **Assembly models**: [`../../../TOP_LEVEL/`](../../../TOP_LEVEL/)
