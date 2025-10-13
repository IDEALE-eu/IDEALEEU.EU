# AFT — Aft Zone IGES Exports

## Purpose

This directory contains IGES exports for components and assemblies located in the aft zone of the CENTER-BODY subsystem.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Aft frames**: Frames in aft section
- **Aft panels**: Skin panels in aft zone
- **Aft bulkheads**: Bulkheads at aft stations
- **Tail attachment**: Empennage attachment structure
- **Aft pressure bulkhead**: Rear pressure boundary (if applicable)
- **Aft fittings**: Attachments and fittings in aft area

## Zone Definition

**Aft Zone** typically includes:
- Aft fuselage section from center to tail
- Tail cone and empennage attachment structure
- Aft bulkhead to tail attachment
- Aft equipment bays and systems

Refer to zone definition drawings for exact station boundaries.

## File Naming Convention

```
<subsystem>_AFT_<component>_<part-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_AFT_FRAME-A01_PN-33001_RevA_20250110.igs`
- `53-10_AFT_PANEL-AFT-01_PN-33002_RevB_20250110.igs`
- `53-10_AFT_TAIL-ATTACH_PN-33003_RevA_20250110.igs`

## Zone Characteristics

Aft zone geometry typically includes:
- **Tapered structure**: Decreasing cross-section toward tail
- **Empennage attachment**: Tail attachment fittings and structure
- **Pressure bulkhead**: Aft pressure boundary (if pressurized)
- **APU bay**: Auxiliary Power Unit installation (if applicable)
- **Tail cone**: Aftmost structural elements
- **Equipment bays**: Aft equipment installations

## Related Directories

- **Parent**: [`../`](../) — All ZONES
- **Adjacent zones**: [`../FWD/`](../FWD/) — Forward zone, [`../CTR/`](../CTR/) — Center zone
- **Parts**: [`../../PARTS/`](../../PARTS/) — Component-type organization
- **Assemblies**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/) — Assembly-based organization
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD models

## Critical Interfaces

Aft zone contains important interfaces:
- **Center zone interface**: Forward boundary connection
- **Empennage**: Horizontal and vertical stabilizer attachments
- **Systems**: Aft-mounted systems and equipment
- **APU**: Auxiliary Power Unit (if applicable)
- **Tail bumper**: Tail strike protection (if applicable)

## Zone Organization Benefits

Organizing by zone enables:
- **Manufacturing**: Aft section fabrication planning
- **Assembly**: Aft body assembly as separate unit
- **Installation**: Sequential aft section installation
- **Maintenance**: Aft zone maintenance access planning
- **Documentation**: Zone-based technical manuals

## Coordinate System

Aft zone uses aircraft coordinate system:
- **X-axis**: Positive forward (increasing fuselage stations going aft)
- **Y-axis**: Positive right (viewing from behind)
- **Z-axis**: Positive up

Document fuselage station references and tail attachment datums.

## Structural Considerations

Aft zone typically features:
- **Load concentration**: Empennage loads transferred to fuselage
- **Pressure containment**: Aft pressure bulkhead (if pressurized)
- **Taper geometry**: Complex taper from center body to tail
- **Service access**: Aft equipment access doors and panels
- **Aerodynamic shaping**: Smooth aft fuselage contours

## Best Practices

- Export complete aft zone geometry for integration
- Include empennage attachment interface geometry
- Document aft pressure bulkhead (if applicable)
- Verify fit with center zone geometry
- Check clearances for aft systems and equipment
- Maintain accurate tail attachment datums
- Cross-reference to empennage interface definitions

## Zone-Based Workflow

When working with aft zone IGES files:
1. Identify fuselage station boundaries
2. Export geometry in zone coordinate system
3. Verify empennage attachment interfaces
4. Check aft pressure bulkhead integrity (if applicable)
5. Validate fit with center zone
6. Document zone-specific structural requirements
7. Coordinate with empennage design team

## APU and Systems Integration

If aft zone includes APU or major systems:
- Document APU installation envelope
- Include APU mounting structure
- Define access doors and service panels
- Coordinate with systems design teams
- Verify clearances and maintenance access
