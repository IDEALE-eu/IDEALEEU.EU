# TIER1 — Tier 1 Supplier Integration Packages

## Purpose

Integration data from Tier 1 suppliers providing major structural assemblies, systems, and sub-assemblies for the CENTER-BODY subsystem.

## Content Types

- **Assembly Drawings** — Supplier-provided assembly documentation
- **Interface Definitions** — Tier 1 to aircraft interfaces
- **Qualification Data** — Test reports and certifications
- **Manufacturing Data** — Process specifications and quality plans

## File Formats

- `.pdf` — Supplier documentation
- `.step` — 3D assembly models
- `.csv` — Part lists and schedules
- `.xlsx` — Test data and qual reports

## Naming Convention

```
TIER1_{supplier}_{assembly}_{type}_v{version}.{ext}
```

Examples:
- `TIER1_Spirit_center_fuselage_assy_v001.pdf`
- `TIER1_FACC_composite_panels_interface_v002.step`

## Cross-References

- [Parent: SUPPLIER_DATA](../README.md)
- [OEM Data](../OEM/README.md)
- [Mounting Provisions](../../MOUNTING/)
- [Interface Definitions](../../INTERFACES/)

## Tier 1 Integration Requirements

Major assemblies from Tier 1:
- Full structural analysis responsibility
- Interface control with aircraft
- Quality assurance and inspection
- Delivery of flight hardware
- Technical support and field service

## Typical Tier 1 Suppliers

| Assembly | Typical Supplier | Scope |
|----------|------------------|-------|
| Center fuselage | Spirit, Alenia | Complete barrel sections |
| Composite panels | FACC, GKN | Skin panels and components |
| Bulkheads | Premium AEROTEC | Machined structures |
| Floor structures | Triumph, ASCO | Floor beams and fittings |

## Data Package Requirements

- Assembly drawings (3D + 2D)
- Interface Control Documents
- Structural substantiation reports
- Manufacturing process specs
- Quality control plans
- First article inspection reports (AS9102)

## Change Control

Tier 1 changes require:
- Joint engineering review
- Bilateral ECO approval
- Re-qualification if affecting performance
- Update to aircraft integration data
