# 09-DEPLOYMENT

FL model deployment strategies, rollout procedures, and changelogs.

## Purpose

Define how FL models are deployed to production, including canary rollouts, progressive deployment, rollback procedures, and version control.

## Contents

- **00-README.md** - This file
- **ROLLOUT_STRATEGY.md** - Ring/canary deployment by tail number or orbit plane
- **CANARY_ROLLOUTS.md** - Monitor KPIs before full fleet push
- **ROLLBACK_PROCEDURE.md** - Auto-trigger on drift or safety alert
- **CHANGELOG.md** - Semantic versioning (v1.2.0-fl)

## Deployment Workflow

1. **Approval**: CCB approval (see ../10-GOVERNANCE/CCB_HANDOFF.md)
2. **Canary**: Deploy to 5 aircraft, monitor 24h
3. **Progressive**: 10% → 25% → 50% → 100% over 7-14 days
4. **Monitoring**: Real-time drift detection, performance tracking
5. **Rollback**: Auto-rollback if safety gate violated

## Related Documents

- **ROLLOUT_STRATEGY.md** - Deployment phases
- **ROLLBACK_PROCEDURE.md** - Rollback triggers and procedures
- **../10-GOVERNANCE/CCB_HANDOFF.md** - Approval process
