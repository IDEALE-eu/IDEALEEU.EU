# Human-First Policy
## Ethical Guardrails for AI Optimization in IDEALE-EU

**Version:** 1.0.0  
**Policy ID:** EPE-HUMAN-FIRST  
**Status:** Active  
**Owner:** MAL-EEM Review Committee  
**Last Updated:** 2025-10-18

---

## Purpose

This policy establishes **human-centric ethical principles** that govern all AI-driven optimization within the IDEALE-EU platform. It ensures that:

1. **Human safety** always supersedes efficiency, cost, or performance objectives
2. **Human dignity** is preserved through empathic guardrails and fair treatment
3. **Human conditions** (fatigue, stress, crisis) are considered in all task assignments
4. **Asset optimization** never exploits human labor

---

## Core Principles

### 1. Human Safety > System Efficiency

**"Never optimize cost, schedule, or energy over human life or physical integrity."**

- All optimization algorithms must include explicit safety constraints
- Risk to humans automatically triggers rejection or review
- No override possible when human safety is at stake
- Applies to: workforce scheduling, asset deployment, maintenance planning

**Example Violations:**
- ❌ Scheduling maintenance during known fatigue periods to meet delivery deadline
- ❌ Reducing inspection frequency to cut costs
- ❌ Deploying undertrained personnel to expedite project

**Compliant Approaches:**
- ✅ Include safety as hard constraint in objective function
- ✅ Use multi-objective optimization with safety weights
- ✅ Implement safety validation layer before execution

---

### 2. Human Dignity > Automation

**"No human shall be treated as a replaceable node; empathy, rest, and cognitive load are first-class constraints."**

- Humans are not resources to be optimized like machines
- Fatigue limits and rest requirements are mandatory
- Cognitive load and wellbeing are measurable, enforceable constraints
- Work-life balance preserved even under operational pressure

**Fatigue Thresholds:**
- Maximum continuous duty: 12 hours
- Minimum rest between shifts: 8 hours
- Cognitive load score threshold: 0.85 (0-1 scale)
- Weekly duty hours: 48 hours maximum

**Empathic Guardrails:**
- Personnel in crisis zones: automatic scheduling pause
- Personal emergency: priority override for absence
- Wellbeing score decline: workload reduction triggered
- Team distress signals: manager notification

---

### 3. Transparency > Opacity

**"All AI decisions affecting humans must be explainable, contestable, and logged in UTCS."**

- Every decision documented with rationale
- Model cards required for personnel-affecting AI
- SHAP values or equivalent explainability metrics
- Human-readable explanations mandatory

**Explainability Requirements:**

| Decision Impact | Explainability Requirement |
|----------------|---------------------------|
| Low (routine) | Basic logging |
| Medium (scheduling) | Model card + decision log |
| High (promotion/termination) | Full SHAP + human review |
| Critical (safety-related) | Complete audit trail + CCB review |

---

### 4. Fairness > Speed

**"Workload, risk, and opportunity must be distributed equitably across roles, genders, and geographies."**

- Demographic parity in task assignment
- No algorithmic discrimination
- Regular bias audits required
- Disparate impact analysis for all personnel AI

**Protected Attributes:**
- Gender
- Age
- Ethnicity
- Disability status
- Union membership
- Parental status
- Geographic location

**Fairness Metrics:**
- Demographic parity: ≥ 0.8
- Equal opportunity: ≥ 0.85
- Predictive parity: ≥ 0.80

---

## Application Domains

### Human Resources & Operations (OOO, MMM)

**Applies to:**
- MRO technician scheduling
- Task assignment and workload balancing
- Skills development and training allocation
- Shift planning and crew rostering
- Crisis-aware leave policies

**Example Rules:**
- No scheduling during local emergencies (EMPATHY-GUARD-04)
- Fatigue-aware task deferral (HUM-DIGN-02)
- Equitable workload distribution (HUM-FAIR-03)

### Asset Optimization (LIB, PPP, CQH, EEE)

**Applies to:**
- Circular part reuse planning
- H₂ logistics route optimization
- Power distribution strategies
- Maintenance interval optimization

**Example Rules:**
- Inspection burden limits for reused parts (ASSET-HUM-03)
- Safety-constrained power optimization (COST-SAFE-07)
- Human oversight for autonomous decisions (AUTON-09)

---

## Implementation in QPLC

The Ethical Policy Engine (EPE) is integrated into the QPLC runtime:

```
┌─────────────────────────────────┐
│   AGI/AI Proposes Optimization  │
└─────────────┬───────────────────┘
              │
    ┌─────────▼──────────┐
    │  EPE Validator     │
    │  Evaluates Rules   │
    └─────────┬──────────┘
              │
     ┌────────┼─────────┐
     │        │         │
┌────▼────┐ ┌▼───────┐ ┌▼─────────┐
│ REJECT  │ │ FLAG   │ │ APPROVE  │
│ (Safety)│ │ REVIEW │ │ (Safe)   │
└─────────┘ └────┬───┘ └──────────┘
                 │
        ┌────────▼──────────┐
        │ Human Review      │
        │ Portal            │
        └────────┬──────────┘
                 │
        ┌────────▼──────────┐
        │ Decision Logged   │
        │ to UTCS           │
        └───────────────────┘
```

---

## Enforcement Mechanisms

### 1. Automated Policy Gates

- **Pre-execution validation**: All proposals checked against EPE rules
- **Blocking mode**: Violations prevent execution
- **Real-time monitoring**: Continuous compliance checking

### 2. Human Review Portal

