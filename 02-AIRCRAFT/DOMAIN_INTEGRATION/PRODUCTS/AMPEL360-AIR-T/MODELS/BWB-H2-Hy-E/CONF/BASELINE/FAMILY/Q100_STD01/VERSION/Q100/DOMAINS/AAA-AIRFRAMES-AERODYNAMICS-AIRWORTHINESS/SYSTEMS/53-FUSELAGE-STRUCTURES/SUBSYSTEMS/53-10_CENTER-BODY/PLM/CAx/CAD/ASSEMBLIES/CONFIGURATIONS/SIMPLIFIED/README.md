# SIMPLIFIED — Simplified Assembly Configurations

## Purpose

This directory contains simplified assembly models with reduced detail for design reviews, presentations, and preliminary analysis.

## Contents

This directory is organized into the following subdirectories:

### Directory Structure
- **[ASM/](./ASM/)** — Simplified assembly model files
- **[PARTS/](./PARTS/)** — Simplified component parts
- **[RULES/](./RULES/)** — Simplification rules and guidelines
- **[SUPPRESSION/](./SUPPRESSION/)** — Feature suppression records
- **[VIEW_STATES/](./VIEW_STATES/)** — Saved display configurations
- **[EXPORTS/](./EXPORTS/)** — Neutral format exports
- **[DOCS/](./DOCS/)** — Approval and validation documentation
- **[INDEX/](./INDEX/)** — Model registry and tracking

### Simplified Model Types
- **Design review models**: Reduced detail for stakeholder reviews
- **Conceptual models**: Early-stage design representations
- **Envelope models**: Boundary and interface representations
- **Presentation models**: Marketing and communication visuals

## Simplification Techniques

### Geometry Simplification
- Remove internal features (fillets, chamfers, small holes)
- Combine multiple parts into single bodies
- Use envelopes instead of detailed components
- Represent complex assemblies with simplified proxies

### Feature Suppression
- Suppress non-critical features
- Hide internal components
- Remove fastener details
- Simplify surface finishes

### Level of Detail
- LOD1: Envelope only (outer boundary)
- LOD2: Major components simplified
- LOD3: Moderate detail for review
- LOD4: Full detail (reference only)

## Naming Convention

Use the following pattern:
```
53-10_ASM_<assembly-name>_SIMP_LOD<level>_<version>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_SIMP_LOD1_v01.CATProduct`
- `53-10_ASM_FRAME-SECTION_SIMP_LOD2_v02.asm`
- `53-10_ASM_WING-ATTACH_SIMP_LOD3_v01.sldasm`

## Use Cases

### Executive Reviews
- High-level design overview
- Strategic decision making
- Program milestone reviews

### Stakeholder Presentations
- Customer presentations
- Supplier briefings
- Regulatory submissions

### Early Analysis
- Preliminary mass estimates
- Rough clearance checks
- Concept validation

## Documentation Requirements

Each simplified model should document:
- Level of simplification applied
- Reference to detailed baseline
- Limitations and restrictions
- Intended use case
- Approval for use

## Related Directories

- **Lightweight models**: [`../LIGHTWEIGHT/`](../LIGHTWEIGHT/)
- **Full assemblies**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)
- **References**: [`../../REFERENCES/`](../../REFERENCES/)
