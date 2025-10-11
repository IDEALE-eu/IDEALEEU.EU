# Surrogate Model Card: Thermal Avionics Temperature

**Surrogate ID**: `thermal_avionics_temp`  
**Version**: `1.0.0`  
**Date**: 2024-11-20  
**Owner**: Thermal Analysis Team  
**Status**: Production

---

## 1. Model Purpose

### What does this surrogate model predict?

This surrogate model predicts the steady-state temperature of an avionics bay electronic component (IMA module) as a function of ambient temperature, component power dissipation, and cooling airflow rate. It replaces expensive finite element thermal simulations for real-time health monitoring and digital twin applications.

**Use Case**: The model enables continuous thermal health monitoring of avionics systems, predicting component hotspot temperatures in milliseconds rather than hours required by high-fidelity FEM simulations.

### Physical Domain

- **Domain**: Thermal
- **ATA Chapter**: ATA-31 - Indicating/Recording Systems
- **Subsystem**: Integrated Modular Avionics (IMA)

### Intended Use

- **Primary Use Case**: Real-time thermal health monitoring of avionics bay components
- **Operational Context**: Integrated into aircraft digital twin for continuous temperature prediction
- **Users**: 
  - Health monitoring system (automatic alerts)
  - Maintenance planning system (predictive maintenance)
  - Flight operations (thermal management)

---

## 2. Scope and Limitations

### In Scope

- Steady-state temperature prediction for standard IMA modules
- Ambient temperature range: -20°C to 70°C
- Power dissipation range: 5W to 120W
- Airflow range: 0.5 to 8.0 m³/min
- Natural and forced convection cooling

### Out of Scope

- Transient thermal response (heating/cooling time constants)
- Non-standard component geometries or materials
- Radiation-dominated heat transfer scenarios
- Multiple interacting heat sources
- Extreme conditions outside training envelope

### Known Limitations

1. **Steady-State Only**: Model does not capture transient thermal dynamics. Time to reach steady state is not predicted.
2. **Component-Specific**: Trained for standard IMA module thermal properties. Accuracy may degrade for different component types.
3. **Low Airflow Accuracy**: Slight underestimation (2-5°C) at very low airflow rates (<1 m³/min) due to neglected radiation effects.
4. **Material Properties**: Assumes constant thermal properties. Accuracy may degrade at temperature extremes where material properties vary significantly.

---

## 3. Model Details

### Algorithm

- **Type**: Gaussian Process Regression
- **Framework**: scikit-learn 1.2.0
- **Kernel**: Matérn (ν=1.5)

### Input-Output Specification

**Inputs** (N = 3):
| Name | Description | Unit | Range | Type |
|------|-------------|------|-------|------|
| `T_ambient` | Ambient temperature in avionics bay | °C | [-20, 70] | float |
| `P_load` | Electrical power dissipated by component | W | [5, 120] | float |
| `airflow` | Cooling air flow rate | m³/min | [0.5, 8.0] | float |

**Outputs** (M = 1):
| Name | Description | Unit | Expected Range | Type |
|------|-------------|------|----------------|------|
| `T_component` | Steady-state component temperature | °C | [-30, 150] | float |

### Reference Frame

- **Inputs**: Scalar quantities, no coordinate frame
- **Outputs**: Temperature at component hotspot (estimated junction temperature)

---

## 4. Training Data

### High-Fidelity Source

- **Source Model**: ANSYS Mechanical - Thermal Steady State Analysis
- **Fidelity Level**: Finite Element Method with 250,000+ elements
- **Computational Cost**: ~30 minutes per simulation on 8-core workstation

**Physics**: 3D conduction, natural and forced convection boundary conditions, temperature-dependent material properties.

### Design of Experiments (DOE)

- **DOE Type**: Latin Hypercube Sampling
- **Training Samples**: 2,000 simulations
- **Validation Samples**: 500 simulations
- **Test Samples**: 10 physical bench tests
- **Coverage**: 95% of operational envelope

### Data Characteristics

- **Training Period**: September-November 2024
- **Data Hash**: `3f7a9b2c1d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a`
- **Data Location**: `/data/thermal_fem_simulations/training_set_v1.npz`

---

## 5. Performance Metrics

### Accuracy

