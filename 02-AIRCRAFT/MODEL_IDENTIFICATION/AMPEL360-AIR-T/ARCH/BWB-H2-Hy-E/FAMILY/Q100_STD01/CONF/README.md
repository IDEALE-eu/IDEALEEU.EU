# CONF — Configuration Management

## Navigation

- ⬆️ [Back to Q100_STD01](../README.md)
- 🏠 [Back to MODEL_IDENTIFICATION](../../../../../README.md)
- 🧭 [Navigation Index](../../../../../NAVIGATION_INDEX.md)

## Overview

This directory contains configuration management data for the Q100_STD01 family. Configuration data is managed at the family level to support configuration control across all systems and domains within this product family.

## Purpose

The CONF directory serves as the central repository for:
- Baseline configurations
- Component tracking
- Effectivity management
- Configuration items and their relationships
- Version control and change history

## Directory Structure

```
CONF/
├── BASELINE/              # Baseline configurations
│   └── COMPONENTS/        # Component-level configurations
│       └── {COMP_ID}/     # Individual component folders
│           └── SUBPRODUCT/
│               └── {SUBPROD_ID}/
│                   └── SUBJECT/
│                       └── {SUBJECT_ID}/
│                           └── RANGE-EFFECT/
│                               └── {RANGE}/
│                                   └── artifacts/
```

## Components

Configuration items are organized by component ID following the ATA chapter structure:

### Example: ATA-53-10-01
- **Component ID**: ATA-53-10-01 (Center Body - Primary Structure)
- **Location**: [BASELINE/COMPONENTS/ATA-53-10-01/](./BASELINE/COMPONENTS/ATA-53-10-01/)

## Organization Principles

### Family-Level Configuration
Configuration management is performed at the family level (Q100_STD01) rather than at individual system levels. This approach:
- Provides centralized configuration control
- Enables cross-system configuration management
- Supports product-level baseline definition
- Facilitates effectivity tracking across the family

### Component Identification
Components are identified using the ATA chapter structure:
- Format: `ATA-{XX}-{YY}-{ZZ}`
- Example: `ATA-53-10-01` = Fuselage (53), Center Body (10), Component 01

## Configuration Items

Each configuration item includes:
- **META.json**: Metadata and artifact information
- **MANIFEST.csv**: File manifest and checksums
- **CONFIG.yml**: Configuration parameters
- **DOC/**: Supporting documentation

## Subproduct and Subject Hierarchy

### Subproduct Level
- Identifier format: `SUBPROD_{NNN}`
- Contains: SUBPRODUCT_INDEX.csv

### Subject Level
- Identifier format: `SUBJ_{NNN}`
- Contains: SUBJECT_META.json, SUBJECT_MANIFEST.csv, SUBJECT_CONFIG.yml

### Effectivity Range
- Format: `{START}-{END}`
- Examples:
  - `0001-9999`: All aircraft
  - `0001-0100`: First 100 aircraft
  - `0101-9999`: From aircraft 101 onwards

## Artifacts

Artifacts are stored under the effectivity range:
```
RANGE-EFFECT/{RANGE}/artifacts/{SEQ}-{description}/
```

Each artifact directory contains:
- META.json
- MANIFEST.csv
- CONFIG.yml
- DOC/ (documentation folder)

## Change Control

All configuration changes must follow the Configuration Control Board (CCB) process:
1. Submit change request
2. Impact assessment
3. CCB review and approval
4. Implementation
5. Verification
6. Documentation update

## Related Documentation

- [Configuration Management Plan](../../../../../../00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)
- [Change Control Process](../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- [Baseline Management](./BASELINE/)

## Version Control

All configuration items are under version control with full traceability to:
- Design documentation
- Engineering changes
- Test results
- Manufacturing instructions

---

**Status**: Active  
**Created**: 2025-10-15  
**Last Updated**: 2025-10-15
