# Templates — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Master templates for work instructions (WI), assembly plans (PLAN), inspection checklists (CHK), torque tables (TOR), and other CAI documents. Templates provide consistent structure and formatting for controlled documents.

## Content Types

- **WI Templates** — Work instruction document templates
- **PLAN Templates** — Assembly plan templates
- **CHK Templates** — Inspection checklist templates
- **TOR Templates** — Torque table templates
- **Traveler Templates** — Serialized data collection forms
- **Report Templates** — ATP, ATR, as-run record formats

## File Formats

- `.docx` — Editable Word templates for documents
- `.xlsx` — Excel templates for data sheets and checklists
- `.pptx` — PowerPoint templates for presentations
- `.pdf` — Reference versions of released templates

## Naming Convention

```
Template_{type}_{description}_v{version}.{ext}
```

**Examples:**
- `Template_WI_Installation_Procedure_v01.docx`
- `Template_PLAN_Assembly_Sequence_v02.xlsx`
- `Template_CHK_Inspection_Checklist_v01.xlsx`
- `Template_TOR_Torque_Table_v01.docx`
- `Template_TRV_Traveler_Data_v03.xlsx`

## Template Components

### Work Instruction Template
- **Header:** Document ID, title, revision, approval signatures
- **Purpose/Scope:** Applicable hardware and operations
- **Prerequisites:** Required training, certs, prior steps
- **Materials & Equipment:** Parts list, tools, MGSE
- **Safety:** Hazards, PPE, ESD precautions
- **Procedure:** Numbered steps with acceptance criteria
- **Inspection Points:** QA hold points
- **Sign-off Block:** Mechanic, inspector, engineer
- **References:** Drawings, specs, related documents
- **Revision History:** Change log

### Assembly Plan Template
- **Header:** Document ID, title, revision
- **Scope:** Hardware assemblies covered
- **Flow Diagram:** Visual sequence representation
- **Operations List:** Steps with duration and resources
- **Dependencies:** Predecessor/successor relationships
- **Hold Points:** Required inspections
- **Resources:** Personnel, tools, facilities
- **Risk Items:** Critical operations and mitigations
- **Sign-off Block:** Engineering approval

### Inspection Checklist Template
- **Header:** Document ID, hardware serial, date
- **Checklist Items:** Acceptance criteria with pass/fail
- **Data Recording:** Fields for measurements
- **Tools/Gages:** Required inspection equipment
- **Method:** Inspection procedure reference
- **Non-conformance:** Process if criteria not met
- **Sign-off Block:** Inspector stamp and date

### Torque Table Template
- **Header:** Document ID, title, revision
- **Fastener Specifications:** Type, size, grade, material
- **Torque Values:** Target torque with tolerances
- **Torque Pattern:** Sequence diagram
- **Re-torque:** Requirements and timing
- **Tooling:** Required torque wrench specifications
- **Notes:** Special conditions, lubrication

### Traveler Template
- **Header:** Part number, serial number
- **Traceability:** Component serials, batch numbers
- **Operation Log:** Date, time, operator, inspector
- **Data Recording:** Measurements, torques, gaps
- **Inspection Results:** Pass/fail, deviations
- **Sign-off Blocks:** Each operation approved
- **Final Configuration:** As-built part list

## Template Usage

1. **Select Template:** Choose appropriate template for document type
2. **Customize:** Fill in specific hardware and procedures
3. **Review:** Engineering review of content
4. **Approve:** Obtain required approvals
5. **Release:** Issue as controlled document with proper ID and revision
6. **Maintain:** Update template based on lessons learned

## Template Standards

- **Branding:** IDEALE logo and document formatting
- **Fonts:** Arial or similar sans-serif, 10-12pt
- **Margins:** 1 inch (25mm) all sides
- **Headers/Footers:** Document ID, revision, page number
- **Tables:** Grid format for data entry
- **Signature Blocks:** Name, date, signature line
- **Revision Tracking:** Document history table

## Document Control

- **Template Version:** Maintain version control on templates
- **Master Location:** Templates stored in this directory
- **Access:** Read-only for users; edit rights for document control
- **Updates:** Template changes require document control approval
- **Distribution:** Users copy template to create new documents

## Cross-References

- [Parent: CAI](../README.md)
- [Work Instructions](../work_instructions/README.md)
- [Assembly Plans](../assembly_plans/README.md)
- [Travelers](../travelers/README.md)
- [Inspection Checklists](../inspection_checklists/README.md)
- [Torque Tables](../torque_tables/README.md)

## Template Maintenance

- **Review Frequency:** Annual or as needed
- **Update Process:** Document control board approval
- **Feedback:** Collect user feedback for improvements
- **Lessons Learned:** Incorporate field experience
- **Consistency:** Ensure compatibility across templates

## Available Templates

| Template Type | Current Version | Description |
|---------------|-----------------|-------------|
| WI_Installation | v01 | General installation work instruction |
| WI_Bonding | v01 | Adhesive/TIM application procedure |
| PLAN_Assembly | v01 | Master assembly plan format |
| CHK_Flatness | v01 | Surface flatness inspection |
| CHK_Ports | v01 | Port and thread inspection |
| CHK_TIM | v01 | TIM thickness verification |
| TOR_Metric | v01 | Metric fastener torque table |
| TRV_Integration | v03 | Integration traveler data sheet |
| ATP_Leak | v01 | Leak test procedure template |
| ATR_Generic | v01 | Generic test report format |

## Future Templates

- Witness coupon test procedure
- MGSE usage guide
- Kitting checklist
- As-run data collection form
- Configuration audit report