| Metric | Training | Validation | Test (FEM) | Physical Test | Target |
|--------|----------|------------|------------|---------------|--------|
| RMSE (°C) | 1.8 | 2.1 | 2.3 | 2.8 | ≤ 3.0 |
| MAE (°C) | 1.4 | 1.6 | 1.8 | 2.1 | ≤ 2.5 |
| R² | 0.987 | 0.982 | 0.978 | 0.971 | ≥ 0.95 |
| Max Error (°C) | 6.2 | 7.8 | 8.5 | 9.2 | ≤ 10.0 |
| p95 Error (°C) | 3.8 | 4.2 | 4.6 | 5.1 | ≤ 6.0 |

**Note**: Physical test data shows slightly higher errors due to measurement uncertainty and real-world variability not captured in simulations.

### Speedup Factor

- **FEM Evaluation Time**: ~30 minutes (1,800 seconds)
- **Surrogate Evaluation Time**: ~3.5 ms
- **Speedup**: ~514,000×

### Inference Performance

- **Mean Latency**: 3.5 ms
- **p95 Latency**: 5.2 ms
- **p99 Latency**: 6.8 ms
- **Throughput**: ~280 queries/second (single core)
- **Memory Footprint**: 1.2 MB (model) + 50 MB (runtime)

---

## 6. Uncertainty Quantification

### Method

- **UQ Method**: Gaussian Process Posterior Variance
- **Confidence Level**: 95%

### Calibration

- **Expected Coverage**: 95%
- **Measured Coverage**: 94% (well-calibrated)
- **Calibration Quality**: Well-calibrated (coverage within 1% of target)

### Out-of-Domain (OOD) Detection

- **OOD Policy**: Flag + Extrapolate with increased uncertainty
- **Warning Margin**: 5% from domain boundary
- **Confidence Degradation**: Exponential decay with extrapolation distance

**Example**: Query at `P_load=130W` (outside training range of 5-120W) triggers warning and increases uncertainty by factor of 2.0.

---

## 7. Validation and Verification

### Validation Against High-Fidelity

- **Validation Date**: 2024-11-18
- **Validation Report**: `validation/validation_report.json`
- **Test Points**: 500 FEM simulations + 10 physical tests
- **Pass Criteria**: RMSE < 3.0°C on independent test set
- **Status**: ✅ Passed (RMSE = 2.1°C)

### Monotonicity and Physics Constraints

- **Constraints Checked**:
  - ✅ `T_component ≥ T_ambient` (component always warmer than ambient)
  - ✅ `∂T_component/∂P_load > 0` (temperature increases with power)
  - ✅ `∂T_component/∂airflow < 0` (temperature decreases with airflow)
  - ✅ `∂T_component/∂T_ambient > 0` (temperature increases with ambient)

### Golden Test Set

- **Golden Test Cases**: 50 reference scenarios
- **Location**: `tests/golden.npz`
- **All Tests Pass**: ✅ Yes (max deviation: 0.002°C)

---

## 8. Domain of Validity

### Valid Input Ranges

| Input | Physical Range | Training Range | Recommended Range |
|-------|----------------|----------------|-------------------|
| `T_ambient` | [-40°C, 85°C] | [-20°C, 70°C] | [-15°C, 65°C] |
| `P_load` | [0W, 150W] | [5W, 120W] | [10W, 110W] |
| `airflow` | [0, 10 m³/min] | [0.5, 8.0 m³/min] | [0.8, 7.5 m³/min] |

**Recommended Range**: Training range with 5% safety margin removed from boundaries.

### Combined Constraints

- **High Power Cooling**: For `P_load > 100W`, ensure `airflow ≥ 2.0 m³/min`
- **Thermal Runaway Prevention**: Avoid `T_ambient > 60°C` AND `P_load > 80W` AND `airflow < 3.0 m³/min`

### Extrapolation Warnings

- **Beyond Training Range**: Predictions flagged with warning
- **Confidence Penalty**: Uncertainty increases exponentially beyond training envelope
- **Max Extrapolation**: 10% beyond training range (hard limit)

---

## 9. Integration and Usage

### Runtime API

```python
# Python example
from runtime.python.evaluate import predict

inputs = {
    'T_ambient': 35.0,  # °C
    'P_load': 65.0,     # W
    'airflow': 3.5      # m³/min
}

outputs = predict(inputs)
# Returns: {'T_component': 68.2, 'uncertainty_95': 2.1}
```

### FMU Export

- **FMU Available**: ✅ Yes
- **FMI Version**: 2.0
- **Location**: `runtime/fmu/thermal_avionics_temp.fmu`

