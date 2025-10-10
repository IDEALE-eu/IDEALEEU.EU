# CERTS — Calibration Certificates

## Purpose

This directory contains calibration certificates for check fixtures and inspection equipment.

## Contents

### Certificate Types
- **Fixture calibration certificates**: Check fixture accuracy verification
- **Equipment calibration certificates**: CMM, laser tracker, gauges
- **Reference standard certificates**: Master standards and artifacts
- **Traceability certificates**: Chain of traceability documentation

## Naming Convention

Use the following pattern:
```
CERT_<equipment-id>_<cal-date>_<cert-number>.pdf
```

Examples:
- `CERT_FIX-CHECK-F05_2024-01-15_CAL-001234.pdf`
- `CERT_CMM-001_2024-02-20_CAL-002345.pdf`
- `CERT_PIN-GAGE-SET-01_2024-03-10_CAL-003456.pdf`

## Certificate Requirements

Each calibration certificate must include:
- **Certificate number**: Unique identifier
- **Equipment ID**: Device being calibrated
- **Calibration date**: Date of calibration
- **Next due date**: When recalibration is required
- **Calibration laboratory**: Name and accreditation
- **Standards used**: Traceability information
- **Measurement results**: As-found and as-left data
- **Uncertainties**: Measurement uncertainty statement
- **Pass/fail status**: Conformance to specifications
- **Technician signature**: Calibrated by
- **Approval signature**: Reviewed and approved by

## Certificate Format

### Header Section
- Laboratory name and logo
- Certificate number
- Accreditation number (ISO/IEC 17025)
- Issue date

### Equipment Section
- Equipment description
- Manufacturer and model
- Serial number
- Asset/ID number
- Location

### Calibration Section
- Calibration date
- Procedure reference
- Environmental conditions
- Standards used with cert numbers
- Measurement uncertainty

### Results Section
- Test points measured
- As-found data
- As-left data (if adjusted)
- Tolerance limits
- Pass/fail for each point

### Traceability Section
- Chain of traceability to national standards
- Reference standard cert numbers
- Calibration hierarchy

### Approval Section
- Technician name and signature
- Date performed
- Reviewer/approver signature
- Next calibration due date

## Certificate Retention

Certificates must be:
- Retained for equipment lifetime + 10 years
- Readily available for audit
- Backed up electronically
- Traceable to equipment and measurements

## Related Directories

- **Schedule**: [`../SCHEDULE/`](../SCHEDULE/)
- **Records**: [`../RECORDS/`](../RECORDS/)
- **QA documentation**: [`../../QA/`](../../QA/)
