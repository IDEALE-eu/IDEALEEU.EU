# JT — ISO 14306 JT Format Exports

## Purpose

This directory contains JT (ISO 14306) format exports for lightweight visualization and design review of spacecraft structural body models.

## Format Details

### JT (ISO 14306)
- **Full name**: Jupiter Tessellation format
- **Primary use**: Lightweight 3D visualization
- **Advantages**:
  - Fast loading of large assemblies
  - Reduced file sizes (50-90% smaller than native)
  - Suitable for web and mobile viewing
  - PLM system integration

## Export Settings

### Recommended Settings
- **Version**: Latest JT version supported
- **LOD**: Multiple levels of detail
- **Tessellation**: High quality for visualization
- **Assembly structure**: Maintain hierarchy
- **Attributes**: Include metadata

## Naming Convention

```
53_00_<component>_<part-number>_<revision>_<date>.jt
```

Examples:
- `53_00_ASM_STRUCTURAL-BODY_PN-10000_RevA_20250110.jt`
- `53_00_FRAME-SECTION_PN-20000_RevB_20250110.jt`

## Use Cases

### Design Reviews
- Share with stakeholders without CAD licenses
- Fast loading for large assemblies
- Web-based visualization
- Mobile device compatibility

### Collaboration
- Lightweight file transfer
- Mark-up and commenting
- Configuration comparison
- Design review documentation

## File Organization

Organize by:
- **Assembly level**: System, subsystem, component
- **Configuration**: Simplified, lightweight, full detail
- **Review purpose**: PDR, CDR, TRR variants

## Validation

Before committing JT files:
- [ ] File opens in JT viewer (e.g., JT2Go)
- [ ] Visual fidelity acceptable
- [ ] Assembly structure preserved
- [ ] File size reduced vs. native
- [ ] Metadata included

## Tools

- **JT2Go**: Free viewer from Siemens
- **Teamcenter Visualization**: PLM integration
- **Web viewers**: Various browser-based options

## Related Directories

- **Source CAD models**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/)
- **Full geometry**: [`../STEP/`](../STEP/) — For manufacturing use
