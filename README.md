# IDEALEEU.EU

[https://www.idealeeu.eu](https://www.idealeeu.eu)

> **Mission:** Design, certify, manufacture, and industrialise next‑gen **aircraft**, **spacecraft** and **aerospace full assets portfolio** with a closed‑loop digital thread—from concept to fleet ops.

---

## Primary Folders 

* **[00-PROGRAM](./00-PROGRAM/)** — Governance, CM, QMS, standards, supply chain
* **[01-FLEET](./01-FLEET/)** — Operational Data Hub, MRO Strategy, Federated Learning
* **[02-AIRCRAFT](./02-AIRCRAFT/)** — AIR‑T (ATA) baselines, domain integration, twin
* **[03-SPACECRAFT](./03-SPACECRAFT/)** — STA baselines, domain integration, AIT/mission
* **[04-SATELLITES](./04-SATELLITES/)** — STA-aligned satellite product structures
* **[05-TELESCOPES](./05-TELESCOPES/)** — Observatory payload/domain structures
* **[06-PROBES](./06-PROBES/)** — Deep‑space probes (STA)
* **[07-DRONES](./07-DRONES/)** — UAS/UAM product lines
* **[08-LAUNCHERS](./08-LAUNCHERS/)** — Launch vehicles (stages, GSE, range)
* **[09-STM-SPACE-STATION-MODULES](./09-STM-SPACE-STATION-MODULES/)** — Station modules/segments
* **[10-BUSINESS](./10-BUSINESS/)** — Market, partnerships, finance

---

## Core Architectures

### AIR‑T (Aircraft • ATA‑aligned)

* **Common pattern (both AIR‑T & STA):**
  `DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT>/MODELS/<MODEL>/VERSION/<Qn>/SYSTEMS/…`
* **Examples**

  * Config baselines: **[02-AIRCRAFT/CONFIGURATION_BASE](./02-AIRCRAFT/CONFIGURATION_BASE/)** (ATA chapters, EWIS in ATA‑92, IMA in ATA‑42)
  * Domain integration (15 domains): **[02-AIRCRAFT/DOMAIN_INTEGRATION](./02-AIRCRAFT/DOMAIN_INTEGRATION/)**
  * Cross‑system integration: **[02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/)**
  * Digital Twin: **[02-AIRCRAFT/DIGITAL_TWIN_MODEL](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/)**
  * **Reference product**: `AMPEL360-AIR-T / MODELS / BWB-H2-Hy-E / VERSION / Q100`
* **Aircraft 15 Domains (primary ATA)**
  AAA(06,50–57) · PPP(28,49,54,60–61,70–73,75,78,81–82) · MEC(27,29,32,36–37,63,67,79,83) · LCC(08,22–23,44–45,76,93) · EDI(31,34,42,77,84,94) · EEE(24,33,39,74,80,97) · EER(15,26,38,85) · DDD(09,21,30,41) · CCC(11,25,35,43,50) · IIS(16,46,91) · LIB(01,04–05,12) · AAP(10) · CQH(47) · IIF(07) · OOO(13,20,+reserved)

### STA (Spacecraft • Space‑chapter aligned)

* **Same pattern as AIR‑T** for products/models/versions/systems.
* **Examples**

  * Spacecraft DI: **[03-SPACECRAFT/DOMAIN_INTEGRATION](./03-SPACECRAFT/DOMAIN_INTEGRATION/)**
  * Satellites DI: **[04-SATELLITES/DOMAIN_INTEGRATION](./04-SATELLITES/DOMAIN_INTEGRATION/)**
  * Telescopes DI: **[05-TELESCOPES/DOMAIN_INTEGRATION](./05-TELESCOPES/DOMAIN_INTEGRATION/)**
* **Key STA groupings (condensed)**
  Structures & Mechanisms (06,50–57,66,94) · Thermal/TPS (21,30) · Power/EPS/Harness (24,39,49,97) · Comms/TT&C (23,33,48) · Nav/Time/C&DH (31,34,41) · Avionics/FSW/Databus (40,42,93) · Control/Autonomy/FDIR (22,44,45) · ECLSS/Crew/Payload Accom (25,35–38) · Propulsion/Fluids (28–29,47,60–61,70–85) · Docking/Sampling/Robotics (58–59) · Environment/Safety/Traffic (15,26,86–87,90) · Ground/Integration/Ops (07,10,16,32,46,92) · Program/Compliance (01,04–05,11–14,17–20,98–99)

---

## Ways of Working

* **Baselines & Releases:**
  [04‑BASELINES](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/) · [07‑RELEASES](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/)
* **Changes (ECR/ECO + CCB):**
  [06‑CHANGES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/) · [05‑CCB](./00-PROGRAM/CONFIG_MGMT/05-CCB/)
* **Traceability & ICDs:**
  [10‑TRACEABILITY](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/) · [09‑INTERFACES](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
  * **UTCS Registry:** [10-TRACEABILITY/UTCS/](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/)
* **Compliance & Security:**
  * **Badge Registry:** [11-BADGES/](./00-PROGRAM/CONFIG_MGMT/11-BADGES/)
  * **Ethical ML (MAL-EEM):** [13-GOVERNANCE/MAL-EEM/](./00-PROGRAM/13-GOVERNANCE/MAL-EEM/)
* **Contribution & Reviews:**
  * **CI validators:** [12-CI/validate-structure.sh](./00-PROGRAM/CONFIG_MGMT/12-CI/validate-structure.sh)

---

## Metrics

Coverage ≥ 99% · Defect escape ≤ target · Mass within margins · Schedule variance ≤ target · Unit cost ≤ target · Dispatch reliability / mission success ≥ target.
Dashboards: [Program metrics](./00-PROGRAM/DIGITAL_THREAD/10-METRICS/) · [Fleet KPIs](./01-FLEET/ANALYTICS_AND_AI/DASHBOARD_SPECS/)

---

## Get Started

1. Read **Governance** → [00‑PROGRAM/GOVERNANCE.md](./00-PROGRAM/GOVERNANCE.md)
2. Review **CM Plan** → [01‑CM_PLAN.md](./00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)
3. Use **ICD template** → [ICD‑XXXX.md](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-XXXX.md)
4. File **ECR** → [06‑CHANGES/05‑ECR](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/)

---

## Glossary (scoped)

* **AIR‑T** — *Air Transport Architecture* (ATA‑aligned aircraft architecture).
* **STA** — *Space Transport Architecture* (space chapter mapping for spacecraft).
* **ATA** — Air Transport Association chapter taxonomy (aircraft systems).
* **IMA** — Integrated Modular Avionics (ARINC‑653 partitions; ATA‑42).
* **EWIS** — Electrical Wiring Interconnection System (aircraft wiring; ATA‑92).
* **PLM / CAx** — Product Lifecycle Mgmt; CAD/CAE/CAM/CAI/CAV/CAP/CAS/CMP artifacts (in **SUBSYSTEMS/PLM/**).
* **ECR / ECO / CCB** — Change Request, Change Order, Config Control Board.

---

**Program site:** [https://www.idealeeu.eu](https://www.idealeeu.eu)
**Ownership:** Program & Configuration Management (see [CCB](./00-PROGRAM/CONFIG_MGMT/05-CCB/))


