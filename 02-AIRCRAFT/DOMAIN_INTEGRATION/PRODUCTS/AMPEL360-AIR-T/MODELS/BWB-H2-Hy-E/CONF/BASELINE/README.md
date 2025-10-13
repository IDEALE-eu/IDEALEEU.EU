# BASELINE — Standard Production Configurations

This directory contains standard production configurations for the BWB-H2-Hy-E aircraft model.

## Purpose

BASELINE configurations represent the standard, certified production configurations that form the foundation for all delivered aircraft. These configurations are controlled through the Configuration Control Board (CCB) and are referenced by production serial numbers.

## Structure

```
BASELINE/
└── FAMILY/
    └── Q100_STD01/              # Q100 family standard configuration
        └── VERSION/
            ├── HEAD/            # Development version
            │   └── EFFECTIVITY/
            │       └── 0001-9999/
            └── R01/             # Release 01 (frozen)
                └── EFFECTIVITY/
                    └── 0001-9999/
```

## Configuration Hierarchy

### FAMILY Level
- **Q100_STD01** - Standard Q100 family configuration
  - Defines the base aircraft family characteristics
  - Reference for all production aircraft
  - Establishes standard systems and interfaces

### VERSION Level
- **HEAD** - Active development version
  - Mutable, used for ongoing development
  - Configuration changes allowed with proper approval
  - Baseline for next release
  
- **R01, R02, ...** - Released versions
  - Immutable, frozen at release gate
  - Tagged in version control
  - Certified configuration baseline
  - Changes require formal ECO process

### EFFECTIVITY Level
- **0001-9999** - Serial number range
  - Defines which aircraft serial numbers this configuration applies to
  - Coordinated with production planning
  - Links to `../Q100/01-EFFECTIVITY/MSN_EFFECTIVITY.csv`

## Usage

### Applying a Baseline Configuration

1. Determine the aircraft serial number (MSN)
2. Check effectivity range to confirm applicability
3. Select appropriate VERSION (HEAD for development, Rxx for production)
4. Reference configuration data at the EFFECTIVITY level
5. Cross-reference with `FAMILY/Q100_STD01/VERSION/Q100/01-EFFECTIVITY/` for detailed effectivity

### Creating a New Baseline Version

1. Freeze current HEAD configuration
2. Create new release version directory (e.g., R02)
3. Copy configuration from HEAD to new release
4. Tag in version control with release identifier
5. Update CCB records and baseline documentation
6. Continue development in HEAD

### Configuration Content

At the EFFECTIVITY level, include:
- Configuration identifiers (part numbers, software loads)
- System configuration data
- Installation specifications
- Interface definitions
- Certification basis
- Links to detailed configuration in `../Q100/00-CONFIG/`

## Integration with Effectivity System

BASELINE configurations integrate with the effectivity management system:

```
MSN Q100-0001 → Config Set CFG-Q100-BASE → BASELINE/FAMILY/Q100_STD01/VERSION/R01/EFFECTIVITY/0001-9999/
```

Reference:
- **[FAMILY/Q100_STD01/VERSION/Q100/01-EFFECTIVITY/MSN_EFFECTIVITY.csv](../FAMILY/Q100_STD01/VERSION/Q100/01-EFFECTIVITY/MSN_EFFECTIVITY.csv)** - MSN to configuration mapping
- **[FAMILY/Q100_STD01/VERSION/Q100/00-CONFIG/CONFIG_SETS/](../FAMILY/Q100_STD01/VERSION/Q100/00-CONFIG/CONFIG_SETS/)** - Configuration set definitions

## Change Control

Baseline configurations are subject to strict change control:
- **HEAD** - Changes via standard approval process
- **Released versions (Rxx)** - No modifications allowed
  - Changes create new baseline version
  - Tracked through ECR/ECO process
  - Full traceability maintained

## Certification

Each released baseline version must:
- Be approved by CCB
- Have complete configuration audit trail
- Include certification evidence
- Link to verification data
- Meet regulatory requirements

## References

- **Configuration Management Plan** - [00-PROGRAM/CONFIG_MGMT/00-README.md](../../../../../../00-PROGRAM/CONFIG_MGMT/00-README.md)
- **Baseline Process** - [00-PROGRAM/CONFIG_MGMT/04-BASELINES/](../../../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/)
- **Effectivity Management** - [FAMILY/Q100_STD01/VERSION/Q100/01-EFFECTIVITY/](../FAMILY/Q100_STD01/VERSION/Q100/01-EFFECTIVITY/)

---

**Owner:** Configuration Management  
**Status:** Active  
**Last Updated:** 2025-10-13
