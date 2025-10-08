# Change Policy

> Location: `CONFIG_MGMT/06-CHANGES/01-POLICY/CHANGE_POLICY.md`  
> Authority: Configuration Control Board (CCB)

## Purpose

Define governance, thresholds, and evidence requirements for all configuration changes.

## Scope

All changes to baselined configuration items including:
- Aircraft and spacecraft hardware
- Software and firmware
- Ground support equipment (GSE)
- Documentation and specifications
- Test procedures and equipment
- Manufacturing processes affecting form, fit, or function

## Policy Statements

### 1. Change Authority

All changes to baselined configuration items require formal review and approval:
- **Class I changes** — CCB approval required
- **Class II changes** — Delegated approval (Engineering Manager + Quality)
- **Class III changes** — Configuration Manager approval

### 2. Baseline Control

Once a configuration item is baselined:
- No changes without approved ECR/ECO
- All changes tracked in **[../03-REGISTERS/CHANGE_REGISTER.csv](../03-REGISTERS/CHANGE_REGISTER.csv)**
- Baseline updates require CCB approval
- Changes linked to affected baseline in **[../03-REGISTERS/BASELINE_LINKS.csv](../03-REGISTERS/BASELINE_LINKS.csv)**

### 3. Change Threshold Criteria

#### Class I — Major Changes (CCB Approval Required)
- Affects form, fit, function, or interchangeability
- Safety-critical or certification-affecting changes
- Interface changes affecting external systems
- Changes requiring customer or regulatory approval
- Cost impact >$50K or schedule impact >2 weeks
- Changes to flight-critical software (DO-178C Level A/B)
- Changes to safety-critical hardware (DO-254 Category A)

#### Class II — Minor Changes (Delegated Approval)
- Documentation corrections (non-procedural)
- Performance optimizations (no functional change)
- Manufacturing process improvements (no FFF impact)
- Non-critical design refinements
- Internal interface changes (same subsystem)
- Cost impact $10K-$50K or schedule impact ≤2 weeks

#### Class III — Administrative (CM Approval)
- Editorial corrections
- Drawing clarifications (no design change)
- Reference updates
- Format changes
- Cost impact <$10K, no schedule impact

### 4. Evidence Requirements

All change requests must include:

**Minimum Requirements (All Classes):**
- Problem statement or justification
- Proposed solution description
- Affected items list (part numbers, documents)
- Impact assessment (technical, cost, schedule)
- Verification approach

**Additional Requirements for Class I:**
- Detailed impact analysis per **[../04-TEMPLATES/IMPACT_ASSESSMENT.md](../04-TEMPLATES/IMPACT_ASSESSMENT.md)**
- Safety assessment (if applicable) — link to **[../../QUALITY_QMS/13-RISK_SAFETY/](../../QUALITY_QMS/13-RISK_SAFETY/)**
- Certification impact analysis (FAA/EASA/ESA)
- Interface impact analysis — link to **[../09-INTERFACES/](../09-INTERFACES/)**
- Requirements traceability update
- Test/verification plan
- Implementation plan with schedule
- Risk assessment and mitigation

**Additional Requirements for Safety-Critical Changes:**
- Complete safety analysis per **[../04-TEMPLATES/CHECKLISTS/CLASS_I_CHECKLIST.md](../04-TEMPLATES/CHECKLISTS/CLASS_I_CHECKLIST.md)**
- Hazard analysis update (HARA/SSA/FTA/FMEA)
- Certification authority coordination plan
- Independent verification and validation (IV&V) plan

**Additional Requirements for Software Changes (DO-178C):**
- Requirements traceability matrix update
- Source code diff and analysis
- Structural coverage analysis
- Tool qualification impact
- Configuration management impact
- See **[../04-TEMPLATES/CHECKLISTS/SOFTWARE_DO178C_CHECKLIST.md](../04-TEMPLATES/CHECKLISTS/SOFTWARE_DO178C_CHECKLIST.md)**

**Additional Requirements for Hardware Changes (DO-254):**
- HDL/schematic changes with verification
- PAL/PSL coverage analysis
- Hardware verification plan
- See **[../04-TEMPLATES/CHECKLISTS/HARDWARE_DO254_CHECKLIST.md](../04-TEMPLATES/CHECKLISTS/HARDWARE_DO254_CHECKLIST.md)**

### 5. Review and Approval Process

**Class I Changes:**
1. Submit ECR with complete evidence package
2. Configuration Manager triages and routes
3. Technical reviewers assess impact (5 business days)
4. CCB reviews at next scheduled meeting
5. CCB disposition: Approve / Approve with Conditions / Reject / Defer
6. If approved, ECO issued for implementation
7. Implementation tracked in **[../06-ECO/ACTIVE/](../06-ECO/ACTIVE/)**

