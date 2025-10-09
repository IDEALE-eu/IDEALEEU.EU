# IDEALEEU.EU

[https://www.idealeeu.eu](https://www.idealeeu.eu)

> **Mission:** Design, certify, manufacture, and industrialise next-gen **aircraft** and **space systems** with a closed-loop digital thread—from concept to fleet ops.

---

## Program Overview

Single source of truth for **engineering**, **certification**, **industrialisation**, and **fleet operations**. We use **ATA-aligned (AIR-T)** and **STA-aligned (SPACE-T)** architectures, rigorous CM, and domain-based integration.

**Standards (baseline)**
Aircraft: ARP4754A/ARP4761, DO-178C/DO-254/DO-160, AS9100, CS-23/CS-25
Space: ECSS (E/Q/M) and mission-specific authority rules

**Stage gates**
SRR → MCR → PDR → CDR → TRR → PRR → ORR/EIS (aircraft) / FRR (space)

---

## Repository Map

```
IDEALEEU.EU/
├─ 00-PROGRAM/          # Governance, CM, QMS, standards, supply chain
├─ 01-FLEET/            # Operational data hub, MRO, federated learning
├─ 02-AIRCRAFT/         # AIR-T (ATA) baselines + domain integration
├─ 03-SPACECRAFT/       # SPACE-T (STA) baselines + domain integration
└─ 04-BUSINESS/         # Market, partnerships, finance
```

**Quick links**

* CM (all): [`00-PROGRAM/CONFIG_MGMT/`](./00-PROGRAM/CONFIG_MGMT/) · QMS: [`00-PROGRAM/QUALITY_QMS/`](./00-PROGRAM/QUALITY_QMS/)
* Digital Thread: [`00-PROGRAM/DIGITAL_THREAD/`](./00-PROGRAM/DIGITAL_THREAD/)
* ATA Baselines (AIR-T): [`02-AIRCRAFT/CONFIGURATION_BASE/`](./02-AIRCRAFT/CONFIGURATION_BASE/)
* STA Baselines (SPACE-T): [`03-SPACECRAFT/CONFIGURATION_BASE/`](./03-SPACECRAFT/CONFIGURATION_BASE/)
* Cross-System/Integration (air): [`02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/`](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/)
* Fleet ops hub: [`01-FLEET/OPERATIONAL_DATA_HUB/`](./01-FLEET/OPERATIONAL_DATA_HUB/)

---

## Unified Product Architecture (AIR-T & SPACE-T)

**Both aircraft and spacecraft use the same first-level organisation and path pattern.**

**Canonical path (applies to AIR-T and SPACE-T):**

```
<02-AIRCRAFT | 03-SPACECRAFT>/DOMAIN_INTEGRATION/
  PRODUCTS/<ARCH-FAMILY>/
    MODELS/<MODEL-ID>/            # e.g., BWB-H2-Hy-E
      VERSION/<TAG>/              # e.g., Q100
        SYSTEMS/ATA-XX_* or STA-XX_*/
          INTEGRATION_VIEW.md
          INTERFACE_MATRIX/<X↔Y.csv>
          SUBSYSTEMS/<XX-YY_*>/PLM/CAx/(CAD/CAE/CAM/…)
```

### AIR-T (ATA — Air Transport Architecture, aircraft)

* Systems folders use **ATA-XX** (e.g., `ATA-24_ELECTRICAL_POWER/`).
* EWIS wiring is **only** in `ATA-92`.

### SPACE-T (STA — Space Transport Architecture, spacecraft)

* Systems folders use **STA-XX** (space-adapted chaptering mirroring the sets below).
* Spacecraft-specific sets (A–M) map to STA chapters (structures, thermal/TPS, EPS, TT&C, C&DH, avionics/SW, control/FDIR, ECLSS, propulsion/fluids, docking/robotics, env/safety/traffic, ground/ops, program/compliance).

---

## Domain Integration (15 canonical domains, `/SYSTEMS/` everywhere)

> **PLM/CAx live only inside `SUBSYSTEMS/…/PLM/CAx/`**.
> **Software lives with its host LRU. EWIS only in ATA-92 (AIR-T) / STA-97 (wiring).**

### Aircraft (AIR-T) — Domains → primary ATA

* **AAA** Airframes/Aero/Airworthiness → 06, 50, **51–57**, 54*(shared)*
* **PPP** Propulsion/Fuel → **28**, **49**, 54*(shared)*, 60–61, 70–73, **75**, 78, 81–82
* **MEC** Mechanical → **27**, **29**, **32**, 36–37, 63, 67, 79, 83
* **LCC** Linkages/Control/Comms → 08, **22**, 23, 44, 45, 76, 93
* **EDI** Electronics/Digital/Instruments → **31**, **34**, **42**, **77**, 84, 94
* **EEE** Electrical/Lights/Start → **24**, **33**, 39, 74, 80, 97
* **EER** Environmental/Emissions → 15, **26**, **38**, 85
* **DDD** Drain/De-ice → 09, **21**, **30**, 41
* **CCC** Cockpit/Cabin/Cargo → 11, **25**, **35**, 43, **50**
* **IIS** Information/IT → 16, **46**, 91
* **LIB** Logistics/Limits → 01, 04, **05**, **12**
* **AAP** Airport/Handling → **10**
* **CQH** Cryogenics/H₂/NGS → **47**
* **IIF** Industrial Infrastructure → **07**
* **OOO** OS/Ontologies/Reserved → 13, 20, reserved chapters

### Space (SPACE-T) — Domains → STA sets (chapter families)

* **Structures & Mechanisms (A)** → STA 06, 50–57, 66, 94
* **Thermal & TPS (B)** → STA 21, 30
* **Power / EPS / Harness (C)** → STA 24, 39, 49, 97
* **Comms & TT&C (D)** → STA 23, 33, 48
* **Nav, Time & Data Handling (E)** → STA 31, 34, 41
* **Avionics, FSW & Databus (F)** → STA 40, 42, 93
* **Control, Autonomy & FDIR (G)** → STA 22, 44, 45
* **ECLSS & Payload Accommodation (H)** → STA 25, 35–38
* **Propulsion & Fluids (I)** → STA 28–29, 47, 60–61, 70–83, 84–85
* **Docking, Sampling & Robotics (J)** → STA 58–59
* **Environment, Safety & STM (K)** → STA 15, 26, 86–87, 90
* **Ground, Integration & Mission Ops (L)** → STA 07, 10, 16, 32, 46, 92
* **Program, Compliance & Records (M)** → STA 01, 04–05, 11–14, 17–20, 98–99
* **Plus the remaining two domains (IIF/OOO) mirrored for space where applicable.**

---

## Product Portfolio (families you can instantiate under `/PRODUCTS/`)

* **AMPEL360-AIR-T** (aircraft) — e.g., `MODELS/BWB-H2-Hy-E/`
* **AMPEL360-SPACE-T** (spacecraft bus)
* **SATELLITES** *(04)* — GEO/LEO/MEO families
* **TELESCOPES** *(05)* — space & ground segments
* **PROBES** *(06)* — planetary/interplanetary
* **DRONES** *(07)* — UAS/VTOL families
* **LAUNCHERS** *(08)* — small/medium/heavy
* **STM — Space Station Modules** *(09)* — pressurised/unpressurised

> Each family follows the same `PRODUCTS/<FAMILY>/MODELS/<MODEL>/VERSION/<TAG>/SYSTEMS/…` pattern (AIR-T uses ATA; SPACE-T uses STA).

---

## Example (aircraft) — model spotlight

**AMPEL360-AIR-T · `BWB-H2-Hy-E` · Q100**

```
02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/
└─ SYSTEMS/
   ├─ ATA-28_FUEL_H2/…/SUBSYSTEMS/28-10_H2_TANKS_CRYOSTATS/PLM/CAx/
   ├─ ATA-24_ELECTRICAL_POWER/…/SUBSYSTEMS/24-20_BATTERIES/PLM/CAx/
   ├─ ATA-42_INTEGRATED_MODULAR_AVIONICS/…/SUBSYSTEMS/42-90_H2_MGMT_PARTITIONS/PLM/CAx/
   ├─ ATA-71_POWERPLANT/…                       # + interface matrices & integration views
   └─ ATA-92_EWIS/…                             # wiring only
```

---

## Ways of Working

* **Baselines & Releases:** [`00-PROGRAM/CONFIG_MGMT/04-BASELINES/`](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/) · [`07-RELEASES/`](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/)
* **Changes:** ECR/ECO via [`06-CHANGES/`](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/) with CCB oversight (`05-CCB/`).
* **Traceability:** [`10-TRACEABILITY/`](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)
* **ICDs:** [`09-INTERFACES/`](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/) + index.
* **Validation gates (CI):** every `SYSTEMS/…` must include `INTEGRATION_VIEW.md`, `INTERFACE_MATRIX/*.csv`, and at least one `SUBSYSTEMS/*/PLM/CAx/` branch. No PLM at domain level.

---

## Metrics

* Requirements coverage ≥ **99%** · Dispatch/mission success ≥ **target**
* Weight/mass within **margins** · Schedule variance ≤ **target** · Unit cost ≤ **target**
  Dashboards: [`00-PROGRAM/DIGITAL_THREAD/10-METRICS/`](./00-PROGRAM/DIGITAL_THREAD/10-METRICS/) and fleet dashboards under `01-FLEET/ANALYTICS_AND_AI/DASHBOARD_SPECS/`.

---

## Get Started

1. Governance: [`00-PROGRAM/GOVERNANCE.md`](./00-PROGRAM/GOVERNANCE.md)
2. CM Plan: [`00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md`](./00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)
3. Use the ICD template: [`…/09-INTERFACES/ICD-XXXX.md`](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-XXXX.md)
4. File an ECR: [`…/06-CHANGES/05-ECR/`](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/)

---

## Glossary (terms used here)

* **AIR-T**: *Air Transport Architecture* (aircraft; ATA-aligned).
* **STA**: *Space Transport Architecture* (spacecraft; space-adapted chaptering).
* **ATA**: Air Transport Association chaptering standard (aircraft systems).
* **IMA (ATA-42)**: Integrated Modular Avionics.
* **EWIS (ATA-92/STA-97)**: Electrical Wiring Interconnection System.
* **PLM / CAx**: Product Lifecycle Management / CAD-CAE-CAM… artefacts.
* **LRU**: Line-Replaceable Unit (host for software baselines).
* **ICD**: Interface Control Document.
* **ECR/ECO / CCB**: Change request/order / Change Control Board.
* **SRR/PDR/CDR/TRR/PRR/ORR/FRR**: Program review gates (system & flight).

---

**Program site:** [https://www.idealeeu.eu](https://www.idealeeu.eu)
**Ownership:** Program Management & Configuration Management (`00-PROGRAM/CONFIG_MGMT/05-CCB/`)

