# PACKAGES — Supplier Distribution Packages

## Purpose

Complete packages prepared for distribution to suppliers. These are curated sets of JT files with supporting documentation.

## What to Store

- Complete supplier packages
- Manufacturing data sets
- Interface control packages
- Supplier-specific deliverables
- RFQ/RFP packages

## Package Contents

A typical supplier package includes:
- JT visualization files (parts and assemblies)
- STEP files for manufacturing (in parallel directory)
- PDF drawings and specifications
- Interface control documents
- Material specifications
- Quality requirements
- Delivery schedule

## Package Organization

```
<supplier-name>_<part-number>_<date>/
├── JT/                    # Visualization files
├── STEP/                  # Manufacturing files (reference)
├── PDF/                   # Drawings and docs
├── REQUIREMENTS/          # Specifications
└── README.txt             # Package contents
```

## Usage

Use packages for:
- RFQ (Request for Quotation)
- Manufacturing release
- Supplier onboarding
- Production authorization
- Change orders
- Quality audits

## Related Directories

- [`../ACK/`](../ACK/) — Supplier acknowledgments
- [`../`](../) — SUPPLIERS directory
- [`../../PARTS/PMI/`](../../PARTS/PMI/) — Parts with PMI
- [`../../REVISIONS/RELEASED/`](../../REVISIONS/RELEASED/) — Released files
- [`../../README.md`](../../README.md) — JT format overview

## Best Practices

- Include complete package documentation
- Version control entire package
- Track distribution date and recipients
- Include contact information
- Define deliverable requirements
- Document change procedures
