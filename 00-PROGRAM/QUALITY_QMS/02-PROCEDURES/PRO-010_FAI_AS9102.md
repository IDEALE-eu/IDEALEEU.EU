# PRO-010: First Article Inspection (AS9102)

**Procedure Number:** PRO-010  
**Revision:** 1.0  
**Effective Date:** 2025-01-01  
**Owner:** Quality Manager

## 1. Purpose

Establish First Article Inspection (FAI) requirements per AS9102 to verify that production processes can produce parts conforming to engineering requirements.

## 2. Scope

Applies to:
- New parts or assemblies
- Design changes affecting form, fit, or function
- Process changes
- New or relocated manufacturing facility
- Change in numerical control program
- Tooling change or refurbishment
- Change of supplier
- Extended production break (>24 months)

## 3. Responsibilities

- **Quality Manager:** FAI program oversight
- **Quality Engineer:** FAI planning and coordination
- **Inspector:** Perform FAI per AS9102
- **Engineering:** Provide technical requirements, review results
- **Customer:** Approve FAI report (if required)

## 4. AS9102 Forms

### Form 1: First Article Inspection Accountability
- Part identification
- FAI reason and type (complete, partial, delta)
- Organization and personnel information
- Serial numbers of articles inspected
- Approval signatures

### Form 2: Product Accountability
- Part/assembly hierarchy
- Characteristics to be verified
- Index to Form 3 detail sheets
- Traceability to engineering requirements

### Form 3: Characteristic Accountability
- Characteristic number and description
- Specification or drawing requirement
- Measurement method
- Actual measurement results
- Acceptance decision (Pass/Fail)
- Inspector signature

## 5. FAI Types

### Complete FAI
- All characteristics verified
- Required for new parts
- All Form 1, 2, and 3 completed

### Partial FAI
- Specific characteristics verified
- Used when only portion of part changed
- Changed characteristics plus sample of unchanged

### Delta FAI
- Only changed characteristics verified
- References previous complete FAI
- Documents what changed and verification

## 6. Procedure

### 6.1 FAI Planning

1. Identify FAI requirement
2. Determine FAI type (complete, partial, delta)
3. Assign FAI number
4. Identify characteristics to verify (all if complete)
5. Identify measurement methods and equipment
6. Verify measurement equipment calibrated
7. Schedule FAI

### 6.2 FAI Execution

1. Produce first article under production conditions
2. Identify and serialize first article
3. Verify all dimensions and characteristics per Form 3
4. Record actual measurements
5. Perform material/performance tests as required
6. Verify special process certifications
7. Photograph critical features (as needed)
8. Complete Forms 1, 2, and 3

### 6.3 Sampling

**Sample Size:**
- Simple parts: 1 sample minimum
- Assemblies: 1 complete assembly + 1 of each unique component
- Complex characteristics: May require 3-5 samples for capability assessment

**Selection:**
- First production run
- Normal production conditions
- Production tooling and processes
- Qualified personnel

### 6.4 Measurement Requirements

**Accuracy:**
- Gage R&R < 10% preferred
- Measurement uncertainty < 1/10 of tolerance
- Calibrated equipment per PRO-011

**Documentation:**
- Actual measured values (not just Pass/Fail)
- Units of measure
- Measurement method
- Environmental conditions (if applicable)

### 6.5 Characteristics to Verify

**Mandatory:**
- All dimensions on drawing
- Material specifications
- Material certifications
- Performance requirements
- Surface finish
- Coating thickness
- Special process certifications
- Marking and identification

**Risk-Based:**
- Critical characteristics: 100% verification
- Key characteristics: Full verification
- Other characteristics: Representative sampling acceptable

### 6.6 FAI Report Review and Approval

**Internal Review:**
1. Inspector completes Forms 1, 2, 3
2. Quality Engineer reviews for completeness and accuracy
3. Engineering reviews for technical compliance
4. Quality Manager approves

**Customer Review (if required):**
- Submit FAI package to customer
- Address any customer questions or findings
- Obtain customer approval before full production

**Approval Criteria:**
- All characteristics within specification
- Forms complete and accurate
- Required certifications included
- Measurement systems adequate

### 6.7 Discrepancies

**Nonconforming FAI:**
- Document discrepancy
- Issue NCR per PRO-004
- Determine root cause
- Implement corrective action
- Re-perform FAI after correction
- Cannot start production without approved FAI

**Waivers:**
- Engineering disposition required
- Customer approval if contractual requirement
- Document in FAI report

## 7. FAI Records

**Package Contents:**
- Form 1 (Accountability)
- Form 2 (Product)
- Form 3 sheets (Characteristics)
- Raw measurement data
- Material certifications
- Special process certifications
- Test reports
- Photographs
- Customer approval (if applicable)

**Retention:** Life of product + 10 years minimum

**Storage:**
- Digital archive
- Accessible to customer and auditors
- Secure backup

## 8. Digital Thread Integration

- FAI data linked to part number and revision
- Traceability to engineering requirements
- Linked to PPAP package
- API access per section 12-DIGITAL_THREAD_HOOKS

## 9. Related Documents

- AS9102 (First Article Inspection Requirement)
- PRO-009_APQP_PPAP
- PRO-011_CALIBRATION_MSA
- PRO-004_NONCONFORMANCE
- Section 07-SUPPLIER_QUALITY/PPAP_PACKAGES/

## 10. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Quality Manager |
