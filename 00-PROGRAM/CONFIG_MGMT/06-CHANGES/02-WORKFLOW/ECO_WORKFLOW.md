# ECO Workflow

> Location: `CONFIG_MGMT/06-CHANGES/02-WORKFLOW/ECO_WORKFLOW.md`  
> Authority: Configuration Manager

## Purpose

Define the Engineering Change Order (ECO) process from planning through closure and baseline update.

## Workflow Overview

```
Plan → Implement → Verify → Close → Baseline Update
```

## Process Steps

### 1. Plan Implementation

**Responsible:** Implementation Lead, Configuration Manager

**Trigger:** ECR approved by CCB, ECO issued

**Actions:**
1. Configuration Manager:
   - Issues ECO using template **[../04-TEMPLATES/ECO.yml](../04-TEMPLATES/ECO.yml)**
   - Assigns ECO number (format: `ECO-YYYY-####`)
   - Links to source ECR
   - Creates ECO folder in **[../06-ECO/ACTIVE/](../06-ECO/ACTIVE/)**
   - Notifies implementation team

2. Implementation Lead:
   - Reviews approved ECR and impact assessment
   - Develops detailed implementation plan:
     * Task breakdown
     * Resource assignments
     * Schedule with milestones
     * Dependencies
     * Risk mitigation actions
   - Identifies affected configuration items
   - Coordinates with:
     * Engineering (design changes)
     * Manufacturing (process changes)
     * Quality (verification approach)
     * Supply Chain (supplier coordination)
     * Test (verification testing)
   - Establishes verification criteria
   - Develops rollback plan (if needed)

3. Review and approval of implementation plan:
   - Engineering Manager reviews technical approach
   - Quality Manager reviews verification approach
   - Configuration Manager reviews baseline impact

**Outputs:**
- ECO document issued
- Implementation plan approved
- Resource assignments confirmed
- Schedule established
- Verification plan defined

**Duration:** 1-2 weeks

---

### 2. Implement Changes

**Responsible:** Implementation Team (Engineering, Manufacturing, Quality, etc.)

**Actions:**

**Design Changes:**
1. Update drawings, specifications, models
2. Update CAD/SysML models
3. Review and approve changes per drawing release process
4. Update part numbers/revisions
5. Update Bill of Materials (BOM)
6. Update Interface Control Documents (ICDs) if applicable

**Software Changes:**
1. Create branch per **[../../12-CI_CD_RULES/BRANCHING_MODEL.md](../../12-CI_CD_RULES/BRANCHING_MODEL.md)**
2. Implement code changes
3. Update requirements traceability
4. Update software configuration management records
5. Perform code reviews
6. Update software documentation
7. Track in **[../11-SOFTWARE_CHANGES/SW_CHANGE_LOG.md](../11-SOFTWARE_CHANGES/SW_CHANGE_LOG.md)**

**Manufacturing Changes:**
1. Update work instructions
2. Modify or create tooling
3. Update manufacturing processes
4. Update inspection procedures
5. Train personnel on new procedures
6. Coordinate with suppliers (if applicable)

**Documentation Changes:**
1. Update technical manuals
2. Update test procedures
3. Update maintenance procedures
4. Update training materials
5. Update safety documentation

**Configuration Management:**
1. Update Item Master database
2. Update traceability matrices
3. Update baseline links
4. Maintain change log

**Progress Tracking:**
1. Implementation Lead tracks activities
2. Weekly status updates to Configuration Manager
3. Issues and risks logged and managed
4. Schedule updates as needed

**Outputs:**
- All planned changes implemented
- Documentation updated
- Traceability maintained
- Progress tracked

**Duration:** 2-12 weeks (varies by scope and complexity)

---

### 3. Verify Changes

**Responsible:** Quality, Test, Implementation Team

**Actions:**

**Verification Activities:**
1. Execute verification per plan:
   - **Test:** Execute test procedures, record results
   - **Analysis:** Perform required analyses (structural, thermal, etc.)
   - **Demonstration:** Demonstrate functionality
   - **Inspection:** Inspect physical changes

2. Software verification (if applicable):
   - Unit testing
   - Integration testing
   - Regression testing
   - Structural coverage analysis (DO-178C)
   - Requirements-based testing

3. Hardware verification (if applicable):
   - Functional testing
   - Environmental testing (DO-160G)
   - Safety verification

4. Safety verification (if safety-critical):
   - Hazard analysis review
   - Safety assessment update
   - Independent safety review

5. Certification coordination (if applicable):
   - Regulatory authority review
   - Compliance documentation
   - Authority approval/acceptance

**Verification Documentation:**
1. Test reports
2. Analysis reports
3. Inspection records
4. Compliance statements
5. Safety assessment updates
6. Certification evidence

**Non-Conformance Handling:**
- If verification fails:
  1. Document non-conformance
  2. Root cause analysis
  3. Determine corrective action
  4. Re-verify after correction
  5. May require ECR/MRB if design inadequate

