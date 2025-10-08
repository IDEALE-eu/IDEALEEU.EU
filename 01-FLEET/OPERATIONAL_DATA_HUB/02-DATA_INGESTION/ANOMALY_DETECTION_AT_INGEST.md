# ANOMALY_DETECTION_AT_INGEST

Real-time anomaly detection before data storage.

## Purpose

Detect anomalies in telemetry at ingestion to enable:
- Early warning for system faults
- Data quality assessment
- Triggering maintenance alerts
- Filtering noise from curated datasets

## Detection Methods

### 1. Statistical Anomaly Detection

**3-Sigma Rule:**
```python
# Flag values outside 3 standard deviations
anomaly = abs(value - mean) > 3 * std_dev
```

**Interquartile Range (IQR):**
```python
# Flag values outside 1.5 * IQR from quartiles
Q1, Q3 = quantile(data, [0.25, 0.75])
IQR = Q3 - Q1
anomaly = (value < Q1 - 1.5*IQR) or (value > Q3 + 1.5*IQR)
```

**Moving Average Deviation:**
```python
# Flag sudden deviations from moving average
moving_avg = exponential_moving_average(window=100)
anomaly = abs(value - moving_avg) > threshold
```

**Applicability:** Good for gradual drift, sensor failures, outliers

### 2. Machine Learning-Based Detection

**Isolation Forest:**
- Unsupervised anomaly detection
- Isolates anomalies by random partitioning
- Low computational cost, suitable for streaming

**Autoencoder:**
- Neural network trained to reconstruct normal patterns
- Anomalies have high reconstruction error
- Trained on historical "normal" data

**One-Class SVM:**
- Learn boundary around normal data
- Points outside boundary flagged as anomalies

**Applicability:** Complex multivariate patterns, context-dependent anomalies

### 3. Domain-Specific Checks

**Physics-Based Constraints:**
```yaml
# Example: Energy balance check
rule: power_balance_check
condition: |
  power_generated + battery_discharge >= power_consumed
tolerance: 5%  #允许5%测量误差
anomaly_action: ALERT
```

**State Machine Validation:**
```yaml
# Example: Valid state transitions
rule: flight_phase_sequence
valid_transitions:
  ground: [taxi, takeoff]
  taxi: [ground, takeoff]
  takeoff: [climb]
  climb: [cruise, descent]
  cruise: [descent]
  descent: [approach]
  approach: [landing, climb]  # Go-around
  landing: [ground]
invalid_transition_action: ANOMALY
```

**Applicability:** Known physical laws, operational procedures

## Anomaly Severity Classification

| Severity | Description | Action |
|----------|-------------|--------|
| **Critical** | Safety-critical system failure | Immediate alert to operators |
| **High** | Major system degradation | Alert within 5 minutes |
| **Medium** | Minor anomaly, may indicate early fault | Log and flag for review |
| **Low** | Statistical outlier, likely benign | Log only |

## Anomaly Types

### Sensor Faults
- **Stuck Sensor**: Value unchanged for extended period
- **Drift**: Gradual deviation from expected range
- **Spike**: Sudden transient outlier
- **Noise**: High-frequency oscillations

### System Faults
- **Performance Degradation**: Parameter slowly declining
- **State Inconsistency**: Multiple sensors disagree
- **Energy Imbalance**: Power generation/consumption mismatch

### Operational Anomalies
- **Off-Nominal Maneuver**: Unexpected flight profile
- **Configuration Error**: System in invalid state

## Detection Pipeline

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Telemetry    │────▶│ Statistical  │────▶│ ML-Based     │
│ Message      │     │ Detectors    │     │ Detectors    │
└──────────────┘     └──────────────┘     └──────────────┘
                              │                    │
                              ▼                    ▼
                     ┌─────────────────────────────┐
                     │ Anomaly Aggregation &       │
                     │ Severity Classification     │
                     └─────────────────────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
          ┌─────────────┐  ┌─────────────┐  ┌──────────┐
          │ Alert       │  │ Anomaly     │  │ Continue │
          │ Operators   │  │ Queue       │  │ Normal   │
          └─────────────┘  └─────────────┘  └──────────┘
```

## Configuration Example

```yaml
# h2_tank_pressure_fwd anomaly detection
signal: h2_tank_pressure_fwd
detectors:
  - type: statistical
    method: 3_sigma
    window: 1000  # samples
    threshold: 3.0
    severity: MEDIUM
  
  - type: statistical
    method: moving_average
    window: 100
    deviation_threshold: 20  # bar
    severity: HIGH
  
  - type: ml
    model: isolation_forest
    model_version: v1.2.0
    contamination: 0.01  # Expected anomaly rate
    severity: HIGH
  
  - type: domain
    rule: physics_constraint
    max_rate_of_change: 50  # bar/second
    severity: CRITICAL
```

## Performance Requirements

- **Latency**: <100 ms per message (including ML inference)
- **Throughput**: 10k messages/second per detector
- **False Positive Rate**: <1% (tunable per detector)
- **False Negative Rate**: <0.1% for critical anomalies

## Model Management

### Training Data
- Historical "normal" operation data (no known faults)
- Labeled anomaly data (from maintenance logs, NCRs)
- Synthetic anomalies (injected for testing)

### Model Versioning
- Models versioned in `../../05-DATA_PRODUCTS/ANOMALY_REPORTS/`
- Semantic versioning (major.minor.patch)
- A/B testing before production deployment

### Retraining
- **Scheduled**: Monthly retraining with latest data
- **Triggered**: When false positive rate exceeds threshold
- **Process**: Train → validate → canary deploy → full rollout

## Anomaly Output Format

```json
{
  "timestamp": 1704067200000,
  "platform_id": "AC-H2-001",
  "signal_name": "h2_tank_pressure_fwd",
  "value": 385.7,
  "anomaly_detected": true,
  "anomaly_type": "out_of_range",
  "severity": "HIGH",
  "confidence": 0.95,
  "detector": "3_sigma_v1.0",
  "context": {
    "expected_range": [0, 350],
    "deviation": 35.7,
    "recent_trend": "increasing"
  }
}
```

## Integration with Downstream Systems

### Predictive Maintenance
- Anomalies forwarded to `../../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/`
- Anomaly patterns correlated with maintenance events
- RUL models trained on anomaly frequency

### Digital Twin
- Anomalies used to tune digital twin parameters
- Physics-based models updated with real-world discrepancies

### Federated Learning
- Anomaly labels used as training data
- Privacy-preserving anomaly detection models

## Monitoring

**Key Metrics:**
- Anomaly detection rate (anomalies/hour)
- False positive rate (operator-confirmed)
- Detection latency (time from occurrence to detection)
- Detector coverage (signals monitored)

**Alerts:**
- Critical anomaly detected
- False positive rate >5%
- Detector down >5 minutes

## Related Documents

- **DATA_VALIDATION_RULES.md** - Validation rules
- **../05-DATA_PRODUCTS/ANOMALY_REPORTS/** - Anomaly report format
- **../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/** - Maintenance integration

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial anomaly detection specs | Data Engineering Team |
