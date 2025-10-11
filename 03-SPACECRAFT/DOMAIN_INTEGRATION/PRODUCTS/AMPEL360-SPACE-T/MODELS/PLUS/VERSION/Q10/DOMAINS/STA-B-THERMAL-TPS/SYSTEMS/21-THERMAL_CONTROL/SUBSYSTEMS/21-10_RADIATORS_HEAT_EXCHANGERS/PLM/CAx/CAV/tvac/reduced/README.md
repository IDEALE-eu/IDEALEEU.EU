# REDUCED — Processed TVAC Data

## Purpose

This directory contains cleaned, processed, and synchronized TVAC datasets ready for analysis and reporting.

## Contents

- Cleaned time-series data
- Synchronized datasets (time-aligned channels)
- Filtered and noise-reduced data
- Derived parameters and metrics
- Statistical summaries
- Processed data in analysis-ready format

## File Naming Convention

```
<test-id>_<serial>_<phase>_<date>_REDUCED.<ext>
```

Examples:
- `TVAC-001_RAD-SN001_hot_survival_20251011_REDUCED.csv`
- `TVAC-002_HX-SN005_cold_soak_20251012_REDUCED.parquet`
- `TVAC-003_CP123_thermal_cycle_20251015_REDUCED.xlsx`

## Data Processing Steps

### 1. Data Cleaning
- Remove startup transients
- Flag and handle outliers
- Remove invalid data points
- Apply quality filters
- Document all deletions

### 2. Time Synchronization
- Align all channels to common time base
- Handle DAQ timing differences
- Interpolate to consistent sample rate
- Maintain temporal relationships

### 3. Filtering
- Apply low-pass filters to remove noise
- Smooth temperature data (moving average)
- Remove high-frequency artifacts
- Document filter parameters

### 4. Calibration Application
- Apply calibration factors
- Correct sensor offsets
- Convert to engineering units
- Verify unit consistency

### 5. Derived Parameters
Calculate and add:
- Temperature differences (∆T)
- Heat fluxes (Q)
- Thermal resistances
- Stability metrics
- Performance indices

## Data Quality Assurance

Processed data must:
- ✅ **Traceable** — Link to raw data source
- ✅ **Documented** — Processing steps logged
- ✅ **Validated** — Spot-checks against raw data
- ✅ **Complete** — All channels and time periods
- ✅ **Consistent** — Units and formats uniform

## Processing Documentation

For each reduced dataset, document:
- Processing script/tool used
- Filter parameters applied
- Outliers identified and handled
- Time synchronization method
- Calibration factors applied
- Quality flags and notes

## File Formats

### CSV
Human-readable, standard analysis tools.

### Parquet
Efficient for large datasets, fast queries.

### Excel/XLSX
Convenient for review and quick analysis.

## Metadata

Include metadata header or companion file:
- Test identification
- Raw data source file(s)
- Processing date and version
- Processing parameters
- Quality notes

## Related Directories

- **[../raw/](../raw/)** — Source raw data
- **[../plots/](../plots/)** — Visualization of processed data
- **[../../reports/](../../reports/)** — Analysis reports
- **[../../calibration/](../../calibration/)** — Calibration data used

---

**Last Updated**: 2025-10-10
