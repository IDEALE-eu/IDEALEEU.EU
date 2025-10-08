# DRIFT_DETECTION

Model drift detection methods and alerting policies.

## Overview

Detect when deployed FL models degrade due to data distribution changes, concept drift, or adversarial attacks.

## Methods

### PSI (Population Stability Index)

```
PSI = Σ (p_i - q_i) * ln(p_i / q_i)

where:
  p_i = expected distribution (training)
  q_i = actual distribution (inference)
```

**Thresholds**:
- PSI < 0.1: No drift
- 0.1 ≤ PSI < 0.2: Minor drift (monitor)
- PSI ≥ 0.2: Significant drift (alert, retrain)

### KS Test (Kolmogorov-Smirnov)

- Statistical test for distribution differences
- **p-value < 0.05**: Reject null hypothesis (drift detected)

### Concept Drift

- Monitor model accuracy over time
- **Accuracy drop > 10%**: Concept drift suspected

## Detection Schedule

- **Real-time**: Every inference (lightweight PSI)
- **Hourly**: Full PSI, KS test on batch
- **Daily**: Accuracy trends, concept drift analysis

## Alerting

- **Minor drift**: Log to 12-METRICS/DRIFT_ALERTS.csv
- **Significant drift**: Slack alert, email to AI/ML Team
- **Critical drift**: Auto-rollback to previous model (see [../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md](../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md))

## Related Documents

- [**../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md**](../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md) - Auto-rollback on drift
- **../12-METRICS/DRIFT_ALERTS.csv** - Drift event logs
