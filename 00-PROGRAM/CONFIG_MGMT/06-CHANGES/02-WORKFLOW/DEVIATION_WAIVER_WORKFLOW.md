# Deviation and Waiver Workflow

> Location: `CONFIG_MGMT/06-CHANGES/02-WORKFLOW/DEVIATION_WAIVER_WORKFLOW.md`  
> Authority: Configuration Control Board (CCB)

## Purpose

Define the process for requesting, reviewing, and dispositioning deviations and waivers.

## Definitions

**Deviation:** One-time departure from a requirement or specification for a specific unit, lot, or production run.
- Temporary acceptance
- Limited scope and quantity
- No permanent design change
- Typically used for prototypes, test articles, or specific production lots

**Waiver:** Permanent acceptance of a non-conformance to a requirement or specification.
- Permanent acceptance
- May affect multiple units or all future production
- Engineering justification required
- Must not affect safety or certification (typically)
- May require customer approval

---

## Deviation Workflow

### When to Use

- Prototype or test article doesn't meet full requirements
- Production part has minor non-conformance (one-time)
- Temporary workaround while permanent fix is developed
- Cost/schedule constraint for limited quantity

### Process

**1. Submit Deviation Request**

**Responsible:** Originator (Engineering, Manufacturing, Quality)

**Actions:**
1. Complete deviation request using **[../04-TEMPLATES/DEVIATION.yml](../04-TEMPLATES/DEVIATION.yml)**
2. Provide:
   - Requirement being deviated
   - Affected items (part numbers, serial numbers, lot numbers)
   - Quantity affected
   - Technical justification
   - Impact assessment (safety, performance, interfaces)
   - Duration/effectivity
   - Mitigation (if applicable)
3. Submit to Configuration Manager

**2. Technical Review**

**Responsible:** Engineering, Quality, Safety (as applicable)

**Actions:**
1. Assess technical acceptability
2. Evaluate safety impact
3. Evaluate performance impact
4. Evaluate interface impact
5. Provide recommendation: Approve / Reject

**3. CCB Approval (Class I items)**

**Responsible:** CCB

**Actions:**
1. Review deviation request and technical assessments
2. Discuss risks and mitigations
3. Vote on disposition
4. Document decision

**4. Implementation and Tracking**

**Responsible:** Configuration Manager

**Actions:**
1. Assign deviation number (format: `DEV-YYYY-####`)
2. Record in **[../03-REGISTERS/CHANGE_REGISTER.csv](../03-REGISTERS/CHANGE_REGISTER.csv)**
3. Move to **[../07-DEVIATIONS/OPEN/](../07-DEVIATIONS/OPEN/)**
4. Track effectivity (serial numbers, quantities)
5. Notify affected parties
6. Update as-built records

**5. Closure**

**Actions:**
1. Verify deviation effectivity complete
2. If permanent fix developed, link to ECR/ECO
3. Close deviation
4. Move to **[../07-DEVIATIONS/CLOSED/](../07-DEVIATIONS/CLOSED/)**

---

## Waiver Workflow

### When to Use

- Permanent relaxation of requirement
- Engineering trade-off accepted
- Requirement found to be overly restrictive
- Cost/benefit analysis supports acceptance
- Must not affect safety or certification (typically)

### Process

**1. Submit Waiver Request**

**Responsible:** Originator (Engineering, typically)

**Actions:**
1. Complete waiver request using **[../04-TEMPLATES/WAIVER.yml](../04-TEMPLATES/WAIVER.yml)**
2. Provide:
   - Requirement being waived
   - Affected items (all or specific configurations)
   - Technical justification
   - Engineering analysis supporting waiver
   - Impact assessment (safety, performance, certification, customer)
   - Risk assessment
   - Verification approach (if modified requirement)
3. Submit to Configuration Manager

**2. Comprehensive Technical Review**

**Responsible:** Engineering, Quality, Safety, Systems Engineering

**Actions:**
1. Detailed technical assessment
2. Safety analysis (must demonstrate no safety impact or acceptable risk)
3. Certification impact analysis
4. Performance impact analysis
5. System-level impact analysis
6. Customer impact analysis
7. Provide recommendation with strong justification

**3. CCB Approval**

**Responsible:** CCB (always required for waivers)

**Actions:**
1. Review waiver request and all technical assessments
2. Discuss implications and risks
3. Ensure engineering justification is sound
4. Vote on disposition
5. Document decision with detailed rationale

**4. Customer Approval (if required)**

**Responsible:** Configuration Manager, Program Manager

**Actions:**
1. Determine if customer approval required (per contract)
2. Prepare customer notification
3. Submit to customer for approval
4. Track customer response
5. Document customer decision

**5. Implementation and Tracking**

**Responsible:** Configuration Manager

**Actions:**
1. Assign waiver number (format: `WAIV-YYYY-####`)
2. Record in **[../03-REGISTERS/CHANGE_REGISTER.csv](../03-REGISTERS/CHANGE_REGISTER.csv)**
3. Move to **[../08-WAIVERS/OPEN/](../08-WAIVERS/OPEN/)**
4. Update requirements database (if applicable)
5. Update specifications/drawings with waiver note
6. Update baseline
7. Notify all affected parties
8. Update verification plans (if applicable)

---

## Decision Criteria

### Deviation Approval Criteria

- [ ] Technical justification adequate
- [ ] No safety impact or acceptable safety risk with mitigation
- [ ] No certification impact or authority concurrence obtained
- [ ] Limited scope and quantity clearly defined
- [ ] Effectivity clearly identified
- [ ] As-built records will be updated
- [ ] Temporary nature acceptable

### Waiver Approval Criteria

- [ ] Strong engineering justification
- [ ] No unacceptable safety impact
- [ ] No adverse certification impact or authority approval obtained
- [ ] Customer approval obtained (if required)
- [ ] Permanent acceptance is appropriate
- [ ] Requirements traceability maintained
- [ ] Verification approach updated (if applicable)
- [ ] Baseline documentation updated

---

## Effectivity Tracking

**Deviations:**
- Track by serial number, lot number, or date range
- Record in as-built configuration
- Maintain in **[../07-DEVIATIONS/OPEN/](../07-DEVIATIONS/OPEN/)**

**Waivers:**
- Apply to all future units unless otherwise specified
- Update baseline requirements
- Maintain in **[../08-WAIVERS/OPEN/](../08-WAIVERS/OPEN/)**

---

## Relationship to ECR/ECO

**Deviation → ECR:**
- Deviation identifies need for permanent fix
- ECR submitted to implement design change
- Once ECO implemented, deviation can be closed

**Waiver → Baseline:**
- Waiver accepted as permanent
- Baseline updated to reflect waived requirement
- No ECR/ECO needed unless reverting waiver

---

## Related Documents

- **[ECR_WORKFLOW.md](./ECR_WORKFLOW.md)** — ECR process
- **[../01-POLICY/CHANGE_POLICY.md](../01-POLICY/CHANGE_POLICY.md)** — Change policy
- **[../04-TEMPLATES/DEVIATION.yml](../04-TEMPLATES/DEVIATION.yml)** — Deviation template
- **[../04-TEMPLATES/WAIVER.yml](../04-TEMPLATES/WAIVER.yml)** — Waiver template
- **[../../05-CCB/00-CHARTER.md](../../05-CCB/00-CHARTER.md)** — CCB charter

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-15 | Configuration Manager | Initial release |
