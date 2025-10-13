# DRAFT — Draft Revisions

## Purpose

This directory contains draft versions of the top-level assembly that are work-in-progress and not yet released.

## Draft Status

### Characteristics
- **Not released**: Not approved for production or formal use
- **Subject to change**: May undergo significant modifications
- **For development only**: Internal use during design development
- **No baseline**: Not configuration controlled

### Use Cases
- **Concept development**: Early design exploration
- **Design iterations**: Incremental improvements
- **Interface coordination**: Working with other teams
- **Pre-review**: Before formal design review

## Draft Management

### File Naming
```
53-10_ASM_CENTER-BODY_<version>-WIP.<ext>
53-10_ASM_CENTER-BODY_<version>-DRAFT.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_v03-WIP.CATProduct`
- `53-10_ASM_CENTER-BODY_v04-DRAFT.prt`

### Version Tracking
- Use incremental versions for iterations
- Document what is being explored/changed
- Keep notes on design decisions
- Track issues and open questions

## Working Files

### Organization
- Latest working version
- Recent iterations (keep last 3-5)
- Dated backups
- Alternative concepts

### Documentation
- Design notes and sketches
- Calculation worksheets
- Analysis results
- Review comments

## Transition to Released

### Before Release
- [ ] Design review completed
- [ ] All review comments addressed
- [ ] Validation checks passed
- [ ] Drawings updated
- [ ] BOM verified
- [ ] Approvals obtained

### Release Process
1. Finalize design
2. Complete validation
3. Obtain approvals
4. Copy to [`../RELEASED/`](../RELEASED/)
5. Update revision history
6. Notify stakeholders

## File Retention

### Keep
- Current working version
- Recent iterations (for rollback)
- Key milestone versions

### Archive or Delete
- Superseded iterations (after review)
- Test files and experiments
- Duplicate files

## Collaboration

### Team Access
- Shared draft folder for team
- Communication of changes
- Conflict resolution
- Merge strategies

### Naming for Collaboration
```
53-10_ASM_CENTER-BODY_v03-WIP-<initials>-<date>.<ext>
```

Example:
- `53-10_ASM_CENTER-BODY_v03-WIP-JDS-20240115.CATProduct`

## Related Directories

- **Released**: [`../RELEASED/`](../RELEASED/) — Approved designs
- **Obsolete**: [`../OBSOLETE/`](../OBSOLETE/) — Superseded designs
