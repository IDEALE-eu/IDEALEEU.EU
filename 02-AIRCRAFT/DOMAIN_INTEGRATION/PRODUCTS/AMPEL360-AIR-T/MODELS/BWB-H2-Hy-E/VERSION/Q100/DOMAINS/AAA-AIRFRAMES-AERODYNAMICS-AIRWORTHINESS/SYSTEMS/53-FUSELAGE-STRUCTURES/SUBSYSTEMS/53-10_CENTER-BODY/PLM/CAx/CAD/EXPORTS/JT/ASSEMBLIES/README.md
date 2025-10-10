# ASSEMBLIES — Assembly JT Files

## Purpose

This directory contains JT visualization files for assemblies and sub-assemblies of the center body structure. These files represent complete product structures with multiple components.

## What to Store

- Complete assembly structures
- Sub-assembly models
- Component hierarchies
- Assembly-level PMI
- Large assembly visualizations

## Subdirectories

- [`TOP_LEVEL/`](./TOP_LEVEL/) — Complete center body assembly
- [`SUB_ASSEMBLIES/`](./SUB_ASSEMBLIES/) — Sub-assemblies (frames, sections, etc.)
- [`LOD_LOW/`](./LOD_LOW/) — Low LOD assemblies (simplified)
- [`LOD_MED/`](./LOD_MED/) — Medium LOD assemblies (balanced)
- [`LOD_HIGH/`](./LOD_HIGH/) — High LOD assemblies (full detail)
- [`PMI/`](./PMI/) — Assemblies with embedded PMI/GD&T

## Related Directories

- [`../PARTS/`](../PARTS/) — Individual part JT files
- [`../CONFIGURATIONS/`](../CONFIGURATIONS/) — Configuration variants
- [`../../ASSEMBLIES/`](../../ASSEMBLIES/) — Source CAD assemblies
- [`../README.md`](../README.md) — JT format overview

## Assembly Structure

JT assemblies preserve:
- Component hierarchy
- Assembly relationships
- Part instances and positions
- Metadata and attributes
- BOM information

## Best Practices

- Maintain logical assembly hierarchy
- Use LOD variants for large assemblies
- Include assembly-level PMI where applicable
- Use consistent naming: `53-10_ASM_<name>_<revision>_<date>.jt`
- Validate structure in JT2Go before committing
