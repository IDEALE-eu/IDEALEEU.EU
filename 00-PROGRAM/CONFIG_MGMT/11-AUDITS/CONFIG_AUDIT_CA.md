# Configuration Audit (CA)

## Overview

Configuration audits verify that the actual configuration of items matches the documented configuration and that configuration management processes are being followed.

## Types of Configuration Audits

### Physical Configuration Audit (PCA)
Verifies that the as-built hardware matches the design documentation.

### Functional Configuration Audit (FCA)
Verifies that the item's performance meets the specified requirements.

### Configuration Management Audit
Verifies that CM processes and procedures are being followed.

## Configuration Audit Schedule

| Audit Type | Frequency | Scope | Next Audit Date |
|------------|-----------|-------|-----------------|
| PCA | At major milestones | Selected configuration items | TBD |
| FCA | At qualification completion | Flight-critical items | TBD |
| CM Process Audit | Quarterly | CM processes and tools | TBD |

## Physical Configuration Audit (PCA)

### 1. Purpose
Establish that the as-built configuration of an item:
- Conforms to design documentation
- Is adequately documented
- Is reproducible

### 2. Timing
- After first article manufacture
- Before acceptance testing
- At key milestones (CDR, TRR, PRR)

### 3. PCA Process

#### 3.1 Pre-Audit
- [ ] Select items for audit
- [ ] Notify responsible parties (2 weeks advance)
- [ ] Prepare audit checklist
- [ ] Assemble documentation package
- [ ] Schedule audit team

#### 3.2 Audit Execution
- [ ] Opening meeting
- [ ] Review as-built documentation
- [ ] Physical inspection of item
- [ ] Compare as-built to design documentation
- [ ] Review manufacturing records
- [ ] Review inspection records
- [ ] Review serialization
- [ ] Identify discrepancies
- [ ] Document findings

#### 3.3 Post-Audit
- [ ] Closing meeting
- [ ] Prepare audit report
- [ ] Issue discrepancy reports (DRs)
- [ ] Track corrective actions
- [ ] Verify corrections
- [ ] Issue audit certification

### 4. PCA Checklist

#### Configuration Item Identification
- [ ] Part number correct and legible
- [ ] Revision level correct
- [ ] Serial number correct and legible (if serialized)
- [ ] Data matrix code scannable (if applicable)

#### Physical Configuration
- [ ] As-built matches approved drawings
- [ ] Correct materials used
- [ ] Correct finishes applied
- [ ] Correct hardware used
- [ ] Correct torque values applied
- [ ] All components present and correct
- [ ] No unauthorized modifications

#### Documentation
- [ ] Assembly drawings current and approved
- [ ] Bill of materials matches as-built
- [ ] Manufacturing instructions followed
- [ ] Inspection records complete
- [ ] Test records complete and acceptable
- [ ] Material certifications on file
- [ ] Serialization records complete
- [ ] Traveler signed off

#### Traceability
- [ ] Component serial numbers recorded
- [ ] Material lot numbers recorded
- [ ] Process lot numbers recorded
- [ ] Inspection stamps and dates recorded

## Functional Configuration Audit (FCA)

### 1. Purpose
Verify that the item's actual performance meets requirements.

### 2. Timing
- After qualification testing
- Before operational use
- Before production release

### 3. FCA Process

#### 3.1 Pre-Audit
- [ ] Identify requirements to be verified
- [ ] Review test plans and procedures
- [ ] Review test results
- [ ] Schedule FCA

#### 3.2 Audit Execution
- [ ] Review requirements
- [ ] Review test procedures
- [ ] Review test results
- [ ] Verify all requirements tested
- [ ] Verify test methods adequate
- [ ] Verify success criteria met
- [ ] Review non-conformances
- [ ] Document findings

#### 3.3 Post-Audit
- [ ] Issue FCA report
- [ ] Address findings
- [ ] Close open items
- [ ] Issue FCA certification

### 4. FCA Checklist

