# ONNX Model Tools

Python scripts for exporting, validating, optimizing, and profiling ONNX models.

## Prerequisites

```bash
pip install onnx onnxruntime numpy
pip install tensorflow tf2onnx  # For TensorFlow models
pip install torch  # For PyTorch models
pip install scikit-learn skl2onnx  # For scikit-learn models
pip install psutil  # For memory profiling
```

For TensorRT support (NVIDIA GPUs only):
```bash
# Install TensorRT from https://developer.nvidia.com/tensorrt
pip install pycuda
```

## Tool Overview

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `export_to_onnx.py` | Export trained models to ONNX | After training, before deployment |
| `validate_onnx.py` | Validate model structure and run test inference | After export, before optimization |
| `quantize_onnx.py` | Quantize to INT8/FP16 for edge deployment | Before deploying to resource-constrained devices |
| `profile_ort.py` | Profile latency, throughput, memory | After optimization, before deployment |
| `build_trt_engine.py` | Build TensorRT engine for NVIDIA GPUs | For GPU-accelerated inference |

## Usage Examples

### 1. Export TensorFlow Model to ONNX

```bash
python export_to_onnx.py \
  --model-path /path/to/trained_model.h5 \
  --framework tf \
  --output ../ice_detector_pitot/1.0.0/model.onnx \
  --opset 17
```

**Output:**
- `model.onnx` - ONNX model file
- `opset.txt` - ONNX opset version

### 2. Export PyTorch Model to ONNX

```bash
python export_to_onnx.py \
  --model-path /path/to/model.pth \
  --framework torch \
  --output ../model.onnx \
  --opset 17 \
  --input-shape "1,50"  # batch_size=1, features=50
```

### 3. Export scikit-learn Model to ONNX

```bash
python export_to_onnx.py \
  --model-path /path/to/model.pkl \
  --framework sklearn \
  --output ../model.onnx
```

### 4. Validate ONNX Model

```bash
# Basic validation (structure + dummy inference)
python validate_onnx.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx

# With test data (golden vectors)
python validate_onnx.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx \
  --test-data ../ice_detector_pitot/1.0.0/tests/golden_inputs.npz \
  --runtime ort
```

**Checks:**
- ✓ Model structure integrity (ONNX checker)
- ✓ Shape inference
- ✓ Opset compatibility (ORT, TensorRT, OpenVINO)
- ✓ Test inference (runs successfully)

### 5. Quantize Model

#### Dynamic INT8 Quantization (No Calibration)

```bash
python quantize_onnx.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx \
  --mode int8_dynamic \
  --output ../ice_detector_pitot/1.0.0/model.int8.onnx
```

**Use Case:** Quick quantization for edge deployment, ~4x size reduction.

#### Static INT8 Quantization (With Calibration)

```bash
python quantize_onnx.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx \
  --mode int8_static \
  --output ../ice_detector_pitot/1.0.0/model.int8.onnx \
  --calibration-data ../calibration_data.npz
```

**Use Case:** Best INT8 accuracy, requires calibration dataset.

#### FP16 Quantization

```bash
python quantize_onnx.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx \
  --mode fp16 \
  --output ../ice_detector_pitot/1.0.0/model.fp16.onnx
```

**Use Case:** GPU acceleration with Tensor Cores, ~2x size reduction.

### 6. Profile Performance

```bash
python profile_ort.py \
  --model ../ice_detector_pitot/1.0.0/model.int8.onnx \
  --batch-size 1 \
  --iterations 100 \
  --duration 10 \
  --output ../ice_detector_pitot/1.0.0/benchmarks/latency.json
```

**Metrics:**
- Latency: mean, std, p50, p95, p99 (ms)
- Throughput: inferences per second
- Memory: peak RSS (MB)

**With per-operator profiling:**

```bash
python profile_ort.py \
  --model ../ice_detector_pitot/1.0.0/model.int8.onnx \
  --batch-size 1 \
  --iterations 100 \
  --profile-ops
```

### 7. Build TensorRT Engine

```bash
# FP16 precision (recommended for NVIDIA GPUs)
python build_trt_engine.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx \
  --output ../ice_detector_pitot/1.0.0/model.fp16.trt \
  --precision fp16 \
  --max-batch-size 1 \
  --workspace-size-gb 1
```

**INT8 with calibration:**

