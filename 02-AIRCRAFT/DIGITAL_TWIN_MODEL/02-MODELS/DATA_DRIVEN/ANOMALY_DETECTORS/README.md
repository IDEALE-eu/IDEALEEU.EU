# ANOMALY_DETECTORS

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/DATA_DRIVEN > ANOMALY_DETECTORS**

ML-based anomaly detection models (residual-based, autoencoder) with Model Cards.

## Purpose

Detect anomalies in sensor data and system behavior for predictive maintenance.

## Contents

- **RESIDUAL_DETECTORS/** - Statistical residual-based anomaly detection
- **AUTOENCODERS/** - Deep learning autoencoders for pattern recognition
- **MODEL_CARDS/** - Model documentation (see `../../13-TEMPLATES/MODEL_CARD_TEMPLATE.md`)

## Model Formats

- **ONNX**: Neural network models (autoencoders, LSTM)
- **Pickle**: Scikit-learn models (Isolation Forest, One-Class SVM)

## Performance Metrics

- **Sensitivity**: >85% (true positive rate)
- **Specificity**: >95% (true negative rate, <5% false positives)

## Validation Requirements

- Cross-validation: 5-fold CV on historical data
- Operational validation: 30-day shadow mode before deployment

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
