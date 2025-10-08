# CDR_CHECKLIST

Critical Design Review Checklist

## Overview

This checklist ensures readiness for Critical Design Review (CDR). CDR is the most important review—it freezes the certification basis, approves the detailed design, and authorizes proceeding to manufacturing/integration. **This is the last chance to make design changes without significant cost and schedule impact.**

## Standards Evidence Required at CDR

### 1. Standards Compliance

- [ ] **1.1** All applicable standards confirmed and no changes expected
- [ ] **1.2** Compliance matrices complete for all standards:
  - [ ] ARP4754A_CM.csv (if aircraft)
  - [ ] DO178C_CM.csv (if software, aircraft)
  - [ ] ECSS_CM.csv (if spacecraft)
- [ ] **1.3** All deviations/waivers approved and documented
- [ ] **1.4** Certification basis frozen and agreed with authorities (aircraft)
- [ ] **1.5** Tailoring finalized and approved (spacecraft)
- [ ] **1.6** Standards-to-requirements traceability complete and audited

### 2. Requirements

- [ ] **2.1** All system requirements complete, reviewed, and baselined
- [ ] **2.2** All subsystem requirements allocated and baselined
- [ ] **2.3** Requirements traceability verified (requirements ↔ design ↔ verification)
- [ ] **2.4** Derived requirements identified and justified
- [ ] **2.5** Requirements stability >95% (minimal changes expected)
- [ ] **2.6** Interface requirements documented in ICDs and baselined
- [ ] **2.7** Requirements verification methods defined for all requirements

### 3. Design

- [ ] **3.1** Detailed design complete for all subsystems
- [ ] **3.2** All drawings released and in configuration control
- [ ] **3.3** Bill of Materials (BOM) complete
- [ ] **3.4** All parts selected and qualified
- [ ] **3.5** Design analyses complete with positive margins:
  - [ ] Structural analysis (FEA, stress, fatigue, fracture)
  - [ ] Thermal analysis (hot case, cold case, worst case)
  - [ ] Power budget (BOL, EOL, all modes)
  - [ ] Mass budget (with margin)
  - [ ] EMC analysis
  - [ ] Radiation analysis (spacecraft)
- [ ] **3.6** Design margins verified (typically 15-25% remaining)
- [ ] **3.7** Design reviews completed at all levels
- [ ] **3.8** All trade studies closed
- [ ] **3.9** Critical design areas addressed (tests planned or completed)

### 4. Verification

- [ ] **4.1** Verification Plan complete and approved
- [ ] **4.2** Verification procedures drafted
- [ ] **4.3** Verification requirements traced to all system/subsystem requirements
- [ ] **4.4** Test facilities secured (internal or external)
- [ ] **4.5** Test equipment identified and availability confirmed
- [ ] **4.6** Environmental test plan complete (DO-160 or ECSS)
- [ ] **4.7** Verification Control Document (VCD) complete (spacecraft)
- [ ] **4.8** Verification independence identified (for safety-critical items)

### 5. Safety

- [ ] **5.1** Functional Hazard Assessment (FHA) complete
- [ ] **5.2** Preliminary System Safety Assessment (PSSA) complete
- [ ] **5.3** System Safety Assessment (SSA) in progress
- [ ] **5.4** Fault Tree Analysis (FTA) and FMEA complete
- [ ] **5.5** Common Cause Analysis (CCA) complete
- [ ] **5.6** Safety case documented
- [ ] **5.7** Safety-critical items list finalized
- [ ] **5.8** Redundancy and fault tolerance verified in design

### 6. Standards-Specific Deliverables

#### Aircraft (ARP4754A, DO-178C, DO-254)

- [ ] **6.1** Plan for Software Aspects of Certification (PSAC) approved by authority
- [ ] **6.2** Plan for Hardware Aspects of Certification (PHAC) approved by authority
- [ ] **6.3** Software Development Plan (SDP) complete
- [ ] **6.4** Software Requirements Standards (SRS) established
- [ ] **6.5** Software Design Standards (SDS) established
- [ ] **6.6** Software Code Standards (SCS) established
- [ ] **6.7** Hardware Development Plan (HDP) complete
- [ ] **6.8** Hardware Requirements Standards established
- [ ] **6.9** Hardware Design Standards established
- [ ] **6.10** Tool Qualification Plans complete (DO-330)
- [ ] **6.11** DO-160 test plan complete
- [ ] **6.12** Certification Liaison with EASA/FAA ongoing

#### Spacecraft (ECSS)

- [ ] **6.13** Design Justification File (DJF) complete
- [ ] **6.14** Verification Control Document (VCD) complete
- [ ] **6.15** Software Requirements Document (SWRD) baselined
- [ ] **6.16** Software Design Document (SDD) complete
- [ ] **6.17** Preferred Parts List (PPL) finalized
- [ ] **6.18** Materials and Processes List (MPL) finalized
- [ ] **6.19** Thermal Mathematical Model (TMM) correlated
- [ ] **6.20** Finite Element Model (FEM) validated
- [ ] **6.21** AIT Plan complete
- [ ] **6.22** Product Assurance Plans approved

