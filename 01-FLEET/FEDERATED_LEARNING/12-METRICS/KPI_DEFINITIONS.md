# KPI_DEFINITIONS

FL key performance indicator (KPI) definitions and targets.

## System Health KPIs

### Client Participation Rate

**Definition**: % of eligible clients that contributed to training round

```
participation_rate = (num_clients_contributed / num_clients_selected) * 100
```

**Target**: ≥ 80%  
**Warning**: < 70%  
**Critical**: < 50%

### Round Completion Time

**Definition**: Duration from model distribution to new global model ready

**Target**: ≤ 7 days (weekly cadence)  
**Warning**: > 8 days  
**Critical**: > 10 days

### Aggregation Latency

**Definition**: Server-side aggregation time

**Target**: ≤ 30 minutes  
**Warning**: > 45 minutes  
**Critical**: > 60 minutes

## Training Performance KPIs

### Global Loss

**Definition**: Aggregated training loss across clients

**Target**: Decreasing trend (convergence)  
**Warning**: Plateau for > 5 rounds  
**Critical**: Increasing trend (divergence)

### Validation Accuracy (AUC)

**Definition**: Area Under ROC Curve on holdout dataset

**Target**: ≥ 0.90  
**Warning**: < 0.85  
**Critical**: < 0.80

### Privacy Budget (ε)

**Definition**: Cumulative privacy loss

**Target**: ≤ 1.0 (strong privacy)  
**Warning**: > 2.0  
**Critical**: > 5.0

## Inference Performance KPIs

### Inference Latency (p95)

**Definition**: 95th percentile inference time

**Target**: ≤ 500 ms  
**Warning**: > 750 ms  
**Critical**: > 1000 ms

### CPU Usage (Aircraft Edge)

**Definition**: % of CPU used by FL client

**Target**: ≤ 30%  
**Warning**: > 50%  
**Critical**: > 70%

## Drift Detection KPIs

### PSI (Population Stability Index)

**Definition**: Distribution shift metric

**Target**: < 0.1 (no drift)  
**Warning**: 0.1 - 0.2 (minor drift)  
**Critical**: > 0.2 (significant drift)

### Concept Drift (Accuracy Drop)

**Definition**: % accuracy degradation vs. baseline

**Target**: < 5%  
**Warning**: 5% - 10%  
**Critical**: > 10%

## Related Documents

- **TRAINING_METRICS.csv** - Training metric logs
- **INFERENCE_METRICS.csv** - Inference metric logs
- **DRIFT_ALERTS.csv** - Drift event logs
