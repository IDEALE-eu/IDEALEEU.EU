# coords

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > [01-ARCHITECTURE](../) > coords**

Coordinate system definitions and transformations.

## Purpose

This directory contains definitions of coordinate frames used in the digital twin and transformation matrices between them.

## Contents

- **[frames.yaml](frames.yaml)** - Coordinate frame definitions
- **[transforms/](transforms/)** - Transformation matrices and quaternions
  - **[body_to_wind.yaml](transforms/body_to_wind.yaml)** - Body to wind frame transformation
  - **[body_to_earth.yaml](transforms/body_to_earth.yaml)** - Body to Earth (NED) frame transformation

## Coordinate Frames

### Body Frame
- Origin: Aircraft center of gravity
- X-axis: Forward (nose direction)
- Y-axis: Right wing
- Z-axis: Down

### Wind Frame
- X-axis: Along relative wind (airspeed vector)
- Y-axis: Right, perpendicular to relative wind
- Z-axis: Down, completing right-hand system

### Earth Frame (NED)
- Origin: Local reference point
- X-axis: North
- Y-axis: East
- Z-axis: Down

### ECEF Frame
- Origin: Earth center of mass
- X-axis: Through equator at prime meridian
- Y-axis: Through equator at 90°E
- Z-axis: Through North Pole

## Related Documents

- **[../mapping/coord_map.csv](../mapping/coord_map.csv)** - Coordinate transformation mappings
- **[../../02-MODELS/PHYSICS/](../../02-MODELS/PHYSICS/)** - Physics models using these frames

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Dynamics Team | Initial coordinate frame definitions |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
