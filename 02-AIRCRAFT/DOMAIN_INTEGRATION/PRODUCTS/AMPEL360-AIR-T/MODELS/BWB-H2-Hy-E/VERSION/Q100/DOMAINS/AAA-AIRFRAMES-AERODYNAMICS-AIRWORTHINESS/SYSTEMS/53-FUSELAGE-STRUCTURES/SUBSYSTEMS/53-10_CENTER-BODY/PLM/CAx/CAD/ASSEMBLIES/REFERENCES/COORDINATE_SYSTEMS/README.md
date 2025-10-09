# COORDINATE_SYSTEMS — Coordinate System Definitions

## Purpose

This directory contains CAD models defining coordinate systems used throughout the 53-10 Center Body design, manufacturing, and analysis activities.

## Contents

### Coordinate System Types
- **Master Coordinate System (MCS)**: Primary aircraft reference
- **Station Coordinate Systems**: Local references at key stations
- **Interface Coordinate Systems**: Attachment and mating point references
- **Tooling Coordinate Systems**: Manufacturing and assembly references

## Coordinate System Hierarchy

### Aircraft Master Coordinate System (MCS)
```
Origin: Aircraft nose reference point
X-axis: Longitudinal (nose to tail, positive aft)
Y-axis: Lateral (left to right, positive starboard)
Z-axis: Vertical (bottom to top, positive up)
```

### Center Body Local Coordinate System
```
Origin: Center body datum point (typically forward attachment)
Aligned with aircraft MCS
Offset documented in interface control document
```

### Interface Coordinate Systems
- Wing-to-body attachment points
- Door frame interfaces
- Bulkhead interfaces
- Equipment mounting points

## Naming Convention

Use the following pattern:
```
53-10_REF_CS_<location>_<purpose>_<version>.<ext>
```

Examples:
- `53-10_REF_CS_MASTER_v01.CATPart`
- `53-10_REF_CS_STA-500_v01.prt`
- `53-10_REF_CS_WING-ATTACH-LEFT_v02.sldprt`
- `53-10_REF_CS_DOOR-FRAME-FWD_v01.CATPart`

## Coordinate System Definition

Each coordinate system should specify:
- Origin location (X, Y, Z in parent coordinate system)
- Axis orientations
- Reference features for establishment
- Tolerance requirements
- Traceability to master datum

## Usage Guidelines

### Design
- Use for component positioning
- Define assembly relationships
- Establish interface requirements

### Manufacturing
- Tooling alignment reference
- Inspection setup
- Assembly positioning

### Analysis
- FEA model setup
- Load application
- Boundary conditions

## Documentation Requirements

Each coordinate system must include:
- Definition document (origin, axes)
- Parent coordinate system reference
- Transformation matrix (if applicable)
- Usage instructions
- Approval and revision history

## Standards

Follow:
- **ATA iSpec 2200**: Aircraft coordinate system conventions
- **ISO 1101**: Geometric product specifications
- **ASME Y14.5**: Dimensioning and tolerancing

## Related Directories

- **Reference planes**: [`../PLANES/`](../PLANES/)
- **Assembly models**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)
- **Interface control**: [`../../DOCS/INTERFACE_CONTROL/`](../../DOCS/INTERFACE_CONTROL/)
