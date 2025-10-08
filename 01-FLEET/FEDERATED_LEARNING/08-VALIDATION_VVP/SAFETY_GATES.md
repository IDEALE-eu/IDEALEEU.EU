# SAFETY_GATES

Safety gate criteria for FL model deployment (NO autotuning on flight-critical systems).

## Critical Safety Constraints

⚠️ **MANDATORY RESTRICTIONS:**

1. **NO autotuning on flight-critical systems**: FL models are advisory only
2. **Human-in-the-loop**: All model updates require CCB approval
3. **Sandboxing**: ARINC 653 partitioning enforced (see [../03-CLIENTS/AIRCRAFT_EDGE/SANDBOXING.md](../03-CLIENTS/AIRCRAFT_EDGE/SANDBOXING.md))
4. **Rollback capability**: Immediate reversion on drift or safety alert
5. **Resource limits**: CPU%, power, thermal constraints strictly enforced

## Safety Gate Checklist

- [ ] **Functional correctness**: Model passes all test cases (95%+ accuracy on validation set)
- [ ] **No flight-critical interference**: FL client does not impact flight control systems
- [ ] **Resource compliance**: CPU, memory, disk, network within limits
- [ ] **Drift detection**: Monitoring enabled, thresholds configured
- [ ] **Rollback tested**: Rollback procedure validated
- [ ] **Audit trail**: Immutable logs enabled
- [ ] **CCB approval**: Configuration Control Board sign-off

## Related Documents

- [**../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md**](../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md) - Rollback procedures
- [**../10-GOVERNANCE/CCB_HANDOFF.md**](../10-GOVERNANCE/CCB_HANDOFF.md) - CCB approval process
