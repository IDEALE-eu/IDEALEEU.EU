# RELEASED — Approved Production Files

## Purpose

This directory contains **approved and released** STEP files that are configuration-controlled and authorized for production use.

## What to Store

- Approved production models
- Released assembly files
- Baseline configurations
- Files cleared for manufacturing
- Customer deliverables

## Status and Usage

✅ **RELEASED STATUS**: Files in this directory are:
- Approved for production use
- Configuration-controlled
- Subject to formal change management (ECO)
- Traceable to engineering documentation

## Release Criteria

Files must meet these requirements before release:
- [ ] Engineering review completed
- [ ] Design validation passed
- [ ] Quality checks completed ([**../../QA/CHECKS/**](../../QA/CHECKS/))
- [ ] ECO approved and documented
- [ ] File validated in target systems
- [ ] Metadata complete (part number, revision, date)

## File Naming

Must include release revision:
```
53-10_FRAME-F01_PN-12345_RevB_20250110.step
```

## Workflow

1. **Draft**: Initial file in [**../DRAFT/**](../DRAFT/)
2. **Review**: Engineering validation
3. **ECO approval**: Change control process
4. **Release**: File moves here with approved revision
5. **Superseded**: Previous revision moves to [**../OBSOLETE/**](../OBSOLETE/)

## Related Directories

- [**../DRAFT/**](../DRAFT/) — Work-in-progress files
- [**../OBSOLETE/**](../OBSOLETE/) — Superseded versions
- [**../../QA/CHECKS/**](../../QA/CHECKS/) — Quality validation records
- [**../../INDEX/**](../../INDEX/) — Release catalogs and BOMs

## Configuration Management

- All files are configuration-controlled
- Changes require ECO: `00-PROGRAM/CONFIG_MGMT/06-CHANGE_CONTROL/`
- Baseline tracking: `00-PROGRAM/CONFIG_MGMT/04-BASELINES/`
- Part number registry: `00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING/`

## Traceability

Each released file should link to:
- Engineering Change Order (ECO) number
- Design review documentation
- Quality inspection reports
- BOM or EBOM entry

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- CM procedures: `00-PROGRAM/CONFIG_MGMT/`
