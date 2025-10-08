# ROLLOUT_STRATEGY

Ring/canary deployment strategy for FL models by tail number or orbit plane.

## Deployment Phases

### Phase 1: Canary (5 Aircraft, 24-48 Hours)

- **Purpose**: Detect critical issues before full rollout
- **Aircraft selection**: Diverse fleet (different types, ages, routes)
- **Monitoring**: Real-time performance, drift alerts
- **Rollback**: Auto-rollback if KPI violation

### Phase 2: Ring 1 (10%, 2-3 Days)

- **Purpose**: Expand to 10% of fleet
- **Selection**: Random sampling, stratified by aircraft type

### Phase 3: Ring 2 (25%, 3-4 Days)

- **Purpose**: Quarter of fleet

### Phase 4: Ring 3 (50%, 3-4 Days)

- **Purpose**: Half of fleet

### Phase 5: Full Rollout (100%)

- **Purpose**: Complete deployment
- **Duration**: Indefinite (until next model version)

## Rollback Triggers

- **Drift detected**: PSI > 0.3
- **Accuracy drop**: > 10% degradation
- **Resource violation**: CPU, memory, disk exceed limits
- **Safety alert**: Critical system failure

## Related Documents

- [**CANARY_ROLLOUTS.md**](CANARY_ROLLOUTS.md) - Canary phase details
- [**ROLLBACK_PROCEDURE.md**](ROLLBACK_PROCEDURE.md) - Rollback procedures
