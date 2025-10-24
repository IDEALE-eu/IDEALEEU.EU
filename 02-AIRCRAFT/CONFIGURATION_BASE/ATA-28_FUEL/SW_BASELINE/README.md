# SW_BASELINE - Software Baseline

This directory contains software baseline information including software part numbers, versions, load configurations, partition assignments, and release packages.

## Purpose

Software baseline management ensures:
- Controlled software releases
- Version traceability
- Configuration consistency
- Certification compliance
- Reproducible builds

## Contents

This directory should contain:

### Software Releases
- **Software part numbers** - Unique identifiers for each software release
- **Version numbers** - Software version identification
- **Release notes** - Changes and fixes in each release
- **Build configurations** - Compiler settings and build parameters

### Load Configurations
- **Load files** - Binary executables and data files
- **Load manifests** - Complete software load inventory
- **Checksums/signatures** - Integrity verification data
- **Loading procedures** - Software installation instructions

### IMA-Specific (if applicable)
- **Partition assignments** - ARINC 653 partition allocations
- **Partition executables** - Software for each partition
- **Configuration tables** - ARINC 653 configuration data
- **Resource allocations** - CPU, memory, I/O assignments

## File Organization

```
SW_BASELINE/
├── RELEASES/
│   ├── v1.0.0/
│   │   ├── RELEASE_NOTES.md
│   │   ├── SOFTWARE_MANIFEST.json
│   │   ├── BINARIES/
│   │   └── CHECKSUMS.txt
│   └── v1.1.0/
├── PARTITIONS/            # For IMA-hosted applications
└── BUILD_CONFIGS/         # Build configuration files
```

## Software Placement Rules

Per [Configuration Rules](../../ATA-00_GENERAL/RULES.md):
- Software resides with its **host LRU** in the functional chapter
- IMA partition definitions in ATA-42
- Application software in functional chapters (ATA-27, etc.)
- Partition-to-application binding documented

## Software Categories

### Application Software
- Functional algorithms and control laws
- Data processing applications
- User interfaces
- Communication protocols

### System Software
- Operating systems
- Device drivers
- Boot loaders
- BIOS/firmware

### Support Software
- Built-In Test (BIT) software
- Diagnostic applications
- Configuration utilities
- Health monitoring

## Version Control

Software versions must follow:
- **Semantic versioning** (Major.Minor.Patch)
- **Build numbers** for internal tracking
- **Release tags** in version control system
- **Traceability** to requirements

## Certification Requirements

For certified software:
- **DO-178C** compliance (software development)
- **Design Assurance Level (DAL)** assignment
- **Verification evidence** in VERIFICATION/
- **Configuration control** per certification plan

## Change Control

Software changes require:
- Software Change Request (SCR)
- Impact analysis on certification
- Regression testing
- CCB approval for baseline changes
- Update to software manifest

## IMA Considerations

For ARINC 653 IMA systems:
- Partition definitions in **ATA-42/PARAMS/**
- Application binaries in functional chapters
- Partition bindings documented
- Resource allocations specified

## Build and Release Process

1. Source code checkout at release tag
2. Build using approved configuration
3. Generate checksums/signatures
4. Create release package
5. Verify against manifest
6. Obtain CCB approval
7. Archive release baseline

## References

- [Configuration Rules](../../ATA-00_GENERAL/RULES.md)
- [Part Numbering](../../../../00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md)
- [ATA-42 IMA](../ATA-42_INTEGRATED_MODULAR_AVIONICS/) (for partition info)
- [Software Development Plan](../../../../00-PROGRAM/ENGINEERING/SOFTWARE/)

## Standards Compliance

Software must comply with:
- **DO-178C**: Software considerations in airborne systems
- **DO-278A**: CNS/ATM software assurance
- **ARINC 653**: IMA partition management (if applicable)
- **Cybersecurity**: Software security requirements

---

**Status**: Active  
**Owner**: Software Engineering  
**Last Updated**: 2024-01-15
