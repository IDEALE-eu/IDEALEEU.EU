# PIPELINES Directory

**Purpose**: Training and inference pipelines for anomaly detection models.

## Directory Structure

```
PIPELINES/
├─ training/
│  ├─ configs/             # Training configurations (*.yaml)
│  ├─ preprocess.py        # Data preprocessing
│  ├─ featurize.py         # Feature engineering
│  ├─ train.py             # Model training
│  ├─ evaluate.py          # Model evaluation
│  └─ export.py            # Model export (ONNX, scaler)
└─ inference/
   ├─ realtime/
   │  ├─ adapter_databus.py # Real-time data adapter
   │  └─ configs/          # Real-time configs
   └─ batch/
      └─ run_batch.py      # Batch inference
```

## Training Pipeline

### 1. Configuration (`configs/*.yaml`)

Defines complete training setup:
- Data sources and contracts
- Model architecture and hyperparameters
- Training parameters (epochs, batch size, learning rate)
- Evaluation metrics and quality gates
- Export format and artifacts

**Example**: `configs/engine_vibration_config.yaml`

### 2. Preprocessing (`preprocess.py`)

```bash
python preprocess.py --config configs/engine_vibration_config.yaml
```

Steps:
- Load raw data from `../DATA/raw/`
- Validate against data contract
- Handle missing values
- Remove outliers (3-sigma)
- Time synchronization
- Output to `../DATA/interim/`

### 3. Feature Engineering (`featurize.py`)

```bash
python featurize.py --config configs/engine_vibration_config.yaml
```

Steps:
- Load interim data
- Apply windowing (e.g., 10-second windows)
- Compute time domain features (RMS, peak, mean, std)
- Compute frequency domain features (FFT, spectral density)
- Normalize features (z-score scaling)
- Output to `../DATA/features/` and `../DATA/processed/`

### 4. Training (`train.py`)

```bash
python train.py --config configs/engine_vibration_config.yaml
```

Steps:
- Load features and labels
- Train/validation/test split (stratified)
- Initialize model architecture
- Train with early stopping, checkpointing
- Log metrics to TensorBoard/MLflow
- Save best model checkpoint

### 5. Evaluation (`evaluate.py`)

```bash
python evaluate.py --config configs/engine_vibration_config.yaml
```

Steps:
- Load trained model and test set
- Compute performance metrics (AUC, precision, recall, FAR)
- Cross-validation (5-fold stratified)
- Performance breakdown (by flight phase, anomaly type)
- Quality gate checks
- Generate metrics.json

### 6. Export (`export.py`)

```bash
python export.py --config configs/engine_vibration_config.yaml --version 1.0.0
```

Steps:
- Convert model to ONNX format
- Export scaler (pickle)
- Generate signature.json (input/output schema)
- Calibrate thresholds.yaml
- Save metrics.json
- Create model card template
- Package artifacts to `../MODELS/<detector>/<version>/`

## Inference Pipeline

### Real-Time Inference (`inference/realtime/`)

For streaming sensor data from aircraft:

```python
# adapter_databus.py
from mqtt import MQTTClient
import onnxruntime as ort

client = MQTTClient(broker="databus.ideale.eu")
session = ort.InferenceSession("../../MODELS/engine_vibration_detector/1.0.0/model.onnx")

def on_message(topic, data):
    # Preprocess incoming sensor data
    features = preprocess(data)
    
    # Inference
    anomaly_score = session.run(None, {"input_features": features})[1]
    
    # Alert if anomaly
    if anomaly_score > threshold:
        send_alert(anomaly_score, data)

client.subscribe("aircraft/+/engine/vibration", on_message)
client.loop_forever()
```

**Configuration**: `inference/realtime/configs/realtime_config.yaml`

### Batch Inference (`inference/batch/`)

For historical data analysis or digital twin replay:

```bash
python batch/run_batch.py \
    --model ../../MODELS/engine_vibration_detector/1.0.0/ \
    --data ../../DATA/raw/engine_vibration/2025-10/ \
    --output ../../EVALUATION/replay_dt/results.parquet
```

Steps:
- Load batch data (Parquet, CSV)
- Apply preprocessing and feature engineering
- Batch inference (parallelized)
- Generate anomaly scores and predictions
- Save results for analysis

## Configuration Management

All pipeline configurations are version-controlled:
- Training configs linked to model versions
- Changes require ECR (Engineering Change Request)
- Reproducibility: Same config → same model

## CI/CD Integration

Training pipeline triggered by:
- Manual trigger (development)
- Scheduled retraining (quarterly)
- Drift detection alert (automated)

**CI/CD Pipeline**:
1. Validate data contract
2. Run preprocessing and feature engineering
3. Train model
4. Evaluate and check quality gates
5. Export artifacts
6. Update model registry (status: validation)
7. Deploy to shadow mode

## Quality Gates

Training fails if:
- AUC < 0.90 (configurable)
- Precision < 0.85
- Recall < 0.85
- False Alarm Rate > 0.05
- Inference latency > 50ms

## Reproducibility

Ensured by:
- Fixed random seeds
- Versioned data contracts
- Deterministic operations
- Conda/Docker environments
- Git-tracked configurations

## Usage Examples

### Run Full Training Pipeline
```bash
# Step-by-step
python training/preprocess.py --config training/configs/engine_vibration_config.yaml
python training/featurize.py --config training/configs/engine_vibration_config.yaml
python training/train.py --config training/configs/engine_vibration_config.yaml
python training/evaluate.py --config training/configs/engine_vibration_config.yaml
python training/export.py --config training/configs/engine_vibration_config.yaml --version 1.0.0

# Or use orchestrator (e.g., Airflow, Kubeflow)
python training/run_pipeline.py --config training/configs/engine_vibration_config.yaml
```

### Real-Time Inference
```bash
python inference/realtime/adapter_databus.py --config inference/realtime/configs/realtime_config.yaml
```

### Batch Inference
```bash
python inference/batch/run_batch.py \
    --model ../../MODELS/engine_vibration_detector/1.0.0/ \
    --data ../../DATA/raw/engine_vibration/2025-10/ \
    --output results.parquet
```

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
