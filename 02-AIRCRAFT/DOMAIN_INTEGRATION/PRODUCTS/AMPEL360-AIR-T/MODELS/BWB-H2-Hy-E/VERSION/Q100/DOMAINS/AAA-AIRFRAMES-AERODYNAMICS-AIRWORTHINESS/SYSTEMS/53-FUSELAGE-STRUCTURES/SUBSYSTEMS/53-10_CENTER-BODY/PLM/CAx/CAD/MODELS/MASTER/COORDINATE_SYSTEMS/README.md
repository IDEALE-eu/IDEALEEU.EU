# COORDINATE_SYSTEMS — Standard Coordinate System Definitions

## Purpose

Master coordinate system definitions for consistent model orientation and interface definition.

## Content

- Aircraft coordinate system
- Body coordinate system
- Local coordinate systems by zone
- Interface coordinate systems
- Analysis coordinate systems
- Manufacturing coordinate systems

## Naming Convention

```
53-10_MASTER_CSYS_<TYPE>_<DESCRIPTION>_v<VERSION>.<ext>
```

Examples:
- `53-10_MASTER_CSYS_AIRCRAFT_v01.CATPart`
- `53-10_MASTER_CSYS_BODY_v02.prt`
- `53-10_MASTER_CSYS_INTERFACE-LDG-GEAR_v01.prt`

## Usage

All models use these coordinate systems for:
- Model orientation
- Interface definitions
- Load application points
- CG calculations
