# Global Regulatory Compliance Matrix

## Overview

This matrix provides a quick reference for regulatory compliance requirements across major worldwide regions, with focus on data protection, AI governance, and sector-specific considerations for IDEALEEU.EU operations.

Last Updated: January 2025

## Regional Data Protection Comparison

| Region | Primary Law | Consent Model | DPO Required | DPIA Required | Breach Notification | Max Penalties | Extraterritorial | Adequacy with EU |
|--------|-------------|---------------|--------------|---------------|---------------------|---------------|------------------|------------------|
| **EU** | GDPR (2016/679) | Opt-in | Often | High-risk | 72 hrs to authority | €20M or 4% turnover | Strong | N/A |
| **UK** | UK GDPR + DPA 2018 | Opt-in | Often | High-risk | 72 hrs to ICO | £17.5M or 4% turnover | Strong | Yes (reviewed) |
| **US** | State laws (varies) | Opt-in/out (varies) | Varies | Recommended | Varies | Varies ($7,500-$20K/violation) | Limited | No (DPF for some) |
| **China** | PIPL (2021) | Opt-in (explicit for sensitive) | Often | Often | Immediately | ¥50M or 5% revenue | Strong | No |
| **Japan** | APPI (2020 amended) | Opt-out generally | No | No | Without delay | Criminal (¥1M, 1yr) | Limited | Yes (mutual) |
| **Canada** | PIPEDA / Law 25 (Quebec) | Generally required | Recommended | Quebec: Yes | If real risk | CAD 10M or 3% (proposed) | Limited | Adequacy pending |
| **Australia** | Privacy Act 1988 | Required | No | Recommended | If serious harm | AUD 2.5M (proposed higher) | Limited | No |

## Regional AI Governance Comparison

| Region | Approach | Legal Framework | Risk Classification | High-Risk Requirements | Penalties | Status |
|--------|----------|----------------|---------------------|------------------------|-----------|--------|
| **EU** | Prescriptive, risk-based | AI Act (2024/1689) | Prohibited/High/Limited/Minimal | Extensive (conformity assessment, CE marking, registration) | €35M or 7% turnover | Enacted, phased implementation |
| **UK** | Principles-based | Sector regulators apply principles | Context-dependent | Varies by sector | Varies by sector | In effect |
| **US** | Framework-based | NIST AI RMF (voluntary) | Risk-based (voluntary) | Voluntary best practices | N/A (voluntary) | Voluntary |
| **China** | Prescriptive | Multiple laws (algorithms, deepfakes, generative AI) | Use-based | Security assessment, filing | ¥100K+ | In effect and evolving |
| **Japan** | Principles-based | AI Principles and Guidelines (voluntary) | Risk-based (voluntary) | Voluntary governance | N/A (voluntary) | Voluntary |
| **Canada** | Risk-based (proposed) | AIDA (Bill C-27, proposed) | High-impact classification | Impact assessment, mitigation | CAD 25M or 5% (proposed) | Proposed legislation |
| **Australia** | Principles-based | AI Ethics Framework (voluntary) | Context-dependent | Voluntary compliance | N/A (voluntary) | Voluntary |

## Data Protection: Key Requirements Comparison

### Consent Requirements

| Region | Standard | Sensitive Data | Withdrawal | Children |
|--------|----------|----------------|------------|----------|
| **EU** | Freely given, specific, informed, unambiguous | Explicit consent (Article 9) | Easy withdrawal | Age 16 (MS can lower to 13) |
| **UK** | Same as EU | Explicit consent | Easy withdrawal | Age 13 |
| **US** | Varies by state | Varies | Must be provided | Varies (typically 13-16) |
| **China** | Voluntary, specific, informed, unambiguous | Explicit consent | Must be provided | Under 14 (stricter) |
| **Japan** | Purpose specified, opt-out generally | Opt-in for sensitive | Must be provided | None specified |
| **Canada** | Meaningful consent | Required | Subject to legal obligations | None specified |
| **Australia** | Implied or express, reasonable expectation | Express consent | Must be provided | Enhanced protections |

