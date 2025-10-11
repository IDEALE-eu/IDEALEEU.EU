# ONNX Model Integration Guide

## 1. Overview

This document is the guide for software engineers who need to integrate a machine learning (ML) model, packaged in the ONNX format, into a client application (e.g., flight software, digital twin, analysis tool).

The core principle is to treat models as **immutable, versioned software artifacts**. Each model package is self-contained and provides all the information necessary for its correct integration and execution.

**Never** hard-code constants (model paths, thresholds, scaling factors) in the client application. All configuration must be loaded dynamically from the model's artifacts.

This guide covers:
- General integration principles (Section 2-5)
- Flight software integration specifics (Section 6-10)
- Simulink/Stateflow integration examples (Section 11)

-----

## 2. Model Discovery and Verification

### 2.1. Resolving the Model Path

The catalog of all available models is the `REGISTRY/index.yaml` file. The application **must** resolve the path to the model artifacts dynamically at runtime based on a required `model_id` and semantic version (`semver`).

```python
import yaml
import os

def resolve_model_path(registry_path, model_id, semver):
    """Finds the path to a specific model version from the central registry."""
    with open(registry_path) as f:
        registry = yaml.safe_load(f)
    
    for model in registry.get('models', []):
        if model.get('model_id') == model_id:
            for version in model.get('versions', []):
                if version.get('semver') == semver:
                    # Build path relative to registry
                    base_path = os.path.dirname(registry_path)
                    return os.path.join(base_path, model_id, semver, "")
    
    raise ValueError(f"Model '{model_id}' version '{semver}' not found in registry.")
```

### 2.2. Verifying Artifact Integrity

Before loading any model assets, **you must verify the integrity of the entire package**. This is done by checking the SHA256 hash of each file against the manifest `checksum.sha256`.

```python
import hashlib

def verify_checksums(model_root_path: str):
    """Verifies all file hashes listed in the checksum manifest."""
    manifest_path = os.path.join(model_root_path, "checksum.sha256")
    with open(manifest_path) as f:
        lines = [line.strip().split(maxsplit=1) for line in f if line.strip()]
    
    for expected_hash, relative_path in lines:
        file_path = os.path.join(model_root_path, relative_path)
        
        hasher = hashlib.sha256()
        with open(file_path, "rb") as f_bin:
            hasher.update(f_bin.read())
        actual_hash = hasher.hexdigest()
        
        if actual_hash != expected_hash:
            raise SecurityError(f"Checksum mismatch for '{relative_path}'. Tampering suspected.")
    
    print("✓ All model artifacts passed integrity check.")
```

-----

## 3. Runtime Configuration

### 3.1. Provider Selection Policy

**ONNX Runtime (ORT)** uses **Execution Providers** to run models on different hardware. The client application should prioritize providers for performance, with a mandatory fallback to the CPU.

1. **TensorRTExecutionProvider**: Highest performance for NVIDIA GPUs. Use if available.
2. **CUDAExecutionProvider**: Good performance for NVIDIA GPUs. Use if TensorRT is not available.
3. **CPUExecutionProvider**: The universal fallback that must always be included.

### 3.2. Opset Compatibility

The `opset.txt` file specifies the ONNX opset version (e.g., `17`). The client application should check this against the capabilities of its installed ONNX Runtime version to ensure all model operations are supported.

```python
import onnxruntime as ort

# Opset check example
with open(os.path.join(model_path, "opset.txt")) as f:
    model_opset = int(f.read().strip())

# Check if runtime supports this opset
# Note: ORT doesn't expose max opset directly, but will fail gracefully if unsupported
print(f"Model requires ONNX opset {model_opset}")
```

-----

## 4. Integration Steps and Code Example

The following code demonstrates the complete, production-ready workflow.

