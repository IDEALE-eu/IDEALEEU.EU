# REPORTS — CMM Measurement Reports

## Purpose

This directory contains measurement reports generated from CMM inspection operations.

## Contents

### Report Types
- **Inspection reports**: Detailed measurement results
- **Summary reports**: Pass/fail summary with key dimensions
- **Trend reports**: Historical measurement data
- **Non-conformance reports**: Out-of-tolerance findings

## Naming Convention

Use the following pattern:
```
CMM_REPORT_<part-id>_<serial>_<date>.pdf
```

Examples:
- `CMM_REPORT_FRAME-F05_S001_2024-01-15.pdf`
- `CMM_REPORT_WING-INTERFACE_S002_2024-02-20.pdf`
- `CMM_REPORT_SKIN-PANEL-001_S003_2024-03-10.pdf`

## Report Contents

Each report should include:
- **Header**: Part ID, serial number, date, operator
- **Measurement summary**: Pass/fail status
- **Dimensional results**: Measured values vs. tolerances
- **GD&T results**: Geometric tolerances
- **Statistical data**: Cp, Cpk values if applicable
- **Graphical representations**: Deviation plots
- **Sign-off**: Inspector and engineer approval

## Report Format

### Title Section
- Report number and revision
- Part number and description
- Serial number
- Measurement date
- CMM operator

### Results Section
- Feature-by-feature measurements
- Nominal, actual, and deviation values
- Tolerance limits
- Pass/fail indication
- GD&T callouts with results

### Summary Section
- Overall pass/fail status
- Number of features checked
- Number of non-conformances
- Recommended actions

### Approval Section
- Inspector signature and date
- Quality engineer signature and date

## Quality Requirements

Reports must be:
- Generated automatically from CMM software
- Reviewed by quality inspector
- Approved by quality engineer
- Filed per retention requirements
- Traceable to inspection plan

## Related Directories

- **CMM programs**: [`../PROGRAMS/`](../PROGRAMS/)
- **Run data**: [`../../RUN_DATA/`](../../RUN_DATA/)
- **Reports**: [`../../REPORTS/`](../../REPORTS/)
