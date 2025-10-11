# Next Steps - ONNX Model Deployment Architecture

This document addresses the specific questions from the architecture proposal and outlines the next steps for implementing ONNX model deployment in the IDEALE-EU Digital Twin.

## Questions Addressed

### 1. ✅ Define the signature of a model (Ice detector example)

**Answer**: See [TEMPLATES/signature.example.json](TEMPLATES/signature.example.json) and [ice_detector_pitot/1.0.0/signature.json](ice_detector_pitot/1.0.0/signature.json)

The signature defines:
- **Model metadata**: ID, version, framework, opset, description, ATA chapter
- **Inputs**: Names, dtypes, shapes, feature descriptions, normalization method
- **Outputs**: Names, dtypes, shapes, interpretation (thresholds, units)
- **Dynamic axes**: Batch size flexibility
- **Dependencies**: Runtime versions (onnxruntime, numpy)

**Example (Ice Detector):**
```json
{
  "model_id": "ice_detector_pitot",
  "version": "1.0.0",
  "inputs": [
    {
      "name": "sensor_readings",
      "dtype": "float32",
      "shape": [null, 50],
      "description": "Time-windowed sensor readings",
      "features": ["airspeed_indicated", "static_pressure", ...]
    }
  ],
  "outputs": [
    {
      "name": "anomaly_score",
      "dtype": "float32",
      "shape": [null, 1],
      "interpretation": {
        "warning_threshold": 0.05,
        "critical_threshold": 0.15
      }
    }
  ]
}
```

### 2. ✅ Create an I/O contract (Pressure sensor scaling example)

**Answer**: See [TEMPLATES/io_contract.example.yaml](TEMPLATES/io_contract.example.yaml) and [ice_detector_pitot/1.0.0/io_contract.yaml](ice_detector_pitot/1.0.0/io_contract.yaml)

The I/O contract specifies:
- **Data sources**: ATA chapter, sample rate, EBOM references
- **Feature extraction**: Sensor-to-feature mapping, units, ranges, derived features
- **Preprocessing**: Windowing strategy, normalization (StandardScaler), validation rules
- **Postprocessing**: Thresholding, alert generation, temporal smoothing
- **Integration**: How the model is called (shared memory, message queue, function call)

**Example (Pressure Sensor Scaling):**
```yaml
inputs:
  sensor_readings:
    features:
      - name: static_pressure
        unit: hPa
        range: [100, 1100]
        source_signal: static_pressure
      
      - name: differential_pressure
        unit: hPa
        range: [0, 200]
        derived: true
        formula: total_pressure - static_pressure
    
    normalization:
      method: standard_scaler
      scaler_path: artifacts/scaler.pkl
      per_feature: true
      clipping:
        enabled: true
        n_sigma: 5  # Clip outliers beyond 5σ
```

### 3. ✅ Discuss Integration: How would ATA-22 Auto Flight CONTROL_LOGIC consume an ONNX model?

**Answer**: See [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)

**Integration Methods:**

#### A. Simulink S-Function (Recommended)

```cpp
// C++ MEX S-Function wrapper
static void mdlOutputs(SimStruct *S, int_T tid) {
    const real_T *sensor_data = ssGetInputPortSignal(S, 0);
    real_T *anomaly_score = ssGetOutputPortSignal(S, 0);
    
    // Run ONNX Runtime inference
    auto outputs = g_session->Run(..., sensor_data, ...);
    *anomaly_score = outputs[0];
}
```

**Simulink Block Diagram:**
```
[Sensor Bus] ──► [Windowing] ──► [ONNX Ice Detector] ──► [Alert Logic] ──► [Crew Alert]
  (ATA-34)                         (S-Function)                               (CAS)
```

#### B. External C++ Function (Embedded Coder)

```cpp
// External C++ function callable from Simulink
extern "C" void onnx_ice_detector_step(
    const float* inputs, 
    float* anomaly_score, 
    int* alert_level
);
```

**Called from MATLAB Function:**
```matlab
function [score, alert] = ice_detector(sensor_data)
    coder.cinclude('onnx_ice_detector.h');
    score = 0.0;
    alert = int32(0);
    coder.ceval('onnx_ice_detector_step', 
                coder.rref(sensor_data), 
                coder.wref(score), 
                coder.wref(alert));
end
```

#### C. ROS 2 Node (Alternative Architecture)