```bash
python build_trt_engine.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx \
  --output ../ice_detector_pitot/1.0.0/model.int8.trt \
  --precision int8 \
  --calibration-data ../calibration_data.npz
```

**Verify engine:**

```bash
python build_trt_engine.py \
  --model ../model.onnx \
  --output ../model.trt \
  --precision fp16 \
  --verify
```

## Complete Workflow

Here's a typical end-to-end workflow:

```bash
# 1. Export trained model to ONNX
python export_to_onnx.py \
  --model-path /path/to/trained_model.h5 \
  --framework tf \
  --output ../ice_detector_pitot/1.0.0/model.onnx \
  --opset 17

# 2. Validate baseline model
python validate_onnx.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx

# 3. Generate quantized variants
python quantize_onnx.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx \
  --mode int8_dynamic \
  --output ../ice_detector_pitot/1.0.0/model.int8.onnx

# 4. Validate quantized model
python validate_onnx.py \
  --model ../ice_detector_pitot/1.0.0/model.int8.onnx \
  --test-data ../ice_detector_pitot/1.0.0/tests/golden_inputs.npz

# 5. Profile performance
python profile_ort.py \
  --model ../ice_detector_pitot/1.0.0/model.int8.onnx \
  --batch-size 1 \
  --iterations 100 \
  --output ../ice_detector_pitot/1.0.0/benchmarks/latency.json

# 6. Build TensorRT engine (if GPU available)
python build_trt_engine.py \
  --model ../ice_detector_pitot/1.0.0/model.onnx \
  --output ../ice_detector_pitot/1.0.0/model.fp16.trt \
  --precision fp16
```

## Golden Vector Testing

To create golden test vectors for validation:

```python
import numpy as np

# Create test inputs
test_inputs = {
    'sensor_readings': np.random.randn(100, 50).astype(np.float32)
}

# Save as NPZ
np.savez('golden_inputs.npz', **test_inputs)

# Run baseline model to generate expected outputs
# (use validate_onnx.py or your own inference code)
```

## Troubleshooting

### Import Errors

If you get import errors, ensure all dependencies are installed:

```bash
pip install onnx onnxruntime numpy tensorflow tf2onnx torch scikit-learn skl2onnx psutil
```

### Opset Compatibility

If validation fails due to opset version:

- **ONNX Runtime**: Supports opset 7-18
- **TensorRT**: Supports opset 7-17
- **OpenVINO**: Supports opset 10-17

Use `--opset 17` for maximum compatibility.

### Quantization Accuracy

If quantized model accuracy drops significantly:

1. Use static INT8 quantization with calibration data
2. Try FP16 instead of INT8
3. Adjust tolerance in `tests/tolerance.yaml`
4. Consider selective quantization (quantize some layers, not all)

### TensorRT Installation

TensorRT requires:
- NVIDIA GPU with CUDA support
- CUDA Toolkit installed
- TensorRT downloaded from NVIDIA Developer

If you don't have a GPU, skip TensorRT and use ONNX Runtime CPU backend.

## CI/CD Integration

These tools can be integrated into a CI/CD pipeline:

```yaml
# .github/workflows/onnx-pipeline.yml
name: ONNX Model Pipeline

on:
  push:
    paths:
      - 'models/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install dependencies
        run: pip install onnx onnxruntime numpy
      - name: Validate ONNX model
        run: |
          cd ONNX_MODELS/TOOLS
          python validate_onnx.py --model ../ice_detector_pitot/1.0.0/model.onnx
      - name: Run golden vector tests
        run: |
          python validate_onnx.py \
            --model ../ice_detector_pitot/1.0.0/model.onnx \
            --test-data ../ice_detector_pitot/1.0.0/tests/golden_inputs.npz
```

## Additional Resources

- **ONNX Documentation**: https://onnx.ai/
- **ONNX Runtime**: https://onnxruntime.ai/
- **TensorRT**: https://developer.nvidia.com/tensorrt
- **Model Card Template**: `../../13-TEMPLATES/MODEL_CARD_TEMPLATE.md`
- **Integration Guide**: `../INTEGRATION_GUIDE.md`

## Support

For issues or questions:
- Email: ml-ops@ideale-eu.eu
- Documentation: `../README.md`
- Integration guide: `../INTEGRATION_GUIDE.md`
