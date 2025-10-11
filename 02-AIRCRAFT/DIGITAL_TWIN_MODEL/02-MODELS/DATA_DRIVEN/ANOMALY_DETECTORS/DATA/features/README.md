# 🎨 FEATURE DATA

**Path**: `DATA/features/`  
**Purpose**: Engineered features ready for model training and inference

---

## 🎯 Overview

This directory contains **feature-engineered data** extracted from processed windows. Features capture time-domain, frequency-domain, and temporal patterns relevant for anomaly detection.

## 📂 Directory Structure

```
features/
├── engine_vibration/
│   ├── training/
│   │   ├── features_v1.0.parquet
│   │   ├── feature_names.json
│   │   └── feature_statistics.json
│   ├── validation/
│   │   └── features_v1.0.parquet
│   └── test/
│       └── features_v1.0.parquet
├── landing_gear/
│   └── (future data)
└── README.md (this file)
```

## 🧪 Feature Engineering

### Feature Categories

#### 1. **Time-Domain Features**

Statistical aggregations over window:

| Feature | Description | Formula |
|---------|-------------|---------|
| `vib_fan_rms` | RMS vibration (fan) | √(Σx²/n) |
| `vib_fan_peak` | Peak vibration (fan) | max(|x|) |
| `vib_fan_mean` | Mean vibration (fan) | Σx/n |
| `vib_fan_std` | Std deviation (fan) | √(Σ(x-μ)²/n) |
| `vib_compressor_rms` | RMS vibration (compressor) | √(Σx²/n) |
| `vib_turbine_rms` | RMS vibration (turbine) | √(Σx²/n) |

**Why RMS?**
- RMS captures overall vibration energy
- More stable than peak for continuous monitoring
- Industry standard for rotating machinery

#### 2. **Frequency-Domain Features**

FFT-based features for identifying specific fault patterns:

| Feature | Description | Use Case |
|---------|-------------|----------|
| `vib_imbalance_score` | FFT 1P/broadband ratio | Blade imbalance detection |
| `vib_1p_amplitude` | 1P frequency amplitude | Imbalance magnitude |
| `vib_2p_amplitude` | 2P frequency amplitude | Looseness/misalignment |
| `vib_high_freq_energy` | Energy in high freq bands | Bearing wear |

**1P Component**: Vibration at rotational frequency (1x RPM)
- High 1P → Imbalance, bent shaft
- High 2P → Looseness, misalignment
- High freq → Bearing damage

#### 3. **Temporal Features**

Rate of change and trends:

| Feature | Description | Formula |
|---------|-------------|---------|
| `n1_rate_of_change` | N1 acceleration | Δn1/Δt |
| `egt_gradient` | EGT rate of change | ΔEGT/Δt |
| `vib_trend` | Vibration trend | Linear regression slope |

**Why Temporal Features?**
- Capture transient events (e.g., rapid acceleration)
- Detect gradual degradation trends
- Distinguish steady-state from transients

#### 4. **Operational Context Features**

System state variables:

| Feature | Description | Range |
|---------|-------------|-------|
| `n1` | Engine fan speed | 0-110% |
| `n2` | Engine core speed | 0-110% |
| `egt` | Exhaust gas temperature | 0-1200°C |
| `oil_pressure` | Engine oil pressure | 0-150 psi |
| `oil_temperature` | Engine oil temperature | -40-150°C |
| `flight_phase` | Flight phase code | 0-7 |

**Why Context?**
- Normal vibration varies by engine speed
- Model needs context to distinguish normal from anomaly

## 📊 Feature Schema

**Output Format**: Apache Parquet (one row per window)

```python
{
    "window_id": str,
    "aircraft_id": str,
    "flight_id": str,
    "timestamp": datetime64[ns],
    
    # Time-domain features
    "vib_fan_rms": float32,
    "vib_fan_peak": float32,
    "vib_compressor_rms": float32,
    "vib_turbine_rms": float32,
    
    # Frequency-domain features
    "vib_imbalance_score": float32,
    "vib_1p_amplitude": float32,
    "vib_2p_amplitude": float32,
    "vib_high_freq_energy": float32,
    
    # Temporal features
    "n1_rate_of_change": float32,
    "egt_gradient": float32,
    "vib_trend": float32,
    
    # Operational context
    "n1": float32,
    "n2": float32,
    "egt": float32,
    "oil_pressure": float32,
    "oil_temperature": float32,
    "flight_phase": uint8,
    
    # Metadata
    "quality_score": float32
}
```

**Total Features**: 18 (9 core anomaly detection inputs + 9 context)

## 🔄 Feature Engineering Pipeline

```
DATA/processed/ → Time-Domain → Frequency-Domain → Temporal → DATA/features/
                      ↓              ↓                 ↓
                    RMS, Peak      FFT, 1P          Gradients
```

### Implementation

```python
from pipelines.training import featurize

# Extract features from processed windows
featurize.extract_features(
    processed_path="../processed/engine_vibration/training/",
    features_path="engine_vibration/training/features_v1.0.parquet",
    feature_config="../../../PIPELINES/training/configs/engine_vibration_config.yaml"
)
```

