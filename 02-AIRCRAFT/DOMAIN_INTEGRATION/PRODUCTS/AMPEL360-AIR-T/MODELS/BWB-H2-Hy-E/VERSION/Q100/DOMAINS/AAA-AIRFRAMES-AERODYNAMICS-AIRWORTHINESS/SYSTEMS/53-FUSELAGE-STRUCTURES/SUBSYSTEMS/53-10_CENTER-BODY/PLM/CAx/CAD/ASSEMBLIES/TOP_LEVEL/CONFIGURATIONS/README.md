# CONFIGURATIONS — Assembly Configurations

## Purpose

This directory contains different configuration variants of the top-level assembly for various purposes.

## Configuration Types

### Available Configurations
- **[SIMPLIFIED/](./SIMPLIFIED/)** — Simplified models for design reviews
- **[LIGHTWEIGHT/](./LIGHTWEIGHT/)** — Lightweight models for performance
- **[REVIEW/](./REVIEW/)** — Review configurations for stakeholder presentations

## Configuration Management

### Configuration Uses
- **Design reviews**: Simplified geometry for faster visualization
- **Analysis preparation**: Lightweight models for CAE preprocessing
- **Manufacturing planning**: Specific build configurations
- **Documentation**: Configurations for technical publications

## Configuration Features

### Simplified Configurations
- Removed or suppressed small features
- Combined similar components
- Envelope representations
- Reduced polygon count

### Lightweight Configurations
- Suppressed internal components
- Simplified fasteners
- Reduced detail level
- Optimized graphics representation

### Review Configurations
- Key features visible
- Color-coded by system
- Annotations and callouts
- Progressive detail levels

## File Management

Each configuration may include:
- Configuration-specific assembly files
- Display state definitions
- Suppression lists
- Layer/level organization

## Naming Convention

```
53-10_ASM_CENTER-BODY_<config>_<version>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_SIMPLIFIED_v01.CATProduct`
- `53-10_ASM_CENTER-BODY_LIGHTWEIGHT_v01.prt`
- `53-10_ASM_CENTER-BODY_REVIEW_v01.sldasm`

## Best Practices

- Maintain **configuration consistency** across CAD systems
- Document **what is suppressed** in each configuration
- Use **design tables** or configuration files where possible
- **Test configurations** for validity before committing

## Related Directories

- **Assembly**: [`../ASM/`](../ASM/) — Master assembly with all configurations
- **Exports**: [`../EXPORTS/`](../EXPORTS/) — Neutral format exports of configurations
