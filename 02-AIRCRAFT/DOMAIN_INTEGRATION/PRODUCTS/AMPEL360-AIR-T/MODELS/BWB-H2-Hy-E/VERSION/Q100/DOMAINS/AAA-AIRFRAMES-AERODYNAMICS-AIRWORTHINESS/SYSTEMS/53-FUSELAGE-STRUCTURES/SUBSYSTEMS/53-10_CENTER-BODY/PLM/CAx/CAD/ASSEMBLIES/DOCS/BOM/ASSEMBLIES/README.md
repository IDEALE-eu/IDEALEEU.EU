# ASSEMBLIES — Assembly-Level BOMs

## Purpose

This directory contains Bills of Materials for assemblies and sub-assemblies within the 53-10 Center Body. Assembly BOMs include all components and sub-assemblies that make up a higher-level assembly.

## Contents

### Assembly BOM Types
- **Top-level Assembly BOM**: Complete center body assembly
- **Sub-assembly BOMs**: Frame sections, bulkheads, panels
- **Installation Assemblies**: Attachment and integration assemblies

### Assembly BOM Structure
- Assembly header information
- Component list with quantities
- Sub-assembly references
- Fastener and hardware lists
- Installation materials
- Assembly sequence notes

## File Naming Convention

```
53-10_ASSY_<assembly-id>_<bom-type>_v<version>.<ext>
```

Examples:
- `53-10_ASSY_CENTER-BODY_EBOM_v01.csv`
- `53-10_ASSY_FRAME-SECTION-F05_MBOM_v02.xlsx`
- `53-10_ASSY_BULKHEAD-BH02_AS-BUILT_v01.pdf`

## BOM Hierarchy

Assembly BOMs should maintain hierarchical relationships:
1. Top-level assembly
2. Major sub-assemblies
3. Minor sub-assemblies
4. Individual parts
5. Raw materials and consumables

## Usage

Assembly BOMs are used for:
- Production planning
- Material kitting
- Assembly sequencing
- Configuration management
- Change impact analysis

## Related Directories

- **Parts**: [../PARTS/](../PARTS/) — Individual part BOMs
- **Installation**: [../INSTALLATION/](../INSTALLATION/) — Installation-specific BOMs
- **Assembly Models**: [../../../../TOP_LEVEL/](../../../../TOP_LEVEL/) — CAD assembly models