**Class II Changes:**
1. Submit ECR with required evidence
2. Configuration Manager routes to delegated approvers
3. Engineering Manager and Quality review (3 business days)
4. Approval documented, ECO issued
5. Implementation proceeds

**Class III Changes:**
1. Submit ECR (may use simplified form)
2. Configuration Manager reviews and approves (1 business day)
3. Implementation proceeds

### 6. Emergency Changes

For critical safety or operational issues:
- Emergency CCB meeting convened (24-hour notice)
- Streamlined review process
- Temporary approval possible with follow-up documentation
- Retroactive CCB review at next scheduled meeting
- All evidence requirements still apply

### 7. Customer and Regulatory Coordination

Changes affecting customer obligations or regulatory compliance:
- Customer notification required for Class I changes
- Regulatory authority coordination for certification-affecting changes
- Customer approval may be required per contract
- Document in **[../17-NOTICES/CUSTOMER_NOTICES/](../17-NOTICES/CUSTOMER_NOTICES/)** and **[../17-NOTICES/REGULATORY_NOTICES/](../17-NOTICES/REGULATORY_NOTICES/)**

### 8. Traceability

All changes must maintain traceability:
- Requirements affected → update **[../10-TRACEABILITY/](../10-TRACEABILITY/)**
- Baseline affected → update **[../03-REGISTERS/BASELINE_LINKS.csv](../03-REGISTERS/BASELINE_LINKS.csv)**
- Interfaces affected → update **[../09-INTERFACES/](../09-INTERFACES/)**
- Software changes → update **[../11-SOFTWARE_CHANGES/TRACEABILITY.json](../11-SOFTWARE_CHANGES/TRACEABILITY.json)**

### 9. Deviations and Waivers

**Deviations** — One-time departure from requirements:
- Use for prototype/test articles
- Limited scope and quantity
- Temporary acceptance
- Requires technical justification
- CCB approval for Class I items
- See **[../02-WORKFLOW/DEVIATION_WAIVER_WORKFLOW.md](../02-WORKFLOW/DEVIATION_WAIVER_WORKFLOW.md)**

**Waivers** — Permanent acceptance of non-conformance:
- Engineering justification required
- May require customer approval
- Must not affect safety or certification
- CCB approval required
- Document in **[../08-WAIVERS/](../08-WAIVERS/)**

### 10. Material Review Board (MRB)

For non-conforming material:
- MRB convened for disposition
- Options: Use-As-Is, Rework, Repair, Scrap
- Links to **[../../QUALITY_QMS/06-NCR_CAPA/MRB/](../../QUALITY_QMS/06-NCR_CAPA/MRB/)**
- See **[../09-MRB/00-README.md](../09-MRB/00-README.md)**

## Metrics and Performance

Change management effectiveness tracked via:
- **Cycle Time** — ECR submission to closure
- **First-Pass Approval Rate** — CCB approvals without revision
- **Backlog** — Open ECRs by class and age
- **Rework Rate** — Changes requiring re-submission
- **Implementation On-Time** — ECO completion vs. plan

Metrics reported quarterly to Program Management.

## Continuous Improvement

Annual policy review by:
- Configuration Manager
- CCB Chair
- Quality Manager
- Lessons learned from previous year incorporated

## Related Documents

- **[CLASSIFICATION.md](./CLASSIFICATION.md)** — Change classification details
- **[NUMBERING_CONVENTION.md](./NUMBERING_CONVENTION.md)** — ECR/ECO numbering scheme
- **[RASCI.md](./RASCI.md)** — Roles and responsibilities
- **[../02-WORKFLOW/ECR_WORKFLOW.md](../02-WORKFLOW/ECR_WORKFLOW.md)** — ECR process flow
- **[../02-WORKFLOW/ECO_WORKFLOW.md](../02-WORKFLOW/ECO_WORKFLOW.md)** — ECO process flow
- **[../../05-CCB/00-CHARTER.md](../../05-CCB/00-CHARTER.md)** — CCB charter
- **[../../QUALITY_QMS/02-PROCEDURES/PRO-003_CHANGE_CONTROL.md](../../QUALITY_QMS/02-PROCEDURES/PRO-003_CHANGE_CONTROL.md)** — QMS change procedure

## Compliance

- **AS9100D** — Clause 8.5.6 (Control of Changes)
- **ISO 10007** — Configuration Management Guidelines
- **ARP4754A** — Section 10 (Configuration Management)
- **ECSS-M-ST-40C** — Space Configuration Management
- **DO-178C** — Software Configuration Management (Section 7)
- **DO-254** — Hardware Configuration Management

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-15 | Configuration Manager | Initial release |
