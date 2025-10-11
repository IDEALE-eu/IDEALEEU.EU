# 📥 RAW DATA

**Path**: `DATA/raw/`  
**Purpose**: Immutable storage for raw sensor data ingestion

---

## 🎯 Overview

This directory stores **original, unmodified sensor data** from aircraft systems. Data here is **append-only** and serves as the source of truth for all downstream processing.

## 📂 Directory Structure

```
raw/
├── engine_vibration/
│   ├── 2025-10/
│   │   ├── AC001_20251011_120530.parquet
│   │   ├── AC001_20251011_130145.parquet
│   │   └── ...
│   └── 2025-11/
├── landing_gear/
│   └── (future data)
└── README.md (this file)
```

## 📋 Data Organization

### Naming Convention

```
<system>/<YYYY-MM>/<aircraft_id>_<YYYYMMDD_HHMMSS>.<format>
```

**Example**: `engine_vibration/2025-10/AC001_20251011_120530.parquet`

Where:
- `system`: ATA system category (e.g., `engine_vibration`, `landing_gear`)
- `YYYY-MM`: Year and month of data collection
- `aircraft_id`: Pseudonymized aircraft identifier (e.g., `AC001`, `AC042`)
- `YYYYMMDD_HHMMSS`: Timestamp of data collection
- `format`: File format (`.parquet`, `.csv`, `.tdms`)

### Supported Formats

| Format | Use Case | Compression |
|--------|----------|-------------|
| **Parquet** | Preferred for structured sensor data | Snappy (default) |
| **CSV** | Legacy data, human-readable exports | None or gzip |
| **TDMS** | National Instruments DAQ systems | Native |
| **HDF5** | High-frequency sensor arrays | Internal |

## 🔒 Data Immutability Rules

1. ✅ **Allowed**: Appending new data files
2. ❌ **Forbidden**: Modifying existing files
3. ❌ **Forbidden**: Deleting files (use retention policies instead)
4. ✅ **Allowed**: Adding metadata files (`.meta.json`)

## 📊 Data Ingestion Workflow

```
Aircraft Sensors → DAU → Data Bus → Ground Station
    ↓
Ingestion Service → Validation → DATA/raw/
    ↓
Quality Check → Log to ../interim/
```

### Step-by-Step Process

1. **Receive Data**: Aircraft transmits sensor data via ground link or post-flight download
2. **Validate Format**: Check file format, schema compatibility
3. **Validate Contract**: Verify against data contract in `../contracts/`
4. **Pseudonymize**: Replace tail number with aircraft ID
5. **Store Immutably**: Write to appropriate `<system>/<YYYY-MM>/` subdirectory
6. **Generate Metadata**: Create `.meta.json` with ingestion timestamp, checksums
7. **Log Ingestion**: Record in ingestion log for audit trail

## 🔍 Data Validation

Before storage, data is validated against contract specifications:

- **Schema Compliance**: Column names, types match contract
- **Range Checks**: Values within expected ranges
- **Sample Rate**: Verify data frequency matches specification
- **Completeness**: Check for expected number of samples
- **Integrity**: MD5 checksum verification

Failed validation → Data moved to `quarantine/` for review.

## 📝 Metadata Files

Each data file may have an accompanying metadata file:

**Example**: `AC001_20251011_120530.parquet.meta.json`

```json
{
  "aircraft_id": "AC001",
  "flight_id": "FL20251011-001",
  "ingestion_timestamp": "2025-10-11T12:10:45Z",
  "source": "ground_download",
  "data_contract_version": "1.0.0",
  "checksums": {
    "md5": "a1b2c3d4e5f6...",
    "sha256": "9876543210abcdef..."
  },
  "validation_status": "passed",
  "file_size_bytes": 2847392,
  "record_count": 36000,
  "duration_seconds": 3600,
  "ata_system": "ATA-72",
  "sensor_ids": ["VIB_FAN_001", "VIB_COMP_001", "VIB_TURB_001"]
}
```

## 🔐 Security & Privacy

- **Encryption**: All files encrypted at rest (AES-256)
- **Access Control**: Role-based access (ML Team, Data Engineering, Auditors)
- **Pseudonymization**: Aircraft tail numbers replaced with IDs
- **No PII**: No personally identifiable information stored
- **Audit Logging**: All access logged for compliance

## 📅 Retention Policy

| Data Age | Storage Tier | Retention |
|----------|--------------|-----------|
| 0-90 days | Hot (SSD) | Operational use |
| 91-730 days | Warm (HDD) | Compliance, retraining |
| 2-7 years | Cold (Archive) | Long-term compliance |
| 7+ years | Delete | Per regulatory requirements |

## 🚀 Quick Start

### Ingest New Data

```python
from tools.ingest import RawDataIngester

ingester = RawDataIngester(
    system="engine_vibration",
    contract_path="../contracts/signals_engine_vibration.yaml"
)

# Ingest from file
ingester.ingest_file(
    source_path="/path/to/flight_data.parquet",
    aircraft_id="AC001",
    flight_id="FL20251011-001"
)
```

### Query Raw Data

```python
import pandas as pd
from pathlib import Path

# Load data for specific aircraft and date range
data_files = Path("engine_vibration/2025-10").glob("AC001_*.parquet")
df = pd.concat([pd.read_parquet(f) for f in data_files])

print(f"Loaded {len(df)} records from {len(list(data_files))} files")
```

### Validate Ingested Data

```bash
# Run validation script
python ../../../TOOLS/validate_data.py \
    --system engine_vibration \
    --date 2025-10-11 \
    --aircraft AC001
```

## 📊 Data Quality Metrics

Track data quality metrics:

- **Ingestion Success Rate**: % of files successfully ingested
- **Validation Pass Rate**: % of files passing validation
- **Completeness**: % of expected data received
- **Timeliness**: Delay between flight end and data availability
- **Error Rate**: % of samples flagged as errors

Metrics tracked in: `../../EVALUATION/data_quality_dashboard/`

## 🆘 Troubleshooting

### Issue: File Not Ingested

**Check**:
1. File format compatible? (Parquet preferred)
2. Schema matches contract?
3. Permissions correct? (Read/write access)
4. Disk space available?

**Action**: Check ingestion logs in `/var/log/data_ingestion/`

### Issue: Validation Failed

**Check**:
1. Data contract version mismatch?
2. Values outside expected ranges?
3. Missing required columns?
4. Sample rate incorrect?

**Action**: Review validation report in `quarantine/<filename>.validation.json`

### Issue: Duplicate Data

**Check**:
1. Same flight ingested twice?
2. Checksum matches existing file?

**Action**: Use deduplication tool: `python ../../../TOOLS/deduplicate.py`

## 📚 Related Documentation

- **Data Contracts**: `../contracts/README.md`
- **Data Processing**: `../interim/README.md`
- **Quality Validation**: `../../../TOOLS/validate_data.py`
- **Ingestion API**: Internal API documentation
- **Retention Policy**: Company data governance policy

## 🔗 Integration Points

- **Source**: Aircraft Data Acquisition Units (DAU)
- **Consumers**: Preprocessing pipelines (`../interim/`)
- **Monitoring**: Data quality dashboard
- **Backup**: Automated daily backup to cloud archive

## ✅ Checklist for New System Integration

- [ ] Define data contract in `../contracts/`
- [ ] Create system subdirectory (e.g., `landing_gear/`)
- [ ] Configure ingestion pipeline
- [ ] Set up validation rules
- [ ] Test with sample data
- [ ] Document in this README
- [ ] Update retention policy
- [ ] Configure monitoring alerts

---

**Owner**: Data Engineering Team  
**Contact**: data-engineering@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
