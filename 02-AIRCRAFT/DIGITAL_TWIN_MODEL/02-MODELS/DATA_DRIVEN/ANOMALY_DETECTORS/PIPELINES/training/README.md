# 🚂 TRAINING SCRIPTS

**Path**: `PIPELINES/training/`  
**Purpose**: Python scripts for model training pipeline execution

---

## 🎯 Overview

This directory contains **executable Python scripts** that implement each stage of the training pipeline. These scripts are configuration-driven and designed for reproducibility.

## 📂 Contents

```
training/
├── configs/                      # Configuration files (*.yaml)
│   └── engine_vibration_config.yaml
├── preprocess.py                 # Data preprocessing
├── featurize.py                  # Feature engineering
├── train.py                      # Model training
├── evaluate.py                   # Model evaluation
├── export.py                     # Model export (ONNX)
├── run_pipeline.py               # End-to-end orchestrator
└── README.md (this file)
```

## 📝 Script Descriptions

### `preprocess.py`

**Purpose**: Clean raw data and create windows

**Inputs**:
- Raw data from `../../DATA/raw/`
- Data contract from `../../DATA/contracts/`

**Outputs**:
- Cleaned data → `../../DATA/interim/`
- Windowed data → `../../DATA/processed/`

**Usage**:
```bash
python preprocess.py --config configs/engine_vibration_config.yaml
```

**What it does**:
1. Loads raw sensor data
2. Validates against data contract
3. Handles missing values (interpolation)
4. Removes outliers (3-sigma rule)
5. Time synchronizes signals
6. Creates windows (10s, 5s overlap)
7. Saves processed data

---

### `featurize.py`

**Purpose**: Extract features from windowed data

**Inputs**:
- Processed windows from `../../DATA/processed/`

**Outputs**:
- Features → `../../DATA/features/`

**Usage**:
```bash
python featurize.py --config configs/engine_vibration_config.yaml
```

**What it does**:
1. Loads processed windows
2. Computes time-domain features (RMS, peak, mean, std)
3. Computes frequency-domain features (FFT 1P ratio)
4. Computes temporal features (rate of change)
5. Normalizes features (z-score)
6. Saves feature dataset

---

### `train.py`

**Purpose**: Train anomaly detection model

**Inputs**:
- Features from `../../DATA/features/training/`
- Labels from `../../DATA/labels/training/`
- Configuration from `configs/*.yaml`

**Outputs**:
- Trained model checkpoint
- Training logs (TensorBoard, MLflow)
- Model weights

**Usage**:
```bash
python train.py --config configs/engine_vibration_config.yaml
```

**What it does**:
1. Loads training features and labels
2. Initializes model architecture (autoencoder)
3. Sets up optimizer, loss function
4. Trains with early stopping
5. Validates on validation set
6. Saves best model checkpoint
7. Logs metrics to TensorBoard/MLflow

**Parameters**:
- Learning rate: 0.001
- Batch size: 128
- Epochs: 100 (with early stopping)
- Optimizer: Adam
- Loss: MSE (reconstruction error)

---

### `evaluate.py`

**Purpose**: Evaluate trained model

**Inputs**:
- Trained model checkpoint
- Test features from `../../DATA/features/test/`
- Test labels from `../../DATA/labels/test/`

**Outputs**:
- Metrics JSON → `../../MODELS/<detector>/<version>/metrics.json`
- Confusion matrix, ROC curve plots
- Performance breakdown by flight phase, fault type

**Usage**:
```bash
python evaluate.py --config configs/engine_vibration_config.yaml --checkpoint <path>
```

**What it does**:
1. Loads trained model
2. Runs inference on test set
3. Computes metrics (AUC, precision, recall, FAR)
4. Performs cross-validation (5-fold)
5. Generates performance breakdown
6. Saves metrics and plots

---

### `export.py`

**Purpose**: Export model to production format

**Inputs**:
- Trained model checkpoint
- Scaler parameters

