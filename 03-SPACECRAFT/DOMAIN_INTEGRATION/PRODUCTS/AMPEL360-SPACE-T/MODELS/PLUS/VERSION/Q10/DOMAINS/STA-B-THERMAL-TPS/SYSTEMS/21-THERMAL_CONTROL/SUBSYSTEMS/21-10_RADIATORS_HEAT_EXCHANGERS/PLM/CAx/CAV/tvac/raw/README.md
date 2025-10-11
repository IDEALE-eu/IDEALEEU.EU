# RAW — Raw TVAC Data

## Purpose

This directory contains unprocessed raw data files from TVAC testing, including time-series measurements and chamber logs.

## Contents

- Time-series temperature data (CSV, Parquet, TDMS)
- Chamber pressure logs
- Heater power profiles
- Thermal shroud temperature logs
- DAQ system output files
- Chamber control system logs
- Event logs and operator notes

## File Naming Convention

```
<test-id>_<serial>_<phase>_<date>_RAW.<ext>
```

Examples:
- `TVAC-001_RAD-SN001_hot_survival_20251011_RAW.csv`
- `TVAC-002_HX-SN005_cold_soak_20251012_RAW.parquet`
- `TVAC-003_CP123_thermal_cycle_20251015_RAW.tdms`

## Data Formats

### CSV Format
Plain text comma-separated values:
- Easy to read and process
- Large file sizes
- Human-readable

### Parquet Format
Columnar binary format:
- Efficient storage and fast queries
- Compressed
- Good for large datasets

### TDMS Format
National Instruments format:
- Native DAQ format
- Includes metadata
- Requires TDMS reader

## Data Content

Each raw data file should include:
- **Timestamp**: Absolute time (ISO 8601)
- **Elapsed Time**: Seconds from test start
- **All Channels**: Every sensor channel recorded
- **Sample Rate**: Consistent with channel map
- **Metadata**: Test ID, serial number, configuration

## Data Integrity

Raw data must be:
- 🔒 **Immutable** — Never modify raw files
- 📋 **Complete** — No gaps or missing channels
- 🔐 **Backed up** — Multiple copies immediately after test
- ✅ **Validated** — Checksums or file verification
- 📝 **Documented** — Metadata and test log references

## Storage Requirements

- Store on multiple media/locations
- Maintain backup copies off-site
- Archive for program lifetime + retention period
- Document data file locations

## Data Security

- Restrict access to authorized personnel
- Maintain data access log
- Follow data classification guidelines
- Use secure file transfer methods

## Related Directories

- **[../reduced/](../reduced/)** — Processed data
- **[../plots/](../plots/)** — Data visualization
- **[../../setups/channel_maps/](../../setups/channel_maps/)** — Channel definitions

---

**Last Updated**: 2025-10-10
