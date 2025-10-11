# Aerodynamic Wing Coefficients Surrogate Model

**Version**: 1.0.0  
**Status**: Validated  
**Last Updated**: 2025-01-15

## Overview

This surrogate model predicts lift coefficient (CL) and drag coefficient (CD) for the aircraft wing as functions of angle of attack (α) and Mach number (M). It replaces expensive CFD simulations in flight dynamics and performance analysis.

### Quick Example

```python
from runtime.python.evaluate import predict

result = predict({
    'alpha': 5.0,    # deg
    'Mach': 0.65     # -
})

print(f"CL = {result['CL']:.4f}")
print(f"CD = {result['CD']:.4f}")
```

## Key Specifications

- **Domain**: Aerodynamics (ATA-57 Wings)
- **Algorithm**: Gaussian Process Regression with RBF kernel
- **Source Data**: ANSYS Fluent CFD (SST k-ω turbulence model)
- **Training Samples**: 500 CFD runs (Latin Hypercube)
- **Speedup**: ~2,880,000× vs. CFD

## Performance

| Metric | CL | CD | Target |
|--------|----|----|--------|
| RMSE | 0.015 | 0.0010 | ≤0.020 / ≤0.0015 |
| R² | 0.996 | 0.994 | ≥0.99 |
| Inference | 5 ms | 5 ms | <100 ms |

## Valid Ranges

- **Angle of Attack**: -10° to 20° (recommended: -8° to 18°)
- **Mach Number**: 0.2 to 0.85 (recommended: 0.25 to 0.80)

⚠️ **Avoid transonic buffet region**: 0.7 < M < 0.9 AND 8° < α < 12°

## Documentation

- [**Model Card**](card.md) - Complete documentation
- [**I/O Contract**](io_contract.yaml) - Interface specification
- [**Domain of Validity**](domain_of_validity.yaml) - Valid input ranges

## Status

**Registry**: Tracked in [../../REGISTRY/index.yaml](../../REGISTRY/index.yaml)  
**Approval**: Aerodynamics Team Lead - 2025-01-15  
**Config Control**: CCB-2025-AERO-003

---

*Note: This is a skeleton example. Full model artifacts (model.joblib, training data, etc.) would be populated during actual model training.*
