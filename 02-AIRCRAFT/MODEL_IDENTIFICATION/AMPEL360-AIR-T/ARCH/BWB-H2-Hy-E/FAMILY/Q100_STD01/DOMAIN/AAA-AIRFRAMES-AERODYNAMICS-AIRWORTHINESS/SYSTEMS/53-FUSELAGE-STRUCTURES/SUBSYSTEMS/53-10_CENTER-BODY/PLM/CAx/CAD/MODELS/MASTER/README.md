# MASTER — Master Geometry and Reference Models

## Purpose

This directory contains the master reference geometry, datums, and coordinate systems that define the fundamental geometric framework for the 53-10 Center Body. All part and assembly models reference these master definitions.

## Organization

Master geometry is organized by type:

- **SKELETON/** — Master skeleton geometry and layout structure
- **DATUMS/** — Reference datums and datum targets
- **COORDINATE_SYSTEMS/** — Standard coordinate system definitions
- **SURFACE_REF/** — Reference surfaces (OML, IML, mold lines)

## Naming Convention

Use the following pattern for master files:
```
53-10_MASTER_<TYPE>_<DESCRIPTION>_v<VERSION>.<ext>
```

Examples:
- `53-10_MASTER_SKELETON_LAYOUT_v01.CATPart`
- `53-10_MASTER_OML_SURFACE_v02.prt`
- `53-10_MASTER_CSYS_AIRCRAFT_v01.prt`
- `53-10_MASTER_DATUM_PRIMARY_v01.CATPart`

## Content Guidelines

### SKELETON
- Global layout structure
- Station lines and waterlines
- Zone boundaries
- Major structural hard points

### DATUMS
- Primary datum targets (A, B, C)
- Secondary datums
- Tooling datums
- Inspection datums

### COORDINATE_SYSTEMS
- Aircraft coordinate system
- Body coordinate system
- Local coordinate systems by zone
- Interface coordinate systems

### SURFACE_REF
- Outer Mold Line (OML) surfaces
- Inner Mold Line (IML) surfaces
- Loft surfaces
- Developed surfaces for manufacturing

## Usage

All CAD models in this subsystem must:
- Reference appropriate master geometry
- Use defined coordinate systems
- Align to master datums
- Conform to reference surfaces

## Version Control

Master geometry is critical and changes require:
- Change control board approval
- Impact assessment on dependent models
- Coordinated release with affected assemblies
- Communication to all stakeholders

## Related Documentation

- **Standards**: [`../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/`](../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/)
- **Configuration baseline**: [`../CONFIG/`](../CONFIG/)
- **Assembly models**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/)
- **Interface definitions**: [`../../CAI/INTERFACES/`](../../CAI/INTERFACES/)
