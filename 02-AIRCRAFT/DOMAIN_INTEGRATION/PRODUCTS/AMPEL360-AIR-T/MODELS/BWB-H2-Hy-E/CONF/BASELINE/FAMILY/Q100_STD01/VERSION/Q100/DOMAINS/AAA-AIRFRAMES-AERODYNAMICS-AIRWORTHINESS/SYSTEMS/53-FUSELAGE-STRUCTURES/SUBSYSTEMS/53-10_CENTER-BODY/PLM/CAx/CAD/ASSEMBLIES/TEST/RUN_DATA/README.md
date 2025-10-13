# RUN_DATA — Test Execution Data

## Purpose

This directory contains all data collected during test execution, including raw data files, processed results, and execution logs.

## Directory Structure

### RAW/
Raw unprocessed data files:
- DAQ system output files
- Strain gauge time histories
- Load cell readings
- Pressure transducer data
- Temperature sensor data
- Accelerometer data
- Video recordings
- Image files for DIC

### PROCESSED/
Processed and reduced data:
- Filtered and corrected data
- Engineering units conversions
- Statistical analysis results
- Peak/valley extraction
- Cycle counting results
- Correlation with predictions
- Derived parameters

### LOGS/
Test execution logs and notes:
- Test conductor logs
- Event time logs
- Anomaly reports
- Real-time observations
- Environmental conditions
- Personnel attendance
- Equipment status logs

## Data Management

### Raw Data Handling
- Store raw data in original format
- Make backup copies immediately after test
- Store on multiple media/locations
- Never modify raw data files
- Document data file naming conventions
- Maintain data file index

### Data File Naming Convention

```
<test-id>_<date>_<data-type>_<run-number>.<ext>
```

Examples:
- `53-10_STATIC_20250115_STRAIN_RUN01.tdms`
- `53-10_FATIGUE_20250120_LOAD_RUN03.csv`
- `53-10_PRESSURE_20250125_TEMP_RUN02.dat`

### Data Processing
- Document processing algorithms
- Maintain processing scripts/code
- Verify processed data against raw
- Document all corrections applied
- Maintain processing log
- Store processing parameters

## Data Quality Assurance

### Pre-Test Checks
- Verify data acquisition settings
- Check sampling rates and ranges
- Verify trigger configurations
- Test data file creation
- Check disk space availability

### During-Test Monitoring
- Monitor real-time data display
- Check for sensor dropouts
- Verify data recording
- Monitor file sizes
- Check for data anomalies

### Post-Test Verification
- Verify all channels recorded
- Check data file integrity
- Review data for quality
- Identify any missing data
- Document data quality issues

## Data Storage and Retention

### Short-Term Storage
- Local server storage during test campaign
- Backed up daily
- Accessible to test team

### Long-Term Archive
- Archive to secure storage within 30 days
- Maintain redundant copies
- Document archive location
- Follow data retention policy
- Minimum 20-year retention for flight hardware

## Data Security

- Restrict access to authorized personnel
- Maintain data access log
- Use secure file transfer methods
- Encrypt sensitive data
- Follow data classification guidelines

## Related Directories

- **Instrumentation**: [`../INSTRUMENTATION/`](../INSTRUMENTATION/)
- **Load cases**: [`../LOAD_CASES/`](../LOAD_CASES/)
- **Reports**: [`../REPORTS/`](../REPORTS/)
- **CAV data**: [`../../../CAV/DATA/`](../../../CAV/DATA/)
