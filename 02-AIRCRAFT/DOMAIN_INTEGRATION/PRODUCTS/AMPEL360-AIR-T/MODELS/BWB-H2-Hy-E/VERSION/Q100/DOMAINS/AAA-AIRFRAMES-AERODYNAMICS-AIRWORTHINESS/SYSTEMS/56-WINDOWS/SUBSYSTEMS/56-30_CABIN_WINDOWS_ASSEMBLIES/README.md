# 56-30 CABIN_WINDOWS_ASSEMBLIES — Windows (BWB-H2-Hy-E, Q100)

**Purpose**: Passenger cabin windows with frames, seals, scratch panes, and inner trim integration.

## Scope
- Passenger cabin window assemblies
- Fixed window construction (non-opening)
- Multi-layer glazing (outer pane, interlayer, inner pane)
- Window frames and reveal structure
- Sealing and gaskets
- Integration with cabin interior trim (ATA-25)
- Window shades/blinds mounting provisions

## Key Requirements
- **Structural**: Withstand pressurization differential
- **Optical**: Adequate clarity for passenger viewing
- **Emergency**: Survive emergency landing loads
- **Sealing**: Pressure sealing, no leakage
- **Aesthetics**: Clean interior appearance, trim integration
- **Maintenance**: Accessible for inspection and replacement

## Interfaces
- **25 Cabin Interior** — Interior trim, reveal panels, shade mounting
- **52 Doors** — Coordination with door frame interfaces
- **53 Fuselage** — Window cutouts, structural frames
- **56-60** — Integration with scratch panes and shades

## Deliverables
- Cabin window assembly drawings (CAD)
- Structural analysis (pressurization, emergency loads) (CAE)
- Installation procedures (CAI)
- Manufacturing specifications (CAM)
- Service procedures (CAS)

## PLM Structure

This subsystem contains engineering artifacts organized by CAx discipline in the [PLM/CAx/](./PLM/CAx/) directory.

### Engineering BOM
See [PLM/EBOM_LINKS.md](./PLM/EBOM_LINKS.md) for Bill of Materials references.

## Directory Structure

```
56-30_CABIN_WINDOWS_ASSEMBLIES/
├─ README.md (this file)
└─ PLM/
   ├─ EBOM_LINKS.md
   └─ CAx/
      ├─ CAD/  — Assembly drawings, 3D models
      ├─ CAE/  — Structural analysis
      ├─ CAO/  — Design optimization
      ├─ CAI/  — Installation procedures
      ├─ CAM/  — Manufacturing specifications
      ├─ CAV/  — Validation and testing
      ├─ CAP/  — Production procedures
      ├─ CAS/  — Service and maintenance
      └─ CMP/  — Materials processing
```

## Configuration Management
- Changes via ECR/ECO per `00-PROGRAM/CONFIG_MGMT/`

## References
- Parent system: [56-WINDOWS](../../README.md)
- Standards: [56-00_STANDARDS_GENERAL](../56-00_STANDARDS_GENERAL/README.md)
