# SUB_ASSEMBLIES — Component Assembly IGES Exports

## Purpose

This directory contains IGES exports of sub-assemblies representing major components or functional groups within the CENTER-BODY subsystem.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Frame assemblies**: Frame structures and stiffeners
- **Panel assemblies**: Skin panels with attachments
- **Structural groups**: Related structural components
- **Functional assemblies**: Components grouped by function
- **Installation assemblies**: Pre-assembled installation units

## File Naming Convention

```
<subsystem>_<sub-assembly-name>_<part-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_FRAME-ASSY-F1-F5_PN-23456_RevA_20250110.igs`
- `53-10_SKIN-PANEL-ASSY_PN-23457_RevB_20250110.igs`
- `53-10_BULKHEAD-ASSY_PN-23458_RevA_20250110.igs`

## IGES Assembly Limitations

⚠️ **Important**: IGES has limited assembly support:
- ❌ No hierarchical structure
- ❌ No part instances
- ❌ No assembly constraints or mates
- ⚠️ May export as merged geometry

See [`../TOP_LEVEL/README.md`](../TOP_LEVEL/README.md) for assembly export approaches.

## Sub-Assembly Organization

Organize sub-assemblies by:
- **Function**: Structural frames, panels, bulkheads
- **Zone**: Forward, center, aft sections
- **Installation**: Pre-assembled units ready for installation
- **Manufacturing**: Shop-floor assembly units

## Export Requirements

When exporting sub-assemblies to IGES:
- ✅ Use IGES version 5.3
- ✅ Document export method (merged vs. separate parts)
- ✅ Maintain assembly origin and orientation
- ✅ Include all sub-assembly components
- ✅ Use millimeters for units
- ✅ Set tolerance to 0.001 mm

## Export Strategies

### Strategy 1: Merged Geometry
**Best for**: Manufacturing, CNC programming
- Export sub-assembly as single merged model
- Simplifies downstream processing
- Loses individual part identity

### Strategy 2: Separate Parts
**Best for**: Part-level analysis, individual fabrication
- Export each part of sub-assembly separately
- Maintain in assembly position
- Create separate IGES file per part
- Use consistent file naming with assembly reference

### Strategy 3: Hybrid Approach
**Best for**: Flexibility
- Export both merged and separate versions
- Provide merged file for manufacturing
- Provide separate files for part procurement

## Validation Checklist

Before committing sub-assembly IGES files:
- [ ] All components included
- [ ] Assembly origin documented
- [ ] Orientation correct
- [ ] No interference between parts
- [ ] Scale verified (1:1)
- [ ] File opens successfully
- [ ] Export method documented

## Related Directories

- **Parent**: [`../`](../) — All ASSEMBLIES
- **Top-level**: [`../TOP_LEVEL/`](../TOP_LEVEL/) — Complete assemblies
- **Parts**: [`../../PARTS/`](../../PARTS/) — Individual part geometry
- **Tooling**: [`../../TOOLING/`](../../TOOLING/) — Assembly tooling
- **Source**: [`../../../ASSEMBLIES/`](../../../ASSEMBLIES/) — Native CAD assemblies

## Best Practices

- **Group logically**: Organize by manufacturing or installation sequence
- **Document structure**: Provide BOM and assembly drawing
- **Test import**: Verify in recipient's CAD system
- **Provide alternatives**: Both merged and separate when possible
- **Cross-reference**: Link to native CAD assembly file
- **Use STEP when possible**: Better assembly structure support

## Typical Sub-Assemblies

For CENTER-BODY subsystem:
- **Frame sub-assemblies**: Groups of frames and stiffeners
- **Panel sub-assemblies**: Skin panels with doublers and reinforcements
- **Bulkhead assemblies**: Bulkheads with fittings and attachments
- **Installation units**: Pre-assembled components for installation
- **Access panel assemblies**: Panels with hinges and fasteners

## Manufacturing Notes

When providing IGES sub-assemblies for manufacturing:
- Include merged geometry for CNC programming
- Provide separate parts for component fabrication
- Include tooling reference geometry if needed
- Document assembly sequence
- Specify fastener locations and types (via drawing)

## Alternative Formats

For better sub-assembly exchange:
- **STEP AP242**: Preserves assembly structure
- **JT**: Lightweight visualization with structure
- **Native formats**: Best for same-CAD-system work
