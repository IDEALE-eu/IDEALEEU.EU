# SEALANTS_GASKETS — Sealant and Gasket Specifications

## Purpose

This directory contains specifications for sealants, gaskets, and sealing systems used at interfaces to provide environmental protection, fuel sealing, and pressure sealing.

## Content Types

### Sealant Specifications
- Material specifications
- Application procedures
- Cure times and conditions
- Surface preparation requirements
- Thickness and fillet requirements

### Gasket Specifications
- Gasket materials and types
- Compression requirements
- Torque sequences
- Installation procedures
- Replacement intervals

### Sealing Systems
- Fuel seal assemblies
- Pressure seals
- Environmental seals
- Weather seals

## File Formats

- `.pdf` — Sealant/gasket specifications and procedures
- `.csv` — Sealant application schedules
- `.xlsx` — Material compatibility matrices
- `.dwg` / `.dxf` — Gasket profiles and dimensions

## Sealant Types

### Aerospace Sealants
- **Polysulfide** (e.g., PR-1440, PR-1422)
- **Polythioether** (Permapol)
- **Silicone** (RTV)
- **Polyurethane**
- **Epoxy-based**

### Application Areas
- Fuel tank sealing (Class A/B)
- Pressure sealing (Class C)
- Faying surface sealing
- Fillet sealing
- Corrosion protection

## Gasket Types

### Solid Gaskets
- Rubber gaskets (neoprene, silicone, EPDM)
- Cork gaskets
- Paper gaskets
- Composite gaskets

### Formed-in-Place Gaskets
- RTV silicone
- Anaerobic sealants
- Form-a-gasket compounds

### Specialized Gaskets
- Metal gaskets
- O-rings
- Custom-molded seals

## Documentation Requirements

Each sealant/gasket specification should include:

### Material Information
- Manufacturer and part number
- Material specification
- Shelf life and storage
- Handling precautions

### Application Requirements
- Surface preparation
- Primer requirements
- Application method
- Cure schedule
- Environmental conditions

### Performance Requirements
- Operating temperature range
- Pressure rating
- Chemical resistance
- Flexibility and elongation
- Adhesion requirements

## Naming Convention

```
SEAL_{interface}_{type}_v{version}.{ext}
```

Examples:
- `SEAL_WING-ATTACH_FUEL-TANK_v001.pdf`
- `SEAL_DOOR-FRAME_WEATHER_v002.csv`
- `SEAL_BULKHEAD_PRESSURE_v001.xlsx`

## Application Procedures

### Surface Preparation
1. Clean surfaces (solvent wipe)
2. Remove contamination
3. Abrade if required
4. Apply primer (if specified)
5. Allow primer to dry

### Sealant Application
1. Mix sealant (if two-part)
2. Apply within working time
3. Maintain proper thickness
4. Tool/smooth as required
5. Cure per specification

### Gasket Installation
1. Clean mating surfaces
2. Position gasket properly
3. Apply proper torque sequence
4. Verify compression
5. Check for leaks

## Sealant Classes (Aerospace)

- **Class A**: Fuel sealing, integral tanks
- **Class B**: Fuel sealing, non-integral tanks
- **Class C**: Pressure sealing (non-fuel)
- **Class D**: Aerodynamic smoothing

## Inspection and Testing

### Pre-Installation
- Material verification
- Shelf life check
- Mixing ratio verification

### Post-Installation
- Visual inspection
- Fillet dimensions
- Cure verification
- Leak testing (pressure test)

## Cross-References

- [Fasteners](../FASTENERS/)
- [Torque Specifications](../TORQUE_SPECS/)
- [Interface Control Documents](../ICD/)
- [Material Compatibility](../MATERIAL_COMPATIBILITY/)

## Standards

- **MIL-PRF-81733**: Sealant, fuel tank
- **MIL-S-8802**: Sealing compound, corrosion inhibitive
- **SAE-AMS-S-8802**: Sealant, integral fuel tanks
- **SAE AS5127/1**: Sealants, aerospace applications
- **ASTM F104**: Classification of elastomeric gaskets
