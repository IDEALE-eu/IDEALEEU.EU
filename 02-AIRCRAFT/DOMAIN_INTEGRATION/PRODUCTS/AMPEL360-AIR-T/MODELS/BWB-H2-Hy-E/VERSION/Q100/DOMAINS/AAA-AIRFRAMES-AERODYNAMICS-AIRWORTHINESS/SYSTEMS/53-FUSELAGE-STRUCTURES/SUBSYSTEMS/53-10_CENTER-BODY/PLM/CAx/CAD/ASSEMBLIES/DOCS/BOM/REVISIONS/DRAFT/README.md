# DRAFT — Draft BOMs Under Development

## Purpose

This directory contains BOMs that are under development, review, or modification. Draft BOMs are not approved for production use.

## Contents

Draft BOMs include:
- Initial BOM creation and development
- BOMs under engineering review
- BOMs with pending changes
- BOMs awaiting approval

## Status Criteria

A BOM is in DRAFT status when:
- Initial development is in progress
- Changes are being incorporated
- Technical review is underway
- Approval is pending

## File Management

### Naming Convention
```
53-10_BOM_<assembly-id>_<bom-type>_r<revision>_DRAFT.<ext>
```

Examples:
- `53-10_BOM_CENTER-BODY_EBOM_r003_DRAFT.csv`
- `53-10_BOM_FRAME-F05_MBOM_r001_DRAFT.xlsx`

### Best Practices
- Include revision number even in draft
- Document pending changes
- Track review comments
- Maintain version history

## Workflow

### Draft Creation
1. Create new BOM from template
2. Populate with component data
3. Save in DRAFT/ directory
4. Initiate review process

### Draft Review
1. Conduct technical review
2. Verify completeness and accuracy
3. Resolve comments and issues
4. Update BOM as needed

### Draft Approval
1. Complete final validation
2. Obtain CCB approval
3. Move to RELEASED/ directory
4. Update configuration baseline

## Quality Checks

Before moving to RELEASED:
- All part numbers validated
- Quantities verified
- Material specifications complete
- Mass properties calculated
- Supplier information confirmed

## Related Directories

- **Released**: [../RELEASED/](../RELEASED/) — Approved BOMs
- **Checks**: [../../CHECKS/](../../CHECKS/) — Validation checklists
- **Templates**: [../../TEMPLATES/](../../TEMPLATES/) — BOM templates
