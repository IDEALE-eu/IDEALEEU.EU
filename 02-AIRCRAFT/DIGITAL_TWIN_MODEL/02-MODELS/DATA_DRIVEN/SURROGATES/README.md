# SURROGATES

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/DATA_DRIVEN > SURROGATES**

Data-driven surrogate models that replace expensive high-fidelity simulations (CFD, FEM) with fast, accurate approximations for real-time digital twin applications.

## Purpose

Enable real-time "what-if" analysis, optimization, and co-simulation by replacing computationally expensive physics-based models with data-driven surrogates that maintain high accuracy while achieving millisecond inference times.

**Key Capabilities**:
- **Speedup**: 10³ to 10⁶× faster than high-fidelity models
- **Accuracy**: Typically RMSE <5% vs. reference models
- **Uncertainty Quantification**: Calibrated confidence intervals
- **FMU Export**: FMI-compliant for co-simulation
- **Production Ready**: Versioned, validated, and auditable

## Directory Structure

```
SURROGATES/
├── REGISTRY/
│   └── index.yaml                    # Central registry of all surrogate models
├── TEMPLATES/
│   ├── io_contract.example.yaml     # I/O specification template
│   ├── train_config.example.yaml    # Training configuration template
│   └── surrogate_card.example.md    # Model card template
├── TOOLS/
│   ├── fit.py                        # Train surrogate from DOE/data
│   ├── validate.py                   # Validate contract, ranges, metrics
│   ├── profile.py                    # Measure latency and throughput
│   ├── export_c.py                   # Optional C/C++ code generation
│   ├── pack_fmu.py                   # Package as FMU (FMI 2.0/3.0)
│   └── plot_error_maps.py            # Generate diagnostic plots
└── <sur_id>/<semver>/                # Individual surrogate models
    ├── model.joblib                  # Trained model (GP/RBF/XGB/MLP)
    ├── io_contract.yaml              # I/O specification
    ├── domain_of_validity.yaml       # Valid input ranges
    ├── train_config.yaml             # Training parameters
    ├── card.md                       # Model card (documentation)
    ├── README.md                     # Quick start guide
    ├── training/
    │   ├── X_train.npz
    │   ├── y_train.npz
    │   └── data_hash.sha256
    ├── validation/
    │   ├── X_val.npz
    │   ├── y_val.npz
    │   ├── metrics.json
    │   └── diagnostics/              # Parity plots, residuals, etc.
    ├── uncertainty/
    │   └── params.yaml               # UQ configuration
    ├── runtime/
    │   ├── python/evaluate.py        # Stable predict() API
    │   ├── c/                        # Optional C library
    │   └── fmu/<name>.fmu            # FMU package
    ├── tests/
    │   ├── contract_test.py
    │   ├── monotonicity.yaml         # Physics constraints
    │   └── golden.npz                # Regression tests
    └── checksum.sha256
```

## Workflow

### 1. Generate High-Fidelity Data

Run physics-based simulations (CFD, FEM) over a Design of Experiments (DOE):

```bash
# Example: CFD simulations for aerodynamic coefficients
# Vary alpha (angle of attack) and Mach number
# Output: CL (lift) and CD (drag) coefficients
```

### 2. Train Surrogate Model

Use `fit.py` to train a surrogate model:

```bash
cd TOOLS
./fit.py --config ../thermal_avionics_temp/1.0.0/train_config.yaml \
         --output-dir ../thermal_avionics_temp/1.0.0/
```

**Supported Algorithms**:
- Gaussian Process Regression (GPR)
- Random Forest / XGBoost
- Neural Networks (MLP, CNN)
- Polynomial Chaos Expansion (PCE)
- Radial Basis Functions (RBF)
- Reduced-Order Models (ROM/POD/DMD)

### 3. Validate Model

Validate against I/O contract, domain, and performance metrics:

```bash
./validate.py --model-dir ../thermal_avionics_temp/1.0.0/ \
              --test-data test_data.npz \
              --strict
```

Validation checks:
- ✅ I/O contract compliance
- ✅ Domain of validity
- ✅ Performance metrics (RMSE, MAE, R²)
- ✅ Physics constraints (monotonicity, bounds)
- ✅ Golden test set (regression tests)

### 4. Profile Performance

Measure inference latency and throughput:

```bash
./profile.py --model-dir ../thermal_avionics_temp/1.0.0/ \
             --n-samples 1000
```

### 5. Package as FMU

Export for co-simulation (FMI standard):

```bash
./pack_fmu.py --model-dir ../thermal_avionics_temp/1.0.0/ \
              --fmu-name thermal_avionics_temp \
              --fmi-version 2.0
```

### 6. Integrate into Digital Twin

Use the surrogate in your digital twin simulation:

```python
# Option 1: Python API
from thermal_avionics_temp.runtime.python.evaluate import predict

result = predict({
    'T_ambient': 35.0,  # °C
    'P_load': 65.0,     # W
    'airflow': 3.5      # m³/min
})
print(f"Temperature: {result['T_component']:.1f} °C")

# Option 2: FMU Co-Simulation
fmu = load_fmu("thermal_avionics_temp.fmu")
fmu.set_real([0, 1, 2], [35.0, 65.0, 3.5])
fmu.do_step(t, dt)
T = fmu.get_real([3])[0]
```

