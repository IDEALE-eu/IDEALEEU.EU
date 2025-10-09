# EBOM Links - Engineering Bill of Materials

## Overview

This document provides links to the Engineering Bill of Materials (EBOM) for the 48-10_PRIMARY subsystem in the PLM system.

## EBOM Structure

```
48-10_PRIMARY
├── Assembly Level 1
│   ├── Component 1.1
│   ├── Component 1.2
│   └── Subassembly 1.3
│       ├── Component 1.3.1
│       └── Component 1.3.2
└── Assembly Level 2
    ├── Component 2.1
    └── Component 2.2
```

## Part Numbers

| Item | Part Number | Description | Quantity | Source |
|------|-------------|-------------|----------|--------|
| 1 | TBD-XXXX-001 | Primary Assembly | 1 | Make |
| 1.1 | TBD-XXXX-101 | Component A | 2 | Buy |
| 1.2 | TBD-XXXX-102 | Component B | 1 | Make |
| 2 | TBD-XXXX-002 | Secondary Assembly | 1 | Make |

## PLM Links

**PLM System URL:** [Link to PLM workspace/project]

- **Top Assembly:** [PLM Link]
- **3D Model:** [PLM Link]
- **Drawings Package:** [PLM Link]
- **Specification:** [PLM Link]

## Interface Components

Components that interface with other systems:

| Part Number | Description | Interface To | ICD Reference |
|-------------|-------------|--------------|---------------|
| TBD-XXXX-501 | Power Connector | ATA-24 | ICD-XX-24-001 |
| TBD-XXXX-502 | Data Connector | ATA-42 | ICD-XX-42-001 |

## Configuration Control

- **Baseline:** V1.0
- **Change Control:** Per ECR/ECO process (00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- **Approval Authority:** CCB

## References

- Part Numbering: [00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md](../../../../../../../../../../00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md)
- PLM Integration: [00-PROGRAM/INDUSTRIALISATION/16-IT_INTEGRATION/PLM_LINKS/](../../../../../../../../../../00-PROGRAM/INDUSTRIALISATION/16-IT_INTEGRATION/PLM_LINKS/)
- Item Master: [00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/](../../../../../../../../../../00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/)

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-09 | Configuration Management | Initial EBOM structure |