**Outputs:**
- Verification complete
- All acceptance criteria met
- Verification reports documented
- Non-conformances resolved

**Duration:** 2-8 weeks (varies by scope and complexity)

---

### 4. Close ECO

**Responsible:** Configuration Manager, Implementation Lead

**Actions:**

1. **Verification Review:**
   - Quality Manager confirms verification complete
   - All acceptance criteria met
   - All documentation complete

2. **Configuration Updates:**
   - Configuration Manager updates:
     * Item Master database
     * Baseline links per **[../03-REGISTERS/BASELINE_LINKS.csv](../03-REGISTERS/BASELINE_LINKS.csv)**
     * Change register per **[../03-REGISTERS/CHANGE_REGISTER.csv](../03-REGISTERS/CHANGE_REGISTER.csv)**
     * Traceability matrices

3. **Documentation Completion:**
   - Compile final ECO package:
     * ECO document
     * Implementation plan and actual execution
     * Verification reports
     * Updated drawings/specifications
     * Traceability updates
     * Lessons learned

4. **Lessons Learned:**
   - What went well?
   - What could be improved?
   - Recommendations for future changes

5. **CCB Closure Review (Class I):**
   - Present closure package to CCB
   - CCB reviews and approves closure
   - CCB minutes document closure

6. **Archive:**
   - Create change package: `CP-ECO-YYYY-####_v1.zip`
   - Store in **[../16-CHANGE_PACKAGES/](../16-CHANGE_PACKAGES/)**
   - Move ECO from **[../06-ECO/ACTIVE/](../06-ECO/ACTIVE/)** to **[../06-ECO/CLOSED/](../06-ECO/CLOSED/)**

7. **Notification:**
   - Notify stakeholders of closure
   - Notify customer (if required)
   - Update project schedule/status

**Outputs:**
- ECO closed
- Final package archived
- Lessons learned documented
- Stakeholders notified

**Duration:** 1-2 weeks

---

### 5. Update Baseline

**Responsible:** Configuration Manager

**Trigger:** ECO closed, baseline update required

**Actions:**
1. Identify baseline affected (SRR, PDR, CDR, etc.)
2. Update baseline manifest in **[../../04-BASELINES/](../../04-BASELINES/)**
3. Update baseline changelog
4. Tag new baseline version (if major update)
5. CCB approves baseline update
6. Notify stakeholders of baseline change
7. Update digital thread references

**Outputs:**
- Baseline updated
- Baseline version incremented (if applicable)
- Traceability maintained
- Stakeholders notified

**Duration:** 1 week

---

## Total Cycle Time

**Typical Duration (from ECO issuance to closure):**
- **Minor changes:** 4-8 weeks
- **Moderate changes:** 8-16 weeks
- **Major changes:** 16-26 weeks

**Factors affecting duration:**
- Complexity of changes
- Number of affected items
- Verification scope
- Supplier coordination requirements
- Certification requirements

---

## ECO States

| State | Description | Location |
|-------|-------------|----------|
| **Open** | ECO issued, planning in progress | **[../06-ECO/ACTIVE/](../06-ECO/ACTIVE/)** |
| **In Progress** | Implementation underway | **[../06-ECO/ACTIVE/](../06-ECO/ACTIVE/)** |
| **Verification** | Changes implemented, verification in progress | **[../06-ECO/ACTIVE/](../06-ECO/ACTIVE/)** |
| **Closed** | Verification complete, ECO closed | **[../06-ECO/CLOSED/](../06-ECO/CLOSED/)** |
| **Cancelled** | ECO cancelled (rare) | **[../06-ECO/CLOSED/](../06-ECO/CLOSED/)** |

---

## Roles and Responsibilities

See **[../01-POLICY/RASCI.md](../01-POLICY/RASCI.md)** for detailed RASCI matrix.

**Key Roles:**
- **Configuration Manager:** ECO issuance, tracking, baseline updates
- **Implementation Lead:** Planning, execution, coordination
- **Engineering:** Design changes, analysis
- **Manufacturing:** Process changes, production
- **Quality:** Verification oversight, approval
- **Test:** Verification testing
- **Supply Chain:** Supplier coordination

---

## Related Documents

- **[ECR_WORKFLOW.md](./ECR_WORKFLOW.md)** — ECR submission and review workflow
- **[../01-POLICY/CHANGE_POLICY.md](../01-POLICY/CHANGE_POLICY.md)** — Change policy
- **[../04-TEMPLATES/ECO.yml](../04-TEMPLATES/ECO.yml)** — ECO template
- **[../../04-BASELINES/](../../04-BASELINES/)** — Baseline management
- **[../../12-CI_CD_RULES/BRANCHING_MODEL.md](../../12-CI_CD_RULES/BRANCHING_MODEL.md)** — Version control

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-15 | Configuration Manager | Initial release |
