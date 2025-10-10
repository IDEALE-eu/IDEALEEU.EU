# REVISIONS — BOM Revision Management

## Purpose

This directory manages BOM revisions through their lifecycle states, tracking changes from initial draft through release to obsolescence.

## Directory Structure

```
REVISIONS/
├── DRAFT/      — Working BOMs under development
├── RELEASED/   — Approved and released BOMs
└── OBSOLETE/   — Superseded or retired BOMs
```

## Revision Workflow

### 1. DRAFT
- BOMs under development or review
- Work-in-progress changes
- Pending approval

### 2. RELEASED
- Approved BOMs for production use
- Current active configurations
- Baseline configurations

### 3. OBSOLETE
- Superseded BOMs
- Retired configurations
- Historical reference only

## Revision Control

### Revision Numbering
- Use sequential revision numbers (001, 002, 003...)
- Major changes increment revision number
- Document change rationale

### Change Documentation
Each revision should include:
- Revision number and date
- Change description
- Reason for change
- Approver information
- Effectivity

## File Naming Convention

Include revision status in filename:
```
53-10_BOM_<assembly-id>_<bom-type>_<revision>_<status>.<ext>
```

Examples:
- `53-10_BOM_CENTER-BODY_EBOM_r001_DRAFT.csv`
- `53-10_BOM_CENTER-BODY_EBOM_r002_RELEASED.csv`
- `53-10_BOM_CENTER-BODY_EBOM_r001_OBSOLETE.csv`

## Lifecycle Management

### Draft to Released
- Complete technical review
- Obtain CCB approval
- Move from DRAFT/ to RELEASED/
- Update configuration baseline

### Released to Obsolete
- Superseded by new revision
- Configuration no longer applicable
- Move from RELEASED/ to OBSOLETE/
- Maintain for historical reference

## Related Directories

- **Templates**: [../TEMPLATES/](../TEMPLATES/) — BOM templates
- **Checks**: [../CHECKS/](../CHECKS/) — Validation checklists
- **Index**: [../INDEX/](../INDEX/) — BOM catalog and index
