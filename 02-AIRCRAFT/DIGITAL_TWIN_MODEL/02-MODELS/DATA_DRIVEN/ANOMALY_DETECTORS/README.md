# ANOMALY_DETECTORS

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/DATA_DRIVEN > ANOMALY_DETECTORS**

ML-based anomaly detection models with complete ML lifecycle infrastructure: data contracts, training pipelines, model registry, drift monitoring, and ATA system integration.

## Purpose

Detect anomalies in sensor data and system behavior for predictive maintenance, with focus on:
- **ATA-72**: Engine vibration anomaly detection (production)
- **ATA-32**: Landing gear health monitoring (planned)
- Other critical aircraft systems

## Directory Structure

```
ANOMALY_DETECTORS/
├─ DATA/
│  ├─ contracts/              # Data schemas and signal definitions
│  ├─ raw/                    # Immutable raw data ingestion
│  ├─ interim/                # Cleaned and synchronized data
│  ├─ processed/              # Windowed and preprocessed data
│  ├─ features/               # Engineered features (.parquet, .npy)
│  └─ labels/                 # Ground truth and event labels
├─ PIPELINES/
│  ├─ training/
│  │  ├─ configs/             # Training configurations (*.yaml)
│  │  ├─ preprocess.py        # Data preprocessing scripts
│  │  ├─ featurize.py         # Feature engineering scripts
│  │  ├─ train.py             # Model training scripts
│  │  ├─ evaluate.py          # Model evaluation scripts
│  │  └─ export.py            # Model export (ONNX, scaler, signature)
│  └─ inference/
│     ├─ realtime/
│     │  ├─ adapter_databus.py # Real-time data adapter
│     │  └─ configs/          # Real-time inference configs
│     └─ batch/
│        └─ run_batch.py      # Batch inference scripts
├─ MODELS/
│  └─ <detector>/<semver>/    # Versioned model artifacts
│     ├─ model.onnx           # ONNX model file
│     ├─ scaler.pkl           # Preprocessing scaler
│     ├─ signature.json       # Model signature (inputs/outputs)
│     ├─ thresholds.yaml      # Anomaly detection thresholds
│     ├─ metrics.json         # Performance metrics (ROC, PR, FAR)
│     ├─ explain/             # Explainability artifacts (SHAP, saliency)
│     └─ card.md              # Model card documentation
├─ EVALUATION/
│  ├─ offline/                # K-fold CV, ablation studies
│  └─ replay_dt/              # Digital twin replay validation
├─ DRIFT_MONITORING/
│  ├─ data_drift.yaml         # Data drift config (PSI, KS, KL)
│  ├─ concept_drift.yaml      # Concept drift config (ADWIN, DDM)
│  └─ alerts/                 # Drift alert logs
├─ REGISTRY/
│  └─ index.yaml              # Central model catalog and status
├─ TESTS/
│  ├─ unit/                   # Unit tests
│  ├─ integration/            # Integration tests
│  └─ regression/             # Regression tests (golden outputs)
├─ TOOLS/
│  ├─ validate_data.py        # Data validation utilities
│  ├─ check_signature.py      # Model signature validation
│  └─ bench_inference.py      # Inference benchmarking
├─ ATA_SYSTEM_CONNECTIONS.md  # ATA system integration guide
└─ README.md                  # This file
```

## Example: Engine Vibration Anomaly Detector

**Model ID**: `ANOMALY_DETECTOR_ENGINE_VIB_V1.0.0`  
**Status**: Production  
**ATA Chapter**: ATA-72 (Engine)  
**Criticality**: Level A (Catastrophic)

**Key Files**:
- **Data Contract**: `DATA/contracts/signals_engine_vibration.yaml`
- **Model Card**: `MODELS/engine_vibration_detector/1.0.0/card.md`
- **Training Config**: `PIPELINES/training/configs/engine_vibration_config.yaml`
- **Metrics**: `MODELS/engine_vibration_detector/1.0.0/metrics.json`
- **Registry Entry**: `REGISTRY/index.yaml`

**Performance**:
- AUC: 0.92
- Precision: 89.2%
- Recall: 87.5%
- False Alarm Rate: 2.7%
- Inference Latency: 12ms

## ML Lifecycle Integration

### 1. Data Ingestion and Contracts
- Raw sensor data from aircraft → `DATA/raw/`
- Validated against data contract → `DATA/contracts/signals_*.yaml`
- Immutable storage for auditability

### 2. Training Pipeline
- Configuration-driven training → `PIPELINES/training/configs/*.yaml`
- Preprocessing → Feature engineering → Training → Evaluation → Export
- Produces versioned model artifacts in `MODELS/<detector>/<semver>/`

### 3. Model Registry
- Central catalog of all models → `REGISTRY/index.yaml`
- Tracks status (development, validation, shadow mode, production, deprecated)
- Links to ATA chapters, certification evidence, ownership

