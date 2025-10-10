# FWD — Forward Zone IGES Exports

## Purpose

This directory contains IGES exports for components and assemblies located in the forward zone of the CENTER-BODY subsystem.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Forward frames**: Frames in forward section
- **Forward panels**: Skin panels in forward zone
- **Forward bulkheads**: Bulkheads at forward stations
- **Nose structure**: Forward-most structural elements
- **Forward fittings**: Attachments and fittings in forward area

## Zone Definition

**Forward Zone** typically includes:
- Fuselage stations forward of center section
- Nose cone and forward fuselage structure
- Forward bulkhead to mid-body transition
- Forward attachment points and interfaces

Refer to zone definition drawings for exact station boundaries.

## File Naming Convention

```
<subsystem>_FWD_<component>_<part-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_FWD_FRAME-F01_PN-31001_RevA_20250110.igs`
- `53-10_FWD_PANEL-FWD-01_PN-31002_RevB_20250110.igs`
- `53-10_FWD_BULKHEAD_PN-31003_RevA_20250110.igs`

## Zone Characteristics

Forward zone geometry typically includes:
- **Tapered structure**: Decreasing cross-section
- **Nose attachment**: Forward-most attachment points
- **Cockpit interface**: Flight deck integration (if applicable)
- **Equipment bays**: Forward equipment installation
- **Landing gear interface**: Nose gear attachments (if applicable)

## Related Directories

- **Parent**: [`../`](../) — All ZONES
- **Adjacent zones**: [`../CTR/`](../CTR/) — Center zone, [`../AFT/`](../AFT/) — Aft zone
- **Parts**: [`../../PARTS/`](../../PARTS/) — Component-type organization
- **Assemblies**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/) — Assembly-based organization
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD models

## Zone Organization Benefits

Organizing by zone enables:
- **Manufacturing**: Zone-based manufacturing planning
- **Assembly**: Sequential zone-based assembly
- **Installation**: Zone-by-zone installation planning
- **Maintenance**: Zone-specific maintenance access
- **Documentation**: Zone-based technical publications

## Coordinate System

Forward zone uses aircraft coordinate system:
- **X-axis**: Positive forward (decreasing fuselage stations)
- **Y-axis**: Positive right (viewing from behind)
- **Z-axis**: Positive up

Document datum and station references in file metadata or accompanying documentation.

## Integration Points

Forward zone interfaces with:
- **Center zone**: Aft boundary of forward zone
- **Nose systems**: Radome, sensors, forward equipment
- **Cockpit**: Flight deck structure (if applicable)
- **Systems**: Forward system installations
- **Landing gear**: Nose gear (if applicable)

## Best Practices

- Organize files by fuselage station or frame number
- Include zone boundary references
- Cross-reference to zone assembly drawings
- Document interfaces with adjacent zones
- Maintain consistent coordinate system
- Verify fit with center zone geometry

## Zone-Based Workflow

When working with forward zone IGES files:
1. Identify fuselage stations and boundaries
2. Export geometry in zone coordinate system
3. Verify interfaces with adjacent zones
4. Check clearances within zone
5. Document zone-specific requirements
6. Coordinate with zone assembly planning
