# MODEL_CARD_TEMPLATE

Model card template for FL models (based on Google's Model Card framework).

## Model Details

- **Model Name**: {Name}
- **Model Version**: {Version}
- **Model ID**: {FL-MODEL-*}
- **Owner**: {AI/ML Team}
- **Date**: {YYYY-MM-DD}

## Intended Use

### Primary Use Case

{Description of primary use case, e.g., predictive maintenance for engine bearings}

### Secondary Use Cases

{Optional: Other validated use cases}

### Out-of-Scope Use Cases

{Use cases this model should NOT be used for, e.g., flight-critical actuation}

## Model Architecture

- **Type**: {LSTM|CNN|Transformer|...}
- **Framework**: {PyTorch|TensorFlow}
- **Input**: {Input signals, see data contract}
- **Output**: {Output format, e.g., binary classification}

## Training Data

- **Dataset**: {Dataset ID, see [../../06-MODELS/DATASETS_INDEX.md](../../06-MODELS/DATASETS_INDEX.md)}
- **Size**: {Number of samples}
- **Date Range**: {YYYY-MM to YYYY-MM}
- **Provenance**: {Source: aircraft fleet, sim rigs, etc.}

## Performance

- **Accuracy (AUC)**: {0.90}
- **Precision**: {0.85}
- **Recall**: {0.90}
- **F1 Score**: {0.87}
- **False Positive Rate**: {5%}

### Performance by Group

| Group          | AUC  | Precision | Recall |
|----------------|------|-----------|--------|
| Aircraft Type A| 0.91 | 0.86      | 0.91   |
| Aircraft Type B| 0.89 | 0.84      | 0.89   |

## Limitations

- {Limitation 1, e.g., lower accuracy on aircraft > 15 years old}
- {Limitation 2, e.g., requires sensor calibration within 6 months}
- {Limitation 3, e.g., not validated for extreme weather conditions}

## Safety Considerations

⚠️ **ADVISORY ONLY**: This model provides recommendations only. All decisions must be reviewed by qualified personnel.

- **No flight-critical actuation**: Model outputs do not directly control aircraft systems
- **Human-in-the-loop**: CCB approval required for deployment
- **Rollback capability**: Model can be rolled back immediately if drift detected

## Ethical Considerations

- **Fairness**: Model performance disaggregated by aircraft type, age, region (see [../../08-VALIDATION_VVP/BIAS_FAIRNESS.md](../../08-VALIDATION_VVP/BIAS_FAIRNESS.md))
- **Privacy**: Differential privacy (ε=1.0), pseudonymisation applied
- **Transparency**: Model card published, training data provenance documented

## Changelog

| Version | Date       | Changes                     | Author     |
|---------|------------|-----------------------------|------------|
| 1.0.0   | 2024-11-01 | Initial release             | AI/ML Team |
| 1.1.0   | 2024-11-15 | Improved accuracy, added DP | AI/ML Team |

## Related Documents

- [**../../06-MODELS/REGISTRY.md**](../../06-MODELS/REGISTRY.md) - Model versioning
- [**../../08-VALIDATION_VVP/**](../../08-VALIDATION_VVP/) -  Validation results
- [**../../11-COMPLIANCE/**](../../11-COMPLIANCE/) -  Compliance frameworks
