# PROPERTIES — Standard Properties

## Purpose

Storage for standard properties and metadata extracted from JT files. These are the common, well-defined properties used across all CAD and PLM systems.

## What to Store

- Part numbers and identifiers
- Revision and version information
- Material specifications
- Mass properties
- Author and organization data
- Timestamps (creation, modification)
- File provenance information

## Standard Properties

### Identification
- Part Number
- Drawing Number
- Assembly Number
- Name/Title
- Description

### Version Control
- Revision (A, B, C, etc.)
- Version number
- Status (Draft, Released, Obsolete)
- Effectivity dates

### Physical Properties
- Material specification
- Material code
- Mass (calculated)
- Volume
- Surface area
- Center of gravity

### Administrative
- Author
- Company/Organization
- Creation date
- Last modified date
- Last modified by
- CAD system and version
- Export date and settings

## File Format

Properties typically stored as:
- JSON files (one per JT file or catalog)
- CSV spreadsheets (for batch exports)
- XML property lists

## Related Directories

- [`../ATTRIBUTES/`](../ATTRIBUTES/) — Custom attributes
- [`../`](../) — METADATA directory
- [`../../INDEX/`](../../INDEX/) — File indexes
- [`../../README.md`](../../README.md) — JT format overview

## Best Practices

- Extract properties automatically during export
- Keep synchronized with source CAD files
- Use for BOM generation
- Validate completeness before release
