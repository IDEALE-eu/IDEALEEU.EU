# GLOBAL — Global Reference Coordinate Systems

## Purpose

This directory contains definitions for global aircraft reference coordinate systems used across the entire BWB-H2-Hy-E aircraft program.

## Contents

### AIRCRAFT_BODY/
Aircraft body-fixed coordinate system definitions:
- Origin at aircraft reference point
- X-axis: Longitudinal (positive aft)
- Y-axis: Lateral (positive starboard/right)
- Z-axis: Vertical (positive up)
- Standard aircraft body axes per ATA iSpec 2200

### AIRCRAFT_WIND/
Wind-axis coordinate system definitions for aerodynamic analysis:
- Aligned with relative wind direction
- Used for aerodynamic force and moment decomposition
- Transformation matrices from body axes

### AERODYNAMIC/
Aerodynamic reference coordinate systems:
- Stability axes
- Principal axes
- Flight path axes
- Transformations for various flight conditions

## Cross-References

- [Parent: COORDINATE_SYSTEMS](../README.md)
- [Global Datums: ATA-06-10](../../../../../../../06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-10_GLOBAL_DATUMS_COORDINATES/README.md)
- [CAD Templates](../../../TEMPLATES/README.md)

## Standards

- **ATA iSpec 2200**: Aircraft coordinate system conventions
- **ISO 1151-1**: Flight dynamics coordinate systems
- **AIAA S-119**: Recommended practice for aerodynamic coordinate systems

## Usage

All aircraft-level components, assemblies, and analyses must reference these global coordinate systems as their primary datum.

---

**Owner**: 06-DIMENSIONS-STATIONS / 53-10 Integration  
**Status**: Active  
**Criticality**: High — Program-wide reference
