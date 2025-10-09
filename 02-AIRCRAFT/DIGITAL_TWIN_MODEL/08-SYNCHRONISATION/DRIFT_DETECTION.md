# DRIFT_DETECTION

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 08-SYNCHRONISATION > DRIFT_DETECTION**

PSI/KS thresholds; alert if >0.25 over 7 days.

## Purpose

Detect statistical drift in data-driven models to trigger retraining or recalibration.

## Drift Types

### 1. Data Drift (Covariate Shift)
**Definition**: Input distribution changes (features shift from training distribution)

**Example**: New mission profile (high-altitude cruise) not in training data

### 2. Concept Drift
**Definition**: Relationship between inputs and outputs changes

**Example**: Engine degradation over time (fuel flow vs. thrust relationship changes)

### 3. Label Drift (Prior Shift)
**Definition**: Output distribution changes

**Example**: More anomalies detected (shift in failure rate)

## Drift Detection Methods

### Population Stability Index (PSI)

**Formula**:
```
PSI = Σ (P_actual - P_expected) * ln(P_actual / P_expected)
```

**Interpretation**:
- PSI < 0.1: No significant drift
- 0.1 ≤ PSI < 0.25: Moderate drift (monitor)
- PSI ≥ 0.25: Significant drift (retraining required)

**Implementation**:
```python
def calculate_psi(expected, actual, bins=10):
    expected_percents = np.histogram(expected, bins=bins)[0] / len(expected)
    actual_percents = np.histogram(actual, bins=bins)[0] / len(actual)
    psi = np.sum((actual_percents - expected_percents) * np.log(actual_percents / expected_percents))
    return psi
```

### Kolmogorov-Smirnov (KS) Test

**Definition**: Statistical test to compare two distributions

**Interpretation**:
- KS statistic: 0-1 (0 = identical distributions, 1 = completely different)
- p-value: <0.05 → distributions are significantly different

**Use Case**: Continuous variables (e.g., sensor readings)

### Kullback-Leibler (KL) Divergence

**Definition**: Measure of how one probability distribution diverges from another

**Interpretation**:
- KL ≥ 0 (0 = identical distributions)
- No fixed threshold (depends on application)

**Use Case**: Probability distributions (e.g., anomaly scores)

## Monitoring Strategy

### Continuous Monitoring
- **Frequency**: Daily computation of PSI/KS for all data-driven models
- **Window**: 7-day rolling window (compare last 7 days vs. training data)
- **Storage**: Time-series DB (InfluxDB) for trend analysis

### Per-Model Thresholds

| Model | Metric | Threshold | Action |
|-------|--------|-----------|--------|
| **Anomaly Detector (H₂ Leak)** | PSI | 0.25 | Retrain with recent data |
| **Surrogate (Aero)** | KS (CL) | 0.3 | Recalibrate with flight test |
| **RUL Predictor** | PSI | 0.2 | Update with maintenance records |

### Alerting

**Drift Alert Workflow**:
```
1. [Drift Detected] → PSI >0.25 for 7 consecutive days
2. [Generate Alert] → Email to data science team + ops team
3. [Impact Assessment] → Which use cases affected? Safety-critical?
4. [Retraining Plan] → Identify new training data, schedule retraining
5. [Shadow Mode Deployment] → Deploy retrained model in parallel (30 days)
6. [A/B Testing] → Compare old vs. new model (statistical significance)
7. [Full Deployment] → If new model performs better, deploy to fleet
```

## Retraining Triggers

### Automatic Triggers
- PSI >0.25 for 7 consecutive days
- KS test p-value <0.01 for 7 consecutive days
- Model accuracy drops below threshold (e.g., AUC <0.80)

### Manual Triggers
- New aircraft variant introduced
- Major system modification (e.g., engine upgrade)
- Post-incident review (e.g., undetected anomaly)

## Retraining Process

1. **Data Collection**: Gather recent operational data (see `../05-CALIBRATION_ALIGNMENT/DATASETS/`)
2. **Data Labeling**: For supervised learning, label new data (expert review)
3. **Model Retraining**: Train new model version (see `../02-MODELS/DATA_DRIVEN/`)
4. **Validation**: V&V on hold-out set (see `../06-VALIDATION_VERIFICATION/`)
5. **Shadow Mode**: Deploy in parallel with current model (30 days minimum)
6. **A/B Testing**: Statistical comparison (p<0.05 for significance)
7. **Deployment**: Ring deployment (see `../00-README.md#deployment-rings`)
8. **Update Manifest**: Update `../04-VERSIONING_CONFIG/MODEL_MANIFEST.yaml`

## Drift Visualization

### Dashboard Metrics
- **PSI Trend**: Time-series plot of PSI over last 90 days
- **Feature Drift**: Per-feature PSI (which features drifting most?)
- **Model Performance**: Accuracy, AUC, F1-score over time

### Example Plot
```
PSI Trend (Last 90 Days)
PSI
0.4 |                                    *** (Drift Alert)
    |                                 ***
0.25|                           ******
    |                      *****
0.1 |              ********
    |     *********
0.0 |_____
    +----+----+----+----+----+----+----+----+----+
       10   20   30   40   50   60   70   80   90 Days
```

## Tools

- **Python**: `scipy.stats` (KS test), custom PSI implementation
- **Evidently AI**: Open-source ML monitoring (drift detection)
- **Grafana**: Dashboards for drift visualization
- **InfluxDB**: Time-series storage for drift metrics

## Related Documents

- **UPDATE_POLICY.md** - Model update and retraining policy
- **../02-MODELS/DATA_DRIVEN/** - Data-driven model specifications
- **../10-METRICS/MODEL_HEALTH.csv** - Model health metrics

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
