# RELEASED — Released Parts

## Purpose

This directory contains CAD part files that have been formally released through the Engineering Change Order (ECO) process and are approved for manufacturing, procurement, and assembly. These parts represent the current production configuration.

## Usage

### Configuration Control
Parts in RELEASED/ are:
- **Approved**: Released via ECO/ECR process
- **Under configuration management**: Changes require formal change process
- **Authorized for use**: Manufacturing, procurement, and assembly
- **Baseline**: Current production standard

### Access Control
- **Read access**: All project personnel
- **Write access**: Configuration management only
- **Modification**: Requires ECO approval and CM authority

## File Organization

Organize released parts by:
- Component type (frames, stringers, skin panels, etc.)
- Part number sequence
- Revision level

Consider using subdirectories by component type if volume is high.

## Revision Management

### Revision Tracking
- Part file name includes revision: `_v01`, `_v02`, etc.
- Maintain previous revisions for traceability
- Document changes in ECO and commit messages

### Supersession
When a new revision supersedes an older revision:
1. Move old revision to [`../OBSOLETE/`](../OBSOLETE/)
2. Add reference to superseding revision in metadata
3. Update assemblies and drawings to reference new revision
4. Notify affected stakeholders

## Release Process

To release a part from WIP:
1. **Design complete**: All requirements met
2. **Review approved**: PDR/CDR sign-off obtained
3. **Drawing created**: Manufacturing drawing complete (if required)
4. **Metadata verified**: All properties and documentation complete
5. **ECO approved**: Formal release authorization
6. **Neutral export**: STEP file exported to [`../../EXPORTS/STEP/`](../../EXPORTS/STEP/)
7. **Move to RELEASED**: File moved from WIP to appropriate component directory

## Naming Convention

Use standard part naming with revision:
```
53-10_<component>_<part-number>_<description>_<revision>.<ext>
```

Examples:
- `53-10_FRAME_F01_FWD_v01.CATPart` (initial release)
- `53-10_FRAME_F01_FWD_v02.CATPart` (revision)

## Quality Assurance

Released parts must include:
- [ ] Complete metadata (part number, revision, material, mass)
- [ ] Engineering drawing (if required)
- [ ] Material specification
- [ ] Neutral format export (STEP)
- [ ] ECO reference number
- [ ] Approved signature/date

## Cross-References

- **Work in progress**: [`../WIP/`](../WIP/)
- **Obsolete parts**: [`../OBSOLETE/`](../OBSOLETE/)
- **Engineering drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)
- **Neutral exports**: [`../../EXPORTS/`](../../EXPORTS/)
- **EBOM**: [`../../../EBOM_LINKS.md`](../../../EBOM_LINKS.md)

## Change Management

To modify a released part:
1. Create ECR (Engineering Change Request) documenting need
2. If approved, create new WIP version in [`../WIP/`](../WIP/)
3. Implement design changes
4. Complete review and approval process
5. Create ECO for release
6. Move new revision to RELEASED/
7. Move superseded revision to [`../OBSOLETE/`](../OBSOLETE/)
