# 🛠️ TOOLS

**Path**: `TOOLS/`  
**Purpose**: Utility scripts for data validation, model checking, and benchmarking

---

## 🎯 Overview

This directory contains **utility scripts** for common tasks like data validation, model signature verification, and inference benchmarking. These tools support development, testing, and deployment workflows.

## 📂 Contents

```
TOOLS/
├── validate_data.py          # Data contract validation
├── check_signature.py        # Model signature verification
├── bench_inference.py        # Inference performance benchmarking
├── generate_model_card.py    # Auto-generate model card skeleton
├── visualize_features.py     # Feature distribution visualization
├── compare_models.py         # Compare two model versions
└── README.md (this file)
```

## 🔧 Tool Descriptions

### `validate_data.py`

**Purpose**: Validate data against contract

**Usage**:
```bash
python validate_data.py \
    --data ../../DATA/raw/engine_vibration/2025-10-11/ \
    --contract ../../DATA/contracts/signals_engine_vibration.yaml \
    --report validation_report.json
```

**What it checks**:
- Schema compliance (column names, types)
- Range validation (values within specified ranges)
- Sample rate consistency
- Missing value percentage
- Outlier detection

**Output**: `validation_report.json`
```json
{
  "status": "PASSED",
  "files_checked": 150,
  "violations": [
    {
      "file": "AC001_20251011_120530.parquet",
      "signal": "vib_fan_rms",
      "issue": "3 values outside range [0, 10]",
      "severity": "warning"
    }
  ],
  "summary": {
    "total_samples": 3600000,
    "compliant_pct": 99.95
  }
}
```

---

### `check_signature.py`

**Purpose**: Verify model signature matches specification

**Usage**:
```bash
python check_signature.py \
    --model ../../MODELS/engine_vibration_detector/1.0.0/model.onnx \
    --signature ../../MODELS/engine_vibration_detector/1.0.0/signature.json
```

**What it checks**:
- Input tensor names and shapes
- Output tensor names and shapes
- Data types (float32, int32, etc.)
- Batch dimension handling
- Signature JSON completeness

**Output**:
```
✓ Input signature matches
  - input_features: float32[batch, 9]
✓ Output signature matches
  - reconstruction: float32[batch, 9]
  - anomaly_score: float32[batch, 1]
✓ Model signature valid
```

---

### `bench_inference.py`

**Purpose**: Benchmark model inference performance

**Usage**:
```bash
python bench_inference.py \
    --model ../../MODELS/engine_vibration_detector/1.0.0/ \
    --samples 1000 \
    --warmup 100 \
    --report benchmark_report.json
```

**What it measures**:
- Latency (p50, p95, p99, max)
- Throughput (inferences/second)
- Memory usage
- CPU utilization

**Output**: `benchmark_report.json`
```json
{
  "model": "engine_vibration_detector/1.0.0",
  "samples": 1000,
  "latency_ms": {
    "mean": 12.3,
    "p50": 11.8,
    "p95": 14.2,
    "p99": 18.5,
    "max": 25.1
  },
  "throughput": {
    "inferences_per_second": 81.3
  },
  "resources": {
    "memory_mb": 10.2,
    "cpu_percent": 3.5
  },
  "passes_requirements": true
}
```

---

### `generate_model_card.py`

**Purpose**: Auto-generate model card skeleton

**Usage**:
```bash
python generate_model_card.py \
    --model-id ANOMALY_DETECTOR_ENGINE_VIB_V1.0.0 \
    --ata ATA-72 \
    --output ../../MODELS/engine_vibration_detector/1.0.0/card.md
```

**What it generates**:
- Model card template (based on `../../13-TEMPLATES/MODEL_CARD_TEMPLATE.md`)
- Pre-filled sections (model ID, version, date)
- Placeholders for metrics, limitations, etc.

---

### `visualize_features.py`

**Purpose**: Visualize feature distributions

**Usage**:
```bash
python visualize_features.py \
    --features ../../DATA/features/engine_vibration/training/features_v1.0.parquet \
    --output feature_distributions.png
```

**What it generates**:
- Histograms of feature distributions
- Correlation matrix heatmap
- Box plots for outlier detection
- Time-series plots (if timestamp available)

---

### `compare_models.py`

**Purpose**: Compare two model versions

**Usage**:
```bash
python compare_models.py \
    --model1 ../../MODELS/engine_vibration_detector/1.0.0/ \
    --model2 ../../MODELS/engine_vibration_detector/1.1.0/ \
    --test-data ../../DATA/features/test/ \
    --output comparison_report.json
```

**What it compares**:
- Performance metrics (AUC, precision, recall)
- Inference latency
- Model size (parameters, file size)
- False alarm rate
- Confusion matrix differences

**Output**: `comparison_report.json`
```json
{
  "model1": "1.0.0",
  "model2": "1.1.0",
  "metrics_comparison": {
    "auc": {"v1.0.0": 0.92, "v1.1.0": 0.94, "improvement": "+2.2%"},
    "precision": {"v1.0.0": 0.892, "v1.1.0": 0.905, "improvement": "+1.3%"},
    "recall": {"v1.0.0": 0.875, "v1.1.0": 0.890, "improvement": "+1.5%"}
  },
  "latency_comparison": {
    "v1.0.0": "12.3ms",
    "v1.1.0": "13.1ms",
    "regression": "+0.8ms"
  },
  "recommendation": "Deploy v1.1.0 (better metrics, acceptable latency increase)"
}
```

---

## 🚀 Common Workflows

### Pre-Training Data Validation

```bash
# Validate all training data
python validate_data.py \
    --data ../../DATA/raw/engine_vibration/2025-10/ \
    --contract ../../DATA/contracts/signals_engine_vibration.yaml
```

### Pre-Deployment Model Checks

```bash
# 1. Verify signature
python check_signature.py \
    --model ../../MODELS/.../model.onnx \
    --signature ../../MODELS/.../signature.json

# 2. Benchmark performance
python bench_inference.py \
    --model ../../MODELS/.../
    
# 3. Generate model card
python generate_model_card.py \
    --model-id ... \
    --output ../../MODELS/.../card.md
```

### Model Version Comparison

```bash
# Compare before promoting new version
python compare_models.py \
    --model1 ../../MODELS/.../1.0.0/ \
    --model2 ../../MODELS/.../1.1.0/ \
    --test-data ../../DATA/features/test/
```

---

## 📊 Tool Requirements

**Dependencies**:
```bash
pip install pandas numpy onnxruntime matplotlib seaborn pyyaml
```

**Minimum Python Version**: 3.8+

---

## 📚 Related Documentation

- **Data Contracts**: `../DATA/contracts/README.md`
- **Model Registry**: `../REGISTRY/README.md`
- **Model Card Template**: `../13-TEMPLATES/MODEL_CARD_TEMPLATE.md`

---

**Owner**: MLOps Team  
**Contact**: mlops@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
