# ONNX_MODELS

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/DATA_DRIVEN > ONNX_MODELS**

Production-ready ONNX models with full CI/CD pipeline for ML deployment.

## Purpose

This directory provides a complete infrastructure for deploying machine learning models to aircraft systems, bridging the gap between data science development and certified aviation software.

## Directory Structure

```
ONNX_MODELS/
├── REGISTRY/
│   └── index.yaml                 # Model catalog and deployment status
├── TOOLS/
│   ├── export_to_onnx.py          # Export from TF/PyTorch/sklearn → ONNX
│   ├── validate_onnx.py           # Validate structure, opset, inference
│   ├── quantize_onnx.py           # Quantization (INT8/FP16)
│   ├── profile_ort.py             # Performance profiling
│   └── build_trt_engine.py        # TensorRT optimization (optional)
├── TEMPLATES/
│   ├── signature.example.json     # Model signature template
│   └── io_contract.example.yaml   # I/O contract template
└── <model_id>/<semver>/
    ├── model.onnx                 # Baseline FP32 model
    ├── model.fp16.onnx            # FP16 variant (if applicable)
    ├── model.int8.onnx            # INT8 quantized variant
    ├── opset.txt                  # ONNX opset version (e.g., 17)
    ├── signature.json             # Input/output names, dtypes, shapes
    ├── io_contract.yaml           # Data transformations and scaling
    ├── preprocess.yaml            # Windowing and normalization
    ├── postprocess.yaml           # Thresholding and alert logic
    ├── artifacts/
    │   ├── scaler.pkl             # Fitted preprocessing artifacts
    │   └── labels.json            # Class labels
    ├── runtimes/
    │   ├── ort/                   # ONNX Runtime configs
    │   ├── trt/                   # TensorRT engine and calibration
    │   └── openvino/              # OpenVINO IR blobs (if applicable)
    ├── benchmarks/
    │   ├── hw_profile.yaml        # Target hardware specifications
    │   ├── latency.json           # Inference latency metrics
    │   └── accuracy.json          # Model accuracy on test set
    ├── tests/
    │   ├── golden_inputs.npz      # Reference test inputs
    │   ├── golden_outputs.npz     # Expected outputs
    │   └── tolerance.yaml         # Acceptable tolerances per variant
    ├── explain/                   # Model explainability (SHAP, saliency)
    ├── checksum.sha256            # File integrity checksums
    ├── license.txt                # Model license
    └── card.md                    # Model card (metadata, limitations)
```

## CI/CD Pipeline for ML Models

This structure enables a complete deployment pipeline:

1. **Export & Version**: Train model in [ANOMALY_DETECTORS](../ANOMALY_DETECTORS/) → Export to ONNX → Create versioned directory
2. **Optimize**: Generate FP16/INT8 variants using `quantize_onnx.py` and `build_trt_engine.py`
3. **Validate**: Run `validate_onnx.py` and golden vector tests to ensure correctness
4. **Benchmark**: Profile performance on target hardware using `profile_ort.py`
5. **Register**: Update `REGISTRY/index.yaml` with model metadata and deployment status
6. **Deploy**: Digital Twin or flight software loads optimized model variant

## Model Registry

The `REGISTRY/index.yaml` serves as the central catalog of all deployed models:

```yaml
models:
  - model_id: ice_detector_pitot
    name: Ice Detection - Pitot Sensor
    ata_chapter: ATA-34-12
    versions:
      - semver: 1.0.0
        status: deployed
        variants: [baseline, fp16, int8]
        deployed_to: ["AC001", "AC002"]
```

**Status Values**: `draft`, `validated`, `canary`, `deployed`, `deprecated`, `archived`

## Example Models

### Ice Detector (Pitot Tube)
**Path**: `ice_detector_pitot/1.0.0/`  
**Purpose**: Detect ice formation on pitot tube sensors  
**Algorithm**: Autoencoder anomaly detection  
**ATA Chapter**: ATA-34-12

See [ice_detector_pitot/1.0.0/card.md](ice_detector_pitot/1.0.0/card.md) for full model card.

## Tools Usage

### Export Model to ONNX
```bash
python TOOLS/export_to_onnx.py \
  --model-path /path/to/trained/model.h5 \
  --framework tf \
  --output ice_detector_pitot/1.0.0/model.onnx \
  --opset 17
```