### Individual Rights

| Region | Access | Correction | Erasure | Portability | Object | Automated Decisions |
|--------|--------|------------|---------|-------------|--------|---------------------|
| **EU** | Yes | Yes | Yes (with exceptions) | Yes | Yes | Yes |
| **UK** | Yes | Yes | Yes (with exceptions) | Yes | Yes | Yes |
| **US** | Varies | Varies | Some states | Some states | Some states | Some states |
| **China** | Yes | Yes | Yes | Yes | Limited | Limited |
| **Japan** | Yes | Yes | Suspension of use | No | No | No |
| **Canada** | Yes | Yes | No (implied via correction) | No | No | No |
| **Australia** | Yes | Yes | No (but can stop use) | Proposed | Proposed | Proposed |

### Cross-Border Transfers

| Region | Mechanism | Adequacy Decisions | Contractual | Other |
|--------|-----------|-------------------|-------------|-------|
| **EU** | Adequacy, SCCs, BCRs, certification, derogations | UK, Japan, Canada (commercial), others | Standard Contractual Clauses (SCCs) | BCRs, certifications, consent |
| **UK** | UK adequacy, IDTA, Addendum | EU + UK extensions | International Data Transfer Agreement | Addendum to EU SCCs |
| **US** | Varies by state | N/A | Contracts | DPF for EU transfers (limited) |
| **China** | Security assessment, certification, standard contract | None | CAC standard contract | Certification |
| **Japan** | Consent, adequacy, standards | EU (mutual recognition) | APEC CBPR | Voluntary standards |
| **Canada** | Similar protection | N/A | Contractual safeguards | Quebec: specific requirements |
| **Australia** | Reasonable steps for APP compliance | N/A | Contractual safeguards | Accountability for recipient |

## AI Governance: Detailed Comparison

### Prohibited AI Practices

| Region | Social Scoring | Subliminal Manipulation | Exploitation of Vulnerabilities | Real-Time Biometric ID | Emotion Recognition (Work/School) |
|--------|----------------|-------------------------|--------------------------------|------------------------|-----------------------------------|
| **EU** | Yes (public authorities) | Yes | Yes | Yes (narrow exceptions) | Yes (limited exceptions) |
| **UK** | Not explicitly prohibited | Not explicitly prohibited | Sector-dependent | Sector-dependent | Sector-dependent |
| **US** | Not prohibited (varies by use) | Not prohibited | Not prohibited | Varies by state/locality | Not prohibited |
| **China** | Prohibited for certain uses | Not explicitly | Not explicitly | Regulated | Regulated by sector |
| **Japan** | Not prohibited | Not prohibited | Ethics-based approach | Ethics-based approach | Ethics-based approach |
| **Canada** | Not prohibited (proposed restrictions) | Not prohibited | Not prohibited | Not prohibited | Not prohibited |
| **Australia** | Not prohibited | Not prohibited | Ethics-based approach | Ethics-based approach | Ethics-based approach |

### High-Risk AI System Requirements

| Region | Risk Assessment | Data Quality | Documentation | Logging | Human Oversight | Accuracy/Robustness | Conformity Assessment | Registration |
|--------|----------------|--------------|---------------|---------|-----------------|---------------------|-----------------------|--------------|
| **EU** | Mandatory | Mandatory | Extensive (Annex IV) | Automatic | Mandatory | Mandatory | Yes (internal or 3rd party) | Yes (EU database) |
| **UK** | Sector-dependent | Sector-dependent | Best practice | Best practice | Sector-dependent | Sector-dependent | Sector-dependent | No |
| **US** | Voluntary (NIST RMF) | Voluntary | Voluntary | Voluntary | Voluntary | Voluntary | No | No |
| **China** | For certain categories | For certain categories | For filed systems | For filed systems | For certain categories | For certain categories | Security assessment | Filing required |
| **Japan** | Voluntary | Voluntary | Voluntary | Voluntary | Voluntary | Voluntary | No | No |
| **Canada** | Proposed (high-impact) | Proposed | Proposed | Proposed | Proposed | Proposed | Proposed (assessment) | No |
| **Australia** | Voluntary | Voluntary | Voluntary | Voluntary | Voluntary | Voluntary | No | No |

