# REVISIONS — Revision Control

## Purpose
DXF files organized by revision status for configuration management.

## Contents
- **[DRAFT/](DRAFT/)** — Draft and work-in-progress DXF files
- **[RELEASED/](RELEASED/)** — Released and approved DXF files
- **[OBSOLETE/](OBSOLETE/)** — Obsolete and superseded DXF files

## Revision Workflow
```
DRAFT → RELEASED → OBSOLETE
```

**Progression**:
1. **Draft**: Initial creation and development
2. **Released**: Approved for manufacturing/use
3. **Obsolete**: Superseded by newer revision

## Revision Naming Convention
Files use revision letters or numbers:
```
<part>_<description>_<REV>_<date>.dxf
```

Examples:
- `53-10-FRM01_FRAME_A_20250110.dxf` (Released)
- `53-10-FRM01_FRAME_B_20250125.dxf` (New revision, supersedes A)
- `53-10-FRM01_FRAME_DRAFT_20250105.dxf` (Draft)

## Revision Letters
Standard progression:
- **DRAFT** or **WIP**: Work in progress
- **A**: First released revision
- **B, C, D...**: Subsequent revisions
- Engineering Change Orders (ECO) may drive revisions

## Revision Control Requirements
For each revision:
- Document changes from previous revision
- Maintain revision history
- Reference ECO or change order
- Update revision block in drawing
- Archive superseded revisions

## Related Directories
- **[../PARTS/](../PARTS/)** — Current part files (all revisions)
- **[../ASSEMBLIES/](../ASSEMBLIES/)** — Assembly files
- Main DXF directory contains latest released revisions

## Guidelines
- Always work in DRAFT until approved
- Move to RELEASED only after formal approval
- Move superseded revisions to OBSOLETE
- Keep revision history documentation
- Never delete obsolete files (archive them)

## Best Practices
- Clear revision change documentation
- Formal approval process for releases
- Traceability to configuration management
- Regular cleanup of old drafts
- Proper archival of obsolete revisions
