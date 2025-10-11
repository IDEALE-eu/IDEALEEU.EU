# Thermal Avionics Temperature Surrogate Model

**Version**: 1.0.0  
**Status**: Production  
**Last Updated**: 2024-11-20

## Quick Start

This surrogate model predicts steady-state temperature of avionics bay electronic components.

### Python API

```python
from runtime.python.evaluate import predict

inputs = {
    'T_ambient': 35.0,  # °C
    'P_load': 65.0,     # W
    'airflow': 3.5      # m³/min
}

result = predict(inputs)
print(f"Component temperature: {result['T_component']:.1f} °C")
print(f"Uncertainty (95% CI): ±{result['uncertainty_95']:.1f} °C")
```

### FMU Co-Simulation

```python
# Load FMU
fmu = load_fmu("runtime/fmu/thermal_avionics_temp.fmu")

# Set inputs
fmu.set_real([0, 1, 2], [35.0, 65.0, 3.5])

# Execute step
fmu.do_step(t, dt)

# Get output
T_component = fmu.get_real([3])[0]
```

## Documentation

- [**Model Card**](card.md) - Detailed model documentation
- [**I/O Contract**](io_contract.yaml) - Input/output specification
- [**Training Config**](train_config.yaml) - Training parameters
- [**Domain of Validity**](domain_of_validity.yaml) - Valid input ranges

## Model Files

```
thermal_avionics_temp/1.0.0/
├── model.joblib              # Trained GP model
├── io_contract.yaml          # I/O specification
├── train_config.yaml         # Training configuration
├── domain_of_validity.yaml   # Valid ranges
├── card.md                   # Model card
├── README.md                 # This file
├── training/
│   ├── X_train.npz
│   ├── y_train.npz
│   └── data_hash.sha256
├── validation/
│   ├── X_val.npz
│   ├── y_val.npz
│   ├── metrics.json
│   └── diagnostics/
├── runtime/
│   ├── python/evaluate.py
│   └── fmu/
└── tests/
    ├── contract_test.py
    └── golden.npz
```

## Performance

- **RMSE**: 2.1°C (validation set)
- **Inference Time**: 3.5 ms (mean)
- **Speedup**: 514,000× vs. FEM
- **Uncertainty**: Well-calibrated 95% confidence intervals

## Valid Ranges

- **Ambient Temperature**: -20°C to 70°C
- **Power Load**: 5W to 120W
- **Airflow**: 0.5 to 8.0 m³/min

## Contact

**Owner**: Thermal Analysis Team  
**Email**: thermal-analysis@ideale-eu.eu

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
