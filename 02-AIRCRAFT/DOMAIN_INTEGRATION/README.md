# Domain Integration

This directory contains the integration of multiple engineering domains for aircraft products.

## Structure

```
DOMAIN_INTEGRATION/
├── PRODUCTS/
│   └── AMPEL360-AIR-T/
│       └── MODELS/
│           └── BWB/
│               └── VERSION/
│                   └── Q100/
│                       ├── README.md                    # Main documentation
│                       ├── [15 DOMAIN directories]      # Engineering domains
│                       └── ...
└── MECHANICAL_CONTROL_SYSTEMS/                          # Legacy structure
```

## Quick Start

### Creating Domain Structure

To generate the complete domain integration structure with all 15 domains and sample systems:

```bash
./scripts/create-domains.sh
```

This creates:
- 15 engineering domains (AAA, PPP, MEC, LCC, EDI, EEE, EER, DDD, CCC, IIS, LIB, AAP, CQH, IIF, OOO)
- **Representative systems with subsystems** (one per domain demonstrating the pattern)
- Complete PLM/CAx structure in each subsystem

### Validating Structure

To validate the domain integration structure complies with all rules:

```bash
./scripts/validate-structure.sh
```

This validates:
- Mandatory SYSTEMS/ directory in all domains
- Proper system structure (INTEGRATION_VIEW.md, INTERFACE_MATRIX/)
- Subsystem structure with PLM/CAx
- Absence of prohibited PLM/CAx at domain level
- Required metadata files

## Documentation

For detailed information about the domain structure, conventions, and rules, see:

**[Q100/README.md](./PRODUCTS/AMPEL360-AIR-T/MODELS/BWB/VERSION/Q100/README.md)**

## Key Conventions

1. **Unified /SYSTEMS/ structure** - Single level for systems organization
2. **PLM/CAx only in SUBSYSTEMS** - Engineering artifacts at subsystem level only
3. **SW with LRU host** - Software resides with its host hardware (ATA chapter)
4. **EWIS in ATA-92 only** - All electrical wiring in dedicated chapter
5. **Integration focus** - Each system has INTEGRATION_VIEW.md and INTERFACE_MATRIX/

## Integration with Configuration Management

All domain structures integrate with:
- `00-PROGRAM/CONFIG_MGMT/` - Change control and baselines
- `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/` - Interface control documents
- `02-AIRCRAFT/CONFIGURATION_BASE/` - ATA chapter configurations

## Scripts

Located in `/scripts/`:
- `create-domains.sh` - Creates the complete domain structure
- `validate-structure.sh` - Validates structure compliance

Both scripts are idempotent and safe to run multiple times.
