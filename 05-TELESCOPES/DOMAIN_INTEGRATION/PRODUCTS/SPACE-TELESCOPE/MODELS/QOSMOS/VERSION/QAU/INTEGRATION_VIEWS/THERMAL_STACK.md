# Thermal Stack Integration View

**Systems:** 21/72/75 ↔ 51/53

## Overview

This integration view describes the thermal control architecture including:
- Active thermal control systems (System 21)
- Cryogenic cooling (System 72)
- Thermal radiators (System 75)
- Structural thermal interfaces (Systems 51, 53)

## Interface Summary

| From System | To System | Interface Type | Description |
|-------------|-----------|----------------|-------------|
| 21-THERMAL_CONTROL | 51-PRIMARY_STRUCTURE | Mechanical/Thermal | Heater mounting and conduction |
| 21-THERMAL_CONTROL | 53-OPTICAL_TUBE_ASSEMBLY | Mechanical/Thermal | Tube thermal control |
| 72-CRYOGENIC_COOLING | 51-PRIMARY_STRUCTURE | Mechanical/Thermal | Cryo system mounting |
| 75-THERMAL_RADIATORS | 51-PRIMARY_STRUCTURE | Mechanical | Radiator mounting |
| 21-THERMAL_CONTROL | 72-CRYOGENIC_COOLING | Thermal/Electrical | Temperature monitoring |

## Thermal Budget

TBD - To be populated during thermal analysis.

## References

- Interface matrices in `/INTERFACE_MATRIX/`
- Thermal models: System-level thermal analysis
- ICDs: `../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
