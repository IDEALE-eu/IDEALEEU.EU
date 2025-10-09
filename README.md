# IDEALEEU.EU
https://www.idealeeu.eu

> **Mission:** Design, certify, manufacture, and industrialise next-gen aircraft and spacecraft with a closed-loop digital thread from concept to fleet operations.

---

## Program Overview

Single source of truth for IDEALE EU’s engineering, certification, industrialisation, and fleet operations. The repo integrates **ATA-aligned configuration baselines**, **IMA-centric integration**, and **fleet learning** under rigorous configuration management (CM).

**Goals**
- Flight-ready prototypes
- Type certification / flight-worthiness (aircraft) & FRR (spacecraft)
- Serial production ramp ≥ target rate
- Cost, safety, reliability KPIs within targets

**Standards Baseline**
- **Aircraft:** ARP4754A/ARP4761, DO-178C/DO-254/DO-160, AS9100, CS-23/CS-25  
- **Spacecraft:** ECSS (E/Q/M series), CCSDS (comms), DO-326A/355/356A (cyber)

**Stage Gates**  
SRR → MCR → PDR → CDR → TRR → PRR → ORR/EIS (aircraft) / FRR (spacecraft)  
**V&V:** Requirements trace, HARA/SSA, FTA/FMEA, ground/flight (AIT) test, conformity

---

## Repository Map (AIR & SPACE are symmetric)

```

IDEALEEU.EU/
├─ 00-PROGRAM/                 # Governance, CM, QMS, standards, supply chain
├─ 01-FLEET/                   # Operational data hub, MRO, federated learning
├─ 02-AIRCRAFT/                # Aircraft (ATA iSpec 2200)
│  ├─ CONFIGURATION_BASE/
│  ├─ CROSS_SYSTEM_INTEGRATION/
│  ├─ DIGITAL_TWIN_MODEL/
│  ├─ DOMAIN_INTEGRATION/
│  └─ FINAL_ASSEMBLY_OPS/
├─ 03-SPACECRAFT/              # Spacecraft (ECSS + CCSDS)
│  ├─ CONFIGURATION_BASE/
│  ├─ CROSS_SYSTEM_INTEGRATION/
│  ├─ DIGITAL_TWIN_MODEL/
│  ├─ DOMAIN_INTEGRATION/
│  └─ FINAL_ASSEMBLY_OPS/      # (= AIT)
└─ 04-BUSINESS/

```

**Quick links**
- CM: [`00-PROGRAM/CONFIG_MGMT/`](./00-PROGRAM/CONFIG_MGMT/)
- QMS: [`00-PROGRAM/QUALITY_QMS/`](./00-PROGRAM/QUALITY_QMS/)
- Digital Thread: [`00-PROGRAM/DIGITAL_THREAD/`](./00-PROGRAM/DIGITAL_THREAD/)
- Fleet Hub: [`01-FLEET/OPERATIONAL_DATA_HUB/`](./01-FLEET/OPERATIONAL_DATA_HUB/)
- MRO Strategy: [`01-FLEET/MRO_STRATEGY/`](./01-FLEET/MRO_STRATEGY/)
- **Aircraft** baselines: [`02-AIRCRAFT/CONFIGURATION_BASE/`](./02-AIRCRAFT/CONFIGURATION_BASE/)
- **Spacecraft** baselines: [`03-SPACECRAFT/CONFIGURATION_BASE/`](./03-SPACECRAFT/CONFIGURATION_BASE/)
- Cross-System Integration: [`02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/`](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/) · [`03-SPACECRAFT/CROSS_SYSTEM_INTEGRATION/`](./03-SPACECRAFT/CROSS_SYSTEM_INTEGRATION/)
- ICDs: [`00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)

---

## Unified Product View & Domain Integration

Both vehicles use the same **product hierarchy** and **domain pattern**:

```

[02-AIRCRAFT|03-SPACECRAFT]/DOMAIN_INTEGRATION/
└─ PRODUCTS/
└─ AMPEL360-[AIR-T|SPACE-T]/
└─ MODELS/[BWB|PLUS]/
└─ VERSION/[Q100|Q10]/
├─ SYSTEMS/                         # << unified level for all domains
│  └─ <DOMAIN>/SYSTEMS/ATA-XX_NAME/
│     ├─ INTEGRATION_VIEW.md
│     ├─ INTERFACE_MATRIX/<XX↔…>.csv
│     └─ SUBSYSTEMS/ATA-XX-YY_NAME/
│        └─ PLM/
│           ├─ EBOM_LINKS.md
│           └─ CAx/ (CAD/CAE/CAO/CAM/CAI/CAV/CAP/CAS/CMP)
├─ DELs/   (deliverables packages)
├─ PAx/    (packaging standards/artifacts)
└─ tests/  (domain/system test specs)

````

**Rules**
- **Only one level:** `/SYSTEMS/` for every domain.  
- **PLM/CAx lives only in `SUBSYSTEMS`** (real artifacts). Domain level carries policies/templates only.  
- **Software with its host LRU (ATA of host).** EWIS only in **ATA-92** (air).  
- **Spacecraft uses the same structure**; chapter semantics adapt to ECSS sets below.

---

## Domain ↔ Systems Mapping (AIR & SPACE)

### Aircraft (ATA iSpec 2200, primaries)
- **AAA (Airframes/Aero/AW):** 06, 50, **51–57**, 54 (shared)  
- **PPP (Propulsion/Fuel):** **28**, **49**, 54 (shared), 60–61, 70–73, **75**, 78, 81–82  
- **MEC (Mechanical):** **27**, **29**, **32**, **36–37**, 63, 67, 79, 83  
- **LCC (Control/Comms):** 08, **22**, 23, 44, 45, 76, 93  
- **EDI (Avionics/Digital/Indicating):** **31**, **34**, **42**, **77**, 84, 94  
- **EEE (Electrical/Lights/Start):** **24**, **33**, 39, 74, 80, 97  
- **EER (Env/Emissions):** 15, **26**, **38**, 85  
- **DDD (Drainage/De-ice):** 09, **21**, **30**, 41  
- **CCC (Cabin/Cargo/HSI):** 11, **25**, **35**, 43, **50**  
- **IIS (Information/IT):** 16, **46**, 91  
- **LIB (Logistics/Limits):** 01, 04, **05**, **12**  
- **AAP (Airport Ops):** **10**  
- **CQH (Cryogenics/H₂/NGS):** **47**  
- **IIF (Industrial Infra):** **07**  
- **OOO (OS/Ontologies/Reserved):** 13, 20, reserved chapters (templates)

### Spacecraft adaptation (ECSS/CCSDS aligned “sets”)
- **A) Structures & Mechanisms:** 06, 50–57, 66, 94  
- **B) Thermal & TPS:** 21, 30  
- **C) Power / EPS / Harness:** 24, 39, 49, 97  
- **D) Communications (RF/Optical) & TT&C:** 23, 33, 48  
- **E) Navigation, Time & Data Handling:** 31, 34, 41  
- **F) Avionics, Flight Software & Databus:** 40, 42, 93  
- **G) Control, Autonomy, FDIR & Health:** 22, 44, 45  
- **H) ECLSS / Crew / Payload Accommodation:** 25, 35–38 (per mission)  
- **I) Propulsion & Fluids:** 28, 29, 47, 60–61, 70–83, 84–85  
- **J) Docking, Sampling & Robotics:** 58, 59  
- **K) Environment, Safety & Space Traffic:** 15, 26, 86, 87, 90  
- **L) Ground, Integration & Mission Ops:** 07, 10, 16, 32, 46, 92  
- **M) Program, Compliance & Records:** 01, 04–05, 11–14, 17–20, 98–99

