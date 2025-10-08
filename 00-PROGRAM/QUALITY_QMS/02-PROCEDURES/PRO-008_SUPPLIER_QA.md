# PRO-008: Supplier Quality Assurance

**Procedure Number:** PRO-008  
**Revision:** 1.0  
**Effective Date:** 2025-01-01  
**Owner:** Supply Chain Director

## 1. Purpose

Establish supplier selection, evaluation, and ongoing quality management to ensure externally provided products and services meet requirements.

## 2. Scope

Applies to all suppliers of materials, components, services, and special processes.

## 3. Responsibilities

- **Supply Chain Director:** Supplier management oversight
- **Supplier Quality Engineer:** Supplier audits, qualification, performance
- **Procurement:** Supplier selection, contracts, purchase orders
- **Quality:** Incoming inspection, supplier NCRs
- **Engineering:** Technical requirements, supplier approval

## 4. Procedure

### 4.1 Supplier Classification

**Critical Suppliers:**
- Flight-critical components
- Special processes (heat treat, plating, NDT)
- High value/long lead items
- Single source suppliers

**Non-Critical Suppliers:**
- Standard hardware
- Non-flight items
- Readily available items
- Multiple sources

### 4.2 Supplier Selection

**Criteria:**
- AS9100 or ISO 9001 certification (preferred for critical)
- Aerospace experience
- Technical capability
- Financial stability
- Delivery performance
- Geographic location
- Pricing competitiveness

**Evaluation Methods:**
- Desktop assessment (certifications, references)
- Supplier questionnaire
- Facility audit
- Sample evaluation
- Trial order

### 4.3 Approved Supplier List (ASL)

**Listing Requirements:**
- Completed evaluation
- Acceptable quality, delivery, cost
- Signed quality agreement
- Risk assessment completed

**ASL Contents:**
- Supplier name and contact
- Approved products/services
- Approval date
- Restrictions or limitations
- Certificate status

**Location:** ASL_APPROVED_SUPPLIERS.csv

### 4.4 Supplier Audits

**Audit Types:**
- Initial approval audit
- Surveillance audits (annual for critical)
- For-cause audits (quality issues)
- Process audits (special processes)

**Audit Scope:**
- QMS compliance (AS9100/ISO 9001)
- Process control
- Calibration and equipment
- Training and competence
- Material control and traceability
- Special process validation

**Records:** SUPPLIER_AUDITS/

### 4.5 Purchase Order Requirements

**Minimum Requirements:**
- Part number, specification, revision
- Quantity and delivery date
- Quality requirements and acceptance criteria
- Certification requirements (CoC, test reports)
- Traceability requirements
- Special process requirements
- Right of access for verification
- Flow-down of customer requirements

### 4.6 Incoming Inspection

**Levels:**
- **Level 1 - 100%:** Critical items, new suppliers
- **Level 2 - Sample:** Proven suppliers, routine items
- **Level 3 - Source Inspection:** Supplier verification accepted
- **Level 4 - Certificate Review:** Documentation only

**Inspection includes:**
- Quantity verification
- Part number and revision
- Visual inspection
- Dimensional inspection (sampling)
- Material certification review
- Certificate of Conformance (CoC)

**Nonconformances:** Supplier NCR issued per PRO-004

### 4.7 Supplier Performance Monitoring

**Metrics (Scorecards):**
- Quality: Incoming defect rate, NCRs, RMA rate
- Delivery: On-time delivery percentage, lead time
- Responsiveness: Quote turnaround, communication
- Overall score: Weighted average

**Scoring:**
- **Excellent:** 90-100%
- **Acceptable:** 75-89%
- **Needs Improvement:** 60-74%
- **Unacceptable:** <60%

**Actions:**
- Excellent: Maintain, reduce inspection
- Acceptable: Monitor
- Needs Improvement: Corrective action required, audit
- Unacceptable: Probation, replacement sourcing

**Location:** SCORECARDS/

### 4.8 Supplier Development

**Activities:**
- Corrective action support
- Process improvement coaching
- Training on requirements
- Quality agreements
- Joint problem solving

### 4.9 PPAP Requirements

Production Part Approval Process per PRO-009_APQP_PPAP required for:
- New parts
- New suppliers
- Design changes
- Process changes
- Restart after hiatus

**Location:** PPAP_PACKAGES/

### 4.10 Special Process Suppliers

**Requirements:**
- Process specification compliance
- Personnel certification (Nadcap where applicable)
- Process validation and qualification
- Control plan and process parameters
- Equipment calibration
- Material traceability

**Nadcap Certification (preferred):**
- Heat treatment
- Chemical processing
- Non-destructive testing (NDT)
- Welding
- Coating

## 5. Records

- ASL_APPROVED_SUPPLIERS.csv
- Supplier audits (SUPPLIER_AUDITS/)
- PPAP packages (PPAP_PACKAGES/)
- Supplier scorecards (SCORECARDS/)
- Supplier NCRs
- Quality agreements

**Retention:** Duration of relationship + 10 years

## 6. Related Documents

- PRO-004_NONCONFORMANCE
- PRO-009_APQP_PPAP
- PRO-013_SPECIAL_PROCESSES
- Section 07-SUPPLIER_QUALITY/

## 7. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Supply Chain Director |
