# REVISIONS — Drawing Revision Management

## Purpose

This directory organizes drawings by their revision status, providing a clear view of drawing maturity and release state.

## What to Store

Drawings organized by revision status provide configuration management and change control visibility.

### Revision-Organized Drawings
- Symbolic links or references to drawings from type directories
- Revision tracking indices
- Revision history logs
- Change documentation

## Subdirectories

- [`DRAFT/`](./DRAFT/) - Drawings in development, not yet released
- [`RELEASED/`](./RELEASED/) - Officially released drawings for production
- [`OBSOLETE/`](./OBSOLETE/) - Superseded or retired drawings

## Revision States

### DRAFT
- **Status**: Work in progress
- **Use**: Design development, review, and approval
- **Access**: Engineering team and stakeholders
- **Changes**: Informal, no change control required
- **Naming**: May include "DRAFT" or "PRELIMINARY" watermark

### RELEASED
- **Status**: Approved for use
- **Use**: Manufacturing, procurement, inspection
- **Access**: All authorized users
- **Changes**: Formal change control via ECO/ECN process
- **Configuration**: Under configuration management

### OBSOLETE
- **Status**: Superseded or retired
- **Use**: Reference only, not for new applications
- **Access**: Historical reference
- **Changes**: No changes allowed (archived)
- **Retention**: Maintained for traceability and historical record

## Revision Conventions

### Revision Letters
- **Pre-release**: -, DRAFT, A (Draft)
- **First release**: A or Rev A
- **Subsequent releases**: B, C, D, E, F, G, H, J, K, L, M, N, P, R, S, T, U, V, W, X, Y, Z
- **Omitted letters**: I, O, Q (to avoid confusion with numbers 1, 0)

### Revision Numbers
Some organizations use numbers instead of letters:
- **Pre-release**: 0 or DRAFT
- **First release**: 1
- **Subsequent releases**: 2, 3, 4, 5, ...

## Revision History

### Revision Block Content
Each drawing must have a revision block showing:
- **Revision**: Letter or number
- **Description**: Brief description of changes
- **Date**: Date of revision
- **Approved by**: Engineer or manager approval
- **ECO/ECN**: Engineering Change Order/Notice reference

### Example Revision Block
```
REV | DESCRIPTION           | DATE       | APPROVED BY | ECO
----|----------------------|------------|-------------|-------
-   | Initial Release      | 2025-01-10 | J. Smith    | -
A   | Updated dimensions   | 2025-02-15 | J. Smith    | ECO-123
B   | Material change      | 2025-03-20 | M. Johnson  | ECO-145
```

## Organization Methods

### Option 1: Symbolic Links (Recommended)
Use symbolic links to reference drawings in type directories:
```bash
ln -s ../../PART/53-10_DWG_PART_FRAME-F01_D0001_SH1_RevA.pdf RELEASED/
ln -s ../../PART/53-10_DWG_PART_FRAME-F01_D0001_SH1_DRAFT.pdf DRAFT/
```

### Option 2: Revision Index Files
Create index files that list drawings by revision status:
- `DRAFT/DRAFT_INDEX.md` - List of all draft drawings
- `RELEASED/RELEASED_INDEX.md` - List of all released drawings
- `OBSOLETE/OBSOLETE_INDEX.md` - List of obsolete drawings

### Option 3: Physical Copies
Store actual drawing files organized by revision state (if not using links)

## Revision Workflow

### Typical Drawing Lifecycle
1. **Create**: New drawing created in DRAFT/
2. **Review**: Internal review and iterations (remains in DRAFT/)
3. **Approve**: Drawing approved, moved to RELEASED/
4. **Change**: Engineering change initiated (new revision created)
5. **Update**: New revision released, old revision moved to OBSOLETE/
6. **Archive**: Long-term archival of all revisions

### Change Control Process
1. **Initiate change**: ECR (Engineering Change Request)
2. **Review impact**: Assess impact of proposed change
3. **Approve change**: CCB (Configuration Control Board) approval
4. **Implement**: Create new revision with changes
5. **Release**: New revision released, supersedes previous
6. **Notify**: Notify affected parties of change

## Best Practices

### Revision Management
- Use clear revision letter/number scheme
- Document all changes in revision block
- Link revisions to ECO/ECN numbers
- Maintain complete revision history
- Archive superseded revisions
- Track drawing status rigorously

### Configuration Control
- All released drawings under configuration control
- Changes require CCB approval
- Track effectivity of changes
- Maintain traceability
- Document configuration baselines
- Support audits and reviews

### Drawing Status Indicators
- Use watermarks for DRAFT drawings
- Include release date on released drawings
- Mark OBSOLETE drawings clearly
- Reference superseding drawing on obsolete drawings
- Maintain "latest revision" indices

## Quality Requirements

### Revision Control Checklist
- [ ] Revision letter/number assigned
- [ ] Revision block updated
- [ ] Changes documented clearly
- [ ] ECO/ECN referenced
- [ ] Approvals obtained
- [ ] Previous revision obsoleted
- [ ] Affected parties notified
- [ ] Configuration management updated

## Related Directories

- **Type organization**: [`../PART/`](../PART/), [`../ASSEMBLY/`](../ASSEMBLY/), etc.
- **Zone organization**: [`../ZONES/`](../ZONES/)
- **Index**: [`../INDEX/`](../INDEX/) - Master drawing index with revision tracking

## References

- **Parent README**: [`../README.md`](../README.md) - General drawing standards
- **DRAFT**: [`./DRAFT/README.md`](./DRAFT/README.md) - Draft drawing management
- **RELEASED**: [`./RELEASED/README.md`](./RELEASED/README.md) - Released drawing management
- **OBSOLETE**: [`./OBSOLETE/README.md`](./OBSOLETE/README.md) - Obsolete drawing archival
- **Configuration Management**: `/00-PROGRAM/CONFIG_MGMT/` - CM standards and procedures
