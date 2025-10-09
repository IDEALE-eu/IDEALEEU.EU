# TOLERANCES — Tolerance Specifications

## Purpose

This directory contains tolerance specifications and acceptance criteria for check fixture inspection operations.

## Contents

### Tolerance Types
- **Dimensional tolerances**: Linear and angular dimensions
- **Geometric tolerances**: GD&T specifications
- **Surface finish requirements**: Roughness and texture
- **Fit tolerances**: Assembly clearances and interferences

## Naming Convention

Use the following pattern:
```
TOLERANCES_<part-id>_<spec-type>_<version>.xlsx
```

Examples:
- `TOLERANCES_FRAME-F05_DIMENSIONAL_v01.xlsx`
- `TOLERANCES_WING-INTERFACE_GEOMETRIC_v02.xlsx`
- `TOLERANCES_SKIN-PANEL-001_ALL_v01.xlsx`

## Tolerance Specification Format

Each tolerance specification should include:
- **Feature ID**: Reference to check point
- **Nominal value**: Design intent dimension
- **Upper limit**: Maximum acceptable value
- **Lower limit**: Minimum acceptable value
- **Tolerance type**: Bilateral, unilateral, limit
- **GD&T symbol**: If geometric tolerance
- **Material condition**: RFS, MMC, LMC if applicable
- **Drawing reference**: Source document

## Tolerance Classes

### Critical Tolerances
- ±0.05 mm or tighter
- Safety or function critical
- 100% inspection required
- SPC monitoring recommended
- Engineering review if out of tolerance

### Standard Tolerances
- ±0.1 mm to ±0.5 mm
- Normal production tolerances
- Sample inspection acceptable
- Standard disposition procedures

### General Tolerances
- ±0.5 mm or looser
- Non-critical features
- Reduced inspection frequency
- Standard acceptance procedures

## GD&T Tolerances

Supported geometric tolerances:
- **Form**: Straightness, flatness, circularity, cylindricity
- **Orientation**: Perpendicularity, parallelism, angularity
- **Location**: Position, concentricity, symmetry
- **Profile**: Profile of line, profile of surface
- **Runout**: Circular runout, total runout

## Tolerance Analysis

Consider:
- Tolerance stack-up at interfaces
- Worst-case vs. statistical analysis
- Manufacturing capability (Cp, Cpk)
- Measurement uncertainty
- Tolerance allocation strategy

## Related Directories

- **Datums**: [`../DATUMS/`](../DATUMS/)
- **Locations**: [`../LOCATIONS/`](../LOCATIONS/)
- **Drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)
