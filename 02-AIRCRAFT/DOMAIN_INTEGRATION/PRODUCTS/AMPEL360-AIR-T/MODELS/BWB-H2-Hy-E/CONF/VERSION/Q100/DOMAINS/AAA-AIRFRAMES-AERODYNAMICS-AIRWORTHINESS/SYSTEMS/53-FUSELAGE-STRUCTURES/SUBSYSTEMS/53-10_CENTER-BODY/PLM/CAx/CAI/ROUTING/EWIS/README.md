# EWIS — Electrical Wiring and Harness Routing

## Purpose

Detailed electrical wiring routing paths, support provisions, and installation specifications for all electrical harnesses passing through or terminating in the CENTER-BODY subsystem.

## Content Types

- **Harness Routing Drawings** — 3D wire routing paths
- **Wire Bundle Schedules** — Harness specifications and part numbers
- **Support Bracket Locations** — Clamp and tie-wrap positions
- **Separation Requirements** — Clearances from other systems

## File Formats

- `.pdf` — Wiring diagrams and installation procedures
- `.step` — 3D harness routing geometry
- `.csv` — Wire bundle schedules and support locations
- `.xlsx` — Separation compliance matrices

## Naming Convention

```
EWIS_{zone}_{harness_id}_{type}_v{version}.{ext}
```

Examples:
- `EWIS_fwd_H001_routing_path_v001.pdf`
- `EWIS_center_H015_support_schedule_v002.csv`
- `EWIS_aft_H020_separation_analysis_v001.xlsx`

## Cross-References

- [Parent: ROUTING](../README.md)
- [53_TO_92 Interface](../../INTERFACES/53_TO_92/README.md)
- [Bonding/Grounding](../../BONDING_GROUNDING/README.md)
- [Access Clearances](../../ACCESS_CLEARANCES/)
- [ATA-92 EWIS System](../../../../../../../EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION/SYSTEMS/92-EWIS/)

## EWIS Design Standards

Compliance with:
- **FAA SFAR 88** — EWIS regulations
- **AC 25.1701-1** — EWIS certification
- **FAR 25.1707-25.1713** — EWIS requirements
- **ATA Spec 100** — Wiring practices

## Harness Routing Requirements

### Physical Routing
- Minimum bend radius: 10× wire bundle diameter
- Support spacing: Maximum 610mm (24 inches)
- Vibration isolation at resonance points
- Slack provision: 25mm minimum at each end

### Separation Requirements
| From | Minimum Separation |
|------|-------------------|
| Hydraulic lines | 75mm (3 inches) |
| Fuel lines | 150mm (6 inches) |
| Hot surfaces (>65°C) | 75mm (3 inches) |
| Moving parts | 25mm + travel envelope |
| Oxygen lines | 150mm (6 inches) |

### Power/Signal Separation
- Power and signal cables: Separate bundles
- High-voltage (>50V): Shielded or separated
- Avionics cables: Shielded and segregated
- Critical flight control: Redundant routing

## Wire Bundle Categories

| Category | Voltage Range | Application | Shielding |
|----------|---------------|-------------|-----------|
| **High Power** | 115VAC, 28VDC | Main power distribution | No |
| **Low Power** | 5-28VDC | Equipment power | No |
| **Signal** | <5V | Sensors, data | Yes |
| **Avionics** | 5VDC | Computers, displays | Yes |
| **Critical** | Various | Flight controls | Yes + Redundant |

## Support Hardware

Standard support types:
- **MS21919 Clamps** — Cushioned wire bundle clamps
- **Tie-wraps** — Non-metallic, self-locking
- **Grommets** — Protective pass-through bushings
- **Conduit** — Protective tubing in harsh environments

## Installation Requirements

Critical installation steps:
1. **Route verification** — Check path before installation
2. **Support installation** — Install clamps before wiring
3. **Harness routing** — Follow approved path
4. **Securing** — Clamp at specified intervals
5. **Separation check** — Verify clearances
6. **Continuity check** — Electrical testing
7. **Documentation** — As-built records

## Validation Requirements

- Routing path accessibility verification
- Separation distance measurements
- Bonding resistance testing
- High-potential (Hi-Pot) testing
- Visual inspection (chafing, stress points)
- Vibration testing (if in high-vibration zone)

## Change Control

EWIS routing changes require:
- Electrical systems engineering review
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Separation analysis re-validation
- Re-testing (continuity, Hi-Pot)
- As-built drawing updates
- Update to [53_TO_92 Interface](../../INTERFACES/53_TO_92/README.md)

## Safety Critical

EWIS is **SAFETY CRITICAL**:
- All installations require inspector sign-off
- No field modifications without engineering approval
- Damaged wiring must be repaired per OEM procedures
- Inspection required after any maintenance in area
