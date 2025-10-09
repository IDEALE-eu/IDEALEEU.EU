# MTL-CIRCULARITY - Materials Circularity Integration View

## Overview

The Materials Circularity domain encompasses non-ATA-specific circular economy principles for aircraft materials:
- Material passports and composition tracking
- Life Cycle Assessment (LCA) and Life Cycle Costing (LCC)
- Reuse, repair, refurbish, and recycle strategies
- Reverse logistics and end-of-life management

## Circular Economy Framework

### 4R Strategy
1. **Reuse**: Direct reuse of components without modification
2. **Repair**: Fix components to restore original function
3. **Refurbish**: Upgrade components with improved parts/software
4. **Recycle**: Material recovery for new components

### Material Hierarchy
```
Design for Circularity
  ↓
Production (virgin + recycled materials)
  ↓
Use Phase (maintenance, upgrades)
  ↓
End of Service Life
  ↓
Assessment (reuse/repair/refurbish/recycle)
  ↓
Recovery → [Back to Production]
```

## Key Components

### Material Passport System
Digital records tracking:
- **Composition**: Material types, alloys, coatings
- **Provenance**: Supplier, batch, certification
- **Treatment**: Heat treatment, surface finishing
- **Joining**: Welding, riveting, bonding methods
- **Recyclability**: Separation ease, contamination risk

### LCA/LCC Models
- **Life Cycle Assessment**: Environmental impact (CO₂, energy, water)
- **Life Cycle Costing**: Total ownership cost (acquisition, operation, disposal)
- **Trade-offs**: Balance environmental vs. economic factors

## Key Interfaces

### ATA-25 Cabin Furnishings
- **Interior Materials**: Seats, panels, carpets, textiles
- **Design for Disassembly**: Snap-fit, modular design
- **Material Passports**: Composition of interior materials
- **Refurbishment**: 5-7 year cabin refresh cycle

### ATA-51 Structures (Primary)
- **Fuselage Frames**: Aluminum alloys (2xxx, 7xxx)
- **Longerons/Stringers**: Aluminum or composites
- **Bulkheads**: Aluminum or titanium
- **Recyclability**: 90%+ for aluminum, 30-50% for composites

### ATA-53 Fuselage (Secondary)
- **Skin Panels**: Aluminum or composite
- **Fairings**: Composites, thermoplastics
- **Doors/Windows**: Aluminum frames, polycarbonate
- **Recyclability**: High for metals, moderate for composites

### ATA-57 Wings
- **Wing Skins**: Aluminum or CFRP
- **Ribs/Spars**: Aluminum or CFRP
- **Leading Edge**: Aluminum or titanium
- **Recyclability**: Material-dependent (metal > composite)

### Supply Chain
- **Reverse Logistics**: Return of end-of-life components
- **Recycling Partners**: Material recovery facilities
- **Remanufacturers**: Component refurbishment vendors
- **Material Suppliers**: Closed-loop material supply

## Material Categories

### Metals
| Material | Primary Use | Recyclability | Recovery Rate |
|----------|-------------|---------------|---------------|
| Aluminum (2xxx) | Fuselage, wing skins | High | 90-95% |
| Aluminum (7xxx) | Structural frames | High | 90-95% |
| Titanium | Engine mounts, fittings | High | 80-90% |
| Stainless steel | Hydraulics, fuel systems | High | 85-95% |
| Copper/brass | EWIS, connectors | High | 95%+ |

### Composites
| Material | Primary Use | Recyclability | Recovery Rate |
|----------|-------------|---------------|---------------|
| CFRP (epoxy) | Wing, fuselage, empennage | Moderate | 30-50% |
| GFRP (epoxy) | Secondary structure, fairings | Moderate | 30-50% |
| Thermoplastic composites | Interior panels | High | 70-90% |
| Sandwich panels | Cabin panels, doors | Low | 20-40% |

