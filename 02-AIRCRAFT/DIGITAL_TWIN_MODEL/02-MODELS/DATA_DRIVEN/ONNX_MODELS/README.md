# ONNX_MODELS

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/DATA_DRIVEN > ONNX_MODELS**

Signed, versioned ONNX inference artifacts for deployment.

## Purpose

Production-ready ONNX models with signatures and version control.

## Contents

- **SIGNED_MODELS/** - GPG/SLSA-signed ONNX files
- **VERSION_REGISTRY/** - Model version manifest (model_id, version, signature)
- **RUNTIME_CONFIG/** - ONNX Runtime configuration (CPU/GPU, optimization level)

## Security

- **Model Signing**: All models signed with GPG key (see `../../07-RUNTIME_DEPLOYMENT/CYBERSECURITY.md`)
- **Integrity Check**: SHA-256 checksum verification before loading

## Model Versioning

Format: `<model_name>_v<major>.<minor>.<patch>.onnx`

Example: `anomaly_detector_h2_leak_v1.2.3.onnx`

## Deployment Process

1. Train model → Export to ONNX → Validate inference
2. Sign model with GPG key → Generate SHA-256 checksum
3. Upload to model registry → Update VERSION_REGISTRY
4. Deploy via CI/CD pipeline (see `../../12-CODE/CI_CD/`)

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