#### Requirements Verification
- [ ] All requirements identified
- [ ] Verification method defined for each requirement
- [ ] Verification completed for each requirement
- [ ] Results documented
- [ ] Success criteria met
- [ ] Margin adequate

#### Test Documentation
- [ ] Test plans approved
- [ ] Test procedures approved
- [ ] Test setup correct
- [ ] Test configuration documented
- [ ] Test results recorded
- [ ] Anomalies documented and resolved
- [ ] Data quality acceptable

#### Traceability
- [ ] Requirement-to-test traceability complete
- [ ] Test article configuration documented
- [ ] Test equipment calibrated

## Configuration Management Process Audit

### 1. Purpose
Verify CM processes are being followed.

### 2. Scope
- Item identification and numbering
- Baseline management
- Change control
- Status accounting
- Documentation control

### 3. CM Process Audit Checklist

#### Item Identification
- [ ] Part numbering scheme followed
- [ ] Part numbers unique
- [ ] Item master maintained
- [ ] Serialization requirements followed

#### Baseline Management
- [ ] Baselines established at stage gates
- [ ] Baseline content documented
- [ ] Baseline changes controlled
- [ ] Baseline integrity maintained

#### Change Control
- [ ] ECR/ECO process followed
- [ ] Change classification correct
- [ ] CCB approval obtained for Class I changes
- [ ] Change impact assessed
- [ ] Changes implemented per ECO
- [ ] Verification performed

#### Status Accounting
- [ ] Configuration status tracked
- [ ] Item master current
- [ ] Traceability maintained
- [ ] Metrics reported

#### Document Control
- [ ] Drawings and specs under CM control
- [ ] Revision control maintained
- [ ] Obsolete documents archived
- [ ] Distribution controlled

#### Tools and Systems
- [ ] CM tools functional
- [ ] Data backup performed
- [ ] User access controlled
- [ ] Training current

## Audit Reporting

### Discrepancy Report (DR)

| Field | Description |
|-------|-------------|
| DR Number | Unique identifier |
| Item | Configuration item affected |
| Discrepancy | Description of discrepancy |
| Severity | Critical / Major / Minor |
| Root Cause | Identified root cause |
| Corrective Action | Required corrective action |
| Responsible Party | Owner of corrective action |
| Due Date | Completion date |
| Status | Open / In Work / Closed |

### Audit Report Contents

1. **Executive Summary**
   - Audit scope
   - Items audited
   - Overall results
   - Major findings

2. **Audit Details**
   - Audit date and location
   - Audit team
   - Items audited
   - Documents reviewed
   - Tests witnessed

3. **Findings**
   - Discrepancies identified
   - Severity classification
   - Evidence

4. **Recommendations**
   - Corrective actions
   - Process improvements

5. **Conclusion**
   - Audit certification (pass/conditional/fail)
   - Open items
   - Follow-up required

## Audit Team

| Role | Responsibilities |
|------|------------------|
| Lead Auditor | Plan audit, lead team, prepare report |
| Technical Specialists | Evaluate technical aspects |
| Quality Representative | Verify quality compliance |
| Configuration Manager | Verify CM compliance |

## Corrective Action Process

1. **Identification** - Discrepancy identified during audit
2. **Classification** - Severity determined
3. **Assignment** - Responsible party assigned
4. **Root Cause** - Root cause analysis performed
5. **Corrective Action** - Action planned and implemented
6. **Verification** - Action verified effective
7. **Closure** - Discrepancy closed

## Audit Records

All audit records maintained for life of program + 10 years:
- Audit plans
- Audit checklists
- Audit reports
- Discrepancy reports
- Corrective action records
- Follow-up audit results

## Audit Metrics

Track and report:
- Number of audits conducted
- Discrepancies per audit
- Discrepancy severity distribution
- Corrective action cycle time
- Repeat discrepancies
- Process improvement trends

---

**Document Owner:** Quality Assurance  
**Maintained By:** Configuration Management  
**Next Review Date:** TBD