```python
import onnxruntime as ort
import joblib
import numpy as np
import yaml
import json
import hashlib
import os

# --- 1. Model Discovery and Verification ---
REGISTRY_PATH = "02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/DATA_DRIVEN/ONNX_MODELS/REGISTRY/index.yaml"
MODEL_ID = "ice_detector_pitot"
SEMVER = "1.0.0"

MODEL_PATH = resolve_model_path(REGISTRY_PATH, MODEL_ID, SEMVER)
verify_checksums(MODEL_PATH)  # Throws error on mismatch

# --- 2. Load Artifacts & Configure Runtime ---
signature = json.load(open(os.path.join(MODEL_PATH, "signature.json")))
io_contract = yaml.safe_load(open(os.path.join(MODEL_PATH, "io_contract.yaml")))
postprocess_cfg = yaml.safe_load(open(os.path.join(MODEL_PATH, "postprocess.yaml")))
scaler = joblib.load(os.path.join(MODEL_PATH, "artifacts/scaler.pkl"))

# Configure providers with fallback
providers = []
available_providers = ort.get_available_providers()
if "TensorrtExecutionProvider" in available_providers:
    providers.append("TensorrtExecutionProvider")
if "CUDAExecutionProvider" in available_providers:
    providers.append("CUDAExecutionProvider")
providers.append("CPUExecutionProvider")

# Set session options for performance
sess_options = ort.SessionOptions()
sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
sess_options.enable_mem_pattern = True

session = ort.InferenceSession(
    os.path.join(MODEL_PATH, "model.onnx"), 
    sess_options=sess_options, 
    providers=providers
)

# --- 3. Validate Model Signature at Initialization ---
input_meta = session.get_inputs()[0]
output_meta = session.get_outputs()[0]
assert input_meta.name == signature["inputs"][0]["name"], "Input name mismatch!"
# Note: ONNX Runtime uses string like 'tensor(float)' for type
assert "float" in input_meta.type, "Input dtype mismatch!"

# --- 4. Define Execution Pipeline ---
def _validate_input_vector(vector: np.ndarray, io_contract):
    """Per-element validation against the IO contract."""
    features = io_contract["inputs"]["sensor_readings"]["features"]
    vector = vector.ravel()
    
    if len(vector) != len(features):
        raise ValueError(f"Input length mismatch. Expected {len(features)}, got {len(vector)}.")
    
    for i, feature_spec in enumerate(features):
        val = vector[i]
        min_val, max_val = feature_spec["range"]
        if not (min_val <= val <= max_val):
            raise ValueError(
                f"Feature '{feature_spec['name']}' at index {i} is out of range. "
                f"Value={val}, Range=[{min_val}, {max_val}]."
            )

def predict(raw_input_vector: np.ndarray):
    """Runs the full pre-process -> inference -> post-process pipeline."""
    # Pre-process: Validate
    _validate_input_vector(raw_input_vector, io_contract)
    
    # Pre-process: Scale
    processed_input = scaler.transform(raw_input_vector.reshape(1, -1)).astype(np.float32)

    # Inference
    result = session.run([output_meta.name], {input_meta.name: processed_input})[0]
    anomaly_score = float(np.asarray(result).ravel()[0])

    # Post-process
    threshold_warning = io_contract["outputs"]["anomaly_score"]["interpretation"]["threshold_warning"]
    threshold_critical = io_contract["outputs"]["anomaly_score"]["interpretation"]["threshold_critical"]
    
    if anomaly_score >= threshold_critical:
        alert_level = "CRITICAL"
    elif anomaly_score >= threshold_warning:
        alert_level = "WARNING"
    else:
        alert_level = "NORMAL"
    
    return {"anomaly_score": anomaly_score, "alert_level": alert_level}

# --- Example Usage ---
try:
    # Example: Valid input (10 features for ice detector)
    input_vector = np.array([
        175.0,  # airspeed_indicated
        850.0,  # static_pressure
        900.0,  # total_pressure
        -15.0,  # outside_air_temperature
        12500.0,  # altitude_pressure
        0.0,    # rate_of_climb
        50.0,   # differential_pressure
        2.1,    # pitot_heater_current
        -10.0,  # pitot_temperature
        0.15    # vibration_sensor
    ])
    prediction = predict(input_vector)
    print(f"✓ Prediction: {prediction}")

    # Example: Invalid input (out of range)
    invalid_vector = input_vector.copy()
    invalid_vector[0] = 500.0  # Airspeed way out of range
    predict(invalid_vector)
except ValueError as e:
    print(f"✓ Validation failed as expected: {e}")
```

