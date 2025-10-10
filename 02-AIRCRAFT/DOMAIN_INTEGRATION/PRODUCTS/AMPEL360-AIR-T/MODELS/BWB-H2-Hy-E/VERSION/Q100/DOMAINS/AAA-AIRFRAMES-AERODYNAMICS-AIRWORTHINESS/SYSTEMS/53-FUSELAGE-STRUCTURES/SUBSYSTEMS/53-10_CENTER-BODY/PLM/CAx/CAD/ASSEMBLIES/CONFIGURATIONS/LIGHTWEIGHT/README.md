# LIGHTWEIGHT — Lightweight Assembly Configurations

## Purpose

This directory contains lightweight assembly configurations optimized for performance, file size, and system responsiveness while maintaining design fidelity.

## Contents

### Lightweight Model Types
- **Graphics-optimized models**: Reduced tessellation and display quality
- **Suppressed feature models**: Non-essential features suppressed
- **Display state models**: Optimized visualization states
- **Performance models**: Fast-loading configurations

## Optimization Techniques

### Graphics Optimization
- Reduced polygon count (tessellation)
- Simplified display quality
- Optimized edge rendering
- Reduced texture resolution

### Feature Management
- Suppress non-visible features
- Simplify pattern instances
- Use reference representations
- Defer loading of sub-assemblies

### Memory Optimization
- Shared geometry instances
- Reduced precision where acceptable
- Compressed file formats
- Lazy loading strategies

## Naming Convention

Use the following pattern:
```
53-10_ASM_<assembly-name>_LW_<version>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_LW_v01.CATProduct`
- `53-10_ASM_FRAME-SECTION_LW_v02.asm`
- `53-10_ASM_WING-ATTACH_LW_v01.sldasm`

## Use Cases

### Design Work
- Faster assembly loading
- Improved CAD performance
- Reduced memory usage
- Smoother navigation

### Collaboration
- Easier file sharing
- Faster network transfers
- Web-based viewing
- Remote collaboration sessions

### Large Assemblies
- System-level integration work
- Multi-subsystem assemblies
- Aircraft-level models
- Configuration management

## Performance Targets

Lightweight models should achieve:
- File size reduction: 50-70%
- Load time reduction: 40-60%
- Memory usage reduction: 30-50%
- Visual fidelity: 85-95% of original

## Quality Assurance

Lightweight models must:
- Maintain accurate external interfaces
- Preserve critical dimensions
- Retain mass properties (±5%)
- Keep coordinate system references
- Document optimization applied

## Related Directories

- **Simplified models**: [`../SIMPLIFIED/`](../SIMPLIFIED/)
- **Full assemblies**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)
- **References**: [`../../REFERENCES/`](../../REFERENCES/)