```
Flight Control ──► /sensor/pitot ──► ONNX Detector ──► /alerts/pitot ──► Alert Manager
   (Simulink)        (DDS topic)         (Node)          (DDS topic)        (CAS)
```

**Key Integration Points:**
- Model loads at system startup: `onnx_ice_detector_init()`
- Called at 10 Hz from flight control loop: `onnx_ice_detector_step()`
- Preprocessing (windowing, normalization) done in flight code
- Postprocessing (thresholds, alerts) applied after inference
- Fail-safe: Watchdog timer + hardware backup

## What's Been Created

### 1. REGISTRY/ - Model Catalog
- **index.yaml**: Central registry of all models, versions, deployment status
- Tracks: model_id, versions, variants (FP32, FP16, INT8), deployment targets, performance metrics

### 2. TOOLS/ - ML DevOps Scripts
- **export_to_onnx.py**: Export from TensorFlow/PyTorch/sklearn → ONNX
- **validate_onnx.py**: Validate structure, opset, run test inference
- **quantize_onnx.py**: Quantize to INT8/FP16 for edge deployment
- **profile_ort.py**: Profile latency, throughput, memory usage
- **build_trt_engine.py**: Build optimized TensorRT engine (GPU)

### 3. TEMPLATES/ - Example Contracts
- **signature.example.json**: Model input/output signature template
- **io_contract.example.yaml**: Data preprocessing/postprocessing contract

