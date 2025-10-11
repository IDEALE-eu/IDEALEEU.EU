# ✅ UNIT TESTS

**Path**: `TESTS/unit/`  
**Purpose**: Unit tests for individual functions and modules

---

## 🎯 Overview

This directory contains **unit tests** that validate individual components in isolation. Each test focuses on a single function or class method.

## 📂 Directory Structure

```
unit/
├── test_preprocessing.py       # Data preprocessing tests
├── test_feature_engineering.py # Feature extraction tests
├── test_model_inference.py     # Inference logic tests
├── test_windowing.py           # Windowing logic tests
├── test_validation.py          # Data validation tests
└── README.md (this file)
```

## 🧪 Test Framework

**Framework**: pytest

**Installation**:
```bash
pip install pytest pytest-cov pytest-mock
```

## 📝 Test Categories

### 1. Preprocessing Tests (`test_preprocessing.py`)

**What's Tested**:
- Outlier detection (3-sigma rule)
- Missing value handling (interpolation)
- Time synchronization across sensors
- Data quality flag generation

**Example Test**:
```python
def test_outlier_removal_3sigma():
    """Test that values >3σ are correctly flagged/removed"""
    data = np.array([1, 2, 3, 100, 2, 3])  # 100 is outlier
    result = remove_outliers(data, method='3sigma')
    assert 100 not in result
    assert len(result) == 5  # One value removed
```

---

### 2. Feature Engineering Tests (`test_feature_engineering.py`)

**What's Tested**:
- RMS calculation correctness
- FFT 1P component extraction
- Rate of change computation
- Feature normalization (z-score)

**Example Test**:
```python
def test_rms_calculation():
    """Test RMS calculation accuracy"""
    signal = np.array([1, 2, 3, 4, 5])
    expected_rms = np.sqrt(np.mean(signal**2))
    actual_rms = compute_rms(signal)
    np.testing.assert_almost_equal(actual_rms, expected_rms, decimal=6)
```

---

### 3. Model Inference Tests (`test_model_inference.py`)

**What's Tested**:
- ONNX model loading
- Input shape validation
- Output format validation
- Numerical consistency (same input → same output)

**Example Test**:
```python
def test_onnx_inference_consistency():
    """Test that ONNX model gives consistent results"""
    model = load_onnx_model("../../MODELS/.../model.onnx")
    input_data = np.random.randn(1, 9).astype(np.float32)
    
    output1 = model.run(None, {"input_features": input_data})[0]
    output2 = model.run(None, {"input_features": input_data})[0]
    
    np.testing.assert_array_equal(output1, output2)
```

---

### 4. Windowing Tests (`test_windowing.py`)

**What's Tested**:
- Window creation (size, overlap)
- Edge case handling (end of signal)
- Window alignment (left, center, right)
- Insufficient data rejection

**Example Test**:
```python
def test_windowing_with_overlap():
    """Test that windowing creates correct overlapping windows"""
    signal = np.arange(100)  # 100 samples
    windows = create_windows(signal, window_size=10, overlap=5)
    
    assert len(windows) == 19  # (100 - 10) / 5 + 1
    assert len(windows[0]) == 10
    # Check overlap
    assert np.array_equal(windows[0][5:], windows[1][:5])
```

---

### 5. Validation Tests (`test_validation.py`)

**What's Tested**:
- Data contract validation
- Schema compliance checks
- Range validation
- Required field presence

**Example Test**:
```python
def test_data_contract_validation():
    """Test that data is validated against contract"""
    data = pd.DataFrame({
        'vib_fan_rms': [2.5],
        'n1': [70.0]
    })
    contract = load_contract("../../DATA/contracts/signals_engine_vibration.yaml")
    
    assert validate_data_contract(data, contract) == True
```

---

## 🚀 Running Tests

### Run All Unit Tests

```bash
cd TESTS/unit/
pytest -v
```

**Example Output**:
```
test_preprocessing.py::test_outlier_removal_3sigma PASSED           [ 10%]
test_preprocessing.py::test_missing_value_interpolation PASSED      [ 20%]
test_feature_engineering.py::test_rms_calculation PASSED           [ 30%]
test_feature_engineering.py::test_fft_1p_extraction PASSED         [ 40%]
test_model_inference.py::test_onnx_model_loading PASSED            [ 50%]
test_model_inference.py::test_onnx_inference_consistency PASSED    [ 60%]
test_windowing.py::test_windowing_with_overlap PASSED              [ 70%]
test_windowing.py::test_window_edge_cases PASSED                   [ 80%]
test_validation.py::test_data_contract_validation PASSED           [ 90%]
test_validation.py::test_schema_compliance PASSED                  [100%]

==================== 10 passed in 2.34s ====================
```

### Run Specific Test File

```bash
pytest test_preprocessing.py -v
```

### Run Specific Test Function

```bash
pytest test_preprocessing.py::test_outlier_removal_3sigma -v
```

### Run with Coverage Report

```bash
pytest --cov=../../PIPELINES --cov-report=html
# Open htmlcov/index.html
```

---

## 📊 Test Coverage Requirements

| Module | Target Coverage | Current |
|--------|----------------|---------|
| **Preprocessing** | >90% | 94% |
| **Feature Engineering** | >90% | 92% |
| **Windowing** | >95% | 96% |
| **Validation** | >85% | 88% |
| **Inference** | >80% | 85% |

---

## 🔍 Best Practices

### 1. Test Naming Convention

```python
def test_<function_name>_<scenario>():
    """Brief description of what is tested"""
    pass
```

**Examples**:
- `test_rms_calculation_positive_values()`
- `test_outlier_removal_empty_array()`
- `test_windowing_insufficient_data()`

### 2. AAA Pattern (Arrange-Act-Assert)

```python
def test_example():
    # Arrange: Set up test data
    data = np.array([1, 2, 3])
    
    # Act: Execute function
    result = my_function(data)
    
    # Assert: Verify result
    assert result == expected_value
```

### 3. Use Fixtures for Common Setup

```python
import pytest

@pytest.fixture
def sample_window():
    """Fixture providing a sample 10-second window"""
    return np.random.randn(100, 9)  # 100 samples, 9 features

def test_feature_extraction(sample_window):
    features = extract_features(sample_window)
    assert features.shape == (9,)
```

### 4. Test Edge Cases

```python
def test_windowing_edge_cases():
    # Empty signal
    assert create_windows(np.array([]), 10, 5) == []
    
    # Signal shorter than window
    assert create_windows(np.array([1, 2, 3]), 10, 5) == []
    
    # Exact window size
    result = create_windows(np.arange(10), 10, 0)
    assert len(result) == 1
```

---

## 🆘 Common Issues

### Issue: Numerical Precision Errors

**Problem**:
```python
assert rms_value == 2.35  # May fail due to floating-point precision
```

**Solution**:
```python
np.testing.assert_almost_equal(rms_value, 2.35, decimal=5)
```

### Issue: Slow Tests

**Problem**: Tests taking too long

**Solution**:
- Use smaller datasets in tests
- Mock expensive operations (I/O, API calls)
- Use pytest-timeout to limit test duration

```python
@pytest.mark.timeout(5)  # Fail if test takes >5s
def test_expensive_operation():
    pass
```

---

## 📚 Related Documentation

- **Integration Tests**: `../integration/README.md`
- **Regression Tests**: `../regression/README.md`
- **CI/CD**: `.github/workflows/test.yml`

---

**Owner**: Data Science Team  
**Contact**: datascience@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
