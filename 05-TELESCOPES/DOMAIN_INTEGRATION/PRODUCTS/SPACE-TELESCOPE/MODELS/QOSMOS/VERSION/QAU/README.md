# SPACE-TELESCOPE / QOSMOS / QAU
**Path:** `05-TELESCOPES/DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/QOSMOS/VERSION/QAU/`

> **Architecture:** STA (Space Transport Architecture)  
> **Release tag:** **QAU** — model/baseline family keyed to Astronomical Units  
> **Scope:** End-to-end domain integration for a space observatory (optics, payloads, EPS, thermal, avionics, C&DH, AIT/ops) with PLM/CAx embedded at *subsystem* level.

---

## 1) Product Card

| Field | Value |
|---|---|
| Product | SPACE-TELESCOPE |
| Model | QOSMOS |
| Version | QAU |
| Mission Class | Space Observatory (L2/Lunar/GEO — TBD) |
| Primary Science | TBD (λ range, resolution, SNR, survey cadence) |
| Key Drivers | Wavefront stability, cryo performance, pointing, data throughput |
| UTCS Anchor | `utcs://space-telescopes/qosmos/qau` (placeholder) |
| CM Owner | Systems Engineering + Configuration Management |

---

## 2) Repository Layout (this level)

```
VERSION/QAU/
├─ SYSTEMS/                            # ATA/STA-aligned systems
│  ├─ 01-INTRO/
│  ├─ 06-DIMENSIONS_ALIGNMENTS/
│  ├─ 15-ENVIRONMENT_VIBRATION/
│  ├─ 21-THERMAL_CONTROL/
│  ├─ 24-ELECTRICAL_POWER/
│  ├─ 26-FIRE_SAFETY/                  # Ground handling only
│  ├─ 30-ICE_DEW_PREVENTION/           # Ground/airborne only
│  ├─ 31-DATA_HANDLING/
│  ├─ 32-POINTING_STABILIZATION/
│  ├─ 33-LIGHTS/
│  ├─ 34-NAVIGATION_ATTITUDE/
│  ├─ 42-AVIONICS_CONTROL/
│  ├─ 45-HEALTH_MONITORING/
│  ├─ 51-PRIMARY_STRUCTURE/
│  ├─ 52-ACCESS_HATCHES/
│  ├─ 53-OPTICAL_TUBE_ASSEMBLY/
│  ├─ 55-SECONDARY_SUPPORT/
│  ├─ 56-WINDOWS_DOMES/
│  ├─ 57-INSTRUMENT_BAYS/
│  ├─ 66-DEPLOYABLE_OPTICS/
│  ├─ 70-OPTICAL_SUBSYSTEMS/           # STA custom optics block
│  ├─ 71-INSTRUMENTS_PAYLOADS/
│  ├─ 72-CRYOGENIC_COOLING/
│  ├─ 73-FOCUS_ACTUATION/
│  ├─ 75-THERMAL_RADIATORS/
│  ├─ 76-MIRROR_CONTROL/
│  ├─ 77-ALIGNMENT_SENSING/
│  ├─ 78-BACKPLANE_ELECTRONICS/
│  ├─ 79-LUBRICATION/
│  ├─ 80-STARTUP_SEQUENCING/
│  ├─ 84-PROPULSION/                   # Only if station-keeping
│  ├─ 92-EWIS_HARNESS/
│  └─ 94-ELECTRONIC_COMPARTMENTS/
├─ INTEGRATION_VIEWS/                  # SoS views for telescope
│  ├─ OPTICAL_CHAIN.md                 # 70↔76↔77↔71
│  ├─ THERMAL_STACK.md                 # 21/72/75 ↔ 51/53
│  ├─ POINTING_CONTROL.md              # 32/34/42 ↔ 70/71
│  └─ DATA_FLOW.md                     # 31/42/78 ↔ downlink
├─ INTERFACE_MATRIX/                   # System-level interface csvs
│  ├─ optics_70↔21_32_45_51_55_57.csv
│  ├─ payloads_71↔24_31_70_57.csv
│  ├─ thermal_21_72_75↔51_53_70.csv
│  ├─ pointing_32↔34_42_70_71.csv
│  ├─ power_24↔70_71_72_78_92.csv
│  └─ harness_92↔all.csv
├─ TEMPLATES/
│  ├─ INTEGRATION_VIEW_TEMPLATE.md
│  ├─ INTERFACE_MATRIX_TEMPLATE.csv
│  └─ OPTICAL_REQUIREMENTS_TEMPLATE.md
├─ CHANGE_LOG/
│  └─ QAU_CHANGE_LOG.csv
└─ README.md                          # (this file)
```