**Outputs**:
- ONNX model → `../../MODELS/<detector>/<version>/model.onnx`
- Scaler → `../../MODELS/<detector>/<version>/scaler.pkl`
- Signature → `../../MODELS/<detector>/<version>/signature.json`
- Thresholds → `../../MODELS/<detector>/<version>/thresholds.yaml`

**Usage**:
```bash
python export.py \
    --config configs/engine_vibration_config.yaml \
    --checkpoint <path> \
    --version 1.0.0
```

**What it does**:
1. Loads trained TensorFlow/PyTorch model
2. Converts to ONNX format
3. Validates ONNX model (numerical consistency)
4. Exports scaler parameters
5. Generates signature JSON
6. Calibrates detection thresholds
7. Packages artifacts to MODELS/

---

### `run_pipeline.py`

**Purpose**: End-to-end pipeline orchestrator

**Usage**:
```bash
python run_pipeline.py --config configs/engine_vibration_config.yaml --version 1.0.0
```

**What it does**:
1. Runs preprocessing (`preprocess.py`)
2. Runs feature engineering (`featurize.py`)
3. Runs training (`train.py`)
4. Runs evaluation (`evaluate.py`)
5. Runs export (`export.py`)
6. Validates quality gates
7. Updates model registry

**Quality Gates**:
- AUC ≥ 0.90
- Precision ≥ 0.85
- Recall ≥ 0.85
- FAR ≤ 0.05
- Inference latency ≤ 50ms

If any gate fails → Pipeline stops, no export

---

## 🔧 Configuration Management

All scripts are driven by YAML configuration files in `configs/`:

**Example**: `configs/engine_vibration_config.yaml`

Key sections:
- `data`: Data paths, contracts, split ratios
- `model`: Architecture, hyperparameters
- `training`: Optimizer, epochs, batch size
- `evaluation`: Metrics, thresholds
- `export`: ONNX settings, artifact paths

**Advantage**: Change hyperparameters without modifying code

---

## 🚀 Quick Start Guide

### Run Full Pipeline

```bash
# End-to-end training
python run_pipeline.py \
    --config configs/engine_vibration_config.yaml \
    --version 1.1.0
```

### Run Individual Stages

```bash
# 1. Preprocessing only
python preprocess.py --config configs/engine_vibration_config.yaml

# 2. Feature engineering only
python featurize.py --config configs/engine_vibration_config.yaml

# 3. Training only
python train.py --config configs/engine_vibration_config.yaml

# 4. Evaluation only
python evaluate.py --config configs/engine_vibration_config.yaml --checkpoint models/best_model.pth

# 5. Export only
python export.py --config configs/engine_vibration_config.yaml --checkpoint models/best_model.pth --version 1.0.0
```

### Resume Training

```bash
python train.py \
    --config configs/engine_vibration_config.yaml \
    --checkpoint models/checkpoint_epoch_50.pth \
    --resume
```

---

## 📊 Monitoring Training

### TensorBoard

```bash
tensorboard --logdir logs/tensorboard/
# Open http://localhost:6006
```

**Metrics tracked**:
- Training loss (MSE)
- Validation loss
- Learning rate
- Gradient norms

### MLflow

```bash
mlflow ui
# Open http://localhost:5000
```

**Logged**:
- Hyperparameters
- Metrics (AUC, precision, recall)
- Model artifacts
- Configuration files

---

## 🛠️ Dependencies

```bash
pip install -r requirements.txt
```

**Key Dependencies**:
- `tensorflow==2.14` or `torch==2.0`
- `scikit-learn==1.3`
- `pandas==2.0`
- `numpy==1.24`
- `onnx==1.14`
- `onnxruntime==1.15`

---

## 📚 Related Documentation

- **Configuration**: `configs/engine_vibration_config.yaml`
- **Data Contracts**: `../../DATA/contracts/README.md`
- **Model Registry**: `../../REGISTRY/README.md`
- **Inference**: `../inference/README.md`

---

**Owner**: Data Science Team  
**Contact**: datascience@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
