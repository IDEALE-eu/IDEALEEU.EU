# SUB_ASSEMBLIES — Component Sub-Assemblies

## Purpose

This directory contains **sub-assembly files** representing functional groups of components within the center body structure (e.g., frame assemblies, panel assemblies, bulkhead assemblies).

## What to Store

- **Frame assemblies**: Groups of frames with stiffeners
- **Panel assemblies**: Skin panels with doublers and reinforcements
- **Bulkhead assemblies**: Pressure bulkheads with frames
- **Equipment installations**: Racks, mounts, and brackets as assemblies
- **Functional groups**: Related components assembled together

## File Naming Convention

```
<subsystem>_<subassembly-name>_<part-number>_<revision>_<date>.step
```

Example:
```
53-10_SUBASM_FRAME-CLUSTER-FWD_PN-10100_RevA_20250110.step
```

## Sub-Assembly Guidelines

- Include 10-50 parts per sub-assembly (manageable size)
- Group by function, zone, or installation sequence
- Maintain clear parent-child relationships
- Use descriptive sub-assembly names

## Related Directories

- [**../TOP_LEVEL/**](../TOP_LEVEL/) — Complete master assemblies
- [**../../PARTS/**](../../PARTS/) — Individual component parts
- [**../../ZONES/**](../../ZONES/) — Zone-specific organization
- [**../../INDEX/**](../../INDEX/) — Sub-assembly catalogs

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
