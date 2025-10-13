# PLANES — Reference Planes and Datum Surfaces

## Purpose

This directory contains CAD models defining reference planes and datum surfaces used for design, manufacturing, and inspection of the 53-10 Center Body.

## Contents

### Reference Plane Types
- **Fuselage Reference Plane (FRP)**: Primary vertical reference
- **Buttock Line Planes (BL)**: Lateral reference planes
- **Waterline Planes (WL)**: Horizontal reference planes
- **Station Planes (STA)**: Longitudinal reference planes

## Standard Reference Planes

### Fuselage Reference Plane (FRP)
- Vertical plane through aircraft centerline
- Defines symmetry plane
- Primary datum for lateral measurements
- Buttock Line 0 (BL0)

### Buttock Lines (BL)
- Parallel to FRP
- Offset in lateral (Y) direction
- Positive values: starboard side (right)
- Negative values: port side (left)
- Typical spacing: 100mm or per design standard

### Waterlines (WL)
- Horizontal planes
- Perpendicular to FRP
- Reference for vertical dimensions
- Origin typically at aircraft datum
- Typical spacing: 100mm or per design standard

### Station Planes (STA)
- Perpendicular to aircraft longitudinal axis
- Define longitudinal positions
- Origin at aircraft reference point
- Typical spacing: varies by structural design

## Center Body Specific Planes

### Key Station Planes
- Forward bulkhead plane
- Wing attachment planes (left/right)
- Center body frame stations (F01-F20)
- Aft bulkhead plane

### Interface Planes
- Wing-to-body interface plane
- Door frame planes
- Equipment mounting planes
- Inspection access planes

## Naming Convention

Use the following pattern:
```
53-10_REF_PLANE_<plane-type>_<location>_<version>.<ext>
```

Examples:
- `53-10_REF_PLANE_FRP_v01.CATPart`
- `53-10_REF_PLANE_BL-0_v01.prt`
- `53-10_REF_PLANE_WL-1000_v01.sldprt`
- `53-10_REF_PLANE_STA-500_v02.CATPart`

## Plane Definition Requirements

Each reference plane should specify:
- Plane type (FRP, BL, WL, STA)
- Location/offset from reference
- Normal vector direction
- Associated coordinate system
- Tolerance requirements

## Usage

### Design Applications
- Component positioning
- Symmetry checks
- Dimension references
- Section views

### Manufacturing Applications
- Tooling setup planes
- Machining references
- Assembly alignment
- Inspection setup

### Analysis Applications
- Model sectioning
- Symmetry boundary conditions
- Load plane definitions
- Results visualization

## Documentation

Each plane model should include:
- Plane definition (normal, point)
- Reference coordinate system
- Offset/location values
- Usage instructions
- Related interface documents

## Standards Compliance

Follow:
- **ATA iSpec 2200**: Aircraft reference plane conventions
- **ISO 5458**: Positional tolerancing
- **ASME Y14.5**: Datum reference frames

## Related Directories

- **Coordinate systems**: [`../COORDINATE_SYSTEMS/`](../COORDINATE_SYSTEMS/)
- **Assembly models**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)
- **Drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)
