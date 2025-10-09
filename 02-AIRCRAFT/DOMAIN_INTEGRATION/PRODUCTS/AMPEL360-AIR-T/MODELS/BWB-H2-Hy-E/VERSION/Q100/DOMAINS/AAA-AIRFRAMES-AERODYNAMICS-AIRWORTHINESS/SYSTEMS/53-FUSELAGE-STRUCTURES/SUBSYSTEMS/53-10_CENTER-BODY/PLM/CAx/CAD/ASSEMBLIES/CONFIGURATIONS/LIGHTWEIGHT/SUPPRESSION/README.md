# SUPPRESSION — Feature and Component Suppression States

## Purpose

This directory contains suppression state files that define which features, components, or sub-assemblies are suppressed in lightweight configurations.

## Contents

### Suppression State Files
- **Component suppression**: Lists of components to suppress
- **Feature suppression**: Lists of features to suppress
- **Conditional suppression**: Rules-based suppression criteria
- **Suppression sets**: Predefined suppression combinations

## Naming Convention

Use the following pattern:
```
53-10_SUPP_<assembly-name>_<suppression-type>_<version>.<ext>
```

Examples:
- `53-10_SUPP_CENTER-BODY_fasteners_v01.txt`
- `53-10_SUPP_FRAME-SECTION_internal-details_v02.csv`
- `53-10_SUPP_SKIN-PANEL_small-features_v01.xml`

## Suppression Categories

### Component-Level Suppression
Items typically suppressed:
- **Fasteners**: Screws, rivets, bolts (except critical interfaces)
- **Internal details**: Hidden components not affecting external envelope
- **Non-structural items**: Cable clips, brackets, minor fittings
- **Duplicate instances**: Repeated patterns (keep representative samples)

### Feature-Level Suppression
Features typically suppressed:
- **Small fillets**: < 2mm radius
- **Chamfers**: < 1mm size
- **Cosmetic threads**: Internal/external threads
- **Text/engravings**: Part numbers, logos
- **Construction geometry**: Reference planes, sketches, axes

### Conditional Suppression
Suppression based on:
- View distance (LOD - Level of Detail)
- Analysis type (visual vs. structural)
- User role (designer vs. reviewer)
- Performance requirements

## File Formats

### Text Format (.txt)
```
# Component suppression list
# Format: ComponentID, SuppressionState (0=unsuppressed, 1=suppressed)
FASTENER_001, 1
FASTENER_002, 1
BRACKET_SMALL_01, 1
```

### CSV Format (.csv)
```csv
ComponentID,PartName,SuppressionState,Reason
FAST_001,Rivet_4mm,1,Non-critical fastener
BRKT_012,Cable_Clip,1,Internal detail
FILL_023,Fillet_1mm,1,Small feature
```

### XML Format (.xml)
```xml
<SuppressionState>
  <Assembly name="53-10_CENTER-BODY">
    <Component id="FAST_001" suppress="true" reason="Non-critical"/>
    <Feature id="FILLET_023" suppress="true" reason="Small feature"/>
  </Assembly>
</SuppressionState>
```

## Best Practices

### Creating Suppression States
1. Start from full assembly
2. Identify non-essential components
3. Test suppression (verify constraints)
4. Document suppression rationale
5. Validate mass properties and interfaces

### Maintaining Suppression States
- Keep suppression states version-controlled
- Document changes in commit messages
- Review suppression states quarterly
- Update when assembly structure changes

## Validation Requirements

Before applying suppression, verify:
- Assembly constraints remain valid
- External interfaces are preserved
- Mass properties within ±5% tolerance
- Critical dimensions maintained
- No broken references

## Related Directories

- **Assembly files**: [`../ASM/`](../ASM/)
- **Configuration rules**: [`../RULES/`](../RULES/)
- **View states**: [`../VIEW_STATES/`](../VIEW_STATES/)
- **Documentation**: [`../DOCS/`](../DOCS/)
