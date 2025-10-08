# Configuration Control Board (CCB) Charter

> Location: `CONFIG_MGMT/05-CCB/CCB_CHARTER.md`  
> Governance: see **[../GOVERNANCE.md](../GOVERNANCE.md)**

## 1. Purpose
Provide governance and decision authority for all changes to **baselined configuration items**.

## 2. Authority
Under Program Manager authority. Responsibilities:
- Review and disposition all **ECRs** (**[../06-CHANGES/ECR/](../06-CHANGES/ECR/)**)
- Approve or reject **ECOs** (**[../06-CHANGES/ECO/](../06-CHANGES/ECO/)**)
- Authorize **deviations** (**[../06-CHANGES/DEVIATIONS/](../06-CHANGES/DEVIATIONS/)**) and **waivers** (**[../06-CHANGES/WAIVERS/](../06-CHANGES/WAIVERS/)**)
- Establish and maintain program **baselines** (**[../04-BASELINES/](../04-BASELINES/)**)
- Ensure change impact assessment and configuration integrity

## 3. Scope
Aircraft, spacecraft, GSE, software/firmware, documentation/specs, test procedures/equipment, manufacturing processes affecting FFF.

## 4. CCB Membership

### 4.1 Voting Members
| Role | Responsibility |
|---|---|
| **CCB Chair** | Final decision authority |
| **Chief Engineer** | Technical assessment |
| **Systems Engineer** | System impact |
| **Quality Manager** | Quality/compliance |
| **Manufacturing Manager** | Producibility/cost |
| **Test Manager** | Test impact |
| **Safety Manager** | Safety/risk |
| **Certification Manager** | Regulatory impact |

### 4.2 Non-Voting
| Role | Responsibility |
|---|---|
| **Configuration Manager** | Secretary, records |
| **Procurement** | Supply chain impact |
| **Finance** | Cost analysis |
| **Customer Rep** | Customer interests |

Members list: **[./01-MEMBERS.md](./01-MEMBERS.md)**

### 4.3 Ad-Hoc
SMEs invited as needed.

## 5. CCB Meetings
- **Regular:** Weekly (dev), bi-weekly (prod). ≤2h. In-person/virtual.
- **Emergency:** Called by Chair. ≥24h notice when possible.
- **Agenda:** Minutes review → Actions → New ECRs → Pending ECOs → Deviations/Waivers → Baseline status → Metrics.

Minutes stored in **[./02-MINUTES/](./02-MINUTES/)**.

## 6. Decision Process
**Quorum:** ≥5 voting, incl. Chair (or delegate) and Chief Engineer.  
**Voting:** Consensus preferred; majority >50%; Chair veto allowed; abstentions excluded.  
**Dispositions:** Approved · Approved w/ conditions · Rejected · Deferred · Returned for rework.

## 7. Change Classification
- **Class I:** FFF, safety/certification, interchangeability, customer approval → **Full CCB approval**
- **Class II:** Minor/doc/process → **Chair + Chief Engineer**
- **Class III:** Administrative/typos → **Configuration Manager**

## 8. ECR/ECO Process

### 8.1 ECR Submission
1. Originator completes **ECR** (**[../13-TEMPLATES/ECR.yml](../13-TEMPLATES/ECR.yml)**).  
2. Submit to CM.  
3. CM assigns ECR ID and routes.  
4. Technical assessment.  
5. CCB disposition.

### 8.2 ECO Implementation
1. Approved ECR becomes ECO.  
2. CM assigns ECO ID.  
3. Plan and execute implementation.  
4. QA verification.  
5. Close ECO.

### 8.3 Tracking
All records in **[../06-CHANGES/ECR/](../06-CHANGES/ECR/)** and **[../06-CHANGES/ECO/](../06-CHANGES/ECO/)**.

## 9. Deviation and Waiver
- **Deviation:** One-time departure. No safety impact. **CCB approval**. Track **[../06-CHANGES/DEVIATIONS/](../06-CHANGES/DEVIATIONS/)**.  
- **Waiver:** Permanent acceptance. Engineering justification; may need customer approval. **CCB approval**. Track **[../06-CHANGES/WAIVERS/](../06-CHANGES/WAIVERS/)**.

## 10. Baseline Management
**Establishment:** SRR, PDR, CDR, TRR, PRR, ORR/EIS, FRR.  
**Control:** All changes to baselined items require CCB approval (Class I).  
Baselines archived in **[../04-BASELINES/](../04-BASELINES/)**. Status accounting per **[../10-TRACEABILITY/CHANGE_BASELINE.csv](../10-TRACEABILITY/CHANGE_BASELINE.csv)**.

## 11. Roles

**CCB Chair:** Lead meetings, final decisions, report metrics.  
**Configuration Manager:** Agenda, materials (48h prior), minutes (publish <24h), actions, records.  
**Voting Members:** Pre-read, impact assessment, vote, execute actions.

## 12. Documentation
**Minutes content:** attendees, ECRs, dispositions/votes, actions, baseline status.  
Retention: Minutes — permanent; ECR/ECO/Deviation/Waiver — program life +10 years.

## 13. Metrics
ECRs/month, approval rate, ECR cycle time, ECO implementation time, open backlog, category trends. Report via **[../11-AUDITS/](../11-AUDITS/)** and PM dashboard.

## 14. Continuous Improvement
Annual charter review, member training, lessons learned, process updates.

## 15. Conflict Resolution
Escalate to Program Manager → final decision → record rationale in minutes.

## 16. Signatures
| Role | Name | Signature | Date |
|---|---|---|---|
| Program Manager | TBD | ______ | ____ |
| Chief Engineer | TBD | ______ | ____ |
| Configuration Manager | TBD | ______ | ____ |

---

**Effective Date:** TBD  
**Next Review:** TBD + 1 year  
**Owner:** Configuration Manager
```

