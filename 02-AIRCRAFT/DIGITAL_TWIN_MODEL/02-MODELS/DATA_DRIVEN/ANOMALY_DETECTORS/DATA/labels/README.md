# 🏷️ LABELS DATA

**Path**: `DATA/labels/`  
**Purpose**: Ground truth labels for supervised and semi-supervised anomaly detection

---

## 🎯 Overview

This directory contains **ground truth labels** for training, validating, and testing anomaly detection models. Labels identify normal operation vs. anomalies, with severity and fault type classification.

## 📂 Directory Structure

```
labels/
├── engine_vibration/
│   ├── training/
│   │   ├── labels_v1.0.parquet
│   │   └── labeling_metadata.json
│   ├── validation/
│   │   └── labels_v1.0.parquet
│   └── test/
│       └── labels_v1.0.parquet
├── landing_gear/
│   └── (future data)
└── README.md (this file)
```

## 🔖 Label Schema

**Format**: Apache Parquet (one row per window, aligned with features)

```python
{
    "window_id": str,                 # Matches features window_id
    "aircraft_id": str,
    "flight_id": str,
    "timestamp": datetime64[ns],
    
    # Primary label
    "is_anomaly": bool,               # Binary: 0=normal, 1=anomaly
    
    # Severity classification
    "anomaly_severity": uint8,        # 0=normal, 1=minor, 2=moderate, 3=severe
    
    # Fault type classification
    "fault_type": uint8,              # 0=none, 1=bearing_wear, 2=blade_imbalance,
                                      # 3=mounting_looseness, 4=shaft_misalignment, 5=other
    
    # Confidence and provenance
    "label_confidence": float32,      # 0.0-1.0 (expert confidence)
    "label_source": str,              # 'expert', 'maintenance_record', 'automated'
    "labeled_by": str,                # Engineer ID or system name
    "labeled_at": datetime64[ns],     # Labeling timestamp
    
    # Maintenance linkage
    "ncr_id": str,                    # Non-Conformance Report ID (if applicable)
    "maintenance_action": str,        # Action taken (e.g., "bearing replacement")
    "verified": bool                  # Post-maintenance verification
}
```

## 📊 Label Categories

### Binary Classification

| Label | Value | Description |
|-------|-------|-------------|
| Normal | 0 | Healthy operation, no anomaly detected |
| Anomaly | 1 | Anomaly detected, requires investigation |

**Class Balance** (training set):
- Normal: 97% (437,000 windows)
- Anomaly: 3% (13,000 windows)

**Note**: Imbalanced dataset reflects realistic operational conditions.

### Severity Classification

| Severity | Code | Description | Action |
|----------|------|-------------|--------|
| Normal | 0 | No anomaly | Continue monitoring |
| Minor | 1 | Early-stage anomaly | Schedule inspection (next maintenance) |
| Moderate | 2 | Progressive anomaly | Inspect within 48 hours |
| Severe | 3 | Critical anomaly | Ground aircraft, immediate action |

### Fault Type Classification

| Fault Type | Code | Typical Indicators | Root Cause |
|------------|------|-------------------|------------|
| None | 0 | N/A | Normal operation |
| Bearing Wear | 1 | Elevated broadband vibration | Bearing degradation, contamination |
| Blade Imbalance | 2 | High 1P component | Blade damage, ice accumulation |
| Mounting Looseness | 3 | Multiple frequency peaks | Loose bolts, structural issues |
| Shaft Misalignment | 4 | 2P, 3P harmonics | Installation error, thermal warping |
| Other/Unknown | 5 | Atypical patterns | Novel fault, requires investigation |

## 🔍 Labeling Methodology

### 1. Expert Labeling

**Process**:
1. Senior engine engineers review flight data
2. Identify anomalous windows based on:
   - Vibration levels exceeding thresholds
   - Unusual patterns (e.g., sudden spikes)
   - Correlation with other symptoms (oil pressure drop)
3. Classify severity and fault type
4. Assign confidence score (based on clarity of signature)

**Typical Team**: 3 senior engineers, consensus labeling

**Time Investment**: ~2 hours per 1000 windows

### 2. Maintenance Record Labeling

**Process**:
1. Link flight data to post-flight inspection reports
2. If issue found (e.g., bearing replacement), label prior windows as anomalous
3. Retrospective labeling: Work backward from confirmed failure
4. High confidence labels (verified by physical inspection)

**Linkage**: NCR (Non-Conformance Report) IDs

### 3. Automated Labeling (Low Confidence)

**Process**:
1. Use rule-based thresholds (e.g., vibration >5 mils)
2. Flag potential anomalies for expert review
3. Only used as weak labels for semi-supervised learning

**Confidence**: Lower (0.5-0.7), requires validation

## 📈 Labeling Statistics

**Example**: `labeling_metadata.json`

