---
area: "00-PROGRAM/COMPLIANCE/99-TEMPLATES"
owner: "Compliance Office"
status: "Active"
utcs_anchor: "utcs://PROGRAM/COMPLIANCE/TEMPLATES"
confidentiality: "Internal"
---

# 99-TEMPLATES

Standard forms, templates, and schemas for compliance documentation and data exchange.

## Purpose

Provide consistent, reusable templates for compliance activities to ensure completeness, standardization, and efficient information capture across the IDEALEEU.EU program.

## Contents

### Document Templates

#### Compliance Documentation
- **Compliance Matrix Template** - Pre-formatted spreadsheet with required columns
- **Statement of Compliance** - Formal compliance declaration template
- **Compliance Checklist** - By standard (DO-178C, DO-254, ARP4754A, etc.)
- **Certification Plan** - PSAC/PHAC outline template
- **Tool Qualification** - TQP/TOR/TQD templates

#### Process Documents
- **Work Instruction** - Standard WI format with approval workflow
- **Standard Operating Procedure** - SOP template with revision control
- **Policy Document** - Policy statement template
- **Process Flow Diagram** - Standard notation and layout

#### Forms
- **Deviation/Waiver Request** - Request form with approval routing
- **CAPA Form** - Corrective/Preventive Action documentation
- **Audit Finding** - Finding report and response template
- **Non-Conformance Report** - NCR form
- **Evidence Submission** - Evidence package cover sheet

### Data Schemas

#### CSV Templates
Pre-configured CSV files with headers and validation rules:
- `COMPLIANCE_MATRIX_TEMPLATE.csv`
- `DEVIATIONS_WAIVERS_TEMPLATE.csv`
- `CAPA_LOG_TEMPLATE.csv`
- `EVIDENCE_INDEX_TEMPLATE.csv`
- `ROPA_TEMPLATE.csv`
- `EXPORT_CLASSIFICATION_TEMPLATE.csv`

#### YAML/JSON Schemas
Structured data formats for tool integration:
- `compliance_matrix.schema.json`
- `evidence_package.schema.yaml`
- `capa_record.schema.json`
- `audit_finding.schema.yaml`

#### XML Schemas
Authority-specific submission formats:
- `easa_compliance_submission.xsd`
- `faa_certification_package.xsd`

### Checklists

#### Standards Compliance
- **DO-178C Checklist** - All objectives by DAL (A, B, C, D, E)
- **DO-254 Checklist** - Hardware assurance objectives
- **ARP4754A Checklist** - Systems development objectives
- **ARP4761 Checklist** - Safety assessment tasks
- **AS9100 Checklist** - Quality system requirements
- **ECSS Checklist** - Space standards requirements by ECSS volume

#### Process Compliance
- **Document Review Checklist** - Peer review criteria
- **Code Review Checklist** - Software inspection criteria
- **Audit Preparation Checklist** - Pre-audit readiness
- **Test Readiness Checklist** - Test execution prerequisites
- **Design Review Checklist** - PDR/CDR/TRR criteria

### Report Templates

#### Management Reports
- **Compliance Status Report** - Monthly dashboard
- **CAPA Status Report** - Open/closed/overdue summary
- **Audit Results Report** - Findings and recommendations
- **Risk Report** - Compliance risk register summary
- **Metrics Dashboard** - KPIs and trends

#### Technical Reports
- **Compliance Analysis Report** - Gap analysis results
- **Test Compliance Report** - Verification results vs. requirements
- **Tool Qualification Report** - TQR summary
- **Safety Assessment Report** - FHA/PSSA/SSA results

### Presentation Templates

PowerPoint/slide decks for:
- **Certification Review** - Authority presentation format
- **Management Review** - Executive briefing format
- **Training Materials** - Standard training slide master
- **Audit Briefing** - Audit opening/closing meeting

## Template Structure

All templates include:
- **Header**: Document ID, title, version, date
- **Metadata**: Owner, approver, review date, status
- **Instructions**: How to use the template (may be hidden/removed in final)
- **Content Sections**: Pre-formatted sections with guidance
- **Footer**: Document control information, page numbers
- **Change Log**: Revision history table

## Usage Guidelines

### Selecting Templates
- Use the template appropriate for the document type
- Do not modify template structure without approval
- Tailor content as needed but maintain format

### Filling Out Templates
- Replace [PLACEHOLDER] text with actual content
- Delete instructional text (shown in italics or brackets)
- Complete all required fields
- Mark N/A for non-applicable sections with justification

### Customization
- Minor customization (fonts, logos) allowed
- Structural changes require Compliance Office approval
- Custom templates for specific contracts approved case-by-case

### Version Control
- Templates versioned separately from documents created from them
- Template version noted in document metadata
- Old template versions archived but available

