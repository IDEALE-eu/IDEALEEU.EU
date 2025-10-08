# 12-METRICS

FL performance metrics, KPIs, training/inference logs, and drift alerts.

## Purpose

Define key performance indicators (KPIs) for FL system health, training performance, and model drift detection.

## Contents

- [**00-README.md**](00-README.md) - This file
- [**KPI_DEFINITIONS.md**](KPI_DEFINITIONS.md) - KPI definitions (participation, round time, ε-budget)
- **TRAINING_METRICS.csv** - Aggregated training metrics (privacy-preserving)
- **INFERENCE_METRICS.csv** - Inference metrics (AUC, RMSE, CPU%, memory)
- **DRIFT_ALERTS.csv** - Drift alerts from ../../04-ALGORITHMS/DRIFT_DETECTION.md

## Metrics Categories

### System Health

- **Client participation rate**: % of eligible clients contributing per round
- **Round completion time**: Duration from model distribution to aggregation
- **Aggregation latency**: Time for server-side aggregation

### Training Performance

- **Global loss**: Aggregated training loss across clients
- **Validation accuracy**: AUC, F1 score, precision, recall
- **Privacy budget**: Cumulative ε, δ consumed

### Inference Performance

- **Latency**: p50, p95, p99 percentiles
- **Accuracy**: Real-time prediction accuracy
- **Resource usage**: CPU%, memory%, disk%, network

### Drift Detection

- **PSI (Population Stability Index)**: Distribution drift metric
- **KS test p-value**: Statistical significance of drift
- **Concept drift**: Accuracy degradation over time

## Dashboards

- **Grafana**: Real-time FL metrics
- **MLflow**: Experiment tracking (see [../../07-EXPERIMENTS/TRACKING.md](../../07-EXPERIMENTS/TRACKING.md))

## Related Documents

- [**KPI_DEFINITIONS.md**](KPI_DEFINITIONS.md) - Detailed metric definitions
- [**../../04-ALGORITHMS/DRIFT_DETECTION.md**](../../04-ALGORITHMS/DRIFT_DETECTION.md) - Drift detection methods