> **PLM/CAx policy:** CAD/CAE/CAM/… live **only** under `SYSTEMS/<…>/SUBSYSTEMS/<…>/PLM/CAx/` (see §4).  
> Software is stored **with its host LRU**; physical wiring **only** under `92-EWIS_HARNESS`.

---

## 3) Critical Systems — Scope & Deliverables

| System | Purpose | Key Outputs |
|---|---|---|
| `70-OPTICAL_SUBSYSTEMS` | Primary/secondary/tertiary optics, filters, calibration | Optical prescriptions, WFE budgets, alignment trees, **SUBSYSTEMS (70-10…70-80)** with PLM/CAx |
| `71-INSTRUMENTS_PAYLOADS` | Science instruments (imager, spectrograph, coronagraph) | Interface budgets, FPA ICDs, detector configs, env. constraints |
| `21-THERMAL_CONTROL` + `72-CRYOGENIC_COOLING` + `75-THERMAL_RADIATORS` | Stability & cooldown, cryo chains, heat rejection | Thermal math models, TVAC plans/results, heater/MLI configs |
| `32-POINTING_STABILIZATION` + `34-NAVIGATION_ATTITUDE` | Gimbals, FGS/AO, star trackers/IMUs | Pointing control laws, jitter budgets, calibration sequences |
| `31-DATA_HANDLING` + `42-AVIONICS_CONTROL` + `78-BACKPLANE_ELECTRONICS` | C&DH, onboard processing, instrument electronics | CCSDS/SpaceWire/1553 ICDs, storage, throughput sizing |
| `24-ELECTRICAL_POWER` | EPS generation/storage/regulation/distribution | Power budgets, PCDU configs, protection/bonding |
| `51/53/55/57/66` | Structure, bench, bays, deployables | Stiffness & mode targets, kinematics, launch locks |
| `92-EWIS_HARNESS` | Physical wiring only | Harness drawings, connectors, zoning, EMC controls |

---

## 4) Subsystems & PLM/CAx (examples)

### `SYSTEMS/70-OPTICAL_SUBSYSTEMS/`
```
70-OPTICAL_SUBSYSTEMS/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/70↔21_32_45_51_55_57.csv
└─ SUBSYSTEMS/
   ├─ 70-10_PRIMARY_MIRROR/
   │  ├─ README.md
   │  └─ PLM/
   │     ├─ EBOM_LINKS.md
   │     └─ CAx/ (CAD/ CAE/ CAM/ CAI/ CAV/ CAP/ CAS/ CMP/)
   ├─ 70-20_SECONDARY_MIRROR/
   ├─ 70-30_TERTIARY_FLAT/
   ├─ 70-40_CORRECTORS_LENS/
   ├─ 70-50_FILTERS_GRISMS/
   ├─ 70-60_DETECTOR_CRYOSTATS/
   ├─ 70-70_WAVEFRONT_SENSORS/
   └─ 70-80_CALIBRATION_SOURCES/
```

### `SYSTEMS/71-INSTRUMENTS_PAYLOADS/`
- `SUBSYSTEMS/71-10_IMAGER/PLM/CAx/*`  
- `SUBSYSTEMS/71-20_SPECTROGRAPH/PLM/CAx/*`  
- `SUBSYSTEMS/71-30_CORONAGRAPH/PLM/CAx/*`