## Key Artifacts

### TEMPLATE_CATALOG.xlsx
Master list of all templates:
- Template ID, Name, Description
- File Location, Format (Word, Excel, PDF)
- Version, Last Updated
- Owner, Usage Count
- Related Standard/Process

### TEMPLATE_LIBRARY/
Organized by category:
- `COMPLIANCE_DOCS/` - Compliance matrices, checklists, statements
- `CERTIFICATIONS/` - Plans, reports, submissions
- `QUALITY/` - NCR, CAPA, audit forms
- `RISK/` - Risk registers, assessments
- `EXPORT/` - Classification, screening, licensing
- `PRIVACY/` - DPIA, RoPA, notices
- `REPORTS/` - Status reports, dashboards
- `PRESENTATIONS/` - Slide decks

### SCHEMAS/
Data structure definitions:
- `CSV/` - CSV templates with headers
- `JSON/` - JSON schemas for API/tool integration
- `YAML/` - YAML schemas for configuration/data
- `XML/` - XML schemas for authority submissions

### EXAMPLES/
Filled-out examples (anonymized/fictitious):
- Show proper completion
- Demonstrate good practices
- Training aids

## Template Development Process

1. **Need Identification**: Gap in existing templates
2. **Drafting**: SME creates draft template
3. **Review**: Stakeholders review and comment
4. **Testing**: Pilot use in small scope
5. **Approval**: Compliance Office approves
6. **Release**: Published to template library
7. **Training**: Users trained on new template
8. **Maintenance**: Periodic review and update

## Template Governance

### Template Owner
Each template has designated owner:
- Maintains template
- Approves customizations
- Reviews for currency
- Addresses user feedback

### Change Control
Template changes:
- Minor (formatting, typos): Owner approval
- Major (structure, content): Compliance Office approval
- New templates: Same as major changes

### Feedback
Users encouraged to:
- Report errors or ambiguities
- Suggest improvements
- Request new templates
- Share lessons learned

Submit via `template_feedback@idealeeu.eu` (placeholder)

## Compliance Automation

### Template-Driven Tools
Tools that consume/produce template formats:
- Compliance matrix validators
- Evidence hash calculators
- CAPA SLA checkers
- Automated report generators

### Integration
Templates designed for:
- PLM/PDM integration
- CI/CD pipeline consumption
- Dashboard data feeds
- Authority submission systems

### Validation Rules
Embedded in schema files:
- Required fields
- Data types and formats
- Allowed values (enumerations)
- Cross-field dependencies

## Localization

Templates available in:
- English (primary)
- German, French, Italian, Spanish (EU languages)
- Additional languages as needed

Authority-specific templates:
- EASA format for EU submissions
- FAA format for US submissions
- ESA format for space missions

## Quality Assurance

Templates reviewed for:
- **Completeness**: All necessary information captured
- **Clarity**: Instructions and fields unambiguous
- **Compliance**: Meets standard/regulatory requirements
- **Usability**: Easy to understand and complete
- **Consistency**: Aligns with other program templates

## Training Materials

Template-specific training:
- User guides for complex templates
- Video tutorials for key templates
- Quick reference cards
- FAQ documents
- Example walk-throughs

## Metrics

- Template usage (downloads/uses)
- User satisfaction (survey ratings)
- Error rates (incorrect completions)
- Efficiency (time to complete)
- Compliance (audit findings related to template use)

## Integration Points

- **Document Control**: [`../../CONFIG_MGMT/01-DOCUMENTS/`](../../CONFIG_MGMT/01-DOCUMENTS/)
- **Quality System**: [`../../QUALITY_QMS/04-FORMS_TEMPLATES/`](../../QUALITY_QMS/04-FORMS_TEMPLATES/)
- **Standards**: [`../01-STANDARDS/`](../01-STANDARDS/)
- **Tools**: [`../98-TOOLS/`](../98-TOOLS/)

## Related Documents

- Document Control Procedure: [`../../QUALITY_QMS/02-PROCEDURES/PRO-001_DOC_CONTROL.md`](../../QUALITY_QMS/02-PROCEDURES/PRO-001_DOC_CONTROL.md)
- Compliance Policies: [`../02-POLICIES/`](../02-POLICIES/)
- Standards Library: [`../01-STANDARDS/`](../01-STANDARDS/)

## Template Requests

To request a new template or modification:
1. Submit request via compliance portal or email
2. Describe need and justification
3. Provide example or draft if available
4. Compliance Office reviews and prioritizes
5. Development and approval per process
6. Release and training

---

**Owner**: Compliance Office (Template Librarian)  
**Review**: Semi-annual review of template library  
**Approval**: Compliance Officer

**💡 TIP**: Always use the latest template version. Check the template library for updates before starting new documents.
