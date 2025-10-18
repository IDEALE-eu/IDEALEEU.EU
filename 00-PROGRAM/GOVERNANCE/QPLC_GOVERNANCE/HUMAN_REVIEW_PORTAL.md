# Human Review Portal
## Interface Specification for QPLC Human Approval Gates

**Version:** 1.0.0  
**Status:** Specification  
**Owner:** IIS Domain Lead  
**Last Updated:** 2025-10-18

---

## Purpose

The **Human Review Portal** is the primary interface through which authorized personnel review, approve, or reject AGI/ASI decisions flagged by the QPLC system. It ensures human sovereignty over AI decision-making while maintaining efficient operations.

---

## Architecture

### System Context

```
┌──────────────────────────────────────────────────┐
│           AGI/ASI Decision Engine                │
└──────────────────┬───────────────────────────────┘
                   │
         ┌─────────▼──────────┐
         │   QPLC Validator   │
         │   (EPE + Safety)   │
         └─────────┬──────────┘
                   │
           [Decision Flagged]
                   │
         ┌─────────▼──────────┐
         │  Approval Queue    │
         │  (by Risk Level)   │
         └─────────┬──────────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
┌───▼────┐   ┌────▼────┐   ┌────▼────┐
│ Mobile │   │ Web App │   │  Email  │
│  App   │   │ Portal  │   │ Alerts  │
└────────┘   └────┬────┘   └─────────┘
                  │
        ┌─────────▼─────────┐
        │ Human Reviewer    │
        │ (Evaluate & Decide)│
        └─────────┬─────────┘
                  │
        ┌─────────▼─────────┐
        │ Approval/Rejection │
        │ with Rationale     │
        └─────────┬─────────┘
                  │
         ┌────────▼────────┐
         │ UTCS Logging    │
         │ & Execution     │
         └─────────────────┘
```

---

## User Roles & Permissions

### Role Hierarchy

| Role | Access Level | Responsibilities |
|------|--------------|------------------|
| **Operator** | View Only | Monitor decision queue |
| **Operations Manager** | Medium Risk | Review and approve medium-risk decisions |
| **Domain Lead** | Medium-High | Technical evaluation of domain-specific decisions |
| **Safety Officer** | High-Critical | Safety validation and critical approvals |
| **Ethics Board Member** | High-Critical | Ethical validation |
| **CCB Member** | Critical Only | Configuration Control Board decisions |
| **Chief Safety Officer** | All + Override | Emergency override authority |

### Permission Matrix

| Action | Operator | Ops Mgr | Domain Lead | Safety Officer | Ethics Board | CCB | CSO |
|--------|----------|---------|-------------|----------------|--------------|-----|-----|
| View Low | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| View Medium | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| View High | - | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| View Critical | - | - | - | ✓ | ✓ | ✓ | ✓ |
| Approve Medium | - | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Approve High | - | - | ✓ | ✓ | ✓ | ✓ | ✓ |
| Approve Critical | - | - | - | ✓* | ✓* | ✓* | ✓ |
| Emergency Override | - | - | - | - | - | - | ✓ |

*Requires consensus of all assigned reviewers

---

## User Interface Specification

### Dashboard View

#### Primary Components

1. **Pending Approvals Queue**
   - Risk level indicator (color-coded)
   - Decision summary
   - Time remaining before timeout
   - Assigned reviewers
   - Quick action buttons

2. **Active Decisions Monitor**
   - Real-time status of currently executing decisions
   - Performance metrics
   - Anomaly alerts

3. **Recent Activity Feed**
   - Last 24 hours of approvals/rejections
   - Trends and patterns
   - Team performance metrics

4. **System Health Indicators**
   - QPLC system status
   - Quantum backend availability
   - EPE compliance rate
   - Average approval latency

#### Wireframe (Dashboard)

