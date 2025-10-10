# CAP · 21-10_RADIATORS_HEAT_EXCHANGERS
Process planning and industrialization for radiator panels, embedded HP radiators, LPHX, coldplates, mounts, TIM/bondlines, and coating stacks. No source code.

---

## Deliverables
- **BoP / Routings:** operation sequences with resources, takt, and WIP controls.
- **Control Plans:** CTQ list, gauges, sampling, SPC methods, reaction plans.
- **PFMEA:** process risks, RPN mitigation, special characteristics.
- **Special Processes:** bonding, brazing/welding, coating/paint, cleaning/bake-out.
- **Materials & Specs:** adhesives/TIM/coatings data sheets, cure schedules.
- **Tooling & Workcells:** fixture master data, cell layouts, ergonomics/safety.
- **Qualification Packages:** IQ/OQ/PQ evidence, capability (Cp/Cpk), MSA (Gage R&R).
- **Supplier Industrialization:** PPAP/FAI requirements, source inspection plans.

---

## Layout
```
CAP/
├─ bop_routings/                 # BOP-21-10-xxxx__rNN__.xlsx / .yaml
├─ control_plans/                # CP-21-10-CTQ-xxxx__rNN__.pdf
├─ pfmea/                        # PFMEA-21-10-xxxx__rNN__.xlsx
├─ special_processes/
│  ├─ bonding/                   # adhesives, surface prep, cure cycles
│  ├─ brazing_welding/           # LPHX manifolds, coldplates (if applicable)
│  ├─ coatings/                  # SSM/white paints, thickness & α/ε targets
│  ├─ cleaning_bakeout/          # vacuum bake, cleanliness, outgassing
│  └─ corrosion_protection/      # conversions/anodize, masking
├─ materials/                    # datasheets, shelf-life, storage specs
├─ tooling_workcells/
│  ├─ fixtures_master/           # fixture BOMs, calibration, IDs
│  └─ cell_layouts/              # layouts, utilities, safety notes
├─ qualification/                # IQ/OQ/PQ, capability, run@rate
├─ msa_spc/                      # GR&R, control charts, capability studies
├─ supplier_readiness/           # PPAP, source insp., flowdowns
├─ safety_ergonomics/            # risk assessments, PPE, lifts
├─ lessons_learned/              # NCR summaries, CI actions
└─ templates/                    # BoP / CP / PFMEA templates
```

---

## Naming & revisions
`21-10-CAP_<artifact>__rNN__{WIP|RVW|REL}.*`  
Examples: `21-10-CAP-BOP-radiator_assy__r02__REL.xlsx`, `21-10-CAP-PFMEA-bonding__r01__RVW.xlsx`

---

## Special process requirements
### Bonding (adhesives/TIM)
- Surface prep: solvent clean, abrading (if spec'd), prime if needed.
- Mix ratio, pot life, bead size per datasheet.
- Cure: time/temp profile; witness coupons for DSC/pull test.
- Thickness control: measure post-cure; log deviations.

### Coatings (SSM/white paint)
- Substrate prep: degrease, conversion coat (if Al).
- Application: spray/dip per IFU; thickness targets (µm).
- Cure schedule: ramp rates, hold times, cooldown.
- Optical properties: measure α/ε on witness coupons (link to CAV).

### Cleaning & Bake-out
- Cleaning: solvents per contamination control; NVR/particle limits.
- Bake-out: vacuum/temp profile for outgassing (CVCM/TML targets).
- Handling: gloves, bags, clean-room protocols.

---

## Tooling & fixture management
- **Master List:** fixture IDs, rev, calibration due dates.
- **Calibration:** periodic verification; certs in CMP.
- **Maint. Logs:** usage, repairs, mods, obsolescence.

## Capability & qualification
- **IQ (Installation Qualification):** equipment setup, utilities verified.
- **OQ (Operational Qualification):** process params proven at extremes.
- **PQ (Performance Qualification):** run@rate, Cp/Cpk ≥ 1.33 for CTQs.
- **MSA:** Gage R&R <10% for critical dimensions; retrain if >30%.

## Continuous improvement
- **NCR review:** quarterly; root cause, corrective action, PFMEA update.
- **SPC triggers:** out-of-control signals → reaction plan → document.
