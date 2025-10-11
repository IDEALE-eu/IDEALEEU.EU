# 🔗 INTEGRATION TESTS

**Path**: `TESTS/integration/`  
**Purpose**: Test interactions between components and end-to-end workflows

---

## 🎯 Overview

Integration tests validate that **multiple components work together correctly**. These tests check data flow through the entire pipeline, API integrations, and system interactions.

## 📂 Directory Structure

```
integration/
├── test_pipeline_end_to_end.py        # Full training pipeline
├── test_inference_pipeline.py         # Real-time + batch inference
├── test_data_contract_integration.py  # Data validation flow
├── test_model_export_import.py        # Model serialization
├── test_mqtt_integration.py           # MQTT data ingestion
└── README.md (this file)
```

## 🧪 Test Scenarios

### 1. End-to-End Training Pipeline

**Test**: `test_pipeline_end_to_end.py`

**What's Tested**:
```
Raw Data → Preprocess → Featurize → Train → Evaluate → Export
```

**Example**:
```python
def test_full_training_pipeline():
    """Test complete training pipeline from raw data to ONNX model"""
    # 1. Preprocess
    preprocess_result = run_preprocessing(
        raw_data_path="test_data/raw/",
        output_path="test_data/interim/"
    )
    assert preprocess_result.success
    
    # 2. Featurize
    features = run_featurization(
        interim_path="test_data/interim/",
        output_path="test_data/features/"
    )
    assert features.shape[1] == 9  # 9 features
    
    # 3. Train
    model = run_training(
        features_path="test_data/features/",
        config="test_config.yaml"
    )
    assert model is not None
    
    # 4. Export
    onnx_path = export_model(model, "test_model.onnx")
    assert os.path.exists(onnx_path)
    
    # 5. Validate ONNX
    onnx_model = onnx.load(onnx_path)
    onnx.checker.check_model(onnx_model)
```

---

### 2. Inference Pipeline Integration

**Test**: `test_inference_pipeline.py`

**What's Tested**:
- Real-time data ingestion → inference → alerting
- Batch processing → results aggregation
- Model loading and prediction consistency

**Example**:
```python
def test_realtime_inference_flow():
    """Test real-time inference from MQTT to alert"""
    # 1. Start inference service
    service = InferenceService(model_path="...")
    service.start()
    
    # 2. Send test data via MQTT
    mqtt_client.publish("aircraft/TEST/engine/vibration", test_payload)
    
    # 3. Wait for inference
    time.sleep(1)
    
    # 4. Check that inference completed
    assert service.get_inference_count() > 0
    
    # 5. Verify alert (if anomaly injected)
    alerts = service.get_alerts()
    if test_payload_is_anomaly:
        assert len(alerts) > 0
```

---

### 3. Data Contract Validation Flow

**Test**: `test_data_contract_integration.py`

**What's Tested**:
- Raw data ingestion with contract validation
- Rejection of non-compliant data
- Quality flag propagation

---

### 4. Model Export/Import Consistency

**Test**: `test_model_export_import.py`

**What's Tested**:
- TensorFlow/PyTorch → ONNX conversion
- Numerical consistency between frameworks
- Scaler export/import

**Example**:
```python
def test_model_export_import_consistency():
    """Test that exported ONNX model gives same results as original"""
    # Original model (TensorFlow)
    tf_model = load_tensorflow_model("model.h5")
    
    # Export to ONNX
    export_to_onnx(tf_model, "model.onnx")
    
    # Load ONNX
    onnx_model = load_onnx_model("model.onnx")
    
    # Compare outputs
    test_input = np.random.randn(1, 9).astype(np.float32)
    tf_output = tf_model.predict(test_input)
    onnx_output = onnx_model.run(None, {"input_features": test_input})[0]
    
    np.testing.assert_allclose(tf_output, onnx_output, rtol=1e-5)
```

---

## 🚀 Running Integration Tests

### Run All Integration Tests

```bash
cd TESTS/integration/
pytest -v --tb=short
```

### Run with Test Data Setup

```bash
# Set up test environment
./setup_test_env.sh

# Run tests
pytest -v

# Cleanup
./cleanup_test_env.sh
```

### Run Specific Integration Test

```bash
pytest test_pipeline_end_to_end.py -v
```

---

## 📊 Test Duration

Integration tests are slower than unit tests:

| Test | Duration | Why Slow |
|------|----------|----------|
| End-to-end pipeline | ~5 min | Training model |
| MQTT integration | ~30s | Network I/O |
| Batch inference | ~2 min | Processing data |
| Model export | ~1 min | ONNX conversion |

**Total**: ~10-15 minutes for full integration suite

---

## 🔧 Test Environment Setup

Integration tests require:

1. **Test Data**: Small representative dataset
   ```bash
   # Download test data
   aws s3 cp s3://test-data/engine_vibration_test.tar.gz .
   tar -xzf engine_vibration_test.tar.gz -C test_data/
   ```

2. **Services**: MQTT broker, database
   ```bash
   # Start services via Docker Compose
   docker-compose -f docker-compose.test.yml up -d
   ```

3. **Configuration**: Test-specific configs
   ```yaml
   # test_config.yaml
   data:
     raw_path: test_data/raw/
   model:
     epochs: 2  # Fast training for testing
   ```

---

## 📚 Related Documentation

- **Unit Tests**: `../unit/README.md`
- **Regression Tests**: `../regression/README.md`
- **CI/CD**: `.github/workflows/integration-test.yml`

---

**Owner**: Data Science Team + MLOps  
**Contact**: datascience@ideale.eu, mlops@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