```json
{
  "dataset": "engine_vibration_training",
  "total_windows": 450000,
  "labeled_windows": 450000,
  "labeling_completeness": 100.0,
  
  "class_distribution": {
    "normal": 437000,
    "anomaly": 13000
  },
  
  "severity_distribution": {
    "normal": 437000,
    "minor": 6500,
    "moderate": 4500,
    "severe": 2000
  },
  
  "fault_type_distribution": {
    "none": 437000,
    "bearing_wear": 6500,
    "blade_imbalance": 3200,
    "mounting_looseness": 1800,
    "shaft_misalignment": 1200,
    "other": 300
  },
  
  "label_source_distribution": {
    "expert": 10000,
    "maintenance_record": 2500,
    "automated": 500
  },
  
  "mean_confidence": 0.92,
  "labeling_period": ["2025-09-01", "2025-09-30"],
  "labeling_team": ["engineer_001", "engineer_002", "engineer_003"]
}
```

## 🚀 Quick Start

### Load Labels

```python
import pandas as pd

# Load training labels
y_train = pd.read_parquet("engine_vibration/training/labels_v1.0.parquet")

# Basic statistics
print(f"Total samples: {len(y_train)}")
print(f"Anomaly rate: {y_train['is_anomaly'].mean():.2%}")
print(f"Severity distribution:\n{y_train['anomaly_severity'].value_counts()}")
```

### Join with Features

```python
# Load features
X_train = pd.read_parquet("../features/engine_vibration/training/features_v1.0.parquet")

# Join on window_id
df_train = X_train.merge(y_train, on="window_id")

print(f"Training set: {len(df_train)} samples")
```

### Filter by Confidence

```python
# Use only high-confidence labels
df_high_conf = y_train[y_train["label_confidence"] >= 0.8]
print(f"High-confidence labels: {len(df_high_conf)} / {len(y_train)}")
```

## 🔧 Handling Class Imbalance

### Strategies

1. **Class Weights**: Penalize false negatives more
   ```python
   from sklearn.utils.class_weight import compute_class_weight
   weights = compute_class_weight('balanced', classes=[0, 1], y=y_train['is_anomaly'])
   ```

2. **Oversampling**: SMOTE for minority class
   ```python
   from imblearn.over_sampling import SMOTE
   X_resampled, y_resampled = SMOTE().fit_resample(X_train, y_train)
   ```

3. **Undersampling**: Reduce majority class
   ```python
   from imblearn.under_sampling import RandomUnderSampler
   X_resampled, y_resampled = RandomUnderSampler().fit_resample(X_train, y_train)
   ```

4. **Threshold Tuning**: Optimize decision threshold for desired recall/precision

**Recommended**: Class weights + threshold tuning (maintains all data)

## 🔍 Quality Checks

### 1. Completeness Check

```python
# Every window must have a label
assert len(y_train) == len(X_train), "Label count mismatch!"
assert y_train["window_id"].isin(X_train["window_id"]).all(), "Window ID mismatch!"
```

### 2. Consistency Check

```python
# Anomaly severity should match is_anomaly
assert (y_train[y_train["is_anomaly"] == 0]["anomaly_severity"] == 0).all()
assert (y_train[y_train["is_anomaly"] == 1]["anomaly_severity"] > 0).all()
```

### 3. Confidence Distribution

```python
# Check labeling confidence
print(f"Mean confidence: {y_train['label_confidence'].mean():.2f}")
print(f"Low-conf samples (<0.7): {(y_train['label_confidence'] < 0.7).sum()}")
```

## 📊 Label Quality Metrics

Track labeling quality:

- **Inter-Rater Agreement**: Cohen's kappa between engineers (target: κ >0.8)
- **Maintenance Verification Rate**: % of predicted anomalies confirmed by maintenance
- **False Alarm Rate**: % of alerts that were false alarms
- **Missed Anomaly Rate**: % of maintenance issues not flagged

## 🆘 Troubleshooting

### Issue: Extreme Class Imbalance

**Action**:
- Use class weights in training
- Adjust decision threshold (lower threshold → higher recall)
- Collect more anomaly examples (seeded faults in test cells)

### Issue: Low Confidence Labels

**Action**:
- Re-review low-confidence samples with experts
- Consider discarding confidence <0.5 samples
- Use semi-supervised learning (train on high-conf, test on all)

### Issue: Label Noise

**Action**:
- Cross-validate with multiple engineers
- Compare with maintenance records
- Use label smoothing in training

## 📚 Related Documentation

- **Features**: `../features/README.md`
- **Model Training**: `../../PIPELINES/training/train.py`
- **Data Contracts**: `../contracts/README.md`
- **Labeling Guidelines**: Internal documentation

## 🔗 Integration Points

- **Features**: Labels aligned with feature window_ids
- **Training**: Used in supervised/semi-supervised training
- **Evaluation**: Ground truth for metrics (precision, recall, AUC)
- **Maintenance**: Linked to NCRs for traceability

## ✅ Labeling Checklist

Before training:

- [ ] All windows labeled (100% completeness)
- [ ] Labels aligned with features (same window_ids)
- [ ] Class distribution documented
- [ ] Mean confidence ≥0.8
- [ ] Inter-rater agreement validated (if multiple labelers)
- [ ] Maintenance records linked (NCR IDs)
- [ ] Metadata file generated
- [ ] Ready for model training

---

**Owner**: Data Science Team + Engine Systems Team  
**Contact**: datascience@ideale.eu, enginesystems@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
