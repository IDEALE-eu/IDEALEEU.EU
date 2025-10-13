# RELEASED — Released Production Models

## Purpose

This directory contains formally released, production-ready CAD models for the 53-10 Center Body that have completed all review, approval, and quality assurance processes. These models are baselined and ready for manufacturing.

## Criteria for Release

Models in this directory must have:
- Completed design reviews
- Obtained all required approvals
- Passed quality checks (interference, mass properties)
- Complete and accurate metadata
- Proper part numbers assigned
- Released status in PLM system
- Associated engineering drawings
- Manufacturing documentation

## Organization

Released models are organized by:
- **Release batch**: Group by release date/event
- **Configuration**: Baseline or variant designation
- **Part type**: Frames, stringers, skins, etc.

## Naming Convention

Released models follow strict naming:
```
53-10_<COMPONENT>_<PART-NUMBER>_REL-<DATE>_r<REVISION>.<ext>
```

Examples:
- `53-10_FRAME_FR-001_REL-20240115_r01.CATPart`
- `53-10_SKIN-PANEL_SP-AFT-003_REL-20240120_r02.prt`
- `53-10_ASSY_CENTER-BODY_REL-20240125_r01.CATProduct`

## Version Control

Released models are strictly controlled:
- **Immutable**: Released models are frozen
- **Revisions**: Changes create new revision (r02, r03, etc.)
- **Traceability**: Full change history maintained
- **Notifications**: Releases communicated to stakeholders
- **Archival**: Previous revisions archived, not deleted

## Change Process

To modify a released model:
1. Create Engineering Change Request (ECR)
2. Check out model from PLM system
3. Make changes in controlled workspace
4. Document changes in revision notes
5. Submit for review and approval
6. Update revision letter/number
7. Re-release with new revision

## Documentation Requirements

Each released model must have:
- Engineering drawing in [`../../DRAWINGS/`](../../DRAWINGS/)
- EBOM entry in [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)
- Metadata file with all required attributes
- Quality check reports in [`../CHECKS/`](../CHECKS/)
- Manufacturing specifications (if applicable)
- Material certifications (if required)

## Configuration Management

Released models are:
- Baselined in configuration management system
- Tracked for effectivity and applicability
- Linked to change requests and issues
- Part of formal configuration audits
- Included in configuration status accounting

## Access Control

Released models have restricted access:
- Read access for most users
- Write access only for authorized personnel
- Modification requires proper authorization
- Download tracked for traceability

## Quality Assurance

Released models are:
- Verified against requirements
- Validated through analysis or test
- Checked for compliance with standards
- Reviewed for manufacturability
- Approved by responsible engineer
- Certified for production use

## Integration

Released models integrate with:
- **PLM system**: Configuration and lifecycle management
- **ERP system**: Manufacturing and procurement
- **Drawing system**: Engineering documentation
- **Quality system**: Inspection and verification
- **Change management**: ECR/ECO process

## Archival

When superseded:
- Previous revision moved to archive
- Supersession relationship documented
- Archive maintained for historical reference
- Obsolete models eventually moved to [`../OBSOLETE/`](../OBSOLETE/)

## Related Documentation

- **WIP models**: [`../WIP/`](../WIP/)
- **Drawing package**: [`../../DRAWINGS/`](../../DRAWINGS/)
- **EBOM**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)
- **Change management**: [`../../../../../../../../00-PROGRAM/CONFIG_MGMT/`](../../../../../../../../00-PROGRAM/CONFIG_MGMT/)
- **Quality records**: [`../../../../../../../../00-PROGRAM/QUALITY/`](../../../../../../../../00-PROGRAM/QUALITY/)

## Certification

For critical parts, released models may require:
- DER (Designated Engineering Representative) approval
- Regulatory agency approval
- Customer approval
- Supplier qualification
