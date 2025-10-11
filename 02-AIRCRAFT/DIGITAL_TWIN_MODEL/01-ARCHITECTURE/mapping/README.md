# mapping

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > [01-ARCHITECTURE](../) > mapping**

Signal and coordinate system mappings for digital twin data integration.

## Purpose

This directory contains mapping definitions between physical signals, digital twin variables, and coordinate systems.

## Contents

- **[signal_map.csv](signal_map.csv)** - Mapping between aircraft signals and twin variables
- **[coord_map.csv](coord_map.csv)** - Coordinate system transformations and mappings

## Signal Mapping

Maps physical sensor signals to digital twin model variables:
- Sensor IDs → Model inputs
- Controller outputs → Actuator commands
- Telemetry parameters → Twin state variables

## Coordinate Mapping

Defines transformations between coordinate frames:
- Body frame ↔ Wind frame
- Body frame ↔ Earth frame
- Local NED ↔ ECEF (Earth-Centered Earth-Fixed)
- Sensor frames → Aircraft body frame

## Related Documents

- **[../coords/](../coords/)** - Coordinate frame definitions
- **[../interfaces/](../interfaces/)** - Interface control documents
- **[../../03-INTERFACES_APIS/](../../03-INTERFACES_APIS/)** - API definitions

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Integration Team | Initial signal and coordinate mappings |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
