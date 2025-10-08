# ECR Workflow

> Location: `CONFIG_MGMT/06-CHANGES/02-WORKFLOW/ECR_WORKFLOW.md`  
> Authority: Configuration Manager

## Purpose

Define the Engineering Change Request (ECR) process from submission through disposition.

## Workflow Overview

```
Submit → Triage → Impact Assessment → CCB Review → Disposition
```

## Process Steps

### 1. Submit ECR

**Responsible:** Change Originator

**Actions:**
1. Identify need for change (problem, improvement, requirement)
2. Complete ECR using template: **[../04-TEMPLATES/ECR.yml](../04-TEMPLATES/ECR.yml)**
3. Gather supporting documentation:
   - Problem description or justification
   - Affected items list (part numbers, documents)
   - Preliminary impact estimate
   - Supporting analysis or test data
4. Submit to Configuration Manager

**Outputs:**
- Completed ECR draft
- Supporting attachments

**Duration:** 1-3 days (originator effort)

---

### 2. Triage and Assignment

**Responsible:** Configuration Manager

**Actions:**
1. Receive and log ECR
2. Assign ECR number (format: `ECR-YYYY-####`)
3. Record in **[../03-REGISTERS/CHANGE_REGISTER.csv](../03-REGISTERS/CHANGE_REGISTER.csv)**
4. Perform initial completeness check
5. Determine initial classification (Class I/II/III)
6. Route to appropriate reviewers based on:
   - Change classification
   - Affected systems/subsystems
   - Safety/certification impact
   - Customer/regulatory implications
7. Set review due dates

**Outputs:**
- ECR number assigned
- Initial classification determined
- Review assignments made
- Review due dates established

**Duration:** 1-2 business days

---

### 3. Impact Assessment

**Responsible:** Technical Reviewers (Engineering, Quality, Manufacturing, Safety, etc.)

**Actions:**
1. Receive ECR assignment
2. Review change request and supporting documentation
3. Assess impact in respective domain:
   - **Engineering:** Technical feasibility, design impact, requirements traceability
   - **Quality:** Quality/compliance impact, certification requirements
   - **Manufacturing:** Producibility, tooling, process changes, cost
   - **Safety:** Safety analysis, hazard impact, risk assessment
   - **Test:** Test impact, verification approach
   - **Supply Chain:** Supplier impact, procurement actions
4. Complete impact assessment per **[../04-TEMPLATES/IMPACT_ASSESSMENT.md](../04-TEMPLATES/IMPACT_ASSESSMENT.md)**
5. Provide recommendation: Approve / Approve with Conditions / Reject / Defer
6. Submit assessment to Configuration Manager

**Class I Changes — Additional Requirements:**
- Detailed impact analysis across all domains
- Safety assessment (if applicable)
- Certification impact analysis
- Interface analysis (if applicable)
- Requirements traceability update
- Test/verification plan
- Implementation plan with schedule
- Risk assessment and mitigation
- Domain-specific checklist completion

**Outputs:**
- Completed impact assessments by domain
- Technical recommendations
- Cost and schedule estimates
- Risk identification

**Duration:** 
- Class I: 5-10 business days
- Class II: 3-5 business days
- Class III: 1-2 business days

---

### 4. CCB Review (Class I) or Delegated Approval (Class II/III)

#### 4a. CCB Review (Class I Changes)

**Responsible:** CCB Chair, CCB Members

**Actions:**
1. Configuration Manager prepares CCB package:
   - ECR with all impact assessments
   - Supporting documentation
   - Technical recommendations
   - Cost/schedule estimates
   - Presentation materials
2. ECR added to CCB meeting agenda
3. CCB package distributed 48 hours before meeting
4. Originator presents ECR at CCB meeting
5. Technical discussion
6. CCB members vote
7. CCB Chair makes final disposition
8. Configuration Manager documents decision in CCB minutes

**Disposition Options:**
- **Approved:** ECO issued for implementation
- **Approved with Conditions:** Specific conditions must be met; may require re-review
- **Rejected:** Not approved; rationale documented
- **Deferred:** More information needed; return for additional analysis

**Outputs:**
- CCB disposition documented
- Conditions or actions identified (if applicable)
- ECO number assigned (if approved)
- Originator notified

**Duration:** Depends on CCB meeting schedule (typically 1-2 weeks from readiness)

#### 4b. Delegated Approval (Class II Changes)

