# CABINS_CARGO_PAX - Domain Integration

Cabin interior, cargo systems, and passenger experience integration.

## Overview

This domain integrates all cabin-related systems, cargo handling systems, and passenger experience components across the aircraft. It covers ATA-25 (Equipment & Furnishings), ATA-44 (Cabin Systems), and ATA-50 (Cargo & Load Systems).

## Scope

- **Cabin Interior**: Seats, galleys, lavatories, trims, overhead bins, floors, PSUs
- **Cabin Systems**: CMS, IFE, cabin network, connectivity, passenger power, lighting
- **Cargo Systems**: Main deck, lower deck, ULDs, locks, PDUs, load sensing, control electronics
- **Passenger Experience**: End-to-end passenger journey systems and interfaces

## Directory Structure

```
CABINS_CARGO_PAX/
├── 00-README.md                    # This file
├── 01-GOVERNANCE/                  # Policies, boundaries, and change rules
├── 02-ARCHITECTURE/                # Domain context, dependencies, data contracts
├── 03-SYSTEMS/                     # ATA chapters with subsystems and PLM artifacts
├── 04-VERIFICATION/                # Verification and validation plans
├── 05-LINKS/                       # Cross-references to config base and ICDs
├── 06-METRICS/                     # KPIs and performance metrics
└── 07-TEMPLATES/                   # Standard templates for integration work
```

## Key Principles

1. **Reference, Don't Copy**: This domain references ATA chapter configurations in CONFIGURATION_BASE rather than duplicating them
2. **Integration Focus**: Emphasizes cross-system interfaces and integration views
3. **PLM-Centric**: All design artifacts managed through PLM with neutral exports (STEP AP242, JT, QIF)
4. **Interface Management**: Clear interface matrices linking to external systems (power, ECS, fire, water, etc.)

## Key External Interfaces

- **ATA-21**: Environmental Control System (ventilation, temperature)
- **ATA-24**: Electrical Power (power distribution to cabin systems)
- **ATA-26**: Fire Protection (fire detection and suppression)
- **ATA-33**: Lighting (cabin lighting integration)
- **ATA-38**: Water/Waste (water supply and grey water systems)
- **ATA-42**: IMA Platform (hosted applications)

## Related Documents

- [Configuration Rules](../../CONFIGURATION_BASE/00-COMMON/RULES.md)
- [Interface Management](../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [ATA-25 Configuration](../../CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/)
- [ATA-44 Configuration](../../CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/)
- [ATA-50 Configuration](../../CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/)

## Contacts

- **Domain Owner**: Cabin & Cargo Engineering
- **Integration Lead**: Systems Integration
- **Configuration Management**: CM Team

---

**Last Updated**: 2025-01-15
