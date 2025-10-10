# PARTS — Component Parts

## Purpose

This directory contains individual component part models for 21-10 radiators and heat exchangers, including facesheets, cores, tubes, manifolds, fins, shims, and thermal interface materials (TIMs).

## Content

### Part Categories
- **Facesheets**: Top and bottom facesheets for radiator panels
- **Cores**: Honeycomb and other core structures
- **Tubes**: Fluid tubes, heat pipe tubes
- **Manifolds**: Inlet/outlet manifolds for LPHX and coldplates
- **Fins**: Heat rejection fins
- **Shims**: Alignment and gap-filling shims
- **TIMs**: Thermal interface materials and pads

### What to Store
- Parametric CAD part models (native CAD format)
- Part configurations and variants
- Material specifications
- Mass properties and PMI data
- Manufacturing features

## Naming Convention

```
21-10_PART_<type>_<description>__r<NN>__<status>.<ext>
```

Examples:
- `21-10_PART_FACESHEET_AL2024__r02__REL.prt`
- `21-10_PART_HONEYCOMB-CORE__r01__RVW.sldprt`
- `21-10_PART_MANIFOLD_INLET__r03__WIP.asm`

### Status Codes
- **WIP**: Work in progress
- **RVW**: In review
- **REL**: Released

## Modeling Standards

### Units
- Length: millimeters (mm)
- Mass: kilograms (kg)
- Angles: degrees (deg)

### Materials
- Assign materials from CAP material tables
- Apply material properties for accurate mass/CG calculation
- Document material specifications in part properties

### Tolerances
- Default: ISO 2768-mK unless otherwise stated
- GD&T per ISO 1101 for critical features
- Surface finish: Ra per drawing notes

### Surface Finish
- Specify Ra values in drawing notes
- Coating stack per CAP/coating specification
- Color code for PMI:
  - Structure: gray
  - Fluid: blue
  - TIM: orange
  - Coating: pink

## Design Requirements

### General Guidelines
- Follow datums per 06 datum reference system
- Design for mounting to 51 structural patterns
- Include ground/bond points per 51 standards
- Document hole classes and torque requirements

### Specific Requirements
- **Facesheets**: Maintain flatness tolerances for coldplate applications
- **Cores**: Specify cell size, density, and orientation
- **Tubes**: Document wall thickness, material, and pressure rating
- **Manifolds**: Port threads/sizes must match ICD specifications
- **Fins**: Optimize for thermal performance and mass
- **TIMs**: Specify thickness and thermal conductivity

## Interface Requirements

### Checklist
- [ ] Flatness requirements met (≤ 0.05 mm for coldplate interfaces)
- [ ] Port threads/sizes match ICD specifications
- [ ] Keep-out zones for harness/heaters (97/21-30) respected
- [ ] Ground/bond points included with proper hole classes
- [ ] Handling features for parts >15 kg

## Manufacturing Considerations

- Design for manufacturability (DFM)
- Include necessary tooling references
- Document special processes (bonding, welding, coating)
- Specify inspection requirements

## Export Requirements

For REL status parts:
- STEP AP242 export in `../exports_step/`
- PDF drawings in `../drawings/` with dimensions and GD&T
- DXF flat patterns in `../exports_dxf/` for sheet metal parts

## Related Directories

- **Assemblies**: [`../assemblies/`](../assemblies/) - Assembly models using these parts
- **Drawings**: [`../drawings/`](../drawings/) - Part drawings
- **Exports (STEP)**: [`../exports_step/`](../exports_step/) - Neutral format exports
- **Exports (DXF)**: [`../exports_dxf/`](../exports_dxf/) - Flat pattern exports
- **Fixtures/Tooling**: [`../fixtures_tooling/`](../fixtures_tooling/) - Manufacturing fixtures
- **EBOM**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md) - Engineering BOM links

---

**Last Updated**: 2025-10-10
