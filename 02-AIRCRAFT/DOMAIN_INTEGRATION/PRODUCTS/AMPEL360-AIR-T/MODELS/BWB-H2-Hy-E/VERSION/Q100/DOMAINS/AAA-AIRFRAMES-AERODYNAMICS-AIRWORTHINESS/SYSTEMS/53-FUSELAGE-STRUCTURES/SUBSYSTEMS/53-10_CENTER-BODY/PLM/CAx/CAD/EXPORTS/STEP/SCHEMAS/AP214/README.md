# AP214 — ISO 10303-214 (Legacy Format)

## Purpose

This directory contains STEP files using the **ISO 10303-214 (AP214)** application protocol. This is a **legacy format** maintained for compatibility with older systems and tools.

## What to Store

Use AP214 only when required for compatibility:
- Legacy system exports
- Tools that don't support AP242
- Historical archive files
- Third-party system compatibility

## AP214 Limitations

⚠️ **Limited PMI support**: Visual annotations only, not semantic GD&T  
⚠️ **Basic metadata**: Less rich than AP242  
⚠️ **Legacy format**: Being phased out in favor of AP242  

## When to Use AP214

- Target system doesn't support AP242
- Compatibility with older CAD versions (pre-2015)
- Specific customer requirements
- Historical data preservation

## Recommendation

**Prefer [**../AP242/**](../AP242/) for all new exports.** Only use AP214 when explicitly required for compatibility.

## Export Settings

### CATIA V5
```
File → Export → STEP
Format: AP214
Options: ✅ Geometry, ⚠️ PMI limited
```

### Siemens NX
```
File → Export → STEP
Application Protocol: AP214
Options: Basic geometry export
```

### SolidWorks
```
File → Save As → STEP
Options → Output as: STEP AP214
Note: Limited annotation support
```

## Migration Path

If you have AP214 files:
1. Re-export from native CAD using AP242
2. Store new AP242 version in [**../AP242/**](../AP242/)
3. Keep AP214 version here for reference if needed
4. Update references to point to AP242 version

## Related Directories

- [**../AP242/**](../AP242/) — Recommended primary format
- [**../../PARTS/**](../../PARTS/) — Part organization
- [**../../ASSEMBLIES/**](../../ASSEMBLIES/) — Assembly organization
- [**../../REVISIONS/OBSOLETE/**](../../REVISIONS/OBSOLETE/) — Superseded files

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- Standard: ISO 10303-214:2010
