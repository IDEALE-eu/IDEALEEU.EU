# RASTER — Raster Format Illustrations

## Purpose

This directory contains **raster format illustrations** for S1000D Data Modules in the 21-10 Radiators & Heat Exchangers subsystem. Raster graphics are used for photographs, complex renderings, and images not suitable for vector format.

## Contents

- **PNG files** (Portable Network Graphics) — Primary format
- **JPG/JPEG files** (Joint Photographic Experts Group) — Photographic images
- Photographs of hardware
- 3D renderings and visualizations
- Thermal imagery (infrared)
- Inspection photographs
- As-built documentation photos
- Screen captures from analysis tools

## File Naming Convention

Follow S1000D ICN (Illustration Control Number) format:
```
ICN-AMPEL360-2110-00000-001-01.png
ICN-AMPEL360-2110-00000-001-01.jpg
```

Where:
- `AMPEL360`: Model Identification Code
- `2110`: System Code
- `00000`: Figure number
- `001`: Sheet number
- `01`: Variant

## Supported Formats

### PNG (Portable Network Graphics)
- **Preferred format** for technical illustrations
- Lossless compression
- Supports transparency
- Suitable for diagrams, screenshots, technical images

### JPEG (Joint Photographic Experts Group)
- **Use for photographs only**
- Lossy compression
- Smaller file sizes
- Good for photographic content

## Illustration Types

### Photographs
- Hardware as-built photos
- Component identification photos
- Inspection and damage documentation
- Installation verification photos
- Test setup documentation

### Renderings
- 3D CAD model renderings
- Cutaway views
- Exploded views from CAD
- Thermal analysis visualizations

### Thermal Imagery
- Infrared camera images
- Temperature distribution maps
- Hot spot identification
- Thermal performance validation

### Analysis Results
- FEA stress plots
- CFD thermal simulation results
- Test data graphs and charts
- Performance curves

## Quality Requirements

### Resolution
- **Minimum**: 150 DPI at intended display size
- **Standard**: 300 DPI for print quality
- **Web display**: 96-150 DPI acceptable

### File Size
- **PNG**: Optimize, target < 2 MB per image
- **JPEG**: Use appropriate quality (80-95%)
- **Large files**: Consider reducing resolution

### Color
- **Color space**: sRGB for web display
- **Bit depth**: 24-bit color (8 bits per channel)
- **Grayscale**: 8-bit for B&W images

## Creation Guidelines

**DO**:
- Use adequate lighting for photographs
- Ensure sharp focus and clarity
- Include scale references where appropriate
- Crop to relevant content only
- Apply appropriate resolution
- Optimize file size for delivery

**DO NOT**:
- Over-compress JPEGs (quality < 80%)
- Include excessive background/clutter
- Use poor lighting or focus
- Include proprietary/sensitive information
- Exceed reasonable file sizes

## Photography Standards

- **Lighting**: Even, shadow-free illumination
- **Background**: Neutral, uncluttered
- **Focus**: Sharp on subject
- **Framing**: Include all relevant features
- **Scale**: Include reference (ruler, coin) if needed
- **Orientation**: Correct, not rotated

## Image Processing

Acceptable processing:
- Cropping to relevant area
- Brightness/contrast adjustment
- Color correction
- Sharpening (moderate)
- Red-eye removal (for personnel photos)
- Watermark/annotation addition

Prohibited processing:
- Content removal or addition
- Misleading alterations
- Excessive filtering
- Merging unrelated images

## Metadata Requirements

Include in file metadata:
- **Title**: Descriptive caption
- **Date**: When photograph/image was created
- **Author**: Photographer or creator
- **Copyright**: Ownership information
- **Description**: Brief description of content

## Review Requirements

Before publishing:
- [ ] Image quality acceptable
- [ ] Resolution appropriate
- [ ] File size optimized
- [ ] No sensitive information visible
- [ ] Proper orientation and framing
- [ ] Metadata complete

## Related Directories

- **[../vector/](../vector/)** — Vector format illustrations
- **[../../dm/](../../dm/)** — Data Modules using illustrations
- **[../../delivery/](../../delivery/)** — Final IETP packages

---

**Last Updated**: 2025-10-11