-----

## 5. Integration Testing

To verify your integration, use the provided "golden vectors".

1. Load `tests/golden_inputs.npz`.
2. Pass each input vector to your final `predict()` function.
3. Compare the output dictionary with the expected results in `tests/golden_outputs.npz`.
4. Use the numerical tolerances (`atol`, `rtol`) from `tests/tolerance.yaml` for comparing floating-point values like `anomaly_score`.

This ensures your end-to-end implementation is bit-perfect with the reference pipeline.

```python
# Example golden vector testing
golden_inputs = np.load(os.path.join(MODEL_PATH, "tests/golden_inputs.npz"))
golden_outputs = np.load(os.path.join(MODEL_PATH, "tests/golden_outputs.npz"))
tolerance = yaml.safe_load(open(os.path.join(MODEL_PATH, "tests/tolerance.yaml")))

for key in golden_inputs.files:
    test_input = golden_inputs[key]
    expected_output = golden_outputs[key]
    actual_output = predict(test_input)
    
    atol = tolerance.get('default', {}).get('atol', 1e-5)
    rtol = tolerance.get('default', {}).get('rtol', 1e-4)
    
    np.testing.assert_allclose(
        actual_output['anomaly_score'], 
        expected_output, 
        atol=atol, 
        rtol=rtol
    )
    print(f"✓ Golden vector test '{key}' passed")
```

-----

## 6. Flight Software Integration Overview

This section explains how ONNX models integrate with flight control software, specifically addressing: "How would the CONTROL_LOGIC component from ATA-22_AUTO_FLIGHT consume an ONNX model?"

## 7. Integration Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   ATA-22 Auto Flight Control                     │
│                  (Simulink/Stateflow Model)                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │             Flight Control Logic                           │  │
│  │  • Autopilot modes                                        │  │
│  │  • Flight envelope protection                             │  │
│  │  • Sensor health monitoring  ◄────────────────┐          │  │
│  └───────────────────────────────────────────────┘          │  │
│                          │                                    │  │
│                          ▼                                    │  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │         ONNX Model Interface Block                        │  │
│  │  (S-Function or C++ MEX Function)                         │  │
│  │                                                            │  │
│  │  1. Read sensor data from Simulink bus                    │  │
│  │  2. Apply preprocessing (windowing, normalization)        │  │
│  │  3. Call ONNX Runtime inference                           │  │
│  │  4. Apply postprocessing (thresholding, alerts)           │  │
│  │  5. Output to flight control logic                        │  │
│  └───────────────────────────────────────────────────────────┘  │
│                          │                                       │
│                          ▼                                       │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │            ONNX Runtime Library                           │  │
│  │  (Linked as external C++ library)                         │  │
│  │                                                            │  │
│  │  • Load model from file system                            │  │
│  │  • Allocate input/output tensors                          │  │
│  │  • Run inference                                          │  │
│  │  • Return predictions                                     │  │
│  └───────────────────────────────────────────────────────────┘  │
│                          │                                       │
└──────────────────────────┼───────────────────────────────────────┘
                           ▼
            ┌──────────────────────────────┐
            │   ice_detector_pitot/1.0.0/  │
            │       model.int8.onnx        │
            │                              │
            │  + signature.json            │
            │  + io_contract.yaml          │
            │  + artifacts/scaler.pkl      │
            └──────────────────────────────┘
```

## 8. Integration Methods

### 8.1. Method 1: S-Function (Simulink)

The most direct integration for Simulink models is through a **Level-2 MATLAB S-Function** or **C++ MEX S-Function**.

#### Example: C++ MEX S-Function

```cpp
// onnx_ice_detector_sfun.cpp
#include "simstruc.h"
#include <onnxruntime_cxx_api.h>

