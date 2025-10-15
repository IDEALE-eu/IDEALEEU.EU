# DOOR_SURROUNDS — Door Frame Reinforcements

## Purpose

This directory contains CAD part files for door surround structures and reinforcements used in the 53-10 Center Body subsystem. Door surrounds provide structural reinforcement around door openings and transfer loads around the cutout.

## Component Description

### Surround Types
- **Passenger door surrounds**: Main cabin entry doors
- **Cargo door surrounds**: Cargo compartment access doors
- **Emergency exit surrounds**: Emergency egress doors
- **Service door surrounds**: Service and equipment access doors

### Components
- **Edge members**: Vertical and horizontal reinforcement beams
- **Corner fittings**: Radius corner reinforcements
- **Doublers**: Local reinforcement plates
- **Hinge fittings**: Door hinge attachment provisions
- **Latch provisions**: Door latch and lock attachment points

## Naming Convention

```
53-10_DOOR-SURROUND_<door-type>_<location>_<version>.<ext>
```

Examples:
- `53-10_DOOR-SURROUND_PAX-MAIN_LEFT-FWD_v01.CATPart`
- `53-10_DOOR-SURROUND_CARGO_AFT_v02.prt`
- `53-10_DOOR-SURROUND_EMER-EXIT_RIGHT_v01.sldprt`

## Design Considerations

### Structural Requirements
- Restore stiffness and strength around door cutout
- Provide continuous load path around opening
- Transfer pressure loads from fuselage to door
- Support door operating loads (hinges, latches)

### Material Specifications
- **Aluminum**: 7075-T6 for high-strength edge members
- **Titanium**: Ti-6Al-4V for weight optimization
- **Composite**: Carbon fiber for integrated structure

## Cross-References

- **Door system**: Reference ATA 52 door system documentation
- **Frame interfaces**: [`../FRAMES/`](../FRAMES/)
- **Skin panels**: [`../SKIN_PANELS/`](../SKIN_PANELS/)
- **Detail drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)
