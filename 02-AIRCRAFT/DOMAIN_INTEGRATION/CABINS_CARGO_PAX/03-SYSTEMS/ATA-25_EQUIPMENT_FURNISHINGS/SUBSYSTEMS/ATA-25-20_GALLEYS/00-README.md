# ATA-25-20 Galleys - Subsystem

## Overview

Aircraft galley systems including structures, equipment, and utility connections for food and beverage service.

## Scope

- Galley structures and monuments
- Galley equipment (ovens, coffee makers, refrigerators, etc.)
- Storage compartments (carts, drawers)
- Utility connections (power, water, waste)
- Safety equipment integration (fire suppression)

## PLM_CAX Directory Structure

Organized following standard PLM workflow:
- CAD, CAE, CAO, CAM, CAI, CAV, CAP, CAS, CMP, METADATA

## Key Interfaces

### Electrical (ATA-24)
- 115V AC, 400Hz for galley equipment
- Circuit protection per equipment
- Power budgets: Up to 20kW per galley

### Water/Waste (ATA-38)
- **Hot water supply**: 80-85°C, 2 GPM
- **Cold water supply**: 15-20°C, 2 GPM
- **Grey water drainage**: From sinks
- **Connection**: Quick-disconnect fittings

### Environmental Control (ATA-21)
- **Ventilation**: 200 CFM exhaust per galley
- **Odor management**: Activated carbon filters
- **Temperature control**: 18-24°C ambient

### Fire Protection (ATA-26)
- Automatic fire suppression in galley areas
- Smoke detection
- Portable fire extinguisher stowage

## INTERFACES.md

Detailed interface specifications in: `./INTERFACES.md`

## TESTS/

- Equipment functional testing
- Electrical load testing
- Water pressure and flow testing
- Fire suppression system testing
- Environmental testing

## Configuration Reference

- [ATA-25 Configuration Base](../../../../../CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/)

---

**Last Updated**: 2025-01-15
