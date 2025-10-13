# RELEASED — Released BOMs for Production

## Purpose

This directory contains approved and released Bills of Materials that are authorized for production, procurement, and operational use.

## Contents

Released BOMs include:
- Approved engineering BOMs (EBOM)
- Approved manufacturing BOMs (MBOM)
- As-designed configurations
- Active baseline configurations

## Status Criteria

A BOM is in RELEASED status when:
- Technical review is complete
- CCB approval obtained
- Configuration baseline established
- Authorized for production use

## File Management

### Naming Convention
```
53-10_BOM_<assembly-id>_<bom-type>_r<revision>_RELEASED.<ext>
```

Examples:
- `53-10_BOM_CENTER-BODY_EBOM_r002_RELEASED.csv`
- `53-10_BOM_FRAME-F05_MBOM_r003_RELEASED.xlsx`
- `53-10_BOM_WING-ATTACH_AS-BUILT_S001_r001_RELEASED.pdf`

### Configuration Control
- Released BOMs are read-only
- Changes require new revision
- Maintain full audit trail
- Track effectivity

## Usage

Released BOMs are used for:
- Material procurement
- Production planning
- Assembly operations
- Configuration management
- Quality assurance
- Maintenance documentation

## Change Management

### Modifying Released BOMs
1. Create new draft revision
2. Document change rationale
3. Conduct impact analysis
4. Obtain CCB approval
5. Release new revision
6. Update baseline

### Superseding BOMs
When a new revision is released:
- Previous revision moves to OBSOLETE/
- Update configuration index
- Notify affected parties
- Maintain traceability

## Baseline Tracking

Released BOMs should track:
- Release date and approval
- Effectivity (aircraft S/N, dates)
- Configuration baseline identifier
- Related engineering changes
- Supplier part numbers

## Quality Assurance

Released BOMs must:
- Pass all validation checks
- Be complete and accurate
- Include all required data
- Be synchronized with CAD models
- Reference correct specifications

## Related Directories

- **Draft**: [../DRAFT/](../DRAFT/) — BOMs under development
- **Obsolete**: [../OBSOLETE/](../OBSOLETE/) — Superseded BOMs
- **Index**: [../../INDEX/](../../INDEX/) — BOM catalog
