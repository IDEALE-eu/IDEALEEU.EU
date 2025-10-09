# ASSEMBLIES — Assembly DXF Files

## Purpose
DXF files for assembly-level drawings and manufacturing documentation.

## Contents
- **[PANEL_STACKUPS/](PANEL_STACKUPS/)** — Panel stack-up and layup drawings
- **[DRILL_TEMPLATES/](DRILL_TEMPLATES/)** — Drilling templates and hole patterns

## Organization
Organize by:
- Assembly level (major, sub-assembly)
- Zone location (FWD, CTR, AFT)
- Manufacturing sequence
- Assembly number

## File Naming Convention
```
<assembly-number>_<description>_<revision>_<date>.dxf
```

Examples:
- `53-10-ASM01_CENTER-BODY-FWD_A_20250110.dxf`
- `53-10-ASM10_PANEL-STACKUP_B_20250110.dxf`

## Guidelines
- Show assembly interfaces clearly
- Include fastener locations and types
- Document assembly sequence when critical
- Reference individual part numbers
- Include tooling and fixture requirements

## Related Directories
- **[../PARTS/](../PARTS/)** — Individual part files
- **[../INSTALLATION/](../INSTALLATION/)** — Installation drawings
- **[../../ASSEMBLIES/](../../ASSEMBLIES/)** — Source 3D assemblies

## Best Practices
- Use assembly-level layers
- Clearly mark part boundaries
- Include fastener patterns
- Document critical interfaces
- Cross-reference to assembly instructions
