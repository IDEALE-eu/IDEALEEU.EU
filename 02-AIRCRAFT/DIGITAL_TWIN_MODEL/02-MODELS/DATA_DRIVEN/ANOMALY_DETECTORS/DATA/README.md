# DATA Directory

**Purpose**: Central repository for all data used in anomaly detection model lifecycle.

## Directory Structure

```
DATA/
├─ contracts/              # Data schemas and signal definitions
├─ raw/                    # Immutable raw data ingestion
├─ interim/                # Cleaned and synchronized data
├─ processed/              # Windowed and preprocessed data
├─ features/               # Engineered features (.parquet, .npy)
└─ labels/                 # Ground truth and event labels
```

## Data Flow

```
Raw Sensors → contracts/ (validation) → raw/ (immutable storage)
    ↓
interim/ (cleaning, sync, quality checks)
    ↓
processed/ (windowing, normalization)
    ↓
features/ (feature engineering)
    ↓
Training Pipeline
```

## contracts/

Contains YAML data contracts defining:
- Signal definitions (name, unit, sample rate, range, type)
- Feature engineering specifications
- Data quality requirements
- Privacy and compliance rules
- ATA system references

**Example**: `signals_engine_vibration.yaml`

## raw/

Immutable storage of ingested sensor data:
- Original format preserved (Parquet, CSV, binary)
- No modifications allowed (append-only)
- Organized by date, aircraft, system
- Retention: 2 years operational, 7 years archived

**Naming Convention**: `<system>/<date>/<aircraft_id>_<timestamp>.parquet`

## interim/

Cleaned and synchronized data:
- Outliers removed (3-sigma rule)
- Missing values handled (interpolation or flagged)
- Time synchronization across sensors
- Quality flags added

## processed/

Preprocessed data ready for feature engineering:
- Windowing applied (e.g., 10-second windows, 5-second overlap)
- Normalization applied (z-score scaling)
- Flight phase annotations added
- Format: Parquet or NumPy arrays

## features/

Engineered features for model training:
- Time domain features (RMS, peak, mean, std)
- Frequency domain features (FFT components, spectral density)
- Temporal features (rate of change, moving averages)
- Format: Parquet (tabular) or NumPy (arrays)

**Storage**: Column-oriented Parquet for efficient querying

## labels/

Ground truth labels for supervised/semi-supervised learning:
- Anomaly labels (binary: normal/anomaly)
- Severity labels (minor, moderate, severe)
- Fault type labels (bearing wear, imbalance, etc.)
- Event timestamps
- Labeling provenance (expert, automated, maintenance records)

**Format**: CSV or Parquet with metadata

## Data Quality Requirements

Per data contract specifications:
- **Completeness**: ≥95% coverage
- **Consistency**: ≤1% outliers
- **Timeliness**: <500ms latency for real-time
- **Accuracy**: Annual sensor calibration

## Privacy and Security

- **No PII**: All data pseudonymized (aircraft_id, not tail number)
- **Encryption**: AES-256 at rest, TLS 1.3 in transit
- **Access Control**: Role-based (ML Team, Maintenance, Safety)
- **Audit Trail**: All data access logged

## Usage

### Ingest New Data
```python
from tools.validate_data import validate_against_contract

# Validate raw data
validate_against_contract(
    data_path="raw/engine_vibration/2025-10-11/",
    contract_path="contracts/signals_engine_vibration.yaml"
)
```

### Load Processed Features
```python
import pandas as pd

features = pd.read_parquet("features/engine_vibration/train_features.parquet")
labels = pd.read_parquet("labels/engine_vibration/train_labels.parquet")
```

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
