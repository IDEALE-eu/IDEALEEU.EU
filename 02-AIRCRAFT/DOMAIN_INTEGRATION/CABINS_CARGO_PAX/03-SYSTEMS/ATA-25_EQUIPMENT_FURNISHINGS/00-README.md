# ATA-25 Equipment & Furnishings - Integration View

## Overview

This directory contains the integration view for ATA-25 Equipment & Furnishings within the CABINS_CARGO_PAX domain. It provides a holistic view of how furnishing subsystems integrate together and with other aircraft systems.

## Purpose

The integration view:
- Assembles all subsystem designs into a master assembly
- Defines layout arrangements and configurations
- Produces neutral file exports for cross-platform collaboration
- Generates integration reports and analyses

## Contents

### MASTER_ASSEMBLY/
Master assembly models integrating all ATA-25 subsystems:
- Complete cabin furnishing assembly
- Structural integration points
- Interface mounting locations
- Zone assignments

### LAYOUTS/
Cabin layout configurations:
- Seat maps and arrangements
- Galley and lavatory positioning
- Overhead bin locations
- Emergency equipment placement
- Passenger flow and egress paths

### NEUTRAL_EXPORTS/
Format-neutral exports for interoperability:

#### STEP_AP242/
- ISO 10303-242 (STEP AP242) files
- Includes geometry, PMI, and metadata
- Industry-standard 3D model exchange

#### JT/
- JT (Jupiter Tessellation) format
- Lightweight visualization
- PLM system integration

#### QIF/
- Quality Information Framework files
- Inspection and quality data
- Measurement results

### REPORTS/
Integration analysis and reports:
- Weight and balance analysis
- Clearance and interference checks
- Installation sequence planning
- Bill of materials (BOM)
- Configuration reports

## Integration Workflow

```
1. Subsystem Design (in PLM_CAX directories)
   ↓
2. Master Assembly Integration
   ↓
3. Layout Definition and Optimization
   ↓
4. Interference and Clearance Analysis
   ↓
5. Neutral File Export Generation
   ↓
6. Integration Report Generation
   ↓
7. Review and Approval
```

## Key Integration Points

### Internal (within ATA-25)
- Seat to floor attachment
- Overhead bins to fuselage structure
- PSU to ceiling structure
- Galley to floor and utilities
- Lavatory to floor and utilities

### External (to other systems)
- Floor structure to airframe (ATA-51/52)
- Power connections to electrical system (ATA-24)
- Water/waste to plumbing system (ATA-38)
- Ventilation to ECS (ATA-21)
- Fire detection integration (ATA-26)

## Configuration Management

All integration views are version controlled and baseline controlled:
- Master assembly revisions tracked
- Layout configurations baselined
- Export file versions managed
- Reports archived with configuration ID

## Subsystems Integrated

- ATA-25-10: Seats
- ATA-25-20: Galleys
- ATA-25-30: Lavatories
- ATA-25-40: Trims & Linings
- ATA-25-50: Overhead Bins
- ATA-25-60: Floors
- ATA-25-70: Passenger Service Units (PSU)
- ATA-25-80: Emergency Equipment

## References

- [ATA-25 Configuration Baseline](../../../../CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/)
- [Interface Matrix](../INTERFACE_MATRIX.md)
- [Subsystem Designs](../SUBSYSTEMS/)
- [Domain Architecture](../../../02-ARCHITECTURE/)

---

**Last Updated**: 2025-01-15
