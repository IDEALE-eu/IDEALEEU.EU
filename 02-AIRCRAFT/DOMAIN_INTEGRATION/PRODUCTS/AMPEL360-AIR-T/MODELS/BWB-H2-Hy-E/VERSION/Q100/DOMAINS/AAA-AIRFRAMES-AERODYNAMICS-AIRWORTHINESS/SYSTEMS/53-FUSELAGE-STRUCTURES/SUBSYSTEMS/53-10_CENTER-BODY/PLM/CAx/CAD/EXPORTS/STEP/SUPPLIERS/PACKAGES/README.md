# PACKAGES — Supplier Data Packages

## Purpose

This directory contains **supplier data packages** including STEP files and documentation provided to or received from suppliers and subcontractors.

## What to Store

- Supplier-provided STEP files
- Make-to-print package exports
- Build-to-specification deliverables
- Supplier design proposals
- As-built documentation from suppliers

## Package Structure

Each supplier package should include:
- STEP geometry files
- Technical drawings (PDF)
- Material specifications
- Process requirements
- Inspection criteria
- Supporting documentation

## File Naming Convention

```
<subsystem>_SUPPLIER_<supplier-name>_<package-id>_<date>.step
```

Example:
```
53-10_SUPPLIER_ACME-AERO_PKG-001_20250110.step
```

## Package Management

- One subdirectory per supplier or major package
- Include package transmittal documentation
- Track package versions and revisions
- Coordinate with procurement team

## Related Directories

- [**../ACK/**](../ACK/) — Supplier acknowledgments and returns
- [**../../PARTS/**](../../PARTS/) — Parts for supplier manufacturing
- [**../../TOOLING/**](../../TOOLING/) — Supplier tooling requirements
- [**../../QA/CHECKS/**](../../QA/CHECKS/) — Supplier quality requirements

## Procurement Integration

- Reference RFQ/PO numbers
- Link to supplier agreements
- Track to procurement schedule
- Coordinate with: `00-PROGRAM/PROCUREMENT/`

## Quality Requirements

Each supplier package should reference:
- Quality standards and specifications
- Inspection requirements
- First article inspection (FAI) criteria
- Material certifications needed

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- Supplier management: `00-PROGRAM/PROCUREMENT/`
