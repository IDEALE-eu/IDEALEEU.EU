# ASSEMBLIES — Top-Level Assembly Models

## Purpose

This directory contains top-level assembly models for 21-10 radiators and heat exchangers, including radiator panels, liquid plate heat exchangers (LPHX), and coldplates.

## Content

### Assembly Types
- **RAD-PANEL**: Radiator panel assemblies (port and starboard configurations)
- **RAD-HP-EMB**: Radiator panels with embedded heat pipes
- **LPHX**: Liquid plate heat exchangers for avionics cooling loops
- **COLDPLATE**: Coldplate assemblies with serpentine channels

### What to Store
- Parametric CAD assembly models (native CAD format)
- Assembly configurations and variants
- Subassembly references
- Interface definitions
- Mass properties and PMI data

## Naming Convention

```
21-10_ASSY_<type>_<variant>__r<NN>__<status>.<ext>
```

Examples:
- `21-10_ASSY_RAD-PANEL-L1__r03__RVW.step`
- `21-10_ASSY_LPHX-AV__r02__REL.prt`
- `21-10_ASSY_COLDPLATE__r01__WIP.asm`

### Status Codes
- **WIP**: Work in progress
- **RVW**: In review
- **REL**: Released

## Assembly Standards

### Units
- Length: millimeters (mm)
- Mass: kilograms (kg)
- Angles: degrees (deg)

### Coordinate System
- Follow 06 datums reference
- Align mounting interfaces to 51 structural patterns
- Maintain consistent orientation with spacecraft coordinate system

### Materials
- Apply material properties from CAP material tables
- Ensure mass and CG properties are accurate
- Document material specifications in assembly properties

### Tolerances
- Default: ISO 2768-mK unless otherwise stated
- GD&T per ISO 1101
- Critical interfaces: specify in drawings

## Interface Requirements

### Checklist
- [ ] Coldplate flatness ≤ 0.05 mm; TIM thickness documented
- [ ] Port threads/sizes match ICD specifications (LPHX inlet/outlet)
- [ ] Keep-out zones for harness/heaters (97/21-30) defined
- [ ] Ground/bond points per 51 standards with hole classes and torque notes
- [ ] Lift/handling features included if assembly mass >15 kg (STA-L MGSE)

## BOM Integration

- Assembly BOM tables must trace to EBOM structure
- Reference: `../../EBOM_LINKS.md`
- All subassemblies and parts must have valid part numbers

## Export Requirements

For REL status assemblies:
- STEP AP242 export in `../exports_step/`
- PDF drawings in `../drawings/` with sign-offs
- BOM tables matching EBOM structure

## Related Directories

- **Parts**: [`../parts/`](../parts/) - Component parts used in assemblies
- **Drawings**: [`../drawings/`](../drawings/) - Assembly drawings
- **Exports (STEP)**: [`../exports_step/`](../exports_step/) - Neutral format exports
- **EBOM**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md) - Engineering BOM links

---

**Last Updated**: 2025-10-10
