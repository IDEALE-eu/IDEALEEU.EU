# DESIGN_RULES — Design Rules and Standards

## Purpose

Design rules, constraints, and standards that govern CAD model development for the center body.

## Content

- Minimum bend radii by material/thickness
- Edge distance requirements for fasteners
- Hole spacing and pattern rules
- Fillet and corner radii requirements
- Manufacturing process constraints
- Assembly clearance requirements
- Material thickness standards
- Fastener selection rules

## File Formats

- `.yaml` — Rule definitions
- `.json` — Machine-readable rules
- `.pdf` — Published rule documents
- `.md` — Human-readable documentation

## Naming Convention

```
53-10_CONFIG_RULES_<CATEGORY>_v<VERSION>.<ext>
```

Examples:
- `53-10_CONFIG_RULES_STRUCTURAL_v01.yaml`
- `53-10_CONFIG_RULES_FASTENERS_v02.json`

## Usage

All models must comply with design rules. Deviations require formal waiver process.
