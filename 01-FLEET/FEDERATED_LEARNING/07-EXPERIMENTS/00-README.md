# 07-EXPERIMENTS

Experiment tracking, A/B testing, and shadow deployments for FL.

## Purpose

Track FL experiments, conduct A/B tests, and validate models in shadow mode (inference without actuation).

## Contents

- **00-README.md** - This file
- **TRACKING.md** - MLflow/W&B integration notes
- **AB_TESTS/** - A/B test specifications
- **SHADOW_DEPLOYMENTS/** - Parallel inference without actuation

## Experiment Lifecycle

1. **Design**: Define hypothesis, metrics, success criteria
2. **Approval**: MAL-FE (Fleet Experiments) policy
3. **Execution**: Run experiment, collect metrics
4. **Analysis**: Statistical significance testing
5. **Decision**: Deploy, iterate, or discard

## Related Documents

- **../10-GOVERNANCE/MAL-FE/POLICY.md** - Experiment approval process
- **TRACKING.md** - Experiment tracking tools
