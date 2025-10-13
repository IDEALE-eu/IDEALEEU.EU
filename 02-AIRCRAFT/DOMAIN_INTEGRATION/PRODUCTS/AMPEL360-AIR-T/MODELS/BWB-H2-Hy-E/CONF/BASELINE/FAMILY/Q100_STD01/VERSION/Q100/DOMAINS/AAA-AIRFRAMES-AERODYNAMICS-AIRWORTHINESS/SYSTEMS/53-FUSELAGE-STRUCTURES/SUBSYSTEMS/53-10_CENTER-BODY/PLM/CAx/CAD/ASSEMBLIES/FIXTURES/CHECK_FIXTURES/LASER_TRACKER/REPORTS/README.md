# REPORTS — Laser Tracker Measurement Reports

## Purpose

This directory contains measurement reports generated from laser tracker inspection operations.

## Contents

### Report Types
- **Inspection reports**: Detailed measurement results with deviations
- **Alignment reports**: Fixture and assembly alignment verification
- **Certification reports**: Tooling and fixture certification
- **Trend reports**: Historical measurement tracking

## Naming Convention

Use the following pattern:
```
LT_REPORT_<part-id>_<serial>_<date>.pdf
```

Examples:
- `LT_REPORT_FRAME-F05_S001_2024-01-15.pdf`
- `LT_REPORT_WING-INTERFACE_S002_2024-02-20.pdf`
- `LT_REPORT_SKIN-PANEL-001_S003_2024-03-10.pdf`

## Report Contents

Each report should include:
- **Header**: Part ID, serial number, date, operator
- **Setup information**: Coordinate system definition, reference targets
- **Measurement summary**: Pass/fail status, number of points
- **Deviation data**: Measured vs. nominal with color-coded results
- **Statistical analysis**: Mean, standard deviation, max/min deviations
- **3D visualization**: Point cloud with deviation map
- **Sign-off**: Inspector and engineer approval

## Report Sections

### Title Section
- Report ID and revision
- Part number and description
- Serial number
- Measurement date and time
- Laser tracker operator
- Equipment ID and calibration status

### Coordinate System Section
- Reference target locations
- Coordinate transformation parameters
- Fit quality and uncertainty

### Results Section
- Point-by-point measurements
- X, Y, Z coordinates
- Deviation magnitude and direction
- Tolerance limits
- Pass/fail status

### Visual Section
- 3D deviation plots
- Color maps (green/yellow/red)
- Section views
- Comparison overlays

### Summary Section
- Overall pass/fail
- Statistics (mean, std dev, Cp/Cpk)
- Non-conformance listing
- Recommended actions

## Report Formats

- **PDF**: Primary distribution format
- **Excel**: Data analysis format
- **Native**: Leica, FARO, API formats for re-analysis
- **Point cloud**: `.pts`, `.xyz` for CAD comparison

## Quality Requirements

Reports must be:
- Generated from validated measurement
- Reviewed by quality inspector
- Approved by engineering
- Filed per retention policy
- Traceable to inspection plan

## Related Directories

- **Layouts**: [`../LAYOUTS/`](../LAYOUTS/)
- **Run data**: [`../../RUN_DATA/`](../../RUN_DATA/)
- **Reports**: [`../../REPORTS/`](../../REPORTS/)
