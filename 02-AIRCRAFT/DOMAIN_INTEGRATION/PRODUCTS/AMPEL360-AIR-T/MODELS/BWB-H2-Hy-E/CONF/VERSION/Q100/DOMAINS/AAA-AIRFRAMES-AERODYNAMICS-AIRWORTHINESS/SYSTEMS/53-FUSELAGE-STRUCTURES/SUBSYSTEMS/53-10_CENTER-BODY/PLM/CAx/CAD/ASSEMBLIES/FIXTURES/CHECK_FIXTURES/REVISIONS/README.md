# REVISIONS — Fixture Revision Control

## Purpose

This directory contains revision-controlled versions of check fixture designs, documentation, and programs.

## Contents

### Subdirectories
- **[DRAFT/](./DRAFT/)** — Work-in-progress, not yet released
- **[RELEASED/](./RELEASED/)** — Approved and released versions
- **[OBSOLETE/](./OBSOLETE/)** — Superseded or retired versions

## Revision Control Process

### Draft Phase
- Initial design and development
- Review and validation
- Testing and debugging
- Not for production use
- Iterative changes allowed

### Release Phase
- Engineering approval obtained
- Quality approval obtained
- Formal release to production
- Change control required for modifications
- Distributed to users

### Obsolete Phase
- Superseded by new revision
- Archived for reference
- Not for active use
- Historical record maintained
- Traceability preserved

## Revision Levels

### Revision Coding
- **Draft**: `D1`, `D2`, `D3`, etc.
- **Released**: `Rev A`, `Rev B`, `Rev C`, etc.
- **Obsolete**: Marked as "OBSOLETE - See Rev X"

### Revision Increments
- **Major changes**: New revision letter (A→B)
- **Minor changes**: Dash number (B-1, B-2)
- **Corrections**: Sub-dash (B-1-1)

## Revision Documentation

Each revision should include:
- **Revision number**: Identification
- **Date**: When released
- **Description**: What changed
- **Reason**: Why change was made
- **Approved by**: Engineering and quality signatures
- **Effectivity**: When change takes effect
- **Supersedes**: Previous revision(s)

## Change Control

### Change Request Process
1. Engineering Change Request (ECR) initiated
2. Impact assessment performed
3. Design changes made (draft)
4. Review and approval
5. Engineering Change Order (ECO) issued
6. New revision released
7. Previous revision obsoleted
8. Users notified

### Documentation Updates
When fixture is revised:
- CAD models updated
- Drawings revised
- Procedures updated
- CMM programs revised
- Training materials updated
- Change notice distributed

## Version Tracking

### Traceability Matrix
Link revisions to:
- Part numbers affected
- Inspection results
- Non-conformances
- ECR/ECO numbers
- Customer notifications

## Archival

### Draft Archival
- Retain for reference
- Show design evolution
- Support investigations
- Minimum 5 years

### Released Archival
- Active production use
- Readily accessible
- Protected from unauthorized changes
- Retained indefinitely

### Obsolete Archival
- Historical reference
- Support legacy parts
- Root cause investigations
- Minimum 20 years retention

## Related Directories

- **Models**: [`../MODELS/`](../MODELS/)
- **Drawings**: [`../DRAWINGS/`](../DRAWINGS/)
- **CMM programs**: [`../CMM/PROGRAMS/`](../CMM/PROGRAMS/)
