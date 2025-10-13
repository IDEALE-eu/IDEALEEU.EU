# PARTS — Individual Component JT Files

## Purpose

This directory contains JT visualization files for individual parts and components of the center body structure. These files represent single components exported from CAD systems for visualization, review, and PLM integration.

## What to Store

- Individual part models exported as JT
- Component-level geometry
- Single part files (not assemblies)
- Part-specific PMI and annotations

## Subdirectories

- [`LOD_LOW/`](./LOD_LOW/) — Low level of detail parts (simplified geometry)
- [`LOD_MED/`](./LOD_MED/) — Medium level of detail parts (balanced)
- [`LOD_HIGH/`](./LOD_HIGH/) — High level of detail parts (full detail)
- [`PMI/`](./PMI/) — Parts with embedded Product Manufacturing Information

## Related Directories

- [`../ASSEMBLIES/`](../ASSEMBLIES/) — Assembly JT files
- [`../CONFIGURATIONS/`](../CONFIGURATIONS/) — Configuration variants
- [`../../MODELS/`](../../MODELS/) — Source CAD models
- [`../README.md`](../README.md) — JT format overview

## Best Practices

- Export parts at appropriate LOD for intended use
- Include PMI for manufacturing-critical parts
- Use consistent naming convention: `53-10_<component>_<part-number>_<revision>_<date>.jt`
- Validate files in JT2Go before committing