## Example Models

### Thermal Avionics Temperature (`thermal_avionics_temp/1.0.0`)

Predicts steady-state temperature of electronic components in avionics bay.

- **Inputs**: Ambient temperature, power load, airflow
- **Output**: Component temperature
- **Algorithm**: Gaussian Process (Matérn kernel)
- **Performance**: RMSE = 2.1°C, inference = 3.5ms, speedup = 514,000×

See [thermal_avionics_temp/1.0.0/README.md](thermal_avionics_temp/1.0.0/README.md) for details.

### Aerodynamic Wing Coefficients (`aero_wing_cl_cd/`)

*(Example from registry - not yet implemented)*

Predicts lift (CL) and drag (CD) coefficients for wing.

- **Inputs**: Angle of attack, Mach number
- **Outputs**: CL, CD
- **Algorithm**: Gaussian Process
- **Source**: CFD simulations (ANSYS Fluent)

## Model Formats

- **Joblib/Pickle**: Scikit-learn models (GP, RF, XGB)
- **ONNX**: Neural networks (portable across frameworks)
- **HDF5**: Large ROM basis functions
- **FMU**: FMI 2.0/3.0 for co-simulation

## Model Registry

All surrogate models are tracked in [REGISTRY/index.yaml](REGISTRY/index.yaml):

```yaml
surrogates:
  thermal_avionics_temp:
    domain: thermal
    ata_chapter: ATA-31
    versions:
      - semver: 1.0.0
        status: production
        location: thermal_avionics_temp/1.0.0/
```

## Fidelity Levels

- **Level 5 (Real-Time)**: Inference <100ms
- **Level 4 (Fast)**: Inference <1s
- **Level 3 (Standard)**: Inference <10s

Target: Level 5 (real-time) for digital twin integration.

## Validation Requirements

| Criterion | Target | Typical |
|-----------|--------|---------|
| **Accuracy** | RMSE <5% vs. high-fidelity | 1-3% |
| **Coverage** | 95% of operational envelope | >95% |
| **Inference Time** | <100ms | 1-10ms |
| **Uncertainty** | Well-calibrated 95% CI | ±1% coverage |

## Quality Assurance

Each surrogate model includes:

1. **Model Card** (`card.md`): Purpose, performance, limitations, risks
2. **I/O Contract** (`io_contract.yaml`): Formal interface specification
3. **Domain of Validity** (`domain_of_validity.yaml`): Valid input ranges
4. **Training Config** (`train_config.yaml`): Reproducible training setup
5. **Validation Report**: Metrics, diagnostics, test results
6. **Golden Tests**: Regression test suite for version control

## Integration with Digital Twin Architecture

Surrogates integrate into the digital twin architecture at multiple levels:

- **L2 Model Layer**: Replace expensive physics models in real-time loops
- **Co-Simulation**: FMU packages for model exchange and co-simulation
- **Control Logic**: Fast predictions enable model-based control
- **Optimization**: Rapid "what-if" analysis for design and operations

See [../../01-ARCHITECTURE/REFERENCE_ARCHITECTURE.md](../../01-ARCHITECTURE/REFERENCE_ARCHITECTURE.md) for integration details.

## Best Practices

### Training

1. Use systematic DOE (LHS, Sobol, adaptive sampling)
2. Include validation and test sets (80/10/10 or 70/20/10 split)
3. Document all training parameters for reproducibility
4. Use version control for training data (hash checksums)

### Validation

1. Validate against independent high-fidelity data
2. Check physics constraints (monotonicity, bounds, conservation laws)
3. Profile performance (latency, throughput, memory)
4. Test uncertainty calibration

### Deployment

1. Package as FMU for portability
2. Provide stable Python API with semantic versioning
3. Monitor performance in production
4. Plan for model retraining (data drift, domain expansion)

## Tools Documentation

| Tool | Purpose | Usage |
|------|---------|-------|
| `fit.py` | Train model from data | `./fit.py --config train_config.yaml` |
| `validate.py` | Validate model | `./validate.py --model-dir path/ --test-data data.npz` |
| `profile.py` | Performance profiling | `./profile.py --model-dir path/` |
| `export_c.py` | C/C++ code gen | `./export_c.py --model-dir path/ --output-dir c_code/` |
| `pack_fmu.py` | FMU packaging | `./pack_fmu.py --model-dir path/ --fmu-name name` |
| `plot_error_maps.py` | Diagnostics plots | `./plot_error_maps.py --model-dir path/ --test-data data.npz` |

## References

- [FMI Standard](https://fmi-standard.org/) - Functional Mock-up Interface
- [Model Cards](https://modelcards.withgoogle.com/) - Model documentation framework
- [Surrogate Modeling Best Practices](https://arxiv.org/abs/1906.12323)

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`

**Maintainer**: Digital Twin Model Team  
**Last Updated**: 2024-11-20
