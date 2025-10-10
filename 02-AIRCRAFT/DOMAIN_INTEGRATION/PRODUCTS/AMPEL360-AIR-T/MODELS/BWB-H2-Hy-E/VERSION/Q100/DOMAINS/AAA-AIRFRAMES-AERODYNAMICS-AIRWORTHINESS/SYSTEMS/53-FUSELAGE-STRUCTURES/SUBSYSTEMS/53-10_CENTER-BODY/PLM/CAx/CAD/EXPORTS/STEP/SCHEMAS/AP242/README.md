# AP242 — ISO 10303-242 (Primary Format)

## Purpose

This directory contains STEP files using the **ISO 10303-242 (AP242)** application protocol, which is the **primary and recommended format** for aerospace CAD data exchange.

## What to Store

All STEP exports should primarily use AP242 format:
- Parts, assemblies, and tooling
- Full PMI and GD&T data
- Product structure and metadata
- Configuration management information

## AP242 Advantages

✅ **Complete PMI support**: Semantic GD&T, not just visual annotations  
✅ **Rich metadata**: Material, mass, properties, lifecycle data  
✅ **Assembly structure**: Full product hierarchy with transformations  
✅ **Industry standard**: Required by major aerospace OEMs  
✅ **Long-term archival**: Designed for decades of preservation  

## Export Settings

### CATIA V5/V6
```
File → Export → STEP
Format: AP242
Options: ✅ Export PMI, ✅ Assembly structure, ✅ Attributes
```

### Siemens NX
```
File → Export → STEP
Application Protocol: AP242
Options: ✅ Export PMI, ✅ Product structure, ✅ Attributes
```

### SolidWorks
```
File → Save As → STEP
Options → Output as: STEP AP242
Include: Geometry + PMI
```

## File Organization

Files in this directory should follow the same organization as parent directories:
- Reference [**../../PARTS/**](../../PARTS/) for parts
- Reference [**../../ASSEMBLIES/**](../../ASSEMBLIES/) for assemblies
- Reference [**../../TOOLING/**](../../TOOLING/) for tooling

## Related Directories

- [**../AP214/**](../AP214/) — Legacy ISO 10303-214 format (compatibility only)
- [**../../PARTS/PMI/**](../../PARTS/PMI/) — PMI-focused files
- [**../../REVISIONS/**](../../REVISIONS/) — Version control
- [**../../QA/CHECKS/**](../../QA/CHECKS/) — Validation files

## Validation

Use these tools to validate AP242 files:
- CAx Implementor Forum (CAx-IF) Recommended Practices
- STEP file analyzers (Jotne EDM Model Checker, etc.)
- Target CAD system import verification

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- Standard: ISO 10303-242:2020
- Best practices: `00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`