### Other Materials
| Material | Primary Use | Recyclability | Recovery Rate |
|----------|-------------|---------------|---------------|
| Polycarbonate | Windows, displays | Moderate | 60-80% |
| Polyurethane | Seals, insulation | Low | 10-30% |
| Elastomers | Seals, dampers | Low | 10-30% |
| Adhesives | Bonding | Very Low | < 10% |

## Subsystems

### MTL-00 Material Passports
- Digital material composition records
- Blockchain or PLM-based tracking
- Supplier certification linkage
- See [SUBSYSTEMS/MTL-00_MATERIAL_PASSPORTS/](SUBSYSTEMS/MTL-00_MATERIAL_PASSPORTS/)

### MTL-10 LCA/LCC Models
- Environmental impact models (SimaPro, GaBi)
- Cost models (TCO, NPV)
- Trade-off analysis tools
- See [SUBSYSTEMS/MTL-10_LCA_LCC_MODELS/](SUBSYSTEMS/MTL-10_LCA_LCC_MODELS/)

### MTL-20 Reuse/Repair/Recycle
- Disassembly plans and instructions
- Reverse logistics processes
- Recycling partner network
- See [SUBSYSTEMS/MTL-20_REUSE_REPAIR_RECYCLE/](SUBSYSTEMS/MTL-20_REUSE_REPAIR_RECYCLE/)

## Performance Targets

| Metric | Target | Baseline | Notes |
|--------|--------|----------|-------|
| Material recyclability | > 80% by weight | 60% | Increase recycled content |
| Component reuse rate | > 30% | 10% | Focus on high-value items |
| Virgin material reduction | 25% by 2030 | 0% | Use recycled materials |
| LCA CO₂ reduction | 40% by 2030 | Baseline 2020 | Full lifecycle |

## Design for Circularity Principles

### Design Guidelines
1. **Material Selection**: Prefer recyclable materials (metals > composites)
2. **Mono-Materials**: Avoid mixed materials where possible
3. **Disassembly**: Design for easy separation (snap-fit, bolts > adhesives)
4. **Modularity**: Modular components for easier replacement
5. **Standardization**: Standard fasteners, connectors
6. **Identification**: Clear material labeling (ISO 11469, ISO 1043)

### Lifecycle Considerations
- **Production**: Use recycled materials where possible
- **Use**: Design for long life, easy maintenance
- **End-of-Life**: Plan for disassembly, recovery, recycling

## Integration with ATA Systems

### Circular Material Flow Examples
1. **Aluminum Skins (ATA-53)**:
   - End-of-life → Sort by alloy → Melt → New sheet → Aircraft parts
2. **Cabin Seats (ATA-25)**:
   - End-of-life → Disassemble → Refurbish frame → New upholstery → Reuse
3. **CFRP Wing Skins (ATA-57)**:
   - End-of-life → Shred → Pyrolysis → Recovered fibers → Non-structural use

## Digital Thread Links

- **MBSE Model**: [04-DIGITAL_THREAD/MBSE_BINDINGS.md](../../04-DIGITAL_THREAD/MBSE_BINDINGS.md)
- **Digital Twin**: [04-DIGITAL_THREAD/TWIN_ANCHORS.md](../../04-DIGITAL_THREAD/TWIN_ANCHORS.md)
- **Material Passports**: [04-DIGITAL_THREAD/DATA_CONTRACTS/](../../04-DIGITAL_THREAD/DATA_CONTRACTS/)

## Compliance

- **REACH**: Registration, Evaluation, Authorization of Chemicals
- **RoHS**: Restriction of Hazardous Substances
- **WEEE**: Waste Electrical and Electronic Equipment
- **ISO 14001**: Environmental Management Systems
- **ISO 14040/14044**: Life Cycle Assessment standards

## References

- Ellen MacArthur Foundation: Circular Economy Principles
- ISO 14067: Carbon footprint of products
- ISO 11469: Material identification marking
- [02-INTERFACES/INTERFACE_MATRIX.csv](../../02-INTERFACES/INTERFACE_MATRIX.csv)
- [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
