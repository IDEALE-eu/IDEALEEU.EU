# OBSOLETE — Obsolete and Superseded IGES Files

## Purpose

This directory contains IGES export files that have been superseded by newer revisions and are no longer current but retained for historical reference and traceability.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Superseded revisions**: Previous revisions replaced by newer versions
- **Historical records**: Archive of design evolution
- **Obsolete designs**: Discontinued or replaced designs
- **Legacy files**: Files from previous configurations
- **Reference files**: Historical reference for change tracking

## File Status

**Obsolete** status indicates:
- ❌ **Superseded**: Replaced by newer revision
- ❌ **Not current**: No longer the active design
- ❌ **Not for manufacturing**: Should not be used for production
- ⚠️ **Historical only**: Retained for reference and records
- ✅ **Archived**: Preserved for traceability

## File Naming Convention

```
<subsystem>_<component>_<part-number>_<revision>_OBSOLETE_<date>.igs
```

**Examples:**
- `53-10_FRAME-F01_PN-12345_RevA_OBSOLETE_20250110.igs`
- `53-10_PANEL_PN-12346_RevA_OBSOLETE_20250110.igs`

Include "OBSOLETE" designation to clearly indicate superseded status.

## Usage Guidelines

Obsolete IGES files should be used for:
- ✅ Historical reference
- ✅ Change tracking and comparison
- ✅ Root cause analysis
- ✅ Design evolution documentation
- ✅ Audit trail and traceability

Obsolete files should **NOT** be used for:
- ❌ New manufacturing or production
- ❌ New tooling or fixtures
- ❌ Current supplier quotes
- ❌ New installations
- ❌ Active projects (use current revision)

## Obsolescence Process

Files become obsolete when:
1. New revision is released and approved
2. Previous revision is superseded
3. Design is discontinued or replaced
4. Configuration change is implemented
5. Part is redesigned or re-numbered

## Retention Requirements

Obsolete files must be retained for:
- **Traceability**: Link to delivered hardware
- **Configuration management**: Change history tracking
- **Regulatory compliance**: Certification record retention
- **Warranty support**: Support for fielded aircraft
- **Lessons learned**: Design evolution documentation

Retention period: Typically aircraft lifetime + regulatory requirement (often 50+ years for aerospace).

## Related Directories

- **Parent**: [`../`](../) — All REVISIONS
- **Draft**: [`../DRAFT/`](../DRAFT/) — Work-in-progress files
- **Released**: [`../RELEASED/`](../RELEASED/) — Current approved files
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD models

## Best Practices

- Move superseded files to OBSOLETE promptly after new release
- Maintain complete revision history
- Document reason for obsolescence
- Link to superseding revision
- Retain all metadata and documentation
- Clearly mark files as obsolete
- Restrict access to prevent inadvertent use
- Maintain archive integrity

## Obsolescence Documentation

For each obsolete file, retain:
- **Original part number and revision**: Identity of obsolete file
- **Superseding revision**: Current revision that replaced it
- **Obsolescence date**: Date file was superseded
- **ECR/ECO reference**: Engineering change that superseded it
- **Change description**: Reason for change
- **Affected units**: Serial numbers or aircraft using obsolete revision
- **Configuration**: Which configurations used this revision

## As-Built Configuration

Obsolete files are critical for:
- **As-built records**: Documenting delivered aircraft configuration
- **Serial number tracking**: Which aircraft have which revision
- **Retrofit analysis**: Planning modifications and upgrades
- **Service bulletins**: Supporting field changes
- **Warranty claims**: Investigating issues on fielded aircraft

## Access Control

Obsolete files should be:
- Read-only (no modifications)
- Clearly marked as obsolete
- Accessible for reference but not active use
- Protected from deletion
- Backed up for long-term retention
- Indexed for easy retrieval

## Comparison and Analysis

Obsolete files enable:
- **Change comparison**: Compare old vs. new revisions
- **Impact analysis**: Assess change effects
- **Root cause investigation**: Analyze design issues
- **Lessons learned**: Understand design evolution
- **Reverse engineering**: Reference historical designs

## Communication

When referencing obsolete files:
- Clearly state obsolete status
- Reference current revision
- Explain historical context
- Document why reviewing obsolete file
- Avoid confusion with current design
