# CHECKS — Quality Control Checks

## Purpose

This directory contains quality control check records and verification data for check fixture operations.

## Contents

### Check Types
- **Pre-use fixture checks**: Daily verification before use
- **Periodic fixture verification**: Scheduled accuracy checks
- **Post-maintenance checks**: Verification after repair
- **Calibration verification**: Confirm calibration status
- **Setup verification**: Confirm proper setup
- **Process capability studies**: Measure and verify process performance

## Naming Convention

Use the following pattern:
```
QC_CHECK_<fixture-id>_<check-type>_<date>.xlsx
```

Examples:
- `QC_CHECK_FIX-CHECK-F05_PRE-USE_2024-01-15.xlsx`
- `QC_CHECK_CMM-001_PERIODIC_2024-02-20.xlsx`
- `QC_CHECK_FIX-CHECK-WING-INT_POST-MAINT_2024-03-10.xlsx`

## Check Procedures

### Pre-Use Fixture Checks
Performed daily or before each use:
- Visual inspection for damage
- Verify calibration status (not expired)
- Check locating features for wear
- Verify datum references
- Confirm cleanliness
- Test measurement instruments
- Document results

### Periodic Fixture Verification
Performed monthly or per schedule:
- Dimensional accuracy check
- Datum reference verification
- Locating feature inspection
- Measurement repeatability study
- Wear assessment
- Overall condition evaluation
- Corrective actions if needed

### Post-Maintenance Checks
After any repair or modification:
- Re-verify dimensional accuracy
- Confirm calibration
- Test functionality
- Compare to baseline data
- Approve for return to service
- Update records

## Check Documentation

### Check Record Contents
- **Date and time**: When performed
- **Inspector**: Who performed check
- **Fixture ID**: Equipment checked
- **Check type**: Pre-use, periodic, etc.
- **Criteria**: What was checked
- **Results**: Pass/fail for each item
- **Measurements**: Actual data
- **Actions**: Corrective actions taken
- **Approval**: Sign-off

## Pass/Fail Criteria

### Acceptance Criteria
- Fixture dimensions within tolerance (±0.1mm typical)
- No visible damage or excessive wear
- Calibration current
- All components functional
- Locating features in good condition
- Measurement repeatability acceptable

### Failure Response
If fixture fails check:
1. Tag and remove from service
2. Document failure mode
3. Investigate cause
4. Determine if parts inspected are affected
5. Repair or replace fixture
6. Re-verify before returning to service
7. Update records

## Statistical Process Control

### Process Monitoring
- Control charts for key measurements
- Track trends over time
- Detect process shifts
- Identify out-of-control conditions
- Trigger investigation and correction

### Capability Studies
- Measure process capability (Cp, Cpk)
- Verify fixture accuracy
- Confirm measurement system capability
- Document capability for critical characteristics

## Check Retention

Quality check records must be:
- Filed and indexed
- Retained for minimum 10 years
- Available for audit
- Linked to fixture and inspection records
- Backed up electronically

## Continuous Improvement

Use check data to:
- Identify improvement opportunities
- Optimize check frequency
- Update acceptance criteria
- Improve fixture design
- Enhance procedures
- Train personnel

## Related Directories

- **Calibration**: [`../../CALIBRATION/`](../../CALIBRATION/)
- **Setup procedures**: [`../../SETUP/`](../../SETUP/)
- **Reports**: [`../../REPORTS/`](../../REPORTS/)
