# 📊 OFFLINE EVALUATION

**Path**: `EVALUATION/offline/`  
**Purpose**: Offline model evaluation using cross-validation and ablation studies

---

## 🎯 Overview

This directory contains **offline evaluation results** for model validation before deployment. Includes cross-validation reports, ablation studies, and performance analysis.

## 📂 Directory Structure

```
offline/
├── cross_validation/
│   ├── kfold_5_results.json
│   ├── fold_1_metrics.json
│   ├── fold_2_metrics.json
│   └── ...
├── ablation_studies/
│   ├── feature_importance_ablation.json
│   ├── architecture_ablation.json
│   └── hyperparameter_sensitivity.json
├── performance_analysis/
│   ├── confusion_matrices/
│   ├── roc_curves/
│   ├── pr_curves/
│   └── calibration_plots/
└── README.md (this file)
```

## 📝 Evaluation Types

### 1. Cross-Validation

**Purpose**: Assess model stability and generalization

**Method**: 5-fold stratified cross-validation

**What's Evaluated**:
- AUC consistency across folds
- Precision/recall stability
- Variance in performance

**Example**: `kfold_5_results.json`
```json
{
  "method": "stratified_kfold",
  "n_splits": 5,
  "folds": [
    {"fold": 1, "auc": 0.925, "precision": 0.898, "recall": 0.882},
    {"fold": 2, "auc": 0.912, "precision": 0.885, "recall": 0.870},
    {"fold": 3, "auc": 0.920, "precision": 0.895, "recall": 0.878},
    {"fold": 4, "auc": 0.915, "precision": 0.888, "recall": 0.873},
    {"fold": 5, "auc": 0.918, "precision": 0.892, "recall": 0.875}
  ],
  "mean_metrics": {
    "auc": 0.918,
    "precision": 0.892,
    "recall": 0.876
  },
  "std_metrics": {
    "auc": 0.012,
    "precision": 0.011,
    "recall": 0.009
  },
  "cv_score": 0.918,
  "passes_threshold": true
}
```

**Interpretation**:
- Low std (< 0.02) → Stable model ✅
- High std (> 0.05) → Unstable, investigate ⚠️

---

### 2. Ablation Studies

**Purpose**: Understand feature/component importance

#### Feature Ablation

**Method**: Remove one feature at a time, measure performance drop

**Example**: `feature_importance_ablation.json`
```json
{
  "baseline_auc": 0.92,
  "ablation_results": [
    {"feature": "vib_fan_rms", "auc_without": 0.78, "importance": 0.35},
    {"feature": "vib_compressor_rms", "auc_without": 0.82, "importance": 0.28},
    {"feature": "vib_imbalance_score", "auc_without": 0.85, "importance": 0.18},
    {"feature": "vib_turbine_rms", "auc_without": 0.88, "importance": 0.12},
    {"feature": "n1_rate_of_change", "auc_without": 0.90, "importance": 0.07}
  ],
  "top_3_features": ["vib_fan_rms", "vib_compressor_rms", "vib_imbalance_score"]
}
```

**Insight**: `vib_fan_rms` is most important (35% contribution)

#### Architecture Ablation

**Method**: Test different architectures

**Example**: `architecture_ablation.json`
```json
{
  "architectures_tested": [
    {"name": "9-16-8-4", "auc": 0.92, "latency_ms": 12.3},
    {"name": "9-32-16-8", "auc": 0.94, "latency_ms": 18.5},
    {"name": "9-8-4", "auc": 0.88, "latency_ms": 8.2}
  ],
  "selected": "9-16-8-4",
  "reason": "Best balance of performance and latency"
}
```

---

### 3. Performance Analysis

**Visualizations**:

#### Confusion Matrix
```
                Predicted
            Normal    Anomaly
Actual Normal  47,250      250
       Anomaly    188    1,312
```

#### ROC Curve
- AUC = 0.92
- TPR @ FPR=0.05: 0.875

#### Precision-Recall Curve
- AUC-PR = 0.88
- Precision @ Recall=0.90: 0.83

#### Calibration Plot
- Measures if predicted probabilities match actual probabilities
- Well-calibrated model: Points lie on diagonal

---

## 🚀 Running Evaluation

### Cross-Validation

```bash
python ../../PIPELINES/training/evaluate.py \
    --mode cross_validation \
    --config ../../PIPELINES/training/configs/engine_vibration_config.yaml \
    --output cross_validation/kfold_5_results.json
```

### Feature Ablation

```bash
python ../../PIPELINES/training/evaluate.py \
    --mode feature_ablation \
    --config ../../PIPELINES/training/configs/engine_vibration_config.yaml \
    --output ablation_studies/feature_importance_ablation.json
```

### Generate Performance Plots

```bash
python ../../TOOLS/generate_plots.py \
    --metrics ../../MODELS/.../metrics.json \
    --output performance_analysis/
```

---

## 📊 Evaluation Checklist

Before deploying model:

- [ ] Cross-validation AUC ≥ 0.90
- [ ] Cross-validation std ≤ 0.02
- [ ] Ablation study confirms feature importance
- [ ] ROC curve generated
- [ ] PR curve generated
- [ ] Confusion matrix reviewed
- [ ] Calibration validated
- [ ] All plots saved to `performance_analysis/`

---

## 📚 Related Documentation

- **Digital Twin Replay**: `../replay_dt/README.md`
- **Model Metrics**: `../../MODELS/README.md`
- **Training Pipeline**: `../../PIPELINES/training/README.md`

---

**Owner**: Data Science Team  
**Contact**: datascience@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
