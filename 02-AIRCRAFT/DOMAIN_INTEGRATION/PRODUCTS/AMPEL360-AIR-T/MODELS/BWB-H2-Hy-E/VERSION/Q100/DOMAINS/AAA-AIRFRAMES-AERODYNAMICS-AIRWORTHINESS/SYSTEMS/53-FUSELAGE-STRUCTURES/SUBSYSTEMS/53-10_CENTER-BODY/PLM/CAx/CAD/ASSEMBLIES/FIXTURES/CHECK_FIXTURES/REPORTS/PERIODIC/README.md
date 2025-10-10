# PERIODIC — Periodic Inspection Reports

## Purpose

This directory contains periodic inspection reports for ongoing production and maintenance verification.

## Contents

### Report Types
- **Production inspection reports**: Routine part verification
- **Fixture verification reports**: Periodic fixture accuracy checks
- **Process monitoring reports**: Statistical process control
- **Trend analysis reports**: Long-term performance tracking
- **Audit reports**: Internal and external audit findings

## Naming Convention

Use the following pattern:
```
PERIODIC_<part-id>_<period>_<version>.pdf
```

Examples:
- `PERIODIC_FRAME-F05_2024-Q1_v01.pdf`
- `PERIODIC_WING-INTERFACE_2024-01_v02.pdf`
- `PERIODIC_FIXTURE-VERIFICATION_2024-Q1_v01.pdf`

## Inspection Frequency

### Standard Frequencies
- **Daily**: High-volume production, critical parts
- **Weekly**: Regular production items
- **Monthly**: Lower volume production
- **Quarterly**: Low volume or stable processes
- **Annual**: Fixture and tooling verification

### Trigger Events
- Scheduled interval
- Process change
- Quality alert
- Customer request
- After corrective action

## Report Contents

Each periodic report should include:
- **Period covered**: Date range
- **Parts inspected**: Part numbers and quantities
- **Inspection results**: Summary of pass/fail
- **Statistical data**: Cp, Cpk, trends
- **Non-conformances**: Issues found
- **Corrective actions**: Actions taken
- **Trends**: Comparison to previous periods
- **Recommendations**: Process improvements

## Report Sections

### Summary Section
- Period and scope
- Total parts inspected
- Overall pass rate
- Key findings
- Action items

### Statistical Analysis
- Process capability (Cp, Cpk)
- Control charts
- Trend analysis
- Histogram and distribution
- Comparison to specifications

### Non-Conformance Section
- Number and type of defects
- Root cause analysis
- Corrective actions
- Preventive actions
- Effectiveness verification

### Recommendations
- Process improvements
- Tooling adjustments
- Training needs
- Procedure updates

## Fixture Verification

Periodic fixture checks include:
- Dimensional accuracy verification
- Wear inspection
- Datum reference check
- Locating feature verification
- Overall condition assessment
- Calibration status

## Quality Monitoring

### Key Metrics
- First pass yield
- Defect rate by type
- Process capability indices
- Inspection cycle time
- Cost of quality

### Trend Analysis
- Month-over-month comparison
- Year-over-year comparison
- Seasonal variations
- Process improvements impact

## Related Directories

- **First article reports**: [`../FIRST_ARTICLE/`](../FIRST_ARTICLE/)
- **Run data**: [`../../RUN_DATA/`](../../RUN_DATA/)
- **QA checks**: [`../../QA/CHECKS/`](../../QA/CHECKS/)
