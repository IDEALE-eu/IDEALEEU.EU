# OBSOLETE — Obsolete and Superseded Parts

## Purpose

This directory archives CAD part files that have been superseded by newer revisions or discontinued. Parts in OBSOLETE/ are retained for historical reference, traceability, and to support legacy configurations but are not authorized for new designs or manufacturing.

## Usage

### Archive Purpose
Parts in OBSOLETE/ are:
- **Superseded**: Replaced by newer revision
- **Discontinued**: No longer in use in current design
- **Historical reference**: Maintained for traceability and lessons learned
- **Not for production**: Do not use for manufacturing or procurement

### Retention Policy
- Maintain indefinitely for configuration history
- Include supersession information in metadata
- Reference successor part number if applicable

## File Organization

Organize obsolete parts with clear traceability:
- Retain original component type subdirectory structure
- Include supersession date and reason in metadata
- Reference ECO that obsoleted the part

Example structure:
```
OBSOLETE/
├─ FRAMES/
│  └─ 53-10_FRAME_F01_FWD_v01.CATPart (superseded by v02)
├─ STRINGERS/
│  └─ 53-10_STRINGER_STR-L01_v01.prt (superseded by v03)
└─ SKIN_PANELS/
   └─ 53-10_SKIN-PANEL_SP-001_v01.sldprt (design concept abandoned)
```

## Metadata Requirements

Obsolete parts must include:
- **Obsolete date**: When part was superseded or discontinued
- **Superseded by**: Part number of replacement (if applicable)
- **Reason**: Why part was obsoleted
- **ECO reference**: Change order that authorized obsolescence
- **Last used**: Final assembly or aircraft serial number using this part

## Naming Convention

Retain original part naming, optionally add `_OBSOLETE` suffix:
```
53-10_<component>_<part-number>_<description>_<revision>_OBSOLETE.<ext>
```

Examples:
- `53-10_FRAME_F01_FWD_v01_OBSOLETE.CATPart`
- `53-10_STRINGER_STR-L05_v02_OBSOLETE.prt`

## Supersession Process

When superseding a part:
1. Release new revision via ECO
2. Move superseded revision from [`../RELEASED/`](../RELEASED/) to OBSOLETE/
3. Update metadata with supersession information
4. Document in ECO which assemblies are affected
5. Update assembly models to reference new revision
6. Notify affected stakeholders

## Access and Usage

### Viewing Obsolete Parts
- Permitted for reference and historical research
- Useful for understanding design evolution
- Required for supporting legacy configurations

### Prohibited Actions
- Do not use obsolete parts in new designs
- Do not manufacture or procure obsolete parts
- Do not reference in new assemblies or drawings
- Exception: Spare parts for legacy aircraft (with approval)

## Cross-References

- **Current released parts**: [`../RELEASED/`](../RELEASED/)
- **Work in progress**: [`../WIP/`](../WIP/)
- **Component directories**: See parent [`../README.md`](../README.md)
- **ECO records**: Reference configuration management system

## Legacy Support

For spare parts or repairs on legacy aircraft:
1. Verify serial number applicability
2. Check if current revision can be substituted
3. If obsolete part required, obtain special approval
4. Document use in aircraft maintenance records
