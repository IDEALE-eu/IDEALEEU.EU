# 06-CI — Continuous Integration and Validation

This directory contains automated validation checks and schema definitions for the CONF structure.

## Purpose

Provide automated validation of configuration management rules, naming conventions, and structural integrity through continuous integration checks.

## Contents

### schema.json
JSON schema defining valid configuration file formats and naming conventions.

**Validates:**
- Version naming (HEAD or R01-R99)
- Effectivity range formats (MSN ranges, test article IDs)
- Configuration types (BASELINE, VARIANT, CUSTOMER, TEST)
- Family designations (Q100_STD01 format)
- Release tags (PROD, HOTFIX-YYYYMMDD, EXP)

### checks.yaml
CI validation rules and guardrails for configuration management.

**Checks Include:**
- Version naming compliance
- Effectivity format validation
- BASELINE to PROD linkage verification
- Test configuration inheritance rules
- Artifact location validation
- README presence in leaf directories
- MSN_EFFECTIVITY.csv format validation
- Compliance file presence

## Guardrails

### Enforced Rules (Blocking)
1. **Only BASELINE feeds PROD** - Production releases must come from BASELINE configurations
2. **Test inheritance** - FTI and SIM must inherit from BASELINE or VARIANT via 00-CONFIG/BLOCKS
3. **No artifacts outside CONF/VERSION/** - All configuration artifacts must be within this structure
4. **Immutable release versions** - R01-R99 versions cannot be modified once created

### Informational Rules
1. **HEAD is mutable** - Development version allows changes with proper approval

## Validation Workflow

### On Commit
- Version naming validation
- Effectivity format checks
- README presence verification

### On Merge
- Full structural validation
- Dependency checks
- Compliance file validation
- Release tag verification

### Scheduled (Daily)
- Complete validation suite
- Coverage analysis
- Orphan detection

## Usage

### Running Validation Locally
```bash
# Validate schema compliance
jsonschema -i config.json schema.json

# Run all CI checks
yaml-lint checks.yaml
```

### Integration with CI/CD
Add to your CI pipeline:
```yaml
validation:
  script:
    - python scripts/validate_conf_structure.py
    - jsonschema -i $CONF_FILE 06-CI/schema.json
```

## Naming Rules

### Versions
- **HEAD** - Mutable development version
- **R01-R99** - Immutable release versions

### Release Tags (02-RELEASE_TAGS)
- **PROD** - Production release (from BASELINE only)
- **HOTFIX-YYYYMMDD** - Hotfix release with date
- **EXP** - Experimental/test release

### Effectivity
Format in MSN_EFFECTIVITY.csv:
```csv
MSN,FROM,TO,CONF_ID
Q100-0001,0001,9999,CFG-Q100-BASE
```

## Error Handling

Validation failures are categorized:
- **ERROR** - Blocking issues that prevent merge
- **WARNING** - Issues requiring attention but not blocking
- **INFO** - Informational messages

## References

- Configuration Management Plan
- Schema Specification: schema.json
- Validation Rules: checks.yaml

---

**Owner:** Configuration Management & DevOps  
**Status:** Active  
**Last Updated:** 2025-10-13
