# STANDARD_PARTS — Catalog Standard Parts

## Purpose

This directory contains CAD part files for standard catalog parts used in the 53-10 Center Body subsystem. These are commercially available, off-the-shelf components that are not specific to the aircraft design but are procured from suppliers.

## Component Description

### Standard Part Categories
- **Bushings**: Plain and flanged bushings for bearing surfaces
- **Inserts**: Threaded inserts (Helicoil, Keensert, etc.)
- **Bearings**: Plain bearings, spherical bearings, roller bearings
- **Pins**: Clevis pins, cotter pins, roll pins
- **Grommets**: Wire harness grommets and edge protectors
- **Shims**: Adjustment shims and spacers
- **Retaining rings**: Snap rings, retaining rings
- **O-rings and seals**: Standard size O-rings and gaskets

## Naming Convention

```
53-10_STANDARD_<type>_<manufacturer-PN>_<size>.<ext>
```

Examples:
- `53-10_STANDARD_BUSHING_MS21250-4F.CATPart`
- `53-10_STANDARD_INSERT_HELICOIL-8-32.prt`
- `53-10_STANDARD_BEARING_NAS1523-6.sldprt`

## File Organization

Organize by:
- Component type
- Manufacturer or standard designation
- Size or specification

Consider subdirectories by type:
```
STANDARD_PARTS/
├─ BUSHINGS/
├─ INSERTS/
├─ BEARINGS/
├─ PINS/
└─ SEALS/
```

## Standard Parts Management

### Part Libraries
- Use manufacturer-provided CAD models when available
- Create simplified models for assembly performance
- Maintain library of commonly used standard parts
- Reference online supplier catalogs (McMaster-Carr, Grainger, etc.)

### Bill of Materials (BOM)
- Include manufacturer part number in BOM
- Reference supplier catalogs for procurement
- Specify material and finish requirements
- Note any special certifications required (aerospace grade)

## Design Considerations

### Selection Criteria
- **Availability**: Select readily available parts
- **Certification**: Ensure aerospace certification if required
- **Interchangeability**: Use standard sizes for ease of substitution
- **Cost**: Consider lifecycle costs including procurement and spares

### Material Specifications
- Aluminum alloys (2024, 6061, 7075)
- Stainless steel (300 series)
- Brass or bronze (for bushings)
- Various plastics (Teflon, nylon, Delrin)

## Procurement

### Specifications
Standard parts typically follow:
- **MS (Military Standard)**: Legacy military specifications
- **NAS (National Aerospace Standard)**: Current aerospace standards
- **AN (Army-Navy)**: Historical standards still in use
- **ASTM**: Material and testing standards
- **ISO**: International standards

### Supplier Management
- Maintain approved supplier list
- Verify material certifications
- Track shelf life for age-sensitive items (O-rings, adhesives)

## Cross-References

- **Fasteners**: [`../FASTENERS/`](../FASTENERS/) (related but separate category)
- **Part specifications**: Reference industry standards (MS, NAS, AN)
- **Material database**: [`../../../CAE/DATA/MATERIALS_DB/`](../../../CAE/DATA/MATERIALS_DB/)
- **Supplier data**: [`../../../CAI/SUPPLIER_DATA/`](../../../CAI/SUPPLIER_DATA/)

## Quality Requirements

Standard parts must meet:
- Aerospace material certifications (when required)
- Dimensional conformance to specification
- Supplier quality requirements per AS9100
- Traceability to manufacturer lot/batch
