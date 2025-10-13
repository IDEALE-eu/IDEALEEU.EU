# DOOR_SURROUNDS — Door Surround Sub-Assemblies

## Purpose

This directory contains sub-assembly models for door surround structures of the 53-10 Center Body. Door surrounds are reinforced structural frames that provide load paths around door cutouts and support door installations.

## Contents

### Door Types Supported
- **Passenger doors**: Main entry/exit doors (Type A, Type I)
- **Service doors**: Catering and service access doors
- **Emergency exits**: Over-wing and fuselage emergency exits
- **Cargo doors**: Lower deck cargo loading doors
- **Equipment doors**: Access doors for systems and equipment

## Door Surround Components

A typical door surround assembly includes:
- **Primary surround frame**: Main structural ring around door opening
- **Reinforced skin panels**: Thickened or doubled skin at door edges
- **Frame reinforcements**: Beefed-up frames at door corners
- **Stringer terminations**: Special fittings where stringers are cut
- **Door sill beam**: Lower door threshold structure
- **Door header beam**: Upper door frame structure
- **Door hinge/latch fittings**: Attachment provisions for door hardware
- **Pressure sealing interfaces**: Seal mating surfaces

## Naming Convention

Use the following pattern for door surround assemblies:
```
53-10_ASM_DOOR-SURROUND_<door-type>-<position>_v<version>.<ext>
```

Examples:
- `53-10_ASM_DOOR-SURROUND_PAX-FWD-LEFT_v01.CATProduct`
- `53-10_ASM_DOOR-SURROUND_SERVICE-AFT-RIGHT_v02.asm`
- `53-10_ASM_DOOR-SURROUND_CARGO-MAIN_v01.sldasm`

## Design Considerations

### Structural Design
- Design for loads around cutout (stress concentration)
- Transfer interrupted frame and stringer loads
- Design for door operating loads (hinges, latches)
- Include fail-safe provisions (redundant load paths)
- Validate fatigue life at high-stress regions

### Door Interface
- Define door attachment points (hinges, latches, locks)
- Specify seal mating surfaces and tolerances
- Include door alignment provisions
- Design for door weight support
- Provide for door removal/installation

### Load Paths
- **Circumferential loads**: Pressure hoop loads around opening
- **Longitudinal loads**: Fuselage tension/compression
- **Shear loads**: Vertical and lateral shear transfer
- **Local loads**: Door operating loads, impact loads
- **Emergency loads**: Rapid decompression, evacuation slide deployment

## Pressure Containment

For pressure doors:
- Design for cabin pressure differential (8.5 psi typical)
- Include redundant sealing provisions
- Design for rapid decompression scenario
- Validate door frame stiffness for sealing
- Plan for pressure testing during certification

## Integration Points

Door surrounds interface with:
- **Frame sections**: Reinforced frames at door corners
- **Skin panel modules**: Reinforced skin around door opening
- **Stringer bays**: Stringer terminations and doublers
- **Floor modules**: Door sill integration with floor
- **Door systems (ATA-52)**: Door hardware and mechanisms
- **Escape slides**: Slide pack installation provisions

## Door Locations

Typical door locations in center body:
- **Forward left**: Main passenger door (Type A)
- **Forward right**: Service/catering door
- **Mid left/right**: Additional passenger doors or emergency exits
- **Aft left/right**: Aft passenger or service doors
- **Lower deck**: Cargo doors (forward and aft)

## Related Directories

- **Frame sections**: [`../FRAME_SECTIONS/`](../FRAME_SECTIONS/)
- **Skin panel modules**: [`../SKIN_PANEL_MODULES/`](../SKIN_PANEL_MODULES/)
- **Stringer bays**: [`../STRINGER_BAYS/`](../STRINGER_BAYS/)
- **Component models**: [`../../../MODELS/`](../../../MODELS/)
- **Documentation**: [`../DOCS/`](../DOCS/)
- **Top-level assembly**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)

## Design Guidelines

### Cutout Reinforcement
- Increase frame cross-section at door corners
- Add doublers to skin panels around opening
- Terminate stringers with special fittings
- Include diagonal members for shear transfer
- Design for damage tolerance and crack arrest

### Door Hardware Interface
- Provide for hinge pin installation and removal
- Design latch engagement surfaces
- Include lock pin provisions
- Provide for door stop and holdopen features
- Plan for escape slide installation (passenger doors)

### Sealing Provisions
- Machine or bond seal mating surfaces
- Design for proper seal compression
- Include drainage for seal grooves
- Provide for seal replacement access
- Validate sealing under all load conditions

## Certification Requirements

### Structural Testing
- Static strength test to ultimate load
- Fatigue test for design life
- Rapid decompression test (for pressure doors)
- Door operating loads test
- Emergency evacuation demonstration

### Door Operation
- Door opening/closing force limits
- Emergency operation time limits (evacuation)
- Fail-safe and backup systems validation
- Warning system functionality
- Slide deployment testing (passenger doors)

## Metadata Requirements

Each door surround assembly should include:
- **Part number**: Following 53-10 numbering system
- **Description**: Door type and location
- **Door dimensions**: Height x width of opening
- **Door type code**: Per regulatory classification
- **Pressure rating**: Design pressure differential (if applicable)
- **Material**: Primary materials and treatments
- **Mass properties**: Weight and CG
- **Status**: Design state (draft, released, obsolete)

## Manufacturing Considerations

### Fabrication Planning
- Complex forming may be required for doublers
- Large machined fittings for corners
- Precision drilling for door hardware
- Surface finish requirements for seals
- Heat treatment and finishing processes

### Assembly Integration
- Install door surround before final door installation
- Coordinate with systems installations
- Plan for alignment checks during assembly
- Include provisions for shimming and adjustment
- Document final acceptance criteria

## Safety Considerations

Critical safety items:
- Redundant load paths (fail-safe design)
- Emergency operation provisions
- Warning systems for improper closure
- Fire protection at door frame
- Escape slide installation and deployment

## Quality Assurance

Critical quality checks:
- Dimensional accuracy of opening
- Door hardware hole locations
- Seal surface flatness and finish
- Load path continuity verification
- Non-destructive inspection of critical areas

## Version Control

- Use Git LFS for large assembly files (> 10 MB)
- Tag design reviews and certification tests
- Document door type or location changes
- Maintain revision history for each door surround
- Coordinate changes with ATA-52 door system owner
