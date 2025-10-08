# 12-TEMPLATES

Standard forms and templates for MRO operations including task cards, MPD formats, NCR forms, and competency assessments.

## Purpose

Provide standardized templates ensuring consistency, completeness, and compliance across all MRO documentation and processes.

## Contents

- [**00-README.md**](00-README.md) - This file
- [**TASK_CARD_TEMPLATE.md**](TASK_CARD_TEMPLATE.md) - Maintenance task card format and structure
- [**MPD_TASK_FORMAT.csv**](MPD_TASK_FORMAT.csv) - Maintenance Planning Document task database schema
- [**MRO_NCR_FORM.md**](MRO_NCR_FORM.md) - Non-conformance report template
- [**COMPETENCY_ASSESSMENT_SHEET.md**](COMPETENCY_ASSESSMENT_SHEET.md) - Personnel competency evaluation form

## Overview

Standardized templates provide:
- **Consistency**: Uniform format across organization
- **Completeness**: Ensure all required information captured
- **Compliance**: Meet regulatory and quality system requirements
- **Efficiency**: Pre-structured documents reduce preparation time
- **Traceability**: Standardized data enables analysis and reporting

## Template Categories

### Maintenance Documentation
- **Task Cards**: Work instructions for specific maintenance activities
- **Job Cards**: Package of related tasks for a maintenance check
- **Inspection Reports**: Findings from scheduled and unscheduled inspections
- **Test Procedures**: Step-by-step functional and operational tests
- **Repair Procedures**: Damage assessment and repair instructions

### Program Management
- **MPD Tasks**: Structured format for maintenance program database
- **Reliability Reports**: PIREP, MAREP, component removal analysis
- **Engineering Orders**: Operator-specific modifications and procedures
- **Service Bulletin Compliance**: Tracking embodiment status

### Quality and Compliance
- **NCR Forms**: Non-conformance identification and resolution
- **CAPA Forms**: Corrective and preventive action tracking
- **Audit Checklists**: Internal and external audit protocols
- **Certificate of Release to Service**: Aircraft return-to-service authorization

### Workforce Management
- **Competency Assessments**: Knowledge and skills evaluation
- **Training Records**: Course completion and authorization tracking
- **OJT Logbooks**: On-the-job training documentation
- **Authorization Cards**: Personnel task approval records

### Logistics
- **Parts Requisitions**: Spare parts ordering forms
- **Receiving Inspection**: Incoming parts acceptance/rejection
- **Tool Calibration**: Calibration due dates and records
- **Loan/Exchange**: Temporary component tracking

## Task Card Template

### Essential Elements
```
Task Number: XXX-XX-XX-XXX (ATA chapter-section-task-interval)
Task Description: Brief summary of work to be performed
Effectivity: Aircraft/spacecraft serial numbers or configurations
Interval: Calendar time, flight hours/cycles, or condition
Zone/Access: Physical location and required access panels
Personnel: Number and qualifications (licensed, authorized, etc.)
Estimated Time: Labor hours for planning and scheduling
Tools: Special tools, test equipment, GSE required
Materials: Consumables, parts, fluids needed
References: Technical manual sections, engineering data
Procedure: Step-by-step instructions
Inspection: Sign-off points and quality checks
```

See [**TASK_CARD_TEMPLATE.md**](TASK_CARD_TEMPLATE.md) for detailed format.

### Task Card Types
- **Inspection (INS)**: Visual or detailed examination
- **Operational Check (OPC)**: Functional verification
- **Servicing (SVC)**: Fluid replenishment
- **Lubrication (LUB)**: Application of lubricants
- **Restoration (RST)**: Component overhaul or replacement
- **Discard (DIS)**: Life-limited part replacement

## MPD Task Format

### Database Schema
[**MPD_TASK_FORMAT.csv**](MPD_TASK_FORMAT.csv) defines columns:
- **Task_ID**: Unique identifier (e.g., 321100-01-001-006)
- **Description**: Task title and summary
- **Interval**: Threshold and repeat values
- **Type**: Task category (INS, OPC, SVC, etc.)
- **Reference**: AMM/WDM/SRM section
- **Zone**: Aircraft location
- **Access**: Panels/doors to be opened
- **Man-Hours**: Estimated labor time
- **Skill**: Required license and authorization
- **Tools**: Special equipment needed
- **Parts**: Consumables and replaceable items
- **Effectivity**: Applicable serial numbers

### Interval Notation
- **FH**: Flight hours (e.g., 6000 FH)
- **FC**: Flight cycles (e.g., 8000 FC)
- **DY**: Calendar days (e.g., 24 DY)
- **MO**: Calendar months (e.g., 12 MO)
- **CM**: Condition monitoring (no fixed interval)

### Integration
- Import into maintenance management systems
- Generate work packages and planning
- Track compliance and due dates

## NCR Form Template

### Form Sections
1. **Identification**: NCR number, date, originator, location
2. **Description**: What, when, where, how discovered
3. **Classification**: Major/minor, safety impact, customer impact
4. **Containment**: Immediate actions to prevent continuation
5. **Root Cause**: Analysis using 5 Whys, fishbone, etc.
6. **Corrective Action**: Permanent fix with timeline
7. **Preventive Action**: Systemic improvements
8. **Verification**: Effectiveness check and sign-off
9. **Closure**: Approval by quality manager

