# Risk Assessment Template

**Model/System**: [Name]  
**Version**: [Version]  
**UTCS ID**: [UTCS-XXX]  
**Date**: YYYY-MM-DD  
**Assessor**: [Risk Assessor Name]

---

## 1. System Overview

### Description
[Brief description of the ML system and its purpose]

### Operational Context
- **Deployment Environment**: [Where the system operates]
- **User Population**: [Who uses the system]
- **Criticality**: [Safety-critical, mission-critical, non-critical]
- **Human Oversight**: [Level of human supervision]

---

## 2. Hazard Identification

### Hazards
List all identified hazards associated with the ML system:

| Hazard ID | Description | Triggering Condition | Potential Harm |
|-----------|-------------|---------------------|----------------|
| HAZ-001 | [Description] | [Condition] | [Harm] |
| HAZ-002 | [Description] | [Condition] | [Harm] |

**Hazard Analysis**: [Link to detailed hazard analysis]

---

## 3. Risk Assessment

### Risk Matrix
For each identified hazard:

| Hazard ID | Likelihood | Severity | Risk Level | Acceptability |
|-----------|-----------|----------|------------|---------------|
| HAZ-001 | Rare/Unlikely/Possible/Likely/Certain | Negligible/Minor/Moderate/Major/Catastrophic | Low/Medium/High/Critical | Acceptable/ALARP/Unacceptable |

### Risk Scoring
- **Likelihood Scale**: 
  - Rare (1), Unlikely (2), Possible (3), Likely (4), Certain (5)
- **Severity Scale**: 
  - Negligible (1), Minor (2), Moderate (3), Major (4), Catastrophic (5)
- **Risk Level**: Likelihood × Severity
  - Low (1-4), Medium (5-9), High (10-15), Critical (16-25)

---

## 4. Failure Modes

### Model Failure Modes
| Failure Mode | Description | Detection Method | Impact |
|--------------|-------------|-----------------|--------|
| False Positive | [Description] | [How detected] | [Impact] |
| False Negative | [Description] | [How detected] | [Impact] |
| Overconfidence | [Description] | [How detected] | [Impact] |
| Drift/Degradation | [Description] | [How detected] | [Impact] |

---

## 5. Misuse Scenarios

### Intentional Misuse
- [Misuse scenario 1]: [Potential harm]
- [Misuse scenario 2]: [Potential harm]

### Unintentional Misuse
- [Misuse scenario 1]: [Potential harm]
- [Misuse scenario 2]: [Potential harm]

**Red Team Report**: [Link to red_team/ documentation]

---

## 6. Ethical Risks

### Fairness Risks
- [Risk 1]: [Description and affected groups]
- [Risk 2]: [Description and affected groups]

### Privacy Risks
- [Risk 1]: [Description]
- [Risk 2]: [Description]

**DPIA Reference**: [Link if applicable]

### Transparency Risks
- [Risk 1]: [Description]
- [Risk 2]: [Description]

---

## 7. Mitigations

### Existing Controls
| Hazard/Risk | Mitigation | Type | Effectiveness |
|-------------|-----------|------|---------------|
| HAZ-001 | [Mitigation] | Preventive/Detective/Corrective | [Assessment] |

### Mitigation Types
- **Preventive**: Prevent the risk from occurring
- **Detective**: Detect when risk is occurring
- **Corrective**: Reduce impact after occurrence

---

## 8. Safety Interlocks

### Rate Limits
- **Query Rate Limit**: [Limit to prevent abuse]
- **Update Rate Limit**: [Limit for model updates]

### Safewords/Kill Switches
- **Kill Switch Criteria**: [When to activate]
- **Kill Switch Owner**: [Role responsible]
- **Activation Procedure**: [Steps to activate]

**Kill Switch Runbook**: [Link to runbook]

### Human Escalation
- **Escalation Triggers**: [Conditions requiring human intervention]
- **Escalation Path**: [Who gets notified and in what order]
- **Response Time**: [Expected response time]

---

## 9. Monitoring and Detection

### Performance Monitoring
- **Metrics Tracked**: [List of metrics]
- **Monitoring Frequency**: [How often]
- **Alert Thresholds**: [When alerts are triggered]

### Anomaly Detection
- **Anomaly Indicators**: [What indicates an anomaly]
- **Detection Method**: [How anomalies are detected]
- **Response Procedure**: [What happens when anomaly detected]

### Incident Logging
- **Logging Level**: [What is logged]
- **Log Retention**: [How long logs are kept]
- **Log Review**: [Who reviews logs and how often]

---

## 10. Residual Risk

### Accepted Risks
After mitigations, list residual risks:

| Risk ID | Residual Likelihood | Residual Severity | Residual Risk Level | Justification for Acceptance |
|---------|-------------------|------------------|-------------------|----------------------------|
| RES-001 | [Level] | [Level] | [Level] | [Why this risk is acceptable] |

### ALARP Justification
For risks in the "As Low As Reasonably Practicable" (ALARP) region:

[Provide justification that further risk reduction is not reasonably practicable]

---

## 11. Safety Case Linkage

**Safety Case**: [Link to safety_case/ documentation]

### Safety Claims
- Claim 1: [The system is adequately safe for...]
- Claim 2: [Hazards are mitigated to acceptable levels]

### Evidence
- [Evidence 1]: [Link]
- [Evidence 2]: [Link]

---

## 12. Compliance

### Standards
- [ ] ISO 14971 - Medical Device Risk Management
- [ ] ARP4754A - Safety Assessment Process
- [ ] MAL-EEM Risk Assessment Requirements
- [ ] Other: [Specify]

### Regulatory Requirements
[List applicable regulatory requirements and compliance status]

---

## 13. Review and Updates

### Review Schedule
**Review Frequency**: [How often risk assessment is reviewed]

**Next Review Date**: YYYY-MM-DD

### Update Triggers
Risk assessment should be updated when:
- [ ] New hazards identified
- [ ] Operational context changes
- [ ] Model updated or retrained
- [ ] Incident occurs
- [ ] Regulatory requirements change

---

## 14. Approvals

**Risk Assessor**: [Name, Date]  
**Safety Lead**: [Name, Date]  
**ML Lead**: [Name, Date]  
**CCB**: [Name, Date]

**Decision Record**: Store in `REVIEW_BOARDS/SAFETY/decisions/`

---

## Attachments

- [Detailed hazard analysis]
- [FMEA/FMECA]
- [Fault tree analysis]
- [Red team reports]