**Usage in Co-Simulation**:
```python
# Load FMU in simulation environment
fmu = load_fmu("thermal_avionics_temp.fmu")
fmu.set_real([T_ambient, P_load, airflow], [35.0, 65.0, 3.5])
fmu.do_step(current_time, dt)
T_component = fmu.get_real([output_index])
```

### Co-Simulation

- **Integration Points**: 
  - Avionics thermal management system
  - Health monitoring dashboard
  - Predictive maintenance scheduler
- **Calling Frequency**: Every simulation time step (typically 1-10 Hz)
- **Dependencies**: Requires ambient temperature sensor, power monitor, airflow sensor

---

## 10. Risks and Mitigations

### Risk 1: Extrapolation Beyond Training Domain

- **Description**: User queries outside [-20°C, 70°C] ambient temperature range
- **Likelihood**: Medium (operational envelope occasionally exceeds during ground ops)
- **Impact**: High (incorrect predictions could affect safety)
- **Mitigation**: 
  - OOD detection enabled (warning at 5% margin)
  - Uncertainty increases exponentially outside domain
  - Hard limit at 10% extrapolation
  - Logging of all OOD queries for monitoring

### Risk 2: Component Degradation Over Time

- **Description**: Thermal interface material degradation increases thermal resistance
- **Likelihood**: Low (short-term), Medium (long-term >5 years)
- **Impact**: Medium (gradual accuracy degradation)
- **Mitigation**:
  - Periodic validation against in-service temperature measurements
  - Model retraining recommended every 2 years
  - Drift detection monitors prediction errors

### Risk 3: Model Does Not Capture Transients

- **Description**: Users expect transient thermal response, model only predicts steady-state
- **Likelihood**: Medium (users may not read documentation)
- **Impact**: Low (predictions still valid, just not time-dependent)
- **Mitigation**:
  - Clear documentation in model card
  - API returns warning if used in transient context
  - Complementary dynamic thermal model available for transients

---

## 11. Maintenance and Updates

### Retraining Policy

- **Retraining Trigger**: 
  - Validation error exceeds 4.5°C (1.5× target)
  - Physical test errors consistently >5°C
  - Component specification changes
- **Retraining Frequency**: Every 2 years (scheduled) or event-triggered
- **Data Refresh**: Incorporate new FEM simulations and physical test data

### Monitoring

- **Metrics Tracked**: RMSE, MAE, OOD rate, uncertainty calibration
- **Monitoring Frequency**: Daily aggregate statistics
- **Alert Thresholds**: 
  - RMSE > 4.5°C
  - OOD rate > 10%
  - Calibration drift > 5%

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2024-11-20 | Initial production version | Thermal Analysis Team |

---

## 12. Compliance and Traceability

### Requirements Traceability

- **Linked Requirements**: REQ-THM-001, REQ-THM-015, REQ-DT-042
- **Verification Tests**: TEST-THM-VAL-001, TEST-THM-VAL-002

### Certification

- **Certification Level**: DO-178C Level D (non-safety-critical)
- **Safety Case**: Model used for monitoring only, not flight-critical control

### Approval

- **Reviewed By**: Dr. Maria Santos, Thermal Systems Lead
- **Approved By**: Dr. Maria Santos
- **Approval Date**: 2024-11-20
- **Configuration Control**: CCB-2024-THM-011

---

## 13. Attachments and References

### Documentation

- **Training Report**: `training/training_report.pdf`
- **Validation Report**: `validation/validation_report.json`
- **I/O Contract**: `io_contract.yaml`
- **Training Config**: `train_config.yaml`
- **Domain of Validity**: `domain_of_validity.yaml`

### Artifacts

- **Model File**: `model.joblib`
- **Training Data**: `training/X_train.npz`, `training/y_train.npz`
- **Validation Data**: `validation/X_val.npz`, `validation/y_val.npz`
- **Diagnostics**: `validation/diagnostics/`

### External References

- ANSYS Mechanical Thermal Analysis User Manual
- IMA Module Thermal Design Guidelines (ARINC 664)
- Bench Test Report: BTR-THM-2024-11-15

---

## 14. Contact Information

**Model Owner**: Thermal Analysis Team  
**Email**: thermal-analysis@ideale-eu.eu  
**Team Lead**: Dr. Maria Santos  
**Support**: Slack: #thermal-systems

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`

**Last Updated**: 2024-11-20
