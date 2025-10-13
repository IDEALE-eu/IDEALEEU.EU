# REVISIONS — Document and Design Revisions

## Purpose

This directory manages revisions and configuration control of test-related documentation, designs, and procedures throughout the development lifecycle.

## Directory Structure

### DRAFT/
Work-in-progress and draft documents:
- Initial test plans
- Draft procedures
- Preliminary designs
- Review copies
- Coordination drafts
- Unapproved changes

### RELEASED/
Approved and released documentation:
- Released test procedures
- Approved test plans
- Baseline configurations
- Signed-off designs
- Controlled documents
- Configuration-managed items

### OBSOLETE/
Superseded and obsolete documents:
- Previous revisions
- Obsolete procedures
- Retired configurations
- Historical reference
- Lessons learned archive
- Superseded designs

## Revision Control Process

### Draft Phase
1. Create initial document/design
2. Store in DRAFT/ directory
3. Conduct internal reviews
4. Incorporate comments
5. Prepare for formal review

### Review Phase
1. Distribute for formal review
2. Collect and adjudicate comments
3. Update document/design
4. Obtain approvals
5. Prepare for release

### Release Phase
1. Final approval signature
2. Assign revision identifier
3. Move to RELEASED/ directory
4. Distribute per distribution list
5. Update document register
6. Archive superseded version to OBSOLETE/

## Revision Identification

### Revision Numbering Scheme
- **Draft revisions**: `vX.Y-DRAFT` (e.g., v1.0-DRAFT, v1.1-DRAFT)
- **Released revisions**: `vX.Y` (e.g., v1.0, v2.0)
- **Minor changes**: Increment Y (v1.0 → v1.1)
- **Major changes**: Increment X (v1.9 → v2.0)

### Change Classification
- **Class I (Major)**: Requires full review and re-approval
  - Changes to test requirements
  - Major procedure changes
  - Design changes affecting safety
  - Changes to acceptance criteria

- **Class II (Minor)**: Limited review and approval
  - Editorial corrections
  - Clarifications
  - Format improvements
  - Non-technical updates

## Document Control

### Document Identification
Each document should have:
- Unique document number
- Revision identifier
- Issue date
- Author/originator
- Approval signatures
- Distribution list

### Change Documentation
All changes must include:
- Change request number (if applicable)
- Description of change
- Reason for change
- Impact assessment
- Review and approval
- Effectivity

### Configuration Baseline
Establish configuration baselines at key milestones:
- **Preliminary Baseline**: After preliminary design review
- **Critical Baseline**: After critical design review
- **As-Tested Baseline**: After test completion
- **Final Baseline**: After final report approval

## Traceability

Maintain traceability between:
- Requirements and test procedures
- Test procedures and test results
- Designs and test articles
- Changes and change requests
- Revisions and approval records

## Archive and Retention

### Retention Requirements
- **Released documents**: Retain for program life + 20 years
- **Draft documents**: Retain for 2 years after release
- **Obsolete documents**: Retain for 10 years after supersession

### Archive Location
- Primary: Local secure server
- Backup: Off-site archive
- Digital: PLM/document management system

## Related Directories

- **Templates**: [`../TEMPLATES/`](../TEMPLATES/)
- **Index**: [`../INDEX/`](../INDEX/)
- **Reports**: [`../REPORTS/`](../REPORTS/)
- **CAV configuration**: [`../../../CAV/CONFIG/`](../../../CAV/CONFIG/)
