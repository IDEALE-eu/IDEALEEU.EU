# Data Protection Impact Assessment (DPIA) Checklist

**Project/System**: [Name]  
**UTCS ID**: [UTCS-XXX]  
**Assessment Date**: YYYY-MM-DD  
**Assessor**: [Name, Role]  
**DPO Review**: [Name, Date]

---

## 1. Purpose and Legal Basis

- [ ] Purpose of data processing clearly documented
- [ ] Legal basis identified (consent, contract, legitimate interest, legal obligation, etc.)
- [ ] Purpose limitation validated (no mission creep)
- [ ] Data processing necessity justified

**Notes**:
[Describe the purpose and legal basis for data processing]

---

## 2. Data Inventory and Flows

- [ ] All personal data types identified and documented
- [ ] Data sources mapped (collection points)
- [ ] Data flows documented (where data goes)
- [ ] Data recipients identified (who accesses data)
- [ ] Cross-border transfers assessed (if applicable)
- [ ] Data retention periods defined

**Data Types**:
- [List personal data types: names, email addresses, biometrics, etc.]

**Data Flow Diagram**: [Link to diagram]

---

## 3. Data Minimization

- [ ] Only necessary data collected
- [ ] Proportionality verified
- [ ] Alternatives considered (pseudonymization, anonymization)
- [ ] Excessive data collection eliminated

**Minimization Measures**:
[Describe how data collection is minimized]

---

## 4. Data Subject Rights

- [ ] Access rights supported (data export)
- [ ] Rectification procedures defined
- [ ] Erasure/deletion paths implemented
- [ ] Objection mechanisms available
- [ ] Portability supported (where applicable)
- [ ] Restriction of processing defined

**Rights Implementation**: [Describe how rights are supported]

---

## 5. Security Measures

- [ ] Encryption at rest implemented
- [ ] Encryption in transit implemented
- [ ] Access controls defined and enforced
- [ ] Audit logging enabled
- [ ] Backup and recovery procedures defined
- [ ] Incident response plan in place

**Security Controls**: [List key security measures]

---

## 6. Privacy by Design

- [ ] Privacy considered from the start
- [ ] Default settings are privacy-preserving
- [ ] User consent mechanisms clear and granular
- [ ] Opt-out options available
- [ ] Data anonymization/pseudonymization used where possible

**Privacy Features**: [Describe privacy-preserving design choices]

---

## 7. Third-Party Processors

- [ ] All processors identified
- [ ] Data Processing Agreements (DPAs) in place
- [ ] Processor security assessed
- [ ] Sub-processors documented
- [ ] Transfer mechanisms compliant (SCCs, etc.)

**Processors**:
- [List third-party processors and their roles]

---

## 8. Retention and Deletion

- [ ] Retention periods defined per data type
- [ ] Retention policy ≤ regulatory/policy limits
- [ ] Automated deletion procedures implemented
- [ ] Manual deletion requests supported
- [ ] Deletion verification process defined

**Retention Schedule**:
| Data Type | Retention Period | Deletion Method |
|-----------|-----------------|----------------|
| [Type] | [Period] | [Method] |

---

## 9. Data Breach Procedures

- [ ] Breach detection mechanisms in place
- [ ] Breach notification procedures defined
- [ ] DPO notification process clear
- [ ] Authority notification (72 hours) procedure ready
- [ ] Data subject notification process defined

**Breach Response Plan**: [Link to incident response documentation]

---

## 10. Risk Assessment

### Identified Risks

| Risk | Likelihood | Impact | Mitigation | Residual Risk |
|------|-----------|--------|------------|--------------|
| [Risk description] | Low/Med/High | Low/Med/High | [Mitigation measures] | Low/Med/High |

---

## 11. Consultation and Approval

- [ ] Stakeholders consulted
- [ ] Data subjects consulted (if applicable)
- [ ] Legal review completed
- [ ] DPO approval obtained

**Consultations**:
- [List consultations performed]

---

## 12. DPO Sign-Off

**DPO Name**: [Name]  
**Date**: YYYY-MM-DD  
**Approval Status**: [ ] Approved [ ] Conditional [ ] Rejected

**DPO Comments**:
[Any comments or conditions]

**Decision Record**: Store in `REVIEW_BOARDS/DATA_PROTECTION/decisions/`

---

## Attachments

- [Link to data flow diagrams]
- [Link to security documentation]
- [Link to privacy policy]
- [Link to data processing agreements]
