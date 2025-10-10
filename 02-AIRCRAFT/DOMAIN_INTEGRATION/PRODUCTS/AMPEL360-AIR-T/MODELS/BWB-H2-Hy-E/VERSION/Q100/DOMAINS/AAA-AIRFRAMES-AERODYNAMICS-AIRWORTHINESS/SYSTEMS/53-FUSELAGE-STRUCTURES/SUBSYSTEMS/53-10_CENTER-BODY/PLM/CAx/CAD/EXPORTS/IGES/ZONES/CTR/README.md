# CTR — Center Zone IGES Exports

## Purpose

This directory contains IGES exports for components and assemblies located in the center zone of the CENTER-BODY subsystem.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Center frames**: Frames in center section
- **Center panels**: Skin panels in center zone
- **Center bulkheads**: Bulkheads at center stations
- **Wing attachment**: Wing-to-body joint structure
- **Main structure**: Primary load-bearing center structure
- **Center fittings**: Major attachments and fittings

## Zone Definition

**Center Zone** typically includes:
- Primary load-bearing fuselage section
- Wing-body intersection and attachment
- Major bulkheads and frames
- Center fuselage section between forward and aft

Refer to zone definition drawings for exact station boundaries.

## File Naming Convention

```
<subsystem>_CTR_<component>_<part-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_CTR_FRAME-C01_PN-32001_RevA_20250110.igs`
- `53-10_CTR_PANEL-CTR-01_PN-32002_RevB_20250110.igs`
- `53-10_CTR_WING-ATTACH_PN-32003_RevA_20250110.igs`

## Zone Characteristics

Center zone geometry typically includes:
- **Maximum cross-section**: Largest fuselage diameter
- **Wing integration**: Wing-body joint and carrythrough
- **Primary structure**: Main load-bearing frames and bulkheads
- **Equipment bays**: Major equipment installations
- **Landing gear bays**: Main landing gear (if applicable)
- **Fuel tanks**: Center fuel tank structure (if applicable)

## Related Directories

- **Parent**: [`../`](../) — All ZONES
- **Adjacent zones**: [`../FWD/`](../FWD/) — Forward zone, [`../AFT/`](../AFT/) — Aft zone
- **Parts**: [`../../PARTS/`](../../PARTS/) — Component-type organization
- **Assemblies**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/) — Assembly-based organization
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD models

## Critical Interfaces

Center zone contains critical interfaces:
- **Wing-body joint**: Primary wing attachment (System 57)
- **Forward zone interface**: Forward bulkhead connection
- **Aft zone interface**: Aft bulkhead connection
- **Landing gear**: Main landing gear interface (if applicable)
- **Systems**: Major system installations and routing

## Zone Organization Benefits

Organizing by zone enables:
- **Manufacturing**: Focus on center body fabrication
- **Assembly**: Center section assembly as major unit
- **Load analysis**: Primary structure load paths
- **Weight distribution**: Center of gravity analysis
- **System integration**: Centralized system installations

## Coordinate System

Center zone uses aircraft coordinate system:
- **X-axis**: Positive forward
- **Y-axis**: Positive right (viewing from behind)
- **Z-axis**: Positive up
- **Origin**: Typically at nose or datum reference point

Document fuselage station references for all geometry.

## Structural Significance

Center zone is typically the:
- **Primary load path**: Main structural load-bearing section
- **Wing attachment**: Critical wing-body integration
- **Fuel structure**: Center fuel tank containment (if applicable)
- **Landing gear**: Main gear support structure (if applicable)
- **Pressure boundary**: Critical pressure vessel section

## Best Practices

- Export complete zone geometry for integration analysis
- Include all interface boundaries with adjacent zones
- Document critical load paths and attachments
- Verify wing-body joint geometry accuracy
- Maintain tight tolerances for critical interfaces
- Cross-reference to structural analysis models
- Coordinate with systems integration

## Zone-Based Workflow

When working with center zone IGES files:
1. Identify fuselage station boundaries
2. Export complete zone structure
3. Verify wing attachment interfaces
4. Check clearances for systems and equipment
5. Validate load paths and structural continuity
6. Document zone-specific structural requirements
7. Coordinate with adjacent zone geometry
