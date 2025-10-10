# REVISIONS — Design Revisions

## Purpose

This directory contains different revision states of the top-level assembly organized by release status.

## Revision Categories

### Revision States
- **[DRAFT/](./DRAFT/)** — Work in progress, not released
- **[RELEASED/](./RELEASED/)** — Approved and released designs
- **[OBSOLETE/](./OBSOLETE/)** — Superseded or retired designs

## Revision Control

### Version Numbering
- **Major versions**: Significant design changes (v1, v2, v3)
- **Minor versions**: Incremental improvements (v1.1, v1.2)
- **Revision letters**: Released drawings (Rev A, Rev B)

### Revision Process
1. **Draft**: Working design, subject to change
2. **Review**: Submitted for design review
3. **Approved**: Design review complete
4. **Released**: Formally released to production
5. **Obsolete**: Superseded by newer revision

## File Organization

### By Revision State
```
DRAFT/
  53-10_ASM_CENTER-BODY_v03-WIP.CATProduct
RELEASED/
  53-10_ASM_CENTER-BODY_v02_RevB.CATProduct
OBSOLETE/
  53-10_ASM_CENTER-BODY_v01_RevA.CATProduct
```

### Metadata Requirements
Each revision should document:
- **Revision identifier**: Version or revision letter
- **Date**: When revision was created/released
- **Author**: Who created the revision
- **Approver**: Who approved the release
- **Description**: Summary of changes
- **Reason**: Why revision was made
- **Effectivity**: Serial numbers or dates affected

## Revision History

Maintain revision log with:
- Revision number/letter
- Date
- Description of changes
- Approval status
- Related change orders

## Change Management

### Engineering Change Orders (ECO)
- Link revisions to ECOs
- Document change rationale
- Track impact to other systems
- Obtain required approvals

### Configuration Control
- Baselined configurations
- Controlled changes only
- Traceability to requirements
- Release authorization

## File Formats

- Native CAD files (revision-specific)
- `.pdf` — Revision documentation
- `.xlsx` — Revision history log
- `.txt` — Change descriptions

## Naming Convention

```
53-10_ASM_CENTER-BODY_<version>_<rev>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_v01_RevA.CATProduct` (released)
- `53-10_ASM_CENTER-BODY_v02_WIP.prt` (draft)
- `53-10_ASM_CENTER-BODY_v01_RevA_OBSOLETE.sldasm` (obsolete)

## Best Practices

- **Archive released versions**: Keep copies of all released designs
- **Document changes**: Clear description of what changed and why
- **Maintain history**: Don't delete old revisions
- **Use version control**: Git or PLM system for tracking
- **Tag releases**: Mark released versions in VCS

## Related Documents

- **Change orders**: Engineering change documentation
- **Release records**: Formal release approval
- **Drawings**: [`../DRAWINGS/`](../DRAWINGS/) — Drawing revisions
