# Work Instructions — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Work Instructions (WI) for installation of radiator panels, LPHX, coldplates, mounts, and TIM/bondlines. These documents provide step-by-step procedures for assembly and integration operations.

## Content Types

- **Installation Procedures** — Step-by-step radiator panel installation
- **LPHX Integration** — Loop heat pipe heat exchanger mounting and connection
- **Coldplate Assembly** — Coldplate mounting and TIM application
- **Mount Installation** — Bracket and mount assembly procedures
- **TIM/Bondline Application** — Thermal interface material and adhesive application

## File Formats

- `.pdf` — Controlled work instruction documents
- `.docx` — Working drafts (WIP status only)

## Naming Convention

```
WI-21-10-{identifier}__{revision}__{status}.pdf
```

**Status Codes:**
- `WIP` — Work In Progress (draft)
- `RVW` — Under Review
- `REL` — Released (approved for use)

**Examples:**
- `WI-21-10-radiator_panel_install__r01__REL.pdf`
- `WI-21-10-lphx_mounting__r02__RVW.pdf`
- `WI-21-10-coldplate_tim_apply__r00__WIP.pdf`

## Work Instruction Requirements

Each WI must include:
- **Scope** — Applicable hardware and operations
- **Prerequisites** — Required completed steps, certs, training
- **Tools & Equipment** — Required MGSE, fixtures, torque wrenches
- **Materials** — Parts, adhesives, TIM, fasteners (ref to kitting)
- **Safety & ESD** — Hazards, PPE, ESD precautions
- **Procedure Steps** — Numbered steps with acceptance criteria
- **Inspection Points** — Hold points for QA verification
- **Sign-offs** — Mechanic, inspector, engineer approval blocks
- **Reference Documents** — Drawings, specs, torque tables

## Standards & Constraints

- **Units:** mm, N·m, °C
- **Datums:** per 06-DIMENSIONS and 51-STRUCTURES
- **Adhesives/cure:** parameters from CAP process specs
- **Torque:** per 51 fastener standards; mandatory witness and re-torque log
- **TIM thickness:** per CAD call-out; measure actual after clamp
- **Cleanliness:** NVR/particle per 21 cleanliness plan before closeout
- **ESD:** all electronics/heaters per ESD plan (STA-C)

## Typical WI Sequence

1. **Kitting & Prep:** Verify parts, cure adhesives, clean surfaces
2. **Dry-fit:** Check interfaces, shims, alignment without bond
3. **Bond/Torque:** Apply adhesive/TIM, clamp/torque per WI, cure log
4. **Inspect:** Flatness, gaps, torque check, leak port access
5. **Functional Test:** Continuity, leak sniff (if ports accessible)
6. **As-Run Log:** Record serials, shims, torques, deviations

## Cross-References

- [Parent: CAI](../README.md)
- [Assembly Plans](../assembly_plans/README.md)
- [Travelers](../travelers/README.md)
- [Torque Tables](../torque_tables/README.md)
- [Bondline](../bondline/README.md)
- [Kitting](../kitting/README.md)
- [MGSE](../mgse/README.md)
- [Inspection Checklists](../inspection_checklists/README.md)

## Revision Control

- Draft WIs (WIP) are maintained in working area
- Review WIs (RVW) require engineering review
- Released WIs (REL) require formal approval and configuration control
- All revisions tracked in document history table
- Obsolete revisions archived with clear supersession notice

## Change Control

WI changes require:
- Engineering review and approval
- Training update if procedure changes
- Notification to production and QA teams
- Update to associated travelers and assembly plans
- ECO if changes affect hardware configuration
