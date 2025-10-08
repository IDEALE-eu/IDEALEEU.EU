# Change Classification

> Location: `CONFIG_MGMT/06-CHANGES/01-POLICY/CLASSIFICATION.md`  
> Authority: Configuration Control Board (CCB)

## Purpose

Define criteria for classifying changes as Class I, Class II, or Class III to determine appropriate approval authority and review requirements.

## Classification System

### Class I — Major Changes

**Definition:** Changes that affect form, fit, function, safety, or certification.

**Approval Authority:** Configuration Control Board (CCB)

**Characteristics:**
- Affects form, fit, function, or interchangeability
- Changes to flight-critical or safety-critical systems
- Interface changes affecting external systems or suppliers
- Certification-affecting changes (FAA, EASA, ESA)
- Customer approval required per contract
- Significant cost impact (>$50K) or schedule impact (>2 weeks)
- Baseline modification required
- Flight-critical software (DO-178C Level A or B)
- Safety-critical hardware (DO-254 Category A)

**Examples:**
- Wing spar material change
- Flight control software algorithm modification
- Structural reinforcement
- Avionics interface protocol change
- Propulsion system modification
- Safety-critical system redesign
- ICD revision affecting multiple systems
- Manufacturing process change affecting FFF
- Test procedure change affecting acceptance criteria

**Review Requirements:**
- Complete ECR per **[../04-TEMPLATES/ECR.yml](../04-TEMPLATES/ECR.yml)**
- Detailed impact assessment per **[../04-TEMPLATES/IMPACT_ASSESSMENT.md](../04-TEMPLATES/IMPACT_ASSESSMENT.md)**
- Safety analysis (if applicable)
- Certification impact analysis
- Requirements traceability update
- Test plan and verification approach
- Implementation plan with schedule
- Risk assessment and mitigation
- Domain-specific checklist (see **[../04-TEMPLATES/CHECKLISTS/](../04-TEMPLATES/CHECKLISTS/)**)

**Approval Process:**
1. ECR submitted with complete evidence package
2. Configuration Manager triages and routes
3. Technical reviewers assess impact (5 business days)
4. CCB reviews at scheduled meeting
5. CCB disposition documented
6. If approved, ECO issued

**Typical Review Duration:** 2-4 weeks

---

### Class II — Minor Changes

**Definition:** Changes that improve design, process, or documentation without affecting form, fit, function, or certification.

**Approval Authority:** Delegated (Engineering Manager + Quality Manager)

**Characteristics:**
- Documentation corrections (non-procedural)
- Performance optimizations (no functional change)
- Manufacturing process improvements (no FFF impact)
- Non-critical design refinements
- Internal interface changes (same subsystem)
- Moderate cost impact ($10K-$50K) or schedule impact (≤2 weeks)
- Non-flight-critical software changes
- Non-safety-critical hardware changes

**Examples:**
- Drawing clarification (no design change)
- Non-structural component material substitution
- Software user interface improvement
- Test equipment calibration procedure update
- Manufacturing work instruction refinement
- Non-critical documentation update
- Internal cable routing optimization
- Non-functional code refactoring
- Connector type change (same specifications)

**Review Requirements:**
- ECR per **[../04-TEMPLATES/ECR.yml](../04-TEMPLATES/ECR.yml)** (may be abbreviated)
- Basic impact assessment
- Affected items list
- Verification approach
- Cost and schedule estimate

**Approval Process:**
1. ECR submitted
2. Configuration Manager routes to delegated approvers
3. Engineering Manager and Quality Manager review (3 business days)
4. Approval documented
5. ECO issued if approved

**Typical Review Duration:** 1-2 weeks

---

### Class III — Administrative Changes

**Definition:** Editorial, format, or reference changes with no technical impact.

**Approval Authority:** Configuration Manager

**Characteristics:**
- Editorial corrections (spelling, grammar)
- Format changes (layout, fonts)
- Reference updates (document numbers, links)
- Drawing number corrections
- Minimal cost impact (<$10K)
- No schedule impact
- No technical content changes

**Examples:**
- Spelling or grammar corrections
- Document formatting improvements
- Cross-reference updates
- Drawing sheet renumbering
- Title block corrections
- Organization name changes
- Obsolete reference removal
- Non-technical note additions
- Document metadata updates

**Review Requirements:**
- Brief ECR (may use simplified form)
- Description of change
- Affected documents list

**Approval Process:**
1. ECR submitted
2. Configuration Manager reviews and approves (1 business day)
3. Implementation proceeds

**Typical Review Duration:** 1-3 days

---

## Classification Decision Matrix

Use the following decision tree to classify changes:

```
Does the change affect safety or certification?
├─ YES → Class I
└─ NO
   ├─ Does the change affect form, fit, or function?
   │  ├─ YES → Class I
   │  └─ NO
   │     ├─ Does the change affect interfaces or interchangeability?
   │     │  ├─ YES → Class I
   │     │  └─ NO
   │     │     ├─ Does the change affect requirements or verification?
   │     │     │  ├─ YES → Class II
   │     │     │  └─ NO → Class III
```

**Cost/Schedule Thresholds:**
- Cost >$50K or Schedule >2 weeks → Class I
- Cost $10K-$50K or Schedule ≤2 weeks → Class II (minimum)
- Cost <$10K and no schedule impact → May be Class III

**Domain-Specific Considerations:**

**Software:**
- Flight-critical (DO-178C Level A/B) → Class I
- Non-flight-critical → Class II or III based on impact

**Hardware:**
- Safety-critical (DO-254 Category A) → Class I
- Non-safety-critical → Class II or III based on impact

**Documentation:**
- Procedural changes → Class I or II based on impact
- Editorial changes → Class III

---

## Special Cases

### Temporary Changes (Deviations)
- Classified same as permanent change
- Additional workflow per **[../02-WORKFLOW/DEVIATION_WAIVER_WORKFLOW.md](../02-WORKFLOW/DEVIATION_WAIVER_WORKFLOW.md)**
- Document in **[../07-DEVIATIONS/](../07-DEVIATIONS/)**

### Permanent Waivers
- Always Class I (CCB approval required)
- May require customer approval
- Document in **[../08-WAIVERS/](../08-WAIVERS/)**

### Emergency Changes
- Classified per normal criteria
- Streamlined approval process
- Retroactive CCB review required

### Regulatory Changes
- Driven by FAA/EASA/ESA requirements
- Always Class I
- Regulatory coordination required

---

## Classification Appeals

If the assigned classification is disputed:
1. Originator may appeal to Configuration Manager
2. Configuration Manager reviews with CCB Chair
3. CCB Chair makes final determination
4. Rationale documented in ECR

---

## Related Documents

- **[CHANGE_POLICY.md](./CHANGE_POLICY.md)** — Overall change policy
- **[../02-WORKFLOW/ECR_WORKFLOW.md](../02-WORKFLOW/ECR_WORKFLOW.md)** — ECR process
- **[../04-TEMPLATES/ECR.yml](../04-TEMPLATES/ECR.yml)** — ECR template
- **[../04-TEMPLATES/IMPACT_ASSESSMENT.md](../04-TEMPLATES/IMPACT_ASSESSMENT.md)** — Impact assessment template
- **[../../05-CCB/00-CHARTER.md](../../05-CCB/00-CHARTER.md)** — CCB charter

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-15 | Configuration Manager | Initial release |
