# IDEALEEU.EU

[https://www.idealeeu.eu](https://www.idealeeu.eu)

> **Mission:** Design, certify, manufacture, and industrialise next-gen **aircraft** and **space systems** with a closed-loop digital thread from concept to fleet operations.

---

## Program Overview

This repository is the **single source of truth** for IDEALE EU: governance, engineering, certification, industrialisation, and fleet ops. It unifies **ATA-aligned Aircraft (AIR-T)** and **STA-aligned Space (SPACE-T)** architectures with rigorous CM, IMA-centric integration, and operations feedback.

### Charter

**Goals**

* Flight-ready prototypes
* Type certification / flight-worthiness (aircraft) & FRR (space)
* Serial production ramp ≥ target rate
* Cost, safety, reliability KPIs within targets

**Standards Baseline**

* **Aircraft:** ARP4754A / ARP4761, DO-178C / DO-254 / DO-160, AS9100, CS-23 / CS-25
* **Space:** ECSS (E/Q/M series)

**Stage Gates**
SRR → MCR → PDR → CDR → TRR → PRR → ORR/EIS (aircraft) / FRR (space)
**V&V:** Requirements trace, HARA/SSA, FTA/FMEA, ground/flight test, conformity

---

## Repository Map (first level is identical for air & space programs)

```
IDEALEEU.EU/
├─ 00-PROGRAM/
├─ 01-FLEET/
├─ 02-AIRCRAFT/
├─ 03-SPACECRAFT/
├─ 04-SATELLITES/
├─ 05-TELESCOPES/
├─ 06-PROBES/
├─ 07-DRONES/
├─ 08-LAUNCHERS/
├─ 09-STM-SPACE-STATION-MODULES/
└─ 10-BUSINESS/
```

**Quick links**

* Governance: `00-PROGRAM/GOVERNANCE.md`
* Standards: `00-PROGRAM/STANDARDS/`
* CM (plans, baselines, changes, interfaces, trace): `00-PROGRAM/CONFIG_MGMT/`
* QMS: `00-PROGRAM/QUALITY_QMS/`
* Digital Thread: `00-PROGRAM/DIGITAL_THREAD/`
* **Aircraft ATA Baselines (AIR-T):** `02-AIRCRAFT/CONFIGURATION_BASE/`
* **Space STA Baselines (SPACE-T):** `03-SPACECRAFT/CONFIGURATION_BASE/`
* Cross-System Integration (Aircraft): `02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/`
* Fleet Ops Hub: `01-FLEET/OPERATIONAL_DATA_HUB/`
* MRO Strategy: `01-FLEET/MRO_STRATEGY/`
* Federated Learning: `01-FLEET/FEDERATED_LEARNING/`
* STM Modules: `09-STM-SPACE-STATION-MODULES/`

---

## Product Architecture (uniform for AIR-T & SPACE-T families)

All products (air or space) use the same pathing and structure:

```
…/DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT-ID>/MODELS/<MODEL-ID>/VERSION/<TAG>/
└─ SYSTEMS/
   └─ <ATA|STA>-XX_NAME/
      ├─ INTEGRATION_VIEW.md
      ├─ INTERFACE_MATRIX/
      │  └─ XX↔OTHERS.csv
      └─ SUBSYSTEMS/
         └─ <XX-YY_SUBSYS>/
            ├─ README.md
            ├─ DELs/ …            # certification docs (instance scope)
            ├─ PAx/ …             # packaging/output artifacts
            ├─ PLM/               # **real artifacts only at SUBSYSTEM level**
            │  ├─ EBOM_LINKS.md
            │  └─ CAx/ (CAD/CAE/CAO/CAM/CAI/CAV/CAP/CAS/CMP)
            ├─ SUPPLIERS/ …
            ├─ policy/  tests/
            └─ META.json  inherit.json
```

**Rules**

* **SW with its host LRU** (e.g., FADEC in ATA-73; A653 partitions in ATA-42).
* **EWIS only in ATA-92** (aircraft); equivalent harness rules centralised in STA Power/Harness set.
* **Interfaces** live in each system’s `INTERFACE_MATRIX/` + `INTEGRATION_VIEW.md`.
* **PLM/CAx** exists **only** inside `SUBSYSTEMS/` (templates/policies at domain level).

---

## Aircraft Domain Integration (AIR-T, ATA-aligned)

**15 canonical domains** (all use `/SYSTEMS/…/SUBSYSTEMS/…/PLM/CAx`):

| Domain (abbr.)                            | Primary ATA Chapters (examples)                                        |
| ----------------------------------------- | ---------------------------------------------------------------------- |
| **AAA – Airframes/Aero/Airworthiness**    | 06, 50, **51**, **52**, **53**, **54**(shared), **55**, **56**, **57** |
| **PPP – Propulsion/Fuel**                 | **28**, **49**, **54**(shared), 60–61, 70–73, **75**, 78, 81–82        |
| **MEC – Mechanical Systems**              | **27**, **29**, **32**, **36**–37, 63, 67, 79, 83                      |
| **LCC – Linkages/Control/Comms**          | 08, **22**, 23, 44, 45, 76, 93                                         |
| **EDI – Electronics/Avionics/Indicators** | **31**, **34**, **42**, **77**, 84, 94                                 |
| **EEE – Electrical/Lights/Start**         | **24**, **33**, 39, 74, 80, 97                                         |
| **EER – Environmental/Emissions**         | 15, **26**, **38**, 85                                                 |
| **DDD – Drainage/Deshielo**               | 09, **21**, **30**, 41                                                 |
| **CCC – Cockpit/Cabin/Cargo**             | 11, **25**, **35**, 43, **50**                                         |
| **IIS – Information/IT**                  | 16, **46**, 91                                                         |
| **LIB – Logistics/Límites**               | 01, 04, **05**, **12**                                                 |
| **AAP – Operación en tierra**             | **10**                                                                 |
| **CQH – Criogénicos/H2/NGS**              | **47**                                                                 |
| **IIF – Infraestructura industrial**      | **07**                                                                 |
| **OOO – OS/Ontologías/Reservas**          | 13, 20, reserved chapters (templates)                                  |

> Full ATA baseline: `02-AIRCRAFT/CONFIGURATION_BASE/` (IMA in **ATA-42**, EWIS in **ATA-92**).

---

## Space Domain Integration (SPACE-T, STA-aligned)

Space systems follow the same structure and **/SYSTEMS** conventions, organised by **STA “sets”** (chapter groupings). Each set uses standard **10–90** sections (design → test → ops):

* **A) Structures & Mechanisms** — ch. 06, 50, 51, 52, 53, 55, 56, 57, 66, 94
  *10 Primary · 20 Secondary · 30 Doors/Hatches · 40 Joints · 50 Mechanisms/Deploy · 60 Mounts/Align · 70 Materials · 80 NDI · 90 Qual/Acceptance*
