# ICD Links - Interface Control Documents

## Overview

This document provides links to Interface Control Documents (ICDs) managed in the program-level configuration management repository. All ICDs referenced in this domain integration are maintained centrally.

## ICD Repository

**Location**: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/](../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)

All Interface Control Documents (ICDs) are maintained in the program-level configuration management repository to ensure:
- Single source of truth for all interfaces
- Consistent change control process
- Traceability across domains
- Configuration baseline management

## Domain Interface Matrix

The complete interface matrix for this domain is maintained in:
- **[INTERFACE_MATRIX.csv](INTERFACE_MATRIX.csv)** - All interfaces in this domain

Individual system-level interface matrices:
- **[01-SYSTEMS/ATA-21_AIR_CONDITIONING/INTERFACE_MATRIX/](../01-SYSTEMS/ATA-21_AIR_CONDITIONING/INTERFACE_MATRIX/)** - ATA-21 interfaces
- **[01-SYSTEMS/ATA-28_FUEL_H2/INTERFACE_MATRIX/](../01-SYSTEMS/ATA-28_FUEL_H2/INTERFACE_MATRIX/)** - ATA-28 interfaces
- **[01-SYSTEMS/ATA-38_WATER_WASTE/INTERFACE_MATRIX/](../01-SYSTEMS/ATA-38_WATER_WASTE/INTERFACE_MATRIX/)** - ATA-38 interfaces
- **[01-SYSTEMS/MTL-CIRCULARITY/INTERFACE_MATRIX/](../01-SYSTEMS/MTL-CIRCULARITY/INTERFACE_MATRIX/)** - MTL interfaces

## Critical Interfaces

### ATA-21 Air Conditioning
| ICD ID | From System | To System | Criticality | Status |
|--------|-------------|-----------|-------------|--------|
| ICD-21-24-002 | ATA-21 Pack Motors | ATA-24 Power | Critical | Draft |
| ICD-21-36-001 | ATA-36 Bleed Air | ATA-21 Pack | Critical | Draft |
| ICD-21-28-001 | ATA-21 Heat Exchanger | ATA-28 H2 Tank | High | Draft |

### ATA-28 Fuel/H₂
| ICD ID | From System | To System | Criticality | Status |
|--------|-------------|-----------|-------------|--------|
| ICD-28-24-001 | ATA-28 BOP Controller | ATA-24 Power | Critical | Draft |
| ICD-28-24-002 | ATA-28 Transfer Pump | ATA-24 Power | Critical | Draft |
| ICD-28-92-001 | ATA-28 BOP Controller | ATA-92 EWIS | Critical | Draft |

### ATA-38 Water/Waste
| ICD ID | From System | To System | Criticality | Status |
|--------|-------------|-----------|-------------|--------|
| ICD-38-25-001 | ATA-38 Potable Water | ATA-25 Galleys | Medium | Draft |
| ICD-38-25-002 | ATA-38 Potable Water | ATA-25 Lavatories | Medium | Draft |

### MTL-CIRCULARITY
| ICD ID | From System | To System | Criticality | Status |
|--------|-------------|-----------|-------------|--------|
| ICD-MTL-51-001 | MTL Material Passport | ATA-51 Primary Structure | High | Draft |
| ICD-MTL-53-001 | MTL Material Passport | ATA-53 Fuselage | High | Draft |
| ICD-MTL-57-001 | MTL Material Passport | ATA-57 Wings | High | Draft |

## ICD Change Control

Changes to ICDs follow the program change management process:

1. **ECR Submission**: [00-PROGRAM/CONFIG_MGMT/06-CHANGES/](../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
2. **Impact Analysis**: Assess affected systems and domain integration
3. **CCB Review**: Configuration Control Board approval
4. **Baseline Update**: Update configuration baseline
5. **Notification**: Notify affected parties via RASCI matrix

See [00-PROGRAM/CONFIG_MGMT/06-CHANGES/01-POLICY/](../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/01-POLICY/) for detailed change control procedures.

## Traceability

### MBSE Integration
- Interface requirements allocated in SysML model
- Auto-generated ICDs from MBSE model (planned)
- See [04-DIGITAL_THREAD/MBSE_BINDINGS.md](../04-DIGITAL_THREAD/MBSE_BINDINGS.md)

### Requirements Traceability
- System requirements ↔ Interface requirements
- Interface requirements ↔ ICDs
- ICDs ↔ Test cases

## Interface Validation

### Verification Methods
- **Analysis**: Calculations, simulations
- **Inspection**: Design review, documentation review
- **Test**: Component testing, integration testing
- **Demonstration**: Prototype demonstration

See [05-VERIFICATION/VVP_PLAN.md](../05-VERIFICATION/VVP_PLAN.md) for verification planning.

## Related Documents

- [02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/01-ARCHITECTURE_END2END/INTERFACE_MATRIX/](../../CROSS_SYSTEM_INTEGRATION/01-ARCHITECTURE_END2END/INTERFACE_MATRIX/) - Cross-system interfaces
- [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD_INDEX.md](../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD_INDEX.md) - Master ICD catalog
- [00-README.md](../00-README.md) - Domain overview and RASCI

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-12-XX | Domain Integration Team | Initial ICD links for CIRCULAR_SYSTEMS_MATERIALS |
