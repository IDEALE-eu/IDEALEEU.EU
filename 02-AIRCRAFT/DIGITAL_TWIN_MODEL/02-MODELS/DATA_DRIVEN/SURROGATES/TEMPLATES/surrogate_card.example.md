# Surrogate Model Card Template

**Surrogate ID**: `<sur_id>`  
**Version**: `<semver>`  
**Date**: YYYY-MM-DD  
**Owner**: [Team/Lead Name]  
**Status**: [Development | Validated | Production | Deprecated]

---

## 1. Model Purpose

### What does this surrogate model predict?

[Clear description of the surrogate's function]

**Example**: *This surrogate model predicts the lift and drag coefficients (CL, CD) of the aircraft wing as a function of angle of attack (α) and Mach number (M). It replaces expensive CFD simulations in real-time digital twin applications.*

### Physical Domain

- **Domain**: [Aerodynamics | Thermal | Structural | Propulsion | Electrical | Other]
- **ATA Chapter**: [ATA-XX - System Name]
- **Subsystem**: [Specific component or subsystem]

### Intended Use

- **Primary Use Case**: [Description]
- **Operational Context**: [Where/how it will be used in the digital twin]
- **Users**: [Flight dynamics simulator | Control system | Health monitoring | Optimization]

---

## 2. Scope and Limitations

### In Scope

- [Use case 1]
- [Use case 2]
- [Input range 1: min to max]
- [Input range 2: min to max]

### Out of Scope

- [What the model should NOT be used for]
- [Conditions outside training envelope]
- [Known edge cases]

**Example Out of Scope**:
- *Transonic buffet conditions (0.7 < M < 0.9 and 8° < α < 12°) are not well-captured*
- *Do not use for angles of attack beyond ±15°*
- *Model trained for clean configuration only (no flaps/slats deployed)*

### Known Limitations

1. **[Limitation 1]**: [Description]
2. **[Limitation 2]**: [Description]
3. **Extrapolation**: [Behavior outside training domain]

---

## 3. Model Details

### Algorithm

- **Type**: [Gaussian Process | Neural Network | Random Forest | XGBoost | Polynomial Chaos | RBF | Kriging]
- **Framework**: [scikit-learn | GPy | TensorFlow | PyTorch | XGBoost | Custom]
- **Version**: [Framework version]

### Input-Output Specification

**Inputs** (N = X):
| Name | Description | Unit | Range | Type |
|------|-------------|------|-------|------|
| `<input_1>` | [Description] | [unit] | [min, max] | float |
| `<input_2>` | [Description] | [unit] | [min, max] | float |

**Outputs** (M = Y):
| Name | Description | Unit | Expected Range | Type |
|------|-------------|------|----------------|------|
| `<output_1>` | [Description] | [unit] | [min, max] | float |
| `<output_2>` | [Description] | [unit] | [min, max] | float |

**Example**:

**Inputs** (N = 2):
| Name | Description | Unit | Range | Type |
|------|-------------|------|-------|------|
| `alpha` | Angle of attack | deg | [-10, 20] | float |
| `Mach` | Mach number | - | [0.2, 0.85] | float |

**Outputs** (M = 2):
| Name | Description | Unit | Expected Range | Type |
|------|-------------|------|----------------|------|
| `CL` | Lift coefficient | - | [-0.5, 2.0] | float |
| `CD` | Drag coefficient | - | [0.01, 0.15] | float |

### Reference Frame

- **Inputs**: [Description of coordinate system, reference conditions]
- **Outputs**: [Description of output reference frame]

**Example**: *Aerodynamic coefficients in wind axis. Angle of attack measured from zero-lift line. Mach number at flight altitude.*

---

## 4. Training Data

### High-Fidelity Source

- **Source Model**: [CFD code | FEM solver | Test data | Flight data]
- **Fidelity Level**: [Description]
- **Computational Cost**: [CPU-hours per evaluation | Test cost]

**Example**: *ANSYS Fluent CFD simulations with SST k-ω turbulence model. Each run: ~4 hours on 64 cores.*

### Design of Experiments (DOE)

- **DOE Type**: [Latin Hypercube | Full Factorial | Sobol Sequence | Adaptive Sampling | Test Matrix]
- **Training Samples**: [N_train samples]
- **Validation Samples**: [N_val samples]
- **Test Samples**: [N_test samples]
- **Coverage**: [Percentage of operational envelope covered]

### Data Characteristics

- **Training Period**: [Date range, if time-series]
- **Data Hash**: `<SHA-256 hash>`
- **Data Location**: `<path to training data>`

---

## 5. Performance Metrics

### Accuracy

| Metric | Training | Validation | Test | Target |
|--------|----------|------------|------|--------|
| RMSE | [value] | [value] | [value] | ≤ [threshold] |
| MAE | [value] | [value] | [value] | ≤ [threshold] |
| R² | [value] | [value] | [value] | ≥ [threshold] |
| Max Error | [value] | [value] | [value] | ≤ [threshold] |
| p95 Error | [value] | [value] | [value] | ≤ [threshold] |

**Example**:

| Metric | Training | Validation | Test | Target |
|--------|----------|------------|------|--------|
| RMSE (CL) | 0.012 | 0.015 | 0.014 | ≤ 0.020 |
| RMSE (CD) | 0.0008 | 0.0010 | 0.0009 | ≤ 0.0015 |
| R² (CL) | 0.998 | 0.996 | 0.997 | ≥ 0.99 |
| Max Error (CL) | 0.042 | 0.048 | 0.045 | ≤ 0.10 |

### Speedup Factor

- **High-Fidelity Evaluation Time**: [time]
- **Surrogate Evaluation Time**: [time]
- **Speedup**: [factor]x

**Example**: *CFD: 4 hours | Surrogate: 5 ms | Speedup: ~2,880,000×*

### Inference Performance

- **Mean Latency**: [value] ms
- **p95 Latency**: [value] ms
- **p99 Latency**: [value] ms
- **Throughput**: [queries per second]
- **Memory Footprint**: [size] MB

---

## 6. Uncertainty Quantification

### Method

- **UQ Method**: [GP Variance | Ensemble Std | Quantile Regression | Conformal Prediction | None]
- **Confidence Level**: [0.95 | other]

### Calibration

- **Expected Coverage**: [percentage]
- **Measured Coverage**: [percentage]
- **Calibration Quality**: [Well-calibrated | Under-confident | Over-confident]

### Out-of-Domain (OOD) Detection

- **OOD Policy**: [Reject | Flag + Extrapolate | Clip to Boundary]
- **Warning Margin**: [percentage] from domain boundary
- **Confidence Degradation**: [How uncertainty increases outside domain]

---

## 7. Validation and Verification

### Validation Against High-Fidelity

- **Validation Date**: YYYY-MM-DD
- **Validation Report**: [Link or path to report]
- **Test Points**: [Number of validation points]
- **Pass Criteria**: [Description]
- **Status**: ✅ Passed | ❌ Failed | ⏳ Pending

### Monotonicity and Physics Constraints

- **Constraints Checked**:
  - [ ] [Constraint 1]
  - [ ] [Constraint 2]

**Example**:
- ✅ CL increases monotonically with α (for α < 12°)
- ✅ CD always positive
- ✅ CL/CD ratio physically reasonable

### Golden Test Set

- **Golden Test Cases**: [Number]
- **Location**: `tests/golden.npz`
- **All Tests Pass**: ✅ Yes | ❌ No

---

## 8. Domain of Validity

### Valid Input Ranges

| Input | Physical Range | Training Range | Recommended Range |
|-------|----------------|----------------|-------------------|
| `<input_1>` | [min, max] | [min, max] | [min, max] |
| `<input_2>` | [min, max] | [min, max] | [min, max] |

**Example**:

| Input | Physical Range | Training Range | Recommended Range |
|-------|----------------|----------------|-------------------|
| `alpha` | [-180°, 180°] | [-10°, 20°] | [-8°, 18°] (with 2° margin) |
| `Mach` | [0, 3.0] | [0.2, 0.85] | [0.25, 0.80] |

### Combined Constraints

- [Constraint description]
- [Mathematical expression]

**Example**: *Avoid transonic buffet region: NOT (0.7 < Mach < 0.9 AND 8° < alpha < 12°)*

### Extrapolation Warnings

- **Beyond Training Range**: [Policy]
- **Confidence Penalty**: [How uncertainty increases]

---

## 9. Integration and Usage

### Runtime API

```python
# Python example
from runtime.python.evaluate import predict

inputs = {
    'alpha': 5.0,  # deg
    'Mach': 0.65
}

outputs = predict(inputs)
# Returns: {'CL': 0.742, 'CD': 0.0245, 'uncertainty': {...}}
```

### FMU Export

- **FMU Available**: ✅ Yes | ❌ No
- **FMI Version**: [2.0 | 3.0]
- **Location**: `runtime/fmu/<name>.fmu`

### Co-Simulation

- **Integration Points**: [Where in digital twin this surrogate is used]
- **Calling Frequency**: [Per time step | On-demand | Periodic]
- **Dependencies**: [Other models this depends on]

---

## 10. Risks and Mitigations

### Risk 1: [Risk Name]

- **Description**: [What could go wrong]
- **Likelihood**: [Low | Medium | High]
- **Impact**: [Low | Medium | High]
- **Mitigation**: [How risk is addressed]

**Example**:

### Risk 1: Extrapolation Beyond Training Domain

- **Description**: User queries outside [-10°, 20°] alpha range
- **Likelihood**: Medium (operational envelope slightly exceeds training range)
- **Impact**: High (incorrect predictions could affect safety)
- **Mitigation**: 
  - OOD detection enabled (warning at 5% margin)
  - Uncertainty increases exponentially outside domain
  - Logging of all OOD queries for monitoring

### Risk 2: Model Degradation Over Time

- **Description**: Real-world aircraft behavior diverges from model (e.g., due to wear, modifications)
- **Likelihood**: Low (short-term), Medium (long-term)
- **Impact**: Medium
- **Mitigation**:
  - Periodic validation against flight test data
  - Monitoring of prediction errors
  - Retraining schedule every 6 months or when error exceeds threshold

---

## 11. Maintenance and Updates

### Retraining Policy

- **Retraining Trigger**: [When to retrain]
- **Retraining Frequency**: [If scheduled]
- **Data Refresh**: [How training data is updated]

**Example**: *Retrain if validation error exceeds 0.03 RMSE, or annually, or when new flight test data available.*

### Monitoring

- **Metrics Tracked**: [List]
- **Monitoring Frequency**: [Real-time | Daily | Weekly]
- **Alert Thresholds**: [Values that trigger alerts]

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | YYYY-MM-DD | Initial production version | [Name] |
| 1.1.0 | YYYY-MM-DD | [Description of changes] | [Name] |

---

## 12. Compliance and Traceability

### Requirements Traceability

- **Linked Requirements**: [REQ-ID-1, REQ-ID-2, ...]
- **Verification Tests**: [TEST-ID-1, TEST-ID-2, ...]

### Certification

- **Certification Level**: [DO-178C Level X | Not certified]
- **Safety Case**: [Link to safety documentation]

### Approval

- **Reviewed By**: [Name, Role]
- **Approved By**: [Name, Role]
- **Approval Date**: YYYY-MM-DD
- **Configuration Control**: [CCB decision reference]

---

## 13. Attachments and References

### Documentation

- **Training Report**: [Link or path]
- **Validation Report**: [Link or path]
- **I/O Contract**: `io_contract.yaml`
- **Training Config**: `train_config.yaml`
- **Domain of Validity**: `domain_of_validity.yaml`

### Artifacts

- **Model File**: `model.joblib`
- **Training Data**: `training/X_train.npz`, `training/y_train.npz`
- **Validation Data**: `validation/X_val.npz`, `validation/y_val.npz`
- **Diagnostics**: `validation/diagnostics/`

### External References

- [Reference to high-fidelity model documentation]
- [Reference to physics-based theory]
- [Published papers or validation studies]

---

## 14. Contact Information

**Model Owner**: [Name]  
**Email**: [email@ideale-eu.eu]  
**Team**: [Team Name]  
**Support**: [Support channel]

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`

**Last Updated**: YYYY-MM-DD