### 4. Validation and Testing
- Offline validation: K-fold CV, holdout test sets
- Digital twin replay: Test against historical scenarios
- Shadow mode: 30-day operational validation before production

### 5. Deployment
- Real-time inference: MQTT streaming, ONNX runtime
- Batch inference: Parquet processing for historical analysis
- Edge deployment: Planned for Phase 2

### 6. Continuous Monitoring
- **Data Drift**: PSI, KS test, KL divergence (`DRIFT_MONITORING/data_drift.yaml`)
- **Concept Drift**: ADWIN, DDM, performance tracking (`DRIFT_MONITORING/concept_drift.yaml`)
- **Alerts**: Automated notifications, retraining triggers

## ATA System Integration

This anomaly detection framework integrates with physical aircraft systems per ATA chapters:

- **ATA-72 (Engine)**: Vibration-based bearing health monitoring (production)
- **ATA-32 (Landing Gear)**: Structural health and retraction anomalies (planned)
- **Future**: ATA-27 (Flight Controls), ATA-28 (Fuel System), ATA-24 (Electrical)

See `ATA_SYSTEM_CONNECTIONS.md` for detailed system mapping, data flow, and maintenance integration.

## Model Formats

- **ONNX**: Neural network models (autoencoders, LSTM)
- **Pickle**: Scikit-learn models (Isolation Forest, One-Class SVM, scalers)
- **YAML/JSON**: Configurations, thresholds, signatures, registry

## Performance Requirements

- **Sensitivity (Recall)**: >85% (true positive rate)
- **Specificity**: >95% (true negative rate)
- **False Alarm Rate**: <5%
- **AUC (ROC)**: >0.90 for Level A systems
- **Inference Latency**: <50ms (real-time requirements)

## Validation Requirements

- **Cross-Validation**: 5-fold stratified CV on historical data
- **Operational Validation**: 30-day shadow mode (min 100 aircraft for Level A)
- **Safety Assessment**: FMEA, FTA per ARP4754A
- **Software Compliance**: DO-178C Level A for catastrophic systems

## Data Governance

- **Privacy**: No PII, pseudonymization enforced
- **Retention**: 2 years operational, 7 years archived
- **Encryption**: TLS 1.3 in transit, AES-256 at rest
- **Access Control**: Role-based (ML Team, Maintenance, Safety)

## Compliance Standards

- **ARP4754A**: Safety assessment process
- **DO-178C**: Software development (Level A/B)
- **DO-326A**: Cybersecurity (model signing, secure deployment)
- **DO-200B**: Processing aeronautical data
- **EASA Part-21J**: Design Organization Approval

## Getting Started

### 1. Create a New Anomaly Detector

```bash
# 1. Define data contract
cp DATA/contracts/signals_engine_vibration.yaml DATA/contracts/signals_my_system.yaml
# Edit signal definitions, ATA references, quality requirements

# 2. Create training configuration
cp PIPELINES/training/configs/engine_vibration_config.yaml PIPELINES/training/configs/my_system_config.yaml
# Edit model architecture, hyperparameters, quality gates

# 3. Run training pipeline
python PIPELINES/training/train.py --config configs/my_system_config.yaml

# 4. Create model card
cp MODELS/engine_vibration_detector/1.0.0/card.md MODELS/my_detector/1.0.0/card.md
# Document model details, performance, limitations

# 5. Register model
# Add entry to REGISTRY/index.yaml with status: development
```

### 2. Deploy a Model

```bash
# 1. Validate model
python TOOLS/check_signature.py --model MODELS/my_detector/1.0.0/model.onnx

# 2. Benchmark inference
python TOOLS/bench_inference.py --model MODELS/my_detector/1.0.0/

# 3. Update registry status to shadow_mode
# Deploy to limited fleet for 30 days

# 4. Monitor performance (DRIFT_MONITORING/)
# Review weekly reports, check for drift

# 5. Production release
# Update registry status to production after validation
```

## Related Documents

- **Model Card Template**: `../../13-TEMPLATES/MODEL_CARD_TEMPLATE.md`
- **ATA Mapping**: `../../09-INTEGRATIONS/ATA_MAPPING.md`
- **Update Policy**: `../../08-SYNCHRONISATION/UPDATE_POLICY.md`
- **Certification Evidence**: `../../06-VALIDATION_VERIFICATION/CERT_EVIDENCE_LINKS.md`
- **Data Contracts (Fleet)**: `../../../../01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/`

## Contacts

- **Model Owner**: Data Science Team (datascience@ideale.eu)
- **Engine Systems (ATA-72)**: John Peterson (john.peterson@ideale.eu)
- **Landing Gear (ATA-32)**: Maria Garcia (maria.garcia@ideale.eu)
- **Safety Engineering**: Sarah Williams (sarah.williams@ideale.eu)
- **Configuration Control**: CCB (ccb@ideale.eu)

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
