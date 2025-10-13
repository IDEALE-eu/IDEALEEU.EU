# BONDING_GROUNDING — Electrical Bonding and Grounding Provisions

## Purpose

Electrical bonding and grounding provisions for the CENTER-BODY subsystem, ensuring electrical continuity, lightning protection, and electromagnetic compatibility (EMC).

## Content Types

- **Bonding Strap Locations** — Electrical continuity provisions
- **Grounding Point Definitions** — Structure grounding provisions
- **Resistance Test Procedures** — Bonding verification methods
- **Lightning Protection Paths** — Current dissipation routes

## File Formats

- `.pdf` — Bonding/grounding diagrams and procedures
- `.step` — 3D bonding hardware geometry
- `.csv` — Bonding point schedules
- `.xlsx` — Resistance measurement matrices

## Naming Convention

```
Bonding_{zone}_{type}_{identifier}_v{version}.{ext}
```

Examples:
- `Bonding_fwd_strap_locations_v001.pdf`
- `Bonding_center_ground_studs_v002.csv`
- `Bonding_aft_resistance_test_v001.xlsx`

## Cross-References

- [Parent: CAI Root](../README.md)
- [EWIS Routing](../ROUTING/EWIS/README.md)
- [53_TO_92 Interface](../INTERFACES/53_TO_92/README.md)
- [Master Geometry](../MASTER_GEOMETRY/DATUMS/README.md)
- [ATA-92 EWIS](../../../../../../EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION/SYSTEMS/92-EWIS/)

## Bonding Requirements

### Electrical Continuity
All conductive structures and equipment must be bonded to provide:
- **Lightning protection** — Safe current paths to dissipate strikes
- **EMI/EMC** — Electromagnetic interference control
- **Fault protection** — Return paths for fault currents
- **Static discharge** — Prevention of static build-up

### Bonding Resistance Limits
Maximum bonding resistance (per MIL-B-5087):
- **Primary structure**: ≤2.5 mΩ
- **Secondary structure**: ≤5.0 mΩ
- **Equipment mounting**: ≤2.5 mΩ
- **Control surfaces**: ≤5.0 mΩ

## Bonding Methods

| Method | Application | Typical Resistance |
|--------|-------------|-------------------|
| **Direct metal contact** | Structural joints | <1 mΩ |
| **Bonding jumpers** | Across non-conductive | <2.5 mΩ |
| **Grounding studs** | Equipment grounding | <2.5 mΩ |
| **Bonding washers** | Fastener bonding | <5 mΩ |

## Bonding Strap Specifications

Standard bonding strap requirements:
- **Material**: Tinned copper braid or aluminum
- **Cross-section**: Minimum 6 AWG (13mm²)
- **Length**: As short as practical, maximum 300mm
- **Attachment**: Bolted or resistance-welded
- **Protection**: Corrosion-resistant finish

## Bonding Point Locations

Bonding required at:
- **Structural splices** — Every joint with non-conductive coatings
- **Panel attachments** — Every removable panel
- **Equipment mounts** — All rack and shelf attachments
- **Control surface hinges** — All movable control surfaces
- **Access doors** — All hinged or removable doors
- **Waveguide connections** — RF equipment bonding

## Grounding Stud Installation

Grounding stud specifications:
- **Thread size**: M6 to M10 typical
- **Material**: Stainless steel or cadmium-plated
- **Torque**: Per thread size specification
- **Identification**: Marked with grounding symbol
- **Accessibility**: No more than 5m from any equipment

## Lightning Protection

Lightning zones and bonding requirements:
- **Zone 1A** (Direct strike): Heavy bonding, continuous paths
- **Zone 1B** (Swept stroke): Standard bonding
- **Zone 2** (Indirect effects): EMI protection bonding
- **Zone 3** (Internal): Equipment bonding

Lightning current paths:
- Entry point → bonding network → exit point
- Multiple parallel paths for redundancy
- No high-resistance joints in primary paths

## Bonding Installation Schedule

```csv
bond_id,from_location,to_location,type,part_number,qty,resistance_max_mOhm,test_freq
BND-001,Fwd bulkhead,Skin panel,Jumper,M27500-6RC2T14,2,2.5,Annual
BND-002,Floor beam,Side frame,Direct contact,-,-,1.0,Annual
BND-003,Equipment rack,Structure,Stud,MS21042-6,4,2.5,Install only
```

## Validation Requirements

- Resistance measurement (4-wire Kelvin method)
- Visual inspection (corrosion, damage, security)
- Torque verification of bonding hardware
- Lightning strike test (if applicable)
- EMC testing (conducted and radiated)

## Installation Procedures

Critical installation steps:
1. **Surface preparation** — Remove paint, corrosion, contamination
2. **Hardware installation** — Bonding straps or studs
3. **Torque application** — Per specification
4. **Resistance measurement** — Verify <2.5 mΩ
5. **Surface protection** — Apply corrosion preventive
6. **Documentation** — Record resistance values
7. **Marking** — Apply grounding symbol stickers

## Testing Requirements

### Initial Installation Testing
- 100% of bonding joints measured
- Documentation of all resistance values
- Visual inspection and photography
- Sign-off by certified inspector

### Periodic Testing
- Annual resistance measurements (sample or 100%)
- Post-maintenance re-testing
- After lightning strike event
- After any structural modification

## Change Control

Bonding/grounding changes require:
- Electrical systems engineering review
- Lightning protection analysis update
- ECO via [CHANGE_CONTROL/ECO](../CHANGE_CONTROL/ECO/README.md)
- Re-testing after modification
- Update to bonding drawings
- Update to [53_TO_92 Interface](../INTERFACES/53_TO_92/README.md)

## Safety Critical

Bonding/grounding is **SAFETY CRITICAL**:
- All installations require inspector verification
- Degraded bonding is reportable airworthiness issue
- Lightning strike analysis must consider bonding paths
- EMC certification depends on proper bonding
