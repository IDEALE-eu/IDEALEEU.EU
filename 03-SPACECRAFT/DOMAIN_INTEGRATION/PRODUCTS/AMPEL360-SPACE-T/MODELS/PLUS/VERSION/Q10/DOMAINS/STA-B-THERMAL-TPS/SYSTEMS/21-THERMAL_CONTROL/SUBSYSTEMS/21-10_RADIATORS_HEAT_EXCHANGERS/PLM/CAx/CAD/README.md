# CAD · 21-10_RADIATORS_HEAT_EXCHANGERS

Purpose: authoritative 3D geometry and drawings for 21-10 radiators, embedded HP radiators, LPHX, coldplates, mounts, TIMs, and coating masks. No source code.

## Deliverables
- Parametric CAD models (assemblies/parts)
- Fully dimensioned drawings with GD&T
- PMI and mass properties
- Neutral exports (STEP AP242, IGES if needed, DXF for flat)
- Assembly BOM tables (for EBOM trace)

## Layout
```
CAD/
├─ assemblies/           # top-level assy models (RAD-PANEL, LPHX, COLDPLATE)
├─ parts/                # facesheets, cores, tubes, manifolds, fins, shims, TIMs
├─ drawings/             # *.pdf, *.dwg; release PDFs mandatory
├─ fixtures_tooling/     # drill templates, bonding nests
├─ coating_masks/        # paint/SSM masks, keep-out geometry
├─ exports_step/         # *.step AP242 (REL)
├─ exports_dxf/          # flat patterns
└─ templates/            # title block, GD&T, note packs
```

## Naming & revisions
`21-10_<object>__rNN__{WIP|RVW|REL}.<ext>`  
Examples: `21-10-ASSY-RAD-PANEL-L1__r03__RVW.step`, `21-10-PART-HONEYCOMB-CORE__r02__REL.prt`

## Modeling standards
- Units: mm, mass kg, angles deg.  
- Datums: A/B/C per 06 datums; mounting to 51 patterns.  
- Materials: from CAP material tables; apply properties for mass/CG.  
- Tolerances: ISO 2768-mK unless stated; GD&T per ISO 1101.  
- Surface finish: Ra per drawing notes; coating stack per CAP/coating spec.  
- Color code: structure gray, fluid blue, TIM orange, coating pink (PMI only).

## Interfaces to verify (checklist)
- Coldplate flatness ≤ 0.05 mm; TIM thickness call-out.
- Port threads/sizes match ICD (LPHX inlet/outlet).
- Keep-outs for harness/heaters (97/21-30).
- Ground/bond points per 51; hole classes and torque notes.
- Lifts/handling features if >15 kg (STA-L MGSE).

## Exports (DoD for REL)
- STEP AP242 for each REL assembly/part in `exports_step/`
- PDF drawings in `drawings/` with sign-offs visible
- BOM tables match EBOM structure
