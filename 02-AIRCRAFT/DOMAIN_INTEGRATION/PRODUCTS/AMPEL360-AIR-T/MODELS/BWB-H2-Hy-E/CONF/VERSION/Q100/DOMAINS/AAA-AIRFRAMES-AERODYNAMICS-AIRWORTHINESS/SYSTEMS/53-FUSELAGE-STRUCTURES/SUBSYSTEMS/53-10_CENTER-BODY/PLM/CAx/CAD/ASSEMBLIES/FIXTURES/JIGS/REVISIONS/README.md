# REVISIONS — Revision Control and Change Management

## Purpose

This directory manages revision control and change history for jig designs and documentation.

## Contents

### Subdirectories

- **[DRAFT/](./DRAFT/)** — Work-in-progress and draft versions
- **[RELEASED/](./RELEASED/)** — Released and approved versions
- **[OBSOLETE/](./OBSOLETE/)** — Superseded and obsolete versions

## Revision States

### Draft
- Work in progress
- Under development or review
- Not approved for production use
- Subject to change

### Released
- Design review complete
- Approved for production use
- Configuration controlled
- Change requires ECO/ECN

### Obsolete
- Superseded by newer version
- Retired from service
- Retained for reference only
- Not for new production

## Revision Control

### Revision Numbering
Typical scheme:
- **Draft**: v0.x (e.g., v0.1, v0.2)
- **Released**: v1.0, v2.0, etc.
- **Minor changes**: v1.1, v1.2, etc.

### Change Documentation
Each revision should include:
- Revision number
- Date of revision
- Description of changes
- Reason for change
- Approval signatures
- Affected documents/parts

## Change Process

### Engineering Change Order (ECO)
1. Identify need for change
2. Prepare ECO request
3. Engineering review and approval
4. Update affected documents
5. Release new revision
6. Notify affected parties
7. Implement change
8. Verify effectiveness

## Document Control

### Metadata
Each document should have:
- Title and document number
- Revision level
- Date of issue
- Author/originator
- Approver
- Distribution list

### File Naming
```
53-10_FIX_JIG_<name>_<rev>.<ext>
```
Example:
- `53-10_FIX_JIG_FRAME-ASSY_v1.2.pdf`

## Retention Policy

- **Draft**: Delete when obsolete
- **Released**: Retain current + 2 previous versions
- **Obsolete**: Retain per company policy (typically 7 years)

## Related Directories

- **All directories**: Revision control applies to all content
- **Reports**: [`../REPORTS/`](../REPORTS/)
