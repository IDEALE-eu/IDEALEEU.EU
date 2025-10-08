# Functional Configuration Audit (FCA)

## Overview

The Functional Configuration Audit (FCA) verifies that the performance of a configuration item conforms to its functional and allocated configuration documentation (specifications and requirements).

## Purpose

The FCA:
- Verifies that the item's actual performance meets specified requirements
- Validates that all functional requirements have been verified
- Confirms that verification methods are adequate
- Establishes the functional baseline
- Provides confidence for operational use

## Applicability

FCA is conducted for:
- Aircraft systems and subsystems
- Spacecraft systems and subsystems
- Flight-critical components
- Ground support equipment
- Software and firmware
- Test equipment

## Timing

FCA is typically conducted:
- After completion of qualification testing
- Before production release
- Before operational deployment
- At CDR or later milestones
- Before delivery to customer

## Prerequisites

Before conducting FCA:
- [ ] Configuration item identified and documented
- [ ] Functional requirements allocated
- [ ] Verification methods defined
- [ ] Test procedures approved
- [ ] Testing completed
- [ ] Test results documented
- [ ] Physical Configuration Audit (PCA) completed (if applicable)
- [ ] All anomalies resolved or dispositioned

## FCA Process

### 1. Planning Phase

#### 1.1 Preparation (4-6 weeks before FCA)
- [ ] Identify configuration items for FCA
- [ ] Assemble audit team
- [ ] Notify responsible organizations
- [ ] Schedule FCA date
- [ ] Define audit scope
- [ ] Prepare audit agenda

#### 1.2 Documentation Preparation (2-4 weeks before FCA)
- [ ] Compile requirements documents
- [ ] Compile test plans and procedures
- [ ] Compile test results and reports
- [ ] Compile non-conformance reports
- [ ] Prepare verification matrix
- [ ] Prepare configuration documentation
- [ ] Distribute package to audit team (1 week before FCA)

### 2. Execution Phase

#### 2.1 Opening Meeting
- Introductions
- Review audit objectives and scope
- Review audit schedule
- Review documentation provided
- Address questions

#### 2.2 Requirements Review
Review each functional requirement:
- [ ] Requirement clearly stated
- [ ] Verification method appropriate
- [ ] Verification planned or completed
- [ ] Acceptance criteria defined
- [ ] Results documented

#### 2.3 Verification Evidence Review
For each requirement:
- [ ] Test procedure adequate
- [ ] Test configuration correct
- [ ] Test execution documented
- [ ] Test results valid
- [ ] Acceptance criteria met
- [ ] Margin adequate
- [ ] Non-conformances addressed

#### 2.4 Traceability Review
- [ ] Requirements traced to verification
- [ ] All requirements verified
- [ ] No orphan tests
- [ ] Documentation complete
- [ ] Changes incorporated

#### 2.5 Special Topics
- Performance margins
- Environmental qualification
- Software verification
- Safety analysis
- Reliability analysis
- EMI/EMC compliance
- Certification compliance

#### 2.6 Discrepancy Identification
Document any:
- Missing verifications
- Inadequate test methods
- Unmet requirements
- Insufficient margin
- Documentation gaps
- Open anomalies

#### 2.7 Closing Meeting
- Present preliminary findings
- Discuss discrepancies
- Define corrective actions
- Establish follow-up schedule

### 3. Post-Audit Phase

#### 3.1 Audit Report Preparation
- [ ] Document audit findings
- [ ] Classify discrepancies
- [ ] Issue discrepancy reports (DRs)
- [ ] Prepare audit report
- [ ] Distribute draft report for review
- [ ] Incorporate comments
- [ ] Issue final report

#### 3.2 Corrective Action
- [ ] Responsible parties assigned
- [ ] Corrective actions planned
- [ ] Actions implemented
- [ ] Actions verified
- [ ] DRs closed

#### 3.3 FCA Certification
- [ ] All discrepancies resolved or dispositioned
- [ ] Corrective actions verified
- [ ] FCA report approved
- [ ] FCA certificate issued
- [ ] Functional baseline established

## FCA Checklist

### A. Configuration Item Identification
- [ ] Part number and revision
- [ ] Serial number (if applicable)
- [ ] Configuration description document
- [ ] Baseline designation
- [ ] As-built configuration documented

### B. Functional Requirements
- [ ] Requirements specification identified
- [ ] Requirements clearly stated
- [ ] Requirements allocated to item
- [ ] Requirements complete
- [ ] Requirements approved
- [ ] Requirements traceable

### C. Verification Planning
- [ ] Verification methods defined
  - [ ] Test
  - [ ] Analysis
  - [ ] Demonstration
  - [ ] Inspection
- [ ] Verification matrix complete
- [ ] Test plans approved
- [ ] Test procedures approved
- [ ] Success criteria defined
- [ ] Margin requirements specified

### D. Test Configuration
- [ ] Test article configuration documented
- [ ] Test article matches design
- [ ] Test setup documented
- [ ] Test equipment identified
- [ ] Test equipment calibrated
- [ ] Test environment documented
- [ ] Initial conditions documented

### E. Test Execution
- [ ] Tests conducted per procedure
- [ ] Test conditions met
- [ ] Data collection adequate
- [ ] Data quality acceptable
- [ ] Deviations documented and approved
- [ ] Anomalies documented
- [ ] Retest requirements met

### F. Test Results
- [ ] Results documented
- [ ] Requirements verified
- [ ] Success criteria met
- [ ] Margin adequate (typically >10%)
- [ ] Performance within specification
- [ ] Data analysis complete
- [ ] Statistical analysis (if required)

