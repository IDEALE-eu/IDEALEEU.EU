# CAV · 21-10_RADIATORS_HEAT_EXCHANGERS
Authoritative **validation & test evidence** for radiators, embedded heat-pipe radiators, liquid plate HX (LPHX), coldplates, mounts, TIM/bondlines, and coating stacks. No flight SW.

---

## Deliverables
- **Test Plans (TP):** objectives, methods, acceptance criteria.
- **Procedures (PRO):** chamber/rig steps, safety, instrumentation.
- **Setups:** fixture configs, chamber recipes, channel maps.
- **Raw Data:** time-series, images, chamber logs.
- **Reduced Data:** cleaned datasets, KPIs, uncertainties.
- **Plots & Dashboards:** thermal maps, leak trends, vibration spectra.
- **Reports:** ATR/ATP, qualification/acceptance reports.
- **Anomalies:** NCRs, deviations, re-test evidence.
- **Calibration:** certificates, uncertainty budgets.

---

## Layout
```
CAV/
├─ plans/                      # TP-21-10-xxx__rNN__.pdf
├─ procedures/                 # PRO-21-10-xxx__rNN__.pdf
├─ setups/
│  ├─ fixtures/                # fixture IDs, clamp maps, photos
│  ├─ chamber_recipes/         # TVAC profiles (yaml/csv)
│  └─ channel_maps/            # DAQ assignments, scales, units
├─ tvac/                       # thermal vacuum functional/performance
│  ├─ raw/                     # csv/parquet, chamber logs
│  ├─ reduced/                 # cleaned, synchronized datasets
│  └─ plots/                   # time plots, stability, margins
├─ leak_proof/                 # helium leak, proof, burst
│  ├─ sniffer/                 # raw logs + locations
│  ├─ proof/                   # pressure traces
│  └─ burst/                   # curves, photos
├─ vib_shock/                  # sine/random/shock results
├─ thermal_perf/               # coldplate ∆T-Q curves, SER
├─ flow_dp/                    # flow vs ∆P, clog/bleed tests
├─ coating_optical/            # α/ε, thickness, durability
├─ fai/                        # first article inspection packs
├─ calibration/                # certs, traceability chains
├─ anomalies/                  # NCR logs, re-test evidence
├─ reports/                    # ATR/ATP, qual reports (PDFs)
└─ templates/                  # TP/PRO/report templates
```

---

## Naming & revisions
`21-10-CAV_<test>__rNN__{WIP|RVW|REL}.*`  
Examples:  
- `21-10-CAV-TP-tvac_hot__r02__RVW.pdf`  
- `21-10-CAV-ATR-coldplate_ser123__r01__REL.pdf`  
- `21-10-CAV-DATA-leak_sniffer__20251011__.csv`

---

## Test Types & Objectives

### TVAC (Thermal Vacuum)
- **Objective:** demonstrate thermal performance (hot/cold balance, transient response) in vacuum.
- **Setup:** radiator/coldplate in chamber; heaters simulate load; sink plates/IR lamps for environment.
- **Data:** T vs time, heater power, chamber pressure, shroud temp.
- **Acceptance:** temps within predicted ±5°C; margin to limits.

### Leak & Proof/Burst
- **Leak (He sniffer):** <1×10⁻⁶ scc/s per joint; scan all welds/fittings.
- **Proof:** 1.5× MEOP for 5 min; no permanent deformation.
- **Burst:** witness test on sample; validate safety factor.
- **Data:** pressure traces, leak rates, photos of failure modes (burst only).

### Vibration & Shock
- **Sine sweep:** identify resonances; no structural yield.
- **Random vibration:** qualification levels per mission profile.
- **Shock:** pyro/separation simulation; no damage.
- **Data:** accel response, PSD, transfer functions; visual inspection post-test.

### Thermal Performance (Coldplate/LPHX)
- **∆T-Q mapping:** vary heat load, measure inlet/outlet ∆T and ∆P.
- **Flow uniformity:** verify all channels active; detect clogs.
- **SER (System Effectiveness Ratio):** (Q / (A·∆T)); compare to model.
- **Data:** flow rate, temps, pressures, calculated metrics.

### Coating Optical Properties
- **α (solar absorptance), ε (IR emittance):** measure on witness coupons at angles.
- **Thickness:** verify per spec (µm); non-destructive (eddy current).
- **Durability:** UV exposure, thermal cycling, adhesion (tape test).
- **Data:** spectrophotometer scans, certs from vendor.

---

## Data Quality & Traceability
- **Calibration:** all sensors cal'd within 6 months; certs in `calibration/`.
- **Uncertainty budget:** propagate sensor/method errors; report ±U (k=2).
- **Raw data immutable:** archive as-acquired; processing scripts documented.
- **Sync & cleanup:** align time-bases, remove noise, flag outliers.
- **Metadata:** test date, serial, rev, operator, deviations logged.

---

## Anomaly Handling
- **NCR:** non-conformance report if out-of-spec; link to CAI/CAP for root cause.
- **Deviation:** approved changes to procedure; document in report.
- **Re-test:** new data files with "_retest" suffix; cross-ref to original.

---

## Handoff to CMP
- **Qualification:** full test reports → CMP for compliance evidence.
- **Acceptance:** ATP/ATR → CMP for flight hardware release.
- **Correlation:** test vs CAE model deltas → feed back to CAE for updates.