> **54 (Nacelles/Pylons):** if structural ownership → set **A**; if propulsion module internals → set **I**.

---

## Ways of Working

- **Baselines & Releases:** [`00-PROGRAM/CONFIG_MGMT/04-BASELINES/`](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/) · [`07-RELEASES/`](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/)  
- **Changes:** ECR/ECO via [`06-CHANGES/`](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/) with CCB oversight ([`05-CCB/`](./00-PROGRAM/CONFIG_MGMT/05-CCB/))  
- **Traceability:** [`10-TRACEABILITY/`](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)  
- **ICDs:** [`09-INTERFACES/`](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/) (with index & template)  
- **Digital Thread:** telemetry schemas, model registries, metrics in [`00-PROGRAM/DIGITAL_THREAD/`](./00-PROGRAM/DIGITAL_THREAD/)

---

## Automation & Validation

- **Create domain skeletons:** `00-PROGRAM/CONFIG_MGMT/13-AUTOMATION/SCRIPTS/create-domains.sh`  
- **Validate structure (CI):** `00-PROGRAM/CONFIG_MGMT/13-AUTOMATION/SCRIPTS/validate-structure.sh`

Run:
```bash
bash 00-PROGRAM/CONFIG_MGMT/13-AUTOMATION/SCRIPTS/create-domains.sh
bash 00-PROGRAM/CONFIG_MGMT/13-AUTOMATION/SCRIPTS/validate-structure.sh
````

---

## Metrics (Program-level)

* Requirements coverage ≥ **99%**
* Defect escape rate ≤ **target**
* Mass/weight within **allocated margins**
* Schedule variance ≤ **target**
* Unit cost ≤ **target**
* Dispatch reliability / mission success ≥ **target**

Dashboards:
`00-PROGRAM/DIGITAL_THREAD/10-METRICS/` · `01-FLEET/ANALYTICS_AND_AI/DASHBOARD_SPECS/`

---

## Get Started

1. Read **Governance** → [`00-PROGRAM/GOVERNANCE.md`](./00-PROGRAM/GOVERNANCE.md)
2. Review **CM Plan** → [`00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md`](./00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)
3. Use the **ICD template** → [`00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-XXXX.md`](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-XXXX.md)
4. File changes via **ECR** → [`00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/`](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/)

---

**Program site:** [https://www.idealeeu.eu](https://www.idealeeu.eu)
**Ownership:** Program Management & Configuration Management (see [`00-PROGRAM/CONFIG_MGMT/05-CCB/`](./00-PROGRAM/CONFIG_MGMT/05-CCB/))

```
