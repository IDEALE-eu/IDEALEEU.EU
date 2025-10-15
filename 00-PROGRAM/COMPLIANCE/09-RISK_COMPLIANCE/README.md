---
area: "00-PROGRAM/COMPLIANCE/09-RISK_COMPLIANCE"
owner: "Risk Manager & Compliance Office"
status: "Active"
utcs_anchor: "utcs://PROGRAM/COMPLIANCE/RISK"
confidentiality: "Internal"
---

# 09-RISK_COMPLIANCE

Risk registers, compliance risk assessments, and mitigation strategies for regulatory and certification risks.

## Purpose

Identify, assess, and mitigate risks specifically related to compliance, certification, and regulatory requirements to ensure program success and avoid costly delays or failures.

## Contents

### Compliance Risk Register

Tracks risks related to:
- **Certification Delays**: Late authority approvals, finding closures
- **Standard Non-Compliance**: Gap in meeting regulatory requirements
- **Evidence Gaps**: Missing or inadequate compliance evidence
- **Regulatory Changes**: New or updated standards mid-program
- **Authority Findings**: Audit findings that could delay certification
- **Tool Qualification**: Unqualified tools used in development
- **Supplier Compliance**: Supplier unable to meet compliance requirements

### Risk Categories

#### Certification Authority Risks
- Authority resource availability
- Finding resolution disagreements
- Interpretation differences on standards
- Schedule conflicts with authority reviews

#### Technical Compliance Risks
- Design not meeting standard requirements
- Test results not demonstrating compliance
- Analysis assumptions not accepted
- Similarity arguments not accepted

#### Process Compliance Risks
- Procedures not followed consistently
- Documentation inadequate or incomplete
- Configuration control breakdowns
- Change control bypasses

#### Organizational Risks
- Key personnel turnover (loss of expertise)
- Training gaps in compliance team
- Budget constraints affecting compliance work
- Schedule pressure leading to shortcuts

#### External Risks
- Standard updates requiring rework
- New regulations affecting design
- Customer requirement changes
- Geopolitical impacts on certification

### Risk Assessment

Each risk evaluated for:
- **Probability**: Likelihood of occurrence (1-5)
- **Impact on Certification**: Schedule, cost, technical (1-5)
- **Risk Score**: Probability × Impact (1-25)
- **Detectability**: How early can it be detected (1-5)
- **Risk Priority Number**: P × I × D (1-125)

Risk levels:
- **Critical (20-25)**: Immediate action, executive attention
- **High (15-19)**: Priority mitigation, regular monitoring
- **Medium (8-14)**: Managed mitigation, periodic review
- **Low (1-7)**: Monitor, accept or mitigate opportunistically

### Risk Mitigation Strategies

#### Avoidance
- Choose lower-risk design approaches
- Use proven/certified components
- Engage authority early and often

#### Mitigation
- Develop contingency plans
- Allocate schedule buffers
- Establish backup suppliers
- Cross-train personnel

#### Transfer
- Insurance for certification delays
- Fixed-price contracts with suppliers
- Shared risk arrangements with partners

#### Acceptance
- Document risk acceptance decision
- Set aside management reserve
- Define triggers for response activation

## Risk Management Process

```
1. Risk Identification
   - Brainstorming sessions
   - Lessons learned reviews
   - Expert judgment
   - Checklists
   ↓
2. Risk Assessment
   - Probability and impact scoring
   - Risk priority calculation
   - Risk categorization
   ↓
3. Risk Response Planning
   - Mitigation strategy selection
   - Action plan development
   - Resource allocation
   - Responsibility assignment
   ↓
4. Risk Monitoring
   - Regular status reviews
   - Trigger monitoring
   - Effectiveness evaluation
   - Risk re-assessment
   ↓
5. Risk Response Execution
   - Implement mitigations
   - Track to closure
   - Document lessons learned
```

## Risk Monitoring

### Weekly Risk Reviews
Compliance team reviews:
- New risks identified
- Risk score changes
- Mitigation progress
- Risks realized (issues)

### Monthly Risk Board
Management reviews:
- Top 10 compliance risks
- Risk trend analysis
- Resource needs for mitigation
- Escalation decisions

