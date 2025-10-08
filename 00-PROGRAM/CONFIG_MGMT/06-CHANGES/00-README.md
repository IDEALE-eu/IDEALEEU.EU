# Change Management (06-CHANGES)

> Location: `CONFIG_MGMT/06-CHANGES/`  
> Authority: Configuration Control Board (CCB) — **[../05-CCB/](../05-CCB/)**  
> Governance: **[../GOVERNANCE.md](../GOVERNANCE.md)**

## Purpose

Systematic control and documentation of all changes to baselined configuration items throughout the program lifecycle.

## Scope

All changes to:
- Aircraft and spacecraft design
- Software and firmware
- Hardware components
- Manufacturing processes
- Test procedures
- Documentation and specifications
- Interfaces (ICDs)

## Authority

The **Configuration Control Board (CCB)** has authority over all changes to baselined items:
- Review and disposition **ECRs** (Engineering Change Requests)
- Approve or reject **ECOs** (Engineering Change Orders)
- Authorize **deviations** and **waivers**
- Maintain baseline integrity

See **[../05-CCB/00-CHARTER.md](../05-CCB/00-CHARTER.md)** for CCB charter and authority.

## Contents

### Policy and Governance
- **[01-POLICY/](./01-POLICY/)** — Change policies, classification, numbering, roles
  - **[CHANGE_POLICY.md](./01-POLICY/CHANGE_POLICY.md)** — Governance and thresholds
  - **[CLASSIFICATION.md](./01-POLICY/CLASSIFICATION.md)** — Class I/II/III definitions
  - **[NUMBERING_CONVENTION.md](./01-POLICY/NUMBERING_CONVENTION.md)** — ECR/ECO/DEV/WAIV numbering
  - **[RASCI.md](./01-POLICY/RASCI.md)** — Roles and responsibilities matrix

### Workflows
- **[02-WORKFLOW/](./02-WORKFLOW/)** — Change process workflows
  - **[ECR_WORKFLOW.md](./02-WORKFLOW/ECR_WORKFLOW.md)** — Submit → Triage → Impact → CCB → Disposition
  - **[ECO_WORKFLOW.md](./02-WORKFLOW/ECO_WORKFLOW.md)** — Plan → Implement → Verify → Close → Baseline
  - **[DEVIATION_WAIVER_WORKFLOW.md](./02-WORKFLOW/DEVIATION_WAIVER_WORKFLOW.md)** — Temporary vs. permanent
  - **[MRB_WORKFLOW.md](./02-WORKFLOW/MRB_WORKFLOW.md)** — Material Review Board process

### Registers and Tracking
- **[03-REGISTERS/](./03-REGISTERS/)** — Change tracking and status
  - **[CHANGE_REGISTER.csv](./03-REGISTERS/CHANGE_REGISTER.csv)** — Master change log
  - **[OPEN_ITEMS.csv](./03-REGISTERS/OPEN_ITEMS.csv)** — Pending actions tracker
  - **[BASELINE_LINKS.csv](./03-REGISTERS/BASELINE_LINKS.csv)** — Change-to-baseline mapping
  - **[CUSTOMER_NOTICES.csv](./03-REGISTERS/CUSTOMER_NOTICES.csv)** — Regulatory notifications

### Templates
- **[04-TEMPLATES/](./04-TEMPLATES/)** — Standard forms and checklists
  - **[ECR.yml](./04-TEMPLATES/ECR.yml)** — Engineering Change Request template
  - **[ECO.yml](./04-TEMPLATES/ECO.yml)** — Engineering Change Order template
  - **[IMPACT_ASSESSMENT.md](./04-TEMPLATES/IMPACT_ASSESSMENT.md)** — Impact analysis template
  - **[DEVIATION.yml](./04-TEMPLATES/DEVIATION.yml)** — Deviation request template
  - **[WAIVER.yml](./04-TEMPLATES/WAIVER.yml)** — Waiver request template
  - **[MRB_FORM.md](./04-TEMPLATES/MRB_FORM.md)** — Material Review Board form
  - **[CHECKLISTS/](./04-TEMPLATES/CHECKLISTS/)** — Domain-specific checklists

### Active Changes
- **[05-ECR/](./05-ECR/)** — Engineering Change Requests
  - **[INBOX/](./05-ECR/INBOX/)** — Untriaged submissions
  - **[ACTIVE/](./05-ECR/ACTIVE/)** — Under review
  - **[CLOSED/](./05-ECR/CLOSED/)** — Completed or rejected

- **[06-ECO/](./06-ECO/)** — Engineering Change Orders
  - **[ACTIVE/](./06-ECO/ACTIVE/)** — Implementation in progress
  - **[CLOSED/](./06-ECO/CLOSED/)** — Completed changes

