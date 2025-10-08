# TRACKING

Experiment tracking with MLflow, Weights & Biases (W&B), or custom tools.

## Recommended Tools

### MLflow

- **Use case**: Model registry, experiment tracking, deployment
- **Integration**: Python API, REST API
- **Storage**: S3, Azure Blob, local filesystem

### Weights & Biases (W&B)

- **Use case**: Experiment visualization, hyperparameter tuning
- **Integration**: Python API, TensorBoard integration
- **Storage**: Cloud-hosted (W&B SaaS)

## Tracked Metrics

- Training loss, validation accuracy
- Client participation rate
- Privacy budget consumed (ε, δ)
- Model size, inference latency
- Drift metrics (PSI, KS test p-value)

## Related Documents

- [**AB_TESTS/**](AB_TESTS/) -  A/B test experiment designs
- [**../12-METRICS/KPI_DEFINITIONS.md**](../12-METRICS/KPI_DEFINITIONS.md) - Metric definitions
