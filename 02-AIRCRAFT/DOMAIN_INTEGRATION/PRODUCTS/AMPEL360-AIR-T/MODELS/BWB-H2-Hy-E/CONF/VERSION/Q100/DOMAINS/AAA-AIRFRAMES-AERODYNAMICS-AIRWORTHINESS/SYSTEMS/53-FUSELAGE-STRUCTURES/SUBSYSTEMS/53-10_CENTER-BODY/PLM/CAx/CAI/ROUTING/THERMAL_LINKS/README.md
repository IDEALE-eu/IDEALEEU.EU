# THERMAL_LINKS — Thermal Management System Routing

## Purpose

Routing paths for thermal management system components including cooling lines, heat pipes, insulation, and temperature control provisions for the CENTER-BODY subsystem.

## Content Types

- **Cooling Line Routing** — Liquid cooling system paths
- **Heat Pipe Installations** — Passive thermal transfer
- **Insulation Requirements** — Thermal barrier specifications
- **Temperature Sensor Locations** — Monitoring point definitions

## File Formats

- `.pdf` — Thermal system diagrams and procedures
- `.step` — 3D routing and insulation geometry
- `.csv` — Component and sensor schedules
- `.xlsx` — Thermal analysis results

## Naming Convention

```
Thermal_{system}_{component}_{type}_v{version}.{ext}
```

Examples:
- `Thermal_cooling_avionics_routing_v001.pdf`
- `Thermal_insulation_blanket_layout_v002.step`
- `Thermal_sensor_locations_v001.csv`

## Cross-References

- [Parent: ROUTING](../README.md)
- [EWIS Routing](../EWIS/README.md) — For cable thermal effects
- [ATA-21 Air Conditioning](../../INTERFACES/53_TO_21/README.md)
- [Access Clearances](../../ACCESS_CLEARANCES/)
- [Master Geometry](../../MASTER_GEOMETRY/REFERENCES/README.md)

## Thermal System Types

### Active Cooling Systems
- **Liquid Cooling Loops** — For high-power electronics
- **Forced Air Cooling** — For equipment bays
- **Refrigeration Systems** — For cryogenic applications (H2 tanks)

### Passive Thermal Management
- **Heat Pipes** — Passive heat transfer devices
- **Thermal Doubler Plates** — Heat spreading structures
- **Insulation Blankets** — Thermal barriers

## Temperature Requirements

Typical operating ranges:
- **Electronics bay**: -40°C to +55°C
- **Passenger cabin**: +18°C to +27°C
- **Equipment**: Per component specification
- **Cryogenic systems**: -253°C (H2 storage)
- **Hot zones**: Up to +150°C

## Cooling Line Specifications

| Type | Fluid | Flow Rate | Pressure | Application |
|------|-------|-----------|----------|-------------|
| **Avionics cooling** | PAO | 20-50 L/min | 5 bar | Electronics |
| **Equipment cooling** | Glycol/Water | 10-30 L/min | 3 bar | Equipment |
| **Cryogenic** | LH2, LN2 | Variable | 10 bar | Fuel systems |

## Routing Requirements

### Physical Routing
- Minimum bend radius: 5× line outer diameter
- Support spacing: Maximum 500mm
- Slope toward drain points: Minimum 1°
- Expansion loop provisions for temperature changes

### Thermal Considerations
- Insulation thickness per thermal analysis
- Vapor barriers for cryogenic lines
- Thermal breaks to prevent heat transfer
- Condensation drain provisions

### Separation Requirements
| From | Minimum Separation | Reason |
|------|-------------------|---------|
| Hot surfaces (>150°C) | 100mm + insulation | Prevent overheating |
| Cryogenic lines | 150mm | Prevent icing |
| Electrical wiring | 50mm | Thermal protection |

## Insulation Types

| Type | Temperature Range | Application | Material |
|------|------------------|-------------|----------|
| **Blanket** | -40°C to +260°C | General areas | Fiberglass/Silica |
| **Foam** | -40°C to +120°C | Equipment bays | Polyimide foam |
| **MLI** | -253°C to +150°C | Cryogenic | Multi-layer insulation |
| **Ceramic** | +150°C to +1000°C | Fire zones | Ceramic fiber |

## Heat Pipe Installations

Heat pipe specifications:
- **Diameter**: 6-25mm typical
- **Length**: Up to 2000mm
- **Orientation**: Optimized for gravity assistance
- **Thermal capacity**: 50-500W per pipe
- **Working fluid**: Ammonia, methanol, or water

## Temperature Sensor Locations

Critical monitoring points:
- Equipment bay temperatures (multiple zones)
- Cryogenic tank surface temperatures
- Hot zone boundaries
- Heat exchanger inlet/outlet
- Ambient reference points

## Validation Requirements

- Thermal analysis validation (CFD, FEA)
- Temperature measurements under all conditions
- Insulation effectiveness testing
- Heat pipe performance verification
- Condensation and icing tests
- Thermal cycling tests

## Installation Requirements

1. **Surface preparation** — Clean and dry mounting surfaces
2. **Insulation installation** — Secure with approved fasteners
3. **Line routing** — Verify clearances and support
4. **Sensor installation** — Calibrated and positioned correctly
5. **Leak testing** — For all fluid connections
6. **Functional testing** — Verify cooling performance
7. **Documentation** — Record as-built configuration

## Change Control

Thermal system changes require:
- Thermal engineering analysis and approval
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Re-validation of thermal performance
- Temperature monitoring during initial operation
- Update to thermal analysis documentation
