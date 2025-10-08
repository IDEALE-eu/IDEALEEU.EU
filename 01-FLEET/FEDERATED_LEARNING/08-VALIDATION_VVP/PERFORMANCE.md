# PERFORMANCE

FL model performance metrics (latency, accuracy, resource usage).

## Performance Targets

### Inference Latency

- **p50**: < 100 ms
- **p95**: < 500 ms
- **p99**: < 1 second

### Accuracy

- **AUC**: ≥ 0.90 (binary classification)
- **F1 score**: ≥ 0.87
- **False positive rate**: ≤ 5%

### Resource Usage (Aircraft Edge)

- **CPU**: ≤ 30%
- **Memory**: ≤ 1 GB
- **Disk**: ≤ 10 GB (model + logs)
- **Network**: ≤ 10 Mbps upload

## Benchmarking

- **Baseline**: Compare with previous model version
- **Target**: 10% improvement (accuracy, latency, or resource usage)

## Related Documents

- **../03-CLIENTS/AIRCRAFT_EDGE/RUNTIME_CONSTRAINTS.md** - Resource limits
- **../12-METRICS/INFERENCE_METRICS.csv** - Performance logs
