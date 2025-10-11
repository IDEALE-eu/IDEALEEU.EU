# ⚙️ PROCESSED DATA

**Path**: `DATA/processed/`  
**Purpose**: Windowed and normalized data ready for feature engineering

---

## 🎯 Overview

This directory contains **preprocessed sensor data** that has been:
- Windowed into fixed-size time segments
- Normalized (z-score scaling)
- Annotated with flight phase metadata
- Ready for feature extraction

## 📂 Directory Structure

```
processed/
├── engine_vibration/
│   ├── training/
│   │   ├── windows_20251001_20251031.parquet
│   │   ├── scaler_params.pkl
│   │   └── metadata.json
│   ├── validation/
│   │   └── windows_20251101_20251115.parquet
│   └── test/
│       └── windows_20251116_20251130.parquet
├── landing_gear/
│   └── (future data)
└── README.md (this file)
```

## 🪟 Windowing Strategy

### What is Windowing?

Convert continuous time-series data into fixed-size segments for model input.

**Example**:
```
Continuous Signal (1 hour):
[0.0s → 3600.0s] = 36,000 samples @ 10 Hz

Windowed (10s windows, 5s overlap):
Window 1: [0.0s → 10.0s]   = 100 samples
Window 2: [5.0s → 15.0s]   = 100 samples
Window 3: [10.0s → 20.0s]  = 100 samples
...
Total: 719 windows
```

### Configuration

From data contract `signals_engine_vibration.yaml`:

```yaml
windowing:
  window_size_seconds: 10
  overlap_seconds: 5
  min_samples_required: 95  # At least 95% complete
  alignment: center  # or 'left', 'right'
```

**Why Overlap?**
- Captures transient events at window boundaries
- Increases training data volume
- Smooths predictions at inference time

## 📊 Data Format

**Output Format**: Apache Parquet (one row per window)

**Schema**:
```python
{
    "window_id": str,                    # Unique window identifier
    "aircraft_id": str,                  # Aircraft identifier
    "flight_id": str,                    # Flight identifier
    "timestamp_start": datetime64[ns],   # Window start time
    "timestamp_end": datetime64[ns],     # Window end time
    "flight_phase": uint8,               # Flight phase code
    
    # Raw signal arrays (100 samples each @ 10 Hz for 10s window)
    "vib_fan_rms": array[float32],
    "vib_compressor_rms": array[float32],
    "vib_turbine_rms": array[float32],
    "n1": array[float32],
    "n2": array[float32],
    "egt": array[float32],
    "oil_pressure": array[float32],
    "oil_temperature": array[float32],
    
    # Quality indicators
    "completeness_pct": float32,         # % of valid samples in window
    "has_outliers": bool,                # Any outliers in window?
    "quality_score": float32             # Overall quality (0-100)
}
```

## 🔄 Processing Pipeline

```
DATA/interim/ → Windowing → Normalization → Annotation → DATA/processed/
                    ↓            ↓              ↓
               10s segments  z-score       Flight phase
```

### Step-by-Step

1. **Load Cleaned Data**: Read from `../interim/`
2. **Apply Windowing**: Create 10s overlapping windows
3. **Quality Filter**: Remove windows with <95% completeness
4. **Flight Phase Annotation**: Label each window with flight phase
5. **Normalization**: Apply z-score scaling using training set statistics
6. **Train/Val/Test Split**: Stratified by flight phase
7. **Save**: Write to Parquet with metadata

## 📐 Normalization

### Z-Score Scaling

```python
normalized_value = (value - mean) / std_dev
```

**Why Normalize?**
- Neural networks train faster with normalized inputs
- Prevents features with large magnitudes from dominating
- Ensures consistent scale across different sensors

### Scaler Parameters

Computed from **training set only** and saved for inference:

**Example**: `scaler_params.pkl`
```python
{
    "vib_fan_rms": {"mean": 2.35, "std": 0.82},
    "vib_compressor_rms": {"mean": 1.89, "std": 0.65},
    "vib_turbine_rms": {"mean": 1.45, "std": 0.52},
    "vib_imbalance_score": {"mean": 0.08, "std": 0.03},
    "n1": {"mean": 68.5, "std": 18.2},
    "n2": {"mean": 72.3, "std": 16.8},
    "egt": {"mean": 485.0, "std": 125.0},
    "oil_pressure": {"mean": 45.0, "std": 12.0},
    "oil_temperature": {"mean": 85.0, "std": 20.0}
}
```

**Important**: Same scaler used for training, validation, test, and inference!

## 🏷️ Flight Phase Annotation

Each window is labeled with its primary flight phase:

| Code | Phase | Description |
|------|-------|-------------|
| 0 | Ground | Aircraft on ground, engines off/idle |
| 1 | Taxi | Aircraft taxiing |
| 2 | Takeoff | Takeoff roll and initial climb |
| 3 | Climb | Climbing to cruise altitude |
| 4 | Cruise | Steady-state cruise |
| 5 | Descent | Descending from cruise |
| 6 | Approach | Final approach |
| 7 | Landing | Landing and rollout |

**Assignment Logic**:
- Use most common phase in window
- If tie, use higher-severity phase (takeoff > cruise)
- Transitions (e.g., climb → cruise) get labeled as transition phase

## 📊 Data Split Strategy

