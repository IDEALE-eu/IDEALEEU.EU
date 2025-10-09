# ICD Index - CABINS_CARGO_PAX Domain

## Purpose

This document provides an index of all Interface Control Documents (ICDs) relevant to the CABINS_CARGO_PAX domain.

## ICD Management

All formal ICDs are managed through the program-level interface management system:

**Location**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`

## ICD Naming Convention

ICDs follow the naming convention:
- `ICD-[SOURCE_ATA]-[DEST_ATA]-[VERSION].pdf`
- Example: `ICD-25-24-1.2.pdf` (ATA-25 to ATA-24, version 1.2)

## Internal Interfaces (Within Domain)

### ATA-25 ↔ ATA-44
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-44-001 | Seats to IFE Physical Integration | Active | 1.0 |
| ICD-25-44-002 | PSU to CMS Control Signals | Active | 1.1 |
| ICD-25-44-003 | Seat Power Outlets Integration | Active | 1.0 |

### ATA-25 ↔ ATA-50
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-50-001 | Floor Structure Integration | Active | 1.0 |

### ATA-44 ↔ ATA-50
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-44-50-001 | Cargo Monitoring via CMS | Active | 1.0 |

## External Interfaces (Cross-Domain)

### ATA-25 External Interfaces

#### To ATA-21 (Air Conditioning)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-21-001 | Galley Ventilation Requirements | Active | 1.2 |
| ICD-25-21-002 | Lavatory Exhaust Interface | Active | 1.1 |
| ICD-25-21-003 | PSU Air Nozzle Control | Active | 1.0 |

#### To ATA-24 (Electrical Power)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-24-001 | Galley Power Distribution | Active | 1.3 |
| ICD-25-24-002 | Seat Power and USB Interface | Active | 1.1 |
| ICD-25-24-003 | PSU Power Requirements | Active | 1.0 |
| ICD-25-24-004 | Lavatory Power Interface | Active | 1.0 |

#### To ATA-26 (Fire Protection)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-26-001 | Lavatory Smoke Detection | Active | 1.2 |
| ICD-25-26-002 | Galley Fire Suppression | Active | 1.1 |
| ICD-25-26-003 | Emergency Equipment Storage | Active | 1.0 |

#### To ATA-33 (Lighting)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-33-001 | Cabin Reading Light Mounting | Active | 1.0 |
| ICD-25-33-002 | Galley Task Lighting | Active | 1.0 |
| ICD-25-33-003 | Emergency Floor Path Lighting | Active | 1.1 |

#### To ATA-35 (Oxygen)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-35-001 | PSU Oxygen Mask Deployment | Active | 1.2 |

#### To ATA-38 (Water/Waste)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-38-001 | Galley Water Supply | Active | 1.3 |
| ICD-25-38-002 | Lavatory Water/Waste Interface | Active | 1.2 |
| ICD-25-38-003 | Galley Grey Water Drainage | Active | 1.0 |

#### To ATA-51/52 (Structures)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-51-001 | Seat Track Attachment | Active | 1.4 |
| ICD-25-51-002 | Overhead Bin Mounting | Active | 1.2 |
| ICD-25-51-003 | Floor Panel Integration | Active | 1.1 |
| ICD-25-51-004 | Galley Monument Mounting | Active | 1.0 |

#### To ATA-92 (EWIS)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-25-92-001 | Floor Wire Routing Channels | Active | 1.0 |

---

### ATA-44 External Interfaces

#### To ATA-24 (Electrical Power)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-44-24-001 | CMS Server Power | Active | 1.1 |
| ICD-44-24-002 | IFE System Power Distribution | Active | 1.2 |
| ICD-44-24-003 | Network Equipment Power | Active | 1.0 |
| ICD-44-24-004 | Connectivity Equipment Power | Active | 1.0 |

#### To ATA-33 (Lighting)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-44-33-001 | CMS Lighting Control Interface | Active | 1.3 |

#### To ATA-42 (IMA)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-44-42-001 | CMS IMA Hosting Requirements | Active | 1.2 |
| ICD-44-42-002 | AFDX Network Integration | Active | 1.1 |

#### To ATA-92 (EWIS)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-44-92-001 | Cabin Network Cable Routing | Active | 1.0 |

---

### ATA-50 External Interfaces

#### To ATA-24 (Electrical Power)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-50-24-001 | PDU Motor Power | Active | 1.2 |
| ICD-50-24-002 | Control Electronics Power | Active | 1.0 |
| ICD-50-24-003 | Load Cell Power | Active | 1.0 |

#### To ATA-26 (Fire Protection)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-50-26-001 | Cargo Compartment Fire Detection | Active | 1.3 |

#### To ATA-31 (Indicating/Recording)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-50-31-001 | Weight & Balance Data Interface | Active | 1.2 |

#### To ATA-51/52 (Structures)
| ICD ID | Description | Status | Version |
|--------|-------------|--------|---------|
| ICD-50-51-001 | Cargo Floor Track Interface | Active | 1.4 |
| ICD-50-51-002 | ULD Lock Mounting Points | Active | 1.2 |

---

## ICD Status Definitions

- **Active**: Current, approved, in use
- **Draft**: Under development
- **Review**: Under review for approval
- **Superseded**: Replaced by newer version
- **Obsolete**: No longer applicable

## ICD Change Process

1. Interface Change Notice (ICN) initiated
2. Impact analysis performed
3. Affected parties notified and consulted
4. CCB review and approval (for critical interfaces)
5. ICD updated and new version released
6. Stakeholders notified of change

## ICD Access

Full ICD documents available at:
- **Primary Location**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- **System-Specific**: `CONFIGURATION_BASE/ATA-XX/ICD/`

## Related Documents

- [Domain Dependencies](../../02-ARCHITECTURE/DEPENDENCIES.md)
- [Interface Matrices](../../03-SYSTEMS/*/INTERFACE_MATRIX.md)
- [Change Rules](../../01-GOVERNANCE/CHANGE_RULES.md)

---

**Last Updated**: 2025-01-15
