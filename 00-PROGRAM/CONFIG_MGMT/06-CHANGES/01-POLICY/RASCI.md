# RASCI Matrix — Change Management

> Location: `CONFIG_MGMT/06-CHANGES/01-POLICY/RASCI.md`  
> Authority: Configuration Manager

## Purpose

Define roles and responsibilities for change management using the RASCI framework:
- **R** — Responsible (does the work)
- **A** — Accountable (final approval, one per activity)
- **S** — Support (provides resources)
- **C** — Consulted (provides input)
- **I** — Informed (kept updated)

## RASCI Matrix

### ECR Submission and Triage

| Activity | Config Mgr | CCB Chair | Change Originator | Engineering | Quality | Manufacturing | Safety | Customer |
|----------|------------|-----------|-------------------|-------------|---------|---------------|--------|----------|
| Submit ECR | I | I | **R/A** | C | C | C | C | I |
| Assign ECR number | **R/A** | I | I | - | - | - | - | - |
| Initial triage | **R/A** | C | I | C | - | - | - | - |
| Route for review | **R/A** | I | I | I | I | I | I | - |

### ECR Review and Impact Assessment

| Activity | Config Mgr | CCB Chair | Change Originator | Engineering | Quality | Manufacturing | Safety | Customer |
|----------|------------|-----------|-------------------|-------------|---------|---------------|--------|----------|
| Technical review | S | C | S | **R/A** | C | C | C | C |
| Safety assessment | S | C | S | C | C | - | **R/A** | C |
| Cost estimate | S | C | S | C | C | **R/A** | - | - |
| Schedule impact | S | C | S | **R/A** | C | S | - | C |
| Certification impact | S | C | S | C | **R/A** | - | C | C |
| Compile impact assessment | **R** | C | S | S | S | S | S | - |

### CCB Review and Disposition (Class I)

| Activity | Config Mgr | CCB Chair | Change Originator | Engineering | Quality | Manufacturing | Safety | Customer |
|----------|------------|-----------|-------------------|-------------|---------|---------------|--------|----------|
| Prepare CCB package | **R/A** | C | S | S | S | S | S | - |
| Present to CCB | S | **A** | **R** | S | S | S | S | - |
| Technical vote | S | **A** | I | **R** | **R** | **R** | **R** | C |
| Final disposition | S | **R/A** | I | I | I | I | I | I |
| Document decision | **R/A** | S | I | I | I | I | I | - |
| Notify originator | **R/A** | I | I | - | - | - | - | - |
| Customer notification | **R** | S | S | S | C | - | C | I |

### Delegated Approval (Class II)

| Activity | Config Mgr | Engineering Mgr | Change Originator | Engineering | Quality | Manufacturing |
|----------|------------|-----------------|-------------------|-------------|---------|---------------|
| Technical review | S | **A** | S | **R** | C | C |
| Quality review | S | C | S | C | **R/A** | - |
| Approve/reject | I | **R/A** | I | - | **R** | - |
| Document decision | **R/A** | I | I | - | I | - |

### CM Approval (Class III)

| Activity | Config Mgr | Change Originator |
|----------|------------|-------------------|
| Review ECR | **R/A** | S |
| Approve/reject | **R/A** | I |
| Document decision | **R/A** | I |

### ECO Issuance and Planning

| Activity | Config Mgr | CCB Chair | Implementation Lead | Engineering | Quality | Manufacturing | Supply Chain |
|----------|------------|-----------|---------------------|-------------|---------|---------------|--------------|
| Issue ECO | **R/A** | C | I | I | I | I | I |
| Assign ECO number | **R/A** | - | I | - | - | - | - |
| Develop implementation plan | S | C | **R/A** | S | C | S | C |
| Estimate resources | S | C | **R/A** | **R** | C | **R** | C |
| Schedule activities | S | C | **R/A** | S | C | S | - |
| Identify affected items | **R** | - | **R** | **R** | C | C | C |
| Supplier coordination | S | - | S | C | C | C | **R/A** |

### ECO Implementation

| Activity | Config Mgr | Implementation Lead | Engineering | Quality | Manufacturing | Test |
|----------|------------|---------------------|-------------|---------|---------------|------|
| Execute changes | S | **A** | **R** | C | **R** | C |
| Update drawings/specs | S | S | **R/A** | C | C | - |
| Update software | S | S | **R/A** | C | - | C |
| Update processes | S | S | C | C | **R/A** | - |
| Update test procedures | S | S | C | C | C | **R/A** |
| Track progress | **R/A** | **R** | I | I | I | I |

### ECO Verification

| Activity | Config Mgr | Implementation Lead | Engineering | Quality | Test | Safety |
|----------|------------|---------------------|-------------|---------|------|--------|
| Execute verification | S | **A** | C | S | **R** | C |
| Review test results | S | **R** | **R** | **R** | **R** | C |
| Safety verification | S | C | C | C | C | **R/A** |
| Document results | S | **R/A** | S | S | S | S |
| Approve verification | S | S | C | **R/A** | S | C |

