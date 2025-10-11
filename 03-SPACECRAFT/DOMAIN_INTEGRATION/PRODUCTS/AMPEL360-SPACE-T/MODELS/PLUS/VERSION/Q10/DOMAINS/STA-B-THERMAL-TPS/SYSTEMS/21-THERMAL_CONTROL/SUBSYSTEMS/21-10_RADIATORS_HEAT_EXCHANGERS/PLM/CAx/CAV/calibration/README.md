# CALIBRATION — Calibration Certificates and Traceability

## Purpose

This directory contains calibration certificates, schedules, and traceability records for all test instrumentation and measurement equipment.

## Contents

- Calibration certificates (NIST-traceable)
- Calibration schedules and due dates
- Equipment inventory and status
- Calibration procedures
- Out-of-tolerance notifications
- Uncertainty budgets
- Traceability chains to primary standards

## File Naming Convention

```
CAL_<equipment-id>_<date>_cert.{pdf|xlsx}
```

Examples:
- `CAL_TC-DAQ-001_20251011_cert.pdf`
- `CAL_PT-500PSI-05_20251012_cert.pdf`
- `CAL_RTD-READER-02_20251015_cert.pdf`

## Calibration Requirements

All measurement equipment must:
- ✅ Be calibrated to NIST-traceable standards
- ✅ Meet test accuracy requirements (typically 4:1 ratio)
- ✅ Be calibrated within specified intervals
- ✅ Have current, valid calibration certificates
- ✅ Be handled and stored properly

## Typical Calibration Intervals

Equipment-specific intervals:
- **Thermocouples**: 24 months or verification before test
- **RTDs**: 12 months
- **Pressure Transducers**: 12 months
- **Flow Meters**: 12 months
- **DAQ Systems**: 12 months
- **DMMs/Multimeters**: 12 months
- **Scales/Balances**: 12 months
- **After Impact/Drop**: Immediate recalibration required

## Calibration Accuracy Requirements

Measurement accuracy hierarchy:
```
Test Accuracy: ±1.0% (example)
Cal Accuracy: ±0.25% (4:1 ratio or better)
Standard Accuracy: ±0.0625% (4:1 ratio to cal)
```

## Calibration Certificate Content

Each certificate must include:
- Equipment identification and serial number
- Calibration date and due date
- Calibration standard used (with traceability)
- As-found and as-left readings
- Calibration points tested
- Uncertainty statement
- Environmental conditions
- Technician name and signature
- Accreditation (ISO 17025 or equivalent)

## Calibration Status Tracking

Maintain records of:
- Equipment ID and description
- Current calibration status
- Next calibration due date
- Location and responsible person
- Calibration interval
- Special requirements or notes

## Out-of-Tolerance Handling

If equipment found out-of-tolerance:
1. 🛑 Tag equipment "OUT OF SERVICE"
2. 📋 Document findings and date
3. 🔍 Review recent test data for impact
4. 📝 Issue NCR if test data affected
5. 🔧 Repair or replace equipment
6. ✅ Re-calibrate and verify
7. 📁 Document resolution

## Pre-Test Calibration Checks

Before each test:
- ✅ Verify all calibrations current
- ✅ Perform shunt calibration (strain gauges)
- ✅ Zero-check pressure transducers
- ✅ Verify DAQ channel calibrations
- ✅ Document cal status in test records

## Uncertainty Budgets

For critical measurements, document:
- Instrument uncertainty (from cal cert)
- Method uncertainty (repeatability)
- Environmental effects
- Resolution/quantization
- Combined uncertainty (RSS)
- Expanded uncertainty (k=2, 95% confidence)

## Calibration Vendors

Maintain list of approved calibration labs:
- Lab name and contact
- Accreditation (ISO 17025)
- Scope of accreditation
- Typical turnaround time
- Cost and terms

## Traceability Chain

Document traceability:
```
NIST Primary Standard
    ↓
Secondary Transfer Standard (Lab)
    ↓
Working Standard (Vendor)
    ↓
Test Equipment (User)
```

## Related Directories

- **[../setups/channel_maps/](../setups/channel_maps/)** — Equipment usage
- **[../tvac/](../tvac/)** — Test data using calibrated equipment
- **[../fai/](../fai/)** — FAI inspection equipment
- **[../anomalies/](../anomalies/)** — Out-of-cal issues

---

**Last Updated**: 2025-10-10
