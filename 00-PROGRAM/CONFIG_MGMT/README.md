# Configuration Management (CONFIG_MGMT)

## Quick Start

This directory contains the complete configuration management system for the IDEALE EU aerospace program. For detailed information, see **00-README.md**.

## Directory Structure

```
CONFIG_MGMT/
├── 00-README.md                  # Overview and introduction
├── 01-CM_PLAN.md                 # Configuration Management Plan
├── 02-PART_NUMBERING.md          # Part numbering system
├── 03-SERIALIZATION.md           # Serialization guidelines
├── 04-BASELINES/                 # Stage gate baselines
│   ├── SRR/                      # System Requirements Review
│   ├── PDR/                      # Preliminary Design Review
│   ├── CDR/                      # Critical Design Review
│   ├── TRR/                      # Test Readiness Review
│   ├── PRR/                      # Production Readiness Review
│   ├── ORR_EIS/                  # Operational Readiness Review
│   └── FRR/                      # Flight Readiness Review
├── 05-CCB/                       # Configuration Control Board
│   ├── 00-CHARTER.md             # CCB charter
│   ├── 01-MEMBERS.md             # CCB membership
│   └── 02-MINUTES/               # Meeting minutes
├── 06-CHANGES/                   # Change management
│   ├── ECR/                      # Engineering Change Requests
│   ├── ECO/                      # Engineering Change Orders
│   ├── DEVIATIONS/               # Deviation requests
│   └── WAIVERS/                  # Waiver requests
├── 07-RELEASES/                  # Release packages
│   ├── AIRCRAFT/                 # Aircraft releases
│   └── SPACECRAFT/               # Spacecraft releases
├── 08-ITEM_MASTER/               # Configuration items
│   ├── ITEMS.csv                 # Item master list
│   └── ATTRIBUTES.yaml           # Item attribute schema
├── 09-INTERFACES/                # Interface control
│   ├── ICD_INDEX.md              # ICD index
│   └── ICD-XXXX.md               # ICD template
├── 10-TRACEABILITY/              # Traceability
│   ├── REQ_ITEM.csv              # Requirements to items
│   ├── CHANGE_BASELINE.csv       # Changes to baselines
│   └── UTCS_THREADS/             # Use case test system threads
├── 11-AUDITS/                    # Configuration audits
│   ├── CONFIG_AUDIT_CA.md        # Configuration audit procedures
│   └── FUNCTIONAL_AUDIT_FA.md    # Functional audit procedures
├── 12-CI_CD_RULES/               # CI/CD integration
│   ├── CODEOWNERS                # Code ownership
│   ├── BRANCHING_MODEL.md        # Git branching strategy
│   ├── TAGGING.md                # Git tagging conventions
│   └── GATES.md                  # Quality gates
└── 13-TEMPLATES/                 # Standard templates
    ├── ECR.yml                   # ECR template
    └── ECO.yml                   # ECO template
```

## Key Documents

- **[00-README.md](00-README.md)** - Start here for overview
- **[01-CM_PLAN.md](01-CM_PLAN.md)** - Configuration management processes
- **[02-PART_NUMBERING.md](02-PART_NUMBERING.md)** - How to assign part numbers
- **[03-SERIALIZATION.md](03-SERIALIZATION.md)** - Serialization requirements
- **[05-CCB/00-CHARTER.md](05-CCB/00-CHARTER.md)** - CCB authority and process

## Quick Links

### Submitting Changes
1. Review [01-CM_PLAN.md](01-CM_PLAN.md) section 4.2 for change process
2. Use template: [13-TEMPLATES/ECR.yml](13-TEMPLATES/ECR.yml)
3. Submit to Configuration Management

### Looking Up Part Numbers
- See [08-ITEM_MASTER/ITEMS.csv](08-ITEM_MASTER/ITEMS.csv)
- Part numbering rules: [02-PART_NUMBERING.md](02-PART_NUMBERING.md)

### CCB Meetings
- Charter: [05-CCB/00-CHARTER.md](05-CCB/00-CHARTER.md)
- Members: [05-CCB/01-MEMBERS.md](05-CCB/01-MEMBERS.md)
- Minutes: [05-CCB/02-MINUTES/](05-CCB/02-MINUTES/)

### Git Workflow
- Branching: [12-CI_CD_RULES/BRANCHING_MODEL.md](12-CI_CD_RULES/BRANCHING_MODEL.md)
- Tagging: [12-CI_CD_RULES/TAGGING.md](12-CI_CD_RULES/TAGGING.md)
- Quality Gates: [12-CI_CD_RULES/GATES.md](12-CI_CD_RULES/GATES.md)