See [**MRO_NCR_FORM.md**](MRO_NCR_FORM.md) for complete template.

### NCR Categories
- **Maintenance Errors**: Work performed incorrectly
- **Documentation Errors**: Incorrect or missing paperwork
- **Parts Issues**: Defective, wrong, or unapproved parts
- **Facility Issues**: Inadequate tools, equipment, environment
- **Procedure Issues**: Ambiguous or incorrect instructions
- **Training Issues**: Personnel lacking knowledge/skills

## Competency Assessment

### Assessment Components
1. **Knowledge**: Written exam or oral questioning
2. **Skills**: Practical demonstration or portfolio review
3. **Experience**: Number of task completions under supervision
4. **Attitude**: Safety culture, teamwork, quality focus

### Competency Levels
- **Level 1 - Awareness**: Understands concepts
- **Level 2 - Supervised**: Performs with oversight
- **Level 3 - Independent**: Competent without supervision
- **Level 4 - Expert**: Can train others
- **Level 5 - Master**: Industry-recognized authority

### Authorization Record
- **Task**: Specific maintenance activity
- **Training Date**: When training completed
- **Assessment Date**: When competency evaluated
- **Assessor**: Who conducted evaluation
- **Validity**: Expiration date for recurrent authorization
- **Restrictions**: Any limitations on authorization

See [**COMPETENCY_ASSESSMENT_SHEET.md**](COMPETENCY_ASSESSMENT_SHEET.md) for form structure.

## Template Management

### Version Control
- **Document Number**: Unique identifier
- **Revision**: Version number and date
- **Changes**: Summary of modifications from previous version
- **Approval**: Quality manager or designee signature
- **Distribution**: Controlled copy list

### Review and Update
- **Periodic Review**: Annual assessment of continued applicability
- **Change Requests**: Process for suggesting improvements
- **Regulatory Updates**: Incorporate new requirements
- **Lessons Learned**: Update based on operational experience

### Digital Forms
- **Electronic Signatures**: Secure, auditable sign-offs
- **Auto-Population**: Pre-fill from databases (e.g., aircraft S/N)
- **Validation Rules**: Prevent incomplete or inconsistent data
- **Workflow**: Route for approvals and notifications
- **Archival**: Long-term retention and retrieval

## Integration Points

### Technical Publications
- Task cards reference manual procedures
- Template updates follow publication change process
- See [**../02-TECHNICAL_PUBLICATIONS/**](../02-TECHNICAL_PUBLICATIONS/)

### Maintenance Program
- MPD tasks drive work package generation
- Task intervals and requirements standardized
- See [**../03-MAINTENANCE_PROGRAM/**](../03-MAINTENANCE_PROGRAM/)

### Quality System
- NCR forms track non-conformances
- Templates audited for compliance
- See [**../06-QUALITY_AND_COMPLIANCE/**](../06-QUALITY_AND_COMPLIANCE/)

### Workforce Training
- Competency assessment forms track authorizations
- Training completion documented consistently
- See [**../07-WORKFORCE_AND_TRAINING/**](../07-WORKFORCE_AND_TRAINING/)

### Configuration Management
- Template version control via document management system
- Changes follow ECR process for controlled documents
- See [**../08-INTEGRATIONS/CONFIG_MGMT_FEEDBACK.md**](../08-INTEGRATIONS/CONFIG_MGMT_FEEDBACK.md)

### Metrics and KPIs
- Standardized data enables consistent reporting
- Form completion metrics track process compliance
- See [**../11-METRICS_AND_KPIs/**](../11-METRICS_AND_KPIs/)

## Customization Guidelines

### Approved Modifications
- **Company Branding**: Logo, colors, contact information
- **Additional Fields**: Extra data fields (must not remove required fields)
- **Translations**: Local language versions with English original
- **Automation**: Pre-population and workflow enhancements

### Prohibited Changes
- **Required Fields**: Cannot remove regulatory or quality system requirements
- **Data Formats**: Must maintain compatibility with databases and systems
- **Approval Sections**: Cannot bypass required sign-offs
- **Traceability**: Must maintain audit trail and version control

## Related Documents

- [**../02-TECHNICAL_PUBLICATIONS/**](../02-TECHNICAL_PUBLICATIONS/) - Source procedures for task cards
- [**../03-MAINTENANCE_PROGRAM/**](../03-MAINTENANCE_PROGRAM/) - MPD tasks and intervals
- [**../06-QUALITY_AND_COMPLIANCE/**](../06-QUALITY_AND_COMPLIANCE/) - NCR process and quality forms
- [**../07-WORKFORCE_AND_TRAINING/**](../07-WORKFORCE_AND_TRAINING/) - Competency framework
- [**../08-INTEGRATIONS/CONFIG_MGMT_FEEDBACK.md**](../08-INTEGRATIONS/CONFIG_MGMT_FEEDBACK.md) - Document control
- [**../11-METRICS_AND_KPIs/**](../11-METRICS_AND_KPIs/) - Performance measurement from standardized data
- [**../../../00-PROGRAM/CONFIG_MGMT/**](../../../00-PROGRAM/CONFIG_MGMT/) - Enterprise document management
- [**../../../00-PROGRAM/QUALITY_QMS/**](../../../00-PROGRAM/QUALITY_QMS/) - Quality system templates
