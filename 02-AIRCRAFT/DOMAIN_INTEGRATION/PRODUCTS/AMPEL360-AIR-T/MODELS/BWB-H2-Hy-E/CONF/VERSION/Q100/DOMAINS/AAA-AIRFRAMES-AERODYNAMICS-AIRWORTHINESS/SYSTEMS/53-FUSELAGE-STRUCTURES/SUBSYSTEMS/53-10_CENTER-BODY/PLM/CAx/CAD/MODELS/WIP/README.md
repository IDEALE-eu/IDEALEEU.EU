# WIP — Work In Progress Models

## Purpose

This directory serves as a workspace for CAD models that are actively being developed and are not yet ready for formal review or release. It provides designers with a staging area for ongoing work.

## Usage

Store work-in-progress models here when they are:
- In early concept or layout phase
- Undergoing major redesign
- Being tested for feasibility
- Awaiting review or approval
- Incomplete or partially modeled
- Experimental or exploratory designs

## Organization

Organize WIP models by:
- **Designer**: Create personal subdirectories (optional)
- **Project**: Group related WIP items
- **Date**: Include creation date in filenames

## Naming Convention

Use descriptive names with WIP indicator:
```
WIP_<COMPONENT>_<DESCRIPTION>_<DESIGNER>_<DATE>.<ext>
```

Examples:
- `WIP_FRAME-FR012_REDESIGN_JD_20240115.CATPart`
- `WIP_SKIN-PANEL_CONCEPT-A_MS_20240120.prt`
- `WIP_DOOR-SURR_ALTERNATE_TK_20240125.sldprt`

## Lifecycle

Work-in-progress models should:
1. Start in WIP/ directory
2. Develop and iterate in place
3. Move to appropriate directory when ready (PARTS/, SUBCOMPONENTS/)
4. Be cleaned up or archived when complete

## Not for Production Use

**Important**: Models in WIP/ are:
- **Not reviewed** — Have not undergone formal review
- **Not approved** — Lack required approvals
- **Not released** — Not ready for production use
- **Not guaranteed** — May have errors or be incomplete
- **Not tracked** — Not part of formal configuration

## Cleanup Policy

WIP directory should be periodically cleaned:
- Move completed work to appropriate directories
- Archive abandoned concepts to OBSOLETE/
- Delete temporary test files
- Maintain reasonable directory size

## Collaboration

When sharing WIP models:
- Include clear status notes
- Document known issues
- Indicate level of completeness
- Provide contact information
- Use descriptive filenames

## Version Control

WIP models have relaxed version control:
- Frequent saves encouraged
- Informal versioning acceptable
- Minimal documentation required
- No formal approval needed
- Git commits optional but recommended

## Transition to Formal Status

Before moving models out of WIP/:
- [ ] Complete design intent
- [ ] Run quality checks (CHECKS/)
- [ ] Add proper metadata
- [ ] Follow naming conventions
- [ ] Create/update related documents
- [ ] Obtain required reviews
- [ ] Update configuration status

## Related Documentation

- **Released models**: [`../PARTS/`](../PARTS/), [`../SUBCOMPONENTS/`](../SUBCOMPONENTS/)
- **Quality checks**: [`../CHECKS/`](../CHECKS/)
- **Design rules**: [`../CONFIG/DESIGN_RULES/`](../CONFIG/DESIGN_RULES/)
- **Templates**: [`../TEMPLATES/`](../TEMPLATES/)
- **Obsolete models**: [`../OBSOLETE/`](../OBSOLETE/)

## Best Practices

While working in WIP/:
- Save frequently with descriptive names
- Document design decisions
- Note open issues and questions
- Keep backups of major iterations
- Clean up when complete
- Don't reference WIP models from released models
