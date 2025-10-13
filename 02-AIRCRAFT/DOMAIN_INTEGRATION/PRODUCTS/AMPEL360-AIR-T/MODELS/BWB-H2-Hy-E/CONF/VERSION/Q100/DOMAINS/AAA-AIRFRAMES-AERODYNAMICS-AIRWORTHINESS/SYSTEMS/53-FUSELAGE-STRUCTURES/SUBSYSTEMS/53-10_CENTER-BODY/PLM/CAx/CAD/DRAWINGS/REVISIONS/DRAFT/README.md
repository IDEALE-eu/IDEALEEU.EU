# DRAFT — Draft Drawings

## Purpose

This directory contains or references drawings that are in development and have not yet been officially released for production use.

## Scope

### Draft Drawing Status
- **Development**: Preliminary designs and work in progress
- **Review**: Drawings under internal review
- **Approval pending**: Drawings awaiting final approval
- **Not released**: Not yet approved for manufacturing or procurement

## What to Store

### Draft Drawing Types
- New drawings in initial development
- Drawings undergoing design iterations
- Drawings in formal review process
- Drawings pending approval signatures
- Pre-release drawing versions

## Organization

### File Naming
Draft drawings should include clear draft indicators:
```
53-10_DWG_PART_FRAME-F01_D0001_SH1_DRAFT.pdf
53-10_DWG_ASM_CENTER-BODY_D1000_SH1_PRELIMINARY.pdf
53-10_DWG_INST_WING-INTERFACE_D2000_SH1_DRAFT-RevA.pdf
```

### Watermarks
Draft drawings must include clear watermarks:
- **"DRAFT"** - Work in progress
- **"PRELIMINARY"** - For review only
- **"NOT FOR PRODUCTION"** - Not approved for manufacturing
- **"REVIEW COPY"** - For design review

## Draft Workflow

### Development Process
1. **Create**: Initial drawing creation from CAD model
2. **Develop**: Add dimensions, notes, and specifications
3. **Self-check**: Designer verifies completeness
4. **Internal review**: Team review for technical accuracy
5. **Revise**: Incorporate review comments
6. **Final check**: Verify readiness for release
7. **Submit for approval**: Submit to approving authority
8. **Release**: Upon approval, move to RELEASED/

### Review Cycles
- **Informal review**: Quick checks by peers
- **Formal review**: Scheduled design review meetings
- **Checker review**: Independent technical review
- **Management review**: Engineering management approval

## Access and Distribution

### Who Can Access
- Design engineers and drafters
- Design team members
- Review participants
- Stakeholders (with appropriate watermarks)

### Distribution Guidelines
- Draft drawings for internal use only
- Include "DRAFT" watermark on all distributions
- Not for manufacturing or procurement use
- Track distribution to manage review comments
- Collect and incorporate feedback

## Quality Requirements

### Draft Drawing Checklist
Before submitting for release:
- [ ] All views necessary for complete definition
- [ ] All dimensions shown and toleranced
- [ ] Material specifications complete
- [ ] Surface finish specified
- [ ] GD&T applied to critical features
- [ ] Title block complete (except approvals)
- [ ] Revision block prepared
- [ ] Drawing number assigned
- [ ] No model-to-drawing discrepancies
- [ ] Notes and callouts clear
- [ ] References to standards included
- [ ] Self-check completed

## Transition to Released

### Release Criteria
Drawing ready for release when:
- Design is complete and validated
- All review comments incorporated
- Self-check and peer review completed
- Checker approval obtained
- Engineering approval obtained
- Drawing meets all quality standards
- Configuration management notified

### Release Process
1. Remove "DRAFT" watermark
2. Assign initial revision letter (typically "A" or "-")
3. Complete approval signatures in title block
4. Enter into configuration management system
5. Move to RELEASED/ directory
6. Notify affected parties of release

## Best Practices

### During Development
- Update drawings frequently as design evolves
- Maintain design-drawing consistency
- Document design assumptions and TBDs
- Track review comments and dispositions
- Communicate status to stakeholders
- Plan for formal reviews

### Review Management
- Schedule reviews at appropriate milestones
- Distribute drawings in advance of reviews
- Document review comments systematically
- Track comment resolution
- Obtain sign-off on comment resolution
- Re-review if changes are significant

### Version Control
- Use Git to track drawing iterations
- Include meaningful commit messages
- Tag major milestones
- Branch for major design changes
- Merge when changes validated
- Maintain clean commit history

## Related Directories

- **Released**: [`../RELEASED/`](../RELEASED/) - Approved drawings
- **Obsolete**: [`../OBSOLETE/`](../OBSOLETE/) - Superseded drawings
- **Type directories**: [`../../PART/`](../../PART/), [`../../ASSEMBLY/`](../../ASSEMBLY/)
- **CAD models**: [`../../../MODELS/`](../../../MODELS/)

## References

- **Parent README**: [`../README.md`](../README.md) - Revision management
- **Drawing standards**: [`../../README.md`](../../README.md) - General drawing standards
- **Configuration Management**: `/00-PROGRAM/CONFIG_MGMT/` - CM procedures
