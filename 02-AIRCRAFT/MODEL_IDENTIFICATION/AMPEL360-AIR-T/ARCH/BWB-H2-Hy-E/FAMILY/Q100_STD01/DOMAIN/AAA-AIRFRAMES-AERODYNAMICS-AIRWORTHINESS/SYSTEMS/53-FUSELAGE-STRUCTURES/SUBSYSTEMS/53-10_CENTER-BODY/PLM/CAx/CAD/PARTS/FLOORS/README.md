# FLOORS — Floor Panel and Beam Parts

## Purpose

This directory contains CAD part files for floor panels and floor beams used in the 53-10 Center Body subsystem. Floor structures support cabin floor loads, provide a working platform, and transfer loads to frames and bulkheads.

## Component Description

### Floor Types
- **Floor panels**: Removable floor panels for cabin and cargo areas
- **Floor beams**: Longitudinal and transverse beams supporting floor panels
- **Support angles**: Edge members and attachment angles
- **Access panels**: Removable floor sections for equipment access
- **Reinforced panels**: Heavy-duty panels for high-load areas

### Configurations
- **Honeycomb core**: Aluminum honeycomb sandwich for lightweight stiffness
- **Solid sheet**: Single-skin aluminum sheet for simple applications
- **Composite**: Carbon fiber face sheets with foam or honeycomb core

## Naming Convention

```
53-10_FLOOR_<component-type>_<location>_<version>.<ext>
```

Examples:
- `53-10_FLOOR_PANEL_FWD-CABIN_v01.CATPart`
- `53-10_FLOOR_BEAM_TRANSVERSE-F05_v02.prt`
- `53-10_FLOOR_SUPPORT-ANGLE_LEFT_v01.sldprt`

## Design Considerations

### Structural Requirements
- Support passenger and cargo loads per certification requirements
- Transfer loads to frames through floor beams
- Provide stiffness for crew and passenger comfort
- Accommodate systems equipment mounted below floor

### Material Specifications
- **Aluminum honeycomb sandwich**: Al face sheets with Al honeycomb core
- **Solid aluminum**: 2024-T3 sheet for simple panels
- **Composite**: Carbon/epoxy for weight optimization

## Cross-References

- **Frame attachments**: [`../FRAMES/`](../FRAMES/)
- **Bulkhead connections**: [`../BULKHEADS/`](../BULKHEADS/)
- **Access panels**: [`../ACCESS_PANELS/`](../ACCESS_PANELS/)
- **Detail drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)