For flagged decisions:
- Clear explanation of policy trigger
- Context and alternatives presented
- Approval/rejection with rationale required
- Timeout handling (default: DEFER)

### 3. UTCS Audit Trail

All decisions recorded:
```yaml
utcs_events:
  - type: EPE_DECISION
    policy_id: EPE-HUMAN-FIRST-v1.0
    rule_id: HUM-DIGN-02
    outcome: DEFER
    timestamp: 2025-10-18T14:30:00Z
    context_hash: sha256(anonymous_worker_profile)
    reviewer: john.doe@example.com
    rationale: "Technician exceeds 12-hour duty limit"
```

### 4. Escalation Procedures

| Severity | Escalation Path | Response Time |
|----------|----------------|---------------|
| Low | Team Lead | 24 hours |
| Medium | Operations Manager | 4 hours |
| High | Safety Officer + Ethics Board | 1 hour |
| Critical | CCB + CEO | Immediate |

---

## Compliance & Standards

### Regulatory Framework

- **EU AI Act**: High-risk AI system compliance (Article 9, 10, 13, 14)
- **DO-384**: AI in civil aviation
- **ISO/IEC 24027**: Bias in AI systems
- **ISO 45001**: Occupational health and safety
- **GDPR**: Data protection and privacy
- **ILO Conventions**: Labor rights

### Certification Requirements

- Quarterly ethics audits
- Annual red-team testing
- Fairness metric reporting
- Incident investigation and reporting

---

## Monitoring & Metrics

### Key Performance Indicators

| Metric | Target | Frequency |
|--------|--------|-----------|
| Policy violation rate | 0% (critical rules) | Real-time |
| Human override rate | < 5% | Weekly |
| Average approval latency | < 5 minutes | Daily |
| Fairness score (overall) | ≥ 0.85 | Monthly |
| Explainability score | ≥ 0.90 | Monthly |
| Safety incident rate | 0 | Continuous |

### Dashboards

- **Ethics Dashboard**: Real-time policy compliance
- **Fairness Monitor**: Demographic parity tracking
- **Safety Portal**: Incident and near-miss tracking
- **Transparency Hub**: Explainability metrics

---

## Governance & Updates

### Policy Review Cycle

- **Frequency**: Quarterly
- **Authority**: MAL-EEM Review Committee
- **Stakeholders**:
  - Ethics Board
  - Safety Committee
  - Labor Representatives (Union)
  - Legal/Compliance
  - Technical Leads (IIS, OOO)

### Change Process

1. **Propose change**: Submit ECR (Engineering Change Request)
2. **Stakeholder consultation**: 2-week review period
3. **Ethics Board review**: Impact assessment
4. **CCB approval**: Final authorization
5. **Implementation**: Version update, communication
6. **Training**: Team briefings, documentation updates

---

## Use Case Examples

### ✅ Compliant Example: Maintenance Scheduling

**Scenario**: AI proposes maintenance task for technician  
**EPE Check**: Validates duty hours, rest periods, cognitive load  
**Result**: Approved (within limits)  
**Outcome**: Task assigned, logged to UTCS

### ❌ Non-Compliant Example: Cost-Optimized Inspection

**Scenario**: AI proposes reducing inspection frequency to cut costs  
**EPE Check**: Detects safety risk without explicit safety constraint  
**Result**: REJECTED (COST-SAFE-07)  
**Outcome**: Alternative proposal required with safety bounds

### ⚠️ Flagged Example: Emergency Reassignment

**Scenario**: AI proposes assigning technician in crisis zone  
**EPE Check**: Detects location in active crisis area  
**Result**: PAUSED (EMPATHY-GUARD-04)  
**Outcome**: Human review required, alternative assignment suggested

---

## Training & Awareness

### Required Training

- **All Personnel**: Human-first principles overview (1 hour)
- **Managers**: EPE policy implementation (3 hours)
- **AI Developers**: Ethical constraints in ML (8 hours)
- **Ethics Board**: Advanced ethical governance (16 hours)

### Resources

- EPE Policy Documentation (this document)
- EPE Rule Catalog ([EPE-v1.0.yaml](EPE-v1.0.yaml))
- QPLC Framework ([QPLC_DEFINITION.md](../../QPLC_DEFINITION.md))
- MAL-EEM Guidelines ([POLICY.md](../POLICY.md))

---

## Contact & Support

- **Policy Questions**: ethics@idealeeu.eu
- **Technical Issues**: qplc-support@idealeeu.eu
- **Safety Concerns**: safety@idealeeu.eu
- **Escalations**: ccb@idealeeu.eu

---

## Appendix: Rule Quick Reference

| Rule ID | Category | Description | Action |
|---------|----------|-------------|--------|
| HUM-SAFE-01 | Safety | Safety > Cost/Schedule | REJECT |
| HUM-DIGN-02 | Dignity | Fatigue thresholds | DEFER |
| HUM-FAIR-03 | Fairness | Workload equity | FLAG |
| ASSET-HUM-03 | Balance | Inspection burden | FLAG |
| EMPATHY-GUARD-04 | Empathy | Crisis zones | PAUSE |
| PRIVACY-05 | Privacy | Data minimization | FLAG |
| TRANS-06 | Transparency | Explainability | REQUIRE |
| COST-SAFE-07 | Safety | Never cost-only | REJECT |
| BIAS-08 | Anti-discrimination | Demographic fairness | FLAG |
| AUTON-09 | Oversight | Human approval | REQUIRE |

---

**This Human-First Policy ensures that IDEALE-EU's AI and quantum optimizations serve humanity—never the reverse. Human wellbeing, dignity, and safety are non-negotiable constraints in all algorithmic decisions.**
