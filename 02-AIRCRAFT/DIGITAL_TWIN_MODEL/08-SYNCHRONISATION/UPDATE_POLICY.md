# UPDATE_POLICY

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 08-SYNCHRONISATION > UPDATE_POLICY**

Ring deployment, rollback, canary (linked to federated learning).

## Purpose

Define systematic policy for updating digital twin models in production fleet.

## Update Types

### 1. Major Updates
**Definition**: Breaking changes, new physics, major algorithm changes

**Examples**:
- New aerodynamic model (CFD surrogate → neural network)
- Structural model update (linear → nonlinear)
- New behavioral model (added state machine)

**Process**:
- Full V&V cycle (see `../06-VALIDATION_VERIFICATION/VVP_PLAN.md`)
- CCB approval mandatory
- New baseline release (see `../04-VERSIONING_CONFIG/`)
- Minimum 3-month validation period

### 2. Minor Updates
**Definition**: Parameter tuning, bug fixes, non-breaking changes

**Examples**:
- Calibration parameter update (CD0 correction)
- Bug fix (memory leak, numerical stability)
- Performance optimization (faster inference)

**Process**:
- Regression testing against validation test suite
- Technical Lead approval
- Patch version increment (e.g., v1.0.0 → v1.0.1)
- Minimum 1-month validation period

### 3. Data-Driven Model Updates
**Definition**: ML model retraining (new data, drift detected)

**Examples**:
- Anomaly detector retraining (new failure modes)
- Surrogate model update (expanded training set)

**Process**:
- Drift detection triggers retraining (see `DRIFT_DETECTION.md`)
- Shadow mode deployment (30 days minimum)
- A/B testing with statistical significance (p<0.05)
- Model Card update required (see `../13-TEMPLATES/MODEL_CARD_TEMPLATE.md`)

## Deployment Rings

### Ring 0: Lab/HIL Rigs
**Purpose**: Initial validation, smoke testing

**Duration**: 1-2 weeks

**Environment**: HIL/SIL rigs (see `../05-CALIBRATION_ALIGNMENT/DATASETS/LAB_RIG/`)

**Acceptance**: All smoke tests pass, no regressions

### Ring 1: Single Test Aircraft
**Purpose**: Flight validation, real-world data

**Duration**: 2-4 weeks

**Aircraft**: Dedicated test aircraft (e.g., ACFT-999)

**Acceptance**:
- Model accuracy within spec (see `../06-VALIDATION_VERIFICATION/VVP_PLAN.md`)
- No safety violations (see `../07-RUNTIME_DEPLOYMENT/SAFETY_GUARDS.md`)
- Flight test engineer sign-off

### Ring 2: 10% of Fleet (Canary)
**Purpose**: Limited production exposure, monitor for issues

**Duration**: 4-8 weeks

**Selection**: Diverse aircraft (different operators, routes, configurations)

**Monitoring**:
- Model health metrics (see `../10-METRICS/MODEL_HEALTH.csv`)
- Prediction quality (see `../10-METRICS/PREDICTION_QUALITY.csv`)
- User feedback (pilots, maintenance crews)

**Acceptance**:
- Error rate <1% (vs. baseline)
- No critical incidents
- Positive user feedback (>80% satisfaction)

### Ring 3: Full Fleet
**Purpose**: General availability

**Duration**: Ongoing

**Deployment**: Phased rollout (10% per week)

**Monitoring**: Continuous monitoring, automated rollback if issues detected

## Deployment Workflow

```
1. [Model Development] → New model version (v1.1.0)
2. [V&V] → Validation (see ../06-VALIDATION_VERIFICATION/)
3. [Signing] → GPG sign model (see ../07-RUNTIME_DEPLOYMENT/CYBERSECURITY.md)
4. [Ring 0: Lab] → HIL/SIL testing (1-2 weeks)
5. [Ring 1: Test Aircraft] → Flight validation (2-4 weeks)
6. [Ring 2: Canary (10%)] → Limited production (4-8 weeks)
7. [Ring 3: Full Fleet] → Phased rollout (10% per week)
8. [Monitoring] → Continuous monitoring (see ../10-METRICS/)
9. [Rollback if Needed] → Automated or manual rollback
```

## Rollback Policy

### Rollback Triggers

**Automatic Rollback**:
- Error budget exceeded (>5% prediction error vs. baseline)
- CPU usage >20% sustained (edge deployment)
- Crash/hang detected (>3 instances in 1 hour)
- Safety violation (see `../07-RUNTIME_DEPLOYMENT/SAFETY_GUARDS.md`)

**Manual Rollback**:
- Digital Twin Lead or Safety Engineer decision
- Critical incident (e.g., undetected anomaly led to issue)
- User feedback (pilots, maintenance crews report problems)

### Rollback Process

1. **Initiate Rollback**: Automated or manual trigger
2. **Revert to Last Known-Good**: Load previous model version (e.g., v1.0.0)
3. **Verify Stability**: Confirm previous version works (smoke tests)
4. **Root Cause Analysis**: Investigate what went wrong
5. **Fix + Retest**: Fix issue, re-validate before re-deploying
6. **Post-Incident Review**: Document lessons learned

**RTO (Recovery Time Objective)**: 4 hours for ground, N/A for edge (local rollback)

## Federated Learning Integration

**Link**: `01-FLEET/FEDERATED_LEARNING/` (future capability)

**Concept**: Train models on distributed fleet data without centralizing sensitive data

**Benefits**:
- Privacy-preserving (data stays on aircraft)
- Faster model adaptation (learn from entire fleet)
- Reduced bandwidth (only model updates transmitted, not raw data)

**Integration with Update Policy**:
- Federated learning used for continuous model improvement
- Periodic aggregation of local updates (e.g., weekly)
- Aggregated model pushed via ring deployment

## Change Management

### Change Request (CR)
All model updates require CR:
- **CR ID**: Unique identifier (e.g., CR-2025-001)
- **Description**: What is being changed and why
- **Impact Analysis**: Affected models, interfaces, tests
- **Risk Assessment**: Probability and severity of issues
- **Mitigation**: How risks are mitigated (e.g., canary deployment)

### CCB Approval
- **Level A/B Models**: Mandatory CCB approval
- **Level C/D Models**: Technical Lead approval sufficient

## Monitoring and Metrics

### Deployment Success Rate
- **Metric**: % of deployments that complete without rollback
- **Target**: >95%

### Rollback Rate
- **Metric**: % of deployments that trigger rollback
- **Target**: <5%

### Mean Time to Deploy (MTTD)
- **Metric**: Time from model ready to full fleet deployment
- **Target**: <12 weeks (for major updates)

## Related Documents

- **BASELINE_SYNC.md** - Baseline synchronization
- **DRIFT_DETECTION.md** - Drift detection and retraining triggers
- **../00-README.md** - Update policy summary
- **../04-VERSIONING_CONFIG/MODEL_MANIFEST.yaml** - Model versioning
- **../10-METRICS/** - Model health and prediction quality metrics
- **01-FLEET/FEDERATED_LEARNING/** - Federated learning integration (future)

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
