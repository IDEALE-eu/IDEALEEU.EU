# AQUA-QC: Quantum Computing Infrastructure

This directory contains quantum computing algorithms for noise mitigation and environmental monitoring, with full traceability via UTCS-MI v5.0.

## Repository Layout

```
aqua-qc/
├── algos/                    # Algorithm implementations
│   ├── qnoise_qiskit_001.py # Quantum noise mitigation (Qiskit_001)
│   └── qml_env_002.py       # QML for environmental monitoring (Qiskit_002)
├── tests/                    # Acceptance tests
│   ├── test_qnoise_001.py   # Noise mitigation tests
│   ├── test_qml_002.py      # QML algorithm tests
│   └── test_reward_mint.py  # TeknIA reward tests
├── benches/                  # Benchmark configurations
│   ├── vqe_h2_sto3g.py      # VQE H₂ benchmark
│   ├── qaoa_maxcut_erdos.py # QAOA MaxCut benchmark
│   └── kernels_svm_pm25.py  # Quantum kernel SVM benchmark
├── ci/                       # CI configuration
│   ├── config.yaml          # Build and test config
│   └── device_matrix.yaml   # Backend configurations
└── utcs/                     # Traceability
    └── schema_utcsmi_v5.json # UTCS-MI v5.0 schema
```

## Algorithms

### 1. Qiskit_001 — Enhanced Quantum Noise Mitigation

**Purpose**: Mitigate noise in quantum circuits through multiple techniques:
- Zero-noise extrapolation (ZNE)
- Clifford data regression (CDR)
- Readout error mitigation with drift tracking
- ML-based residual correction

**API**:
```python
from algos.qnoise_qiskit_001 import mitigate_observable

result = mitigate_observable(
    circ=circuit,
    backend=backend,
    shots=4096,
    zne_budget={"fold_scales": [1, 3, 5]},
    cdr_budget={"n_samples": 10},
    readout_cal={"matrix": ro_matrix, "timestamp": ts},
    drift_tracker={"ΔT": 0.02, "τ_max": 0.5},
    resid_model=sklearn_regressor,
    hooks={"on_fold": callback, ...}
)
# Returns: {"exp": float, "stderr": float, "meta": {...}}
```

**KPI Acceptance Gates**:
- `infidelity_drop ≥ 0.30`
- `vqe_energy_err_drop ≥ 0.50 * |E_ref - E_unmit|`
- `overhead_depth ≤ 3.0`
- `wall_time_ratio ≤ 1.5`

### 2. Qiskit_002 — QML for Environmental Monitoring

**Purpose**: Apply quantum machine learning to environmental data:
- Quantum kernel methods with configurable feature maps
- Temporal embedding for time-series
- Domain adaptation (MMD, CORAL)
- Hybrid classical-quantum features

**API**:
```python
from algos.qml_env_002 import train_quantum_kernel

result = train_quantum_kernel(
    X_train=features,
    y_train=labels,
    X_val=val_features,
    y_val=val_labels,
    feature_map_cfg={"type": "ZZ", "n_qubits": 4, "reps": 2},
    temporal_embed_cfg={"window_size": 5, "aggregation": "mean"},
    nyström=50,  # Optional: use Nyström approximation
    mix_classical=True,
    hooks={"on_eval": callback, ...}
)
# Returns: {"model": obj, "val_metrics": {...}, "meta": {...}}
```

**KPI Acceptance Gates**:
- `F1_anomaly ≥ 0.80`
- `RMSE_drop ≥ 0.10` (vs baseline)
- `Energy_per_inf_drop ≥ 0.15`

## Testing

### Run All Tests

```bash
cd aqua-qc
pytest tests/ -v
```

### Run Specific Test Suite

```bash
# Noise mitigation tests
pytest tests/test_qnoise_001.py -v

# QML tests
pytest tests/test_qml_002.py -v

# Reward calculation tests
pytest tests/test_reward_mint.py -v
```

