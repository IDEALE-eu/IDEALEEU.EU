# BASELINE - Configuration Baseline

This directory contains baseline configuration data including component lists, system architecture definitions, and baseline snapshots at major program gates.

## Purpose

Configuration baselines establish the approved, controlled configuration of the system at specific points in time. Baselines serve as:
- Reference points for change management
- Foundation for impact analysis
- Basis for configuration audits
- Snapshots at program milestones

## Contents

This directory should contain:

### Baseline Snapshots
- **Gate baselines** - Configuration frozen at program gates (PDR, CDR, etc.)
- **Release baselines** - Approved configurations for specific releases
- **As-built baselines** - Actual configuration of delivered systems

### Configuration Data
- **Component lists** - Bill of materials and component inventories
- **System architecture** - High-level system design and interfaces
- **Configuration identifiers** - Part numbers, version numbers, serial numbers
- **Baseline manifests** - Complete inventory of configuration items

## File Organization

```
BASELINE/
├── GATE_[X]/              # Gate-specific baselines (PDR, CDR, etc.)
│   ├── MANIFEST.json      # Complete baseline inventory
│   ├── COMPONENTS.csv     # Component list
│   └── ARCHITECTURE.pdf   # System architecture
├── RELEASE_[X.Y]/         # Release baselines
└── CURRENT/               # Current approved baseline
```

## Baseline Establishment Process

1. Freeze configuration at milestone
2. Generate complete manifest with checksums
3. Document all configuration items
4. Obtain CCB approval
5. Tag in version control
6. Archive baseline package

## Change Control

Baselines are **immutable**:
- No modifications to established baselines
- Changes create new baseline versions
- All changes tracked in CHANGE_LOG
- Full traceability maintained

## Baseline Types

### Functional Baseline
- Requirements and specifications
- System functional description
- Interface definitions

### Allocated Baseline
- Hardware/software allocations
- Component specifications
- Interface control documents

### Product Baseline
- As-designed configuration
- Manufacturing specifications
- Acceptance criteria

## References

- [Baseline Process](../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/00-README.md)
- [Configuration Rules](../../ATA-00_GENERAL/RULES.md)
- [Item Master](../../../../00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/)

## Compliance

Baselines must comply with:
- Configuration Management Plan
- Program milestone requirements
- Certification requirements
- Customer specifications

---

**Status**: Active  
**Owner**: Configuration Management  
**Last Updated**: 2024-01-15
