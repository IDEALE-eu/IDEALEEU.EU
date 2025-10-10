# LOCAL — Local Component Reference Planes

## Purpose

This directory contains CAD models of local reference planes specific to individual structural components and assemblies of the 53-10 Center Body. These planes are defined relative to local coordinate systems of specific features.

## Contents

### FRAME_FXX/ — Frame Local Planes
- **Description**: Reference planes local to individual frame structures
- **Coordinate System**: Origin at frame centerline and baseline
- **Plane Types**:
  - Frame web plane
  - Cap attachment planes
  - Stringer attachment planes
  - Clip mounting planes
  - Inspection access planes
- **Usage**: Frame fabrication, assembly, and inspection

**Typical Frame Planes**:
- `FRAME_F05_WEB`: Main web plane of frame F05
- `FRAME_F10_CAP_UPPER`: Upper cap attachment plane
- `FRAME_F15_STRINGER_LEFT`: Left side stringer attachment plane

### STRINGER_LXX/ — Stringer Local Planes
- **Description**: Reference planes local to longitudinal stringer members
- **Coordinate System**: Origin at stringer centerline
- **Plane Types**:
  - Stringer web plane
  - Cap attachment planes
  - Clip mounting planes
  - Frame intersection planes
  - Runout planes
- **Usage**: Stringer fabrication, splicing, and installation

**Typical Stringer Planes**:
- `STRINGER_L01_WEB`: Main web plane of stringer L01
- `STRINGER_L03_CAP`: Cap attachment reference
- `STRINGER_L05_SPLICE`: Splice joint reference plane

### PANEL_PXX/ — Panel Local Planes
- **Description**: Reference planes local to skin panel sections
- **Coordinate System**: Origin at panel geometric center or corner
- **Plane Types**:
  - Panel outer mold line (OML) plane
  - Panel inner mold line (IML) plane
  - Edge trim planes
  - Stiffener attachment planes
  - Fastener pattern planes
- **Usage**: Panel fabrication, trimming, and assembly

**Typical Panel Planes**:
- `PANEL_P01_OML`: Outer surface reference
- `PANEL_P02_IML`: Inner surface reference
- `PANEL_P03_EDGE_FWD`: Forward edge trim plane
- `PANEL_P04_EDGE_AFT`: Aft edge trim plane

### DOOR_DXX/ — Door Local Planes
- **Description**: Reference planes local to door openings and assemblies
- **Coordinate System**: Origin at door frame geometric center
- **Plane Types**:
  - Door opening plane
  - Hinge attachment planes
  - Latch mounting planes
  - Seal groove planes
  - Clearance planes
- **Usage**: Door fabrication, installation, and adjustment

**Typical Door Planes**:
- `DOOR_D01_OPENING`: Door opening reference plane
- `DOOR_D01_HINGE_LINE`: Hinge centerline plane
- `DOOR_D01_SEAL`: Seal contact plane
- `DOOR_D01_CLEARANCE`: Minimum clearance envelope

## Local Coordinate System Definition

Each local coordinate system should specify:
- **Origin**: Location relative to global aircraft coordinates
- **X-axis**: Primary direction (typically longitudinal or along feature)
- **Y-axis**: Secondary direction (typically lateral or across feature)
- **Z-axis**: Normal direction (typically perpendicular to surface)
- **Transformation**: Translation and rotation from global coordinates

## Naming Convention

Use the following pattern:
```
53-10_LOCAL_<component-type>_<id>_<plane-description>_<version>.<ext>
```

Examples:
- `53-10_LOCAL_FRAME_F05_WEB_v01.CATPart`
- `53-10_LOCAL_STRINGER_L03_CAP_v01.prt`
- `53-10_LOCAL_PANEL_P01_OML_v01.sldprt`
- `53-10_LOCAL_DOOR_D01_HINGE_v01.CATPart`

## Component Numbering

### Frame Numbering
- Format: `FXX` where XX is frame number (01-99)
- Example: F05, F10, F15

### Stringer Numbering
- Format: `LXX` where XX is stringer number (01-99)
- L prefix for longitudinal member
- Example: L01, L03, L05

### Panel Numbering
- Format: `PXX` where XX is panel number (01-99)
- Example: P01, P02, P03

### Door Numbering
- Format: `DXX` where XX is door number (01-99)
- Example: D01, D02

## Usage Guidelines

### Design Applications
- Component-specific dimensioning
- Local feature positioning
- Assembly fit verification
- Clearance checking

### Manufacturing Applications
- Fabrication datum setup
- Machining references
- Tool alignment
- Quality inspection

### Assembly Applications
- Component alignment
- Mating surface verification
- Fastener pattern location
- Interface gap control

## Documentation Requirements

Each local plane model should include:
- Local coordinate system definition
- Relationship to global coordinates
- Associated component identification
- Tolerance specifications
- Usage notes

## Standards Compliance

Follow:
- **ATA Chapter 53**: Fuselage structures
- **ASME Y14.5**: Datum reference frames
- **ISO 1101**: Geometrical tolerancing
- **Company design standards**: Local coordinate system conventions

## Related Directories

- **Global planes**: [`../GLOBAL/`](../GLOBAL/)
- **Station planes**: [`../STATIONS/`](../STATIONS/)
- **Assembly models**: [`../../../TOP_LEVEL/`](../../../TOP_LEVEL/)
- **Component models**: [`../../../../MODELS/`](../../../../MODELS/)
