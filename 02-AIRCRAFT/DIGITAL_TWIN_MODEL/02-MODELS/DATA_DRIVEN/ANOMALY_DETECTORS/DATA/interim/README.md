# 🧹 INTERIM DATA

**Path**: `DATA/interim/`  
**Purpose**: Cleaned and synchronized data ready for feature engineering

---

## 🎯 Overview

This directory contains **cleaned, synchronized, and quality-checked** sensor data. Data here has been validated, outliers handled, and time-synchronized across sensors.

## 📂 Directory Structure

```
interim/
├── engine_vibration/
│   ├── 2025-10/
│   │   ├── AC001_20251011_cleaned.parquet
│   │   ├── AC001_20251011_quality_report.json
│   │   └── ...
│   └── 2025-11/
├── landing_gear/
│   └── (future data)
└── README.md (this file)
```

## 🔄 Data Processing Pipeline

```
DATA/raw/ → Cleaning → Outlier Handling → Time Sync → DATA/interim/
                ↓           ↓                ↓
            Missing     3-sigma         Interpolation
             Values      Rule            & Alignment
```

## 🛠️ Processing Steps

### 1. Data Cleaning

**Operations**:
- Remove duplicate records (by timestamp)
- Handle missing values (interpolation or flagging)
- Correct sensor calibration offsets
- Remove initialization transients
- Flag sensor malfunctions

**Example**:
```python
# Before: Raw data with gaps
timestamp, vib_fan_rms
2025-10-11 12:00:00, 2.3
2025-10-11 12:00:01, NaN      # Missing value
2025-10-11 12:00:02, 2.5

# After: Cleaned data
timestamp, vib_fan_rms, quality_flag
2025-10-11 12:00:00, 2.3, VALID
2025-10-11 12:00:01, 2.4, INTERPOLATED  # Linear interpolation
2025-10-11 12:00:02, 2.5, VALID
```

### 2. Outlier Detection & Handling

**Method**: 3-sigma rule (configurable)

```python
# Outliers detected if:
|value - mean| > 3 * std_dev
```

**Handling Strategies**:
- **Remove**: For gross errors (>5σ)
- **Cap**: For moderate outliers (3-5σ)
- **Flag**: For inspection (keep original value, add flag)
- **Interpolate**: For isolated spikes

**Quality Flags**:
- `VALID`: Normal value
- `OUTLIER_CAPPED`: Value capped to 3σ
- `OUTLIER_REMOVED`: Value removed, interpolated
- `SENSOR_ERROR`: Suspected sensor malfunction

### 3. Time Synchronization

**Challenge**: Sensors sample at different rates

| Sensor | Rate | Sync Method |
|--------|------|-------------|
| Vibration | 100 Hz | Upsample/downsample to common rate |
| N1/N2 | 10 Hz | Linear interpolation |
| EGT | 10 Hz | Linear interpolation |
| Oil Pressure | 1 Hz | Forward fill |

**Output**: All signals aligned to common timebase (e.g., 10 Hz)

### 4. Gap Filling

**Policy** (per data contract):
- Gaps < 10 seconds: Linear interpolation
- Gaps ≥ 10 seconds: Mark as missing, no imputation
- Maximum 5% missing values per signal per flight

## 📊 Quality Reporting

Each cleaned file has an accompanying quality report:

**Example**: `AC001_20251011_quality_report.json`

```json
{
  "flight_id": "FL20251011-001",
  "aircraft_id": "AC001",
  "processing_timestamp": "2025-10-11T12:15:30Z",
  "raw_file": "../raw/engine_vibration/2025-10/AC001_20251011_120530.parquet",
  "interim_file": "engine_vibration/2025-10/AC001_20251011_cleaned.parquet",
  
  "quality_metrics": {
    "total_samples": 36000,
    "valid_samples": 35640,
    "missing_samples": 180,
    "outliers_detected": 180,
    "outliers_capped": 150,
    "outliers_removed": 30,
    "interpolated_samples": 210,
    "completeness_pct": 99.0
  },
  
  "per_signal_quality": {
    "vib_fan_rms": {
      "missing_pct": 0.5,
      "outlier_pct": 0.4,
      "mean": 2.35,
      "std": 0.82,
      "min": 0.1,
      "max": 8.2,
      "quality_score": 98.5
    },
    "n1": {
      "missing_pct": 0.0,
      "outlier_pct": 0.1,
      "mean": 68.5,
      "std": 18.2,
      "min": 0.0,
      "max": 105.0,
      "quality_score": 99.8
    }
  },
  
  "validation_status": "PASSED",
  "warnings": [
    "vib_fan_rms: 30 outliers removed (>5σ)",
    "n1: 5 samples capped to 105% (max limit)"
  ],
  "errors": []
}
```

## 📋 File Format

**Output Format**: Apache Parquet (column-oriented, compressed)

