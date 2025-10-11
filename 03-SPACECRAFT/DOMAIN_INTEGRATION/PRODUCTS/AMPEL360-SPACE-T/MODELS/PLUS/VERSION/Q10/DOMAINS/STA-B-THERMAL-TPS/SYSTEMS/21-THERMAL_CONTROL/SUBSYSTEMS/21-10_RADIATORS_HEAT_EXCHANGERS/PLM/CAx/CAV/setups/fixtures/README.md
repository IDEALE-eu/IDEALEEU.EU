# FIXTURES — Test Fixtures and Mounting Hardware

## Purpose

This directory contains documentation for test fixtures, mounting hardware, and mechanical interface configurations.

## Contents

- Fixture identification and part numbers
- Clamp and bolt patterns
- Torque specifications
- Assembly drawings and photos
- Fixture calibration and inspection records
- Interface diagrams

## File Naming Convention

```
FIXTURE_<fixture-id>_<description>_<rev>.{pdf|png|yaml}
```

Examples:
- `FIXTURE_RAD-001_mounting_clamps_r01.pdf`
- `FIXTURE_TVAC-HX-01_coldplate_mount_r02.png`
- `FIXTURE_VIB-01_adapter_plate_config_r01.yaml`

## Fixture Documentation

Each fixture should be documented with:
- **ID**: Unique fixture identifier
- **Description**: Purpose and test article compatibility
- **Drawings**: Assembly and detail drawings
- **Parts List**: All hardware components
- **Torque Specs**: Bolt torques and sequences
- **Photos**: As-installed configuration
- **Interface Points**: Mounting locations and interfaces
- **Calibration**: Fixture inspection and calibration

## Fixture Types

### TVAC Fixtures
- Chamber mounting frames
- Thermal interface mounts
- Plumbing support fixtures
- Instrumentation mounting brackets

### Vibration Fixtures
- Shaker adapter plates
- Vibration isolation mounts
- Fixture resonance characterization

### Pressure Test Fixtures
- Leak test fixtures
- Proof/burst test supports
- Pressure containment shields

## Quality Requirements

- ✅ All fixtures must be inspected before use
- ✅ Calibration current and traceable
- ✅ Photos of as-installed configuration
- ✅ Damage inspection after each test
- ✅ Maintenance records maintained

## Related Directories

- **[../](../)** — Test setups overview
- **[../chamber_recipes/](../chamber_recipes/)** — TVAC profiles
- **[../../procedures/](../../procedures/)** — Setup procedures

---

**Last Updated**: 2025-10-10