### 4. ice_detector_pitot/1.0.0/ - Complete Model Package
- **model.onnx**: Baseline FP32 model (placeholder)
- **model.fp16.onnx**: FP16 variant (placeholder)
- **model.int8.onnx**: INT8 quantized variant (placeholder)
- **opset.txt**: ONNX opset version (17)
- **signature.json**: Model signature
- **io_contract.yaml**: I/O contract
- **preprocess.yaml**: Windowing and normalization config
- **postprocess.yaml**: Thresholding and alert logic
- **artifacts/**: scaler.pkl, labels.json
- **runtimes/**: ORT, TensorRT, OpenVINO configs
- **benchmarks/**: hw_profile.yaml, latency.json, accuracy.json
- **tests/**: tolerance.yaml, golden vectors
- **explain/**: Model explainability artifacts
- **card.md**: Complete model card (documentation)
- **license.txt**: Model license
- **checksum.sha256**: File integrity checksums

### 5. Documentation
- **README.md**: Updated with complete structure and usage
- **INTEGRATION_GUIDE.md**: How to integrate with flight software
- **TOOLS/README.md**: Detailed tool usage and examples

## Next Steps

### Phase 1: Model Training and Export (Now → Week 1)

1. **Train ice detector model** in [ANOMALY_DETECTORS](../ANOMALY_DETECTORS/)
   - Use autoencoder architecture
   - Train on simulated + real pitot sensor data
   - Achieve >90% accuracy on test set

2. **Export to ONNX**
   ```bash
   python TOOLS/export_to_onnx.py \
     --model-path ../ANOMALY_DETECTORS/ice_detector/trained_model.h5 \
     --framework tf \
     --output ice_detector_pitot/1.0.0/model.onnx
   ```

3. **Create preprocessing artifacts**
   - Fit StandardScaler on training data
   - Save to `artifacts/scaler.pkl`
   - Document feature means/stds in `preprocess.yaml`

### Phase 2: Optimization and Validation (Week 2)

4. **Generate quantized variants**
   ```bash
   # FP16 (for GPU)
   python TOOLS/quantize_onnx.py --mode fp16 ...
   
   # INT8 (for edge CPU)
   python TOOLS/quantize_onnx.py --mode int8_dynamic ...
   ```

5. **Validate with golden vectors**
   - Create test dataset (100 samples: normal, ice, edge cases)
   - Run baseline inference to generate expected outputs
   - Save as `tests/golden_inputs.npz` and `tests/golden_outputs.npz`
   - Validate quantized models meet tolerance

6. **Profile on target hardware**
   ```bash
   # On Honeywell HCU-4000 (ARM Cortex-A72)
   python TOOLS/profile_ort.py \
     --model ice_detector_pitot/1.0.0/model.int8.onnx \
     --iterations 1000
   ```
   - Verify latency < 50ms requirement
   - Verify memory < 10MB requirement

### Phase 3: Integration with Flight Software (Week 3-4)

7. **Create Simulink S-Function wrapper**
   - Implement `onnx_ice_detector_sfun.cpp`
   - Link ONNX Runtime library
   - Test in Simulink simulation

8. **Integrate with ATA-22 Auto Flight**
   - Add ice detector block to sensor health monitoring
   - Connect to pitot sensor bus
   - Wire alerts to crew alerting system (CAS)

9. **Hardware-in-the-Loop (HIL) testing**
   - Run on actual flight computer
   - Inject recorded sensor data
   - Verify real-time performance
   - Validate alert triggering

### Phase 4: Certification and Deployment (Week 5-8)

10. **DO-178C compliance artifacts**
    - Software Requirements Specification (SRS)
    - Software Design Description (SDD)
    - Software Verification Plan (SVP)
    - Traceability matrix (requirements → model card → tests)

11. **Update model registry**
    ```yaml
    # REGISTRY/index.yaml
    - model_id: ice_detector_pitot
      versions:
        - semver: 1.0.0
          status: validated  # → deployed
          deployed_to: ["AC001", "AC002", "AC003"]
    ```

12. **CI/CD pipeline setup**
    - Automated validation on model updates
    - Deployment to aircraft via OTA updates
    - A/B testing with shadow deployment
    - Rollback capability

### Phase 5: Monitoring and Retraining (Ongoing)

13. **Drift detection**
    - Monitor Population Stability Index (PSI) daily
    - Alert if PSI > 0.25 for 7 consecutive days

14. **Performance tracking**
    - Track accuracy on recent flight data
    - Retrain if accuracy drops below 90%

15. **Model versioning**
    - Create v1.1.0 with improved accuracy
    - Deploy to subset of aircraft (canary)
    - Promote to production after validation

## Integration Example: End-to-End Flow

```
1. Sensor Data Acquisition
   └─► ATA-34 Pitot-Static System
       └─► ARINC 429 Bus @ 10 Hz
           └─► [airspeed, static_pressure, total_pressure, OAT, ...]

2. Preprocessing (Flight Software)
   └─► Windowing: 50 samples (5 seconds @ 10 Hz)
       └─► Normalization: StandardScaler (artifacts/scaler.pkl)
           └─► Validation: Range check, NaN check, outlier clipping

3. ONNX Inference (ONNX Runtime)
   └─► Model: ice_detector_pitot/1.0.0/model.int8.onnx
       └─► Input: [1, 50] float32 tensor
           └─► Output: anomaly_score (float32)

4. Postprocessing (Flight Software)
   └─► Threshold: anomaly_score > 0.05 → WARNING
       └─► Threshold: anomaly_score > 0.15 → CRITICAL
           └─► Persistence: 3 consecutive violations → Alert

5. Action (Flight Control / Crew Alerting)
   └─► WARNING: Display "PITOT ICE POSSIBLE" to crew
       └─► CRITICAL: Activate pitot heater boost + Display "PITOT ICE DETECTED"
           └─► Log event for maintenance
```

## Questions for Discussion

1. **Hardware Platform**: Confirm target flight computer specs (currently: ARM Cortex-A72)
2. **Update Mechanism**: OTA updates or manual update during maintenance?
3. **Certification Level**: Confirm DO-178C Level D (advisory) is correct
4. **Backup Strategy**: Hardware-based ice detector as fallback?
5. **Testing Scope**: How many aircraft for initial deployment? How long is shadow mode?

## Success Criteria

✅ Model achieves >90% accuracy on test set  
✅ Quantized INT8 model < 2% accuracy degradation vs FP32  
✅ Inference latency < 50ms on target hardware  
✅ Memory footprint < 10MB  
✅ Passes golden vector tests (within tolerance)  
✅ Integrates with Simulink (S-Function compiles and runs)  
✅ HIL testing validates real-time performance  
✅ DO-178C Level D artifacts complete  
✅ Deployment via CI/CD pipeline  
✅ Monitoring and retraining pipeline operational  

## Conclusion

This ONNX model deployment architecture provides:

1. **Complete CI/CD pipeline** for ML models in aviation
2. **Tools and templates** for export, validation, optimization
3. **Example ice detector model** with full package structure
4. **Integration guide** for Simulink/flight software
5. **Clear next steps** for implementation

The architecture bridges the gap between data science (model training) and flight software (real-time inference), while maintaining DO-178C certification compliance.

---

**Status**: ✅ Architecture complete, ready for Phase 1 implementation  
**Next action**: Train ice detector model in ANOMALY_DETECTORS  
**Owner**: AI/ML Team - Sensor Health  
**Timeline**: 8 weeks to production deployment