### Quarterly Risk Deep-Dive
Executive review of:
- Program-level compliance risks
- Strategic mitigation decisions
- Risk appetite assessment
- External risk landscape

## Key Artifacts

### COMPLIANCE_RISK_REGISTER.xlsx
Master register with columns:
- Risk ID, Title, Description
- Category, Probability, Impact, Score
- Status (Open/Closed/Monitoring)
- Owner, Mitigation Plan
- Due Date, Last Review Date
- Related Requirements/Standards

### RISK_MITIGATION_PLANS/
Detailed plans for top risks:
- Risk description and impact
- Root cause analysis
- Mitigation strategy
- Action items with owners and dates
- Success criteria
- Monitoring approach

### RISK_TREND_ANALYSIS.xlsx
Monthly snapshots showing:
- Risk score trends over time
- New risks vs. closed risks
- Risk distribution by category
- Top risks by severity

### LESSONS_LEARNED_COMPLIANCE.md
Documented experiences:
- What went wrong (risks realized)
- What went right (mitigations successful)
- Recommendations for future
- Incorporation into risk checklists

## Specific Compliance Risks

### DO-178C/DO-254 Risks
- Tool qualification not completed on time
- Verification independence compromised
- Traceability gaps discovered late
- Configuration control errors

### ARP4754A/ARP4761 Risks
- Safety assessment not accepted by authority
- Hazard not properly mitigated
- Certification credit for previous analysis not granted
- FHA/PSSA/SSA inadequate

### ECSS Risks
- Tailoring not accepted by customer/ESA
- Space environment testing not completed
- Mission assurance requirements unclear
- Launch approval delayed

### AS9100/ISO 9001 Risks
- Non-conformances not resolved before audit
- Process not followed, evidence lacking
- Supplier quality issue affecting program
- Management review inadequate

### Export Control Risks
- Unintentional technology transfer
- Personnel not properly screened
- Foreign national access violations
- Controlled data not properly marked

## Risk-Based Decision Making

Compliance decisions consider:
- Risk to certification schedule
- Risk to product safety
- Risk to regulatory compliance
- Cost-benefit of mitigation
- Stakeholder risk tolerance

## Integration with Program Risk

Compliance risks roll up to:
- **Program Risk Register**: [`../../RISK_MANAGEMENT/`](../../RISK_MANAGEMENT/)
- **System Safety**: [`../../SAFETY/`](../../SAFETY/)
- **Schedule Risk**: [`../../PROJECT_MANAGEMENT/SCHEDULE/`](../../PROJECT_MANAGEMENT/SCHEDULE/)

Cross-reference ensures:
- No duplication of risks
- Consistent risk scoring
- Coordinated mitigation efforts
- Holistic risk view

## Compliance Risk Indicators (CRI)

Leading indicators of compliance risk:
- Audit findings trend (increasing)
- Evidence collection behind schedule
- Training completion rate (declining)
- Standard interpretation questions (unresolved)
- Authority responsiveness (slowing)

Lagging indicators:
- Certification milestone slips
- Non-compliance findings issued
- Rework costs (increasing)
- Schedule delays attributed to compliance

## Related Documents

- Program Risk Management: [`../../RISK_MANAGEMENT/`](../../RISK_MANAGEMENT/)
- System Safety: [`../../SAFETY/`](../../SAFETY/)
- Audit Program: [`../04-AUDITS/`](../04-AUDITS/)
- Compliance Matrix: [`../05-REGISTERS/COMPLIANCE_MATRIX.csv`](../05-REGISTERS/COMPLIANCE_MATRIX.csv)
- CAPA System: [`../04-AUDITS/CAPA_LOG.csv`](../04-AUDITS/CAPA_LOG.csv)

## Metrics

- Open compliance risks (count by severity)
- Risk score trend (average, max)
- Mitigation plan completion (%)
- Risks realized (count, cost impact)
- Closed risks (closure rate)

---

**Owner**: Risk Manager with Compliance Office input  
**Review**: Weekly (team), Monthly (management), Quarterly (executive)  
**Approval**: Program Manager, Chief Engineer