### Transparency Requirements

| Region | User Notification (Chatbots) | Deepfake Labeling | AI-Generated Content | Explainability |
|--------|------------------------------|-------------------|----------------------|----------------|
| **EU** | Mandatory | Mandatory | Mandatory (detectability) | Required for high-risk |
| **UK** | Best practice | Best practice | Best practice | Sector-dependent |
| **US** | Some states require | Some states require | Emerging requirements | Voluntary |
| **China** | Required | Required | Required | Required for filed systems |
| **Japan** | Voluntary | Voluntary | Voluntary | Voluntary |
| **Canada** | Proposed | Proposed | Proposed | Proposed (high-impact) |
| **Australia** | Voluntary | Voluntary | Voluntary | Voluntary |

## Sector-Specific Considerations

### Aviation

| Region | Safety Regulator | Software Standard | AI Certification | Data Protection (Crew) | Data Protection (Passengers) | PNR Requirements |
|--------|------------------|-------------------|------------------|------------------------|--------------------------|------------------|
| **EU** | EASA | DO-178C/ED-12C | In development | GDPR (special considerations) | GDPR | EU PNR Directive |
| **UK** | CAA | DO-178C (aligned) | Aligned with EASA | UK GDPR | UK GDPR | UK PNR system |
| **US** | FAA | DO-178C | AI guidance emerging | State laws, sector-specific | State laws, PNR requirements | US PNR system |
| **China** | CAAC | AC-25 (based on FAA) | Following international | PIPL | PIPL | China requirements |
| **Japan** | JCAB | Aligned with ICAO | Following international | APPI | APPI | Japan requirements |
| **Canada** | Transport Canada | Aligned with FAA/EASA | Following international | PIPEDA / Quebec Law 25 | PIPEDA / Quebec Law 25 | Canadian PNR |
| **Australia** | CASA | Aligned with FAA/EASA | Following international | Privacy Act | Privacy Act | Australian PNR |

### Space

| Region | Space Regulator | Launch Licensing | Standards | Data Protection (Crew) | Export Control | Debris Mitigation |
|--------|----------------|------------------|-----------|------------------------|----------------|-------------------|
| **EU** | ESA + National | National authorities | ECSS | GDPR (multinational considerations) | EU Dual-Use Reg | IADC guidelines |
| **UK** | UK Space Agency | Space Industry Act 2018 | ECSS (aligned) | UK GDPR | UK export control | IADC guidelines |
| **US** | FAA/AST, NASA | 14 CFR Part 400s | NASA standards | Limited (privacy expectations) | ITAR/EAR | NASA requirements |
| **China** | CNSA | National regulations | Chinese standards | PIPL | Chinese export control | Increasing focus |
| **Japan** | JAXA | Space Activity Act | Aligned international | APPI | Japanese export control | IADC guidelines |
| **Canada** | CSA | Emerging framework | Aligned international | PIPEDA | Canadian export control | IADC guidelines |
| **Australia** | ASA | Space Act 2018 | Aligned international | Privacy Act | Australian export control | IADC guidelines |

### Defense

