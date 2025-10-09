# CONFIGURATIONS — Assembly Configuration Variants

## Purpose

This directory contains different configuration variants of assembly models for various purposes such as performance optimization, design reviews, and analysis.

## Contents

### Configuration Categories
- **[SIMPLIFIED/](./SIMPLIFIED/)** — Simplified assemblies for reviews and analysis
- **[LIGHTWEIGHT/](./LIGHTWEIGHT/)** — Lightweight configurations for performance

## Configuration Types

### Simplified Configurations
- Reduced detail for design reviews
- Simplified representations for stakeholder presentations
- Performance-optimized models for large assemblies
- Concept and preliminary design configurations

### Lightweight Configurations
- Graphics-optimized representations
- Reduced polygon count models
- Display states for performance
- Suppressed features for faster loading

## Use Cases

### Design Reviews
- Executive reviews with simplified geometry
- Stakeholder presentations
- Early-stage design evaluation
- Concept validation

### Performance Optimization
- Large assembly management
- Reduced computational load
- Faster file operations
- Improved CAD system performance

## Naming Convention

Use the following pattern:
```
53-10_ASM_<assembly-name>_<config-type>_<version>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_SIMPLIFIED_v01.CATProduct`
- `53-10_ASM_FRAME-SECTION_LIGHTWEIGHT_v02.asm`

## Configuration Requirements

Configuration variants should:
- Maintain external interfaces
- Preserve overall dimensions
- Document simplifications made
- Reference baseline assembly
- Maintain traceability

## Related Directories

- **Full assemblies**: [`../TOP_LEVEL/`](../TOP_LEVEL/)
- **Sub-assemblies**: [`../SUB_ASSEMBLIES/`](../SUB_ASSEMBLIES/)
- **References**: [`../REFERENCES/`](../REFERENCES/)
