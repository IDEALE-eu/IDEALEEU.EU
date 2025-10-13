# EDI - Electronics, Digital, Instruments Domain

## Navigation

- ⬆️ [Back to Q100_STD01 Family](../../README.md)
- 🏠 [Back to MODEL_IDENTIFICATION](../../../../../../../README.md)
- 🧭 [Navigation Index](../../../../../../../NAVIGATION_INDEX.md)
- 📋 [ATA-Domain Mapping](../ATA_DOMAIN_MAPPING.csv)

## Overview

This domain encompasses all systems related to:
- **Electronics**: Electronic systems and components
- **Digital**: Digital processing and computing
- **Instruments**: Instrumentation and sensors

## ATA Chapters

This domain includes the following ATA chapters as **Primary Domain**:

### Avionics & Instrumentation
- **ATA-31**: Indicating/Recording *(To be added)*
- **ATA-34**: Navigation (Avionics) *(To be added)*
- **ATA-42**: Integrated Modular Avionics *(To be added)*
- **ATA-77**: Engine Indicating *(To be added)*
- **ATA-84**: Propulsion Augmentation *(To be added)*
- **ATA-91**: Charts/Performance *(To be added)*
- **ATA-94**: E/E Compartments *(To be added)*

### Secondary Domain Involvement
- **ATA-22**: Auto Flight (with LCC)
- **ATA-23**: Communications (with LCC)
- **ATA-24**: Electrical Power (with EEE, LCC, MEC)
- **ATA-40**: Avionics Std/General (with OOO)
- **ATA-45**: Central Maintenance (with LCC, EEE)
- **ATA-46**: Information Systems (with IIS, EEE)
- **ATA-48**: Optical/Video (with OOO)
- **ATA-87**: Radiation Effects/Shielding (with OOO, EER)
- **ATA-93**: Central Control Systems (with LCC)

## Scope

### Electronic Systems
- Electronic hardware design
- Circuit board assemblies
- Electronic interfaces
- EMI/EMC compliance

### Digital Systems
- Digital processors and computers
- Software integration points
- Data processing systems
- Digital communication protocols

### Instrumentation
- Flight instruments
- Engine instruments
- Navigation sensors
- Data recorders (FDR, CVR)
- Health monitoring sensors

## Key Standards

- **DO-178C**: Software considerations in airborne systems
- **DO-254**: Hardware considerations in airborne systems
- **DO-160**: Environmental conditions and test procedures
- **ARINC 429/664/653**: Avionics data bus standards
- **AS9100**: Quality management for aerospace
- **ATA Spec 100/iSpec 2200**: Maintenance documentation

## Interfaces

This domain interfaces with:
- **LCC**: Control systems and communications
- **EEE**: Electrical power distribution
- **IIS**: Information systems
- **PPP**: Engine monitoring and control
- **OOO**: Platform standards

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
- Certification requirements (DO-178C, DO-254)
- Software/hardware development standards
- Test and verification records

---

**Domain Owner**: Avionics & Digital Systems Engineering  
**Status**: Active  
**Last Updated**: 2025-10-13
