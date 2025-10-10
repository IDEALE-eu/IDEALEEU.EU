# MEASUREMENTS — Measurement Data Files

## Purpose

This directory contains raw and processed measurement data from inspection operations.

## Contents

### Data Types
- **CMM data files**: Native measurement software formats
- **Laser tracker data**: Point cloud and coordinate files
- **Gauge readings**: Manual measurement records
- **SPC data**: Statistical process control data
- **Exported data**: CSV, Excel formats for analysis

## Naming Convention

Use the following pattern:
```
MEAS_<part-id>_<serial>_<date>_<time>.<ext>
```

Examples:
- `MEAS_FRAME-F05_S001_2024-01-15_143025.dmis`
- `MEAS_WING-INTERFACE_S002_2024-02-20_091530.pts`
- `MEAS_SKIN-PANEL-001_S003_2024-03-10_105045.xlsx`

## File Formats

### CMM Data Formats
- **DMIS**: `.dmis` (standard)
- **PC-DMIS**: `.pcdmis`, `.mea`
- **Calypso**: `.pgm`, `.dat`
- **Export**: `.txt`, `.csv`, `.xlsx`

### Laser Tracker Formats
- **Point cloud**: `.pts`, `.xyz`, `.asc`
- **Leica**: `.lgs`, `.lcs`
- **FARO**: `.fls`, `.faro`
- **API**: `.pts`, `.xyz`

### Gauge Data Formats
- **Spreadsheet**: `.xlsx`, `.csv`
- **Database**: Access to MES/QMS system
- **Text**: `.txt` for simple data

## Data Contents

Each measurement file should contain or reference:
- **Header information**: Part ID, serial number, date, operator
- **Equipment info**: CMM/tracker ID, calibration status
- **Coordinate system**: Datum reference frame
- **Measured points**: X, Y, Z coordinates
- **Nominal values**: Design intent dimensions
- **Deviations**: Actual minus nominal
- **Tolerances**: Acceptance limits
- **Pass/fail status**: For each feature

## Data Organization

### Directory Structure
```
MEASUREMENTS/
├── 2024/
│   ├── 2024-01/
│   │   ├── FRAME-F05/
│   │   └── WING-INTERFACE/
│   ├── 2024-02/
│   └── 2024-03/
└── Archive/
```

### Organization by:
- Year and month
- Part type
- Serial number
- Inspection type

## Data Processing

### Raw Data
- Preserve original measurement files
- No modifications allowed
- Read-only after creation
- Backed up immediately

### Processed Data
- Analysis results
- Statistical summaries
- Derived calculations
- Comparison to specifications

## Data Validation

Verify that measurement data:
- Matches part serial number
- References correct coordinate system
- Has complete header information
- Passes format validation checks
- Is linked to inspection report

## Related Directories

- **Logs**: [`../LOGS/`](../LOGS/)
- **CMM programs**: [`../../CMM/PROGRAMS/`](../../CMM/PROGRAMS/)
- **Reports**: [`../../REPORTS/`](../../REPORTS/)
