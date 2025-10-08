# COMMON

Shared resources for baseline management across all gates.

## Purpose

This directory contains templates, checklists, and schemas used across all baseline gates to ensure consistency and compliance in baseline establishment and approval.

## Contents

### CHECKLISTS/

Gate-specific approval checklists that define the criteria for baseline establishment:

- **SRR_CHECKLIST.md** - System Requirements Review checklist
- **PDR_CHECKLIST.md** - Preliminary Design Review checklist
- **CDR_CHECKLIST.md** - Critical Design Review checklist
- **TRR_CHECKLIST.md** - Test Readiness Review checklist
- **PRR_CHECKLIST.md** - Production Readiness Review checklist
- **ORR_EIS_CHECKLIST.md** - Operational Readiness Review / Entry Into Service checklist (Aircraft)
- **FRR_CHECKLIST.md** - Flight Readiness Review checklist (Spacecraft)

Each checklist includes:
- Required documentation
- Configuration management items
- Verification criteria
- Approval requirements

### TEMPLATES/

Standard templates for baseline documentation:

- **MANIFEST.schema.json** - JSON schema for baseline manifest files
  - Defines the structure and validation rules for MANIFEST.json files
  - Includes all required fields and data types
  - Ensures consistency across all baselines

- **MANIFEST.example.json** - Example baseline manifest
  - Demonstrates proper usage of the schema
  - Shows real-world examples of configuration items
  - Includes sample data for all major CI types (EBOM, MBOM, SW, ICD, etc.)

- **APPROVAL.md** - Baseline approval template
  - CCB approval documentation
  - Signature blocks for key stakeholders
  - Conditions and scope of approval
  - Distribution checklist

- **LINKS.md** - Standard references template
  - Links to configuration management resources
  - Pointers to related artifacts
  - Cross-references to other program areas

## Usage

When establishing a new baseline:

1. **Review Checklist**: Use the appropriate gate checklist to verify all criteria are met
2. **Create Manifest**: Use MANIFEST.schema.json to create a valid MANIFEST.json file
3. **Document Approval**: Fill out APPROVAL.md with CCB decision and signatures
4. **Establish Links**: Copy LINKS.md and update with baseline-specific references
5. **Generate Hashes**: Create MANIFEST.sha256 with SHA-256 hashes of all artifacts

## Validation

The MANIFEST.schema.json can be used to validate baseline manifests:

```bash
# Using a JSON schema validator
jsonschema -i path/to/MANIFEST.json COMMON/TEMPLATES/MANIFEST.schema.json
```

## References

- **Baseline Process**: [../00-README.md](../00-README.md)
- **Baseline Index**: [../INDEX.csv](../INDEX.csv)
- **Tagging Conventions**: [../../12-CI_CD_RULES/TAGGING.md](../../12-CI_CD_RULES/TAGGING.md)
