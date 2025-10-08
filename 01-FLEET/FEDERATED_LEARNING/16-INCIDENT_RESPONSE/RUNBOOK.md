# RUNBOOK

Incident response runbook: Detection → Containment → Communication → Rollback.

## Incident Detection

### Automated Detection

- **Drift alerts**: PSI > 0.3 (see [../../04-ALGORITHMS/DRIFT_DETECTION.md](../../04-ALGORITHMS/DRIFT_DETECTION.md))
- **Performance degradation**: Accuracy drop > 10%
- **Resource violations**: CPU, memory, disk exceed limits
- **Security alerts**: IDS/IPS, anomalous traffic

### Manual Detection

- **User reports**: Fleet operators, pilots
- **Health checks**: Periodic manual review

## Incident Containment

### Step 1: Assess Severity

- **Low**: Monitoring only, no immediate action
- **Medium**: Investigate, prepare rollback
- **High**: Immediate rollback, isolate affected clients
- **Critical**: Emergency rollback, all clients, CCB notification

### Step 2: Isolate Affected Systems

- **Blacklist clients**: Remove malicious clients from training (see [../../02-ORCHESTRATION/CLIENT_SELECTION.md](../../02-ORCHESTRATION/CLIENT_SELECTION.md))
- **Disable model**: Suspend FL client inference on affected aircraft
- **Quarantine data**: Isolate corrupted gradients or telemetry

## Communication

### Incident Commander

- **On-call rotation**: AI/ML Team (primary), Fleet Operations (secondary)
- **Escalation**: PagerDuty, Slack #fl-incidents, Email to leadership

### Stakeholder Notifications

| Severity | Stakeholders to Notify                          | Timeline     |
|----------|------------------------------------------------|--------------|
| Low      | AI/ML Team (Slack)                             | Within 1 hour|
| Medium   | AI/ML Team, Fleet Operations (Slack, Email)    | Within 30 min|
| High     | Above + Safety Engineering, CCB (PagerDuty)    | Immediate    |
| Critical | Above + Executive Leadership, DPO, Regulators  | Immediate    |

### Communication Templates

**Slack Alert:**
```
🚨 FL INCIDENT: {severity}
Summary: {1-sentence description}
Impact: {affected systems, users}
Status: {investigating|contained|resolved}
IC: {Incident Commander name}
Thread: {link to incident tracking}
```

**Email:**
```
Subject: [FL INCIDENT - {severity}] {Brief summary}

Incident ID: {INC-YYYY-XXX}
Detection Time: {YYYY-MM-DD HH:MM:SS UTC}
Severity: {Low|Medium|High|Critical}
Status: {Open|Investigating|Resolved}

Summary:
{Brief description of incident}

Impact:
- {Affected systems}
- {Affected users}
- {Safety impact}

Current Actions:
1. {Action 1}
2. {Action 2}

Next Steps:
1. {Next step 1}
2. {Next step 2}

Incident Commander: {Name}
```

## Rollback Procedure

See **../../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md** for detailed rollback steps.

### Rollback Timeline

- **Detection to alert**: < 5 minutes
- **Alert to rollback initiated**: < 10 minutes
- **Rollback to validation**: < 30 minutes
- **Total**: < 45 minutes (target)

## Investigation

### Root Cause Analysis

- **Timeline reconstruction**: What happened, when, why?
- **Data collection**: Logs, metrics, audit trail
- **Contributing factors**: Why did monitoring/gates fail?
- **Root cause**: Underlying systemic issue

### Documentation

- **Incident report**: Use ../../15-TEMPLATES/INCIDENT_REPORT_TEMPLATE.md
- **Postmortem**: Blameless, action-oriented (see POSTMORTEMS/)
- **Audit logs**: Immutable logs for regulators (see AUDIT_LOGS/)

## Post-Incident Actions

1. **Postmortem meeting**: Within 1 week, all stakeholders
2. **Action items**: Assign owners, deadlines
3. **Follow-up**: Track action items to completion
4. **Lessons learned**: Update runbooks, gates, monitoring

## Related Documents

- [**../../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md**](../../09-DEPLOYMENT/ROLLBACK_PROCEDURE.md) - Rollback procedures
- [**../../15-TEMPLATES/INCIDENT_REPORT_TEMPLATE.md**](../../15-TEMPLATES/INCIDENT_REPORT_TEMPLATE.md) - Incident report template
- [**POSTMORTEMS/**](POSTMORTEMS/) -  Postmortem reports
