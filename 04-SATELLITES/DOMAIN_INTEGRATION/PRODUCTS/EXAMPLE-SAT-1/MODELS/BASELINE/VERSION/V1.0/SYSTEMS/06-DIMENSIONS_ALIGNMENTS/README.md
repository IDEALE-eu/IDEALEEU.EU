# 06-DIMENSIONS_ALIGNMENTS

Reference frames, coordinate systems, focal stations, and alignment tolerances for the spacecraft. This system governs how every unit is positioned, measured, and verified from AIT through launch integration.

---

## Purpose
- Define **authoritative reference frames** (spacecraft body, launcher, payload/instrument).
- Control **datums**, **tolerances**, and **alignment chains** across structures, payloads, antennas, and sensors.
- Provide **survey plans**, **error budgets**, and **signed evidence** for certification/review.

## Scope
- Frames & transforms (SB, LF, PF-i).
- Master datums and mounting interfaces.
- CG/boresight/lever-arm definitions.
- Geometric stability (thermo-elastic effects).
- Launch-stowed vs on-orbit-deployed geometry.

## Key Definitions
- **Spacecraft Body Frame (SB):** right-handed {+X fwd, +Y starboard, +Z nadir}.
- **Launcher Frame (LF):** per launcher ICD; SB↔LF transform controlled here.
- **Payload Frame (PF-i):** one per instrument or antenna; tied to its datum set.

## Deliverables (authoritative set)
- `INTEGRATION_VIEW.md` — system overview, alignment tree, methods.
- `INTERFACE_MATRIX/06↔OTHERS.csv` — cross-system interfaces.
- `FRAME_DEFS.yaml` — SB/LF/PF definitions & transforms (with uncertainties).
- `DATUMS.csv` — master datum coordinates/tolerances & ownership.
- `MEASUREMENT_PLAN.md` — instruments, sequences, uncertainty model.
- `ERROR_BUDGET.xlsx` — allocations & roll-up (k=2 unless noted).
- `SURVEY_RAW/*.csv` — instrument point clouds / CMM dumps.
- `SURVEY_REDUCED/*.csv` — reduced frames, residuals.
- `SURVEY_REPORT.pdf` — signed evidence & pass/fail summary.

## Acceptance Criteria (examples)
| Parameter                               | Requirement                 | Verification                |
|-----------------------------------------|-----------------------------|-----------------------------|
| CG wrt SB origin                        | ≤ ±2 mm per axis            | Mass props + survey         |
| Instrument boresight vs SB +X           | ≤ 30 arcsec                 | Autocollimator/theodolite   |
| Star tracker lever arm                  | ≤ ±0.5 mm                   | Laser tracker               |
| SB↔LF transform uncertainty (pos/ang)   | ≤ 0.5 mm / 20 arcsec        | Joint fit at launcher site  |
| Panel planarity                         | ≤ 0.3 mm RMS                | Laser tracker / CMM         |

> Full list in `ERROR_BUDGET.xlsx`.

## Interfaces
- **51/53 Structures:** master datums, flatness, hole patterns.
- **57 Instrument Bays / 71 Instruments:** PF-i alignment & optical axes.
- **34 Navigation/Attitude:** star tracker/IMU boresight, lever arms.
- **31 Data Handling:** time-tagging of surveys; config baseline storage.
- **21 Thermal / 75 Radiators:** thermo-elastic stability & gradients.
- **24 Power / 92 EWIS:** harness reach & strain relief constraints.

See `INTERFACE_MATRIX/06↔OTHERS.csv`.

## Process (summary)
1. Define frames & datums → baseline `FRAME_DEFS.yaml`, `DATUMS.csv`.
2. Plan measurement → `MEASUREMENT_PLAN.md`, tools calibration records.
3. Execute surveys (rough-in → fine) → capture `SURVEY_RAW/*`.
4. Reduce & correlate (hot/cold) → `SURVEY_REDUCED/*`, update error budget.
5. Report & sign-off → `SURVEY_REPORT.pdf`; update baselines if needed.

## Change Control
Any change to **frames, datums, or transforms** requires ECR/ECO and impact review of connected systems.  
Process: `../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/`

## TBDs / Open Items
- TBD-06-01: Final launcher LF & tolerances from provider.
- TBD-06-02: Thermal distortion limits for on-orbit focus stability.

---
**Owner:** AIT Metrology Lead • **Review:** at each gate (PDR/CDR/FRR) and pre-ship • **Classification:** Internal
