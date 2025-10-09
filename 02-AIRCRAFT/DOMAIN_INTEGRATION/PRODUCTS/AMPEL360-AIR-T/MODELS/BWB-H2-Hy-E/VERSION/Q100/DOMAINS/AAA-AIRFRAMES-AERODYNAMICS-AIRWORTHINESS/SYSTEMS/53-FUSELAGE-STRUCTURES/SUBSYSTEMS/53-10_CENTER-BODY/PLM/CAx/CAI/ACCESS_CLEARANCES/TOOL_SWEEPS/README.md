# TOOL_SWEEPS — Tool Access Envelopes for Assembly and Maintenance

## Purpose

Definition of tool access envelopes and clearance volumes required for assembly, installation, and maintenance operations on the CENTER-BODY subsystem.

## Content Types

- **Tool Sweep Volume Definitions** — 3D tool motion envelopes
- **Access Requirements Matrices** — Tool type and clearance needs
- **Assembly Sequence Studies** — Installation feasibility analysis
- **Maintenance Access Plans** — Scheduled and unscheduled maintenance

## File Formats

- `.step` — 3D tool sweep volumes
- `.pdf` — Tool access drawings and procedures
- `.csv` — Tool specification tables
- `.xlsx` — Access feasibility matrices

## Naming Convention

```
ToolSweep_{task_id}_{tool_type}_v{version}.{ext}
```

Examples:
- `ToolSweep_INST-001_torque_wrench_v001.step`
- `ToolSweep_MAINT-015_borescope_v002.pdf`
- `ToolSweep_ASSY-020_rivet_gun_v001.csv`

## Cross-References

- [Parent: ACCESS_CLEARANCES](../README.md)
- [Keep-Out Zones](../KEEP_OUT_ZONES/README.md)
- [Inspection Access](../INSPECTION/README.md)
- [Fastener Maps](../../MOUNTING/FASTENER_MAPS/README.md)
- [Maintenance Procedures](../../../DELs/)

## Tool Categories

| Category | Typical Tools | Min. Clearance | Access Frequency |
|----------|---------------|----------------|------------------|
| **Installation** | Torque wrench, rivet gun | 150mm arc | One-time |
| **Inspection** | Borescope, NDI probe | 50mm straight | Scheduled |
| **Removal** | Impact wrench, pry bar | 200mm arc | As needed |
| **Adjustment** | Screwdriver, allen key | 75mm arc | Periodic |

## Standard Tool Clearances

### Hand Tools
- **Torque wrench**: 150mm clearance + 300mm arc swing
- **Socket wrench**: 100mm clearance + 180° rotation
- **Screwdriver**: 50mm clearance + 200mm length
- **Pliers/cutters**: 100mm clearance + 45° opening

### Power Tools
- **Pneumatic drill**: 200mm clearance + 100mm depth
- **Impact wrench**: 150mm clearance + tool length
- **Rivet gun**: 300mm clearance + 150mm depth

### Inspection Tools
- **Borescope**: 25mm diameter + 500mm insertion
- **Ultrasonic probe**: 50mm clearance + contact surface
- **Eddy current probe**: 75mm clearance + scanning area

## Access Requirements

### Assembly Access
- All fasteners must be installable with standard tools
- No special tools without documented justification
- Two-person lift clearance where required
- Part removal path must be clear

### Maintenance Access
- Line-replaceable units (LRUs) accessible in <30 min
- Shop-replaceable units (SRUs) accessible in <2 hours
- Inspection points accessible per maintenance schedule
- Emergency access provisions documented

## Validation Requirements

- 3D CAD tool simulation (digital mockup)
- Physical mockup verification for critical access
- Maintainability assessment per ATA MSG-3
- Mean time to repair (MTTR) predictions
- Accessibility ratings (good/fair/poor)

## Documentation Requirements

Each tool sweep must document:
- **Task description**: What operation is performed
- **Tool specification**: Manufacturer, model, dimensions
- **Clearance envelope**: 3D volume required
- **Access direction**: Approach vector and constraints
- **Operator position**: Technician stance and reach
- **Special requirements**: Lighting, mirrors, fixtures

## Accessibility Ratings

- **Good**: Full tool access, visual line-of-sight, comfortable position
- **Fair**: Limited access, restricted vision, awkward position
- **Poor**: Very limited access, no vision, extreme difficulty
- **Not Accessible**: Cannot be reached with standard tools

## Change Control

Tool access modifications require:
- Maintainability engineering review
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Re-validation of access feasibility
- Maintenance procedure updates
- Training material updates if methods change
