# 01-INTRO — Integration View  
**Product:** EXAMPLE-SAT-1 · **Model:** BASELINE · **Version:** V1.0

> System-level integration context for the Mission Introduction (CONOPS, modes, cross-cutting interfaces).  
> Use this as the anchor for linking requirements, ICDs, budgets, and V&V artifacts.

---

## Quick Nav
- Systems index: [`../`](../)
- Product/version root: [`../../`](../../)
- Local interface matrix: [`./INTERFACE_MATRIX/`](./INTERFACE_MATRIX/)

---

## 1) Overview
This system defines the mission narrative (CONOPS), operational phases, and mode architecture used by all other systems for alignment (power, thermal, data handling, TT&C, payload operations).

---

## 2) Functional Context
```mermaid
flowchart LR
  OPS[Mission Ops / MOC] --- TT&C
  TT&C[TT&C] --- CNDH[C&DH / Data Handling]
  CNDH --- PAY[Payload(s)]
  CNDH --- PWR[Power EPS]
  CNDH --- THM[Thermal]
  PAY --- THM
  PWR --- THM
````

* **Authoritative sources:** Mission Objectives, SRS, CONOPS.
* **Consumers:** All flight/ground systems needing phase & mode contracts.

---

## 3) Operating Modes (top-level)

```mermaid
stateDiagram-v2
  [*] --> SAFE
  SAFE --> DETUMBLE
  DETUMBLE --> SUNPOINT
  SUNPOINT --> COMMISSION
  COMMISSION --> NOMINAL
  NOMINAL --> PAYLOAD
  PAYLOAD --> NOMINAL
  NOMINAL --> SAFE
  SAFE --> [*]
```

| Mode       | Purpose                          | Power | Data Link | Notes                |
| ---------- | -------------------------------- | ----: | --------: | -------------------- |
| SAFE       | Survival, thermal safe, min comm |     ~ |       Low | Entry on faults/FDIR |
| DETUMBLE   | Stabilize attitude               |     ~ |       Low | ADCS takeover        |
| SUNPOINT   | Energy-positive attitude         |     ~ |       Med | EPS recovery         |
| COMMISSION | Checkout & calibration           |     ~ |       Med | Subsystems green     |
| NOMINAL    | Routine bus ops                  |     ~ |       Med | Gateway to PAYLOAD   |
| PAYLOAD    | Science/data acquisition         |     ~ |      High | Schedulable windows  |

> Mode definitions and transitions are authoritative for downstream systems; keep in sync with C&DH and TT&C ICDs.

---

## 4) Key Interfaces (summary)

| Partner System | Interface Class     | What / Why                                  | Details                                          |
| -------------- | ------------------- | ------------------------------------------- | ------------------------------------------------ |
| TT&C           | TM/TC, ranging      | Command ingress, housekeeping, ranging      | see [`./INTERFACE_MATRIX/`](./INTERFACE_MATRIX/) |
| C&DH           | Data, timebase      | Mode table distribution, timeline execution | see matrix                                       |
| EPS (Power)    | Power, mode hooks   | Load shedding, survival setpoints           | see matrix                                       |
| Thermal        | Thermal budgets     | Mode-dependent heat loads & limits          | see matrix                                       |
| Payload        | Command/data window | Observation timelines, calibrations         | see matrix                                       |

> Program ICDs live under `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/` (reference IDs only here).

---

## 5) Dependencies & Constraints

* **Power:** Minimum survival margin in SAFE; mode budgets tracked by EPS.
* **Thermal:** Mode envelopes (cooldown rates, heater policies).
* **Data handling:** Timeline capacity, downlink windows, recording limits.
* **Timebase:** Absolute/relative time sync for procedures and FDIR.
* **Safety:** Entry/exit criteria to SAFE; inhibit matrix alignment with FDIR.

---

## 6) Integration Points

* **Structural:** Mounting of TT&C antennas & payload apertures (constraints only).
* **Electrical:** Survival power paths, critical loads list.
* **Thermal:** Interfaces to radiators/heaters for mode-driven setpoints.
* **Data:** Uplink/downlink schemas for mode commands & housekeeping.

---

## 7) Budgets (snapshots)

| Budget     | Alloc | Current | Margin |
| ---------- | ----: | ------: | -----: |
| Mass (kg)  |     — |       — |      — |
| Power (W)  |     — |       — |      — |
| Data (GBd) |     — |       — |      — |
| Thermal °C |     — |       — |      — |

> Keep aligned with product-level budget sheets; this file only summarizes top values.

---

## 8) Verification & Validation Hooks

* Mode transition tests (HIL/SIL) mapped to SRS IDs.
* Timeline execution dry-runs (procedures & safing).
* Telemetry points for mode auditing (enter/exit stamps).
* Evidence stored under product V&V folders; link IDs here.

---

## 9) Configuration & Change Control

* Integration baseline tag(s) for this version recorded at product root.
* Changes via ECR/ECO under `00-PROGRAM/CONFIG_MGMT/06-CHANGES/`.
* Interface updates require matrix + ICD pair updates.

---

## 10) References

* Mission Objectives & SRS (program traceability register)
* ICD Register: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
* Budgets: product power/thermal/data budget sheets

---

## Document Control

| Field   | Value                                    |
| ------- | ---------------------------------------- |
| File    | `…/SYSTEMS/01-INTRO/INTEGRATION_VIEW.md` |
| Status  | Draft ☐ / Review ☐ / Approved ☐          |
| Owner   | Systems Engineering                      |
| Version | V1.0                                     |
| Date    | YYYY-MM-DD                               |

```
```