| Region | Export Control | Cybersecurity | Data Protection | AI Governance | National Security Exemption |
|--------|----------------|---------------|-----------------|---------------|----------------------------|
| **EU** | EU Dual-Use Reg | NIS2 + national | GDPR (exemption for national security) | AI Act (exemption for military) | Yes (GDPR Art 2(2)) |
| **UK** | UK export control | UK cyber framework | UK GDPR (exemption for national security) | UK AI (exemption principles) | Yes |
| **US** | ITAR/EAR | CMMC (DoD), NIST 800-171 | Limited (national security activities) | DoD AI Principles | Yes |
| **China** | Chinese export control | Classified | PIPL (national security exemption) | Military AI regulations | Yes |
| **Japan** | Japanese export control | National security framework | APPI (national security considerations) | Defense-specific approach | Limited |
| **Canada** | Canadian export control | National security framework | PIPEDA (national security exemption) | Defense AI ethics | Yes |
| **Australia** | Australian export control | National security framework | Privacy Act (national security exemption) | Defense AI principles | Yes |

## Compliance Priority Matrix for IDEALEEU.EU

### By Geography (Immediate Compliance Required)

1. **European Union**: 
   - GDPR (active enforcement, high penalties)
   - AI Act (phased implementation 2024-2027)
   - Sector-specific: EASA, ECSS

2. **United Kingdom**:
   - UK GDPR (similar to EU)
   - AI principles (voluntary but expected)
   - Sector-specific: CAA, UK Space Agency

3. **United States**:
   - State privacy laws (especially California)
   - NIST frameworks (voluntary but best practice)
   - Sector-specific: FAA, NASA, DoD (CMMC)

4. **China** (if operations/customers):
   - PIPL, CSL, DSL (strict enforcement)
   - Algorithm regulations
   - Data localization requirements

5. **Other Regions** (Japan, Canada, Australia):
   - If operations or significant customer base
   - Generally less stringent than EU/China
   - Voluntary AI frameworks

### By Risk Level

**Critical (Legal Obligation, High Penalties)**:
- GDPR compliance (EU/UK operations)
- Export control (ITAR/EAR, EU Dual-Use)
- Aviation safety certification (EASA, FAA)
- Cybersecurity (CMMC for DoD contracts)

**High (Regulatory Expectation, Competitive Advantage)**:
- EU AI Act compliance (high-risk systems)
- Data breach notification procedures
- AI ethics and governance framework
- Space mission assurance (ECSS)

**Medium (Best Practice, Voluntary)**:
- NIST frameworks (Privacy, AI RMF)
- ISO standards (27001, 27701, 42001)
- Industry codes of conduct
- Voluntary AI principles (non-EU)

## Implementation Recommendations

### Phase 1 (Q1 2025): Foundation
- [ ] Complete AI system inventory
- [ ] Classify all systems by EU AI Act risk levels
- [ ] Establish baseline GDPR compliance
- [ ] Export control program framework
- [ ] Cybersecurity baseline (NIST 800-171)

### Phase 2 (Q2 2025): Regional Expansion
- [ ] UK GDPR and AI principles compliance
- [ ] US state privacy law assessment
- [ ] China PIPL assessment (if applicable)
- [ ] Sector-specific certifications (EASA, NASA)

### Phase 3 (Q3 2025): AI Act Preparation
- [ ] High-risk AI conformity assessments
- [ ] Technical documentation (Annex IV)
- [ ] Risk management systems
- [ ] Human oversight implementation

### Phase 4 (Q4 2025): Certification and Registration
- [ ] CE marking for high-risk AI (if ready)
- [ ] EU database registration
- [ ] CMMC certification (US DoD)
- [ ] Ongoing monitoring systems

### Phase 5 (2026+): Continuous Compliance
- [ ] Regular audits and assessments
- [ ] Regulatory monitoring and adaptation
- [ ] Training and awareness programs
- [ ] Incident response and improvement

---

**Document Owner**: Chief Compliance Officer  
**Review Frequency**: Quarterly  
**Next Review**: 2025-04  
**Classification**: Internal Use Only

**Note**: This matrix is subject to frequent updates as regulations evolve, particularly AI governance frameworks. Always consult with legal counsel for specific compliance questions.
