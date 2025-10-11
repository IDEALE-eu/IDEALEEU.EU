# Golden Test Vectors

This directory contains "golden" input/output pairs for validating model behavior after quantization or optimization.

## Files

- **golden_inputs.npz**: Reference input data (numpy archive)
- **golden_outputs.npz**: Expected output data from baseline FP32 model
- **tolerance.yaml**: Acceptable tolerances for different model variants

## Usage

```bash
# Validate a model variant against golden vectors
python ../../TOOLS/validate_onnx.py \
  --model ../model.int8.onnx \
  --test-data golden_inputs.npz
```

## Golden Vector Generation

Golden vectors were generated from the baseline FP32 model using a representative sample of test data:
- 100 normal operation samples
- 50 ice formation samples
- 25 edge case samples (extreme conditions)

## Notes

The golden vectors ensure that quantized or optimized model variants produce outputs within acceptable tolerances of the original FP32 model.