### 7. Configuration Management

- [ ] **7.1** Product baseline established (design frozen)
- [ ] **7.2** All configuration items identified and in CM system
- [ ] **7.3** As-designed configuration documented
- [ ] **7.4** Change control process mature and operating smoothly
- [ ] **7.5** Configuration audits (FCA/PCA) planned
- [ ] **7.6** CCB meeting regularly and effectively
- [ ] **7.7** Configuration status accounting operational

### 8. Software (if applicable)

- [ ] **8.1** Software requirements complete and baselined
- [ ] **8.2** Software architecture defined and reviewed
- [ ] **8.3** Detailed design complete for all modules
- [ ] **8.4** Coding started or planned (depending on program phase)
- [ ] **8.5** Unit test plans developed
- [ ] **8.6** Integration test plan developed
- [ ] **8.7** Software verification plan complete
- [ ] **8.8** Traceability: requirements → design → code → test
- [ ] **8.9** Software configuration management operational

### 9. Hardware (if applicable)

- [ ] **9.1** Hardware requirements complete and baselined
- [ ] **9.2** Conceptual design complete and reviewed
- [ ] **9.3** Detailed design (schematics, FPGA/ASIC) complete
- [ ] **9.4** Parts selection complete (all parts on Preferred Parts List)
- [ ] **9.5** Worst-case analysis complete
- [ ] **9.6** Timing analysis complete
- [ ] **9.7** Hardware verification plan complete
- [ ] **9.8** Traceability: requirements → design → verification

### 10. Manufacturing and Production

- [ ] **10.1** Manufacturing plans developed
- [ ] **10.2** Manufacturing readiness assessed
- [ ] **10.3** Tooling designed and fabrication started
- [ ] **10.4** Special processes qualified (welding, coating, etc.)
- [ ] **10.5** Supplier capability assessed
- [ ] **10.6** Production quality plan complete
- [ ] **10.7** First Article Inspection (FAI) procedures defined

### 11. Integration and Test

- [ ] **11.1** Integration sequence finalized
- [ ] **11.2** AIT schedule developed
- [ ] **11.3** AIT facilities available and qualified
- [ ] **11.4** Ground Support Equipment (GSE) designs complete
- [ ] **11.5** Test equipment procured or on order
- [ ] **11.6** Cleanroom available (if required for spacecraft)
- [ ] **11.7** Environmental test schedule coordinated with test labs

### 12. Quality

- [ ] **12.1** Quality Management System certified (AS9100 / ISO 9001)
- [ ] **12.2** Quality audits completed with acceptable results
- [ ] **12.3** Product assurance oversight in place
- [ ] **12.4** Supplier quality assessments complete
- [ ] **12.5** Non-conformance process mature
- [ ] **12.6** Lessons learned from early builds incorporated

### 13. Schedule and Budget

- [ ] **13.1** Detailed schedule through delivery
- [ ] **13.2** Critical path identified and managed
- [ ] **13.3** Schedule margin assessed (typically 10-20%)
- [ ] **13.4** Budget through delivery confirmed
- [ ] **13.5** Cost reserves adequate for identified risks
- [ ] **13.6** Resource loading realistic

### 14. Risk Management

- [ ] **14.1** All major technical risks retired or mitigated
- [ ] **14.2** Risk register up to date
- [ ] **14.3** Residual risks acceptable
- [ ] **14.4** Risk review process operating
- [ ] **14.5** Contingency plans for high risks

### 15. Supply Chain

- [ ] **15.1** All critical parts procured or on order
- [ ] **15.2** Long-lead items secured
- [ ] **15.3** Supplier agreements in place
- [ ] **15.4** Supply chain risks mitigated
- [ ] **15.5** Supplier quality oversight in place

## Open Items

| Item | Description | Owner | Due Date | Criticality | Status |
|------|-------------|-------|----------|-------------|--------|
| | | | | HIGH/MED/LOW | |

## Action Items

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| | | | |

## Review Board Decision

- [ ] **GO** - Design frozen, proceed to manufacturing/integration
- [ ] **CONDITIONAL GO** - Proceed with conditions (list below) - **Use sparingly, critical items must be complete**
- [ ] **NO-GO** - Do not proceed (list reasons below)

### Conditions / Reasons:

---

**Review Date**: ________________

**Review Board Chair**: ________________

**Certification Authority Representative** (if applicable): ________________

**Signature**: ________________

---

**CRITICAL NOTE**: CDR is the last gate before significant expenditure on manufacturing and integration. Design changes after CDR are extremely costly. Ensure all critical items are truly complete before granting GO.
