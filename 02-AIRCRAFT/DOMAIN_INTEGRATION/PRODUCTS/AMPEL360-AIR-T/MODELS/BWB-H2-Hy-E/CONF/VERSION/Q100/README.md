# VERSION/Q100 — Configuration Management Data

This directory contains version-specific configuration management data for the Q100 aircraft family.

## Purpose

Centralized location for configuration sets, effectivity data, release management, compliance tracking, and CI validation for the Q100 family.

## Directory Structure

```
Q100/
├── 00-CONFIG/          # Configuration sets and blocks
│   ├── BLOCKS/         # Serial block definitions (production batches)
│   └── MODS/           # Modification packages
├── 01-EFFECTIVITY/     # MSN effectivity and modification states
│   └── MSN_EFFECTIVITY.csv  # Master effectivity table
├── 02-RELEASE_TAGS/    # Release tags (PROD, HOTFIX, EXP)
├── 03-TRACEABILITY/    # Requirements and design traceability
├── 04-ICD_LINKS/       # Interface control document links
├── 05-COMPLIANCE/      # DO-160/ECSS compliance matrices
│   ├── REQ-COVERAGE.csv       # Requirements coverage
│   └── ENV-QUAL-MATRIX.csv    # Environmental qualification
└── 06-CI/              # Continuous integration validation
    ├── schema.json     # Configuration schema
    └── checks.yaml     # Validation rules and guardrails
```

## Naming Rules

### Versions
- **HEAD** - Mutable development version
- **R01-R99** - Immutable release versions (frozen at release gates)

### Release Tags (02-RELEASE_TAGS)
- **PROD** - Production release (only from BASELINE configurations)
- **HOTFIX-YYYYMMDD** - Hotfix release with date stamp (format: HOTFIX-20251013)
- **EXP** - Experimental or test release

### Effectivity Format (01-EFFECTIVITY/MSN_EFFECTIVITY.csv)
```csv
MSN,FROM,TO,CONF_ID
Q100-0001,0001,9999,CFG-Q100-BASE
Q100-0100,0100,0299,CFG-Q100-V001
```

**Columns:**
- `MSN` - Aircraft serial number
- `FROM` - Starting serial number in range
- `TO` - Ending serial number in range
- `CONF_ID` - Configuration identifier

## Guardrails

Enforced through 06-CI/checks.yaml:

1. **Only BASELINE feeds PROD** - Production releases must originate from BASELINE configurations
2. **FTI and SIM inherit from BASELINE or VARIANT** - Test configurations must inherit via 00-CONFIG/BLOCKS
3. **No artifacts outside CONF/VERSION/** - All configuration artifacts must be within this structure
4. **R01-R99 are immutable** - Release versions cannot be modified once created
5. **HEAD is mutable** - Development version allows changes with proper approval

## Configuration Management Process

### Creating a New Configuration
1. Define configuration in appropriate type (BASELINE/VARIANT/CUSTOMER/TEST)
2. Add effectivity data to 01-EFFECTIVITY/MSN_EFFECTIVITY.csv
3. Create configuration block in 00-CONFIG/BLOCKS/
4. Link to appropriate release tag in 02-RELEASE_TAGS/
5. Validate with 06-CI/checks.yaml

### Releasing a Configuration
1. Freeze HEAD version
2. Create new release version (R01, R02, etc.)
3. Tag in 02-RELEASE_TAGS/ with appropriate tag (PROD, HOTFIX, EXP)
4. Update compliance matrices in 05-COMPLIANCE/
5. Run CI validation checks
6. Obtain CCB approval

### Modifying a Released Configuration
1. Released versions (R01-R99) are immutable
2. Create new release version (e.g., R02)
3. Document changes through ECR/ECO process
4. Update effectivity as needed
5. Complete certification if required

## Integration

### With BASELINE/VARIANT/CUSTOMER/TEST
Configuration types reference this data for:
- Serial number effectivity (01-EFFECTIVITY/)
- Configuration blocks and mods (00-CONFIG/)
- Release versioning (02-RELEASE_TAGS/)

### With Compliance Systems
- Requirements traceability (03-TRACEABILITY/)
- DO-160/ECSS compliance (05-COMPLIANCE/)
- Interface definitions (04-ICD_LINKS/)

### With CI/CD Pipelines
- Schema validation (06-CI/schema.json)
- Automated checks (06-CI/checks.yaml)
- Guardrail enforcement

## References

- **Configuration Management Plan** - [00-PROGRAM/CONFIG_MGMT/](../../../../../../../00-PROGRAM/CONFIG_MGMT/)
- **Effectivity Details** - [01-EFFECTIVITY/README.md](./01-EFFECTIVITY/README.md)
- **Compliance Tracking** - [05-COMPLIANCE/README.md](./05-COMPLIANCE/README.md)
- **CI Validation** - [06-CI/README.md](./06-CI/README.md)

---

**Owner:** Configuration Management  
**Status:** Active  
**Last Updated:** 2025-10-13
