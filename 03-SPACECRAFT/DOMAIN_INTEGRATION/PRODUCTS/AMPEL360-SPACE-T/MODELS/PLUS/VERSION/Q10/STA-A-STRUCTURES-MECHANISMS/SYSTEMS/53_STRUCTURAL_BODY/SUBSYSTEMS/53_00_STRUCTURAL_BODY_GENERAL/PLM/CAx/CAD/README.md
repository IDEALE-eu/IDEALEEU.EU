# CAD for 53_00_STRUCTURAL_BODY_GENERAL

## Purpose

This directory contains Computer-Aided Design (CAD) engineering artifacts for the 53_00 Structural Body General subsystem, including 3D models, assemblies, drawings, and neutral format exports.

## Directory Structure

```
CAD/
├── ASSEMBLIES/          # Assembly models and configurations
│   ├── CONFIGURATIONS/  # Simplified and lightweight variants
│   ├── DOCS/           # BOMs, ICDs, and assembly sequences
│   ├── FIXTURES/       # Assembly and inspection tooling
│   ├── INSTALLATION/   # Installation assemblies
│   ├── REFERENCES/     # Coordinate systems and reference planes
│   ├── SUB_ASSEMBLIES/ # Sub-assembly models
│   ├── TEST/           # Test article assemblies
│   └── TOP_LEVEL/      # Complete system assemblies
├── DRAWINGS/           # 2D engineering drawings
├── EXPORTS/            # Neutral format exports (STEP, IGES, JT, DXF)
├── MODELS/             # Native CAD model files
├── PARTS/              # Individual part files
└── TEMPLATES/          # CAD templates and standards
```

## Main Directories

### [ASSEMBLIES/](./ASSEMBLIES/)
Assembly models combining multiple components into integrated structures:
- Top-level and sub-assemblies
- Configuration variants (simplified, lightweight)
- Installation and test assemblies
- Assembly fixtures and tooling
- Reference geometry and coordinate systems
- Documentation (BOMs, ICDs, assembly sequences)

### [DRAWINGS/](./DRAWINGS/)
2D engineering drawings with dimensions, tolerances, and specifications:
- Part drawings
- Assembly drawings
- Installation drawings
- Interface control drawings

### [EXPORTS/](./EXPORTS/)
Neutral format exports for data exchange and archival:
- **STEP/**: Primary 3D exchange format (ISO 10303-242)
- **IGES/**: Legacy 3D format for compatibility
- **JT/**: Lightweight visualization format (ISO 14306)
- **DXF/**: 2D drawings and profiles

### [MODELS/](./MODELS/)
Native CAD model files:
- Part files in native CAD formats
- Parametric models with design history
- Reference geometry

### [PARTS/](./PARTS/)
Individual component CAD files organized by type:
- Structural components (frames, stringers, skins)
- Interface fittings and mounts
- Detail parts (brackets, clips, doublers)
- Standard parts and fasteners

### [TEMPLATES/](./TEMPLATES/)
Reusable CAD templates and standards:
- Part and assembly templates
- Drawing templates with title blocks
- Material libraries
- Standard parts library
- Design standards and conventions

## Naming Conventions

### Parts
```
53_00_<component-type>_<part-number>_<description>_<version>.<ext>
```

### Assemblies
```
53_00_ASM_<assembly-name>_<version>.<ext>
```

### Drawings
```
53_00_DWG_<component>_<drawing-number>_<sheet>.<ext>
```

### Exports
```
53_00_<component>_<part-number>_<revision>_<date>.<ext>
```

## File Formats

### Native CAD Formats
- CATIA V5/V6: `.CATPart`, `.CATProduct`, `.CATDrawing`
- NX (Siemens): `.prt`
- SolidWorks: `.sldprt`, `.sldasm`, `.slddrw`
- Creo (PTC): `.prt`, `.asm`

### Neutral Formats
- STEP AP242: `.step` (primary 3D exchange)
- IGES 5.3: `.igs` (legacy 3D)
- JT: `.jt` (lightweight visualization)
- DXF: `.dxf` (2D geometry)
- PDF: `.pdf` (drawings)

## Best Practices

### Design Work
- Start from templates in [`TEMPLATES/`](./TEMPLATES/)
- Use consistent naming conventions
- Document design intent and parameters
- Include material specifications
- Export to neutral formats regularly

### Configuration Management
- Track revisions in file names and properties
- Link to EBOM in [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)
- Tag major milestones in Git
- Use Git LFS for files > 10 MB

### Quality Assurance
- Verify models rebuild without errors
- Calculate and document mass properties
- Export and validate neutral formats
- Create engineering drawings
- Perform design reviews

## Standards Compliance

Follow:
- **ECSS-E-ST-10C**: Space engineering standards
- **ECSS-E-ST-32C**: Structural design and verification
- **ISO 10303-242** (STEP AP242): CAD data exchange
- **ISO 14306** (JT): Visualization format
- **ASME Y14.5**: GD&T standards
- **AS9100**: Quality management for aerospace

## Related Documentation

- **Subsystem README**: [`../../README.md`](../../README.md)
- **EBOM Links**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)
- **Other CAx disciplines**: [`../`](../) (CAE, CAM, CAO, etc.)
- **Interface Matrix**: System-level interface definitions

## Support

For assistance with:
- **CAD tools and templates**: Contact CAD Administrator
- **Design standards**: Reference ECSS-E-ST-32C
- **Configuration management**: Contact CCB (Configuration Control Board)
- **Data exchange**: See [`EXPORTS/README.md`](./EXPORTS/README.md)
