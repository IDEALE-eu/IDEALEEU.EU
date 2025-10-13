# CALIBRATION — Instrumentation and Equipment Calibration

## Purpose

This directory contains calibration certificates, schedules, and records for all test instrumentation, measurement systems, and test equipment.

## Directory Structure

### CERTS/
Calibration certificates:
- Load cell calibration certificates
- Strain gauge calibration factors
- Pressure transducer calibrations
- Temperature sensor calibrations
- Accelerometer calibrations
- DAQ system calibrations
- NIST-traceable calibration documents

### SCHEDULE/
Calibration schedules and planning:
- Annual calibration schedule
- Due date tracking
- Calibration frequency requirements
- Out-of-service equipment list
- Calibration vendor contacts
- Special calibration requirements

### RECORDS/
Calibration history and records:
- Historical calibration data
- Calibration trends and drift analysis
- Out-of-tolerance notifications
- Corrective action records
- Re-calibration documentation
- Equipment maintenance logs

## Calibration Standards

### Calibration Requirements
All measurement equipment must:
- Be calibrated to NIST-traceable standards
- Meet or exceed test accuracy requirements
- Be calibrated within specified intervals
- Have current calibration certificates
- Be handled and stored properly

### Typical Calibration Intervals
- **Load cells**: 12 months or after impact
- **Pressure transducers**: 12 months
- **Thermocouples**: 24 months or verification before each test
- **Strain gauges**: Factory calibration + shunt calibration
- **Accelerometers**: 24 months
- **DAQ systems**: 12 months

### Calibration Accuracy Requirements
Calibration accuracy should be at least 4:1 ratio to measurement requirement:
- Test measurement accuracy: ±1% of reading
- Calibration accuracy: ±0.25% of reading (or better)

## Calibration Process

### Pre-Test Calibration
1. Verify calibration certificates are current
2. Perform shunt calibration for strain gauges
3. Verify DAQ channel calibration factors
4. Document calibration status in test records
5. Tag all calibrated equipment

### Post-Test Verification
1. Re-check critical calibrations
2. Identify any calibration drift
3. Document calibration stability
4. Flag equipment for re-calibration if needed

## Calibration Documentation

Each calibration record should include:
- Equipment ID and serial number
- Calibration date and technician
- Calibration standard used (with traceability)
- As-found and as-left readings
- Calibration results and acceptance criteria
- Next calibration due date

## Out-of-Tolerance Handling

If equipment is found out-of-tolerance:
1. Tag equipment as "Out of Service"
2. Notify test director immediately
3. Review recent test data for impact
4. Document corrective action
5. Re-calibrate or replace equipment
6. Update calibration records

## Related Directories

- **Instrumentation**: [`../INSTRUMENTATION/`](../INSTRUMENTATION/)
- **Setup**: [`../SETUP/`](../SETUP/)
- **QA records**: [`../QA/`](../QA/)
- **CAV calibration**: [`../../../CAV/TEST_CAMPAIGNS/INSTRUMENTATION/`](../../../CAV/TEST_CAMPAIGNS/INSTRUMENTATION/)
