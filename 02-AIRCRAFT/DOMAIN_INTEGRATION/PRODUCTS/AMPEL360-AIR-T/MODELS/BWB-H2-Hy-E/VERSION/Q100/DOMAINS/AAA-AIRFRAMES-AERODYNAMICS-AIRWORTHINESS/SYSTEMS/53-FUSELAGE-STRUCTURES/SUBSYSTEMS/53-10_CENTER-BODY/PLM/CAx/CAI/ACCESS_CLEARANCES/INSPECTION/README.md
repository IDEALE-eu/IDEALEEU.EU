# INSPECTION — Inspection Access Points and Requirements

## Purpose

Documentation of inspection access provisions, non-destructive inspection (NDI) requirements, and inspection procedures for the CENTER-BODY subsystem.

## Content Types

- **Inspection Point Definitions** — Location and access requirements
- **NDI Method Specifications** — Technique and procedure details
- **Access Panel Requirements** — Removable panels for inspection
- **Inspection Interval Schedules** — Frequency and scope

## File Formats

- `.pdf` — Inspection procedures and specifications
- `.step` — 3D access panel and inspection point geometry
- `.csv` — Inspection point schedules
- `.xlsx` — NDI method matrices

## Naming Convention

```
Inspection_{zone}_{method}_{type}_v{version}.{ext}
```

Examples:
- `Inspection_fwd_eddy_current_procedure_v001.pdf`
- `Inspection_center_ultrasonic_points_v002.csv`
- `Inspection_aft_visual_access_v001.step`

## Cross-References

- [Parent: ACCESS_CLEARANCES](../README.md)
- [Tool Sweeps](../TOOL_SWEEPS/README.md)
- [Keep-Out Zones](../KEEP_OUT_ZONES/README.md)
- [Load Paths](../../MOUNTING/LOAD_PATHS/README.md)
- [Maintenance Plans](../../../DELs/)

## NDI Methods

| Method | Application | Access Required | Frequency |
|--------|-------------|-----------------|-----------|
| **Visual (VT)** | Surface defects | Line of sight | Every flight |
| **Eddy Current (ET)** | Surface cracks | Probe contact | 1000 FH |
| **Ultrasonic (UT)** | Internal defects | Couplant access | 2000 FH |
| **Radiography (RT)** | Internal voids | Two-sided access | 5000 FH |
| **Magnetic Particle (MT)** | Ferrous cracks | Surface prep | As required |
| **Dye Penetrant (PT)** | Surface cracks | Surface prep | As required |

## Inspection Categories

### Routine Inspections
- Pre-flight walk-around inspection
- Daily inspection items
- Letter check inspections (A, B, C, D)
- Heavy maintenance visits

### Special Inspections
- Corrosion inspection program
- Fatigue critical areas
- Aging aircraft inspections
- Damage tolerance inspections

### Conditional Inspections
- Post-hard landing
- Post-lightning strike
- Post-overstress event
- Collision/ground damage

## Access Requirements

Each inspection point must have:
- **Visual access**: Direct line of sight or mirror/borescope
- **Physical access**: Probe/sensor placement clearance
- **Preparation access**: Surface cleaning/preparation area
- **Documentation access**: Lighting and workspace for recording

## Inspection Point Documentation

Required information for each point:
- **Location**: X, Y, Z coordinates relative to GAF
- **Structural element**: What is being inspected
- **Method**: NDI technique(s) to be used
- **Frequency**: Inspection interval (flight hours/cycles)
- **Access**: How to reach the point
- **Acceptance criteria**: Pass/fail thresholds
- **Recording**: Documentation requirements

## Inspection Point Schedule Format

```csv
inspection_id,location,element,method,interval_FH,access_type,acceptance_criteria
INS-001,Fwd bulkhead,Skin-stringer,ET,1000,Access panel,No cracks
INS-002,Center keel,Splice joint,UT,2000,Removable floor,No disbond
INS-003,Aft frame,Frame web,VT,500,Direct,No corrosion
```

## Access Panel Requirements

Inspection access panels must provide:
- Minimum opening size: 150mm × 150mm
- Tool clearance for NDI equipment
- Lighting provisions or lamp access
- Secure re-installation method
- Sealing if in pressurized area

## Validation Requirements

- Mockup verification of inspection accessibility
- NDI procedure validation on representative samples
- Inspector training and certification verification
- Documentation of inspection coverage (>95%)
- Validation of acceptance criteria

## Documentation Requirements

- Inspection procedure manuals
- Training materials and certifications
- Inspection forms and checklists
- Historical inspection records
- Findings and corrective actions

## Change Control

Inspection requirement changes require:
- Continued airworthiness review
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Procedure updates and re-approval
- Inspector re-training if methods change
- Regulatory notification if affecting certification
