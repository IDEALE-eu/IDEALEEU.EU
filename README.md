# IDEALEEU.EU
https://www.idealeeu.eu

> **Mission:** Design, certify, manufacture, and industrialise next-gen aircraft and spacecraft with a closed-loop digital thread from concept to fleet ops.

---

## Program Overview
Single source of truth for IDEALE EU engineering, certification, industrialisation, and fleet operations. It unifies **ATA-aligned AIR-T** (aircraft) and **STA-aligned SPACE-T** (spacecraft) architectures, rigorous CM/QMS, and fleet learning.

### Stage Gates & V&V
SRR → MCR → PDR → CDR → TRR → PRR → ORR/EIS (aircraft) / FRR (spacecraft)  
**V&V:** requirements trace, HARA/SSA, FTA/FMEA, ground/flight test, conformity.

### Standards Baseline
**Aircraft:** ARP4754A/ARP4761, DO-178C/DO-254/DO-160, AS9100, CS-23/CS-25  
**Spacecraft:** ECSS (E/Q/M)

---

## Repository Map

```

IDEALEEU.EU/
├─ 00-PROGRAM/           # Governance, CM, QMS, Standards, Supply Chain, Digital Thread
├─ 01-FLEET/             # Operational Data Hub, MRO Strategy, Federated Learning
├─ 02-AIRCRAFT/          # AIR-T (ATA) baselines + Domain Integration
├─ 03-SPACECRAFT/        # SPACE-T (STA) baselines + Domain Integration
└─ 04-BUSINESS/          # Market, partnerships, finance

```

**Quick links**
- CM (all): [`00-PROGRAM/CONFIG_MGMT/`](./00-PROGRAM/CONFIG_MGMT/)
- QMS: [`00-PROGRAM/QUALITY_QMS/`](./00-PROGRAM/QUALITY_QMS/)
- Digital Thread: [`00-PROGRAM/DIGITAL_THREAD/`](./00-PROGRAM/DIGITAL_THREAD/)
- Fleet Hub: [`01-FLEET/OPERATIONAL_DATA_HUB/`](./01-FLEET/OPERATIONAL_DATA_HUB/)
- MRO: [`01-FLEET/MRO_STRATEGY/`](./01-FLEET/MRO_STRATEGY/)
- **Aircraft baselines (AIR-T):** [`02-AIRCRAFT/CONFIGURATION_BASE/`](./02-AIRCRAFT/CONFIGURATION_BASE/)
- **Spacecraft baselines (SPACE-T):** [`03-SPACECRAFT/CONFIGURATION_BASE/`](./03-SPACECRAFT/CONFIGURATION_BASE/)
- Cross-System Integration (aircraft): [`02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/`](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/)

---

## Dual Architecture (same first-level layout)

Both product lines use the **same path pattern** for Domain Integration deliverables:

```

[02-AIRCRAFT|03-SPACECRAFT]/DOMAIN_INTEGRATION/PRODUCTS/
└─ AMPEL360-[AIR-T|SPACE-T]/MODELS/[BWB|PLUS]/VERSION/[Q100|Q10]/
├─ 00-README.md
├─ [15 DOMAINS]/                # one folder per domain (shared naming)
│   └─ SYSTEMS/                 # unified (no ZONES/PLATFORM)
│       └─ <System>/
│           ├─ INTEGRATION_VIEW.md
│           ├─ INTERFACE_MATRIX/*.csv
│           └─ SUBSYSTEMS/<SubSystem>/
│               └─ PLM/
│                   ├─ EBOM_LINKS.md
│                   └─ CAx/ (CAD/CAE/CAO/CAM/CAI/CAV/CAP/CAS/CMP)
└─ scripts/ (create-domains.sh, validate-structure.sh)

```

**Rules**
- **PLM/CAx solo en `SUBSYSTEMS/`** (artefactos reales).  
- **SW con su LRU** (en su ATA/host; p.ej. FADEC→ATA-73, IMA partitions→ATA-42).  
- **EWIS solo ATA-92** (referenciado vía matrices de interfaz).  
- Cada *System* requiere: `INTEGRATION_VIEW.md`, `INTERFACE_MATRIX/*.csv`, y ≥1 `SUBSYSTEMS/*/PLM/CAx/*`.

