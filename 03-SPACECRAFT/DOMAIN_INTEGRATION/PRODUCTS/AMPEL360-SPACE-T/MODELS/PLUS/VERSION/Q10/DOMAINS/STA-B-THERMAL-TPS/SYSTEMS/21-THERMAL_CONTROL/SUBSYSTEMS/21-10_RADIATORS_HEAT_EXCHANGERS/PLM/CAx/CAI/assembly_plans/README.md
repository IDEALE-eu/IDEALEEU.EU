# Assembly Plans — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Assembly plans define the overall integration sequence, kitting requirements, and coordination between work instructions for radiator, LPHX, and coldplate installations.

## Content Types

- **Master Assembly Plans** — Overall integration sequence and flow
- **Sequencing Documents** — Step dependencies and critical path
- **Kitting Plans** — Parts staging and readiness
- **Sign-off Sheets** — Approval checkpoints and gates

## File Formats

- `.pdf` — Controlled assembly plan documents
- `.xlsx` — Planning spreadsheets and checklists
- `.mpp` / `.gantt` — Schedule files (if applicable)

## Naming Convention

```
PLAN-21-10-{identifier}__{revision}.pdf
```

**Examples:**
- `PLAN-21-10-radiator_master_sequence__r01.pdf`
- `PLAN-21-10-lphx_integration_flow__r02.pdf`
- `PLAN-21-10-coldplate_install_order__r00.pdf`

## Assembly Plan Requirements

Each plan must include:
- **Scope** — Hardware assemblies covered
- **Flow Diagram** — Visual representation of assembly sequence
- **Predecessor Steps** — Dependencies and prerequisites
- **Duration Estimates** — Time allocation per operation
- **Resource Requirements** — Personnel, tools, facilities
- **Hold Points** — Required inspections and approvals
- **Risk Mitigation** — Critical operations and contingencies
- **Configuration Control** — Part traceability and as-built documentation

## Integration Sequence (Typical)

1. **Kitting & Prep:** Verify parts, cure adhesives, clean surfaces
2. **Dry-fit:** Check interfaces, shims, alignment without bond
3. **Bond/Torque:** Apply adhesive/TIM, clamp/torque per WI, cure log
4. **Inspect:** Flatness, gaps, torque check, leak port access
5. **Functional Test:** Continuity, leak sniff (if ports accessible)
6. **As-Run Log:** Record serials, shims, torques, deviations
7. **Handoff to Test:** CAV takes over for TVAC/leak/proof

## Cross-References

- [Parent: CAI](../README.md)
- [Work Instructions](../work_instructions/README.md)
- [Travelers](../travelers/README.md)
- [Kitting](../kitting/README.md)
- [MGSE](../mgse/README.md)
- [As-Run Records](../as_run_records/README.md)

## Standards & Constraints

- **Units:** mm, N·m, °C
- **Datums:** per 06-DIMENSIONS and 51-STRUCTURES
- **Torque:** per 51 fastener standards
- **Cleanliness:** NVR/particle per 21 cleanliness plan
- **ESD:** per ESD plan (STA-C)

## Revision Control

- Assembly plans maintained under configuration control
- Revisions coordinated with associated work instructions
- Changes require engineering review and approval
- Previous revisions archived with supersession notice
