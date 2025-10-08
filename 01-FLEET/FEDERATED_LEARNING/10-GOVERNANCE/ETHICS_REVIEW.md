# ETHICS_REVIEW

EU AI Act high-risk assessment and ethical review for FL systems.

## EU AI Act Compliance

### High-Risk AI System Assessment

**Annex III (High-Risk AI Systems):**
- **Safety components**: Aircraft systems (predictive maintenance, anomaly detection)
- **Assessment**: FL models are high-risk if used for safety-critical decisions

**Mitigation:**
- FL models are advisory only (no direct actuation)
- Human-in-the-loop (CCB approval required)
- Rollback capability on safety alert

### Transparency Requirements (Art. 13)

- Model cards published (see ../../06-MODELS/MODEL_CARDS/)
- Training data provenance documented (see ../../06-MODELS/DATASETS_INDEX.md)
- Performance metrics disclosed (see ../../08-VALIDATION_VVP/PERFORMANCE.md)

### Human Oversight (Art. 14)

- All model deployments require CCB approval
- Safety gates enforced (see ../../08-VALIDATION_VVP/SAFETY_GATES.md)
- Rollback authority: Safety Engineering, CCB

## Ethical Principles

### Fairness

- Disaggregated performance monitoring (see ../../08-VALIDATION_VVP/BIAS_FAIRNESS.md)
- No discrimination by aircraft type, age, or operator

### Privacy

- Differential privacy (ε ≤ 1.0)
- Pseudonymisation (GDPR Art. 4(5))
- No PII collection

### Accountability

- Immutable audit logs (see ../../16-INCIDENT_RESPONSE/AUDIT_LOGS/)
- Blameless postmortems (see ../../16-INCIDENT_RESPONSE/POSTMORTEMS/)

## Ethics Review Process

- **Trigger**: New high-risk FL use case
- **Reviewer**: DPO, Safety Engineering, AI/ML Team Lead
- **Timeline**: 2 weeks
- **Outcome**: Approved | Conditional | Rejected

## Related Documents

- **../../11-COMPLIANCE/PRIVACY.md** - GDPR compliance
- **../../08-VALIDATION_VVP/BIAS_FAIRNESS.md** - Fairness assessment
- **../../16-INCIDENT_RESPONSE/** - Accountability and audit
