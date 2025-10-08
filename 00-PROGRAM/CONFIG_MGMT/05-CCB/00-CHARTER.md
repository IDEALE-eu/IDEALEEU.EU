# Configuration Control Board (CCB) Charter

## 1. Purpose

The Configuration Control Board (CCB) is established to provide governance and decision-making authority for all changes to baselined configuration items in the IDEALE EU aerospace program.

## 2. Authority

The CCB operates under the authority of the Program Manager and is responsible for:
- Reviewing and dispositioning all Engineering Change Requests (ECRs)
- Approving or rejecting Engineering Change Orders (ECOs)
- Authorizing deviations and waivers
- Establishing and maintaining program baselines
- Ensuring change impact is properly assessed
- Maintaining configuration integrity

## 3. Scope

The CCB has authority over:
- Aircraft design and production
- Spacecraft design and production
- Ground support equipment
- Software and firmware
- Documentation and specifications
- Test procedures and equipment
- Manufacturing processes affecting form, fit, or function

## 4. CCB Membership

### 4.1 Voting Members

| Role | Responsibility |
|------|----------------|
| **CCB Chair** | Program Manager or designee - Final decision authority |
| **Chief Engineer** | Technical assessment and approval |
| **Systems Engineer** | System-level impact assessment |
| **Quality Manager** | Quality and compliance review |
| **Manufacturing Manager** | Producibility and cost impact |
| **Test Manager** | Test impact assessment |
| **Safety Manager** | Safety and risk assessment |
| **Certification Manager** | Regulatory compliance impact |

### 4.2 Non-Voting Members

| Role | Responsibility |
|------|----------------|
| **Configuration Manager** | CCB secretary, maintains records |
| **Procurement** | Supply chain impact (advisory) |
| **Finance** | Cost analysis (advisory) |
| **Customer Representative** | Customer interests (as applicable) |

### 4.3 Ad-Hoc Attendees

Subject matter experts may be invited as needed for specific changes.

## 5. CCB Meetings

### 5.1 Regular Meetings
- **Frequency:** Weekly during development, bi-weekly during production
- **Duration:** 2 hours maximum
- **Location:** Conference room or virtual (Teams/Zoom)

### 5.2 Emergency Meetings
- Called by CCB Chair for critical/urgent changes
- Minimum 24-hour notice (when possible)
- May be conducted virtually

### 5.3 Meeting Agenda
1. Review previous meeting minutes
2. Action item status
3. New ECR presentations
4. Pending ECO dispositions
5. Deviation/waiver requests
6. Baseline status review
7. Metrics and trends

## 6. Decision-Making Process

### 6.1 Quorum
- Minimum 5 voting members required
- Must include CCB Chair (or delegate) and Chief Engineer

### 6.2 Voting
- Consensus preferred
- Majority vote (>50%) required for approval
- CCB Chair has veto authority
- Abstentions not counted in vote total

### 6.3 Dispositions
- **Approved** - Change authorized for implementation
- **Approved with Conditions** - Change authorized with specified modifications
- **Rejected** - Change not authorized
- **Deferred** - More information required, postpone decision
- **Returned for Rework** - Submitter to revise and resubmit

## 7. Change Classification

### 7.1 Class I Changes
- Affect form, fit, or function
- Impact safety or certification
- Affect interchangeability
- Require customer approval
- **Authority:** Full CCB approval required

### 7.2 Class II Changes
- Documentation updates
- Minor process changes
- Non-critical design improvements
- **Authority:** Delegated to CCB Chair and Chief Engineer

### 7.3 Class III Changes
- Administrative changes
- Typographical corrections
- Non-technical updates
- **Authority:** Configuration Manager approval

## 8. ECR/ECO Process

### 8.1 ECR Submission
1. Originator completes ECR form (template: 13-TEMPLATES/ECR.yml)
2. Submit to Configuration Manager
3. CM assigns ECR number and routes to CCB
4. Technical assessment conducted
5. CCB reviews and dispositions

### 8.2 ECO Implementation
1. Approved ECR becomes ECO
2. CM issues ECO number
3. Implementation planned and executed
4. Verification performed
5. ECO closed upon completion

### 8.3 Tracking
All ECRs and ECOs tracked in **06-CHANGES/ECR/** and **06-CHANGES/ECO/**

## 9. Deviation and Waiver Process

### 9.1 Deviation Request
- One-time departure from requirements
- Must demonstrate no safety impact
- Requires CCB approval
- Tracked in **06-CHANGES/DEVIATIONS/**

### 9.2 Waiver Request
- Permanent acceptance of non-conformance
- Requires engineering justification
- May require customer approval
- Requires CCB approval
- Tracked in **06-CHANGES/WAIVERS/**

## 10. Baseline Management

### 10.1 Baseline Establishment
CCB authorizes baselines at stage gates:
- SRR, PDR, CDR, TRR, PRR, ORR/EIS, FRR

### 10.2 Baseline Control
- All changes to baselined items require CCB approval (Class I)
- Baselines archived in **04-BASELINES/[GATE]/**
- Configuration status accounting maintained

## 11. Roles and Responsibilities

### 11.1 CCB Chair
- Lead CCB meetings
- Make final decisions on changes
- Ensure CCB effectiveness
- Report CCB metrics to program management

### 11.2 Configuration Manager (Secretary)
- Prepare meeting agendas
- Distribute materials 48 hours before meeting
- Record meeting minutes
- Track action items
- Maintain CCB records
- Publish meeting minutes within 24 hours

### 11.3 Voting Members
- Review ECRs before meetings
- Assess impact to their discipline
- Participate in discussions
- Vote on changes
- Complete assigned actions

## 12. Documentation

### 12.1 Meeting Minutes
Document:
- Attendees (voting and non-voting)
- ECRs reviewed
- Dispositions and vote tallies
- Action items assigned
- Baseline status

Stored in **05-CCB/02-MINUTES/**

### 12.2 CCB Records Retention
- Meeting minutes: Permanent
- ECR/ECO records: Life of program + 10 years
- Deviation/waiver records: Life of program + 10 years

## 13. Metrics

CCB tracks and reports:
- ECRs submitted per month
- ECR approval rate
- Average ECR cycle time (submission to disposition)
- ECO implementation cycle time
- Open ECR/ECO backlog
- Change categories and trends

## 14. Continuous Improvement

- Annual review of CCB charter and processes
- Regular training for CCB members
- Lessons learned incorporated
- Process refinements as needed

## 15. Conflict Resolution

If consensus cannot be reached:
1. Issue elevated to Program Manager
2. Program Manager makes final decision
3. Decision documented with rationale

## 16. Signatures

This charter is approved by:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Program Manager | TBD | _________ | ____ |
| Chief Engineer | TBD | _________ | ____ |
| Configuration Manager | TBD | _________ | ____ |

---

**Effective Date:** TBD  
**Next Review Date:** TBD + 1 year  
**Document Owner:** Configuration Manager