```
┌─────────────────────────────────────────────────────────────────┐
│ QPLC Human Review Portal                          [User] [Help] │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ System Status: ✓ Operational    Queue: 3 Pending    Latency: 2m│
│                                                                  │
├────────────────────────────────────┬────────────────────────────┤
│                                    │                            │
│  PENDING APPROVALS (3)             │  SYSTEM HEALTH             │
│                                    │                            │
│  ⚠ HIGH RISK (2 reviewers needed) │  ✓ QPLC Runtime: Healthy  │
│  Decision: Crew scheduling change  │  ✓ Quantum Backend: Online │
│  EPE Rule: HUM-DIGN-02 (Fatigue)  │  ✓ EPE Compliance: 100%    │
│  Timeout: 8m 23s remaining         │  ⚠ Avg Latency: 3m 12s    │
│  Assigned: You, Safety Officer     │                            │
│  [View Details] [Approve] [Reject] │  [View Metrics]            │
│  ───────────────────────────────── │                            │
│                                    │  RECENT ACTIVITY (24h)     │
│  ℹ MEDIUM RISK (1 reviewer)       │                            │
│  Decision: Asset reallocation      │  Approved: 45              │
│  EPE Rule: ASSET-HUM-03            │  Rejected: 3               │
│  Timeout: 4m 05s                   │  Deferred: 1               │
│  Assigned: You                     │  Avg Latency: 2m 47s       │
│  [View Details] [Approve] [Reject] │                            │
│  ───────────────────────────────── │  [View Full Report]        │
│                                    │                            │
│  ℹ MEDIUM RISK (awaiting review)  │                            │
│  Decision: Maintenance scheduling  │  ALERTS                    │
│  EPE Rule: None (flagged for rev) │                            │
│  Timeout: 2m 40s                   │  No active alerts          │
│  Assigned: Operations Manager      │                            │
│  [View Details]                    │                            │
│                                    │                            │
└────────────────────────────────────┴────────────────────────────┘
```

---

### Decision Detail View

#### Information Displayed

1. **Decision Summary**
   - Proposed action in plain language
   - Originating AGI/ASI system
   - Timestamp and decision ID

2. **Risk Assessment**
   - Risk level and score breakdown
   - Triggered EPE rules with explanations
   - Safety bounds analysis

3. **Context & Rationale**
   - AGI's reasoning (explainability)
   - Model card link
   - SHAP values or feature importance
   - Alternative options considered

4. **Impact Analysis**
   - Affected personnel/systems
   - Cost implications
   - Safety considerations
   - Reversibility assessment

5. **Approval Requirements**
   - Number of reviewers needed
   - Required reviewer roles
   - Consensus/unanimity requirement
   - Timeout and fallback action

6. **Supporting Documentation**
   - Relevant policies
   - Historical similar decisions
   - Regulatory references

#### Wireframe (Detail View)

