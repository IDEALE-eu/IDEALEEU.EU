# OBSOLETE — Superseded Files

## Purpose

This directory contains **obsolete and superseded** STEP files that have been replaced by newer revisions but are retained for historical reference and audit trail.

## What to Store

- Superseded revisions
- Replaced configurations
- Obsolete designs
- Historical reference files
- Audit trail documentation

## Status and Usage

🗄️ **OBSOLETE STATUS**: Files in this directory are:
- Superseded by newer revisions
- NOT approved for new production
- Retained for historical reference only
- May be referenced for legacy spares or repairs
- Part of configuration audit trail

## Archival Process

When a new revision is released:
1. Previous revision moves from [**../RELEASED/**](../RELEASED/) to here
2. Retain superseded file for traceability
3. Update index with supersession information
4. Document superseding revision number

## File Naming

Preserve original naming with revision:
```
53-10_FRAME-F01_PN-12345_RevA_20250110.step  (superseded by RevB)
```

## Retention Policy

- Retain obsolete files indefinitely for audit trail
- Do not delete superseded files
- Keep full revision history
- Document reason for obsolescence

## When to Reference Obsolete Files

Use obsolete files only for:
- Historical research and lessons learned
- Legacy spare parts manufacturing
- Repair of existing hardware
- Audit and compliance reviews
- Root cause analysis

⚠️ **Do NOT use for new production**

## Related Directories

- [**../RELEASED/**](../RELEASED/) — Current approved files
- [**../DRAFT/**](../DRAFT/) — Work-in-progress files
- [**../../INDEX/**](../../INDEX/) — Revision history tracking
- [**../../QA/CHECKS/**](../../QA/CHECKS/) — Historical validation records

## Configuration Management

- Part of configuration audit trail
- Reference ECOs: `00-PROGRAM/CONFIG_MGMT/06-CHANGE_CONTROL/`
- Baseline history: `00-PROGRAM/CONFIG_MGMT/04-BASELINES/`
- Supersession tracking: `00-PROGRAM/CONFIG_MGMT/03-BOM_MGMT/`

## Supersession Documentation

For each obsolete file, document:
- Superseding file and revision
- ECO number authorizing change
- Date of obsolescence
- Reason for change

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- CM procedures: `00-PROGRAM/CONFIG_MGMT/`
