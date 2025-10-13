# SIMPLIFIED — Simplified Configuration

## Purpose

This directory contains simplified assembly configurations optimized for design reviews and quick visualization.

## Simplification Features

### Geometry Simplification
- **Removed details**: Small holes, fillets, chamfers removed
- **Combined features**: Multiple similar features merged
- **Envelope representations**: Complex parts shown as bounding boxes
- **Suppressed components**: Non-critical parts hidden

### Use Cases
- **Design reviews**: Fast loading for stakeholder presentations
- **Concept evaluation**: Focus on major structural elements
- **Interface reviews**: Show key interfaces without details
- **Documentation**: Technical illustrations and presentations

## Simplification Guidelines

### What to Remove
- Fastener holes and hardware
- Small radii and fillets
- Text and markings
- Internal structure (if not critical)
- Standard hardware

### What to Keep
- Overall envelope and dimensions
- Major structural components
- Interface features
- Critical fastener patterns
- Key reference geometry

## File Types

- Native CAD simplified assemblies
- Neutral format exports (STEP, JT)
- Visualization formats (JT, 3D PDF)

## Naming Convention

```
53-10_ASM_CENTER-BODY_SIMPLIFIED_<version>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_SIMPLIFIED_v01.CATProduct`
- `53-10_ASM_CENTER-BODY_SIMPLIFIED_v01.stp`

## Performance Targets

- **Load time**: < 30 seconds
- **File size**: < 50% of full model
- **Graphics performance**: Smooth rotation and zoom

## Related Configurations

- **Lightweight**: [`../LIGHTWEIGHT/`](../LIGHTWEIGHT/) — Performance-optimized models
- **Review**: [`../REVIEW/`](../REVIEW/) — Presentation configurations