### ECO Closure

| Activity | Config Mgr | CCB Chair | Implementation Lead | Engineering | Quality |
|----------|------------|-----------|---------------------|-------------|---------|
| Complete documentation | **R** | - | **R** | **R** | **R** |
| Update baseline | **R/A** | C | S | S | C |
| Update traceability | **R/A** | - | S | S | C |
| Archive records | **R/A** | - | S | S | S |
| Lessons learned | S | C | **R/A** | **R** | **R** |
| CCB closure review | **R** | **A** | I | I | I |
| Close ECO | **R/A** | C | I | I | I |

### Deviation/Waiver Process

| Activity | Config Mgr | CCB Chair | Originator | Engineering | Quality | Customer |
|----------|------------|-----------|------------|-------------|---------|----------|
| Submit deviation/waiver | I | I | **R/A** | C | C | C |
| Technical justification | S | C | **R** | **R** | C | - |
| Safety assessment | S | C | S | C | C | **R/A** |
| CCB approval | **R** | **A** | I | **R** | **R** | C |
| Customer approval (if req'd) | **R** | S | S | S | C | **A** |
| Track effectivity | **R/A** | I | S | S | C | - |

### MRB Process

| Activity | Quality Mgr | Config Mgr | Engineering | Manufacturing | Customer |
|----------|-------------|------------|-------------|---------------|----------|
| Submit MRB case | **R** | I | C | **R** | - |
| Technical evaluation | C | C | **R/A** | C | - |
| Disposition recommendation | **R/A** | C | **R** | **R** | - |
| Customer concurrence (if req'd) | **R** | S | S | S | **A** |
| Document disposition | **R/A** | **R** | S | S | - |
| Generate ECR (if needed) | S | **R/A** | **R** | S | - |

### Baseline Updates

| Activity | Config Mgr | CCB Chair | Engineering | Quality |
|----------|------------|-----------|-------------|---------|
| Identify baseline changes | **R/A** | C | **R** | C |
| Update baseline manifest | **R/A** | C | S | C |
| Update item master | **R/A** | - | S | C |
| Tag/release baseline | **R/A** | C | S | C |
| CCB approval | **R** | **A** | I | I |
| Notify stakeholders | **R/A** | S | I | I |

### Metrics and Reporting

| Activity | Config Mgr | CCB Chair | Program Manager |
|----------|------------|-----------|-----------------|
| Collect metrics | **R/A** | S | I |
| Analyze trends | **R/A** | C | C |
| Report to PM | **R** | C | **A** |
| Report to CCB | **R** | **A** | I |
| Identify improvements | **R** | **R** | C |

---

## Role Definitions

### Configuration Manager
- Process owner for change management
- Maintains change register and numbering
- Routes ECRs for review
- Issues ECOs
- Updates baselines
- Maintains traceability
- Reports metrics

### CCB Chair
- Leads CCB meetings
- Final approval authority for Class I changes
- Resolves disputes
- Ensures CCB charter compliance

### Change Originator
- Identifies need for change
- Submits ECR with justification
- Provides technical information
- Supports review process

### Engineering
- Technical assessment of changes
- Impact analysis
- Implementation of design changes
- Verification support

### Quality Manager
- Quality and compliance review
- Verification oversight
- Audit change process
- MRB leadership

### Manufacturing Manager
- Producibility assessment
- Manufacturing impact analysis
- Process change implementation

### Safety Manager
- Safety impact assessment
- Hazard analysis updates
- Safety verification

### Test Manager
- Test impact assessment
- Test procedure updates
- Verification testing

### Supply Chain Manager
- Supplier impact assessment
- Supplier coordination
- Procurement actions

### Customer Representative
- Customer requirements validation
- Contractual compliance
- Approval of customer-affecting changes

---

## Escalation Path

1. **Technical Issues:** Engineering → Chief Engineer → Program Manager
2. **Cost/Schedule Issues:** Implementation Lead → Program Manager
3. **Quality Issues:** Quality Manager → Program Manager
4. **Safety Issues:** Safety Manager → Chief Engineer → Program Manager
5. **CCB Disputes:** CCB Chair → Program Manager (final authority)

---

## Related Documents

- **[CHANGE_POLICY.md](./CHANGE_POLICY.md)** — Change policy overview
- **[CLASSIFICATION.md](./CLASSIFICATION.md)** — Classification criteria
- **[../02-WORKFLOW/ECR_WORKFLOW.md](../02-WORKFLOW/ECR_WORKFLOW.md)** — ECR workflow
- **[../02-WORKFLOW/ECO_WORKFLOW.md](../02-WORKFLOW/ECO_WORKFLOW.md)** — ECO workflow
- **[../../05-CCB/00-CHARTER.md](../../05-CCB/00-CHARTER.md)** — CCB charter
- **[../../05-CCB/01-MEMBERS.md](../../05-CCB/01-MEMBERS.md)** — CCB membership

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-15 | Configuration Manager | Initial release |
