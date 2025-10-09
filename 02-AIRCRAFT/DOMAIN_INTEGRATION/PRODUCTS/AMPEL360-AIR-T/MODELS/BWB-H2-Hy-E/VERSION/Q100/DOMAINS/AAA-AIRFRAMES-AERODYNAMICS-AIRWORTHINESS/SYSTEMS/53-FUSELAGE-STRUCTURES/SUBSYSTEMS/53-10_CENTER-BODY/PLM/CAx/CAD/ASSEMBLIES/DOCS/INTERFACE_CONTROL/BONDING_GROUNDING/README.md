# BONDING_GROUNDING — Bonding and Grounding Requirements

## Purpose

This directory contains electrical bonding and grounding specifications for interfaces to ensure electrical continuity, lightning protection, EMI/EMC compliance, and safety.

## Content Types

### Bonding Specifications
- Bonding jumper requirements
- Bonding surface preparation
- Bonding resistance limits
- Bonding verification procedures

### Grounding Requirements
- Ground paths and locations
- Ground stud specifications
- Ground resistance requirements
- Ground fault protection

### Lightning Protection
- Lightning strike zones
- Direct effects protection
- Indirect effects protection
- Current path requirements

### EMI/EMC Bonding
- RF bonding requirements
- Shield terminations
- Connector bonding
- EMI gaskets

## File Formats

- `.pdf` — Bonding drawings and specifications
- `.csv` — Bonding point schedules
- `.xlsx` — Resistance requirement tables
- `.dwg` — Bonding strap layouts

## Bonding Categories

### Primary Structure Bonding
- Metal-to-metal contact
- Bonding across joints
- Fastener bonding
- Faying surface bonding

### System Bonding
- Equipment case grounding
- Wire shield bonding
- Connector shell bonding
- Component mounting bonding

### Lightning Bonding
- Lightning zone bonding
- Current path bonding
- Fastener conductivity
- Composite bonding

## Bonding Methods

### Direct Bonding
- Clean metal-to-metal contact
- Conductive primer removal
- Serrated washers
- Toothed lock washers

### Bonding Jumpers
- Braided copper straps
- Flexible bonding straps
- Multiple-point bonding
- Redundant bonds

### Conductive Fasteners
- Cadmium-plated steel
- Aluminum alloy
- Stainless steel (treated)
- Special bonding fasteners

## Resistance Requirements

### Bonding Resistance Limits
- **Primary structure**: < 2.5 milliohms
- **Equipment grounding**: < 10 milliohms
- **Lightning protection**: < 5 milliohms
- **RF bonding**: < 1 milliohm (at RF frequencies)

### Measurement Method
- Four-wire Kelvin measurement
- DC resistance at 25°C
- Test current: 10A minimum
- Documentation requirements

## Documentation Structure

### Bonding Point Specification
- Bond point identification
- Location and interface
- Bonding method
- Resistance requirement
- Verification procedure

### Bonding Strap Specification
- Part number and material
- Length and cross-section
- Attachment method
- Installation torque

## Naming Convention

```
BOND_{location}_{type}_v{version}.{ext}
```

Examples:
- `BOND_WING-ATTACH_STRUCTURAL_v001.pdf`
- `BOND_DOOR-FRAME_LIGHTNING_v002.csv`
- `BOND_BULKHEAD_EMI_v001.xlsx`

## Bonding Installation

### Surface Preparation
1. Remove non-conductive coatings
2. Clean to bare metal
3. Light abrasion if needed
4. Protect from corrosion (temporary)

### Bonding Strap Installation
1. Install one end with torque
2. Route strap properly
3. Avoid sharp bends
4. Install other end with torque
5. Verify resistance

### Fastener Bonding
1. Use conductive fasteners
2. Ensure metal-to-metal contact
3. Apply proper torque
4. Use bonding washers if needed
5. Verify continuity

## Lightning Protection Zones

### Zone Classification (ARP 5414)
- **Zone 1A**: Initial lightning attachment (wings, nose, tail)
- **Zone 1B**: Wing sweep lightning attachment
- **Zone 2A**: Swept stroke areas
- **Zone 2B**: Intermediate probability areas
- **Zone 3**: Low probability areas

### Protection Methods
- Aluminum mesh in composites
- Expanded aluminum foil
- Metal fasteners
- Bonding jumpers across joints

## EMI/EMC Bonding

### Shield Bonding
- 360° shield termination
- Low-impedance bonds
- Multiple ground points (if required)
- RF continuity

### Equipment Bonding
- Mounting stud bonding
- Chassis grounding
- Multiple ground paths
- EMI gaskets at seams

## Verification and Testing

### Initial Verification
- Visual inspection
- Resistance measurement
- Torque verification
- Documentation

### Periodic Testing
- Resistance monitoring
- Corrosion inspection
- Strap condition
- Re-torque if needed

## Cross-References

- [Fasteners](../FASTENERS/)
- [Torque Specifications](../TORQUE_SPECS/)
- [Interface Control Documents](../ICD/)
- [Material Compatibility](../MATERIAL_COMPATIBILITY/)

## Standards

- **SAE ARP 5412**: Aircraft Lightning Environment and Related Test Waveforms
- **SAE ARP 5414**: Aircraft Lightning Zoning
- **MIL-B-5087**: Bonding, Electrical, and Lightning Protection
- **DO-160**: Environmental Conditions and Test Procedures (Section 17: Lightning)
- **MIL-STD-464**: Electromagnetic Environmental Effects
- **SAE ARP 1870**: Grounding and Bonding of Electrical Equipment
