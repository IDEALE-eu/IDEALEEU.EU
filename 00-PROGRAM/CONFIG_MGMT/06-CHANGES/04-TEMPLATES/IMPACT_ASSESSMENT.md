# Impact Assessment Template

> Use this template for detailed impact analysis of Class I changes

## Change Information

**ECR Number:** ECR-YYYY-####  
**Change Title:** [Brief description]  
**Assessed By:** [Name, Role]  
**Assessment Date:** YYYY-MM-DD

---

## 1. Safety Impact

### Safety Classification
- [ ] Safety-Critical (affects flight safety, life-critical)
- [ ] Safety-Related (indirect safety impact)
- [ ] Non-Safety (no safety impact)

### Hazard Analysis
- **Affected Hazards:** [List hazard IDs from HARA/FHA]
- **New Hazards Introduced:** [Describe any new hazards]
- **Severity Assessment:** [Catastrophic / Hazardous / Major / Minor / No Effect]
- **Risk Mitigation:** [Describe mitigations]
- **Safety Assessment Update Required:** Yes / No

### References
- Link to safety analysis: **[../../QUALITY_QMS/13-RISK_SAFETY/](../../QUALITY_QMS/13-RISK_SAFETY/)**

---

## 2. Certification Impact

### Affected Regulations
- [ ] FAA 14 CFR Part 25 (Transport Category Aircraft)
- [ ] EASA CS-25 (Certification Specifications)
- [ ] DO-178C (Software)
- [ ] DO-254 (Hardware)
- [ ] DO-160G (Environmental)
- [ ] ECSS (Space)
- [ ] Other: [Specify]

### Certification Actions Required
- [ ] Type Certificate amendment
- [ ] Supplemental Type Certificate
- [ ] Authority notification required
- [ ] Certification plan update
- [ ] Compliance demonstration
- [ ] Authority approval required

### Authority Coordination
**Authority:** [FAA / EASA / ESA / etc.]  
**Contact:** [Authority representative]  
**Timeline:** [Estimate for authority review/approval]

---

## 3. Interface Impact

### Affected Interfaces
| ICD Number | Interface Description | Impact | Version Change |
|------------|----------------------|--------|----------------|
| ICD-001 | Wing-Fuselage Interface | Connector change | v2.0 → v2.1 |

### Interface Compatibility
- **Backward Compatible:** Yes / No
- **Forward Compatible:** Yes / No
- **Migration Plan Required:** Yes / No

### Affected Systems/Subsystems
- [List all systems affected by interface changes]

### Coordination Required
- [ ] Update ICD documentation
- [ ] Notify interface owners
- [ ] Coordinate testing
- [ ] Update compatibility matrix

---

## 4. Cost Impact

### Development Cost
| Category | Estimated Cost | Currency |
|----------|---------------|----------|
| Engineering labor | [Hours × Rate] | USD |
| Materials/parts | | USD |
| Tooling | | USD |
| Testing | | USD |
| Certification | | USD |
| **Total Development** | | **USD** |

### Production Cost Impact
- **Recurring Cost Change:** [Per unit]
- **Effectivity:** [When cost change takes effect]

### Total Program Cost Impact
- **One-Time Cost:** [Development + NRE]
- **Recurring Impact:** [Annual or total program]

---

## 5. Schedule Impact

### Development Schedule
- **Estimated Duration:** [Weeks/Months]
- **Critical Path Impact:** Yes / No
- **Milestone Impact:** [List affected milestones]

### Key Milestones
| Milestone | Baseline Date | Impact | New Date |
|-----------|---------------|--------|----------|
| PDR | 2025-03-15 | +2 weeks | 2025-03-29 |

### Resource Availability
- **Resource Constraints:** [Describe any resource limitations]
- **Parallel Activities:** [Activities that can be done in parallel]

---

## 6. Supply Chain Impact

### Affected Suppliers
| Supplier | Part Number | Impact | Lead Time Change |
|----------|-------------|--------|------------------|
| Acme Corp | AC-1234 | Material change | +4 weeks |

### Procurement Actions
- [ ] New supplier qualification required
- [ ] Long lead items identified
- [ ] Purchase orders affected
- [ ] AVL updates required

### Supplier Coordination
- **Notification Required:** Yes / No
- **Supplier Concurrence Required:** Yes / No
- **PPAP Updates:** Yes / No

---

## 7. Technical Impact

### Design Changes
- **Drawings Affected:** [List drawing numbers]
- **Specifications Affected:** [List spec numbers]
- **Models Affected:** [CAD/SysML models]

### Requirements Impact
- **Requirements Affected:** [List requirement IDs]
- **Traceability Update Required:** Yes / No
- **Verification Matrix Update:** Yes / No

### Performance Impact
- **Performance Parameters Affected:** [Weight, speed, range, etc.]
- **Performance Change:** [Quantify change]
- **Acceptable:** Yes / No

---

## 8. Verification Impact

### Test Impact
- **New Tests Required:** Yes / No
- **Existing Tests Affected:** [List test procedures]
- **Test Equipment Impact:** [Any new equipment needed]

### Verification Methods
- [ ] Test
- [ ] Analysis
- [ ] Demonstration
- [ ] Inspection

### Verification Plan
[Describe verification approach]

---

## 9. Recommendation

### Technical Assessment
- [ ] **Approve** — Change is technically sound and acceptable
- [ ] **Approve with Conditions** — [List conditions]
- [ ] **Reject** — [Provide rationale]
- [ ] **Defer** — [List information needed]

### Conditions (if applicable)
1. [Condition 1]
2. [Condition 2]

### Rationale
[Provide detailed justification for recommendation]

---

## 10. Signature

**Assessed By:** ___________________________  
**Role:** ___________________________  
**Date:** ___________________________
