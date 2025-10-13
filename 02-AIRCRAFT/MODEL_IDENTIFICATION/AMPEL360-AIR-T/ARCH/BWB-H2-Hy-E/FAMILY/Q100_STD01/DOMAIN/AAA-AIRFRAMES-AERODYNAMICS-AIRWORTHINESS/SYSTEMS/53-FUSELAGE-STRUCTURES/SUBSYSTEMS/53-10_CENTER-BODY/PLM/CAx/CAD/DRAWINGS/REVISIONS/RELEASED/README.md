# RELEASED — Released Drawings

## Purpose

This directory contains or references drawings that have been officially released and approved for production, procurement, and inspection use.

## Scope

### Released Drawing Status
- **Approved**: Formally approved by authorized personnel
- **Configuration controlled**: Under formal change control
- **Production use**: Authorized for manufacturing and procurement
- **Current**: Latest approved revision

## What to Store

### Released Drawing Types
- All drawing types in released state:
  - Part drawings
  - Assembly drawings
  - Installation drawings
  - Detail drawings
  - Interface control drawings (ICDs)

## Organization

### File Naming
Released drawings include revision letter/number:
```
53-10_DWG_PART_FRAME-F01_D0001_SH1_RevA.pdf
53-10_DWG_ASM_CENTER-BODY_D1000_SH1_RevB.pdf
53-10_DWG_INST_WING-INTERFACE_D2000_SH1_RevA.pdf
```

### Revision Tracking
- Only current (latest) revision should be in active use
- Previous revisions move to OBSOLETE/ when superseded
- Maintain revision history in drawing revision block
- Link revisions to ECO/ECN documentation

## Released Status Requirements

### Approval Requirements
Released drawings must have:
- **Designer signature**: Original designer or drafter
- **Checker signature**: Independent technical reviewer
- **Engineering approval**: Chief engineer or designee
- **Configuration management**: Entry in CM system
- **Release date**: Official release date
- **Revision letter**: Assigned revision (typically starts at "A" or "-")

### Quality Requirements
Released drawings must meet all quality standards:
- Complete dimensional definition
- All materials specified
- Surface finish requirements defined
- GD&T applied correctly
- Title block complete with approvals
- Revision block initialized
- Drawing number unique in system
- PDF exported at correct scale
- No model-to-drawing discrepancies

## Access and Distribution

### Who Can Access
- Manufacturing and production teams
- Quality control and inspection
- Procurement and purchasing
- Suppliers and vendors (as authorized)
- Configuration management
- All authorized users

### Distribution
- Released drawings are official documents
- Distribute via controlled channels
- Track distribution to ensure latest revision used
- Notify users of revisions and changes
- Maintain distribution lists

## Change Control

### Change Process
Changes to released drawings require formal process:

1. **Change request**: ECR (Engineering Change Request) initiated
2. **Impact assessment**: Evaluate technical, cost, schedule impacts
3. **CCB review**: Configuration Control Board reviews and approves
4. **ECO issued**: Engineering Change Order authorizes change
5. **Drawing revised**: New revision created with changes
6. **Approval**: New revision approved following release process
7. **Release**: New revision released, supersedes previous
8. **Notification**: Affected parties notified of change

### Revision Management
- Each change creates new revision letter
- Previous revision moved to OBSOLETE/
- Revision block updated with change description
- ECO number referenced in revision block
- All changes documented and traceable

## Configuration Management

### CM Requirements
Released drawings are configuration items (CIs):
- Tracked in CM system or database
- Part of product baseline
- Subject to change control
- Included in configuration audits
- Maintained for product lifecycle

### Baseline Management
Released drawings form technical baseline:
- Included in baseline snapshots
- Tagged at milestone reviews
- Referenced in product structure
- Support certification and qualification
- Maintained for entire program

## Quality Assurance

### Released Drawing Checklist
Before release:
- [ ] Design complete and validated
- [ ] All review comments resolved
- [ ] Checker review completed
- [ ] Engineering approval obtained
- [ ] Drawing meets all quality standards
- [ ] Revision block initialized
- [ ] Drawing number assigned and unique
- [ ] CM system updated
- [ ] Distribution planned

### Ongoing Monitoring
- Periodic review for currency
- Track usage and feedback
- Identify issues requiring changes
- Monitor for obsolescence
- Support manufacturing questions
- Maintain drawing quality

## Best Practices

### Release Management
- Release drawings when design is stable
- Avoid premature releases
- Group related drawings for release
- Plan releases around manufacturing needs
- Communicate releases clearly
- Support transition to production

### Change Management
- Minimize changes after release
- Assess impact before approving changes
- Group related changes when possible
- Communicate changes to all users
- Verify changes don't break downstream processes
- Document rationale for changes

### Documentation
- Maintain complete revision history
- Link to related documents (ECOs, test reports, etc.)
- Document design intent and assumptions
- Provide manufacturing notes as needed
- Support questions and clarifications
- Maintain drawing quality over time

## Related Directories

- **Draft**: [`../DRAFT/`](../DRAFT/) - Drawings in development
- **Obsolete**: [`../OBSOLETE/`](../OBSOLETE/) - Superseded revisions
- **Type directories**: [`../../PART/`](../../PART/), [`../../ASSEMBLY/`](../../ASSEMBLY/)
- **CAD models**: [`../../../MODELS/`](../../../MODELS/)
- **Index**: [`../../INDEX/`](../../INDEX/) - Master drawing index

## References

- **Parent README**: [`../README.md`](../README.md) - Revision management
- **Drawing standards**: [`../../README.md`](../../README.md) - General drawing standards
- **Configuration Management**: `/00-PROGRAM/CONFIG_MGMT/` - CM standards and procedures
- **Change Control**: `/00-PROGRAM/CONFIG_MGMT/03-CHANGE_CONTROL/` - ECO/ECN procedures
