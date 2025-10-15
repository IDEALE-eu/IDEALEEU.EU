# ACK — Supplier Acknowledgments and Feedback

## Purpose

This directory contains acknowledgment records, feedback, and responses from suppliers regarding IGES packages and geometry distributions.

## Content

Store files related to:
- **Receipt acknowledgments**: Supplier confirmation of package receipt
- **File feedback**: Supplier reports on file quality or issues
- **Import verification**: Confirmation files import correctly
- **Geometry questions**: Supplier questions or clarifications
- **Issue reports**: Problems identified by suppliers
- **Acceptance records**: Formal acceptance of geometry

## File Types

Common files in this directory:
- **Emails**: Supplier email confirmations (saved as .eml or .pdf)
- **Signed acknowledgments**: Signed receipt forms (PDF)
- **Issue reports**: Documented file issues or concerns
- **Screenshots**: Supplier screenshots showing geometry
- **Test imports**: Supplier test import files or reports

## File Naming Convention

```
<supplier-name>_ACK_<package-id>_<date>.<ext>
```

**Examples:**
- `SUPPLIER-A_ACK_PKG-001_20250112.pdf`
- `SUPPLIER-B_ISSUE_PKG-002_20250116.pdf`
- `SUPPLIER-C_VERIFICATION_PKG-003_20250118.pdf`

## Acknowledgment Process

1. **Package sent**: Distribute package to supplier
2. **Receipt deadline**: Request acknowledgment within X days (typically 3-5)
3. **Acknowledgment received**: Supplier confirms receipt
4. **Verification**: Supplier verifies files open correctly
5. **Issues reported**: Supplier reports any problems
6. **Resolution**: Address any issues promptly
7. **Archive**: Store acknowledgment records

## Tracking Acknowledgments

Maintain tracking log:
- Package ID and supplier
- Distribution date
- Expected acknowledgment date
- Actual acknowledgment date
- Status (Received, Pending, Issues)
- Follow-up actions required

## Issue Resolution

When supplier reports issues:
1. **Document issue**: Record problem description
2. **Investigate**: Reproduce and analyze issue
3. **Resolve**: Fix geometry or export settings
4. **Re-export**: Create corrected IGES files
5. **Redistribute**: Send corrected package
6. **Verify**: Confirm supplier can now import
7. **Archive**: Document resolution

## Related Directories

- **Parent**: [`../`](../) — All SUPPLIERS
- **Packages**: [`../PACKAGES/`](../PACKAGES/) — Distributed packages
- **Released**: [`../../REVISIONS/RELEASED/`](../../REVISIONS/RELEASED/) — Released geometry
- **QA**: [`../../QA/CHECKS/`](../../QA/CHECKS/) — Quality verification

## Best Practices

- Request timely acknowledgments (within 3-5 days)
- Follow up on missing acknowledgments
- Document all feedback and issues
- Respond promptly to supplier questions
- Track issue resolution
- Maintain communication records
- Archive all correspondence
- Use acknowledgments for quality metrics

## Acknowledgment Template

Provide suppliers with acknowledgment form:

```
SUPPLIER ACKNOWLEDGMENT FORM

Package ID: _______________
Supplier: _________________
Date Received: ___________

VERIFICATION CHECKLIST:
[ ] All files received
[ ] All files open successfully in CAD system
[ ] Geometry appears correct and complete
[ ] Drawings reviewed
[ ] Specifications reviewed
[ ] No issues identified

ISSUES (if any):
[Description of problems]

CONTACT INFORMATION:
Name: _________________
Email: ________________
Phone: ________________
Date: _________________

Please return this form within 3 business days.
```

## Common Issues

Track common supplier issues:
- **Import errors**: File won't open in supplier CAD system
- **Missing geometry**: Parts or features not imported
- **Scale problems**: Incorrect units or scale
- **File corruption**: Corrupted or damaged files
- **Missing files**: Expected files not in package
- **Drawing mismatches**: Geometry doesn't match drawings

## Quality Metrics

Use acknowledgments to track:
- Package receipt timeliness
- File quality and import success rate
- Issue frequency by supplier
- Resolution time for issues
- Supplier satisfaction
- Process improvement opportunities

## Communication Guidelines

When handling supplier feedback:
- Respond promptly (within 1 business day)
- Acknowledge receipt of feedback
- Provide status updates
- Set expectations for resolution
- Follow up after resolution
- Thank supplier for feedback
- Document lessons learned

## Archive Requirements

Retain acknowledgment records for:
- **Traceability**: Documentation of geometry distribution
- **Quality records**: Evidence of supplier verification
- **Issue tracking**: History of problems and resolutions
- **Audit trail**: Compliance and certification support
- **Metrics**: Performance tracking and improvement

Retention period: Project lifetime + regulatory requirements.
