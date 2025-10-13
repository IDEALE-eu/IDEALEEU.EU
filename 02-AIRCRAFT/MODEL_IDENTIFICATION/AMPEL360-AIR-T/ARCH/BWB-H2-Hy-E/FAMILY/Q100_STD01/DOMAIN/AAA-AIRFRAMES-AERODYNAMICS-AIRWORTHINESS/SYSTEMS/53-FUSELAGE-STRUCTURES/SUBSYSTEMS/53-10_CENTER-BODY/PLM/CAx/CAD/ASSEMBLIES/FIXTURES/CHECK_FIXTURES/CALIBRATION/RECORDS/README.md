# RECORDS — Calibration History Records

## Purpose

This directory contains historical calibration records and tracking data for check fixtures and inspection equipment.

## Contents

### Record Types
- **Calibration history logs**: Chronological calibration records
- **Equipment history files**: Complete life history per equipment
- **Out-of-tolerance reports**: Non-conformance investigations
- **Calibration trends**: Statistical analysis and trends

## Naming Convention

Use the following pattern:
```
RECORD_<equipment-id>_HISTORY_<version>.xlsx
```

Examples:
- `RECORD_FIX-CHECK-F05_HISTORY_v01.xlsx`
- `RECORD_CMM-001_HISTORY_v02.xlsx`
- `RECORD_PIN-GAGE-SET-01_HISTORY_v01.xlsx`

## Record Format

### Equipment History Record
| Date | Type | Cert # | Lab | Result | Next Due | Notes |
|------|------|--------|-----|--------|----------|-------|
| 2024-01-15 | Annual | CAL-001234 | Acme Lab | Pass | 2025-01-15 | All points within tolerance |
| 2023-01-10 | Annual | CAL-000987 | Acme Lab | Pass | 2024-01-10 | Normal wear observed |

### Required Fields
- **Calibration date**: When performed
- **Calibration type**: Annual, semi-annual, special
- **Certificate number**: Reference to certificate
- **Laboratory**: Who performed calibration
- **Result**: Pass, fail, adjusted
- **Next due date**: When recalibration required
- **Technician**: Person who performed calibration
- **Notes**: Observations, adjustments, issues

## Historical Analysis

### Trend Monitoring
- Track measurement drift over time
- Identify equipment degradation
- Predict maintenance needs
- Optimize calibration intervals
- Identify systematic issues

### Performance Metrics
- On-time calibration rate
- Pass rate on first attempt
- Out-of-tolerance frequency
- Average time in calibration
- Cost per calibration

## Out-of-Tolerance Records

When equipment fails calibration:
1. Document as-found condition
2. Investigate root cause
3. Assess impact on measurements
4. Review recent inspection results
5. Document corrective actions
6. Update equipment record
7. Implement preventive measures

### Impact Assessment
- Identify affected measurements
- Review since last calibration
- Determine if re-inspection needed
- Notify affected parties
- Document disposition

## Record Retention

Calibration records must be:
- Maintained for equipment lifetime + 10 years
- Available for audit and review
- Backed up and protected
- Traceable to equipment and measurements
- Accessible to authorized personnel

## Related Directories

- **Certificates**: [`../CERTS/`](../CERTS/)
- **Schedule**: [`../SCHEDULE/`](../SCHEDULE/)
- **Run data**: [`../../RUN_DATA/`](../../RUN_DATA/)
