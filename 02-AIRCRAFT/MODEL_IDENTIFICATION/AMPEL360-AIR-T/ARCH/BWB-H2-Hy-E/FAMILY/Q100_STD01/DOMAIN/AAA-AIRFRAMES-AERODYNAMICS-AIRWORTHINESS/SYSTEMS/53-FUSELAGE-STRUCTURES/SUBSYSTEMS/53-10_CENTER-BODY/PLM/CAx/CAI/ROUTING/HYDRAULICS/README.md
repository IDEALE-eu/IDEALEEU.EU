# HYDRAULICS — Hydraulic Line Routing

## Purpose

Hydraulic system line routing paths, support provisions, and installation specifications for hydraulic lines passing through the CENTER-BODY subsystem.

## Content Types

- **Hydraulic Line Routing Drawings** — 3D routing paths
- **Line Specifications** — Tube/hose sizing and materials
- **Support and Clamp Locations** — Mounting provisions
- **Separation and Protection Requirements** — Safety clearances

## File Formats

- `.pdf` — Hydraulic routing diagrams and procedures
- `.step` — 3D line routing geometry
- `.csv` — Line schedules and support locations
- `.xlsx` — Pressure/flow specifications

## Naming Convention

```
Hydraulic_{system}_{line_id}_{type}_v{version}.{ext}
```

Examples:
- `Hydraulic_primary_L001_routing_v001.pdf`
- `Hydraulic_backup_L015_support_schedule_v002.csv`
- `Hydraulic_emergency_L020_flex_hose_v001.step`

## Cross-References

- [Parent: ROUTING](../README.md)
- [EWIS Routing](../EWIS/README.md) — For separation requirements
- [Access Clearances](../../ACCESS_CLEARANCES/)
- [Mounting Provisions](../../MOUNTING/)
- [ATA-29 Hydraulic Power](../../../../../../../MMM-MECHANICAL-MATERIAL-MODULES/SYSTEMS/29-HYDRAULIC-POWER/)

## Hydraulic System Specifications

Typical system pressures:
- **Primary system**: 207 bar (3000 psi)
- **Backup system**: 207 bar (3000 psi)
- **Emergency system**: 138 bar (2000 psi)
- **Test pressure**: 310 bar (4500 psi)

## Line Types and Applications

| Type | Pressure Rating | Application | Material |
|------|----------------|-------------|----------|
| **Rigid tube** | 310 bar | Main runs | Titanium, Steel |
| **Flexible hose** | 240 bar | Movement areas | Teflon/SS braid |
| **Quick disconnect** | 207 bar | Service points | Aluminum/Steel |

## Routing Requirements

### Physical Routing
- Minimum bend radius: 3× outside diameter (rigid), 6× OD (flexible)
- Support spacing: Max 600mm for rigid, 300mm for flexible
- Slope for drainage: Minimum 1° toward drain points
- Vibration isolation: Required at high-vibe locations

### Separation Requirements
| From | Minimum Separation |
|------|-------------------|
| Electrical wiring | 75mm (3 inches) |
| Hot surfaces | 100mm (4 inches) |
| Fuel lines | 50mm (2 inches) |
| Moving parts | 50mm + full travel |
| Oxygen lines | 100mm (4 inches) |

### Protection Requirements
- Abrasion guards at contact points
- Fire sleeves in fire zones
- Thermal insulation near hot surfaces
- Debris shields in contamination areas

## Support Hardware

Standard support types:
- **MS21919 Cushioned Clamps** — For rigid tubes
- **MS21919 Loop Clamps** — For flexible hoses
- **AN832 Tube Supports** — For long unsupported runs
- **Fire-resistant sleeves** — In designated fire zones

## Line Identification

Hydraulic lines must be marked:
- System designation (A, B, Emergency)
- Pressure rating
- Fluid type (MIL-PRF-83282 or equivalent)
- Flow direction arrows
- Color coding per system

## Installation Requirements

Critical installation steps:
1. **Pre-installation inspection** — Check for damage, contamination
2. **Support installation** — Install clamps before routing
3. **Line routing** — Follow approved path
4. **Fitting torque** — Per specification tables
5. **Leak check** — Pressure test per procedure
6. **Securing** — Clamp at specified intervals
7. **Safety wire** — Critical fittings per standard
8. **Documentation** — Record test results, torque values

## Validation Requirements

- Routing path verification (no interference)
- Separation distance measurements
- Pressure testing (1.5× operating pressure, 5 minutes)
- Leak testing (visual inspection under pressure)
- Flow testing (verify no restrictions)
- Proof load testing (fittings and supports)

## Contamination Control

Hydraulic systems require stringent cleanliness:
- Cap all open lines during installation
- Use filtered fluid only
- NAS 1638 cleanliness level 6 or better
- Flush system before final connection
- Sample and test fluid before operation

## Change Control

Hydraulic routing changes require:
- Hydraulic systems engineering review
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Pressure test after any modification
- Separation analysis re-validation
- System functional test
- Update to routing documentation

## Safety Critical

Hydraulic systems are **SAFETY CRITICAL**:
- All work requires qualified personnel
- Pressure must be relieved before disconnection
- Protective equipment required (goggles, gloves)
- System lockout/tagout procedures mandatory
- Leak-free operation required for flight release
