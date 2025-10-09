# INFERENCE_RUNTIME

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 12-CODE > INFERENCE_RUNTIME**

Model loaders, validators, adapters with unit tests.

## Purpose

Runtime code for loading, executing, and validating digital twin models.

## Contents

- **loaders/** - Model loading utilities (ONNX, pickle, HDF5)
- **validators/** - Input/output validation, schema checking
- **adapters/** - Interface adapters (telemetry → model input, model output → KPIs)
- **tests/** - Unit tests (pytest)

## Code Structure

```
INFERENCE_RUNTIME/
├── loaders/
│   ├── onnx_loader.py
│   ├── pickle_loader.py
│   └── fmu_loader.py
├── validators/
│   ├── input_validator.py
│   ├── output_validator.py
│   └── schema_validator.py
├── adapters/
│   ├── telemetry_adapter.py
│   └── kpi_adapter.py
├── tests/
│   ├── test_loaders.py
│   ├── test_validators.py
│   └── test_adapters.py
└── requirements.txt
```

## Testing

- **Framework**: pytest
- **Coverage**: >95% (Level C), 100% (Level A/B)
- **CI/CD**: Automated testing on every commit (see `../CI_CD/`)

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
