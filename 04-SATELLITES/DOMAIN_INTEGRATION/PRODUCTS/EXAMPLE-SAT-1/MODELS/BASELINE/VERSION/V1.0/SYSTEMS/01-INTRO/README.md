# 01-INTRO — Mission Introduction  
**Product:** EXAMPLE-SAT-1 · **Model:** BASELINE · **Version:** V1.0

> Single source of truth for mission intent, CONOPS, modes, top-level requirements, and cross-domain links.  
> This file anchors traceability to systems, interfaces, budgets, and V&V for the **V1.0** integration baseline.

---

## Quick Nav
- Up one level: [`../`](../)
- Systems index: [`../../`](../../)
- Product root: [`../../../../../../`](../../../../../../)
- Interfaces (ICDs): see program CM → `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- Traceability: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/`

---

## 1) Mission Overview
| Field | Value (fill) |
|---|---|
| Mission class | LEO ☐ / MEO ☐ / GEO ☐ / HEO ☐ / Deep Space ☐ |
| Primary objectives | e.g., EO imaging @ 0.5 m GSD; revisit ≤ 3 days |
| Space segment | Bus: ___ · Payload(s): ___ |
| Ground segment | MOC: ___ · Stations: ___ · Frequencies: ___ |
| Orbit & lifetime | Alt ___ km · Incl ___ ° · LTAN ___ · Design life ___ yrs |
| Launch & LV | Rideshare ☐ / Dedicated ☐ · Vehicle: ___ · Site: ___ |
| Disposition | Deorbit plan / Graveyard orbit / Passivation |
| Authority context | Export ☐ · Licensing ☐ · Frequency filings ☐ |

---

## 2) CONOPS & Phases
```mermaid
flowchart LR
  L[Launch] --> LEOP[LEOP]
  LEOP --> COMM[Commissioning]
  COMM --> NOM[Nominial Ops]
  NOM --> SAFE[Safe Mode]
  SAFE --> NOM
  NOM --> EOL[Deorbit/Disposal]
````

| Phase         | Entry Criteria    | Key Activities              | Exit Criteria    | Primary Owners |
| ------------- | ----------------- | --------------------------- | ---------------- | -------------- |
| Launch        | LV ready, IBL tag | Separation, first contact   | T&C lock         | MOC, AIT       |
| LEOP          | Power positive    | ADCS detumble, TTC config   | Bus stable       | Bus Eng, AOCS  |
| Commissioning | Subsystems green  | Cal/align, payload checkout | Perf within spec | Payload, Bus   |
| Nominal Ops   | All go            | Routine ops, downlink       | Anomaly / EOL    | Ops            |
| Safe Mode     | Fault/FDIR        | Load-shed, sun-point        | Recovery plan    | Ops, AOCS      |
| EOL/Disposal  | EUL reached       | Passivation, decay burn     | Compliance met   | Systems, Ops   |

---

## 3) Operating Modes & Safing

```mermaid
stateDiagram-v2
  [*] --> SAFE
  SAFE --> DETUMBLE
  DETUMBLE --> SUNPOINT
  SUNPOINT --> NOMINAL
  NOMINAL --> PAYLOAD
  PAYLOAD --> NOMINAL
  NOMINAL --> SAFE
