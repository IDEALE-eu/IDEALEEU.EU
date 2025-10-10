# TANK_SUPPORTS — Hydrogen Tank Support Structure Parts

## Purpose

This directory contains CAD part files for tank support structures used in the 53-10 Center Body subsystem. These components support and restrain the hydrogen storage tanks, transferring tank loads to the primary fuselage structure while accommodating thermal expansion and contraction.

## Component Description

### Support Types
- **Cradles**: Curved support structures cradling tank bottom
- **Trunnions**: Pivoting support points for thermal expansion
- **Struts**: Tension/compression members restraining tank position
- **Tie-down fittings**: Attachment points securing tank to structure
- **Anti-rotation devices**: Prevent tank rotation under load
- **Thermal breaks**: Insulating elements minimizing heat transfer

## Naming Convention

```
53-10_TANK-SUPPORT_<support-id>_<location>_<version>.<ext>
```

Examples:
- `53-10_TANK-SUPPORT_TS-01_FWD-CRADLE_v01.CATPart`
- `53-10_TANK-SUPPORT_TS-05_CENTER-TRUNNION_v02.prt`
- `53-10_TANK-SUPPORT_TS-10_AFT-STRUT_v01.sldprt`

## Design Considerations

### Structural Requirements
- Support full tank weight under all flight loads (including crash loads)
- Accommodate thermal contraction of cryogenic hydrogen tanks (-253°C)
- Allow controlled movement for thermal expansion/contraction
- Provide fail-safe load paths
- Minimize heat transfer to maintain tank insulation efficiency

### Material Specifications
- **Titanium**: Ti-6Al-4V for low thermal conductivity and high strength
- **Stainless steel**: 316L for cryogenic compatibility
- **Composite**: Carbon fiber with low thermal conductivity
- **Insulation**: Aerogel or foam thermal breaks

### Thermal Considerations
- Design for temperature differential from -253°C (LH2) to ambient
- Account for differential thermal expansion between tank and structure
- Include thermal breaks to minimize heat leak
- Consider frost/ice formation on support structures

## Interface Management

### Tank Interface
- Coordinate with tank design team (ATA 28 or dedicated hydrogen systems)
- Verify tank attachment provisions and load introduction points
- Define movement allowances for thermal effects
- Document assembly and disassembly procedures

### Fuselage Interface
- Attach to frames and bulkheads at defined hard points
- Distribute loads to primary structure
- Avoid concentrated loads on skin panels

## Cross-References

- **Tank system**: (Reference hydrogen tank system documentation)
- **Frame attachments**: [`../FRAMES/`](../FRAMES/)
- **Bulkhead attachments**: [`../BULKHEADS/`](../BULKHEADS/)
- **Fasteners**: [`../FASTENERS/`](../FASTENERS/)
- **Thermal analysis**: [`../../../CAE/`](../../../CAE/)
- **Detail drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)

## Quality Requirements

Tank support parts must meet:
- Ultimate load capability with positive margin
- Fatigue life for cyclic thermal and flight loads
- Cryogenic material compatibility certification
- Thermal conductivity requirements
- Proof load and thermal cycle testing