### Run with Coverage

```bash
pytest tests/ --cov=algos --cov-report=html
```

## Benchmarks

### VQE H₂ STO-3G

```bash
python benches/vqe_h2_sto3g.py
```

Runs variational quantum eigensolver for H₂ molecule with noise mitigation.

### QAOA MaxCut

```bash
python benches/qaoa_maxcut_erdos.py
```

Runs QAOA on Erdős-Rényi random graphs with various sizes.

### Quantum Kernel SVM (PM2.5)

```bash
python benches/kernels_svm_pm25.py
```

Trains quantum kernel SVM on synthetic PM2.5 air quality data.

## UTCS-MI v5.0 Traceability

All algorithms return metadata conforming to UTCS-MI v5.0 schema:

```json
{
  "uid": "Qiskit_001_20240624_APCGPT",
  "utcs_id13": "ABC1234567890",
  "hash": "sha256...",
  "inputs_sig": "sha256(...)",
  "calib_sig": "sha256(...)",
  "bench_case": "H2|MaxCut|PM25|...",
  "kpi": {
    "infidelity_drop": 0.35,
    "overhead_depth": 2.8,
    ...
  }
}
```

Schema validation:
```bash
# Validate against schema
python -c "import json, jsonschema
schema = json.load(open('utcs/schema_utcsmi_v5.json'))
meta = json.load(open('result_meta.json'))
jsonschema.validate(meta, schema)
print('✓ Valid UTCS-MI v5.0 metadata')"
```

## Hooks for Testing and Monitoring

Both algorithms support testable hooks for observability:

**Noise Mitigation Hooks**:
- `on_fold(scale, circ_id)` - Called for each ZNE fold
- `on_cdr_sample(k, clifford_score)` - CDR sampling
- `on_cal_update(timestamp, t1t2, ro_matrix)` - Calibration updates
- `on_resid_fit(r2, val_mae)` - Residual model fit
- `on_result(exp, stderr)` - Final result

**QML Hooks**:
- `on_embed_stat(mean_amp, sparsity)` - Embedding statistics
- `on_kernel_spectrum(cond_num, eig_decay)` - Kernel spectrum
- `on_domain_adapt(mmd, coral_loss)` - Domain adaptation
- `on_eval(f1, rmse, energy_j)` - Evaluation metrics

## TeknIA Rewards

Reward formula:
```
R_t = αC*(€_saved) + αE*(kgCO2_saved) + αQ*(F1 or ΔE) 
      - αOH*(overhead_depth−3)⁺ - αWT*(wall_time_ratio−1.5)⁺
mint_t = κ * max(R_t, 0)
```

Parameters configured in `ci/config.yaml`.

Test reward calculation:
```bash
pytest tests/test_reward_mint.py -v
```

## CI/CD Integration

Configuration in `ci/device_matrix.yaml`:
- Simulation backends (Aer, fake devices)
- Optional hardware slot for nightly runs
- Test matrix across backends, shots, fold scales
- Drift detection and recalibration policies

Run CI locally:
```bash
# Install dependencies
pip install -r requirements.txt  # (create if needed)

# Run linting
black algos/ tests/ --check
flake8 algos/ tests/

# Run tests
pytest tests/ -v --cov=algos
```

## Dependencies

Core:
- `qiskit >= 0.44.0`
- `qiskit-aer >= 0.12.0`
- `numpy >= 1.24.0`
- `scipy >= 1.10.0`
- `scikit-learn >= 1.3.0`

Development:
- `pytest >= 7.4.0`
- `pytest-cov >= 4.1.0`
- `pyyaml >= 6.0`

## References

- UTCS Registry: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`
- Digital Twin Models: `02-AIRCRAFT/DIGITAL_TWIN_MODEL/`
- Federated Learning: `01-FLEET/FEDERATED_LEARNING/`

## Contact

For questions or issues, see repository maintainers.