---

## Aircraft (AIR-T) — 15 Domains & Primary ATA
> **ATA baseline:** see [`02-AIRCRAFT/CONFIGURATION_BASE/00-README.md`](./02-AIRCRAFT/CONFIGURATION_BASE/00-README.md)

| Domain (code → name) | Primary ATA chapters |
|---|---|
| **AAA — Airframes, Aerodynamics, Airworthiness** | 06, 50, **51**, **52**, **53**, **54** *(shared with PPP)*, **55**, **56**, **57** |
| **PPP — Propulsion & Fuel Systems** | **28**, **49**, **54** *(shared)*, 60–61, 70–73, **75**, 78, 81–82 |
| **MEC — Mechanical Systems & Modules** | **27**, **29**, **32**, 36–37, 63, 67, 79, 83 |
| **LCC — Linkages, Control & Comms** | 08, **22**, 23, 44, 45, 76, 93 |
| **EDI — Electronics, Digital & Instruments** | **31**, **34**, **42**, **77**, 84, 94 |
| **EEE — Electrical, Lights & Start** | **24**, **33**, 39, 74, 80, 97 |
| **EER — Environmental & Remediation** | 15, **26**, **38**, 85 |
| **DDD — Drainage & De-ice** | 09, **21**, **30**, 41 |
| **CCC — Cockpit, Cabin & Cargo** | 11, **25**, **35**, 43, **50** |
| **IIS — Information Systems & IT** | 16, **46**, 91 |
| **LIB — Logistics, Limits & Servicing** | 01, 04, **05**, **12** |
| **AAP — Airport/Air-Ops Platforms** | **10** |
| **CQH — Cryogenics/Nitrogen/H₂** | **47** |
| **IIF — Industrial Infrastructure** | **07** |
| **OOO — OS, Ontologies & Reserved** | 13, 20, *(reserved/templates)* |

> **ATA-92 (EWIS)**: único repositorio de cableado — [`02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/`](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/)

---

## Spacecraft (SPACE-T) — STA System Sets (mirrored domains)
> Same domain folders as AIR-T; systems and matrices follow STA groupings below. Baselines live under `03-SPACECRAFT/CONFIGURATION_BASE/`.

**STA Sets (by functional group):**
- **A) Structures & Mechanisms:** ch. 06, 50, 51, 52, 53, 55, 56, 57, 66, 94 → primary/secondary structure, doors/hatches, deployables, mechanisms, NDI, qualification.  
- **B) Thermal & TPS:** 21, 30 → radiators/HX, MLI, heaters, pipes/straps, TPS, sensors, TVAC.  
- **C) Power / EPS / Harness:** 24, 39, 49, 97 → generation, storage, PCDU, distribution/protection, harness, EGSE.  
- **D) Comms & TT&C:** 23, 33, 48 → RF FE, TRX/modems, antennas, CCSDS TM/TC, optical terminals, ground IF.  
- **E) Navigation, Time & Data Handling:** 31, 34, 41 → Nav sensors, timing, C&DH, I/O, processing/storage, FDIR hooks.  
- **F) Avionics, Flight SW & Databus:** 40, 42, 93 → OBC, FS, networks (SpW/1553/CAN/IMA), boot/update, sync, HIL/SIL, cyber.  
- **G) Control, Autonomy & FDIR:** 22, 44, 45 → control architecture, GNC, allocation, FDIR, health/CBM, redundancy.  
- **H) ECLSS, Crew & Payload Accommodation:** 25, 35, 36, 37, 38 → atmosphere, pressure, CO₂/trace, humidity, water/waste, fire.  
- **I) Propulsion & Fluids:** 28, 29, 47, 60–61, 70–82, 83–85 → tanks/PMD, pressurize/purge, feed, thrusters, ignition, thermal, TVC, safety/plume.  
- **J) Docking, Sampling & Robotics:** 58, 59 → sensing, capture, seals, umbilicals, drives, autonomy, testbeds.  
- **K) Environment, Safety & Space Traffic:** 15, 26, 86, 87, 90 → acoustics/vibe, ordnance/hazards, planetary protection, radiation, conjunctions.  
- **L) Ground, Integration & Mission Ops:** 07, 10, 16, 32, 46, 92 → MGSE/EGSE, I&T, EDL, ground segment, geometry/calibration.  
- **M) Program, Compliance & Records:** 01, 04, 05, 11–14, 17–20, 98–99 → governance, plans, compliance, reviews, data/records.

