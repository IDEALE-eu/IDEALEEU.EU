# METADATA — Model Metadata and Attribute Definitions

## Purpose

This directory contains metadata schemas, material specifications, and attribute definitions that are used to annotate and classify CAD models for the 53-10 Center Body. Proper metadata enables search, configuration management, and lifecycle tracking.

## Organization

Metadata is organized by type:

- **MATERIALS/** — Material specifications and properties
- **ATTRIBUTES/** — Model attributes, tags, and classification schemas

## Naming Convention

Use the following pattern for metadata files:
```
53-10_META_<TYPE>_<DESCRIPTION>_v<VERSION>.<ext>
```

Examples:
- `53-10_META_MATERIAL_ALUMINUM-ALLOYS_v01.json`
- `53-10_META_ATTR_SCHEMA_PARTS_v02.yaml`
- `53-10_META_MATERIAL_COMPOSITES_v01.csv`

## MATERIALS Directory

Contains material specifications including:
- **Material properties**: Density, modulus, yield strength, ultimate strength
- **Material forms**: Sheet, plate, extrusion, forging, casting
- **Heat treatments**: Temper designations and properties
- **Surface treatments**: Anodize, prime, paint specifications
- **Suppliers**: Approved material suppliers and forms
- **Certifications**: Required material certifications

File formats:
- `.json` — Structured material data
- `.yaml` — Hierarchical material definitions
- `.csv` — Material property tables
- `.pdf` — Material specifications and datasheets

Example materials:
- Aluminum alloys (2024-T3, 7075-T6, 7050-T7451)
- Titanium alloys (Ti-6Al-4V)
- Steels (AISI 4340, 15-5PH)
- Composites (CFRP, GFRP layup schedules)

## ATTRIBUTES Directory

Contains attribute schemas including:
- **Part classification**: Type, category, function
- **Lifecycle status**: Draft, Released, Obsolete
- **Configuration**: Baseline, variant, effectivity
- **Manufacturing**: Process, tooling requirements
- **Quality**: Inspection level, special processes
- **Supply chain**: Make/buy, supplier, lead time

File formats:
- `.json` — Attribute schemas
- `.yaml` — Hierarchical attributes
- `.xml` — CAD-system-specific schemas
- `.csv` — Attribute lists and tables

## Standard Attributes

Required attributes for all models:
- **part_number**: Unique identifier
- **revision**: Version/revision letter
- **title**: Part name/description
- **material**: Material specification
- **mass**: Calculated mass in kg
- **author**: Designer ID
- **status**: Lifecycle status
- **effectivity**: Configuration applicability

## Usage

CAD models must:
- Include required metadata in model properties
- Reference material definitions from MATERIALS/
- Use attribute schemas from ATTRIBUTES/
- Keep metadata synchronized with PLM system

## Integration

Metadata integrates with:
- **CAD models**: [`../PARTS/`](../PARTS/) and [`../SUBCOMPONENTS/`](../SUBCOMPONENTS/)
- **Configuration**: [`../CONFIG/`](../CONFIG/)
- **Quality checks**: [`../CHECKS/`](../CHECKS/)
- **PLM system**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)

## Related Documentation

- **Material standards**: [`../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/`](../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/)
- **Configuration management**: [`../../../../../../../../00-PROGRAM/CONFIG_MGMT/`](../../../../../../../../00-PROGRAM/CONFIG_MGMT/)
- **Quality requirements**: [`../../../../../../../../00-PROGRAM/QUALITY/`](../../../../../../../../00-PROGRAM/QUALITY/)

## Maintenance

Metadata files are controlled:
- Updates require engineering approval
- Changes communicated to design team
- Synchronized with PLM system
- Archived versions maintained
