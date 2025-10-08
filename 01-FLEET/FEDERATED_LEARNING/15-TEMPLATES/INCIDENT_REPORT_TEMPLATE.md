# INCIDENT_REPORT_TEMPLATE

Incident report template for FL security or safety incidents.

## Incident Metadata

- **Incident ID**: {INC-YYYY-XXX}
- **Date/Time**: {YYYY-MM-DD HH:MM:SS UTC}
- **Reporter**: {Name, Role}
- **Severity**: {Low|Medium|High|Critical}
- **Status**: {Open|Investigating|Resolved|Closed}

## Incident Summary

{Brief description of what happened, 1-2 sentences}

## Incident Details

### Detection

- **How detected**: {Automated alert, manual inspection, user report}
- **Detection time**: {YYYY-MM-DD HH:MM:SS UTC}
- **Alerting system**: {Grafana, PagerDuty, etc.}

### Impact

- **Systems affected**: {FL clients, aggregation server, etc.}
- **Users affected**: {Aircraft count, ground stations, etc.}
- **Safety impact**: {Yes/No, description}
- **Data impact**: {Data loss, corruption, breach?}

### Timeline

| Time (UTC)          | Event                                    |
|---------------------|------------------------------------------|
| YYYY-MM-DD HH:MM:SS | Incident detected                        |
| YYYY-MM-DD HH:MM:SS | On-call team notified                    |
| YYYY-MM-DD HH:MM:SS | Investigation started                    |
| YYYY-MM-DD HH:MM:SS | Root cause identified                    |
| YYYY-MM-DD HH:MM:SS | Mitigation deployed                      |
| YYYY-MM-DD HH:MM:SS | Incident resolved                        |

## Root Cause Analysis

### Immediate Cause

{What directly caused the incident?}

### Contributing Factors

1. {Factor 1}
2. {Factor 2}
3. {Factor 3}

### Root Cause

{Underlying systemic issue that allowed incident to occur}

## Mitigation Actions

### Immediate Actions (Short-term)

1. {Action 1, e.g., rollback model}
2. {Action 2, e.g., disable affected clients}
3. {Action 3, e.g., notify stakeholders}

### Long-term Actions (Preventive)

1. {Action 1, e.g., improve monitoring}
2. {Action 2, e.g., add validation gate}
3. {Action 3, e.g., update runbook}

## Lessons Learned

- **What went well**: {Things that worked during incident response}
- **What could be improved**: {Gaps in process, tools, or communication}
- **Action items**: {Specific follow-ups with owners and deadlines}

## Related Documents

- **Runbook**: {Link to ../../16-INCIDENT_RESPONSE/RUNBOOK.md}
- **Postmortem**: {Link to postmortem if conducted}
- **Audit logs**: {Link to ../../16-INCIDENT_RESPONSE/AUDIT_LOGS/}

## Sign-off

- **Incident Commander**: {Name} - {Date}
- **AI/ML Team Lead**: {Name} - {Date}
- **Safety Engineering**: {Name} - {Date} (if safety-related)