*Use the same domain folders as AIR-T; each STA system keeps `INTEGRATION_VIEW.md`, `INTERFACE_MATRIX/*.csv`, and `SUBSYSTEMS/*/PLM/CAx/*`.*

---

## Ways of Working
- **Baselines & Releases:** [`00-PROGRAM/CONFIG_MGMT/04-BASELINES/`](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/) · [`07-RELEASES/`](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/)  
- **Changes:** ECR/ECO via CCB — [`06-CHANGES/`](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/) · [`05-CCB/`](./00-PROGRAM/CONFIG_MGMT/05-CCB/)  
- **Traceability:** [`10-TRACEABILITY/`](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)  
- **ICDs:** [`09-INTERFACES/`](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/) (with ICD index)  
- **Automation:** `create-domains.sh` and `validate-structure.sh` live beside each Product VERSION; both are CI-ready and executable.

---

## Metrics
- Requirements coverage ≥ **99%** · Defect escape ≤ **target** · Mass/weight within **margins**  
- Schedule variance ≤ **target** · Unit cost ≤ **target** · Dispatch/mission success ≥ **target**  
Dashboards: [`00-PROGRAM/DIGITAL_THREAD/10-METRICS/`](./00-PROGRAM/DIGITAL_THREAD/10-METRICS/) and fleet dashboards under `01-FLEET/ANALYTICS_AND_AI/DASHBOARD_SPECS/`.

---

## Get Started
1) Governance → [`00-PROGRAM/GOVERNANCE.md`](./00-PROGRAM/GOVERNANCE.md)  
2) CM Plan → [`00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md`](./00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)  
3) Aircraft ATA baseline → [`02-AIRCRAFT/CONFIGURATION_BASE/`](./02-AIRCRAFT/CONFIGURATION_BASE/)  
4) Spacecraft STA baseline → [`03-SPACECRAFT/CONFIGURATION_BASE/`](./03-SPACECRAFT/CONFIGURATION_BASE/)  
5) Use ICD template → [`00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-XXXX.md`](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-XXXX.md)  
6) File ECRs → [`00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/`](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/)

---

## Glossary (only terms used here)
- **AIR-T**: Air Transport Architecture (aircraft stack, ATA-aligned).  
- **STA**: Space Transport Architecture (spacecraft stack, STA sets).  
- **ATA**: Air Transport Association chapter taxonomy (iSpec 2200).  
- **IMA**: Integrated Modular Avionics (e.g., ARINC 653 partitions).  
- **EWIS**: Electrical Wiring Interconnection System (ATA-92).  
- **CM**: Configuration Management (baselines, releases, changes).  
- **CCB**: Configuration Control Board (change approval).  
- **ECR/ECO**: Engineering Change Request / Order.  
- **QMS**: Quality Management System.  
- **ICD**: Interface Control Document.  
- **MBSE**: Model-Based Systems Engineering.  
- **PLM / CAx**: Product Lifecycle Management / CAD-CAE-… tool artifacts (kept under `SUBSYSTEMS/*/PLM/CAx/`).  
- **HIL / SIL**: Hardware/Software-in-the-Loop.  
- **V&V**: Verification & Validation.  
- **SRR/PDR/CDR/TRR/PRR/ORR/EIS/FRR**: Major lifecycle reviews.  
- **ECSS, ARP4754A/4761, DO-178C/254/160, CS-23/25**: Referenced standards families.

---

**Program site:** https://www.idealeeu.eu  
**Ownership:** Program & Configuration Management (see [`00-PROGRAM/CONFIG_MGMT/05-CCB/`](./00-PROGRAM/CONFIG_MGMT/05-CCB/))
```