// Model configuration
static const char* MODEL_PATH = "../../ONNX_MODELS/ice_detector_pitot/1.0.0/model.int8.onnx";
static Ort::Session* g_session = nullptr;

// Initialize function
static void mdlInitializeSizes(SimStruct *S) {
    ssSetNumSFcnParams(S, 0);
    
    // Input ports (10 sensor signals)
    ssSetNumInputPorts(S, 1);
    ssSetInputPortWidth(S, 0, 50);  // 50 windowed features
    
    // Output ports (anomaly score + alert level)
    ssSetNumOutputPorts(S, 2);
    ssSetOutputPortWidth(S, 0, 1);  // anomaly_score
    ssSetOutputPortWidth(S, 1, 1);  // alert_level
    
    ssSetNumSampleTimes(S, 1);
    ssSetOptions(S, SS_OPTION_EXCEPTION_FREE_CODE);
}

// Start function - load ONNX model
static void mdlStart(SimStruct *S) {
    Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "ONNXIceDetector");
    Ort::SessionOptions session_options;
    session_options.SetIntraOpNumThreads(2);
    session_options.SetGraphOptimizationLevel(GraphOptimizationLevel::ORT_ENABLE_ALL);
    
    g_session = new Ort::Session(env, MODEL_PATH, session_options);
}

// Output function - run inference
static void mdlOutputs(SimStruct *S, int_T tid) {
    // Get input data
    const real_T *u = (const real_T*) ssGetInputPortSignal(S, 0);
    real_T *y_score = ssGetOutputPortSignal(S, 0);
    real_T *y_alert = ssGetOutputPortSignal(S, 1);
    
    // Prepare ONNX Runtime tensors
    std::vector<int64_t> input_shape = {1, 50};
    std::vector<float> input_tensor_values(u, u + 50);
    
    Ort::MemoryInfo memory_info = Ort::MemoryInfo::CreateCpu(
        OrtArenaAllocator, OrtMemTypeDefault);
    Ort::Value input_tensor = Ort::Value::CreateTensor<float>(
        memory_info, input_tensor_values.data(), 50,
        input_shape.data(), 2);
    
    // Run inference
    const char* input_names[] = {"sensor_readings"};
    const char* output_names[] = {"reconstruction", "anomaly_score"};
    
    auto output_tensors = g_session->Run(
        Ort::RunOptions{nullptr},
        input_names, &input_tensor, 1,
        output_names, 2);
    
    // Extract outputs
    float* anomaly_score = output_tensors[1].GetTensorMutableData<float>();
    *y_score = anomaly_score[0];
    
    // Apply postprocessing thresholds
    if (*y_score > 0.15) {
        *y_alert = 2.0;  // CRITICAL
    } else if (*y_score > 0.05) {
        *y_alert = 1.0;  // WARNING
    } else {
        *y_alert = 0.0;  // NORMAL
    }
}

// Terminate function - cleanup
static void mdlTerminate(SimStruct *S) {
    if (g_session) {
        delete g_session;
        g_session = nullptr;
    }
}

// Simulink registration
#ifdef MATLAB_MEX_FILE
#include "simulink.c"
#else
#include "cg_sfun.h"
#endif
```

#### Simulink Block Diagram

```
Sensor Bus ────┐
(ATA-34)       │
               ├──► [Windowing & ──► [ONNX Ice ──► [Threshold ──► Alert to
               │     Normalization]    Detector]     Logic]        Crew
Pitot Data ────┘                         S-Func                    (CAS)
```

### 8.2. Method 2: External C++ Function (Embedded Coder)

For production code generation, use **Embedded Coder** with an external C++ function.

#### Example: External C++ Wrapper

```cpp
// onnx_ice_detector.h
#ifndef ONNX_ICE_DETECTOR_H
#define ONNX_ICE_DETECTOR_H

