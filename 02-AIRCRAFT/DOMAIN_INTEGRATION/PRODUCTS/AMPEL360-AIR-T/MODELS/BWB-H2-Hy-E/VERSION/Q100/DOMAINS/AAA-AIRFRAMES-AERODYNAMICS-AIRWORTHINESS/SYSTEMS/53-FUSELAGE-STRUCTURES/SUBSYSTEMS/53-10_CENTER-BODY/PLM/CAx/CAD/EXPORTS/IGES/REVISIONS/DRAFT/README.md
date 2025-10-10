# DRAFT — Draft Revision IGES Files

## Purpose

This directory contains IGES export files in draft status — work-in-progress geometry not yet approved for release or manufacturing.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Work-in-progress**: Geometry under active development
- **Preliminary designs**: Early-stage design concepts
- **Design studies**: Alternative design explorations
- **Pre-release geometry**: Files awaiting approval
- **Iteration models**: Design iteration snapshots

## File Status

**Draft** status indicates:
- ❌ **Not approved**: Not reviewed or approved for release
- ❌ **Not for manufacturing**: Not to be used for production
- ❌ **Not for distribution**: Internal use only
- ⚠️ **Subject to change**: Geometry may change significantly
- ⚠️ **No configuration control**: Not under formal change control

## File Naming Convention

```
<subsystem>_<component>_<part-number>_DRAFT_<date>.igs
```

**Examples:**
- `53-10_FRAME-F01_PN-12345_DRAFT_20250110.igs`
- `53-10_PANEL_PN-12346_DRAFT_20250110.igs`

Include "DRAFT" in filename to clearly indicate status.

## Usage Guidelines

Draft IGES files should be used for:
- ✅ Internal design reviews
- ✅ Preliminary fit checks
- ✅ Concept evaluation
- ✅ Design iteration
- ✅ Early supplier engagement (with clear draft status)

Draft files should **NOT** be used for:
- ❌ Manufacturing or production
- ❌ Tooling design or fabrication
- ❌ Formal supplier quotes
- ❌ Certification submittals
- ❌ Final assembly

## Transition to Released

When draft files are ready for release:
1. Complete design review and approval
2. Assign formal revision letter (Rev A, Rev B, etc.)
3. Move or copy to [`../RELEASED/`](../RELEASED/) directory
4. Update file naming to remove "DRAFT" designation
5. Update configuration control records
6. Notify stakeholders of release

## Related Directories

- **Parent**: [`../`](../) — All REVISIONS
- **Released**: [`../RELEASED/`](../RELEASED/) — Approved and released files
- **Obsolete**: [`../OBSOLETE/`](../OBSOLETE/) — Superseded files
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD models

## Best Practices

- Clearly mark draft files with "DRAFT" watermark or designation
- Include date in filename for version tracking
- Document known issues or incomplete areas
- Limit distribution of draft files
- Track draft iterations if needed
- Communicate draft status clearly to recipients
- Remove draft files after release to avoid confusion

## Draft File Metadata

Document for each draft file:
- Date created
- Author/designer
- Purpose or design intent
- Known issues or limitations
- Expected timeline to release
- Review status

## Configuration Management

Draft files are typically:
- Not under formal ECR/ECO control
- Not tracked in PDM/PLM (or marked as "Draft")
- Subject to rapid iteration
- Used for internal collaboration only

Transition to formal configuration control upon release.

## Communication

When sharing draft IGES files:
- Clearly communicate draft status
- Include disclaimers about use restrictions
- Provide context and design intent
- Set expectations for changes
- Request feedback and input
- Document feedback received