### G. Non-Conformances
- [ ] All NCRs documented
- [ ] Root cause identified
- [ ] Corrective action taken
- [ ] Verification repeated (if required)
- [ ] NCRs closed or dispositioned
- [ ] Impact assessed

### H. Verification Traceability
- [ ] All requirements have verification
- [ ] All verifications trace to requirement
- [ ] No orphan tests
- [ ] Traceability matrix complete
- [ ] Verification coverage 100%

### I. Environmental Qualification
- [ ] Environmental requirements defined
- [ ] Environmental testing completed
  - [ ] Temperature
  - [ ] Humidity
  - [ ] Pressure
  - [ ] Vibration
  - [ ] Shock
  - [ ] EMI/EMC
  - [ ] Salt fog (if applicable)
  - [ ] Radiation (if applicable)
- [ ] Margin demonstrated

### J. Software Verification (if applicable)
- [ ] Software requirements traced
- [ ] Software test procedures
- [ ] Code coverage analysis
- [ ] Static code analysis
- [ ] Integration testing
- [ ] Verification per DO-178C (aircraft)
- [ ] Verification per ECSS-Q-ST-80C (spacecraft)

### K. Safety Verification
- [ ] Safety requirements identified
- [ ] Hazard analysis conducted
- [ ] Safety verifications completed
- [ ] Safety margins adequate
- [ ] Fail-safe features verified
- [ ] Redundancy verified (if required)

### L. Reliability
- [ ] MTBF requirement defined
- [ ] Reliability analysis conducted
- [ ] FMEA completed
- [ ] Reliability testing (if required)
- [ ] Failure modes addressed

### M. Certification (if applicable)
- [ ] Certification requirements identified
- [ ] Compliance demonstrated
- [ ] Certification evidence documented
- [ ] Regulatory authority coordination
- [ ] Type certificate data sheet updated

### N. Documentation
- [ ] Design documentation complete
- [ ] Test documentation complete
- [ ] Analysis reports complete
- [ ] Drawings approved
- [ ] Specifications approved
- [ ] Manuals prepared
- [ ] Maintenance procedures prepared

## FCA Audit Team

| Role | Responsibilities |
|------|------------------|
| **Lead Auditor** | Plan and conduct FCA, prepare report |
| **Systems Engineer** | Review system requirements and verification |
| **Test Engineer** | Review test methods and results |
| **Quality Engineer** | Verify quality compliance |
| **Configuration Manager** | Verify configuration documentation |
| **Safety Engineer** | Review safety verification |
| **Certification Engineer** | Review certification compliance (if applicable) |
| **Software Engineer** | Review software verification (if applicable) |

## FCA Report Contents

### 1. Executive Summary
- FCA scope and objectives
- Configuration item(s) audited
- Audit dates and location
- Overall results
- Certification status

### 2. Configuration Item Description
- Part number, revision, serial number
- Description
- Configuration baseline
- As-built configuration

### 3. Requirements Summary
- Total requirements
- Requirements by verification method
- Verification status summary

### 4. Verification Results
- Requirements verified by test
- Requirements verified by analysis
- Requirements verified by demonstration
- Requirements verified by inspection
- Performance margins achieved

### 5. Findings and Discrepancies
- Discrepancies identified
- Severity classification
- Responsible parties
- Corrective actions

### 6. Non-Conformances
- NCRs reviewed
- NCR dispositions
- Impact assessment

### 7. Recommendations
- Process improvements
- Additional testing
- Documentation updates

### 8. Conclusion
- FCA certification status
  - **Pass** - All requirements verified, discrepancies resolved
  - **Conditional Pass** - Minor discrepancies, corrective action plan in place
  - **Fail** - Major discrepancies, additional work required
- Functional baseline establishment
- Release recommendation

### 9. Appendices
- Verification matrix
- Test results summary
- Discrepancy reports
- Attendance records

## Discrepancy Classification

| Severity | Description | Disposition |
|----------|-------------|-------------|
| **Critical** | Requirement not met, safety impact | Must be resolved before FCA certification |
| **Major** | Requirement not fully verified, margin inadequate | Must be resolved or waived |
| **Minor** | Documentation issue, administrative | May be resolved post-FCA |

## FCA Certification Criteria

For FCA certification:
- [ ] All functional requirements verified
- [ ] All critical and major discrepancies resolved
- [ ] Adequate margin demonstrated
- [ ] Configuration documented
- [ ] Traceability complete
- [ ] Documentation adequate
- [ ] Functional baseline established

## Follow-Up Audits

Follow-up FCA may be required:
- When major changes occur
- After significant rework
- If conditional pass requires verification
- For production qualification
- Periodic re-verification

## Records Retention

FCA records maintained for life of program + 10 years:
- FCA plan and agenda
- Audit checklists
- Verification matrix
- Test results
- Discrepancy reports
- Corrective action records
- FCA report
- FCA certificate

## FCA Certificate

Upon successful completion:

---

**FUNCTIONAL CONFIGURATION AUDIT CERTIFICATE**

Configuration Item: [Part Number/Description]  
Serial Number: [S/N]  
Baseline: [Baseline designation]

This certifies that a Functional Configuration Audit has been conducted and that the performance of the above configuration item conforms to its functional requirements as documented in [Requirements Document].

All requirements have been verified by test, analysis, demonstration, or inspection. All discrepancies have been resolved or dispositioned.

The functional baseline for this configuration item is established.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Lead Auditor | TBD | _______ | ____ |
| Systems Engineer | TBD | _______ | ____ |
| Quality Manager | TBD | _______ | ____ |
| Program Manager | TBD | _______ | ____ |

---

**Document Owner:** Systems Engineering  
**Maintained By:** Configuration Management  
**Review Frequency:** As needed for each FCA
