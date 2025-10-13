# LCC - Linkages, Control, Communications Domain

## Navigation

- ⬆️ [Back to Q100_STD01 Family](../../README.md)
- 🏠 [Back to MODEL_IDENTIFICATION](../../../../../../../README.md)
- 🧭 [Navigation Index](../../../../../../../NAVIGATION_INDEX.md)
- 📋 [ATA-Domain Mapping](../ATA_DOMAIN_MAPPING.csv)

## Overview

This domain encompasses all systems related to:
- **Linkages**: Mechanical and data linkages
- **Control**: Control systems and automation
- **Communications**: Communication systems

## ATA Chapters

This domain includes the following ATA chapters as **Primary Domain**:

### Control & Communications
- **ATA-08**: Leveling/Weighing *(To be added)*
- **ATA-22**: Auto Flight *(To be added)*
- **ATA-23**: Communications *(To be added)*
- **ATA-44**: Cabin Control *(To be added)*
- **ATA-45**: Central Maintenance *(To be added)*
- **ATA-76**: Engine Controls *(To be added)*
- **ATA-93**: Central Control Systems *(To be added)*

### Secondary Domain Involvement
- **ATA-24**: Electrical Power (with EEE, EDI, MEC)
- **ATA-26**: Fire Protection (with EER, EEE)
- **ATA-27**: Flight Controls (with MEC)
- **ATA-31**: Indicating/Recording (with EDI, EEE)
- **ATA-32**: Landing Gear Systems (with MEC, EEE, EER)
- **ATA-34**: Navigation (with EDI, EEE)
- **ATA-42**: Integrated Modular Avionics (with EDI, EEE)
- **ATA-43**: Cabin Systems (with CCC, EEE)
- **ATA-67**: Rotors Flight Control (with MEC)
- **ATA-73**: Engine Fuel & Control (with PPP, EEE)

## Scope

### Control Systems
- Flight control systems coordination
- Autopilot systems (AFCS)
- Auto-throttle systems
- Central maintenance system (CMS)
- Aircraft condition monitoring system (ACMS)
- Health monitoring systems
- Central control and coordination

### Communications
- VHF/HF radio communications
- SATCOM systems
- Datalink systems (ACARS, CPDLC)
- Interphone systems
- Passenger address systems
- Cockpit voice recorder interfaces

### Linkages & Integration
- System integration and coordination
- Data bus management
- Control law implementation
- System health management
- Fault management

## Key Standards

- **DO-178C**: Software considerations in airborne systems
- **DO-254**: Hardware considerations (control electronics)
- **ARINC 429/664**: Avionics data bus standards
- **RTCA DO-160**: Environmental conditions
- **CS-25/FAA Part 25**: Control systems certification
- **AS9100**: Quality management for aerospace
- **ATA Spec 100/iSpec 2200**: Maintenance documentation

## Interfaces

This domain interfaces with:
- **EDI**: Digital control systems and avionics
- **EEE**: Electrical control systems
- **MEC**: Mechanical control systems
- **CCC**: Cabin control systems
- **PPP**: Engine control systems
- **All domains**: System control and coordination

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

## Traceability

All systems maintain traceability to:
- System requirements
- Interface control documents (ICDs)
- Control law requirements
- Certification requirements (DO-178C, DO-254)
- Safety requirements
- Communication standards

---

**Domain Owner**: Control Systems Engineering  
**Status**: Active  
**Last Updated**: 2025-10-13
