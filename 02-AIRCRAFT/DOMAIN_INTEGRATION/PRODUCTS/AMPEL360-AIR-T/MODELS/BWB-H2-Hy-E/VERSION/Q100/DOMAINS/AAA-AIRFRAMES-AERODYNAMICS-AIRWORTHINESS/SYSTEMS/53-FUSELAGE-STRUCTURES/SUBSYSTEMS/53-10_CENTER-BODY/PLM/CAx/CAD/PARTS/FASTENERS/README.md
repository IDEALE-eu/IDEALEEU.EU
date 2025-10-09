# FASTENERS — Fastener and Connector Parts

## Purpose

This directory contains CAD part files for fasteners and mechanical connectors used to join components in the 53-10 Center Body subsystem. Includes both standard catalog fasteners and custom fasteners specific to this application.

## Component Description

### Fastener Types
- **Rivets**: Solid, blind, and Hi-Lok rivets for permanent joints
- **Bolts**: Aerospace-grade bolts (AN, NAS, MS standards)
- **Screws**: Machine screws, self-locking screws
- **Nuts**: Standard and self-locking nuts
- **Washers**: Flat, lock, and special washers
- **Clips**: Sheet metal clips and speed clips
- **Inserts**: Threaded inserts and bushings

### Standards
- **AN (Army-Navy)**: Historical US military standards
- **NAS (National Aerospace Standards)**: Current aerospace standards
- **MS (Military Standards)**: Military fastener specifications
- **ISO**: International Organization for Standardization
- **Custom**: Application-specific proprietary designs

## Naming Convention

```
53-10_FASTENER_<type>_<specification>_<size>.<ext>
```

Examples:
- `53-10_FASTENER_RIVET_AN426AD_D4-6.CATPart` (AN426AD rivet, 1/8" dia, 3/8" length)
- `53-10_FASTENER_BOLT_NAS6604_D6-20.prt` (NAS6604 bolt, 1/4" dia, 1.25" grip)
- `53-10_FASTENER_CLIP_CUSTOM_CLP-001.sldprt` (Custom clip design)

## File Organization

Organize by:
- Fastener type (rivets, bolts, screws, etc.)
- Standard designation (AN, NAS, MS, custom)
- Size range

Consider using subdirectories:
```
FASTENERS/
├─ RIVETS/
├─ BOLTS/
├─ SCREWS/
├─ NUTS_WASHERS/
└─ CUSTOM/
```

## Standard Parts Management

### Catalog vs. Custom
- **Catalog parts**: Reference manufacturer's CAD models where available
- **Custom fasteners**: Full detailed models for unique designs
- **Simplified models**: Use simplified geometry for assembly performance

### Part Libraries
- Reference standard fastener libraries from CAD system
- Maintain local library for project-specific or custom fasteners
- Link to fastener specifications and material certifications

## Design Considerations

### Material Specifications
- **Aluminum**: 2117-T4 (rivets), 2024-T4 (bolts) for aluminum structure
- **Steel**: Cadmium-plated or corrosion-resistant steel for high loads
- **Titanium**: Ti-6Al-4V for high strength-to-weight ratio
- **Stainless steel**: A286 or CRES for corrosion resistance

### Joint Design
- Select fastener type and size based on joint loads
- Account for bearing stress, shear strength, and pull-through
- Consider accessibility for installation and removal
- Plan for torque requirements and lockwiring

## Cross-References

- **Fastener schedules**: In assembly drawings [`../../DRAWINGS/`](../../DRAWINGS/)
- **Joint typologies**: Reference standards in `../../../51-STRUCTURES-GENERAL/`
- **Material specifications**: [`../../../CAE/DATA/MATERIALS_DB/`](../../../CAE/DATA/MATERIALS_DB/)
- **Installation procedures**: Manufacturing engineering documentation

## Quality Requirements

Fasteners must meet:
- Material certifications and traceability
- Dimensional conformance to specification
- Coating and finish requirements
- Lot control and shelf life tracking (for items with limited life)
