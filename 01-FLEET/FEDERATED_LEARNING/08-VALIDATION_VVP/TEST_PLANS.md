# TEST_PLANS

FL model test plans from lab to rig to flight (DO-160, ECSS-E-ST-10).

## Test Phases

### Phase 1: Lab Testing

- **Unit tests**: Model components (input preprocessing, inference)
- **Integration tests**: FL client + aggregation server
- **Coverage**: 90%+ code coverage

### Phase 2: Rig Testing (HIL/SIL)

- **Hardware-in-Loop (HIL)**: Real avionics hardware, simulated environment
- **Software-in-Loop (SIL)**: Fully simulated
- **Test scenarios**: Nominal + failure modes

### Phase 3: Flight Testing

- **Canary deployment**: 5 aircraft, 2-4 weeks
- **Monitoring**: Real-time performance, safety metrics
- **Rollback criteria**: See ../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md

## Compliance

- **DO-160**: Environmental qualification (temperature, vibration, EMI)
- **ECSS-E-ST-10**: Space segment testing (for satellite FL clients)

## Related Documents

- **SAFETY_GATES.md** - Pass/fail criteria
- **../07-EXPERIMENTS/SHADOW_DEPLOYMENTS/** - Shadow mode testing