- **[07-DEVIATIONS/](./07-DEVIATIONS/)** — One-time departures
  - **[OPEN/](./07-DEVIATIONS/OPEN/)** — Active deviations
  - **[CLOSED/](./07-DEVIATIONS/CLOSED/)** — Completed deviations

- **[08-WAIVERS/](./08-WAIVERS/)** — Permanent acceptances
  - **[OPEN/](./08-WAIVERS/OPEN/)** — Active waivers
  - **[CLOSED/](./08-WAIVERS/CLOSED/)** — Completed waivers

- **[09-MRB/](./09-MRB/)** — Material Review Board
  - **[00-README.md](./09-MRB/00-README.md)** — MRB overview
  - **[DECISIONS/](./09-MRB/DECISIONS/)** — Use-As-Is, Rework, Repair, Scrap
  - **[LINKS.md](./09-MRB/LINKS.md)** — Links to QMS NCR/CAPA

### Impact Analysis
- **[10-IMPACTS/](./10-IMPACTS/)** — Domain-specific impact assessments
  - **[SAFETY/](./10-IMPACTS/SAFETY/)** — Safety and risk analysis
  - **[CERTIFICATION/](./10-IMPACTS/CERTIFICATION/)** — Regulatory impact (DO-160/178C/254, ECSS)
  - **[INTERFACES/](./10-IMPACTS/INTERFACES/)** — ICD and interface changes
  - **[COST_SCHEDULE/](./10-IMPACTS/COST_SCHEDULE/)** — Cost and schedule impact
  - **[SUPPLY_CHAIN/](./10-IMPACTS/SUPPLY_CHAIN/)** — Supplier and AVL impact

### Domain-Specific Changes
- **[11-SOFTWARE_CHANGES/](./11-SOFTWARE_CHANGES/)** — Software change management
  - **[SW_CHANGE_LOG.md](./11-SOFTWARE_CHANGES/SW_CHANGE_LOG.md)** — Software change history
  - **[TRACEABILITY.json](./11-SOFTWARE_CHANGES/TRACEABILITY.json)** — Req ↔ Code ↔ Test (DO-178C)
  - **[TOOLING.md](./11-SOFTWARE_CHANGES/TOOLING.md)** — Tools and qualification

- **[12-INTERFACE_CHANGES/](./12-INTERFACE_CHANGES/)** — Interface change control
  - **[ICD_CHANGE_LOG.csv](./12-INTERFACE_CHANGES/ICD_CHANGE_LOG.csv)** — ICD version history
  - **[COMPATIBILITY_MATRIX.md](./12-INTERFACE_CHANGES/COMPATIBILITY_MATRIX.md)** — Compatibility tracking

### Automation and Metrics
- **[13-AUTOMATION/](./13-AUTOMATION/)** — Validation and CI/CD
  - **[GATES.md](./13-AUTOMATION/GATES.md)** — Pre-merge validation gates
  - **[CI_HOOKS.md](./13-AUTOMATION/CI_HOOKS.md)** — CI/CD integration
  - **[SCRIPTS/](./13-AUTOMATION/SCRIPTS/)** — Validation scripts

- **[14-METRICS/](./14-METRICS/)** — Change management metrics
  - **[CYCLE_TIME.csv](./14-METRICS/CYCLE_TIME.csv)** — Lead time tracking
  - **[BACKLOG_TRENDS.csv](./14-METRICS/BACKLOG_TRENDS.csv)** — Backlog analysis
  - **[FIRST_PASS_APPROVAL_RATE.csv](./14-METRICS/FIRST_PASS_APPROVAL_RATE.csv)** — CCB efficiency

### Audit and Packages
- **[15-AUDIT/](./15-AUDIT/)** — Audit trail and evidence
  - **[EVIDENCE_INDEX.md](./15-AUDIT/EVIDENCE_INDEX.md)** — Evidence mapping
  - **[SNAPSHOTS/](./15-AUDIT/SNAPSHOTS/)** — Signed approval records

- **[16-CHANGE_PACKAGES/](./16-CHANGE_PACKAGES/)** — Immutable change packages
  - Archived ZIP files: `CP-ECO-YYYY-####_vN.zip`

- **[17-NOTICES/](./17-NOTICES/)** — External notifications
  - **[CUSTOMER_NOTICES/](./17-NOTICES/CUSTOMER_NOTICES/)** — Customer communications
  - **[REGULATORY_NOTICES/](./17-NOTICES/REGULATORY_NOTICES/)** — Regulatory submissions

## Key Workflows

