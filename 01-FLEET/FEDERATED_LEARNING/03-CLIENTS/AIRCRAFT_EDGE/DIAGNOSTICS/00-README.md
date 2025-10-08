# DIAGNOSTICS

Local health checks and diagnostics for aircraft edge FL clients.

## Purpose

Automated diagnostics to ensure FL client health and detect anomalies before they impact training or safety.

## Diagnostic Checks

### Hardware Health

- **CPU**: Temperature, usage, throttling events
- **Memory**: Usage, fragmentation, swap (should be 0)
- **Disk**: Usage, I/O errors, SMART status
- **Network**: Latency, packet loss, bandwidth

### Software Health

- **FL client process**: Running, responsive, no crashes
- **Model files**: Integrity (checksums), version correctness
- **Gradients**: Not corrupted, within expected size range
- **Logs**: No error spikes, disk space available

### Model Health

- **Inference latency**: p50, p95, p99 percentiles
- **Prediction drift**: PSI, KS test (see [04-ALGORITHMS/DRIFT_DETECTION.md](04-ALGORITHMS/DRIFT_DETECTION.md))
- **Accuracy**: On validation set (if available)

## Diagnostic Schedule

- **Continuous**: CPU, memory, disk (every 60 seconds)
- **Hourly**: Network latency, model inference test
- **Daily**: Full health check, SMART status
- **Weekly**: Model drift detection

## Alerting

- **Local**: Log to /var/fl-client/diagnostics.log
- **Remote**: Send to 12-METRICS/ (if connectivity available)
- **Thresholds**: See RUNTIME_CONSTRAINTS.md

## Related Documents

- [**../RUNTIME_CONSTRAINTS.md**](../RUNTIME_CONSTRAINTS.md) - Resource limits
- [**../../12-METRICS/KPI_DEFINITIONS.md**](../../12-METRICS/KPI_DEFINITIONS.md) - Metric definitions
