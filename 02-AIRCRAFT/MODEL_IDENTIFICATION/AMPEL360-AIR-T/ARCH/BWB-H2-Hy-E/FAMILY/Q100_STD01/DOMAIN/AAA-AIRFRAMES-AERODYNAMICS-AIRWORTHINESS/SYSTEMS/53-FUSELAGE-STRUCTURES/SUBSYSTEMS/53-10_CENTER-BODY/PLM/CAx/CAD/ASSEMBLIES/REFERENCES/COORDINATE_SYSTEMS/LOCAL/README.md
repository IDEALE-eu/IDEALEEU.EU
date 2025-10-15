# LOCAL — Local Component Coordinate Systems

## Purpose

This directory contains local coordinate system definitions for specific structural components within the 53-10 Center Body.

## Contents

### FRAME_FXX/
Frame-specific coordinate systems:
- Local axes at each structural frame location
- Origin at frame centerline intersection with reference plane
- Used for frame design, manufacturing, and installation
- Naming: FXX where XX = frame number/station

### STRINGER_LXX/
Stringer-specific coordinate systems:
- Local axes along stringer run
- Origin at stringer start point
- Tangent, normal, and binormal directions
- Naming: LXX where XX = stringer identifier

### PANEL_PXX/
Panel-specific coordinate systems:
- Local axes for skin panel sections
- Origin at panel reference corner or center
- Used for thickness definition, layup orientation, fastener patterns
- Naming: PXX where XX = panel identifier

### DOOR_DXX/
Door frame coordinate systems:
- Local axes at door/opening locations
- Origin at door frame reference point
- Used for door fitting, sealing, and mechanism mounting
- Naming: DXX where XX = door identifier

## Naming Convention

Local coordinate systems follow:
```
53-10_REF_CS_<component_type>_<identifier>_v<version>.<ext>
```

Examples:
- `53-10_REF_CS_FRAME_F12_v01.CATPart`
- `53-10_REF_CS_STRINGER_L05_v01.prt`
- `53-10_REF_CS_PANEL_P23_v01.sldprt`
- `53-10_REF_CS_DOOR_D01_v02.CATPart`

## Transformation Chain

Local coordinate systems are typically related to global systems through:
```
Global (Aircraft Body) → Station (FS/WL/BL) → Local (Component)
```

Each transformation must be documented with:
- Translation vector (X, Y, Z offsets)
- Rotation matrix or Euler angles
- Tolerance specifications
- Reference to parent coordinate system

## Cross-References

- [Parent: COORDINATE_SYSTEMS](../README.md)
- [Global Systems](../GLOBAL/README.md)
- [Station Systems](../STATIONS/README.md)
- [Component Models](../../../MODELS/README.md)

## Usage Guidelines

### Design
- Component-specific modeling reference
- Local feature positioning
- Assembly relationship definition

### Manufacturing
- Tooling and fixture design
- NC programming references
- Inspection setup

### Assembly
- Installation procedures
- Alignment requirements
- Fit checks

---

**Owner**: 53-10 Center Body Detail Design  
**Status**: Component-specific; created as needed  
**Maintenance**: Update with each design revision