> **Rule recap:** PLM **only** at `SUBSYSTEMS/**/PLM/CAx/*`.  
> Wiring in **92**, software next to **its LRU** (e.g., instrument controller under 71, C&DH under 31/42).

---

## 5) Integration Views & Interface Matrices

- Author/consume SoS views in `/INTEGRATION_VIEWS/*.md` (optical chain, thermal stack, pointing control, data flow).  
- Maintain CSV matrices in `/INTERFACE_MATRIX/` using the provided template.  
- System-local matrices live in `SYSTEMS/<…>/INTERFACE_MATRIX/`.

**ICDs:** centralised under program CM — link them:
- `../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/` (relative from this README)

---

## 6) V&V, Compliance, and Digital Thread

- **V&V:** Plan and evidence are stored per system (`VERIFICATION/` inside each system/subsystem).  
- **TVAC/Modal/EMI:** Evidence links back to releases:
  - `../../../../../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/`
- **Traceability:** Requirements ↔ design ↔ test:
  - `../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/`
- **Digital Thread & Twin:**
  - `../../../../../../00-PROGRAM/DIGITAL_THREAD/`
  - Aircraft twin example (structure reference): `../../../../02-AIRCRAFT/DIGITAL_TWIN_MODEL/` (pattern reuse)
- **Data/Telemetry:** Use the Operational Data Hub patterns:
  - `../../../../01-FLEET/OPERATIONAL_DATA_HUB/`

---

## 7) Configuration Management & Changes

- **Baselines:** `../../../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/`  
- **Changes (ECR/ECO):** `../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/` (with CCB at `05-CCB/`)  
- **Releases:** `../../../../../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/`  
- **ICD Index:** `../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD_INDEX.md`

**Immutable baselines:** any update creates a new baseline; all artifacts SHA-256 hashed; approvals recorded.

---

## 8) Targets & Metrics (placeholders)

| KPI | Target (QAU) | Notes |
|---|---|---|
| WFE (nm RMS) | TBD | End-to-end, incl. thermo-elastic |
| Pointing Stability (mas) | TBD | Over exposure window |
| Cryo Temp Stability (mK) | TBD | At detector |
| Data Throughput (Mbps) | TBD | Onboard → downlink |
| Power Margin (%) | ≥TBD | Worst-case thermal |
| Availability/MTBF | ≥TBD | On-orbit |

---

## 9) RASCI (excerpt)

| Activity | S | A | R | C | I |
|---|---|---|---|---|---|
| Optical chain budgets | SE | SE | Optics Lead | Thermal, Pointing | CM |
| Thermal TVAC plan | SE | SE | Thermal Lead | EPS, Structures | CM |
| C&DH/ICDs | SE | SE | Avionics Lead | Payloads | CM |

---

## 10) Glossary (used here)

- **AO**: Adaptive Optics  
- **C&DH**: Command & Data Handling  
- **CCSDS**: Consultative Committee for Space Data Systems (TM/TC standards)  
- **EPS/PCDU**: Electrical Power System / Power Conditioning & Distribution Unit  
- **EWIS**: Electrical Wiring Interconnection System  
- **FGS**: Fine Guidance Sensor  
- **FPA**: Focal Plane Assembly  
- **ICD**: Interface Control Document  
- **L2**: Sun–Earth Lagrange Point 2  
- **MLI**: Multi-Layer Insulation  
- **STA**: Space Transport Architecture (program structuring)  
- **TVAC**: Thermal Vacuum (test)  
- **UTCS**: Unified Type/Tech Configuration Spec  
- **WFE**: Wavefront Error

---

## 11) TODO (QAU standing items)

- [ ] Freeze **INTERFACE_MATRIX** v0.1 (optics/thermal/power/pointing/data).  
- [ ] Populate **SUBSYSTEMS** for `70-10`, `70-60`, `71-10`.  
- [ ] Draft **INTEGRATION_VIEWS** (optical/thermal/pointing/data).  
- [ ] Register baseline in CM and tag **QAU-IBL-01**.

*Maintained by:* Systems Engineering & Configuration Management  
*Review cadence:* Gate-based and quarterly
