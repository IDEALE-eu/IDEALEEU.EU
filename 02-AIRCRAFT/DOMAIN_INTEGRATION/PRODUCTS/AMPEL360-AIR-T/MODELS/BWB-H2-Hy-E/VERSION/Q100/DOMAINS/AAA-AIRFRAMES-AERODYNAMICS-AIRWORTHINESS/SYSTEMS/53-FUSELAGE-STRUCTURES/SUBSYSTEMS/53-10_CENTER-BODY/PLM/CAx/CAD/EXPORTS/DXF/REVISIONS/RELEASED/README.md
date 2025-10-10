# RELEASED — Released DXF Files

## Purpose
Approved and released DXF files authorized for manufacturing and use.

## Contents
- Formally approved drawings
- Released manufacturing files
- Production-authorized exports
- Supplier package files
- Official configuration items

## File Status
Files in RELEASED are:
- ✅ **Approved** for manufacturing
- ✅ **Authorized** for use
- 🔒 **Configuration controlled**
- 📋 **Formally documented**
- 🎯 **Production ready**

## File Naming
```
<part>_<description>_<REV>_<date>.dxf
```

Examples:
- `53-10-FRM05_FRAME_A_20250110.dxf` (Rev A)
- `53-10-SKIN10_FLAT_B_20250115.dxf` (Rev B)
- `53-10-BRK03_BRACKET_A_20250110.dxf` (Rev A)

## Revision Scheme
- **Rev A**: First released revision
- **Rev B, C, D...**: Subsequent revisions
- Each revision supersedes previous

## Release Requirements
Before moving to RELEASED:
- [ ] Design review completed and approved
- [ ] Engineering sign-off obtained
- [ ] Manufacturing review completed
- [ ] Quality requirements defined
- [ ] Documentation package complete
- [ ] File validation passed
- [ ] Change order issued (if applicable)

## Release Documentation
Each release must include:
- Part number and revision
- Release date
- Approval signatures
- Change description (if not Rev A)
- Reference to ECO/PCO (if applicable)
- Material and process specifications
- Quality and inspection requirements

## Configuration Management
Released files are:
- Tracked in configuration management system
- Referenced in bills of material (BOM)
- Subject to change control process
- Archived with proper version control
- Linked to production records

## Change Control
To modify a RELEASED file:
1. Create new draft with next revision letter
2. Develop and review changes
3. Obtain approvals via ECO/PCO process
4. Release new revision
5. Move previous revision to OBSOLETE

## Related Directories
- **[../DRAFT/](../DRAFT/)** — Files under development
- **[../OBSOLETE/](../OBSOLETE/)** — Superseded revisions
- **[../../PARTS/](../../PARTS/)** — Current part files
- **[../../SUPPLIERS/PACKAGES/](../../SUPPLIERS/PACKAGES/)** — Supplier packages

## Usage Guidelines
**DO**:
- Use for manufacturing and production
- Share with approved suppliers
- Reference in production documentation
- Include in supplier packages
- Maintain traceability

**DO NOT**:
- Modify without change control
- Use superseded revisions
- Skip revision sequence
- Release without approvals

## Archive and Retention
- Keep all released revisions
- Maintain complete revision history
- Archive per company retention policy
- Link to manufacturing records
- Preserve for configuration control

## Best Practices
- Formal release process required
- Complete documentation package
- Clear revision identification
- Proper approval documentation
- Traceable to change orders
- Regular audits and verification
