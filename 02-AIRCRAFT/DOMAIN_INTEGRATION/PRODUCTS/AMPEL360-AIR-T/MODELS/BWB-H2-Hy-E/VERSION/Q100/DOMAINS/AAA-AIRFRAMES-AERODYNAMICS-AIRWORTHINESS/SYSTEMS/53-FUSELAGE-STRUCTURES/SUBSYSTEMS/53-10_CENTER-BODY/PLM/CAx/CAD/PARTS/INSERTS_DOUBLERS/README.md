# INSERTS_DOUBLERS — Reinforcement and Insert Parts

## Purpose

This directory contains CAD part files for doublers, reinforcement plates, and threaded inserts used in the 53-10 Center Body subsystem. These detail parts provide local reinforcement and attachment provisions.

## Component Description

### Doubler Types
- **Reinforcement doublers**: Local stress reinforcement around cutouts or attachments
- **Shear doublers**: Web reinforcement for shear loads
- **Bearing doublers**: Load distribution at bolt holes
- **Repair doublers**: Temporary or permanent repair reinforcements

### Insert Types
- **Threaded inserts**: Helicoil, Keensert, or similar threaded bushings
- **Floating inserts**: Self-aligning threaded inserts
- **Blind inserts**: Inserts installed from one side
- **Nutplates**: Captive nut inserts for assembly fastening

## Naming Convention

```
53-10_<type>_<identifier>_<location>_<version>.<ext>
```

Examples:
- `53-10_DOUBLER_DBL-001_WINDOW-REINF_v01.CATPart`
- `53-10_INSERT_INS-050_THREADED-M6_v01.prt`
- `53-10_DOUBLER_DBL-020_FITTING-REINF_v02.sldprt`

## Design Considerations

### Doubler Design
- Match base material thickness and properties where possible
- Extend doubler beyond stress concentration area
- Use appropriate fastener spacing and edge distance
- Consider galvanic compatibility with adjacent materials

### Insert Design
- Select insert type based on load and accessibility
- Ensure adequate parent material thickness for insert
- Specify installation torque and thread engagement length
- Consider vibration resistance (self-locking vs. plain threads)

### Material Specifications

#### Doublers
- **Aluminum sheet**: 2024-T3 to match base structure
- **Titanium**: Ti-6Al-4V for high-load or high-temperature areas
- **Composite**: Carbon fiber for composite structure reinforcement

#### Inserts
- **Stainless steel**: 300 series for corrosion resistance
- **Aluminum**: 2024-T4 for weight-sensitive applications
- **Brass**: For thread inserts in soft materials

## Cross-References

- **Frames**: [`../FRAMES/`](../FRAMES/)
- **Skin panels**: [`../SKIN_PANELS/`](../SKIN_PANELS/)
- **Interface fittings**: [`../INTERFACE_FITTINGS/`](../INTERFACE_FITTINGS/)
- **Fasteners**: [`../FASTENERS/`](../FASTENERS/)
- **Standard parts**: [`../STANDARD_PARTS/`](../STANDARD_PARTS/)
- **Detail drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)

## Quality Requirements

Doublers and inserts must meet:
- Material specifications and traceability
- Installation torque requirements for inserts
- Edge distance and spacing requirements for doublers
- Galvanic compatibility verification
