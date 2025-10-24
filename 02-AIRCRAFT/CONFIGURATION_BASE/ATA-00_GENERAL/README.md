# ATA-00_GENERAL

Shared resources and standards for all ATA chapters in CONFIGURATION_BASE.

## Overview

This directory contains templates, schemas, rules, and tools that are used across all ATA chapters to ensure consistency and standardization of configuration data.

## Contents

### RULES.md
Comprehensive configuration management rules governing:
- LRU placement (Rule 1)
- Software placement with host LRU (Rule 2)
- EWIS centralization in ATA-92 (Rule 3)
- Change control requirements (Rule 4)
- Baseline immutability (Rule 5)
- And 18 additional rules

See [RULES.md](./RULES.md) for complete details.

### SCHEMAS/
JSON/XML schemas for validating configuration files:
- `parameter.schema.json` - Schema for parameter definitions
- Additional schemas for baselines, ICDs, and other data types

Schemas ensure data quality and consistency across all ATA chapters.

### UTCS_INDEX/
Unified Type Certificate Specification index and schemas:
- `index.json` - Master index of UTCS entries
- `utcs-schemas/` - UTCS-specific schemas

### TEMPLATES/
Standard templates for configuration files:
- `PARAMS.csv` - Parameter definition template
- `PARTITION_MAP.csv` - IMA partition mapping template (for ATA-42)
- `IMA_CONFIG.xml` - ARINC 653 configuration template (for ATA-42)

Copy these templates when creating new configuration files.

### GLOBAL_CHANGE_LOG.csv
Master change log aggregating all configuration changes across all ATA chapters.

Format:
- Chapter
- ECR_Number
- ECO_Number
- Date
- Description
- Affected_Items
- Status
- Approver
- Verification_Status

## Usage

### Creating New Parameters
1. Copy `TEMPLATES/PARAMS.csv` to target ATA chapter PARAMS/ directory
2. Rename appropriately
3. Fill in parameter values
4. Validate against `SCHEMAS/parameter.schema.json`
5. Submit through CCB approval process
6. Update GLOBAL_CHANGE_LOG.csv

### Validating Configuration Files
Use schemas to validate configuration files:

```bash
# Validate JSON parameter file
jsonschema -i ATA-28_FUEL/PARAMS/params.json SCHEMAS/parameter.schema.json

# Validate XML IMA config
xmllint --schema SCHEMAS/ima-config.xsd ATA-42_INTEGRATED_MODULAR_AVIONICS/BASELINE/IMA_CONFIG.xml
```

### Using Templates
```bash
# Copy parameter template
cp ATA-00_GENERAL/TEMPLATES/PARAMS.csv ATA-XX_SYSTEM/PARAMS/MY_PARAMS.csv

# Edit the file with your parameter values
# ...

# Validate
csvlint ATA-XX_SYSTEM/PARAMS/MY_PARAMS.csv
```

## Configuration Rules Summary

Key rules from RULES.md:

1. **LRUs in Primary ATA Chapter** - Hardware goes in its functional chapter
2. **Software with Host LRU** - Software stays with hardware
3. **ALL Wiring in ATA-92** - No wiring in system chapters
4. **Change Control Required** - All changes need ECR/ECO
5. **Baselines are Immutable** - Changes create new versions

See [RULES.md](./RULES.md) for all 23 rules.

## Standards and Compliance

This structure complies with:
- ATA iSpec 2200 specification
- ARINC 653 (for IMA configurations)
- DO-178C/DO-254 (software/hardware development)
- DO-160 (environmental testing)
- FAA/EASA EWIS requirements

## Maintenance

- **Owner**: Configuration Management Team
- **Review Frequency**: Quarterly and at each program gate
- **Change Process**: Via ECR/ECO only

## References

- [Main CONFIGURATION_BASE README](../00-README.md)
- [Configuration Management Plan](../../../00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)
- [Baseline Process](../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/00-README.md)
- [Change Process](../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)

---

**Last Updated**: 2024-01-15
