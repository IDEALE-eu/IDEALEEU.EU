# EEE - Electrical, Endotransponders, Circulation Domain

## Navigation

- ⬆️ [Back to Q100_STD01 Family](../../README.md)
- 🏠 [Back to MODEL_IDENTIFICATION](../../../../../../../README.md)
- 🧭 [Navigation Index](../../../../../../../NAVIGATION_INDEX.md)
- 📋 [ATA-Domain Mapping](../ATA_DOMAIN_MAPPING.csv)

## Overview

This domain encompasses all systems related to:
- **Electrical**: Electrical power generation and distribution
- **Endotransponders**: Electrical end devices and transponders
- **Circulation**: Electrical circulation and wiring systems

## ATA Chapters

This domain includes the following ATA chapters as **Primary Domain**:

### Electrical Systems
- **ATA-24**: Electrical Power *(To be added)*
- **ATA-33**: Lights *(To be added)*
- **ATA-39**: Electrical Panels *(To be added)*
- **ATA-74**: Ignition *(To be added)*
- **ATA-80**: Starting *(To be added)*
- **ATA-92**: EWIS (Wiring) - **AUTHORITATIVE** *(To be added)*

### Secondary Domain Involvement
- **ATA-25**: Equipment & Furnishings (with CCC, DDD)
- **ATA-26**: Fire Protection (with EER, LCC)
- **ATA-28**: Fuel (with PPP, DDD, EER)
- **ATA-29**: Hydraulic Power (with MEC)
- **ATA-30**: Ice & Rain Protection (with DDD, CCC)
- **ATA-31**: Indicating/Recording (with EDI, LCC)
- **ATA-32**: Landing Gear Systems (with MEC, LCC, EER)
- **ATA-34**: Navigation (with EDI, LCC)
- **ATA-35**: Oxygen (with CCC, EER)
- **ATA-36**: Pneumatic (with MEC, DDD)
- **ATA-38**: Water & Waste (with EER, CCC)
- **ATA-42**: Integrated Modular Avionics (with EDI, LCC)
- **ATA-43**: Cabin Systems (with CCC, LCC)
- **ATA-45**: Central Maintenance (with LCC, EDI)
- **ATA-46**: Information Systems (with IIS, EDI)
- **ATA-47**: Inert Gas/Cryo (with CQH, PPP)
- **ATA-49**: APU (with PPP, MEC, DDD)
- **ATA-52**: Doors (with AAA, MEC)
- **ATA-71**: Power Plant (with PPP, MEC)
- **ATA-72**: Engine (with PPP)
- **ATA-73**: Engine Fuel & Control (with PPP, LCC)
- **ATA-94**: E/E Compartments (with EDI)
- **ATA-97**: Reserved (Wiring aux) (with OOO)

## Scope

### Electrical Power
- Power generation (generators, batteries)
- Power distribution networks
- AC/DC power systems
- Emergency power systems
- Power management and control

### Wiring Systems (ATA-92)
- **AUTHORITATIVE domain for all wiring**
- Wire harness design
- Connector systems
- EWIS (Electrical Wiring Interconnection System)
- Wiring protection and routing
- Wire identification and labeling

### Electrical Devices
- Electrical actuators
- Electrical sensors
- Transponders
- External lighting systems
- Internal lighting systems

## Key Standards

- **CS-25/FAA Part 25**: Electrical systems certification
- **DO-160**: Environmental conditions for airborne equipment
- **AS50881**: Wiring aerospace vehicle
- **SAE AS50881**: Wiring and cabling requirements
- **EWIS Requirements**: Electrical Wiring Interconnection Systems
- **AS9100**: Quality management for aerospace
- **ATA Spec 100/iSpec 2200**: Maintenance documentation

## Interfaces

This domain interfaces with:
- **ALL domains**: Provides electrical power and wiring
- **EDI**: Electronic systems power supply
- **LCC**: Control system power
- **MEC**: Electrical actuation
- **PPP**: Engine electrical systems

## Organization

Each ATA chapter contains specific systems organized as:

```
ATA-{XX}/
└── SYSTEMS/
    └── ATA-{XX}-{YY}/
        ├── PLM/              # Product Lifecycle Management
        │   └── CAx/          # Computer-Aided tools
        └── CONF/             # Configuration management
            └── BASELINE/
                └── COMPONENTS/
```

## Special Note on ATA-92 (EWIS)

**ATA-92 is the AUTHORITATIVE chapter for all electrical wiring.** All wiring designs, installations, and modifications must be documented and controlled within this chapter, regardless of which system the wiring serves.

## Traceability

All systems maintain traceability to:
- System requirements
- Interface control documents (ICDs)
- Electrical load analysis
- Certification requirements
- EWIS requirements
- Safety requirements

---

**Domain Owner**: Electrical Systems Engineering  
**Status**: Active  
**Last Updated**: 2025-10-13