### Validate ONNX Model
```bash
python TOOLS/validate_onnx.py \
  --model ice_detector_pitot/1.0.0/model.onnx \
  --test-data ice_detector_pitot/1.0.0/tests/golden_inputs.npz
```

### Quantize for Edge Deployment
```bash
python TOOLS/quantize_onnx.py \
  --model ice_detector_pitot/1.0.0/model.onnx \
  --mode int8_dynamic \
  --output ice_detector_pitot/1.0.0/model.int8.onnx
```

### Profile Performance
```bash
python TOOLS/profile_ort.py \
  --model ice_detector_pitot/1.0.0/model.int8.onnx \
  --batch-size 1 \
  --iterations 100 \
  --output ice_detector_pitot/1.0.0/benchmarks/latency.json
```

## Model Signature and I/O Contract

### Signature (`signature.json`)
Defines the model's input/output interface:
- Tensor names, shapes, and data types
- Metadata (author, training data version, accuracy)
- Dependencies (runtime versions)

See [TEMPLATES/signature.example.json](TEMPLATES/signature.example.json) for detailed example.

### I/O Contract (`io_contract.yaml`)
Defines how data flows into and out of the model:
- **Input**: Sensor mapping, windowing, normalization, validation
- **Output**: Thresholds, alerts, temporal smoothing
- **Integration**: How the model is called from flight software

See [TEMPLATES/io_contract.example.yaml](TEMPLATES/io_contract.example.yaml) for detailed example.

## Integration with Flight Software

### Example: ATA-22 Auto Flight Control Logic

A model can be integrated with flight control software (e.g., Simulink) by:

1. **Load Model**: Load ONNX model using ONNX Runtime C++ API
2. **Preprocess**: Apply windowing and normalization from `preprocess.yaml`
3. **Inference**: Run model inference on sensor data stream
4. **Postprocess**: Apply thresholds and alert logic from `postprocess.yaml`
5. **Action**: Trigger control actions (e.g., activate pitot heater)

The `io_contract.yaml` specifies the exact data transformations and integration points.

## Security

- **Checksums**: All files have SHA-256 checksums in `checksum.sha256`
- **Model Signing**: Models can be signed with GPG keys (see `../../07-RUNTIME_DEPLOYMENT/CYBERSECURITY.md`)
- **Integrity Verification**: Runtime performs checksum verification before loading

## Model Versioning

Format: `<model_id>/<major>.<minor>.<patch>/`

- **Major**: Breaking changes (input/output signature change)
- **Minor**: Backward-compatible improvements (accuracy, performance)
- **Patch**: Bug fixes, documentation updates

Example: `ice_detector_pitot/1.0.0/`

## Deployment Process

1. Train model in [ANOMALY_DETECTORS](../ANOMALY_DETECTORS/) or [SURROGATES](../SURROGATES/)
2. Export to ONNX using `TOOLS/export_to_onnx.py`
3. Create versioned directory structure
4. Generate signature and I/O contract
5. Optimize (quantization, TensorRT)
6. Validate with golden vectors
7. Benchmark on target hardware
8. Update `REGISTRY/index.yaml`
9. Deploy via CI/CD pipeline (see `../../12-CODE/CI_CD/`)

## Related Documentation

- [**MODEL_CARD_TEMPLATE.md**](../../13-TEMPLATES/MODEL_CARD_TEMPLATE.md) - Model documentation template
- [**DATA_CONTRACTS**](../../../../01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/) - Telemetry schema definitions
- [**REFERENCE_ARCHITECTURE.md**](../../01-ARCHITECTURE/REFERENCE_ARCHITECTURE.md) - Digital Twin architecture
- [**CONTROL_LOGIC**](../BEHAVIORAL/CONTROL_LOGIC/) - Flight control integration points

## Next Steps

For new model deployment:
1. Review [TEMPLATES/](TEMPLATES/) for signature and contract examples
2. Follow the export and validation process using [TOOLS/](TOOLS/)
3. Create model card using [card.md](ice_detector_pitot/1.0.0/card.md) as template
4. Register model in [REGISTRY/index.yaml](REGISTRY/index.yaml)

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
