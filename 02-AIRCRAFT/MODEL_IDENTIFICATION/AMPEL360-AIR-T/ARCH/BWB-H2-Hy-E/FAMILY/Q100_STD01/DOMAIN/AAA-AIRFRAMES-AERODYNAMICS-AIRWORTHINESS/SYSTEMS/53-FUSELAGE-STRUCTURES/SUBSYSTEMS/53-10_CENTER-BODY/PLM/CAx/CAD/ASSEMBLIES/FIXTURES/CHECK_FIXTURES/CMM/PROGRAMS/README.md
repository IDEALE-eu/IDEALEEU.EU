# PROGRAMS — CMM Measurement Programs

## Purpose

This directory contains CMM (Coordinate Measuring Machine) measurement programs for check fixture inspection operations.

## Contents

### Program Types
- **Part measurement programs**: Programs for inspecting parts
- **Fixture verification programs**: Programs for checking fixture accuracy
- **First article programs**: FAI measurement programs
- **Periodic inspection programs**: Routine verification programs

## Naming Convention

Use the following pattern:
```
CMM_<fixture-id>_<part-id>_<version>.<ext>
```

Examples:
- `CMM_FIX-CHECK-F05_FRAME-F05_v01.dmis`
- `CMM_FIX-CHECK-WING-INT_INTERFACE_v02.prg`
- `CMM_FIX-CHECK-SKIN_PANEL-001_v01.pcdmis`

## Program Formats

### Supported Formats
- **DMIS**: `.dmis` (Dimensional Measuring Interface Standard)
- **PC-DMIS**: `.pcdmis`
- **Calypso**: `.prg`
- **MCOSMOS**: `.prg`
- **Proprietary**: Vendor-specific formats

## Program Requirements

Each CMM program should include:
- **Header**: Program ID, revision, date, author
- **Coordinate system**: Reference to master datum
- **Probe qualification**: Probe configuration and qualification
- **Measurement sequence**: Point definitions and features
- **Tolerances**: Dimensional and GD&T tolerances
- **Output**: Report format and content
- **Comments**: Explanatory notes

## Program Validation

CMM programs must be:
- Validated with known good part
- Reviewed by quality engineering
- Version controlled
- Documented with measurement plan
- Updated when design changes occur

## Related Directories

- **Probes**: [`../PROBES/`](../PROBES/)
- **Reports**: [`../REPORTS/`](../REPORTS/)
- **Check points**: [`../../CHECK_POINTS/`](../../CHECK_POINTS/)
