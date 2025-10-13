# SUPPLIERS — Supplier Packages and Communications

## Purpose
DXF files and packages prepared for external suppliers and manufacturers.

## Contents
- **[PACKAGES/](PACKAGES/)** — Complete supplier data packages
- **[ACK/](ACK/)** — Supplier acknowledgments and returned data

## Organization
Organize by:
- Supplier name or code
- Package type (RFQ, production, prototype)
- Part or assembly scope
- Date and version

## File Naming Convention
```
SUPPLIER_<supplier-code>_<package-type>_<date>.zip
```

Individual files:
```
<part>_<description>_<supplier>_<revision>_<date>.dxf
```

Examples:
- `SUPPLIER_ABC-MFG_RFQ-001_20250110.zip`
- `SUPPLIER_XYZ-FAB_PROD-PKG_20250110.zip`
- `53-10-FRM01_FRAME_ABC-MFG_A_20250110.dxf`

## Package Contents
Complete supplier packages include:
- DXF files (geometry)
- PDF drawings (reference)
- Material specifications
- Process requirements
- Quality requirements
- Inspection criteria
- Packaging and shipping instructions
- Contact information

## Guidelines
- Include complete documentation
- Specify material and process clearly
- Define acceptance criteria
- Include contact information
- Track package versions
- Maintain supplier communications

## Related Directories
- **[../PARTS/](../PARTS/)** — Source part files
- **[../REVISIONS/RELEASED/](../REVISIONS/RELEASED/)** — Released files for suppliers
- **[../QA/](../QA/)** — Quality requirements

## Best Practices
- Complete and clear documentation
- Formal package release process
- Track supplier acknowledgments
- Version control for packages
- Maintain communication records
- Follow-up on supplier questions
