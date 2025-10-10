# INTERFACES — Interface Connection Geometry IGES Exports

## Purpose

This directory contains IGES exports of interface geometries defining connection points, attachment surfaces, and integration boundaries with adjacent systems and structures.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Attachment interfaces**: Structural attachment surfaces
- **Mounting interfaces**: Component mounting definitions
- **Connection geometry**: Interface join surfaces
- **Mating surfaces**: Part-to-part mating geometry
- **Integration boundaries**: System integration envelopes
- **Bolt patterns**: Fastener hole patterns at interfaces

## File Naming Convention

```
<subsystem>_INTERFACE_<adjacent-system>_<interface-id>_<revision>_<date>.igs
```

**Examples:**
- `53-10_INTERFACE_51-FUSELAGE_IFX-001_RevA_20250110.igs`
- `53-10_INTERFACE_57-WING_IFX-002_RevB_20250110.igs`
- `53-10_INTERFACE_BULKHEAD_IFX-003_RevA_20250110.igs`

## Interface Types

### Structural Interfaces
- **Load-bearing joints**: Primary structure connections
- **Bulkhead interfaces**: Bulkhead attachment surfaces
- **Frame interfaces**: Frame-to-skin connections
- **Wing-body joint**: Wing attachment interface

### System Interfaces
- **Equipment mounting**: System equipment interfaces
- **Access panel interfaces**: Panel attachment boundaries
- **Door frame interfaces**: Door surround connections
- **Window interfaces**: Window mounting surfaces

### Installation Interfaces
- **Pre-installation**: Interface geometry before installation
- **Post-installation**: As-installed interface configuration
- **Service interfaces**: Maintenance access interfaces

## Export Requirements

When exporting interface geometry to IGES:
- ✅ Use IGES version 5.3
- ✅ Export complete interface surfaces and features
- ✅ Include hole patterns and attachment features
- ✅ Verify dimensions and tolerances
- ✅ Use millimeters for units
- ✅ Set tolerance to 0.001 mm or better
- ✅ Document interface coordinate system

## Critical Information

Interface exports should include:
- **Mating surfaces**: Contact surfaces between components
- **Fastener locations**: Bolt/rivet hole positions and sizes
- **Datum references**: Interface coordinate system
- **Clearances**: Required clearances at interface
- **Sealing surfaces**: Seal groove geometry (if applicable)
- **Alignment features**: Dowel pins, locating features

## Validation Checklist

Before committing interface IGES files:
- [ ] All interface surfaces included
- [ ] Hole patterns accurate
- [ ] Dimensions verified against ICD
- [ ] Coordinate system documented
- [ ] Mating parts checked for fit
- [ ] Clearances verified
- [ ] Scale confirmed (1:1)

## Related Directories

- **Parent**: [`../`](../) — All INSTALLATION
- **Envelopes**: [`../ENVELOPES/`](../ENVELOPES/) — Clearance envelopes
- **Parts**: [`../../PARTS/`](../../PARTS/) — Part geometry
- **Assemblies**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/) — Assembly models
- **Integration**: [`../../../../CAI/INTERFACES/`](../../../../CAI/INTERFACES/) — Interface control documents

## Interface Control

Interfaces are governed by:
- **ICDs**: Interface Control Documents
- **Interface matrix**: System-level interface tracking
- **Integration drawings**: Interface definition drawings
- **Tolerance analysis**: Interface stack-up analysis

See [`../../../../CAI/INTERFACE_MATRIX/`](../../../../CAI/INTERFACE_MATRIX/) for interface tracking.

## Best Practices

- Export interface geometry accurately with tight tolerances
- Include both sides of interface when applicable
- Document coordinate system and datums
- Cross-reference to ICD and interface drawings
- Verify fit with mating component geometry
- Include fastener hole patterns and sizes
- Test import in recipient's CAD system

## Integration Notes

When providing interface IGES files:
- **Include**: Complete interface geometry, hole patterns, datums
- **Document**: Interface coordinate system, datum references
- **Specify**: Tolerance requirements, clearances
- **Reference**: ICD document number and revision
- **Coordinate**: With interfacing system design teams
- **Verify**: Fit with mating component models

## Usage Scenarios

Interface IGES files are used for:
- Integration analysis and fit checks
- Fastener pattern verification
- Clearance and interference analysis
- Manufacturing tooling design
- Assembly planning and simulation
- Supplier coordination

## Interface Management

Maintain interface geometry in sync with:
- Interface Control Documents (ICDs)
- System integration models
- Assembly definitions
- Manufacturing plans
- Test and verification procedures
