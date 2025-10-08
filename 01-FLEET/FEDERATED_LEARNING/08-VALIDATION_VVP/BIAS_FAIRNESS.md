# BIAS_FAIRNESS

Disaggregated model performance analysis by fleet segment for fairness assessment.

## Fairness Metrics

### Disaggregated Performance

Evaluate model performance across:
- **Aircraft type**: Airbus A320, Boeing 737, Embraer E-Jet
- **Aircraft age**: New (< 5 years), mid-life (5-15 years), legacy (> 15 years)
- **Flight phase**: Short-haul, medium-haul, long-haul
- **Region**: Europe, Americas, Asia-Pacific

### Fairness Threshold

- **Max performance gap**: 10% (e.g., AUC difference < 0.10)
- **Action if exceeded**: Retrain with fairness constraints (e.g., Fairness Constraints in FedAvg)

## Mitigation Strategies

- **Stratified sampling**: Ensure diverse client participation (see ../02-ORCHESTRATION/CLIENT_SELECTION.md)
- **Fairness-aware aggregation**: Weight clients to balance performance
- **Data augmentation**: Synthetic data for underrepresented groups

## Related Documents

- **../02-ORCHESTRATION/CLIENT_SELECTION.md** - Fairness policies
- **../04-ALGORITHMS/FEDAVG.md** - Aggregation weights
