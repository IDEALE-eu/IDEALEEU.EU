# MEC - Mechanical, Systems, Modules Domain

## Navigation

- ⬆️ [Back to Q100_STD01 Family](../../README.md)
- 🏠 [Back to MODEL_IDENTIFICATION](../../../../../../../README.md)
- 🧭 [Navigation Index](../../../../../../../NAVIGATION_INDEX.md)
- 📋 [ATA-Domain Mapping](../ATA_DOMAIN_MAPPING.csv)

## Overview

This domain encompasses all systems related to:
- **Mechanical**: Mechanical systems and components
- **Systems**: Integrated mechanical systems
- **Modules**: Mechanical modules and assemblies

## ATA Chapters

This domain includes the following ATA chapters as **Primary Domain**:

### Mechanical Systems
- **ATA-27**: Flight Controls *(To be added)*
- **ATA-29**: Hydraulic Power *(To be added)*
- **ATA-32**: Landing Gear Systems *(To be added)*
- **ATA-36**: Pneumatic *(To be added)*
- **ATA-37**: Vacuum *(To be added)*
- **ATA-63**: Main Rotor Drive *(To be added)*
- **ATA-67**: Rotors Flight Control *(To be added)*
- **ATA-79**: Oil (Lubrication) *(To be added)*
- **ATA-83**: Accessory Gearboxes *(To be added)*

### Secondary Domain Involvement
- **ATA-24**: Electrical Power (with EEE, LCC, EDI)
- **ATA-49**: APU (with PPP, EEE, DDD)
- **ATA-52**: Doors (with AAA, EEE)
- **ATA-62**: Main Rotor (with AAA)
- **ATA-64**: Tail Rotor (with AAA)
- **ATA-65**: Tail Rotor Drive (with AAA)
- **ATA-71**: Power Plant (with PPP, EEE)
- **ATA-75**: Engine Bleed Air (with PPP, DDD)

## Scope

### Flight Controls
- Primary flight controls (mechanical)
- Control surface actuators
- Control linkages and cables
- Trim systems
- Feel systems

### Hydraulic Systems
- Hydraulic pumps and motors
- Hydraulic actuators
- Hydraulic reservoirs
- Hydraulic filters and accumulators
- Hydraulic fluid management

### Landing Gear
- Landing gear structures
- Landing gear actuation
- Braking systems
- Steering systems
- Wheels and tires

### Pneumatic Systems
- Bleed air systems
- Pneumatic actuation
- Pressure regulation
- Pneumatic distribution

### Lubrication Systems
- Oil systems
- Lubrication pumps
- Oil cooling and filtration
- Oil level monitoring

### Rotorcraft Systems (if applicable)
- Rotor systems
- Rotor drives and transmissions
- Rotor control systems

## Key Standards

- **CS-25/FAA Part 25**: Mechanical systems certification
- **CS-27/29**: Rotorcraft standards (if applicable)
- **SAE ARP**: Aerospace recommended practices
- **MIL-H-5606**: Hydraulic fluid specification
- **AS9100**: Quality management for aerospace
- **ATA Spec 100/iSpec 2200**: Maintenance documentation

## Interfaces

This domain interfaces with:
- **LCC**: Control system integration
- **EEE**: Electrical actuation and control
- **AAA**: Structural integration
- **PPP**: Engine mechanical interfaces
- **DDD**: Pneumatic interfaces

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
- Mechanical design requirements
- Certification requirements
- Safety requirements
- Test and verification records

---

**Domain Owner**: Mechanical Systems Engineering  
**Status**: Active  
**Last Updated**: 2025-10-13
