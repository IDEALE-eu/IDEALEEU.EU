# METADATA — File Metadata and Properties

## Purpose

This directory contains metadata and property information for JT files. Supports enhanced file management, searchability, and PLM integration.

## What to Store

- File metadata catalogs
- Property definitions
- Attribute schemas
- BOM data extracts
- Mass properties data
- Custom attribute definitions

## Subdirectories

- [`PROPERTIES/`](./PROPERTIES/) — Standard properties (part number, revision, material, mass)
- [`ATTRIBUTES/`](./ATTRIBUTES/) — Custom attributes and extended data

## Metadata Categories

### Standard Properties
- Part number / Drawing number
- Revision / Version
- Material specification
- Mass properties
- Author / Organization
- Creation date / Modification date

### Custom Attributes
- Project-specific data
- PLM system attributes
- Classification codes
- Effectivity data
- Approval status
- Traceability information

## Usage

Use metadata for:
- Enhanced file searchability
- PLM system synchronization
- BOM generation and validation
- Configuration management
- Traceability and compliance
- Automated reporting

## File Formats

Metadata may be stored as:
- JSON/XML catalogs
- CSV property lists
- Database exports
- Embedded in JT files

## Related Directories

- [`../INDEX/`](../INDEX/) — File indexes and catalogs
- [`../ASSEMBLIES/`](../ASSEMBLIES/) — Assembly files
- [`../PARTS/`](../PARTS/) — Part files
- [`../README.md`](../README.md) — JT format overview

## Best Practices

- Keep metadata synchronized with JT files
- Use consistent property schemas
- Automate metadata extraction
- Validate completeness
- Document custom attributes
