# ACK — Supplier Acknowledgments

## Purpose

Storage for supplier acknowledgments, confirmations, and feedback on distributed packages.

## What to Store

- Supplier acknowledgment receipts
- Package receipt confirmations
- Review feedback and comments
- Question/answer logs
- Deviation requests
- Compliance confirmations

## Acknowledgment Types

### Receipt Acknowledgments
- Package received confirmation
- Completeness verification
- File compatibility check
- Data review completion

### Technical Acknowledgments
- Design review feedback
- Manufacturing feasibility
- Tooling requirements
- Lead time estimates
- Cost estimates

### Compliance Acknowledgments
- Requirements acceptance
- Quality plan approval
- Specification confirmation
- Interface agreement

## File Organization

```
<supplier-name>_<part-number>_ACK_<date>/
├── receipt.pdf            # Receipt confirmation
├── review-comments.pdf    # Technical feedback
├── qa-plan.pdf           # Quality plan
└── correspondence/        # Q&A logs
```

## Usage

Use acknowledgments for:
- Tracking distribution
- Confirming receipt and review
- Capturing feedback
- Managing questions
- Documenting agreements
- Audit trail

## Related Directories

- [`../PACKAGES/`](../PACKAGES/) — Distributed packages
- [`../`](../) — SUPPLIERS directory
- [`../../QA/CHECKS/`](../../QA/CHECKS/) — Quality validation
- [`../../README.md`](../../README.md) — JT format overview

## Best Practices

- Request formal acknowledgments
- Track response times
- Archive all correspondence
- Resolve questions promptly
- Document agreements in writing
- Maintain audit trail