**Responsible:** Engineering Manager, Quality Manager

**Actions:**
1. Configuration Manager routes to delegated approvers
2. Engineering Manager reviews technical assessment
3. Quality Manager reviews quality/compliance aspects
4. Both approvers provide disposition
5. Configuration Manager documents approval

**Duration:** 3-5 business days

#### 4c. CM Approval (Class III Changes)

**Responsible:** Configuration Manager

**Actions:**
1. Configuration Manager reviews ECR
2. Verifies administrative nature
3. Approves or rejects
4. Documents decision

**Duration:** 1-2 business days

---

### 5. Disposition and Notification

**Responsible:** Configuration Manager

**Actions:**
1. Document final disposition in ECR
2. Update **[../03-REGISTERS/CHANGE_REGISTER.csv](../03-REGISTERS/CHANGE_REGISTER.csv)**
3. Notify originator and stakeholders
4. If approved:
   - Issue ECO per **[ECO_WORKFLOW.md](./ECO_WORKFLOW.md)**
   - Assign ECO number
   - Move ECR to **[../05-ECR/ACTIVE/](../05-ECR/ACTIVE/)**
   - Create ECO folder in **[../06-ECO/ACTIVE/](../06-ECO/ACTIVE/)**
5. If rejected:
   - Document rationale
   - Move ECR to **[../05-ECR/CLOSED/](../05-ECR/CLOSED/)**
   - Inform originator of appeal process (if applicable)
6. If deferred:
   - Document required information
   - Assign action to originator or reviewers
   - Track in **[../03-REGISTERS/OPEN_ITEMS.csv](../03-REGISTERS/OPEN_ITEMS.csv)**

**Outputs:**
- ECR status updated
- Stakeholders notified
- ECO issued (if approved)
- Actions tracked (if deferred)

**Duration:** 1 business day

---

## Total Cycle Time

**Typical Duration (from submission to disposition):**
- **Class I:** 2-4 weeks
- **Class II:** 1-2 weeks
- **Class III:** 3-5 days

**Emergency Changes:** 24-48 hours (expedited process)

---

## ECR States

| State | Description | Location |
|-------|-------------|----------|
| **Draft** | In preparation by originator | Originator |
| **Submitted** | Received by CM, awaiting triage | CM inbox |
| **Under Review** | Routed to technical reviewers | **[../05-ECR/INBOX/](../05-ECR/INBOX/)** |
| **Ready for CCB** | Impact assessment complete, awaiting CCB | **[../05-ECR/ACTIVE/](../05-ECR/ACTIVE/)** |
| **Approved** | CCB approved, ECO issued | **[../05-ECR/ACTIVE/](../05-ECR/ACTIVE/)** → **[../05-ECR/CLOSED/](../05-ECR/CLOSED/)** |
| **Rejected** | Not approved | **[../05-ECR/CLOSED/](../05-ECR/CLOSED/)** |
| **Deferred** | More information needed | **[../05-ECR/ACTIVE/](../05-ECR/ACTIVE/)** |

---

## Roles and Responsibilities

See **[../01-POLICY/RASCI.md](../01-POLICY/RASCI.md)** for detailed RASCI matrix.

**Key Roles:**
- **Configuration Manager:** Process owner, triage, tracking, notification
- **Change Originator:** Submit ECR, provide information, support reviews
- **Technical Reviewers:** Impact assessment in respective domains
- **CCB Chair:** Lead CCB meeting, final disposition
- **CCB Members:** Review and vote on Class I changes

---

## Related Documents

- **[../01-POLICY/CHANGE_POLICY.md](../01-POLICY/CHANGE_POLICY.md)** — Change policy
- **[../01-POLICY/CLASSIFICATION.md](../01-POLICY/CLASSIFICATION.md)** — Classification criteria
- **[../04-TEMPLATES/ECR.yml](../04-TEMPLATES/ECR.yml)** — ECR template
- **[../04-TEMPLATES/IMPACT_ASSESSMENT.md](../04-TEMPLATES/IMPACT_ASSESSMENT.md)** — Impact assessment template
- **[ECO_WORKFLOW.md](./ECO_WORKFLOW.md)** — ECO implementation workflow
- **[../../05-CCB/00-CHARTER.md](../../05-CCB/00-CHARTER.md)** — CCB charter

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-15 | Configuration Manager | Initial release |
