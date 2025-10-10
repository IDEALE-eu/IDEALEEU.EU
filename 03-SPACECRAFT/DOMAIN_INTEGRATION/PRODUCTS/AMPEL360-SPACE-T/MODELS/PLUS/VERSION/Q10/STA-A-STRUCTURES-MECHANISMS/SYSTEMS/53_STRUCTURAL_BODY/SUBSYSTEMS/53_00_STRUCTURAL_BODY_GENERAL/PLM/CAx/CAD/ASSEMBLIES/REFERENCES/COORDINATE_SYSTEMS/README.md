# COORDINATE_SYSTEMS — Coordinate System Definitions

## Purpose

This directory contains coordinate system definition files for the 53_00 Structural Body subsystem.

## Contents

- Master coordinate system (MCS)
- Interface coordinate systems
- Station coordinate systems
- Tool and fixture coordinate systems

## Naming Convention

```
53_00_REF_CS_<identifier>_<version>.<ext>
```

Examples:
- `53_00_REF_CS_MASTER_v01.CATPart`
- `53_00_REF_CS_INTERFACE-PAYLOAD_v02.prt`

## Coordinate System Standards

### Spacecraft Coordinate System
- **X-axis**: Longitudinal, positive forward
- **Y-axis**: Lateral, positive right (starboard)
- **Z-axis**: Vertical, per spacecraft definition

## Related Directories

- **Reference planes**: [`../PLANES/`](../PLANES/)
- **Top-level assemblies**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)
