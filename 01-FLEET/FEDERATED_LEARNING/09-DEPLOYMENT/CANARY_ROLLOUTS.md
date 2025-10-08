# CANARY_ROLLOUTS

Canary deployment phase with KPI monitoring before full fleet rollout.

## Canary Selection

- **Count**: 5 aircraft (minimum for statistical validity)
- **Diversity**: Different aircraft types, ages, routes
- **Duration**: 24-48 hours (sufficient FL rounds or inference cycles)

## KPIs Monitored

- **Model accuracy**: AUC, F1 score, false positive rate
- **Inference latency**: p50, p95, p99
- **Resource usage**: CPU, memory, disk, network
- **Drift metrics**: PSI, KS test p-value
- **Safety**: No flight-critical system interference

## Success Criteria

- [ ] Accuracy ≥ baseline model (no regression)
- [ ] Latency p95 < 500 ms
- [ ] Resource usage within constraints (see [../03-CLIENTS/AIRCRAFT_EDGE/RUNTIME_CONSTRAINTS.md](../03-CLIENTS/AIRCRAFT_EDGE/RUNTIME_CONSTRAINTS.md))
- [ ] No drift alerts (PSI < 0.2)
- [ ] No safety incidents

## Rollback Criteria

- Any KPI threshold violated
- Safety alert triggered
- CCB veto

## Related Documents

- [**ROLLOUT_STRATEGY.md**](ROLLOUT_STRATEGY.md) - Full rollout phases
- [**ROLLBACK_PROCEDURE.md**](ROLLBACK_PROCEDURE.md) - Rollback procedures
