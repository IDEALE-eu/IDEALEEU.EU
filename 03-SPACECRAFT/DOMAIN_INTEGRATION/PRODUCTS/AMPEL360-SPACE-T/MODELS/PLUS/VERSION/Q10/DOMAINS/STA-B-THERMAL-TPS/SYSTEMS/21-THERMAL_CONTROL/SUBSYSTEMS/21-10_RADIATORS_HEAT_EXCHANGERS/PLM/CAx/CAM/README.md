# CAM · 21-10_RADIATORS_HEAT_EXCHANGERS

Purpose: authoritative **manufacturing data** and **NC programs** for radiator panels, embedded-HP radiators, LPHX, coldplates, mounts, TIM carriers, and coating masks. No source code. Process specs live in **CAP**.

---

## Deliverables
- CNC toolpaths and post-processed NC (`.nc/.tap`) for 3/5-axis mill, mill-turn.
- Honeycomb routing programs and depth control tables.
- Waterjet/laser cut files for sheets, masks, gaskets.
- Drill patterns, hole maps, break-edge cycles.
- Probing/zeroing macros, fixture offsets, work offsets.
- Setup sheets, tool lists, cutters, holder stick-outs.
- Cut simul. reports (collision/over-travel) and machine time.
- Export bundles for release (zip with checksums).

---

## Layout
```
CAM/
├─ cnc_3axis/                 # NC + source ops for flat plates, coldplates
├─ cnc_5axis/                 # NC for manifolds, complex panels
├─ mill_turn/                 # NC for fittings, ports (LPHX)
├─ router_honeycomb/          # panel core routing programs
├─ waterjet_laser/            # DXF/DWG + NC for blanks/masks/gaskets
├─ drilling/                  # pattern cycles, peck params, hole tables
├─ probing/                   # WCS macros, datum probing, verification
├─ fixtures/                  # clamp maps, soft jaws, nests (refs to CAD)
├─ setup_sheets/              # OPxx setup PDFs with photos
├─ tool_libraries/            # cutter DB (.json/.xml), holders
├─ posts/                     # controller posts (Fanuc/Siemens/Heidenhain)
├─ simulation/                # verification reports, videos, logs
├─ exports_rel/               # signed release bundles (zip + sha256)
└─ templates/                 # setup + tool list templates
```

---

## Naming & revisions
`21-10-CAM_<part>__opNN__rNN__{WIP|RVW|REL}.<ext>`  
Examples:  
- `21-10-CAM-coldplate_serpentine__op20__r03__RVW.nc`  
- `21-10-CAM-radiator_panel_core__op10__r02__REL.nc`  
- `21-10-CAM-lphx_manifold__op30__r01__WIP.tap`

---

## Standards & control
- **Units:** mm, mm/min, RPM.  
- **Coordinate systems:** match CAD datums (A/B/C) and fixture offsets.  
- **Tool management:** centralized tool library; no ad-hoc edits in NC.  
- **Verification:** mandatory simulation before first cut; collision-free証.  
- **Post-processors:** approved posts only; no manual G-code edits post-release.  
- **Version control:** NC tied to drawing rev; re-post on CAD changes.

## CAM workflow
1. **Import geometry:** STEP/IGES from CAD `exports_step/`.
2. **Setup & WCS:** align to datums, define fixture offsets.
3. **Tool selection:** from approved library; document reach/clearance.
4. **Toolpath generation:** ops per process plan (CAP).
5. **Post-process:** controller-specific NC output.
6. **Simulate:** verify collisions, over-travel, cycle time.
7. **Bundle release:** zip NC + setup + tool list + simulation report.
8. **Handoff:** to shop floor with signed traveler.
