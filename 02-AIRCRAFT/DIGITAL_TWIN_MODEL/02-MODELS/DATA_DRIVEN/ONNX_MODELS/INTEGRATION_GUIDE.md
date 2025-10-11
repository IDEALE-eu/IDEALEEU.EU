# ONNX Model Integration with Flight Software

This document explains how ONNX models from this directory integrate with flight control software, specifically addressing the question from the architecture proposal: "How would the CONTROL_LOGIC component from ATA-22_AUTO_FLIGHT consume an ONNX model?"

## Integration Architecture

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

## Integration Methods

### Method 1: S-Function (Simulink)

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

### Method 2: External C++ Function (Embedded Coder)

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

### Method 3: ROS 2 Integration (Alternative)

For systems using ROS 2, the model can be deployed as a separate node:

```
┌────────────────────┐         ┌──────────────────┐         ┌────────────────┐
│  Flight Control    │ ──────► │  ONNX Ice        │ ──────► │  Alert         │
│  Node (Simulink)   │  topic  │  Detector Node   │  topic  │  Manager Node  │
│  (ATA-22)          │         │  (Python/C++)    │         │  (CAS)         │
└────────────────────┘         └──────────────────┘         └────────────────┘
     /sensor/pitot              /ice_detector/score          /alerts/pitot
```

## Data Flow and Preprocessing

### Input Pipeline

The `io_contract.yaml` defines the complete data pipeline:

1. **Sensor Data Acquisition**: Read from avionic bus (ARINC 429, AFDX)
2. **Feature Extraction**: Map raw signals to model features
3. **Windowing**: Create sliding window of 50 samples
4. **Normalization**: Apply StandardScaler using `artifacts/scaler.pkl`
5. **Validation**: Check for NaN, outliers, range violations
6. **Inference**: Run ONNX model
7. **Postprocessing**: Apply thresholds, generate alerts

### Example: Preprocessing in Flight Code

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

## Deployment Configuration

### Flight Software Build System

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

## Safety and Certification Considerations

### DO-178C Compliance

- **Model as Software**: ONNX model treated as software artifact
- **Level D**: Advisory function (ice detection alerts)
- **Verification**: Golden vector tests, hardware profiling
- **Traceability**: Model card links to requirements

### Fail-Safe Design

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

## Performance Requirements

From `benchmarks/hw_profile.yaml`:

- **Target Hardware**: ARM Cortex-A72 @ 1.5 GHz
- **Max Latency**: 50ms (INT8 variant: 8.5ms ✓)
- **Max Memory**: 10MB (INT8 variant: 2.8MB ✓)
- **Update Rate**: 10 Hz
- **Real-Time**: Hard deadline

## Testing and Validation

### Integration Tests

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

### Hardware-in-the-Loop (HIL)

The ONNX model is tested on the actual flight computer in a HIL simulator:

1. Inject sensor data from flight test recordings
2. Run ONNX model in real-time
3. Verify latency < 50ms
4. Verify alerts match ground truth

## Summary

The ONNX model integrates with ATA-22 Auto Flight control logic through:

1. **S-Function or external C++ function** in Simulink
2. **ONNX Runtime library** linked to flight software
3. **Preprocessing/postprocessing** as defined in `io_contract.yaml`
4. **Real-time execution** on edge compute unit
5. **Fail-safe design** with hardware backup

This architecture enables data-driven ML models to coexist with traditional flight control logic while meeting DO-178C certification requirements.
