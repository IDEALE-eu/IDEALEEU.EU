# DATUMS — Primary Reference Datums

## Purpose

This directory contains definitions for the three primary reference datums (A, B, C) used for the 53-10 Center Body per ASME Y14.5 and ISO 1101 standards.

## Contents

### A/
Primary Datum A:
- Typically the primary mounting plane or mating surface
- Highest precedence in datum reference frame
- Controls primary orientation (e.g., pitch)
- Examples: Forward bulkhead plane, primary mounting surface

### B/
Secondary Datum B:
- Secondary reference feature
- Controls secondary orientation after Datum A (e.g., roll)
- Typically perpendicular to Datum A
- Examples: Centerline axis, vertical reference plane

### C/
Tertiary Datum C:
- Tertiary reference feature
- Completes the datum reference frame
- Controls final orientation (e.g., yaw) and position
- Examples: Side reference plane, locating pin/hole

## Datum Reference Frame (DRF)

The three datums establish a complete 6-DOF (degrees of freedom) reference:

```
Datum A: Controls 3 DOF (rotation about 2 axes + translation along 1 axis)
Datum B: Controls 2 DOF (rotation about 1 axis + translation along 1 axis)
Datum C: Controls 1 DOF (translation along 1 axis)
Total: 6 DOF fully constrained
```

## Naming Convention

```
53-10_DATUM_<letter>_<description>_v<version>.<ext>
```

Examples:
- `53-10_DATUM_A_FWD_BULKHEAD_v01.CATPart`
- `53-10_DATUM_B_CENTERLINE_v01.prt`
- `53-10_DATUM_C_SIDE_PLANE_v01.sldprt`

## Documentation Requirements

Each datum must include:
- Physical feature definition (plane, axis, point)
- Measurement method and verification procedure
- Tolerance zone specification
- Material condition modifiers (if applicable)
- Relation to aircraft global coordinate system
- Traceability to tooling datums

## Cross-References

- [Parent: COORDINATE_SYSTEMS](../README.md)
- [Global Systems](../GLOBAL/README.md)
- [Interface Control](../../../DOCS/INTERFACE_CONTROL/README.md)
- [GD&T Specifications](../../../../../../../06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-00_GENERAL/TOLERANCES_GDT.md)

## Standards

- **ASME Y14.5-2018**: Dimensioning and Tolerancing
- **ISO 1101:2017**: Geometrical Product Specifications (GPS)
- **ISO 5459:2011**: Geometrical tolerancing — Datums and datum systems

## Usage Guidelines

### Design Phase
- Establish datum features early in design
- Ensure datums are stable, accessible, and repeatable
- Design for manufacturing and inspection

### Manufacturing Phase
- Tooling and fixture design based on datums
- First article inspection verification
- Process capability studies

### Assembly Phase
- Alignment and positioning reference
- Mate verification
- Shimming and adjustment procedures

### Inspection Phase
- CMM setup and alignment
- Dimensional verification
- Acceptance criteria evaluation

---

**Owner**: 53-10 Center Body Chief Engineer  
**Approval**: Structures Engineering + Manufacturing Engineering  
**Criticality**: Critical — Foundation for all dimensional control  
**Change Control**: Requires ECR approval