**Schema**:
```python
{
    "timestamp": datetime64[ns],
    "vib_fan_rms": float32,
    "vib_fan_rms_quality": str,  # Quality flag
    "vib_compressor_rms": float32,
    "vib_compressor_rms_quality": str,
    # ... other signals ...
    "n1": float32,
    "n1_quality": str,
    "flight_phase": uint8,
    "flight_phase_quality": str
}
```

Each signal has a corresponding `_quality` column with flags.

## 🔍 Quality Thresholds

Per data contract requirements:

| Metric | Threshold | Action if Failed |
|--------|-----------|------------------|
| Completeness | ≥95% | Flag for review |
| Outlier Rate | ≤1% | Flag for review |
| Interpolation Rate | ≤5% | Flag for review |
| Sensor Error Rate | ≤0.1% | Flag for review |

Failed thresholds → Data moved to `review/` subdirectory.

## 🚀 Quick Start

### Run Cleaning Pipeline

```python
from pipelines.training import preprocess

# Process raw data
preprocess.clean_raw_data(
    raw_path="../raw/engine_vibration/2025-10/AC001_20251011_120530.parquet",
    interim_path="engine_vibration/2025-10/AC001_20251011_cleaned.parquet",
    contract_path="../contracts/signals_engine_vibration.yaml",
    outlier_sigma=3.0,
    max_gap_seconds=10
)
```

### Load Cleaned Data

```python
import pandas as pd

# Load cleaned data
df = pd.read_parquet("engine_vibration/2025-10/AC001_20251011_cleaned.parquet")

# Check quality flags
print(df[df["vib_fan_rms_quality"] != "VALID"])

# Get only valid samples
df_valid = df[df["vib_fan_rms_quality"] == "VALID"]
```

### Generate Quality Report

```bash
python ../../../TOOLS/generate_quality_report.py \
    --interim engine_vibration/2025-10/AC001_20251011_cleaned.parquet \
    --output engine_vibration/2025-10/AC001_20251011_quality_report.json
```

## 📊 Quality Monitoring Dashboard

Track data quality trends over time:

- **Completeness Trend**: % complete samples per day/week
- **Outlier Rate Trend**: % outliers per sensor per day/week
- **Signal Health**: Color-coded sensor status (green/yellow/red)
- **Processing Time**: Time from raw → interim

Dashboard location: `../../EVALUATION/data_quality_dashboard/`

## 🆘 Troubleshooting

### Issue: High Outlier Rate

**Possible Causes**:
- Sensor calibration drift
- Environmental conditions (turbulence, high vibration flight)
- Sensor malfunction

**Action**:
1. Review outlier distribution (isolated vs. clustered)
2. Check maintenance records (recent sensor work?)
3. Compare with other aircraft in fleet
4. Consider recalibration or sensor replacement

### Issue: Low Completeness

**Possible Causes**:
- Communication dropouts
- DAU recording issues
- Sensor intermittent failures

**Action**:
1. Check data acquisition logs
2. Review communication link quality
3. Inspect sensor connections
4. Consider data recovery from backup systems

### Issue: Time Synchronization Errors

**Possible Causes**:
- Clock drift on DAU
- Incorrect timestamp parsing
- Timezone issues

**Action**:
1. Verify DAU clock synchronization
2. Check timestamp format in raw data
3. Review time sync algorithm parameters

## 🔧 Configuration

Cleaning parameters in: `../../PIPELINES/training/configs/preprocessing_config.yaml`

```yaml
outlier_detection:
  method: zscore
  threshold_sigma: 3.0
  handling: cap  # or 'remove', 'flag'

gap_filling:
  max_gap_seconds: 10
  method: linear  # or 'forward_fill', 'spline'

time_sync:
  target_sample_rate: 10 Hz
  interpolation_method: linear
  
quality_thresholds:
  min_completeness: 0.95
  max_outlier_rate: 0.01
  max_interpolation_rate: 0.05
```

## 📚 Related Documentation

- **Raw Data**: `../raw/README.md`
- **Feature Engineering**: `../processed/README.md`
- **Data Contracts**: `../contracts/README.md`
- **Quality Tools**: `../../../TOOLS/README.md`

## 🔗 Integration Points

- **Input**: `../raw/` (raw sensor data)
- **Output**: `../processed/` (windowed, normalized)
- **Quality Reports**: Logged to data quality dashboard
- **Alerts**: Email/Slack for quality threshold violations

## ✅ Processing Checklist

Before moving to feature engineering:

- [ ] All quality flags reviewed
- [ ] Completeness ≥95%
- [ ] Outlier rate ≤1%
- [ ] Time synchronization validated
- [ ] Quality report generated
- [ ] No critical errors
- [ ] Ready for windowing and feature extraction

---

**Owner**: Data Engineering Team  
**Contact**: data-engineering@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
