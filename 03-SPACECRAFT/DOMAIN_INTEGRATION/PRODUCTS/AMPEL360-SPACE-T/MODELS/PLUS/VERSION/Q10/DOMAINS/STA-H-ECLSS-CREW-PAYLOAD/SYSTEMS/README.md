# STA-H ECLSS, Crew & Payload Systems

## Overview

This directory contains systems for the STA-H domain (ECLSS, Crew & Payload Accommodation) for the AMPEL360-SPACE-T spacecraft. The domain consolidates chapters 25, 35, 36, 37, and 38 into a unified ECLSS system structure.

## Systems in This Domain

| System ID | System Name | Subsystems | Interface Matrix |
|-----------|-------------|------------|------------------|
| **25** | [ECLSS_CABIN_ENVIRONMENT](./25_ECLSS_CABIN_ENVIRONMENT/) | 9 | [CSV](./25_ECLSS_CABIN_ENVIRONMENT/INTERFACE_MATRIX/25↔06_15_21_24_26_33_40_42_51_93_97.csv) |

## System Breakdown

### 25 - ECLSS Cabin Environment

The Environmental Control and Life Support System provides habitable environment for crew and payload accommodation.

**Subsystems:**
- **25-10**: Atmosphere Control
- **25-20**: Pressure Regulation (formerly Ch. 35)
- **25-30**: CO₂ and Trace Gas Removal (formerly Ch. 36)
- **25-40**: Humidity Management (formerly Ch. 37)
- **25-50**: Water/Waste System (formerly Ch. 38)
- **25-60**: Fire Suppression Interfaces (with Ch. 26)
- **25-70**: Environmental Sensors
- **25-80**: Control Interfaces (with Ch. 42)
- **25-90**: Operations and Maintenance

**Key Interfaces:**
- STA-06: Dimensional constraints
- STA-15: Environmental safety
- STA-21: Thermal management
- STA-24: Power distribution
- STA-26: Fire suppression coordination
- STA-33: Communications
- STA-40: Avionics
- STA-42: Software control
- STA-51: Structural support
- STA-93: Data bus
- STA-97: Electrical harness

## Chapter Consolidation

The following chapters have been consolidated as subsystems under System 25:

| Legacy Chapter | New Subsystem | Description |
|----------------|---------------|-------------|
| Ch. 35 | 25-20 | Pressure Regulation |
| Ch. 36 | 25-30 | CO₂ and Trace Gas Removal |
| Ch. 37 | 25-40 | Humidity Management |
| Ch. 38 | 25-50 | Water/Waste System |

## Directory Structure

```
SYSTEMS/
├─ README.md (this file)
└─ 25_ECLSS_CABIN_ENVIRONMENT/
   ├─ README.md
   ├─ INTEGRATION_VIEW.md
   ├─ INTERFACE_MATRIX/
   │  └─ 25↔06_15_21_24_26_33_40_42_51_93_97.csv
   └─ SUBSYSTEMS/
      ├─ 25-10_ATMOSPHERE_CONTROL/
      ├─ 25-20_PRESSURE_REGULATION/
      ├─ 25-30_CO2_TRACE_GAS_REMOVAL/
      ├─ 25-40_HUMIDITY_MANAGEMENT/
      ├─ 25-50_WATER_WASTE_SYSTEM/
      ├─ 25-60_FIRE_SUPPRESSION_IF_26/
      ├─ 25-70_ENVIRONMENTAL_SENSORS/
      ├─ 25-80_CONTROL_INTERFACES_IF_42/
      └─ 25-90_OPERATIONS_MAINTENANCE/
         └─ PLM/
            ├─ EBOM_LINKS.md
            └─ CAx/
               ├─ CAD/
               ├─ CAE/
               ├─ CAM/
               ├─ CAI/
               ├─ CAV/
               ├─ CAP/
               ├─ CAS/
               └─ CMP/
```

## PLM/CAx Structure

All engineering artifacts are stored at the subsystem level under PLM/CAx following the unified architecture:

- **CAD**: Computer-Aided Design (3D models, drawings)
- **CAE**: Computer-Aided Engineering (FEA, analysis)
- **CAM**: Computer-Aided Manufacturing (NC programming, tooling)
- **CAI**: Computer-Aided Installation (installation procedures)
- **CAV**: Computer-Aided Validation (test models, validation data)
- **CAP**: Computer-Aided Planning (process planning)
- **CAS**: Computer-Aided Simulation (system simulations)
- **CMP**: Composite Materials Processing (layup data, curing)

## References

- Domain Configuration: [../domain-config.yaml](../domain-config.yaml)
- Domain README: [../README.md](../README.md)
- Domain Metadata: [../META.json](../META.json)
- Main Spacecraft README: [../../../../../../03-SPACECRAFT/00-README.md](../../../../../../03-SPACECRAFT/00-README.md)
