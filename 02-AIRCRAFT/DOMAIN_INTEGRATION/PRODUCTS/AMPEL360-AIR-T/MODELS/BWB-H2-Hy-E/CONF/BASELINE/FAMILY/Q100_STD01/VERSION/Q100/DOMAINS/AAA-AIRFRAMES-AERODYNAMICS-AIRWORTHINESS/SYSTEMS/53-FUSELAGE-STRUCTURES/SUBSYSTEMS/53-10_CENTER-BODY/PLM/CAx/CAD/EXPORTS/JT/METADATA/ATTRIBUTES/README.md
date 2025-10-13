# ATTRIBUTES — Custom Attributes

## Purpose

Storage for custom attributes and extended metadata for JT files. These are project-specific, domain-specific, or organization-specific attributes beyond standard properties.

## What to Store

- Project-specific attributes
- PLM system custom fields
- Classification and categorization
- Traceability information
- Compliance data
- Workflow status
- Business process attributes

## Custom Attribute Categories

### Project Attributes
- Project code
- Work package
- Cost center
- Schedule milestone
- Deliverable type

### Classification
- Commodity code
- Functional classification
- ATA chapter
- System hierarchy
- Make/buy designation

### Compliance & Traceability
- Certification basis
- Compliance status
- Requirement traceability
- Design authority
- Approval signatures

### PLM Integration
- PLM object ID
- Workflow state
- Change order number
- Baseline identifier
- Configuration context

### Business Process
- Ownership
- Responsibility matrix
- Access control
- Distribution list
- Notification rules

## File Format

Custom attributes stored as:
- JSON schema with values
- XML attribute files
- Custom PLM exports
- Database records

## Related Directories

- [`../PROPERTIES/`](../PROPERTIES/) — Standard properties
- [`../`](../) — METADATA directory
- [`../../INDEX/`](../../INDEX/) — File catalogs
- [`../../README.md`](../../README.md) — JT format overview

## Best Practices

- Document attribute schema
- Maintain consistent taxonomy
- Automate extraction where possible
- Validate against schema
- Synchronize with PLM system
