# PRO-009: APQP and PPAP

**Procedure Number:** PRO-009  
**Revision:** 1.0  
**Effective Date:** 2025-01-01  
**Owner:** Quality Manager

## 1. Purpose

Establish Advanced Product Quality Planning (APQP) and Production Part Approval Process (PPAP) for new product introduction and manufacturing readiness.

## 2. Scope

Applies to new designs, significant design changes, new processes, new suppliers, and production restart after extended hiatus.

## 3. APQP Phases

### Phase 1: Plan and Define
- Program objectives and timeline
- Customer requirements (voice of customer)
- Design goals and reliability targets
- Cost targets
- Team formation

### Phase 2: Product Design and Development
- DFMEA (Design Failure Modes and Effects Analysis)
- Design verification plan
- Design reviews per ARP4754A/ECSS
- Design outputs (drawings, specifications)
- Prototype build and test

### Phase 3: Process Design and Development
- PFMEA (Process Failure Modes and Effects Analysis)
- Control plan development
- Work instructions
- Packaging and handling requirements
- MSA (Measurement System Analysis)

### Phase 4: Product and Process Validation
- Production trial run
- Process capability study (Cpk ≥ 1.33 target)
- Control plan validation
- PPAP submission
- Customer approval

### Phase 5: Launch and Continuous Improvement
- Production ramp-up
- Ongoing process control
- Lessons learned
- Continuous improvement initiatives

## 4. PPAP Requirements

### 4.1 PPAP Levels

**Level 1:** Warrant only (supplier retains records)
**Level 2:** Warrant plus samples
**Level 3:** Warrant, samples, plus supporting data (typical)
**Level 4:** Warrant and complete supporting data
**Level 5:** Warrant, samples, and supporting data submitted to customer and reviewed at supplier location

### 4.2 PPAP Submission Elements

1. Design record
2. Engineering change documentation (if applicable)
3. Customer engineering approval (if required)
4. DFMEA
5. Process flow diagram
6. PFMEA
7. Control plan
8. MSA studies
9. Dimensional results (layout inspection)
10. Material/performance test results
11. Initial process capability study (Ppk)
12. Qualified laboratory documentation
13. Appearance approval report (if applicable)
14. Sample production parts
15. Master sample
16. Checking aids
17. Customer-specific requirements
18. Part Submission Warrant (PSW)

### 4.3 PPAP Approval

- Customer or Quality Manager reviews submission
- Approve, reject, or request additional information
- Approval documented on PSW
- Production authorized upon approval

### 4.4 PPAP Resubmission

**Required when:**
- Design change affecting form, fit, function
- Process change
- Supplier change or new location
- Extended production interruption (>12 months)
- Product nonconformance trends

## 5. Control Plan

**Elements:**
- Part information
- Process steps
- Characteristics to control
- Specification limits
- Measurement method and frequency
- Sample size
- Control method
- Reaction plan for out-of-control

**Types:**
- Prototype control plan
- Pre-launch control plan
- Production control plan

## 6. Process Capability

**Indices:**
- **Cp:** Process capability (width of spec vs. process spread)
- **Cpk:** Process capability accounting for centering
- **Pp/Ppk:** Process performance (initial study)

**Targets:**
- Critical characteristics: Cpk ≥ 1.67
- Important characteristics: Cpk ≥ 1.33
- All others: Cpk ≥ 1.00

## 7. Records

- APQP project plans
- DFMEA/PFMEA
- Control plans
- PPAP packages (PPAP_PACKAGES/)
- Process capability studies
- Part Submission Warrants

**Retention:** Life of product + 10 years

## 8. Related Documents

- PRO-008_SUPPLIER_QA
- PRO-010_FAI_AS9102
- PRO-011_CALIBRATION_MSA
- AS9145 (APQP/PPAP standard)

## 9. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Quality Manager |
