# SURROGATES

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/DATA_DRIVEN > SURROGATES**

Regression models, Gaussian Process Regression (GPR), and reduced-order models for fast inference.

## Purpose

Data-driven surrogate models to accelerate physics-based simulations.

## Contents

- **GPR_MODELS/** - Gaussian Process Regression surrogates for aerodynamics, thermal
- **NEURAL_SURROGATES/** - Neural network-based surrogates (feed-forward, CNN)
- **ROM/** - Reduced-Order Models (POD, DMD)

## Model Formats

- **ONNX**: Standardized format for neural networks
- **Pickle/Joblib**: Scikit-learn models (GPR, linear regression)
- **HDF5**: Large model parameters (ROM basis functions)

## Fidelity Level

- **Level 5 (Real-Time)**: Inference <100ms

## Validation Requirements

- Accuracy: RMSE <5% vs. high-fidelity physics models
- Coverage: Training data covers 95% of operational envelope

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
