# OVERLAYS — Installation Overlay Drawings

## Purpose
Installation overlay drawings for positioning, alignment, and reference during assembly.

## Contents
- Installation reference lines and datums
- Positioning overlays for parts/systems
- Alignment guides and targets
- Interface boundaries
- Clearance zones
- Inspection reference marks

## Overlay Types
- **Positioning overlays**: Part placement guides
- **Alignment overlays**: Datum and reference lines
- **Interface overlays**: System interface boundaries
- **Clearance overlays**: Clearance and access zones
- **Inspection overlays**: QA reference marks

## Layer Structure
**Standard layers**:
- **REFERENCE**: Master reference geometry
- **ALIGNMENT**: Alignment marks and guides
- **POSITIONING**: Part positioning aids
- **CLEARANCE**: Clearance zones
- **INTERFACE**: Interface boundaries
- **TEXT**: Installation notes
- **DIMENSIONS**: Reference dimensions

## Installation Information
Document:
- Reference datums (A, B, C)
- Zero coordinate locations
- Alignment tolerance requirements
- Installation sequence
- Special tooling requirements
- Access and clearance requirements

## Usage
Overlays are used:
- As templates for laser projection
- For manual alignment during assembly
- As inspection reference
- For tooling setup
- For system integration verification

## File Naming
```
<system>_OVERLAY_<description>_<revision>_<date>.dxf
```

Examples:
- `53-10_OVERLAY_FWD-SECTION_A_20250110.dxf`
- `53-10_OVERLAY_FRAME-ALIGNMENT_B_20250110.dxf`
- `53-10_OVERLAY_SYSTEM-INTERFACE_A_20250110.dxf`

## Related Directories
- **[../../../../CAM/COMPOSITES/LASER_PROJECTION/](../../../../CAM/COMPOSITES/LASER_PROJECTION/)** — Laser projection files
- **[../JIG_PLATES/](../JIG_PLATES/)** — Physical jig plates
- **[../../ASSEMBLIES/](../../ASSEMBLIES/)** — Assembly drawings

## Manufacturing Use
- Laser projection systems
- Manual layout and marking
- CNC positioning systems
- Robotic assembly guidance
- Quality inspection

## Quality Requirements
- Accurate reference to master geometry
- Clear datum structure
- Tolerance zones clearly marked
- Compatible with projection systems
- Validated against 3D model

## Best Practices
- Keep overlays simple and clear
- Use distinct colors for different purposes
- Include scale reference
- Document coordinate system
- Validate before production use
