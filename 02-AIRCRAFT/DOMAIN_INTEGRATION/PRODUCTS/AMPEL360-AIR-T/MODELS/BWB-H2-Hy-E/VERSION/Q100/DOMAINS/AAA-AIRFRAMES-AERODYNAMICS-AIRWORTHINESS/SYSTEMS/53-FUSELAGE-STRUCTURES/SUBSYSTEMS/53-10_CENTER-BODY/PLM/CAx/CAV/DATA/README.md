# DATA — Test Data Management

## Purpose

This directory manages all test data collected during validation campaigns, from raw acquisition through processed results and archival.

## Directory Structure

### RAW/
Unprocessed data as acquired from instrumentation:
- Time-history data files
- High-speed video and imagery
- Sensor logs and raw measurements
- Equipment output files in native formats

**Naming Convention**: `RAW/[CAMPAIGN_ID]/[TEST_ID]/[DATE]_[SENSOR]_[RUN].ext`

**Storage**: Use Git LFS for binary files >100MB

### PROCESSED/
Analyzed and processed test results:
- Filtered and calibrated data
- Derived quantities (stress, strain, frequency response)
- Statistical summaries
- Extracted features and metrics

**Naming Convention**: `PROCESSED/[CAMPAIGN_ID]/[TEST_ID]/[ANALYSIS_TYPE]_[DATE].ext`

### METADATA/
Test metadata and conditions:
- Test configuration files
- Environmental conditions log
- Test article state and modifications
- Instrumentation setup and calibration records
- Data quality flags and notes

**Required Files**:
- `TEST_CONFIG.json` — Test setup configuration
- `INSTRUMENTATION.json` — Sensor locations and calibrations
- `CONDITIONS.csv` — Environmental conditions during test
- `QUALITY.md` — Data quality assessment

### LOGS/
Test execution logs and event records:
- Test procedure execution logs
- System event logs
- Anomaly and incident logs
- Real-time operator notes
- Automated data quality checks

## Data Quality Standards

All data must include:
1. **Traceability** — Link to test procedure, test article, and campaign
2. **Timestamp** — UTC timestamp for all measurements
3. **Calibration** — Current calibration records for sensors
4. **Quality Flags** — Data quality assessment and flags
5. **Units** — Clear units for all measurements
6. **Uncertainty** — Measurement uncertainty estimates

## File Formats

### Preferred Formats (Long-term archival)
- **Tabular data**: CSV, HDF5
- **Images**: PNG, TIFF (uncompressed)
- **Video**: MP4 (H.264), AVI (uncompressed)
- **Metadata**: JSON, YAML, XML

### Acceptable Formats
- Native instrument formats with documented converters
- Common engineering formats (TDMS, MAT, NPY)

### Avoid
- Proprietary formats without export capability
- Formats requiring specific software versions
- Encrypted or DRM-protected formats

## Data Retention

- **Raw Data**: Permanent retention (certification record)
- **Processed Data**: Permanent retention
- **Intermediate Files**: 2 years minimum
- **Logs**: Permanent retention

## Access and Security

- Test data classified as company confidential
- Access controlled via repository permissions
- Export-controlled data (ITAR/EAR) marked and segregated
- Personal data (if any) handled per GDPR

## Backup and Archival

- Continuous backup via Git repository
- Monthly backup to offline storage
- Long-term archive to institutional repository
- Checksums verified quarterly

## Data Processing Pipeline

1. **Acquisition** — Raw data from instruments → `RAW/`
2. **Quality Check** — Validate completeness and quality → `METADATA/`
3. **Processing** — Apply calibrations, filters, analysis → `PROCESSED/`
4. **Review** — Engineering review of results
5. **Archival** — Commit to repository with metadata
6. **Reporting** — Generate test reports with processed data

## References

- Acquisition scripts: `../../SCRIPTS/ACQ/`
- Processing scripts: `../../SCRIPTS/PROCESSING/`
- Test reports: `../../REPORTS/TEST_REPORTS/`
- Metadata standards: `METADATA/STANDARDS.md`

---

**Owner**: Data Management Lead  
**Backup Schedule**: Daily automated, monthly offline  
**Review Cycle**: Continuous during campaigns, quarterly audit
