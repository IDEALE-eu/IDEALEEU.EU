# 🔄 REGRESSION TESTS

**Path**: `TESTS/regression/`  
**Purpose**: Ensure model outputs remain consistent across code changes

---

## 🎯 Overview

Regression tests verify that **model behavior hasn't changed** when code is refactored or dependencies are updated. They use golden outputs (reference results) to detect unintended changes.

## 📂 Directory Structure

```
regression/
├── golden_outputs/                # Reference outputs
│   ├── features_golden.parquet
│   ├── inference_golden.json
│   └── metrics_golden.json
├── test_feature_regression.py     # Feature extraction consistency
├── test_inference_regression.py   # Inference output consistency
├── test_metrics_regression.py     # Metrics calculation consistency
└── README.md (this file)
```

## 🧪 Test Philosophy

**Principle**: Same input → Same output (within tolerance)

**Use Cases**:
- Detect breaking changes during refactoring
- Verify dependency upgrades don't change behavior
- Ensure model version consistency

---

## 📝 Test Types

### 1. Feature Extraction Regression

**Test**: `test_feature_regression.py`

**What's Tested**: Feature engineering produces identical results

**Example**:
```python
def test_feature_extraction_regression():
    """Test that feature extraction produces same results as golden output"""
    # Load test input
    windows = load_test_windows("test_data/windows.parquet")
    
    # Extract features
    features = extract_features(windows)
    
    # Load golden output
    golden_features = pd.read_parquet("golden_outputs/features_golden.parquet")
    
    # Compare (allow small numerical differences)
    pd.testing.assert_frame_equal(
        features, 
        golden_features, 
        rtol=1e-6,  # Relative tolerance
        atol=1e-8   # Absolute tolerance
    )
```

**Golden Output Generation**:
```bash
# Generate golden output (once, when features are verified correct)
python ../../PIPELINES/training/featurize.py \
    --input test_data/windows.parquet \
    --output golden_outputs/features_golden.parquet
```

---

### 2. Inference Output Regression

**Test**: `test_inference_regression.py`

**What's Tested**: Model inference produces consistent predictions

**Example**:
```python
def test_inference_output_regression():
    """Test that ONNX model produces same outputs as golden"""
    # Load model
    model = load_onnx_model("../../MODELS/.../model.onnx")
    
    # Load test features
    test_features = load_test_features("test_data/features.npy")
    
    # Run inference
    predictions = model.run(None, {"input_features": test_features})[0]
    
    # Load golden predictions
    golden_predictions = np.load("golden_outputs/inference_golden.npy")
    
    # Compare
    np.testing.assert_allclose(
        predictions, 
        golden_predictions, 
        rtol=1e-5,
        atol=1e-7
    )
```

---

### 3. Metrics Calculation Regression

**Test**: `test_metrics_regression.py`

**What's Tested**: Evaluation metrics calculated consistently

**Example**:
```python
def test_metrics_calculation_regression():
    """Test that evaluation metrics match golden values"""
    # Load test predictions and labels
    y_true = load_test_labels("test_data/labels.npy")
    y_pred = load_test_predictions("test_data/predictions.npy")
    
    # Compute metrics
    metrics = compute_metrics(y_true, y_pred)
    
    # Load golden metrics
    with open("golden_outputs/metrics_golden.json") as f:
        golden_metrics = json.load(f)
    
    # Compare
    for key in ['auc', 'precision', 'recall', 'f1']:
        assert abs(metrics[key] - golden_metrics[key]) < 1e-6
```

---

## 🗂️ Golden Output Management

### Generating Golden Outputs

**When to Generate**:
- Initial test setup
- After verified feature improvements
- After intentional algorithm changes

**How to Generate**:
```bash
# 1. Verify current behavior is correct (manual inspection)
# 2. Generate golden outputs
python generate_golden_outputs.py

# 3. Commit golden outputs to version control
git add golden_outputs/
git commit -m "Update golden outputs for v1.1.0"
```

### Updating Golden Outputs

**When to Update**:
- ✅ Intentional algorithm improvement
- ✅ Bug fix that changes correct behavior
- ❌ Refactoring (should NOT change output)
- ❌ Dependency update (should NOT change output)

**Process**:
1. Verify change is intentional and correct
2. Regenerate golden outputs
3. Document reason in commit message
4. Update test assertions if tolerance needs adjustment

---

## 🚀 Running Regression Tests

### Run All Regression Tests

```bash
cd TESTS/regression/
pytest -v
```

**Expected Output**:
```
test_feature_regression.py::test_feature_extraction_regression PASSED  [33%]
test_inference_regression.py::test_inference_output_regression PASSED  [66%]
test_metrics_regression.py::test_metrics_calculation_regression PASSED [100%]

==================== 3 passed in 5.67s ====================
```

### Run with Detailed Diff

```bash
pytest -v --tb=long
```

If test fails, shows detailed diff of expected vs. actual.

---

## 🔍 Interpreting Failures

### Failure: Feature Extraction Mismatch

**Possible Causes**:
- Refactoring bug introduced
- Dependency version changed behavior (e.g., NumPy, Pandas)
- Random seed not set (non-deterministic operations)

**Action**:
1. Check recent code changes
2. Verify dependency versions match
3. Set random seeds for reproducibility

### Failure: Inference Output Mismatch

**Possible Causes**:
- ONNX model regenerated with different settings
- Model weights changed
- ONNX Runtime version changed

**Action**:
1. Compare model checksums (MD5)
2. Verify model version matches test
3. Check ONNX Runtime version

### Failure: Metrics Mismatch

**Possible Causes**:
- Threshold changed
- Metrics calculation bug
- Label format changed

**Action**:
1. Review metrics calculation code
2. Verify labels match expected format
3. Check threshold configuration

---

## 📊 Test Tolerances

Different components have different numerical precision requirements:

| Component | Relative Tol | Absolute Tol | Reason |
|-----------|--------------|--------------|--------|
| **Feature Extraction** | 1e-6 | 1e-8 | Floating-point precision |
| **Inference** | 1e-5 | 1e-7 | ONNX conversion tolerance |
| **Metrics** | 1e-6 | 1e-8 | Statistical calculation |

**Adjust tolerances** if needed, but document reason:
```python
# Increased tolerance due to ONNX quantization
np.testing.assert_allclose(pred, golden, rtol=1e-4)  # Was 1e-5
```

---

## 🔧 Best Practices

### 1. Use Small Test Datasets

Golden outputs should be small (< 10 MB) to:
- Keep repository size manageable
- Make tests fast
- Easy to inspect manually

### 2. Version Golden Outputs

```bash
golden_outputs/
├── v1.0.0/
│   ├── features_golden.parquet
│   └── inference_golden.npy
└── v1.1.0/
    ├── features_golden.parquet
    └── inference_golden.npy
```

### 3. Document Golden Output Provenance

```json
// golden_outputs/metadata.json
{
  "generated_at": "2025-10-11T14:30:00Z",
  "model_version": "1.0.0",
  "code_commit": "a1b2c3d",
  "dependencies": {
    "numpy": "1.24.0",
    "pandas": "2.0.0",
    "onnxruntime": "1.15.0"
  },
  "test_data_source": "test_data/windows_sample_100.parquet"
}
```

---

## 📚 Related Documentation

- **Unit Tests**: `../unit/README.md`
- **Integration Tests**: `../integration/README.md`
- **CI/CD**: `.github/workflows/regression-test.yml`

---

**Owner**: Data Science Team  
**Contact**: datascience@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
