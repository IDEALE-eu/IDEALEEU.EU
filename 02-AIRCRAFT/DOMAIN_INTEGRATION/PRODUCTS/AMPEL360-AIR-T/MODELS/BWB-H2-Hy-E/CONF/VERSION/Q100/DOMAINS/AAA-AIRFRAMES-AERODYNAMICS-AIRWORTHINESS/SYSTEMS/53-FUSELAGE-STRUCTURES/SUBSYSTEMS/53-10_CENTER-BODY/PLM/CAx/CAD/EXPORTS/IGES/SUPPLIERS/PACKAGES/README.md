# PACKAGES — Supplier Distribution Packages

## Purpose

This directory contains IGES export files organized into distribution packages for suppliers, manufacturers, and external partners.

## Content

Store IGES files (`.igs` or `.iges`) organized as:
- **Supplier packages**: Complete geometry sets for specific suppliers
- **Manufacturing packages**: Files for manufacturing partners
- **Bid packages**: Geometry for RFQ (Request for Quote) responses
- **Production packages**: Released files for production suppliers
- **Subcontractor packages**: Geometry for subcontracted work

## Package Organization

Organize packages by:
- **Supplier name**: Group files by recipient supplier
- **Package date**: Distribution date
- **Work scope**: Type of work or components
- **Contract/PO**: Purchase order or contract number

## File Naming Convention

```
<supplier-name>_<subsystem>_PKG_<package-id>_<date>.zip
```

**Examples:**
- `SUPPLIER-A_53-10_PKG_001_20250110.zip`
- `SUPPLIER-B_53-10_PKG_002_20250115.zip`

Compress related IGES files into ZIP packages for distribution.

## Package Contents

Each supplier package should include:
- **IGES files**: Geometry for manufacturing/assembly
- **README.txt**: Package contents and instructions
- **Drawings (PDF)**: Engineering drawings for reference
- **BOM**: Bill of materials (if applicable)
- **Specifications**: Material and process specifications
- **Metadata**: Part numbers, revisions, dates

## Package Structure Example

```
SUPPLIER-A_53-10_PKG_001_20250110.zip
├── IGES/
│   ├── 53-10_FRAME-F01_PN-12345_RevA_20250110.igs
│   ├── 53-10_FRAME-F02_PN-12346_RevA_20250110.igs
│   └── 53-10_BULKHEAD_PN-12347_RevA_20250110.igs
├── DRAWINGS/
│   ├── DWG-12345_RevA.pdf
│   ├── DWG-12346_RevA.pdf
│   └── DWG-12347_RevA.pdf
├── BOM_53-10_Package-001.xlsx
├── SPECIFICATIONS.pdf
└── README.txt
```

## Distribution Process

1. **Package preparation**: Gather all required files
2. **Verification**: Verify file accuracy and completeness
3. **Documentation**: Prepare README and instructions
4. **Compression**: Create ZIP package
5. **Distribution**: Send via secure file transfer
6. **Tracking**: Record distribution in log
7. **Acknowledgment**: Request supplier receipt confirmation

## Related Directories

- **Parent**: [`../`](../) — All SUPPLIERS
- **Acknowledgments**: [`../ACK/`](../ACK/) — Supplier acknowledgments
- **Released**: [`../../REVISIONS/RELEASED/`](../../REVISIONS/RELEASED/) — Source files
- **Parts**: [`../../PARTS/`](../../PARTS/) — Individual part exports

## Best Practices

- Include complete package with all necessary files
- Provide clear README with instructions
- Verify file quality before distribution
- Use secure file transfer methods
- Track package distribution
- Request acknowledgment of receipt
- Maintain distribution records
- Version packages for updates

## Package README Template

Each package should include README.txt with:
```
SUPPLIER PACKAGE: [Package ID]
DATE: [Distribution Date]
SUPPLIER: [Supplier Name]
CONTRACT: [Contract/PO Number]

CONTENTS:
- IGES Files: [Number] files
- Drawings: [Number] PDF drawings
- BOM: [BOM filename]
- Specifications: [Spec documents]

INSTRUCTIONS:
1. Verify all files open correctly
2. Review drawings and specifications
3. Contact [Engineer Name] with questions
4. Acknowledge receipt within [X] days
5. Report any file issues immediately

CONTACT:
[Engineer Name]
[Email]
[Phone]

NOTES:
[Additional notes or special instructions]
```

## Distribution Log

Maintain log of packages:
- Package ID and date
- Supplier name
- Contents summary
- Distribution method
- Recipient confirmation
- Follow-up actions

## Quality Assurance

Before distributing packages:
- [ ] All files open successfully
- [ ] Drawings match geometry
- [ ] BOM accurate and complete
- [ ] Specifications included
- [ ] README clear and complete
- [ ] Package properly labeled
- [ ] Distribution authorized

## Follow-Up

After distribution:
- Request acknowledgment within defined timeframe
- Address any supplier questions
- Track quote responses or production status
- Update package if changes occur
- Maintain communication with supplier
- Archive package for records
