# VECTOR — Vector Format Illustrations

## Purpose

This directory contains **vector format illustrations** for S1000D Data Modules in the 21-10 Radiators & Heat Exchangers subsystem. Vector graphics provide scalable, high-quality images for technical documentation.

## Contents

- **SVG files** (Scalable Vector Graphics) — Primary format
- **CGM files** (Computer Graphics Metafile) — S1000D standard format
- Exploded view diagrams
- Assembly/disassembly illustrations
- System schematics and diagrams
- Component callout drawings
- Cutaway and section views

## File Naming Convention

Follow S1000D ICN (Illustration Control Number) format:
```
ICN-AMPEL360-2110-00000-001-01.svg
ICN-AMPEL360-2110-00000-001-01.cgm
```

Where:
- `AMPEL360`: Model Identification Code
- `2110`: System Code
- `00000`: Figure number
- `001`: Sheet number
- `01`: Variant

## Supported Formats

### SVG (Scalable Vector Graphics)
- **Preferred format** for creation and editing
- Open standard, widely supported
- Can be edited with vector graphics tools
- Easily converted to other formats

### CGM (Computer Graphics Metafile)
- **S1000D standard format**
- Required for IETP delivery
- Binary or clear text encoding
- ATA 2100 compliant

## Illustration Types

### Exploded Views
- Component identification
- Assembly relationships
- Exploded parts diagrams for IPD

### Procedural Illustrations
- Step-by-step procedure support
- Before/after views
- Tool usage illustrations
- Safety zone markings

### Schematic Diagrams
- Functional flow diagrams
- Thermal circuit diagrams
- Interface connection diagrams

### Detail Views
- Callout details
- Section views
- Magnified critical areas

## Quality Requirements

- **Resolution**: Vector (scalable)
- **Colors**: Use standard S1000D color palette
- **Layers**: Organize by function (base, callouts, highlights)
- **Text**: Use standard fonts, readable at various scales
- **Callouts**: Clear, numbered, match Data Module references
- **File size**: Optimize for web delivery

## Creation Guidelines

**DO**:
- Use consistent line weights and styles
- Apply standard callout conventions
- Include scale references where appropriate
- Embed fonts or convert to paths
- Optimize file size for web use
- Version control illustration updates

**DO NOT**:
- Include raster elements (use raster directory)
- Use proprietary formats as final delivery
- Include excessive detail that obscures purpose
- Use non-standard colors or symbols

## Illustration Standards

- **ATA iSpec 2200**: Illustration conventions
- **S1000D Issue 6.0**: ICN structure and metadata
- **ASD-STE-100**: Text and labeling
- **ISO 128**: Technical drawing standards

## Software Tools

- **Adobe Illustrator**: Industry standard
- **Inkscape**: Open source alternative
- **CorelDRAW**: Professional vector editor
- **Arbortext IsoDraw**: Technical illustration specialist

## Review Requirements

Before publishing:
- [ ] Callouts match Data Module references
- [ ] All parts clearly identified
- [ ] Scale and orientation correct
- [ ] Colors consistent with standards
- [ ] File format compliant (SVG/CGM)
- [ ] Metadata complete

## Conversion Process

SVG to CGM conversion:
1. Validate SVG structure
2. Convert using S1000D-compliant tools
3. Verify CGM rendering
4. Check metadata preservation
5. Archive both formats

## Related Directories

- **[../raster/](../raster/)** — Raster format illustrations
- **[../../dm/](../../dm/)** — Data Modules using illustrations
- **[../../pm/](../../pm/)** — Publication modules

---

**Last Updated**: 2025-10-11