* **B) Thermal & TPS** — ch. 21, 30
  *10 Radiators/HX · 20 MLI · 30 Heaters · 40 Pipes/Straps · 50 TPS · 60 Sensors · 70 Algorithms · 80 TVAC · 90 Contamination/Bakeout*
* **C) Power / EPS / Harness** — ch. 24, 39, 49, 97
  *10 Generation · 20 Storage · 30 Conversion/PCDU · 40 Distribution · 50 Protection/GB · 60 Metering · 70 Control/Modes · 80 Harness · 90 Thermal/EGSE*
* **D) Communications (RF/Optical) & TT&C** — ch. 23, 33, 48
  *10 RF FE · 20 TRX/Modems · 30 Antennas · 40 CCSDS TM/TC · 50 Ranging · 60 RF Switching · 70 Optical Terminals · 80 Calibration · 90 Ground IF/Ops*
* **E) Navigation, Time & Data Handling** — ch. 31, 34, 41
  *10 Nav Sensors · 20 Timing · 30 C&DH/Recording · 40 I/O · 50 Processing/Storage · 60 TLM Params · 70 FDIR Hooks · 80 HIL/SIL · 90 Security/Hardening*
* **F) Avionics, FSW & Databus** — ch. 40, 42, 93
  *10 Computers · 20 FSW/Services · 30 Networks (SpW/1553/CAN/IMA) · 40 Boot/Update · 50 Timebase · 60 Drivers/I-O · 70 Mode Tables · 80 HIL/SIL · 90 Cyber*
* **G) Control, Autonomy, FDIR & Health** — ch. 22, 44, 45
  *10 Architecture/Modes · 20 GNC · 30 Actuation · 40 FDIR Rules · 50 Health/CBM · 60 Redundancy/X-strap · 70 Trending · 80 CL-verification · 90 Ops/Limits*
* **H) ECLSS, Crew & Payload Accommodation** — ch. 25, 35, 36, 37, 38
  *10 Atmosphere · 20 Pressure · 30 CO₂/Trace · 40 Humidity · 50 Water/Waste · 60 Fire(26 IF) · 70 Sensors · 80 Control Elec/SW · 90 Ops/Mx*