```
┌─────────────────────────────────────────────────────────────────┐
│ Decision Review: DEC-2025-1018-0042              [Back to Queue]│
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ⚠ HIGH RISK DECISION                        ⏱ 8m 23s remaining│
│                                                                  │
│  PROPOSED ACTION                                                 │
│  Assign technician Jane Smith to maintenance task MT-1234       │
│  during extended shift (13th hour of duty)                      │
│                                                                  │
│  ORIGINATING SYSTEM: AGI-MRO-Scheduler-v2.3                     │
│  TIMESTAMP: 2025-10-18 14:32:15 UTC                             │
│  DECISION ID: DEC-2025-1018-0042                                │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  RISK ASSESSMENT                                                 │
│                                                                  │
│  Risk Score: 55 / 100 (HIGH)                                    │
│  ├─ Safety Impact: 5/10                                         │
│  ├─ Cost Impact: 2/5                                            │
│  ├─ Regulatory Impact: 4/8                                      │
│  ├─ Reversibility: 3/6                                          │
│  ├─ Ethical Sensitivity: 9/9  ⚠ FLAGGED                        │
│  └─ Complexity: 2/4                                             │
│                                                                  │
│  TRIGGERED EPE RULES                                            │
│  • HUM-DIGN-02: No tasking below fatigue thresholds             │
│    └─ Technician has 12.5 duty hours (threshold: 12)           │
│    └─ Rest hours in last 24h: 7.5 (threshold: 8)               │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  AGI RATIONALE                                                   │
│                                                                  │
│  "Task MT-1234 is time-critical for aircraft AOG situation.     │
│   Technician Smith is most qualified and available. Shift       │
│   extension of 1 hour minimizes overall operational impact."    │
│                                                                  │
│  [View Full Explainability Report] [Model Card] [SHAP Values]  │
│                                                                  │
│  ALTERNATIVES CONSIDERED BY AGI                                  │
│  1. Assign less qualified technician → +3h completion time      │
│  2. Defer task to next shift → +18h aircraft downtime           │
│  3. Call in off-duty technician → +2h response time + overtime  │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  IMPACT ANALYSIS                                                 │
│                                                                  │
│  Affected Personnel: 1 (Jane Smith, Cert: A&P Mech III)        │
│  Current Duty Hours: 12.5 / 12.0 limit (0.5h over)             │
│  Rest Hours (24h): 7.5 / 8.0 required (0.5h under)             │
│  Cognitive Load: 0.78 / 0.85 threshold (within limits)          │
│                                                                  │
│  Safety: MEDIUM - Fatigue may impact work quality               │
│  Cost: $180 overtime pay                                        │
│  Reversibility: HIGH - Can reassign if concerns arise           │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  APPROVAL REQUIREMENTS                                           │
│                                                                  │
│  Reviewers Required: 2 (Consensus)                              │
│  Assigned Reviewers:                                             │
│    ✓ You (Domain Lead - MRO)                                    │
│    ⏳ Safety Officer (Pending)                                  │
│                                                                  │
│  Timeout: 10 minutes (8m 23s remaining)                         │
│  Fallback Action: REJECT (defer to next shift)                  │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  YOUR DECISION                                                   │
│                                                                  │
│  ○ APPROVE                                                       │
│    Optional mitigations:                                         │
│    ☐ Require supervisor observation                             │
│    ☐ Limit to non-critical tasks                                │
│    ☐ Provide rest break before shift end                        │
│                                                                  │
│  ○ REJECT                                                        │
│    Reason (select one):                                          │
│    ○ Safety concern not adequately addressed                     │
│    ○ Better alternative exists                                   │
│    ○ Policy violation                                            │
│    ○ Other (specify)                                             │
│                                                                  │
│  ○ DEFER                                                         │
│    Request additional information:                               │
│    [ Text field for information request ]                       │
│                                                                  │
│  RATIONALE (required):                                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ [Text area for reviewer's rationale]                      │  │
│  │                                                            │  │
│  │                                                            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  [Submit Decision] [Request Consultation] [Save Draft]          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Workflow States

### Decision Lifecycle

```
    [AGI Proposes]
         │
         ▼
   [QPLC Validates]
         │
    ┌────┴────┐
    │         │
    ▼         ▼
[APPROVED] [FLAGGED] ────────────────┐
    │                                │
    │         ┌──────────────────────┘
    │         ▼
    │    [QUEUED]
    │         │
    │         ├─► [ASSIGNED] ─► [UNDER_REVIEW]
    │         │                      │
    │         │                 ┌────┼────┐
    │         │                 │    │    │
    │         ▼                 ▼    ▼    ▼
    │    [TIMEOUT]         [APPROVED] [REJECTED] [DEFERRED]
    │         │                 │    │    │
    │         ▼                 │    │    │
    │    [FALLBACK]             │    │    │
    │                           │    │    │
    └───────────────────────────┴────┼────┘
                                     │
                                     ▼
                              [EXECUTED/LOGGED]
```

---

## Notification System

### Notification Channels

1. **In-App Notifications**
   - Real-time banner alerts
   - Badge counts on approval queue
   - Sound alerts (configurable)

2. **Email Alerts**
   - Immediate: Critical decisions
   - Digest: Medium/Low decisions (every 15 minutes)
   - Daily summary report

3. **SMS/Text (High/Critical only)**
   - Escalation after 50% of timeout elapsed
   - Emergency overrides

4. **Mobile Push Notifications**
   - All risk levels
   - Configurable per user

5. **Slack/Teams Integration**
   - Channel alerts for team visibility
   - Direct messages for assigned reviewers

### Notification Content

```
Subject: [QPLC - HIGH RISK] Decision Approval Required (8m remaining)

Decision ID: DEC-2025-1018-0042
Risk Level: HIGH
Triggered Rule: HUM-DIGN-02 (Fatigue threshold)

