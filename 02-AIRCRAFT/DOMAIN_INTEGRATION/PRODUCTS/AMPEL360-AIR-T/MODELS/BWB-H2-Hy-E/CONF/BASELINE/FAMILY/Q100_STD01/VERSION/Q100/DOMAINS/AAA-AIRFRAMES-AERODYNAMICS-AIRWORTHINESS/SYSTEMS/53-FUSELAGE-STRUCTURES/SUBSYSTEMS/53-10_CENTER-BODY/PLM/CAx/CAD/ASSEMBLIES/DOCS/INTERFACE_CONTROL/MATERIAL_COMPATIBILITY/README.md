# MATERIAL_COMPATIBILITY — Material Compatibility and Selection

## Purpose

This directory contains material compatibility information, galvanic corrosion data, and material selection guidance for interface design.

## Content Types

### Material Compatibility Data
- Galvanic series charts
- Corrosion compatibility matrices
- Material pairing guidelines
- Environmental exposure limits
- Chemical compatibility

### Material Specifications
- Material standards and grades
- Physical properties
- Mechanical properties
- Environmental performance
- Approved materials lists

### Corrosion Prevention
- Isolation methods
- Protective coatings
- Sealants and barriers
- Cathodic protection
- Design guidelines

## File Formats

- `.pdf` — Compatibility charts and specifications
- `.csv` — Compatibility matrices
- `.xlsx` — Material selection tables
- `.json` — Machine-readable material database

## Material Compatibility Categories

### Galvanic Compatibility
- Anodic materials (more active)
- Cathodic materials (more noble)
- Potential differences
- Corrosion risk assessment
- Mitigation requirements

### Chemical Compatibility
- Hydraulic fluids
- Fuels (Jet-A, hydrogen)
- De-icing fluids
- Cleaning solvents
- Environmental exposure

### Thermal Compatibility
- Coefficient of thermal expansion (CTE) matching
- Temperature range compatibility
- Thermal cycling effects
- Heat resistance

## Galvanic Series (Seawater)

### Anodic (Active) End
- Magnesium alloys
- Zinc
- Aluminum alloys
- Cadmium
- Mild steel

### Intermediate
- Cast iron
- Stainless steel (active)
- Copper alloys
- Bronzes

### Cathodic (Noble) End
- Stainless steel (passive)
- Titanium
- Silver
- Gold
- Graphite/Carbon fiber

## Material Pairing Guidelines

### Acceptable Pairings
- **Aluminum to Aluminum**: Compatible
- **Steel to Steel**: Compatible
- **Titanium to Most Materials**: Generally compatible
- **Similar alloys**: Usually acceptable

### Caution Required
- **Aluminum to Steel**: Isolate or coat
- **Aluminum to Graphite**: Isolate required
- **Magnesium to Most Metals**: High corrosion risk

### Unacceptable Pairings (without isolation)
- **Magnesium to Steel**: Severe galvanic corrosion
- **Aluminum to Copper**: High corrosion potential
- **Bare Composites to Aluminum**: Galvanic corrosion

## Corrosion Prevention Methods

### Isolation Techniques
- Non-conductive gaskets
- Plastic bushings/washers
- Dielectric barriers
- Fabric barriers
- Coatings on both surfaces

### Protective Coatings
- **Anodizing**: Aluminum protection
- **Alodine/Chromate**: Conversion coating
- **Primers**: Epoxy, polyurethane
- **Paints**: Topcoat systems
- **Platings**: Cadmium, nickel, zinc

### Design Practices
- Avoid dissimilar metal contact
- Design for drainage
- Avoid crevices and gaps
- Provide ventilation
- Use sacrificial anodes if needed

## Material Selection Criteria

### Structural Requirements
- Strength-to-weight ratio
- Fatigue resistance
- Fracture toughness
- Stiffness

### Environmental Requirements
- Corrosion resistance
- Temperature range
- UV resistance
- Moisture resistance

### Manufacturing Requirements
- Formability
- Machinability
- Weldability
- Availability

### Cost and Availability
- Material cost
- Lead time
- Standard vs. special alloy
- Supply chain reliability

## Common Aerospace Materials

### Aluminum Alloys
- **2024**: High strength, good fatigue
- **7075**: Very high strength
- **6061**: Good corrosion resistance
- **5052**: Marine applications

### Steels
- **4130/4340**: High-strength structural steel
- **300 series SS**: Corrosion resistant
- **PH13-8Mo**: Precipitation hardening stainless

### Titanium Alloys
- **Ti-6Al-4V**: Most common aerospace titanium
- **Ti-6Al-2Sn-4Zr-2Mo**: High temperature
- **CP Titanium**: Corrosion critical areas

### Composites
- **CFRP**: Carbon fiber reinforced polymer
- **GFRP**: Glass fiber reinforced polymer
- **Aramid**: Impact resistance

## Documentation Requirements

Each material pairing should document:

### Compatibility Assessment
- Materials in contact
- Environmental conditions
- Galvanic potential difference
- Corrosion risk level
- Required mitigation

### Specification
- Material standards (e.g., AMS, ASTM)
- Heat treatment condition
- Surface finish
- Coating system

## Naming Convention

```
MAT_{location}_{type}_v{version}.{ext}
```

Examples:
- `MAT_WING-ATTACH_COMPATIBILITY_v001.xlsx`
- `MAT_INTERFACE_GALVANIC-CHART_v002.pdf`
- `MAT_FASTENER_SELECTION_v001.csv`

## Testing and Verification

### Laboratory Tests
- Salt spray testing (ASTM B117)
- Galvanic current measurement
- Exposure testing
- Accelerated aging

### Field Testing
- Environmental exposure
- Corrosion monitoring
- Inspection schedules

## Cross-References

- [Fasteners](../FASTENERS/)
- [Bonding and Grounding](../BONDING_GROUNDING/)
- [Sealants and Gaskets](../SEALANTS_GASKETS/)
- [Interface Control Documents](../ICD/)

## Standards

- **MIL-STD-889**: Dissimilar metals
- **ASTM G82**: Galvanic corrosion
- **AMS 2700**: Passivation of corrosion-resistant steels
- **MIL-DTL-5541**: Chemical conversion coatings on aluminum
- **SAE J1650**: Material compatibility with hydrogen
- **ASTM B117**: Salt spray (fog) testing
