# LOD_LOW — Low Level of Detail Parts

## Purpose

Low level of detail (LOD) JT files for individual parts. These files contain simplified geometry optimized for:
- Fast loading and rendering
- Large assembly visualization
- Overview and navigation
- Web-based viewers

## What to Store

- Simplified part geometry
- Reduced polygon count (coarse tessellation)
- Essential shape representation
- Lightweight files for quick review

## Usage

Use low LOD parts when:
- Viewing large assemblies with many components
- Initial design reviews and overviews
- Performance is critical (web viewers, mobile)
- Detailed geometry is not required

## File Characteristics

- **File size**: Smallest (typically 10-100 KB per part)
- **Polygon count**: Low (coarse tessellation)
- **Detail level**: Basic shape only
- **Load time**: Fastest

## Related Directories

- [`../LOD_MED/`](../LOD_MED/) — Medium LOD parts
- [`../LOD_HIGH/`](../LOD_HIGH/) — High LOD parts
- [`../`](../) — PARTS directory
- [`../../README.md`](../../README.md) — JT format overview

## Best Practices

- Use for assembly visualization at aircraft level
- Maintain recognizable part shape despite simplification
- Balance file size vs. visual clarity
- Consider as default for large assembly exports
