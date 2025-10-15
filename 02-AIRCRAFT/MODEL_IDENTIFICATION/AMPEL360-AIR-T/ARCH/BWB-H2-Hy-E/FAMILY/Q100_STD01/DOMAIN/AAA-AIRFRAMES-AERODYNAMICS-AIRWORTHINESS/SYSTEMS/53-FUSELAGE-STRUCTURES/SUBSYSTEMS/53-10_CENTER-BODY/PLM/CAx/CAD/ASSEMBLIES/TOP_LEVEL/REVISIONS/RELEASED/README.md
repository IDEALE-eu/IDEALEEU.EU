# RELEASED — Released Revisions

## Purpose

This directory contains formally released versions of the top-level assembly that have been approved for use.

## Released Status

### Characteristics
- **Formally approved**: Passed all reviews and approvals
- **Baselined**: Configuration controlled
- **For production**: Can be used for manufacturing
- **Traceable**: Linked to requirements and change orders
- **Archived**: Preserved for record

### Release Types
- **Production release**: For manufacturing
- **Certification release**: For regulatory approval
- **Customer delivery**: For customer use
- **Configuration baseline**: Reference configuration

## Release Process

### Release Criteria
- [ ] Design review completed and approved
- [ ] All validation checks passed
- [ ] Interference issues resolved
- [ ] Mass properties verified
- [ ] BOM complete and accurate
- [ ] Drawings released
- [ ] Documentation complete
- [ ] Required signatures obtained

### Approval Chain
1. **Author**: Design engineer
2. **Checker**: Peer review
3. **Stress**: Structural analysis approval
4. **Manufacturing**: Producibility review
5. **Quality**: Quality assurance approval
6. **Chief Engineer**: Final approval authority

## File Organization

### Released Files
```
53-10_ASM_CENTER-BODY_v02_RevB.CATProduct
53-10_ASM_CENTER-BODY_v02_RevB_RELEASE-PACKAGE.zip
53-10_RELEASE-RECORD_v02_RevB.pdf
```

### Release Package Contents
- Assembly files (native and neutral formats)
- Component files (or references)
- Drawings (PDF)
- BOM (Excel/CSV)
- Release record (PDF)
- Change documentation (if applicable)

## Release Documentation

### Release Record
Each release must document:
- **Part number**: Unique identifier
- **Revision**: Version and revision letter
- **Date**: Release date
- **Description**: Assembly description
- **Changes**: What changed from previous revision
- **Reason**: Why revision was made
- **Approvals**: Signatures and dates
- **Effectivity**: When/where applicable
- **Related documents**: Drawings, ECOs, etc.

## Revision Numbering

### Convention
- **v01 Rev A**: First release
- **v01 Rev B**: Minor changes (corrections, clarifications)
- **v02 Rev A**: Major changes (design modifications)

### Examples
- `53-10_ASM_CENTER-BODY_v01_RevA.CATProduct` — First release
- `53-10_ASM_CENTER-BODY_v01_RevB.CATProduct` — Minor update
- `53-10_ASM_CENTER-BODY_v02_RevA.CATProduct` — Major redesign

## Change Control

### Engineering Change Orders (ECO)
- All changes require ECO
- ECO describes change and rationale
- Impact assessment performed
- Approvals documented

### Revision History
Maintain log with:
- Revision number
- Release date
- Description of changes
- ECO number
- Approver

## Archive and Retention

### Archive Requirements
- **Permanent retention**: All released designs
- **Backup**: Multiple locations
- **Format preservation**: Native + neutral formats
- **Documentation**: Complete release packages

### Access Control
- Read-only access to released files
- No modifications allowed
- Copy to draft for new changes

## Obsolescence

When superseded:
1. Move to [`../OBSOLETE/`](../OBSOLETE/)
2. Update status in PLM system
3. Document superseding revision
4. Maintain for record

## Related Directories

- **Draft**: [`../DRAFT/`](../DRAFT/) — Work in progress
- **Obsolete**: [`../OBSOLETE/`](../OBSOLETE/) — Superseded designs
