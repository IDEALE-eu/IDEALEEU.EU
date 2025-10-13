# PPP - Propulsion Domain

## Navigation

- ⬆️ [Back to Q100_STD01 Family](../../README.md)
- 🏠 [Back to MODEL_IDENTIFICATION](../../../../../../../README.md)
- 🧭 [Navigation Index](../../../../../../../NAVIGATION_INDEX.md)
- 📋 [ATA-Domain Mapping](../ATA_DOMAIN_MAPPING.csv)

## Overview

This domain encompasses all systems related to:
- **Propulsion**: Propulsion systems and powerplants
- **Fuel Systems**: Fuel storage and distribution (including H₂)
- **Power Generation**: Primary and auxiliary power generation

## ATA Chapters

This domain includes the following ATA chapters as **Primary Domain**:

### Fuel Systems
- **ATA-28**: Fuel (incl. H₂) *(To be added)*

### Powerplant
- **ATA-49**: APU *(To be added)*
- **ATA-60**: Propeller—Practices *(To be added)*
- **ATA-61**: Propellers *(To be added)*
- **ATA-70**: Powerplant Practices *(To be added)*
- **ATA-71**: Power Plant *(To be added)*
- **ATA-72**: Engine *(To be added)*
- **ATA-73**: Engine Fuel & Control *(To be added)*
- **ATA-75**: Engine Bleed Air *(To be added)*
- **ATA-78**: Exhaust *(To be added)*
- **ATA-81**: Turbines (Aux) *(To be added)*
- **ATA-82**: Water Injection *(To be added)*

### Secondary Domain Involvement
- **ATA-47**: Inert Gas/Cryo (with CQH, EEE)
- **ATA-54**: Nacelles & Pylons (with AAA) - PPP for internals
- **ATA-74**: Ignition (with EEE)
- **ATA-76**: Engine Controls (with LCC)
- **ATA-77**: Engine Indicating (with EDI)
- **ATA-79**: Oil (Lubrication) (with MEC)
- **ATA-80**: Starting (with EEE)
- **ATA-83**: Accessory Gearboxes (with MEC)
- **ATA-84**: Propulsion Augmentation (with EDI)
- **ATA-85**: Emissions/Environmental (with EER)

## Scope

### Propulsion Systems
- Engine installation and integration
- Engine core and accessories
- Fan/compressor systems
- Turbine systems
- Electric motor propulsion (if applicable)
- Hybrid propulsion systems

### Fuel Systems
- Fuel tanks and bladders
- **Hydrogen (H₂) fuel systems** per regulatory requirements
- Fuel pumps and valves
- Fuel distribution and management
- Fuel quantity indication system (FQIS)
- Fuel management system (FMS)
- Inerting systems

### Engine Control
- Full Authority Digital Engine Control (FADEC)
- Engine control software (under ATA-73)
- Engine monitoring systems
- Thrust management

### Auxiliary Power
- Auxiliary Power Unit (APU)
- APU fuel systems
- APU starting and control
- Emergency power systems

### Exhaust & Emissions
- Exhaust systems
- Thrust reversers
- Noise reduction
- Emissions control

## Key Standards

- **CS-E/FAA Part 33**: Engine certification
- **SAE ARP 4754**: Development of civil aircraft systems
- **DO-178C**: Software (FADEC)
- **SAE AIR 7507**: Hydrogen-powered aircraft safety
- **ISO 14687**: Hydrogen fuel quality
- **EASA SC-HYDROGEN**: Special Condition for hydrogen
- **AS9100**: Quality management for aerospace
- **ATA Spec 100/iSpec 2200**: Maintenance documentation

## Interfaces

This domain interfaces with:
- **CQH**: Cryogenic hydrogen systems
- **EEE**: Electrical power and wiring
- **LCC**: Engine control systems
- **EDI**: Engine monitoring and indication
- **MEC**: Mechanical interfaces and lubrication
- **AAA**: Structural mounting and nacelles
- **EER**: Emissions and exhaust

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

## Special Considerations for H₂

This aircraft uses **hydrogen (H₂)** as fuel, which requires special attention:
- Hydrogen fuel systems under **ATA-28** (this domain)
- Cryogenic storage under **ATA-47** (CQH domain)
- Enhanced safety protocols
- Leak detection and mitigation
- Special materials and sealing

## Traceability

All systems maintain traceability to:
- System requirements
- Interface control documents (ICDs)
- Engine type certificate
- Certification requirements
- Safety requirements (FMEA/FHA)
- Test and verification records
- Hydrogen safety requirements

---

**Domain Owner**: Propulsion Systems Engineering  
**Status**: Active  
**Last Updated**: 2025-10-13