```

| Mode     | Purpose                 | Power (W) | Data Rate | Allowed Transitions  |
| -------- | ----------------------- | --------: | --------: | -------------------- |
| SAFE     | Survival, comms minimal |         ~ |         ~ | ↔ DETUMBLE, SUNPOINT |
| SUNPOINT | Energy positive         |         ~ |         ~ | ↔ NOMINAL            |
| NOMINAL  | Bus ops                 |         ~ |         ~ | ↔ PAYLOAD, SAFE      |
| PAYLOAD  | Science collect         |         ~ |         ~ | ↔ NOMINAL            |

---

## 4) Top-Level Requirements (extract)

> Full set in **SRS** with IDs tracked in program traceability.

| Req ID      | Text (concise)                               | Rationale     | Verification (V) | Validation (Vn) |
| ----------- | -------------------------------------------- | ------------- | ---------------- | --------------- |
| SRS-SYS-001 | Achieve duty cycle ≥ __% over design life    | Mission yield | Test/Analysis    | Ops data        |
| SRS-BUS-002 | End-of-life power margin ≥ __% in worst case | Survival      | Analysis         | TVAC            |
| SRS-PAY-003 | GSD ≤ __ m at SNR ≥ __                       | Science       | Test             | Calibration     |

---

## 5) External Interface Summary

| Partner        | Interface             | Summary               | ICD Ref        |
| -------------- | --------------------- | --------------------- | -------------- |
| Ground Segment | TT&C                  | TM/TC, ranging        | ICD-TT&C-____  |
| Payload        | Power/Data            | LVDS/CAN/SpW          | ICD-PAY-____   |
| Launch Vehicle | Mechanical/Electrical | Separation, umbilical | ICD-LV-IF-____ |

> Authoritative ICDs live under `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`. Link them here when assigned.

---

## 6) Budget Snapshots (V1.0)

| Budget            | Alloc | Current | Margin |
| ----------------- | ----: | ------: | -----: |
| Mass (kg)         |   ___ |     ___ |    ___ |
| Power EOL (W)     |   ___ |     ___ |    ___ |
| Data/day (GB)     |   ___ |     ___ |    ___ |
| Thermal (°C band) |   ___ |     ___ |    ___ |

---

## 7) Risks & Assumptions

* **Assumptions:** LV performance ___; ground coverage ___; radiation env ___.
* **Top risks (RPN):** R-01 ___; R-02 ___; R-03 ___.
* Mitigations tied to **V&V** and **Design Actions**.

---

## 8) Verification & Validation Plan (V&V)

| Gate | Evidence               | Location                                           |
| ---- | ---------------------- | -------------------------------------------------- |
| TRR  | Test readiness package | `00-PROGRAM/CONFIG_MGMT/07-RELEASES/…/COMPLIANCE/` |
| PRR  | Production readiness   | same                                               |
| FRR  | Flight readiness       | same                                               |

---

## 9) Configuration & Baselines

* **Integration Baseline (IBL):** tag(s) for V1.0 recorded under product release notes.
* Changes via **ECR/ECO** (CCB) → see `00-PROGRAM/CONFIG_MGMT/06-CHANGES/`.
* Effectivity rules (blocks/MSNs) tracked at product/version level where applicable.

---

## 10) Cross-Links

* Systems directory: [`../`](../)
* Product model/version root: [`../../`](../../)
* Program CM & QMS: `00-PROGRAM/CONFIG_MGMT/` · `00-PROGRAM/QUALITY_QMS/`

---

## Document Control

| Field        | Value                           |
| ------------ | ------------------------------- |
| File         | `…/SYSTEMS/01-INTRO/README.md`  |
| Version      | V1.0                            |
| Status       | Draft ☐ / Review ☐ / Approved ☐ |
| Owner        | Systems Engineering             |
| Date         | YYYY-MM-DD                      |
| Related tags | IBL-****, REL-****              |

---

### Glossary (used here)

* **AOCS**: Attitude and Orbit Control System
* **CCB**: Configuration Control Board
* **C&DH**: Command and Data Handling
* **CONOPS**: Concept of Operations
* **EGSE/MGSE**: Electrical/Mechanical Ground Support Equipment
* **FDIR**: Fault Detection, Isolation, and Recovery
* **IBL**: Integration Baseline
* **LEOP**: Launch and Early Orbit Phase
* **MOC**: Mission Operations Center
* **SRS**: System Requirements Specification
* **TT&C**: Telemetry, Tracking, and Command
* **V&V**: Verification and Validation

> Replace placeholders (___) and bind actual links/IDs as they are issued by CM.

```
```
