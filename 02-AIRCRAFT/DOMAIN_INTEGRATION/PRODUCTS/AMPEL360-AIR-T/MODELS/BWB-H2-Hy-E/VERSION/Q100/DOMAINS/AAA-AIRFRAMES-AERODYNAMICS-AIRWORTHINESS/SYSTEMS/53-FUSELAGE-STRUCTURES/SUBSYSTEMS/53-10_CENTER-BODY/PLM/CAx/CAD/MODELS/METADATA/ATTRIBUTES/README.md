# ATTRIBUTES — Model Attributes and Classification Schemas

## Purpose

Attribute schemas and classification definitions for annotating CAD models with metadata.

## Content

### Attribute Categories
- Part classification (type, category, function)
- Lifecycle status (Draft, Released, Obsolete)
- Configuration (baseline, variant, effectivity)
- Manufacturing (process, tooling requirements)
- Quality (inspection level, special processes)
- Supply chain (make/buy, supplier, lead time)

## Standard Attributes

Required for all models:
- `part_number` — Unique identifier
- `revision` — Version/revision letter
- `title` — Part name/description
- `material` — Material specification
- `mass` — Calculated mass in kg
- `author` — Designer ID
- `status` — Lifecycle status
- `effectivity` — Configuration applicability

## File Formats

- `.json` — Attribute schemas
- `.yaml` — Hierarchical attribute definitions
- `.xml` — CAD-system-specific schemas
- `.csv` — Attribute lists

## Naming Convention

```
53-10_META_ATTR_<SCHEMA>_v<VERSION>.<ext>
```

Examples:
- `53-10_META_ATTR_SCHEMA_PARTS_v01.json`
- `53-10_META_ATTR_LIFECYCLE_v02.yaml`
