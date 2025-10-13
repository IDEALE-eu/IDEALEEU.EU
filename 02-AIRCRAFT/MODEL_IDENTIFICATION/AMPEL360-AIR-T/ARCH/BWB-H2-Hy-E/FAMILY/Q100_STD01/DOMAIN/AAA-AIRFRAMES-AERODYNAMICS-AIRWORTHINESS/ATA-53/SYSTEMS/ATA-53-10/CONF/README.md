# CONF - Configuration Management

## Overview

This directory contains all configuration management data for the ATA-53-10 Center Body system.

## Purpose

Configuration management ensures:
- Controlled baselines
- Change traceability
- Component tracking
- Version control
- Compliance with standards

## Structure

### [BASELINE/](./BASELINE/)

Contains approved configuration baselines at specific points in time.

#### [BASELINE/COMPONENTS/](./BASELINE/COMPONENTS/)

Component-level configuration data organized hierarchically:

```
COMPONENTS/
└── {COMPONENT_ID}/              # Component identifier (e.g., ATA-53-10-01)
    └── SUBPRODUCT/              # Subproduct organization level
        └── {SUBPROD_ID}/        # Specific subproduct (e.g., SUBPROD_001)
            ├── SUBPRODUCT_INDEX.csv    # Subproduct inventory
            └── SUBJECT/                 # Subject matter organization
                └── {SUBJECT_ID}/        # Specific subject (e.g., SUBJ_001)
                    ├── SUBJECT_META.json       # Subject metadata
                    ├── SUBJECT_MANIFEST.csv    # Artifact manifest
                    ├── SUBJECT_CONFIG.yml      # Subject configuration
                    └── RANGE-EFFECT/            # Effectivity ranges
                        └── {RANGE}/             # Effectivity range (e.g., 0001-9999)
                            └── artifacts/       # Artifact storage
                                └── {ITEM}/      # Artifact item (e.g., 01-design-doc)
                                    ├── META.json      # Artifact metadata
                                    ├── MANIFEST.csv   # File manifest
                                    ├── CONFIG.yml     # Artifact config
                                    └── DOC/           # Documentation files
```

## Key Concepts

### Component
A distinct structural or functional element with its own part number and configuration control.

**Example**: ATA-53-10-01 (Center Body Main Frame Assembly)

### Subproduct
A logical grouping of related subjects within a component.

**Example**: SUBPROD_001 (Primary Structure Subassembly)

### Subject
A specific topic, analysis, or design aspect within a subproduct.

**Example**: SUBJ_001 (Structural Design and Analysis)

### Range-Effect
The serial number or effectivity range for which the configuration applies.

**Format**: `{START}-{END}` (e.g., 0001-9999 for all aircraft)

### Artifacts
Individual deliverable items (documents, models, analyses, etc.).

**Format**: `{SEQ}-{description}` (e.g., 01-design-specification)

## File Types

### SUBPRODUCT_INDEX.csv
Lists all subproducts within a component.

**Columns**: subproduct_id, description, version, status, owner, created_date, modified_date

### SUBJECT_META.json
Metadata describing a subject in machine-readable format.

**Contains**: ID, title, description, version, status, owner, dates, tags, compliance info

### SUBJECT_MANIFEST.csv
Inventory of all artifacts within a subject.

**Columns**: artifact_id, artifact_name, artifact_type, file_path, checksum, version, created_date, status

### SUBJECT_CONFIG.yml
Configuration settings for a subject in human-readable format.

**Contains**: Subject info, effectivity, configuration, traceability, validation, metadata

### Artifact Files
Each artifact has:
- **META.json**: Artifact metadata
- **MANIFEST.csv**: File inventory
- **CONFIG.yml**: Configuration
- **DOC/**: Actual documentation files

## Baseline Types

### Functional Baseline
- Requirements and specifications
- Functional architecture
- Interface definitions

### Allocated Baseline
- Hardware/software allocation
- Component specifications
- Interface control documents

### Product Baseline
- As-designed configuration
- Manufacturing specifications
- Acceptance criteria
- Certification basis

## Change Control Process

1. **Change Request**: Submitted via ECR
2. **Impact Analysis**: Assess effects on configuration
3. **CCB Review**: Configuration Control Board approval
4. **Implementation**: Execute approved changes
5. **Verification**: Confirm correct implementation
6. **Baseline Update**: Update configuration items
7. **Notification**: Inform stakeholders

## Traceability

All configuration items maintain traceability to:
- Parent requirements
- Related artifacts
- Interface agreements
- Test and verification results
- Manufacturing records
- Service documentation

## Version Control

### Versioning Scheme
- **Major**: Significant configuration changes
- **Minor**: Updates and enhancements
- **Patch**: Corrections and clarifications

### Release States
- **Draft**: Work in progress
- **Review**: Under review
- **Approved**: CCB approved
- **Released**: Available for use
- **Obsolete**: Superseded by newer version

## Compliance

Configuration management complies with:
- **AS9100**: Quality management for aerospace
- **ISO 9001**: Quality management systems
- **ISO 10007**: Configuration management guidelines
- **EIA-649**: Configuration management standard

## Tools and Systems

- **PLM System**: Primary data repository
- **Version Control**: Git, SVN for document management
- **Database**: Configuration item tracking
- **Reporting**: Automated configuration status reports

## Example

See [COMPONENTS/ATA-53-10-01/](./BASELINE/COMPONENTS/ATA-53-10-01/) for a complete example of the configuration hierarchy with sample data.

---

**Owner**: Configuration Management  
**Status**: Active  
**Last Updated**: 2025-10-13
