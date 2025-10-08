# ROLLBACK_PROCEDURE

Auto-rollback procedures triggered by drift detection or safety alerts.

## Rollback Triggers

### Automatic Triggers

- **Drift alert**: PSI > 0.3 (significant drift)
- **Accuracy drop**: > 15% degradation on validation set
- **Resource violation**: CPU > 80%, memory > 90%
- **Safety alert**: Flight-critical system interference detected

### Manual Triggers

- **CCB decision**: Configuration Control Board veto
- **Safety engineering**: Safety engineer escalation
- **Incident response**: Security or safety incident (see ../16-INCIDENT_RESPONSE/)

## Rollback Process

1. **Detection**: Automated monitoring detects trigger condition
2. **Alert**: PagerDuty, Slack, Email to on-call team
3. **Rollback**: Revert to previous model version (n-1)
4. **Validation**: Verify rollback successful (KPIs restored)
5. **Postmortem**: Blameless postmortem (see ../16-INCIDENT_RESPONSE/POSTMORTEMS/)

## Rollback Timeline

- **Detection to alert**: < 5 minutes
- **Alert to rollback initiated**: < 10 minutes
- **Rollback to validation**: < 30 minutes
- **Total**: < 45 minutes (target)

## Rollback Validation

- [ ] Previous model version deployed to all clients
- [ ] KPIs returned to baseline
- [ ] No drift alerts
- [ ] No safety incidents

## Related Documents

- **../04-ALGORITHMS/DRIFT_DETECTION.md** - Drift detection methods
- **../16-INCIDENT_RESPONSE/RUNBOOK.md** - Incident response runbook