Proposed Action: Extend technician shift beyond duty hour limit

Your approval is required as Domain Lead (MRO).
Timeout: 8 minutes 23 seconds

Quick Actions:
- View Details: https://portal.idealeeu.eu/qplc/decision/DEC-2025-1018-0042
- Approve: [Click here]
- Reject: [Click here]

Note: This decision requires 2 reviewers. Safety Officer also assigned.
```

---

## Mobile App Specification

### Key Features

- **Simplified approval workflow** for on-the-go reviews
- **Biometric authentication** (fingerprint, Face ID)
- **Offline mode** with sync on reconnection
- **Voice input** for rationale entry
- **Emergency alert override**

### Screen Flow

```
[Login]
   │
   ▼
[Dashboard] ─► [Pending Queue] ─► [Decision Detail]
   │                                     │
   │                                     ├─► [Approve]
   │                                     ├─► [Reject]
   │                                     └─► [Defer]
   │                                           │
   ▼                                           ▼
[Activity Feed]                        [Confirmation]
   │                                           │
   ▼                                           ▼
[Metrics & Reports]                    [Back to Queue]
```

---

## API Specification

### RESTful Endpoints

```
GET    /api/v1/approvals/queue
GET    /api/v1/approvals/{decision_id}
POST   /api/v1/approvals/{decision_id}/approve
POST   /api/v1/approvals/{decision_id}/reject
POST   /api/v1/approvals/{decision_id}/defer
GET    /api/v1/approvals/history
GET    /api/v1/metrics/dashboard
POST   /api/v1/notifications/preferences
```

### WebSocket Events

```javascript
// Real-time updates
ws://portal.idealeeu.eu/qplc/events

Events:
- approval.queued
- approval.assigned
- approval.timeout_warning
- approval.completed
- system.health_alert
```

---

## Security & Compliance

### Authentication
- **Multi-factor authentication (MFA)** required for all users
- **Certificate-based auth** for API access
- **Session timeout**: 15 minutes idle, 8 hours maximum

### Authorization
- **Role-based access control (RBAC)**
- **Attribute-based access control (ABAC)** for sensitive decisions
- **Audit logging** of all access and actions

### Data Protection
- **TLS 1.3** for all communications
- **Encryption at rest** (AES-256)
- **PII anonymization** in logs
- **GDPR compliant** data handling

### Audit Trail
- **Complete logging** to UTCS manifests
- **Tamper-evident** audit logs
- **7-year retention** (regulatory requirement)

---

## Performance Requirements

| Metric | Target | Measurement |
|--------|--------|-------------|
| Page load time | < 2 seconds | P95 |
| API response time | < 500ms | P95 |
| Real-time notification latency | < 1 second | P99 |
| System availability | 99.95% | Monthly |
| Concurrent users supported | 500 | Peak |

---

## Accessibility

### WCAG 2.1 AA Compliance
- **Keyboard navigation** fully supported
- **Screen reader** compatible
- **High contrast mode**
- **Adjustable font sizes**
- **Color-blind friendly** indicators

### Language Support
- **Primary**: English
- **Planned (v2.0)**: Spanish, French, German, Mandarin

---

## Future Enhancements (Roadmap)

### Version 2.0 (Q2 2026)
- [ ] AI-assisted decision recommendations
- [ ] Predictive ethics (pre-emptive flagging)
- [ ] Collaborative review (multi-reviewer real-time)
- [ ] Enhanced mobile app (offline capable)

### Version 3.0 (Q4 2026)
- [ ] VR/AR interface for complex 3D decisions
- [ ] Natural language query interface
- [ ] Automated counterfactual generation
- [ ] Federated ethics learning insights

---

## Support & Training

### Training Requirements
- **All Reviewers**: 4-hour QPLC portal training
- **Safety Officers**: 8-hour advanced training
- **CCB Members**: 6-hour governance training

### Support Contacts
- **Technical Support**: qplc-support@idealeeu.eu
- **Training**: qplc-training@idealeeu.eu
- **Escalation**: qplc-escalation@idealeeu.eu (24/7)

---

**The Human Review Portal ensures that advanced AI serves human judgment—not the reverse.**
