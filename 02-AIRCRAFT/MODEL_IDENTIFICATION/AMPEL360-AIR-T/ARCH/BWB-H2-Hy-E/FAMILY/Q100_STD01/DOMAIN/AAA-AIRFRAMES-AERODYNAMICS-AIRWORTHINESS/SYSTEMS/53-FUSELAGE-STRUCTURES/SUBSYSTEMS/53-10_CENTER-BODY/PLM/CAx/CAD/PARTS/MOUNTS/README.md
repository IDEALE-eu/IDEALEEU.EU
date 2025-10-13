# MOUNTS — Equipment Mounting Provisions

## Purpose

This directory contains CAD part files for equipment mounting provisions and attachment points used in the 53-10 Center Body subsystem. Mounts provide structural interfaces for systems equipment, avionics, and mechanical components.

## Component Description

### Mount Types
- **Avionics racks**: Mounting provisions for avionics boxes and LRUs
- **Pump mounts**: Hydraulic and fuel pump mounting brackets
- **Actuator mounts**: Flight control actuator attachment points
- **Battery trays**: Battery mounting and retention systems
- **Equipment shelves**: Mounting platforms for systems equipment
- **Shock mounts**: Vibration-isolated mounts for sensitive equipment

## Naming Convention

```
53-10_MOUNT_<equipment-type>_<location>_<version>.<ext>
```

Examples:
- `53-10_MOUNT_AVIONICS-RACK_FWD_v01.CATPart`
- `53-10_MOUNT_HYDRAULIC-PUMP_CENTER_v02.prt`
- `53-10_MOUNT_BATTERY-TRAY_AFT_v01.sldprt`

## Design Considerations

### Structural Requirements
- Support equipment weight and operational loads
- Accommodate vibration and shock loads
- Provide access for installation, removal, and maintenance
- Include provisions for cable routing and system connections
- Consider thermal management and cooling requirements

### Material Specifications
- **Aluminum alloy**: 6061-T6 or 2024-T3 for general mounts
- **Steel**: For high-load or high-temperature applications
- **Titanium**: For weight-critical or high-temperature locations

### Interface Management
- Coordinate with equipment suppliers for mounting interface
- Verify bolt patterns and clearances
- Document load introduction points
- Define torque specifications

## Design Requirements

### Equipment Interface
- Match equipment mounting footprint and hole pattern
- Provide adjustment capability for alignment
- Include grounding provisions for electrical bonding
- Consider thermal expansion effects

### Structure Interface
- Attach to primary structure (frames, bulkheads) where possible
- Distribute loads appropriately
- Avoid single-point failures
- Provide redundant load paths where required

## Cross-References

- **Equipment specifications**: Reference system design data
- **Interface control**: [`../../../CAI/INTERFACES/`](../../../CAI/INTERFACES/)
- **Frame attachments**: [`../FRAMES/`](../FRAMES/)
- **Brackets and clips**: [`../BRACKETS_CLIPS/`](../BRACKETS_CLIPS/)
- **Fasteners**: [`../FASTENERS/`](../FASTENERS/)
- **Detail drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)

## Quality Requirements

Equipment mounts must meet:
- Load capability with positive margin per equipment specifications
- Vibration and shock requirements per equipment supplier data
- Electrical bonding and grounding requirements
- Accessibility for maintenance per design standards