### ECR Process
1. **Submit** — Originator completes ECR using **[04-TEMPLATES/ECR.yml](./04-TEMPLATES/ECR.yml)**
2. **Triage** — CM assigns number, routes to **[05-ECR/INBOX/](./05-ECR/INBOX/)**
3. **Impact Assessment** — Technical review, complete **[04-TEMPLATES/IMPACT_ASSESSMENT.md](./04-TEMPLATES/IMPACT_ASSESSMENT.md)**
4. **CCB Review** — Present at CCB meeting (**[../05-CCB/](../05-CCB/)**)
5. **Disposition** — Approve (→ ECO), Reject, or Defer

### ECO Process
1. **Plan** — Create implementation plan
2. **Implement** — Execute changes per plan
3. **Verify** — Test and validate changes
4. **Close** — Complete verification, update baseline
5. **Archive** — Package in **[16-CHANGE_PACKAGES/](./16-CHANGE_PACKAGES/)**

## Change Classification

### Class I — Major Changes
- Affects form, fit, function, or certification
- Safety or performance critical
- Requires CCB approval
- May require customer/regulatory approval

### Class II — Minor Changes
- Documentation corrections
- Non-critical design refinements
- Process improvements
- Delegated approval authority

### Class III — Administrative
- Editorial changes
- Non-technical updates
- CM approval only

See **[01-POLICY/CLASSIFICATION.md](./01-POLICY/CLASSIFICATION.md)** for detailed criteria.

## Cross-References

### Internal Links
- **Baselines:** **[../04-BASELINES/](../04-BASELINES/)** — Gate baselines
- **CCB:** **[../05-CCB/](../05-CCB/)** — Control board charter
- **Interfaces:** **[../09-INTERFACES/](../09-INTERFACES/)** — ICDs
- **Traceability:** **[../10-TRACEABILITY/](../10-TRACEABILITY/)** — Change tracking
- **CI/CD:** **[../12-CI_CD_RULES/](../12-CI_CD_RULES/)** — Version control integration
- **Templates:** **[../13-TEMPLATES/](../13-TEMPLATES/)** — Original ECR/ECO templates

### External Links
- **Quality QMS:** **[../../QUALITY_QMS/02-PROCEDURES/PRO-003_CHANGE_CONTROL.md](../../QUALITY_QMS/02-PROCEDURES/PRO-003_CHANGE_CONTROL.md)**
- **Quality NCR/CAPA:** **[../../QUALITY_QMS/06-NCR_CAPA/](../../QUALITY_QMS/06-NCR_CAPA/)**
- **Risk Management:** **[../../QUALITY_QMS/13-RISK_SAFETY/](../../QUALITY_QMS/13-RISK_SAFETY/)**
- **Supply Chain:** **[../../SUPPLY_CHAIN/](../../SUPPLY_CHAIN/)**
- **Digital Thread:** **[../../DIGITAL_THREAD/](../../DIGITAL_THREAD/)**

## Compliance

### Standards
- **AS9100D** — Quality management (aerospace)
- **ISO 10007** — Configuration management guidelines
- **ARP4754A** — Aircraft systems development
- **ECSS-M-ST-40C** — Space configuration management
- **DO-178C** — Software (airborne systems)
- **DO-254** — Hardware (airborne electronic hardware)
- **DO-160G** — Environmental conditions and test procedures

### Regulatory
- **FAA** — Federal Aviation Administration (14 CFR)
- **EASA** — European Union Aviation Safety Agency (CS-25, CS-E)
- **ESA** — European Space Agency (ECSS)

## Roles & Responsibilities

| Role | Responsibility |
|------|----------------|
| **Configuration Manager** | Process owner, change tracking, baseline control |
| **CCB Chair** | Final approval authority, meeting chair |
| **CCB Members** | Review and vote on changes |
| **Change Originator** | Submit ECR, provide technical details |
| **Technical Reviewer** | Impact assessment, feasibility |
| **Implementation Team** | Execute approved ECOs |
| **Quality** | Verification, audit, compliance |

See **[01-POLICY/RASCI.md](./01-POLICY/RASCI.md)** for detailed RASCI matrix.

## Metrics and Reporting

Key performance indicators:
- **Cycle Time** — Request to closure duration
- **Backlog** — Open ECRs by class and system
- **Approval Rate** — First-pass CCB approval percentage
- **Effectivity** — Implementation on schedule
- **Rework** — Changes requiring revision

Metrics tracked in **[14-METRICS/](./14-METRICS/)** and reported to Program Management.

## Contact

**Configuration Manager:** [See CCB Members](../05-CCB/01-MEMBERS.md)  
**CCB Chair:** [See CCB Charter](../05-CCB/00-CHARTER.md)  
**Change Requests:** Submit to CM via ECR template
