# JIGS — Assembly Jigs and Positioning Fixtures

## Purpose

This directory contains CAD models for assembly jigs and positioning fixtures used in the fabrication and assembly of the 53-10 Center Body.

## Contents

### Jig Types
- **Assembly jigs**: Fixtures for component positioning during assembly
- **Welding/bonding fixtures**: Support structures for joining operations
- **Alignment tools**: Precision positioning and alignment aids
- **Support fixtures**: Temporary supports during assembly

## Jig Categories

### Frame Assembly Jigs
- Frame positioning fixtures
- Stringer alignment jigs
- Skin panel support fixtures

### Integration Jigs
- Wing-to-body assembly fixtures
- Bulkhead installation jigs
- Interface alignment tools

### Fastening Jigs
- Drilling fixtures
- Rivet/fastener installation guides
- Torque application supports

## Naming Convention

Use the following pattern:
```
53-10_FIX_JIG_<assembly-area>_<version>.<ext>
```

Examples:
- `53-10_FIX_JIG_FRAME-F05-ASSEMBLY_v01.CATProduct`
- `53-10_FIX_JIG_WING-ATTACH-ALIGN_v02.asm`
- `53-10_FIX_JIG_SKIN-PANEL-SUPPORT_v01.sldasm`

## Jig Design Requirements

Assembly jigs should:
- Reference production coordinate system
- Provide repeatable positioning (tolerance: ±0.5mm)
- Include clamping provisions
- Allow access for assembly operations
- Be designed for ease of use
- Include identification and revision markings

## Documentation

Each jig should include:
- Usage instructions
- Setup and calibration procedures
- Inspection and maintenance schedule
- Load capacity and limitations
- Safety requirements

## Related Directories

- **Check fixtures**: [`../CHECK_FIXTURES/`](../CHECK_FIXTURES/)
- **Manufacturing processes**: [`../../../../CAM/`](../../../../CAM/)
- **Assembly procedures**: [`../../../../CAI/`](../../../../CAI/)
