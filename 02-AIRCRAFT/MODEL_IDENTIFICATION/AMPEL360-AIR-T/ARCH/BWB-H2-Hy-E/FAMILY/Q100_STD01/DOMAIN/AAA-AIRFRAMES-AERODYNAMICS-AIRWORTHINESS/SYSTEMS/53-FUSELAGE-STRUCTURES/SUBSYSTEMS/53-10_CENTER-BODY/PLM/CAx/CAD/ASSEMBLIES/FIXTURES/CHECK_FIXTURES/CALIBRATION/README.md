# CALIBRATION — Calibration Records and Schedules

## Purpose

This directory contains calibration certificates, schedules, and records for check fixtures and inspection equipment.

## Contents

### Subdirectories
- **[CERTS/](./CERTS/)** — Calibration certificates
- **[SCHEDULE/](./SCHEDULE/)** — Calibration schedules
- **[RECORDS/](./RECORDS/)** — Calibration history records

## Calibration Requirements

### Equipment Requiring Calibration
- Check fixtures
- CMM systems and probes
- Laser trackers
- Gauges (pin, plug, go/no-go)
- Measurement instruments (calipers, micrometers)
- Reference standards

## Calibration Standards

Follow:
- **ISO/IEC 17025**: Testing and calibration laboratories
- **ANSI/NCSL Z540.3**: Calibration laboratories and measuring equipment
- **ISO 10012**: Measurement management systems
- **AS9102**: First Article Inspection (calibration requirements)

## Calibration Frequency

### Standard Frequencies
- **Check fixtures**: Annually or per usage
- **CMM systems**: Semi-annually
- **Laser trackers**: Quarterly
- **Pin gauges Class X**: Annually
- **Pin gauges Class XX**: Semi-annually
- **Pin gauges Class XXX**: Quarterly
- **Reference standards**: Per manufacturer recommendation

### Trigger Events
- Scheduled due date
- After damage or suspect results
- After major repair or modification
- Before critical measurements
- Per customer requirements

## Calibration Traceability

All calibration must be traceable to:
- National standards (NIST, NPL, PTB)
- Certified reference standards
- Accredited calibration laboratories
- ISO/IEC 17025 accreditation

## Out-of-Tolerance Handling

If equipment found out of tolerance:
1. Tag and remove from service
2. Quarantine affected measurements
3. Investigate root cause
4. Review measurements since last calibration
5. Document corrective actions
6. Recalibrate after repair
7. Update records

## Related Directories

- **Setup procedures**: [`../SETUP/`](../SETUP/)
- **Run data**: [`../RUN_DATA/`](../RUN_DATA/)
- **QA checks**: [`../QA/`](../QA/)
