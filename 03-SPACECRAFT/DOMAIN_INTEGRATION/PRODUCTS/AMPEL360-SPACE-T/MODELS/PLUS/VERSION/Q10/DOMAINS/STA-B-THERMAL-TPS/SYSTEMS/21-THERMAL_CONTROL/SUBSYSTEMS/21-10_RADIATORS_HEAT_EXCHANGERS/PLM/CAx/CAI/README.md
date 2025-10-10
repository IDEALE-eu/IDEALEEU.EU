# CAI · 21-10_RADIATORS_HEAT_EXCHANGERS

Purpose: authoritative **integration** artifacts for radiators, embedded HP radiators, LPHX, coldplates, mounts, TIMs, and coating stacks. No source code. No FSW.

---

## Deliverables
- **Work Instructions (WI):** install radiator panels, LPHX, coldplates, mounts, TIM/bondlines.
- **Assembly Plans / Travelers:** kitting, sequencing, sign-offs, torque/bond records.
- **Inspection Plans:** flatness, shim selection, hole pattern, port sizes/threads, TIM thickness.
- **Torque Tables:** fastener specs, patterns, re-torque.
- **Bondline Packages:** adhesive/cure params, bead size, witness coupons.
- **MGSE Usage:** fixtures, lifts, slings, alignment tools.
- **ATP/ATR:** acceptance procedures and test reports (links to CAV/CMP).
- **As-Run Records:** serialized install data, measured gaps, leak test IDs.

---

## Layout
```
CAI/
├─ work_instructions/           # WI-21-10-xxx__rNN__{WIP|RVW|REL}.pdf
├─ assembly_plans/              # PLAN-21-10-xxx__rNN__.pdf
├─ travelers/                   # TRV-21-10-xxx__serial__.xlsx
├─ inspection_checklists/       # CHK-21-10-flatness|ports|threads__rNN__.xlsx
├─ torque_tables/               # TOR-21-10-M6|M8__rNN__.pdf
├─ bondline/                    # BOND-21-10-adhesive|cure__rNN__.pdf
├─ kitting/                     # KIT-21-10-xxx__rNN__.xlsx
├─ mgse/                        # MGSE-21-10-fixture|lift__rNN__.pdf
├─ atp_atr/                     # ATP-21-10-xxx__rNN__.pdf / ATR-...pdf
├─ as_run_records/              # RUN-21-10-serial_logs__YYYYMMDD__.csv
└─ templates/                   # WI / PLAN / CHK / TOR templates
```

**Naming:** `21-10-CAI_<artifact>__rNN__{WIP|RVW|REL}.*`

---

## Standards & constraints
- **Units:** mm, N·m, °C.  
- **Datums:** per 06-DIMENSIONS and 51-STRUCTURES.  
- **Adhesives/cure:** take parameters from **CAP** process specs.  
- **Torque:** per 51 fastener standards; mandatory witness and re-torque log.  
- **TIM thickness:** per CAD call-out; measure actual after clamp.  
- **Cleanliness:** NVR/particle per 21 cleanliness plan before closeout.  
- **ESD:** all electronics/heaters per ESD plan (STA-C).

## Integration sequence (typical)
1. **Kitting & Prep:** verify parts, cure adhesives, clean surfaces.
2. **Dry-fit:** check interfaces, shims, alignment without bond.
3. **Bond/Torque:** apply adhesive/TIM, clamp/torque per WI, cure log.
4. **Inspect:** flatness, gaps, torque check, leak port access.
5. **Functional Test:** continuity, leak sniff (if ports accessible).
6. **As-Run Log:** record serials, shims, torques, deviations.
7. **Handoff to Test:** CAV takes over for TVAC/leak/proof.