**Stratified Split** by flight phase to ensure balanced representation:

| Split | % of Data | Purpose |
|-------|-----------|---------|
| **Training** | 75% | Model training |
| **Validation** | 16.7% | Hyperparameter tuning, early stopping |
| **Test** | 8.3% | Final evaluation, never seen during training |

**Stratification**: Each split has same proportion of flight phases as full dataset.

**Temporal Consideration**: Test set from most recent flights to test generalization.

## 🚀 Quick Start

### Generate Processed Data

```python
from pipelines.training import preprocess

# Process cleaned data
preprocess.create_windows(
    interim_path="../interim/engine_vibration/2025-10/",
    processed_path="engine_vibration/",
    window_size=10,
    overlap=5,
    split_ratio=[0.75, 0.167, 0.083],
    random_seed=42
)
```

### Load Processed Data

```python
import pandas as pd
import pickle

# Load training windows
df_train = pd.read_parquet("engine_vibration/training/windows_20251001_20251031.parquet")

# Load scaler parameters
with open("engine_vibration/training/scaler_params.pkl", "rb") as f:
    scaler_params = pickle.load(f)

print(f"Training set: {len(df_train)} windows")
print(f"Signals normalized with: {scaler_params.keys()}")
```

### Inspect Window

```python
# Get one window
window = df_train.iloc[0]

print(f"Window ID: {window['window_id']}")
print(f"Flight Phase: {window['flight_phase']}")
print(f"Completeness: {window['completeness_pct']:.1f}%")
print(f"Vib Fan RMS shape: {window['vib_fan_rms'].shape}")
```

## 📊 Metadata File

Each dataset has a metadata file describing the processed data:

**Example**: `metadata.json`

```json
{
  "dataset_name": "engine_vibration_training",
  "created_at": "2025-10-11T14:30:00Z",
  "source_flights": 500,
  "date_range": ["2025-10-01", "2025-10-31"],
  "total_windows": 450000,
  
  "windowing": {
    "window_size_seconds": 10,
    "overlap_seconds": 5,
    "sample_rate_hz": 10,
    "samples_per_window": 100
  },
  
  "flight_phase_distribution": {
    "ground": 22500,
    "taxi": 13500,
    "takeoff": 31500,
    "climb": 67500,
    "cruise": 225000,
    "descent": 54000,
    "approach_landing": 36000
  },
  
  "quality_statistics": {
    "mean_completeness": 99.2,
    "windows_with_outliers": 4500,
    "mean_quality_score": 98.5
  },
  
  "normalization": {
    "method": "zscore",
    "scaler_file": "scaler_params.pkl",
    "computed_from": "training_set"
  },
  
  "split_info": {
    "split_ratio": [0.75, 0.167, 0.083],
    "stratified_by": "flight_phase",
    "random_seed": 42
  }
}
```

## 🔍 Quality Checks

Before using processed data:

### 1. Completeness Check

```python
# Ensure high completeness
mean_completeness = df_train["completeness_pct"].mean()
assert mean_completeness >= 95.0, f"Low completeness: {mean_completeness:.1f}%"
```

### 2. Phase Distribution Check

```python
# Verify balanced phases
phase_counts = df_train["flight_phase"].value_counts()
print(phase_counts)
# Cruise should dominate (~50%), but all phases present
```

### 3. Normalization Check

```python
# Check that data is normalized (mean ≈ 0, std ≈ 1)
for signal in ["vib_fan_rms", "n1", "egt"]:
    values = np.concatenate(df_train[signal].values)
    print(f"{signal}: mean={values.mean():.2f}, std={values.std():.2f}")
```

## 🆘 Troubleshooting

### Issue: Insufficient Windows

**Causes**:
- Too few flights in date range
- High rejection due to quality filters
- Incorrect windowing parameters

**Action**:
1. Expand date range
2. Relax quality thresholds (carefully!)
3. Check window size (too large?)

### Issue: Imbalanced Phases

**Causes**:
- Dataset from limited flight profiles
- Missing flight phases (e.g., no takeoffs in data)

**Action**:
1. Collect more diverse flight data
2. Use class weights in training
3. Oversample minority phases

### Issue: Normalization Issues

**Causes**:
- Scaler computed from wrong dataset
- Data leakage (test data in scaler computation)

**Action**:
1. Recompute scaler from training set only
2. Verify pipeline: train scaler → save → apply to val/test

## 📚 Related Documentation

- **Interim Data**: `../interim/README.md`
- **Feature Engineering**: `../features/README.md`
- **Windowing Tool**: `../../../PIPELINES/training/preprocess.py`
- **Data Contracts**: `../contracts/README.md`

## 🔗 Integration Points

- **Input**: `../interim/` (cleaned sensor data)
- **Output**: `../features/` (engineered features)
- **Training Pipeline**: `../../PIPELINES/training/featurize.py`
- **Inference Pipeline**: Same windowing applied at inference time

## ✅ Processing Checklist

Before moving to feature engineering:

- [ ] Windowing parameters validated
- [ ] Scaler computed from training set only
- [ ] Train/val/test split stratified
- [ ] Mean completeness ≥95%
- [ ] All flight phases represented
- [ ] Metadata file generated
- [ ] Quality checks passed
- [ ] Ready for feature extraction

---

**Owner**: Data Science Team  
**Contact**: datascience@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
