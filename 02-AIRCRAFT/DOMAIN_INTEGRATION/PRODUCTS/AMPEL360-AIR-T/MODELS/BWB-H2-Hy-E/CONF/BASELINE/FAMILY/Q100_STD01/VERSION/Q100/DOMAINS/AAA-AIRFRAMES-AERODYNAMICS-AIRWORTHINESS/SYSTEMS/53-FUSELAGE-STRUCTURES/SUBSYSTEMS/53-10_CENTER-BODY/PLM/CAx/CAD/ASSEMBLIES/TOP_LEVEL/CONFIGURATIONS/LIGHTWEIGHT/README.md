# LIGHTWEIGHT — Lightweight Configuration

## Purpose

This directory contains lightweight assembly configurations optimized for graphics performance and reduced memory usage.

## Optimization Features

### Graphics Optimization
- **Reduced polygon count**: Simplified tessellation
- **Level of detail (LOD)**: Progressive detail based on zoom
- **Hidden component suppression**: Internal parts not shown
- **Texture/appearance reduction**: Minimal visual attributes

### Use Cases
- **Large assembly reviews**: When full model is too heavy
- **CAE preprocessing**: Starting point for analysis models
- **Collaboration**: Sharing with external partners
- **Mobile/web viewing**: Lightweight formats for remote access

## Optimization Techniques

### Component Level
- Suppress internal components
- Use bounding box representations
- Remove small parts (< 5mm)
- Simplify curved surfaces

### Assembly Level
- Use assembly envelopes
- Suppress sub-assemblies
- Reduce mate complexity
- Optimize display states

## File Types

- `.JT` — Lightweight visualization format
- `.stp` (simplified) — Reduced STEP export
- `.3dxml` — 3D visualization format
- `.glb`/`.gltf` — Web-ready 3D formats

## Naming Convention

```
53-10_ASM_CENTER-BODY_LIGHTWEIGHT_<version>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_LIGHTWEIGHT_v01.jt`
- `53-10_ASM_CENTER-BODY_LIGHTWEIGHT_v01.glb`

## Performance Targets

- **File size**: < 10% of full model
- **Load time**: < 10 seconds
- **Graphics FPS**: > 30 fps on standard hardware
- **Memory usage**: < 2 GB RAM

## Quality Validation

Verify:
- [ ] Overall dimensions correct
- [ ] Key features visible
- [ ] Interface locations accurate
- [ ] Acceptable visual quality
- [ ] Performance targets met

## Related Configurations

- **Simplified**: [`../SIMPLIFIED/`](../SIMPLIFIED/) — Design review configurations
- **Review**: [`../REVIEW/`](../REVIEW/) — Presentation configurations
