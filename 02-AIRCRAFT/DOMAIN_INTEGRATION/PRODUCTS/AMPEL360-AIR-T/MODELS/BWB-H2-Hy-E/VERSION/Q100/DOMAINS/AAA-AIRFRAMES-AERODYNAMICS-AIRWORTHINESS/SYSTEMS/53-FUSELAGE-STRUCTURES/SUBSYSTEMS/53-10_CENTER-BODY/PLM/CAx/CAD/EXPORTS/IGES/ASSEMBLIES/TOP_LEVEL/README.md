# TOP_LEVEL — Complete Assembly IGES Exports

## Purpose

This directory contains IGES exports of top-level, complete assemblies representing the entire CENTER-BODY subsystem or major integrated assemblies.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Complete assemblies**: Full subsystem integration
- **Major assemblies**: Large integrated structures
- **System-level models**: Complete CENTER-BODY assembly
- **Integration models**: Multiple subsystems combined

## File Naming Convention

```
<subsystem>_<assembly-name>_<revision>_<date>.igs
```

**Examples:**
- `53-10_CENTER-BODY-ASSY_RevA_20250110.igs`
- `53-10_COMPLETE-STRUCTURE_RevB_20250110.igs`
- `53-10_INTEGRATION_RevA_20250110.igs`

## IGES Assembly Limitations

⚠️ **Important**: IGES has limited assembly support compared to STEP:
- ❌ No hierarchical assembly structure
- ❌ No part instances or transformations
- ❌ No assembly constraints
- ⚠️ May export as merged geometry or separate parts

### Assembly Export Approaches

**Option 1: Merged Geometry**
- Export entire assembly as single merged solid/surface
- Loses part boundaries and structure
- Simplest for visualization or manufacturing

**Option 2: Multiple Parts**
- Export each part separately in assembly position
- Maintains individual parts but loses relationships
- Recipient must manage multiple files

**Option 3: Multiple Files + Assembly Structure**
- Export parts individually + assembly definition file
- Most complex but preserves structure
- Not well standardized in IGES

## Recommended Approach

For top-level assemblies:
1. **Primary**: Use STEP AP242 (excellent assembly support)
2. **Secondary**: Export as merged IGES for visualization
3. **Alternative**: Export individual parts separately (see [`../SUB_ASSEMBLIES/`](../SUB_ASSEMBLIES/))

## Export Requirements

When exporting assemblies to IGES:
- ✅ Document export approach used
- ✅ Test import in recipient's system first
- ✅ Verify all parts included
- ✅ Check assembly origin and orientation
- ✅ Use millimeters for units
- ✅ Set tolerance to 0.001 mm

## Validation Checklist

Before committing top-level assembly IGES files:
- [ ] All components present
- [ ] Assembly origin correct
- [ ] Orientation matches expectations
- [ ] Scale is 1:1
- [ ] No missing geometry
- [ ] File opens successfully
- [ ] Documented assembly approach

## Related Directories

- **Parent**: [`../`](../) — All ASSEMBLIES
- **Sub-assemblies**: [`../SUB_ASSEMBLIES/`](../SUB_ASSEMBLIES/) — Component assemblies
- **Parts**: [`../../PARTS/`](../../PARTS/) — Individual part geometry
- **Source**: [`../../../ASSEMBLIES/`](../../../ASSEMBLIES/) — Native CAD assemblies

## Best Practices

- **Prefer STEP AP242** for assembly exchange (better structure support)
- Use IGES assemblies only when specifically required
- Document assembly structure separately (BOM, assembly drawing)
- Provide both merged and separate part files when possible
- Include assembly drawing (PDF) for reference
- Cross-reference to native CAD assembly file

## Alternative Formats

For better assembly exchange, consider:
- **STEP AP242**: Full assembly structure and hierarchy
- **JT**: Lightweight visualization with assembly structure
- **Native formats**: Best for same-CAD-system exchange

## Usage Scenarios

Use top-level assembly IGES when:
- Legacy system requires IGES and cannot read STEP
- Supplier specifically requests IGES assembly
- Merged geometry acceptable for downstream use
- Visualization only (no need for structure)

Otherwise, use STEP AP242 for assembly exchange.