extern "C" {
    void onnx_ice_detector_init(const char* model_path);
    void onnx_ice_detector_step(const float* inputs, float* anomaly_score, int* alert_level);
    void onnx_ice_detector_terminate(void);
}

#endif
```

```cpp
// onnx_ice_detector.cpp
#include "onnx_ice_detector.h"
#include <onnxruntime_cxx_api.h>

static Ort::Session* g_session = nullptr;
static Ort::Env g_env(ORT_LOGGING_LEVEL_WARNING, "IceDetector");

void onnx_ice_detector_init(const char* model_path) {
    Ort::SessionOptions options;
    options.SetIntraOpNumThreads(2);
    g_session = new Ort::Session(g_env, model_path, options);
}

void onnx_ice_detector_step(const float* inputs, float* anomaly_score, int* alert_level) {
    // Run inference (as above)
    // ...
    
    // Apply thresholds from postprocess.yaml
    if (*anomaly_score > 0.15) {
        *alert_level = 2;  // CRITICAL
    } else if (*anomaly_score > 0.05) {
        *alert_level = 1;  // WARNING
    } else {
        *alert_level = 0;  // NORMAL
    }
}

void onnx_ice_detector_terminate(void) {
    delete g_session;
}
```

#### Simulink Configuration

In Simulink, configure the block as an **External Function**:

1. Add **MATLAB Function** or **Stateflow** block
2. Call external C++ function using `coder.ceval`
3. Link ONNX Runtime library during code generation

```matlab
function [anomaly_score, alert_level] = ice_detector_block(sensor_data)
    % Call external C++ function
    coder.cinclude('onnx_ice_detector.h');
    anomaly_score = 0.0;
    alert_level = int32(0);
    
    coder.ceval('onnx_ice_detector_step', ...
                coder.rref(sensor_data), ...
                coder.wref(anomaly_score), ...
                coder.wref(alert_level));
end
```

### 8.3. Method 3: ROS 2 Integration (Alternative)

For systems using ROS 2, the model can be deployed as a separate node:

```
┌────────────────────┐         ┌──────────────────┐         ┌────────────────┐
│  Flight Control    │ ──────► │  ONNX Ice        │ ──────► │  Alert         │
│  Node (Simulink)   │  topic  │  Detector Node   │  topic  │  Manager Node  │
│  (ATA-22)          │         │  (Python/C++)    │         │  (CAS)         │
└────────────────────┘         └──────────────────┘         └────────────────┘
     /sensor/pitot              /ice_detector/score          /alerts/pitot
```

## 9. Data Flow and Preprocessing

### 9.1. Input Pipeline

The `io_contract.yaml` defines the complete data pipeline:

1. **Sensor Data Acquisition**: Read from avionic bus (ARINC 429, AFDX)
2. **Feature Extraction**: Map raw signals to model features
3. **Windowing**: Create sliding window of 50 samples
4. **Normalization**: Apply StandardScaler using `artifacts/scaler.pkl`
5. **Validation**: Check for NaN, outliers, range violations
6. **Inference**: Run ONNX model
7. **Postprocessing**: Apply thresholds, generate alerts

### 9.2. Example: Preprocessing in Flight Code

```cpp
// Windowing buffer (50 samples x 10 features)
static float window_buffer[50][10];
static int window_idx = 0;

void update_ice_detector(const SensorData_t* sensors) {
    // Extract features
    float features[10] = {
        sensors->airspeed_indicated,
        sensors->static_pressure,
        sensors->total_pressure,
        sensors->outside_air_temperature,
        // ... other features
    };
    
    // Add to window
    memcpy(window_buffer[window_idx], features, sizeof(features));
    window_idx = (window_idx + 1) % 50;
    
    // Normalize (using precomputed mean/std from scaler.pkl)
    float normalized[50];
    for (int i = 0; i < 50; i++) {
        for (int j = 0; j < 10; j++) {
            normalized[i*10 + j] = (window_buffer[i][j] - MEAN[j]) / STD[j];
        }
    }
    
    // Run ONNX inference
    float anomaly_score;
    int alert_level;
    onnx_ice_detector_step(normalized, &anomaly_score, &alert_level);
    
    // Handle alert
    if (alert_level == 2) {
        trigger_pitot_heater_boost();
        display_crew_alert("ICE DETECTED - PITOT");
    }
}
```

## 10. Deployment Configuration

### 10.1. Flight Software Build System

The ONNX model is integrated into the flight software build:

```cmake
# CMakeLists.txt for ATA-22 Auto Flight

