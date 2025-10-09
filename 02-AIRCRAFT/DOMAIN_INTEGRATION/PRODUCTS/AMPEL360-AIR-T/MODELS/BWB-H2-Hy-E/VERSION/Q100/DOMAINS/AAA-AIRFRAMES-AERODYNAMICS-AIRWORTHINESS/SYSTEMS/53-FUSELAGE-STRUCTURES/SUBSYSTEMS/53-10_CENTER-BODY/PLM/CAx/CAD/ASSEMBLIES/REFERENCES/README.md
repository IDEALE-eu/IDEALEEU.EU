# REFERENCES — Reference Geometry and Coordinate Systems

## Purpose

This directory contains reference geometry models including coordinate systems, reference planes, and datum features used for assembly alignment and interface definition.

## Contents

### Reference Categories
- **[COORDINATE_SYSTEMS/](./COORDINATE_SYSTEMS/)** — Coordinate system definitions
- **[PLANES/](./PLANES/)** — Reference planes and datum surfaces

## Reference Types

### Coordinate Systems
- Master coordinate system (MCS)
- Station reference systems
- Interface coordinate systems
- Tool and fixture references

### Reference Planes
- Fuselage reference plane (FRP)
- Buttock line planes (BL)
- Waterline planes (WL)
- Station planes (STA)

## Purpose and Usage

### Design Reference
- Establish common datum structure
- Define measurement origins
- Coordinate multi-disciplinary work
- Support interface management

### Manufacturing Reference
- Tooling alignment
- Assembly positioning
- Inspection datum
- Quality control reference

### Analysis Reference
- Coordinate system for FEA
- Load application points
- Boundary condition definition
- Results interpretation

## Naming Convention

Use the following pattern:
```
53-10_REF_<reference-type>_<identifier>_<version>.<ext>
```

Examples:
- `53-10_REF_CS_MASTER_v01.CATPart`
- `53-10_REF_PLANE_FRP_v01.prt`
- `53-10_REF_CS_WING-INTERFACE_v02.sldprt`

## Standards Compliance

Follow:
- **ATA iSpec 2200**: Aircraft coordinate system standards
- **ISO 1101**: Geometric dimensioning and tolerancing
- **ASME Y14.5**: GD&T standards
- **Internal standards**: Company-specific datum definitions

## Related Directories

- **Assembly models**: [`../TOP_LEVEL/`](../TOP_LEVEL/)
- **Installation**: [`../INSTALLATION/`](../INSTALLATION/)
- **CAE analysis**: [`../../../CAE/`](../../../CAE/)
