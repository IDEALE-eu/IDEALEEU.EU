# LAYOUTS — Laser Tracker Measurement Layouts

## Purpose

This directory contains measurement layout files that define the sequence and configuration of laser tracker measurements.

## Contents

### Layout Types
- **Inspection layouts**: Part measurement sequences
- **Setup layouts**: Fixture alignment measurements
- **Verification layouts**: Periodic fixture checks
- **Assembly layouts**: Large assembly measurements

## Naming Convention

Use the following pattern:
```
LAYOUT_<fixture-id>_<measurement-type>_<version>.<ext>
```

Examples:
- `LAYOUT_FIX-CHECK-F05_INSPECTION_v01.job`
- `LAYOUT_FIX-CHECK-WING-INT_SETUP_v02.job`
- `LAYOUT_FIX-CHECK-SKIN_VERIFICATION_v01.plan`

## Layout File Formats

### Supported Formats
- **Leica**: `.job`, `.plan`
- **FARO**: `.plan`, `.fls`
- **API**: `.plan`, `.job`
- **Hexagon**: `.job`
- **Generic**: `.txt`, `.csv`

## Layout Contents

Each layout file should define:
- **Target sequence**: Order of measurement
- **Reference targets**: Coordinate system definition
- **Measurement points**: Feature locations
- **Tolerances**: Acceptance criteria
- **Output format**: Report generation settings
- **Notes**: Special instructions

## Measurement Workflow

### Standard Workflow
1. Load layout file in tracker software
2. Initialize tracker and verify compensation
3. Measure reference targets to establish coordinate system
4. Measure part/fixture targets per layout sequence
5. Compare measured data to nominal values
6. Generate deviation report
7. Save results and export data

## Best Practices

- Use consistent coordinate system across layouts
- Include redundant reference targets
- Document target accessibility
- Verify layout with dry run
- Maintain version control
- Update when design changes

## Related Directories

- **Targets**: [`../TARGETS/`](../TARGETS/)
- **Reports**: [`../REPORTS/`](../REPORTS/)
- **Check points**: [`../../CHECK_POINTS/`](../../CHECK_POINTS/)
