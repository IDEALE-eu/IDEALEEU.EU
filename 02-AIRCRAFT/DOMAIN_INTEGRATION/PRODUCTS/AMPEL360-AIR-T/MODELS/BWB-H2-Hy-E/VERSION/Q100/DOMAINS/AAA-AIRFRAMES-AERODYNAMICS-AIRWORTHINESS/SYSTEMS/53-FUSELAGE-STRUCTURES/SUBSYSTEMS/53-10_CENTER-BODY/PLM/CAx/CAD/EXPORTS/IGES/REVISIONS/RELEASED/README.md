# RELEASED — Released Revision IGES Files

## Purpose

This directory contains IGES export files that have been formally approved and released for use in manufacturing, supplier distribution, or other controlled purposes.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Approved geometry**: Design-reviewed and approved models
- **Released revisions**: Files under formal configuration control
- **Production files**: Geometry released for manufacturing
- **Supplier packages**: Files distributed to suppliers
- **Certified geometry**: Geometry for regulatory submittals

## File Status

**Released** status indicates:
- ✅ **Approved**: Design reviewed and formally approved
- ✅ **Configuration controlled**: Under formal change management
- ✅ **Manufacturing authorized**: Can be used for production
- ✅ **Distributable**: Can be shared with suppliers/partners
- ✅ **Traceable**: Linked to engineering drawings and documentation

## File Naming Convention

```
<subsystem>_<component>_<part-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_FRAME-F01_PN-12345_RevA_20250110.igs`
- `53-10_PANEL_PN-12346_RevB_20250110.igs`
- `53-10_BULKHEAD_PN-12347_RevC_20250110.igs`

Use formal revision letters (RevA, RevB, RevC, etc.) for released files.

## Revision Control

Released files follow formal revision control:
- **Rev A**: Initial release
- **Rev B, C, D...**: Subsequent revisions after engineering changes
- Each revision requires ECR/ECO approval
- Previous revisions move to [`../OBSOLETE/`](../OBSOLETE/) when superseded

## Usage Authorization

Released IGES files are authorized for:
- ✅ Manufacturing and production
- ✅ Tooling design and fabrication
- ✅ Supplier distribution and quotes
- ✅ Assembly and installation
- ✅ Quality inspection
- ✅ Certification submittals
- ✅ Technical publications

## Configuration Management

Released files must be:
- Approved through formal design review
- Linked to engineering drawings
- Tracked in PDM/PLM system
- Subject to ECR/ECO for changes
- Maintained with revision history
- Cross-referenced to source CAD files

## Release Process

Before releasing IGES files:
1. Complete design validation
2. Obtain design review approval
3. Verify against engineering drawings
4. Test import in target system
5. Assign revision letter
6. Update PDM/PLM records
7. Distribute to authorized recipients
8. Archive in released directory

## Related Directories

- **Parent**: [`../`](../) — All REVISIONS
- **Draft**: [`../DRAFT/`](../DRAFT/) — Work-in-progress files
- **Obsolete**: [`../OBSOLETE/`](../OBSOLETE/) — Superseded revisions
- **Suppliers**: [`../../SUPPLIERS/PACKAGES/`](../../SUPPLIERS/PACKAGES/) — Supplier distribution packages

## Best Practices

- Maintain clear revision history
- Cross-reference to engineering drawings
- Document change description for each revision
- Link to ECR/ECO numbers
- Archive previous revisions properly
- Notify stakeholders of new releases
- Verify files before release
- Maintain traceability to source models

## Release Documentation

Each released file should have:
- **Engineering drawing**: Formal drawing with dimensions
- **Part number**: Unique part identifier
- **Revision letter**: Current revision designation
- **Release date**: Date of formal release
- **Approval signatures**: Design review approvals
- **Change history**: Description of changes from previous revision
- **ECR/ECO reference**: Engineering change order number

## Distribution Control

When distributing released IGES files:
- Verify recipient authorization
- Include release metadata (part number, revision, date)
- Provide accompanying documentation (drawings, specs)
- Track distribution records
- Communicate any restrictions or limitations
- Request acknowledgment of receipt

## Superseding Files

When a new revision is released:
1. Move previous revision to [`../OBSOLETE/`](../OBSOLETE/)
2. Update PDM/PLM to reflect current revision
3. Notify users of previous revision
4. Update supplier and manufacturing teams
5. Archive previous revision for record retention
