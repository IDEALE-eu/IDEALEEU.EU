# PANEL_STACKUPS — Panel Stack-Up Drawings

## Purpose
DXF files showing panel layering, bonding, and assembly stack-up details.

## Contents
- Panel layup sequences
- Bonding surface preparation areas
- Adhesive application zones
- Fastener patterns for panel joints
- Seal and sealant locations
- Shim and doubler locations

## Layer Structure
**Standard layers**:
- **PANEL_OUTLINE**: Panel outer boundaries
- **BONDLINES**: Bonded joint interfaces
- **FASTENERS**: Fastener locations and types
- **SEALS**: Seal and gasket locations
- **SHIMS**: Shim and doubler placement
- **TEXT**: Assembly notes and callouts
- **DIMENSIONS**: Critical dimensions

## Stack-Up Information
Document for each layer:
- Panel part number
- Material specification
- Thickness of each layer
- Bonding method (adhesive, fasteners)
- Assembly sequence
- Cure requirements for adhesives

## Annotations
Include:
- Layer count and sequence
- Total stack-up thickness
- Adhesive type and application method
- Torque requirements for fasteners
- Surface preparation requirements
- Curing time and temperature

## File Naming
```
<assembly>_STACKUP_<zone>_<revision>_<date>.dxf
```

Examples:
- `53-10-ASM05_STACKUP_FWD_A_20250110.dxf`
- `53-10-PANEL-12_STACKUP_CTR_B_20250110.dxf`

## Related Directories
- **[../../PARTS/](../../PARTS/)** — Individual panel parts
- **[../../../../CAM/PROCESS_PLANS/](../../../../CAM/PROCESS_PLANS/)** — Assembly process plans
- **[../../../../CAM/WORK_INSTRUCTIONS/](../../../../CAM/WORK_INSTRUCTIONS/)** — Work instructions

## Manufacturing Requirements
- Identify bonding surfaces clearly
- Specify surface preparation (grit blast, prime)
- Document fastener types and spacing
- Include torque specifications
- Note inspection points
- Specify environmental controls (temperature, humidity)

## Quality Control
- Verify layer sequence
- Check fastener patterns
- Validate bondline dimensions
- Ensure sealant coverage
- Document gap tolerances
