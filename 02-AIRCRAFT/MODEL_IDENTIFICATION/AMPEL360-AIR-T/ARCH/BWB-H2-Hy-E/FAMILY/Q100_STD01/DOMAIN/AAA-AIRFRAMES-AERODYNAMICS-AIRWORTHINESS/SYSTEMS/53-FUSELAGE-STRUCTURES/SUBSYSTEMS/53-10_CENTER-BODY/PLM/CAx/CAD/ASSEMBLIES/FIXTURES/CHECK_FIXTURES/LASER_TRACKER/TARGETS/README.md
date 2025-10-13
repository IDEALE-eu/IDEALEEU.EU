# TARGETS — Laser Tracker Target Definitions

## Purpose

This directory contains target location definitions and configurations for laser tracker measurement operations.

## Contents

### Target Types
- **Reference targets**: Fixed datum targets
- **Part targets**: Measurement points on parts
- **Fixture targets**: Measurement points on fixtures
- **Tooling balls**: Precision sphere targets

## Naming Convention

Use the following pattern:
```
TARGETS_<fixture-id>_<target-set>_<version>.txt
```

Examples:
- `TARGETS_FIX-CHECK-F05_DATUM_v01.txt`
- `TARGETS_FIX-CHECK-WING-INT_MEAS-POINTS_v02.txt`
- `TARGETS_FIX-CHECK-SKIN_REFERENCE_v01.txt`

## Target Definition Format

Each target definition should include:
- **Target ID**: Unique identifier
- **Nominal coordinates**: X, Y, Z position
- **Target type**: SMR, tooling ball, prism
- **Tolerance**: Allowable deviation
- **Description**: Purpose and location notes
- **Reference**: Drawing or CAD reference

## Target Placement Guidelines

### Reference Targets
- Stable, permanent locations
- Well-distributed in measurement volume
- Accessible from all measurement positions
- Protected from damage
- Regularly verified

### Measurement Targets
- Located at critical features
- Accessible with laser tracker line-of-sight
- Documented in measurement plan
- Correspond to check points
- Traceable to design specifications

## Target File Formats

Supported formats:
- **Plain text**: `.txt` with coordinates
- **CSV**: `.csv` with tabular data
- **Native formats**: Leica, FARO, API formats
- **CAD formats**: `.step`, `.iges` for visualization

## Related Directories

- **Layouts**: [`../LAYOUTS/`](../LAYOUTS/)
- **Check points**: [`../../CHECK_POINTS/`](../../CHECK_POINTS/)
- **CAD models**: [`../../MODELS/`](../../MODELS/)