* **I) Propulsion & Fluids** — ch. 28, 29, 47, 60–61, 70–75, 76–80, 81–85
  *10 Tanks/PMD · 20 Press/Purge · 30 Feed · 40 Thrust Devices · 50 Ignition/Actuation · 60 Thermal · 70 TVC/Allocation · 80 Control/Seq · 90 Safety/Plume/EMC*
  *(54 structure: if owned by structures → Set A; if propulsion internals → Set I)*
* **J) Docking, Sampling & Robotics** — ch. 58, 59
  *10 Sensing · 20 Latch · 30 Seals · 40 Umbilicals · 50 Drives · 60 Control · 70 Safety/Abort · 80 Testbeds · 90 Ops*
* **K) Environment, Safety & Space Traffic** — ch. 15, 26, 86, 87, 90
  *10 Acoustics/Vibe · 20 Ordnance/Hazards · 30 Planetary Prot · 40 Radiation · 50 Conjunction/Debris · 60 EMC/EMI · 70 Safety Analyses · 80 V&V · 90 Compliance*
* **L) Ground, Integration & Mission Ops** — ch. 07, 10, 16, 32, 46, 92
  *10 MGSE/Handling · 20 EGSE · 30 I&T · 40 EDL/Landing Ops · 50 Ground/MOC IF · 60 Calibration/Geometry · 70 Procedures/Training · 80 Ops Data · 90 Archival/Handover*
* **M) Program, Compliance & Records** — ch. 01, 04, 05, 11–14, 17–20, 98–99
  *10 Governance · 20 Plans · 30 Req/Compliance · 40 Risk · 50 Reviews/Gates · 60 Standards/Tailor · 70 Records · 80 Training · 90 Audits/Export*

> Space families (STA structure) apply to **03-SPACECRAFT**, **04-SATELLITES**, **05-TELESCOPES**, **06-PROBES**, **07-DRONES (space/strat)**, **08-LAUNCHERS**, **09-STM**.

---

## Ways of Working

* **Baselines & Releases:** `00-PROGRAM/CONFIG_MGMT/04-BASELINES/` and `…/07-RELEASES/`
* **Changes:** ECR/ECO via `…/06-CHANGES/` with CCB oversight `…/05-CCB/`
* **Traceability:** `…/10-TRACEABILITY/`
* **ICDs:** `…/09-INTERFACES/` (see `ICD_INDEX.md`)
* **Automation:** repo scripts (e.g., `scripts/create-domains.sh`, `scripts/validate-structure.sh`) and CI gates in `…/13-AUTOMATION/`

---

## Metrics

* Requirements coverage ≥ **99%**
* Defect escape rate ≤ **target**
* Weight/mass budgets within **margins**
* Schedule variance ≤ **target**
* Unit cost ≤ **target**
* Dispatch reliability / mission success ≥ **target**

Dashboards: `00-PROGRAM/DIGITAL_THREAD/10-METRICS/` and `01-FLEET/ANALYTICS_AND_AI/DASHBOARD_SPECS/`

---

## Get Started

1. **Governance:** `00-PROGRAM/GOVERNANCE.md`
2. **CM Plan:** `00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md`
3. **ICD Template:** `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-XXXX.md`
4. **Raise ECR:** `00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/`

---

## Glossary (only terms used here)

* **AIR-T** — *Air Transport Architecture* (aircraft; ATA-aligned).
* **ATA** — Air Transport Association iSpec 2200 chapter scheme.
* **CCB** — Configuration Control Board.
* **ECR / ECO** — Engineering Change Request / Order.
* **EWIS** — Electrical Wiring Interconnection System (ATA-92).
* **FDIR** — Fault Detection, Isolation & Recovery.
* **HIL / SIL** — Hardware/Software-in-the-Loop.
* **ICD** — Interface Control Document.
* **IMA** — Integrated Modular Avionics (e.g., ARINC 653; ATA-42).
* **LRU** — Line Replaceable Unit.
* **MBSE** — Model-Based Systems Engineering.
* **PCDU** — Power Conditioning & Distribution Unit (space).
* **PLM / CAx** — Product Lifecycle Management / CAD-CAE-CAM… artifacts.
* **SPACE-T (STA)** — *Space Transport Architecture* (space; STA chapter sets).
* **STM** — Space Station Modules (pressurised elements).
* **TT&C** — Telemetry, Tracking & Command.
* **V&V** — Verification & Validation.

---

**Program site:** [https://www.idealeeu.eu](https://www.idealeeu.eu)
**Ownership:** Program Management & Configuration Management (`00-PROGRAM/CONFIG_MGMT/05-CCB/`)

