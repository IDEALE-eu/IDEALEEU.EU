# PACKAGES — Supplier Data Packages

## Purpose
Complete data packages prepared for external suppliers, manufacturers, and fabricators.

## Contents
- Complete supplier packages (ZIP archives)
- DXF manufacturing files
- Supporting documentation (PDF)
- Material and process specifications
- Quality and inspection requirements
- Transmittal letters and instructions

## Package Types

### RFQ Packages (Request for Quote)
For quotation purposes:
- DXF files for geometry
- PDF reference drawings
- Material specifications
- Quantity and delivery requirements
- Quality standards
- Special requirements

### Production Packages
For production manufacturing:
- Released DXF files (approved revision)
- Detailed PDF drawings with tolerances
- Complete material specifications
- Manufacturing process requirements
- Inspection and test requirements
- Packaging and shipping instructions
- Purchase order reference

### Prototype Packages
For prototype/development:
- Current DXF files (may be draft)
- Design intent documentation
- Prototype-specific requirements
- Relaxed tolerances (if applicable)
- Expedited delivery requirements

## Package Structure
```
SUPPLIER_<supplier-code>_<package-type>_<date>.zip
├── DXF/
│   ├── <part1>.dxf
│   ├── <part2>.dxf
│   └── ...
├── DRAWINGS/
│   ├── <part1>.pdf
│   ├── <part2>.pdf
│   └── ...
├── SPECIFICATIONS/
│   ├── Materials.pdf
│   ├── Processes.pdf
│   └── Quality_Requirements.pdf
├── PACKAGE_INDEX.xlsx
└── TRANSMITTAL_LETTER.pdf
```

## Package Index
Include spreadsheet with:
- Part numbers and descriptions
- Quantities required
- Material specifications
- Delivery dates
- File names (DXF and PDF)
- Special notes and requirements

## Transmittal Letter
Include cover letter with:
- Package purpose (RFQ, production, etc.)
- Contact information
- Response deadline (for RFQ)
- Special instructions
- Package version/date

## File Naming
```
SUPPLIER_<code>_<type>_<version>_<date>.zip
```

Examples:
- `SUPPLIER_ABC-LASER_RFQ-001_V1_20250110.zip`
- `SUPPLIER_XYZ-MACHINE_PROD-PKG_V2_20250115.zip`
- `SUPPLIER_DEF-SHEETMETAL_PROTO_V1_20250108.zip`

## Supplier Information
Maintain for each package:
- Supplier name and code
- Contact person and email
- Date sent
- Package version
- Response deadline
- Acknowledgment received
- Questions and clarifications

## Quality Requirements
Specify in package:
- Dimensional tolerances
- Surface finish requirements
- Material certifications required
- Inspection reports format
- First article inspection (FAI) requirements
- Ongoing quality requirements

## Related Directories
- **[../ACK/](../ACK/)** — Supplier acknowledgments
- **[../../REVISIONS/RELEASED/](../../REVISIONS/RELEASED/)** — Released files
- **[../../QA/](../../QA/)** — Quality requirements

## Package Release Process
Before sending:
1. [ ] All files validated and tested
2. [ ] Correct revision included
3. [ ] Documentation complete
4. [ ] Material specs verified
5. [ ] Quality requirements defined
6. [ ] Contact information included
7. [ ] Package indexed
8. [ ] Version controlled

## Version Control
- Track package versions
- Document changes between versions
- Maintain history of packages sent
- Link to supplier responses
- Update as needed with revisions

## Follow-Up
After sending package:
- Confirm receipt by supplier
- Answer questions promptly
- Track acknowledgments in ACK/
- Resolve clarifications
- Document agreements
- Issue updates if needed

## Best Practices
- Complete and clear packages
- Avoid ambiguity in requirements
- Provide contact information
- Set clear expectations
- Professional transmittal letters
- Prompt response to questions
- Version control rigorously