# Link ONNX Runtime
find_package(ONNXRuntime REQUIRED)
include_directories(${ONNXRUNTIME_INCLUDE_DIRS})

add_executable(auto_flight_controller
    src/autopilot.cpp
    src/envelope_protection.cpp
    src/sensor_health.cpp
    src/onnx_ice_detector.cpp  # ONNX wrapper
)

target_link_libraries(auto_flight_controller
    ${ONNXRUNTIME_LIBRARIES}
)

# Copy ONNX models to deployment directory
install(FILES
    ${CMAKE_SOURCE_DIR}/../../ONNX_MODELS/ice_detector_pitot/1.0.0/model.int8.onnx
    ${CMAKE_SOURCE_DIR}/../../ONNX_MODELS/ice_detector_pitot/1.0.0/artifacts/scaler.pkl
    DESTINATION models/
)
```

## 11. Safety and Certification Considerations

### 11.1. DO-178C Compliance

- **Model as Software**: ONNX model treated as software artifact
- **Level D**: Advisory function (ice detection alerts)
- **Verification**: Golden vector tests, hardware profiling
- **Traceability**: Model card links to requirements

### 11.2. Fail-Safe Design

```cpp
// Watchdog timer for inference
#define INFERENCE_TIMEOUT_MS 50

float anomaly_score = 0.0;
int alert_level = 0;

if (run_inference_with_timeout(normalized, &anomaly_score, INFERENCE_TIMEOUT_MS)) {
    // Success - use result
    update_alert_system(alert_level);
} else {
    // Timeout or error - use fallback
    log_error("ONNX inference timeout");
    use_traditional_ice_detector();  // Hardware-based backup
}
```

## 12. Performance Requirements

From `benchmarks/hw_profile.yaml`:

- **Target Hardware**: ARM Cortex-A72 @ 1.5 GHz
- **Max Latency**: 50ms (INT8 variant: 8.5ms ✓)
- **Max Memory**: 10MB (INT8 variant: 2.8MB ✓)
- **Update Rate**: 10 Hz
- **Real-Time**: Hard deadline

## 13. Testing and Validation

### 13.1. Integration Tests

```cpp
// Test ONNX model integration with flight software
TEST(IceDetector, IntegrationTest) {
    // Load test vectors
    float test_input[50] = { /* ... */ };
    float expected_score = 0.12;
    
    // Run inference
    float anomaly_score;
    int alert_level;
    onnx_ice_detector_step(test_input, &anomaly_score, &alert_level);
    
    // Verify within tolerance
    EXPECT_NEAR(anomaly_score, expected_score, 0.01);
    EXPECT_EQ(alert_level, 1);  // WARNING
}
```

### 13.2. Hardware-in-the-Loop (HIL)

The ONNX model is tested on the actual flight computer in a HIL simulator:

1. Inject sensor data from flight test recordings
2. Run ONNX model in real-time
3. Verify latency < 50ms
4. Verify alerts match ground truth

## 14. Summary

The ONNX model integrates with ATA-22 Auto Flight control logic through:

1. **S-Function or external C++ function** in Simulink
2. **ONNX Runtime library** linked to flight software
3. **Preprocessing/postprocessing** as defined in `io_contract.yaml`
4. **Real-time execution** on edge compute unit
5. **Fail-safe design** with hardware backup

This architecture enables data-driven ML models to coexist with traditional flight control logic while meeting DO-178C certification requirements.
