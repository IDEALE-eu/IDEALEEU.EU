# PRO-001: Document and Data Control

**Procedure Number:** PRO-001  
**Revision:** 1.0  
**Effective Date:** 2025-01-01  
**Owner:** Quality Manager

## 1. Purpose

This procedure establishes the requirements for controlling documents and data within the Quality Management System to ensure that:
- Current and approved documents are available where needed
- Obsolete documents are prevented from unintended use
- Changes are properly reviewed and approved
- Documents are legible, identifiable, and retrievable

## 2. Scope

This procedure applies to all QMS documents including:
- Quality Manual
- Procedures
- Work Instructions
- Forms and templates
- External documents (standards, regulations, customer specifications)
- Records (controlled separately per retention requirements)

## 3. Responsibilities

### 3.1 Quality Manager
- Overall responsibility for document control system
- Approval of QMS procedures
- Periodic review of document control effectiveness

### 3.2 Document Controller
- Maintaining document register
- Document numbering and version control
- Distribution control
- Archive management

### 3.3 Document Owners
- Document creation and revision
- Ensuring technical accuracy
- Initiating change requests
- Periodic review of owned documents

### 3.4 Approvers
- Reviewing and approving documents within their area of responsibility
- Ensuring compliance with standards and regulations

## 4. Procedure

### 4.1 Document Identification

#### 4.1.1 Document Numbering
Documents are assigned unique identifiers:
- **Format:** [TYPE]-[CATEGORY]-[NUMBER]
- **Example:** PRO-001, FORM-NCR-001, WI-ASSEMBLY-001

#### 4.1.2 Document Metadata
All controlled documents include:
- Document title
- Document number
- Revision level
- Effective date
- Owner/author
- Approver(s)
- Distribution list

### 4.2 Document Creation and Approval

#### 4.2.1 Creation
1. Owner drafts document using approved template
2. Document is assigned a number by Document Controller
3. Owner completes all required metadata
4. Owner submits for review

#### 4.2.2 Review and Approval
1. Technical review by subject matter experts
2. Quality review for QMS compliance
3. Management approval as required
4. Final approval by designated approver
5. Document Controller releases approved document

#### 4.2.3 Approval Authority Levels
| Document Type | Approver |
|--------------|----------|
| Quality Manual | Program Director + Quality Manager |
| Procedures | Quality Manager + Process Owner |
| Work Instructions | Process Owner |
| Forms | Quality Manager |
| Engineering Documents | Chief Engineer |

### 4.3 Document Distribution

#### 4.3.1 Distribution Methods
- Electronic: Document management system / shared repository
- Hard copy: Controlled copies with distribution log (when required)

#### 4.3.2 Access Control
- Read access: All personnel as appropriate to their role
- Edit access: Document owners and authorized editors only
- Approval authority: Per section 4.2.3

#### 4.3.3 Distribution Log
Maintained for:
- Hard copy distributions
- External document distributions
- Customer-provided documents

### 4.4 Document Changes

#### 4.4.1 Change Request
1. Change initiator completes change request form
2. Technical justification documented
3. Impact assessment performed
4. Change submitted to document owner

#### 4.4.2 Change Review
1. Document owner evaluates change
2. Affected parties notified for input
3. Change approved or rejected
4. If approved, document revised

#### 4.4.3 Revision Process
1. Owner incorporates approved changes
2. Revision level incremented:
   - Minor changes: Increment decimal (1.0 → 1.1)
   - Major changes: Increment integer (1.9 → 2.0)
3. Change summary added to revision history
4. Document follows approval process (section 4.2)
5. Previous revision archived

### 4.5 Document Review

#### 4.5.1 Periodic Review
All documents reviewed:
- Annually minimum
- When process changes
- When standards/regulations change
- Following audit findings or non-conformances

#### 4.5.2 Review Process
1. Document Controller generates review notification
2. Owner reviews for accuracy and currency
3. Owner determines if revision needed
4. If no revision: Review date updated in register
5. If revision needed: Follow change process (section 4.4)

### 4.6 Document Obsolescence

#### 4.6.1 Obsolete Document Control
When document becomes obsolete:
1. Document marked "OBSOLETE" or "SUPERSEDED"
2. Active distribution recalled
3. Electronic access restricted or document moved to archive
4. Hard copies stamped "OBSOLETE" or destroyed
5. Archive copy retained per retention requirements

#### 4.6.2 Master Document Retention
One copy of obsolete documents retained for:
- Reference purposes
- Historical record
- Regulatory compliance

### 4.7 External Documents

#### 4.7.1 External Document Types
- Industry standards (AS9100, ARP4754A, DO-178C, ECSS, etc.)
- Regulatory requirements
- Customer specifications and drawings
- Supplier documents

#### 4.7.2 External Document Control
1. External documents identified and listed in register
2. Current versions obtained and verified
3. Access provided to relevant personnel
4. Periodic checks for updates
5. Superseded versions removed from use

### 4.8 Document Register

#### 4.8.1 Register Contents
Document register (LOG_DOC_REGISTER.csv) includes:
- Document number
- Title
- Revision level
- Issue date
- Owner
- Approver
- Status (Draft, Active, Obsolete)
- Review due date
- Distribution list

#### 4.8.2 Register Maintenance
Document Controller:
- Updates register upon document approval
- Tracks review due dates
- Generates review notifications
- Maintains historical records

## 5. Digital Thread Integration

### 5.1 PLM/PDM Integration
Document control integrated with PLM/PDM system for:
- Engineering drawings and CAD models
- BOMs (Bill of Materials)
- Engineering change orders (ECOs)
- Design documentation

### 5.2 Traceability
Document numbers linked to:
- Requirements
- Design artifacts
- Test records
- Non-conformances
- CAPA records

### 5.3 API Integration
Document metadata accessible via APIs per section 12-DIGITAL_THREAD_HOOKS.

## 6. Records

### 6.1 Records Generated
- Document register (LOG_DOC_REGISTER.csv)
- Document change requests
- Review records
- Distribution logs
- Obsolescence notices

### 6.2 Record Retention
- Active documents: Duration of use + 10 years
- Obsolete documents: Per regulatory requirements (minimum 10 years)
- Design documents: Life of product + 10 years

## 7. Related Documents

### 7.1 Procedures
- PRO-003_CHANGE_CONTROL
- PRO-005_CAPA

### 7.2 Forms
- Change Request Form
- Document Review Checklist
- LOG_DOC_REGISTER.csv

### 7.3 Standards
- AS9100 Clause 7.5 (Documented Information)
- ISO 9001 Clause 7.5 (Documented Information)

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Quality Manager |
