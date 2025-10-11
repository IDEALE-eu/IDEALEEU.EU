# MODELS Directory

**Purpose**: Versioned storage of trained anomaly detection models and artifacts.

## Directory Structure

```
MODELS/
└─ <detector_name>/
   └─ <version>/           # Semantic versioning (MAJOR.MINOR.PATCH)
      ├─ model.onnx        # ONNX model file
      ├─ scaler.pkl        # Preprocessing scaler (scikit-learn)
      ├─ signature.json    # Input/output signature
      ├─ thresholds.yaml   # Anomaly detection thresholds
      ├─ metrics.json      # Performance metrics
      ├─ card.md           # Model card documentation
      └─ explain/          # Explainability artifacts (SHAP, saliency maps)
```

## Example: Engine Vibration Detector

```
MODELS/engine_vibration_detector/
└─ 1.0.0/
   ├─ model.onnx         # 23 KB
   ├─ scaler.pkl         # 8 KB
   ├─ signature.json     # Input/output schema
   ├─ thresholds.yaml    # Anomaly thresholds by severity
   ├─ metrics.json       # AUC=0.92, Precision=0.892, Recall=0.875
   ├─ card.md            # Comprehensive model documentation
   └─ explain/
      └─ (SHAP values, feature importance plots)
```

## Versioning Policy

**Semantic Versioning**: MAJOR.MINOR.PATCH

- **MAJOR**: Breaking changes (input schema change, algorithm change)
  - Example: 1.0.0 → 2.0.0 (new input features added)
- **MINOR**: Non-breaking improvements (retrained model, performance boost)
  - Example: 1.0.0 → 1.1.0 (retrained with more data)
- **PATCH**: Bug fixes, no model change
  - Example: 1.0.0 → 1.0.1 (fix threshold config bug)

## Required Artifacts

### model.onnx
- Standard ONNX format for cross-platform deployment
- Supported runtimes: ONNX Runtime, TensorRT, CoreML
- Opset version: 14+

### scaler.pkl
- Preprocessing scaler (StandardScaler, MinMaxScaler)
- Python pickle format
- Must be applied before inference

### signature.json
- Input feature names, types, shapes
- Output names and interpretation
- Preprocessing requirements
- Usage examples

### thresholds.yaml
- Anomaly score threshold (default)
- Severity levels (minor, moderate, severe)
- Flight phase-specific thresholds
- Confidence levels

### metrics.json
- Classification metrics (accuracy, precision, recall, AUC)
- Performance breakdown (by flight phase, anomaly type)
- Cross-validation results
- Shadow mode validation results
- Latency and resource metrics

### card.md
- Comprehensive model documentation
- Training data, architecture, performance
- Limitations, assumptions, ethical considerations
- Compliance, certification, contact information

### explain/
- SHAP values (feature importance)
- Saliency maps (input sensitivity)
- Reconstruction error heatmaps
- Example predictions with explanations

## Model Registry Integration

All models must be registered in `../REGISTRY/index.yaml` with:
- Model ID, version, status
- ATA chapter mapping
- Performance metrics
- Deployment info
- Ownership and contacts

## Deployment Checklist

Before deploying a model to production:
- [ ] All required artifacts present
- [ ] Model card completed
- [ ] Metrics meet quality gates
- [ ] Signature validated (`../../TOOLS/check_signature.py`)
- [ ] Inference benchmarked (`../../TOOLS/bench_inference.py`)
- [ ] Registry entry created (status: validation)
- [ ] Shadow mode completed (30 days, min 100 aircraft for Level A)
- [ ] Safety assessment completed (FMEA, FTA)
- [ ] Certification evidence linked
- [ ] CCB approval obtained

## Usage

### Load and Run Inference

```python
import onnxruntime as ort
import pickle
import numpy as np

# Load model and scaler
session = ort.InferenceSession("MODELS/engine_vibration_detector/1.0.0/model.onnx")
with open("MODELS/engine_vibration_detector/1.0.0/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Prepare input
raw_features = np.array([[2.8, 3.5, 2.1, 1.6, 0.09, 75.0, 80.0, 520.0, 0.5]])
scaled_features = scaler.transform(raw_features)

# Inference
outputs = session.run(None, {"input_features": scaled_features})
reconstruction = outputs[0]
anomaly_score = outputs[1]

# Decision
threshold = 3.5
is_anomaly = anomaly_score[0] > threshold
```

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
