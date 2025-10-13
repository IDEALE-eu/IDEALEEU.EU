# REVISIONS — Revision Management

## Purpose

This directory organizes JT files by revision status and lifecycle stage. Supports configuration management and version control.

## What to Store

- Files organized by revision status
- Design lifecycle stages
- Historical revisions
- Superseded versions

## Subdirectories

- [`DRAFT/`](./DRAFT/) — Work in progress, not released
- [`RELEASED/`](./RELEASED/) — Formally released versions
- [`OBSOLETE/`](./OBSOLETE/) — Superseded or retired versions

## Revision Lifecycle

### Draft
- Initial design iterations
- Work in progress
- Under development
- Not for production use

### Released
- Formally released designs
- Approved for use
- Configuration controlled
- Baseline versions

### Obsolete
- Superseded designs
- Retired versions
- Historical archive
- Reference only

## Usage

Use revision organization for:
- Configuration management
- Change control
- Version tracking
- Design history
- Compliance documentation
- Audit trail

## Related Directories

- [`../ASSEMBLIES/`](../ASSEMBLIES/) — Assembly files
- [`../PARTS/`](../PARTS/) — Part files
- [`../INDEX/`](../INDEX/) — File catalogs
- [`../README.md`](../README.md) — JT format overview

## Best Practices

- Move files between directories as status changes
- Maintain clear revision identification
- Document change rationale
- Preserve obsolete versions for reference
- Synchronize with PLM system status
- Use revision letters/numbers consistently