## 🎯 Feature Selection Rationale

### Why These 9 Core Features?

Based on **domain expertise** (engine health monitoring):

1. **vib_fan_rms**: Primary indicator of fan bearing health
2. **vib_fan_peak**: Detects transient spikes (FOD events)
3. **vib_compressor_rms**: Compressor bearing health
4. **vib_turbine_rms**: Turbine bearing health
5. **vib_imbalance_score**: Blade imbalance detector
6. **n1**: Contextualizes vibration (varies with RPM)
7. **n2**: Core speed context
8. **egt**: Thermal context (affects bearing expansion)
9. **n1_rate_of_change**: Transient detection

**Feature Importance** (from trained model):
1. vib_fan_rms: 35%
2. vib_compressor_rms: 28%
3. vib_imbalance_score: 18%
4. vib_turbine_rms: 12%
5. n1_rate_of_change: 7%

## 📈 Feature Statistics

**Example**: `feature_statistics.json`

```json
{
  "dataset": "engine_vibration_training",
  "feature_count": 18,
  "sample_count": 450000,
  
  "feature_stats": {
    "vib_fan_rms": {
      "mean": 0.0,
      "std": 1.0,
      "min": -3.8,
      "max": 4.2,
      "missing_pct": 0.0
    },
    "vib_imbalance_score": {
      "mean": 0.0,
      "std": 1.0,
      "min": -2.5,
      "max": 5.1,
      "missing_pct": 0.0
    }
  },
  
  "correlation_matrix_path": "correlation_matrix.png"
}
```

## 🔍 Feature Quality Checks

### 1. Range Check

```python
import pandas as pd

df = pd.read_parquet("engine_vibration/training/features_v1.0.parquet")

# After normalization, features should be roughly in [-5, 5]
for col in df.select_dtypes(include='float32').columns:
    assert df[col].min() > -6, f"{col} has extreme min: {df[col].min()}"
    assert df[col].max() < 6, f"{col} has extreme max: {df[col].max()}"
```

### 2. Missing Values Check

```python
# No missing values allowed
assert df.isnull().sum().sum() == 0, "Missing values detected!"
```

### 3. Constant Features Check

```python
# Features should vary (std > 0.01)
for col in df.select_dtypes(include='float32').columns:
    assert df[col].std() > 0.01, f"{col} is near-constant!"
```

## 🚀 Quick Start

### Extract Features

```python
from pipelines.training import featurize

# Process one flight
featurize.extract_features_from_windows(
    windows_df=df_windows,
    feature_config="config.yaml"
)
```

### Load Features for Training

```python
import pandas as pd

# Load training features
X_train = pd.read_parquet("engine_vibration/training/features_v1.0.parquet")
y_train = pd.read_parquet("../labels/engine_vibration/training/labels_v1.0.parquet")

# Drop metadata columns
feature_cols = [col for col in X_train.columns if col not in 
                ["window_id", "aircraft_id", "flight_id", "timestamp", "quality_score"]]
X_train_features = X_train[feature_cols]

print(f"Training set: {len(X_train_features)} samples, {len(feature_cols)} features")
```

### Visualize Feature Distributions

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Plot feature distributions
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
for i, col in enumerate(feature_cols[:9]):
    ax = axes[i//3, i%3]
    df[col].hist(bins=50, ax=ax)
    ax.set_title(col)
plt.tight_layout()
plt.savefig("feature_distributions.png")
```

## 🔬 Feature Engineering Best Practices

### 1. Domain Knowledge First

- Don't blindly create 100+ features
- Start with physics-based features (RMS, FFT)
- Consult domain experts (engine systems engineers)

### 2. Feature Interpretability

- Each feature should have clear meaning
- Avoid black-box transformations (PCA)
- Maintain traceability to raw signals

### 3. Computational Efficiency

- Avoid expensive computations (deep FFT)
- Optimize for real-time inference (<50ms)
- Cache intermediate results

### 4. Robustness

- Features should degrade gracefully with noise
- Handle edge cases (zero-division, NaN)
- Test on unseen aircraft/conditions

## 📚 Related Documentation

- **Processed Data**: `../processed/README.md`
- **Labels**: `../labels/README.md`
- **Feature Config**: `../../PIPELINES/training/configs/engine_vibration_config.yaml`
- **Training Pipeline**: `../../PIPELINES/training/featurize.py`

## 🔗 Integration Points

- **Input**: `../processed/` (windowed, normalized data)
- **Output**: Model training (`../../PIPELINES/training/train.py`)
- **Inference**: Same features extracted at inference time
- **Monitoring**: Feature drift tracked in `../../DRIFT_MONITORING/`

## ✅ Feature Engineering Checklist

Before training:

- [ ] Features extracted from training, validation, test sets
- [ ] Feature names documented
- [ ] Statistics computed and saved
- [ ] No missing values
- [ ] No constant features
- [ ] Feature distributions reasonable
- [ ] Correlation matrix reviewed (no perfect correlations)
- [ ] Ready for model training

---

**Owner**: Data Science Team  
**Contact**: datascience@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
