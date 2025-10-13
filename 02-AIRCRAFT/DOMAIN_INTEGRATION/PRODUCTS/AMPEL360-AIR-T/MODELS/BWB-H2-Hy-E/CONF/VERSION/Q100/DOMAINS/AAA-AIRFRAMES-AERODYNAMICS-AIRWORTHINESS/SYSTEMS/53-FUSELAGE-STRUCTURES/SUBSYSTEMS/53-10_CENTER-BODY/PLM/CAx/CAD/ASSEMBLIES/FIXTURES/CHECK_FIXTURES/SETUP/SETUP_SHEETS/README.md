# SETUP_SHEETS — Setup Configuration Sheets

## Purpose

This directory contains setup sheets used to document fixture configuration and verification during setup operations.

## Contents

### Setup Sheet Types
- **Initial setup sheets**: First-time configuration records
- **Daily setup sheets**: Routine verification records
- **Calibration setup sheets**: Post-calibration verification
- **Troubleshooting logs**: Issue resolution records

## Naming Convention

Use the following pattern:
```
SETUP_SHEET_<fixture-id>_<date>_<serial>.xlsx
```

Examples:
- `SETUP_SHEET_FIX-CHECK-F05_2024-01-15_001.xlsx`
- `SETUP_SHEET_FIX-CHECK-WING-INT_2024-02-20_002.xlsx`
- `SETUP_SHEET_FIX-CHECK-SKIN_2024-03-10_001.xlsx`

## Setup Sheet Contents

Each setup sheet should record:
- **Header information**: Date, operator, fixture ID
- **Pre-setup checks**: Calibration status, cleanliness
- **Setup parameters**: Position, alignment, leveling
- **Verification measurements**: Datum checks, probe verification
- **Pass/fail criteria**: Acceptance limits
- **Sign-off**: Operator and inspector signatures
- **Notes**: Any deviations or observations

## Setup Sheet Format

### Header Section
- Setup date and time
- Operator name and ID
- Fixture identification
- Part number being inspected
- Calibration due date

### Setup Verification Section
- Datum reference checks
- Alignment measurements
- Leveling readings
- Probe/gauge verification
- Pass/fail status

### Sign-off Section
- Operator signature and date
- Inspector signature and date
- Notes and comments

## Quality Requirements

Setup sheets must be:
- Completed for each setup operation
- Signed by authorized personnel
- Filed and retained per quality procedures
- Available for audit and traceability

## Related Directories

- **Procedures**: [`../PROCEDURES/`](../PROCEDURES/)
- **Run data**: [`../../RUN_DATA/`](../../RUN_DATA/)
- **Calibration records**: [`../../CALIBRATION/RECORDS/`](../../CALIBRATION/RECORDS/)
