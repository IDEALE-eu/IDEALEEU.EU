# RULES — Configuration Rules and Scripts

## Purpose

This directory contains configuration rules, scripts, and automation files that define how lightweight configurations are created and maintained.

## Contents

### Rule Types
- **Suppression rules**: Define which features/components to suppress
- **Display rules**: Define visualization settings and quality
- **Simplification rules**: Define geometry simplification parameters
- **Loading rules**: Define deferred loading and lazy loading strategies

### File Formats
- **XML/JSON**: Configuration definition files
- **Scripts**: Automation scripts (Python, VBA, API scripts)
- **Templates**: Rule templates for different model types

## Naming Convention

Use the following pattern:
```
53-10_RULE_<rule-type>_<description>_<version>.<ext>
```

Examples:
- `53-10_RULE_SUPPRESSION_non-visible-features_v01.xml`
- `53-10_RULE_DISPLAY_low-tessellation_v02.json`
- `53-10_RULE_SIMPLIFICATION_small-features_v01.py`

## Rule Categories

### Suppression Rules
Define criteria for suppressing:
- Construction geometry
- Small features (< 2mm)
- Internal components
- Fastener details

### Display Rules
Define settings for:
- Tessellation quality (coarse/fine)
- Edge display (visible/hidden)
- Shading mode
- Texture resolution

### Performance Rules
Define strategies for:
- Memory management
- File size reduction
- Load time optimization
- Graphics performance

## Validation

Rules must be validated to ensure:
- Interface geometry is preserved
- Critical dimensions are maintained
- Mass properties are within tolerance
- No assembly constraints are broken

## Related Directories

- **Assembly files**: [`../ASM/`](../ASM/)
- **Suppression states**: [`../SUPPRESSION/`](../SUPPRESSION/)
- **View states**: [`../VIEW_STATES/`](../VIEW_STATES/)
- **Documentation**: [`../DOCS/`](../DOCS/)
