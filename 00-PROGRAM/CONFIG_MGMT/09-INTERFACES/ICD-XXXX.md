# Interface Control Document (ICD)

**ICD Number:** ICD-XXXX  
**Title:** [Interface Name]  
**Version:** [X.X]  
**Date:** [YYYY-MM-DD]  
**Status:** [Draft | Review | Approved | Active]

## Document Control

| Field | Value |
|---|---|
| Document Number | ICD-XXXX |
| Version | X.X |
| Status | [Status] |
| Release Date | YYYY-MM-DD |
| Next Review Date | YYYY-MM-DD |
| Configuration Baseline | [SRR](../04-BASELINES/SRR/) · [PDR](../04-BASELINES/PDR/) · [CDR](../04-BASELINES/CDR/) · [TRR](../04-BASELINES/TRR/) · [PRR](../04-BASELINES/PRR/) · [ORR_EIS](../04-BASELINES/ORR_EIS/) · [FRR](../04-BASELINES/FRR/) |

## Approvals

| Role | Name | Signature | Date |
|---|---|---|---|
| Party A Representative | TBD | _______ | ____ |
| Party B Representative | TBD | _______ | ____ |
| Systems Engineer | TBD | _______ | ____ |
| CCB Chair | TBD | _______ | ____ |

## Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | YYYY-MM-DD | [Name] | Initial draft |
| | | | |

## 1. Introduction

### 1.1 Purpose
[Describe the purpose of this ICD and what interface it controls]

### 1.2 Scope
[Define the scope and boundaries of the interface]

### 1.3 Interface Parties

**Party A:** [System/Subsystem Name]  
- Organization: [Organization]  
- Point of Contact: [Name, email, phone]

**Party B:** [System/Subsystem Name]  
- Organization: [Organization]  
- Point of Contact: [Name, email, phone]

### 1.4 Applicable Documents

| Document Number | Title | Version |
|---|---|---|
| [Ref-1] | ARINC/IMA/Avionics refs | see **[STANDARDS/02-AIRCRAFT/AVIONICS_INTERFACES/](../../STANDARDS/02-AIRCRAFT/AVIONICS_INTERFACES/)** |
| [Ref-2] | DO-160 environmental | **[STANDARDS/02-AIRCRAFT/ENVIRONMENTAL_TEST/](../../STANDARDS/02-AIRCRAFT/ENVIRONMENTAL_TEST/)** |
| [Ref-3] | ECSS data links | **[STANDARDS/03-SPACECRAFT/COMM_LINKS/](../../STANDARDS/03-SPACECRAFT/COMM_LINKS/)** |
| [Ref-4] | Program baselines | **[CONFIG_MGMT/04-BASELINES/](../04-BASELINES/)** |
| [Ref-5] | Data dictionary | **[DIGITAL_THREAD/06-DATA_MANAGEMENT/DATA_DICTIONARY.csv](../../DIGITAL_THREAD/06-DATA_MANAGEMENT/DATA_DICTIONARY.csv)** |

## 2. Interface Overview

### 2.1 Interface Description
[High-level description of the interface]

### 2.2 Interface Diagram

```
┌─────────────────┐         ┌─────────────────┐
│                 │         │                 │
│    Party A      │◄───────►│    Party B      │
│                 │         │                 │
└─────────────────┘         └─────────────────┘
```

### 2.3 Interface Classification
- **Type:** [Physical | Electrical | Mechanical | Software | Data | Functional]
- **Criticality:** [Critical | Essential | Important | Standard]
- **Complexity:** [Simple | Moderate | Complex]

## 3. Interface Requirements

### 3.1 Functional Requirements

| Req ID | Requirement | Source | Verification Method |
|---|---|---|---|
| ICD-XXXX-FR-001 | [Functional requirement] | [Spec/Stakeholder/MBSE] | [Test/Analysis/Demo/Inspection] |
| | | | |

### 3.2 Performance Requirements

| Req ID | Parameter | Value | Tolerance | Units | Rationale |
|---|---|---|---|---|---|
| ICD-XXXX-PR-001 | [Parameter] | [Value] | ±[Tol] | [Units] | [Why] |
| | | | | | |

### 3.3 Interface Constraints

| Constraint | Description |
|---|---|
| [Constraint name] | [Description] |
| | |

## 4. Physical Interface

### 4.1 Mechanical Interface

#### 4.1.1 Mounting and Attachment
- **Mounting Points:** [Description and coordinates]
- **Bolt Pattern:** [Specifications]
- **Load Transfer:** [Load paths and values]
- **Torque Requirements:** [Torque values]

#### 4.1.2 Envelope and Clearances
- **Dimensions:** [L × W × H]
- **Keep-Out Zones:** [Description]
- **Access Requirements:** [Installation/maintenance]

#### 4.1.3 Materials and Finishes
- **Materials:** [At interface]
- **Surface Finish:** [Requirements]
- **Corrosion Prevention:** [Measures]

### 4.2 Thermal Interface
- **Heat Transfer:** [Heat flux, W/m²]
- **Temperature Limits:** [Min/Max]
- **Thermal Conductivity:** [Reqs]
- **Cooling/Heating:** [Active control]

### 4.3 Structural Interface
- **Load Cases:** [Static/dynamic]
- **Structural Modes:** [Natural freq]
- **Stiffness Requirements:** [Values]
- **Stress Limits:** [Allowables]

## 5. Electrical Interface

### 5.1 Power Interface

| Parameter | Specification | Min | Nom | Max | Units |
|---|---|---|---|---|---|
| Voltage | [DC/AC] | | | | V |
| Current | [Load profile] | | | | A |
| Power | [Budget] | | | | W |
| Frequency | [If AC] | | | | Hz |

### 5.2 Signal Interface

| Signal Name | Type | Direction | Voltage Levels | Frequency | Protocol |
|---|---|---|---|---|---|
| [Signal] | [Digital/Analog] | [A→B/B→A] | [Levels] | [Freq] | [Protocol] |
| | | | | | |

### 5.3 Connector Specifications

| Connector | Part Number | Pin Count | Mating Connector | Location |
|---|---|---|---|---|
| [Designator] | [P/N] | [Count] | [Mate P/N] | [Location] |
| | | | | |

### 5.4 Cable/Harness Specifications
- **Cable Type:** [Spec]
- **Length:** [Req]
- **Routing:** [Req]
- **Shielding:** [Req]

### 5.5 Grounding and EMI/EMC
- **Grounding Scheme:** [Single/Multi-point]
- **EMI Requirements:** see **[STANDARDS/02-AIRCRAFT/ENVIRONMENTAL_TEST/](../../STANDARDS/02-AIRCRAFT/ENVIRONMENTAL_TEST/)** and **[STANDARDS/03-SPACECRAFT/ELECTRICAL_EMC/](../../STANDARDS/03-SPACECRAFT/ELECTRICAL_EMC/)**  
- **Shielding Requirements:** [Specs]

## 6. Data Interface

### 6.1 Communication Protocol
- **Protocol:** [1553/429/Ethernet/CAN/etc.] — refs **[STANDARDS/02-AIRCRAFT/AVIONICS_INTERFACES/](../../STANDARDS/02-AIRCRAFT/AVIONICS_INTERFACES/)**  
- **Data Rate:** [bps]  
- **Message Format:** [Spec]

### 6.2 Data Items

| Data Item | Description | Type | Rate | Units | Range |
|---|---|---|---|---|---|
| [Item] | [Description] | [Type] | [Hz] | [Units] | [Min–Max] |
| | | | | | |

### 6.3 Command Interface

| Command | Description | Parameters | Response |
|---|---|---|---|
| [Command] | [Description] | [Params] | [Response] |
| | | | |

### 6.4 Timing Requirements
- **Latency:** [Max]  
- **Update Rate:** [Hz]  
- **Synchronization:** [PTP/IRIG/1PPS] — see **[DIGITAL_THREAD/03-ARCHITECTURE/INTEGRATION_POINTS.md](../../DIGITAL_THREAD/03-ARCHITECTURE/INTEGRATION_POINTS.md)**

## 7. Fluid/Pneumatic Interface (if applicable)

| Parameter | Specification | Min | Nom | Max | Units |
|---|---|---|---|---|---|
| Fluid Type | [Fluid] | N/A | N/A | N/A | - |
| Pressure | [Operating] | | | | PSI/bar |
| Flow Rate | [Flow] | | | | L/min |
| Temperature | [Operating] | | | | °C |
| Connection Type | [Fitting] | N/A | N/A | N/A | - |

## 8. Software Interface (if applicable)

### 8.1 Software Architecture
[Describe SW interface architecture]

### 8.2 APIs and Function Calls

| Function | Description | Parameters | Return Value |
|---|---|---|---|
| [Function()] | [Description] | [Params] | [Return] |
| | | | |

### 8.3 Data Structures

```c
struct InterfaceData {
  // Define data structures
};
```

### 8.4 Error Handling
[Describe error handling at interface]

## 9. Environmental Conditions

| Condition   | Operating    | Non-Operating | Test Margin |
| ----------- | ------------ | ------------- | ----------- |
| Temperature | [Range] °C   | [Range] °C    | [Margin]    |
| Humidity    | [Range] % RH | [Range] % RH  | [Margin]    |
| Pressure    | [Range] kPa  | [Range] kPa   | [Margin]    |
| Vibration   | [Spec]       | [Spec]        | [Margin]    |
| Shock       | [Spec]       | [Spec]        | [Margin]    |

## 10. Safety and Hazards

### 10.1 Hazard Analysis
[Identify interface-related hazards]

| Hazard ID | Description   | Severity  | Mitigation   |
| --------- | ------------- | --------- | ------------ |
| [ID]      | [Description] | [S/E/I/M] | [Mitigation] |
|           |               |           |              |

### 10.2 Safety Requirements
[Interface safety requirements] — link to **[QUALITY_QMS/13-RISK_SAFETY/](../../QUALITY_QMS/13-RISK_SAFETY/)**

## 11. Verification and Validation

### 11.1 Verification Methods

| Requirement ID | Verification Method          | Success Criteria | Responsible Party |
| -------------- | ---------------------------- | ---------------- | ----------------- |
| [Req ID]       | [Test/Analysis/Demo/Inspect] | [Criteria]       | [Party]           |
|                |                              |                  |                   |

Traceability to reqs and tests: **[CONFIG_MGMT/10-TRACEABILITY/](../10-TRACEABILITY/)**

### 11.2 Interface Testing
[Approach] — rigs/ATE refs: **[INDUSTRIALISATION/10-TEST_INSPECTION/](../../INDUSTRIALISATION/10-TEST_INSPECTION/)**

### 11.3 Integration Plan
[Approach and sequence]

## 12. Configuration Management

### 12.1 Change Control
Changes require **ECR** → **ECO** → **CCB** approval.  
Links: **[ECR/](../06-CHANGES/ECR/)** · **[ECO/](../06-CHANGES/ECO/)** · **[CCB](../05-CCB/)**

### 12.2 Baseline
This ICD is baselined at: **[04-BASELINES/](../04-BASELINES/)**

### 12.3 Related ECRs/ECOs

| ECR/ECO Number | Description   | Status   | Date   |
| -------------- | ------------- | -------- | ------ |
| [Number]       | [Description] | [Status] | [Date] |
|                |               |          |        |

## 13. Open Issues and TBDs

| Item    | Description         | Action Required | Owner   | Due Date |
| ------- | ------------------- | --------------- | ------- | -------- |
| TBD-001 | [Issue description] | [Action]        | [Owner] | [Date]   |
|         |                     |                 |         |          |

## 14. Notes and Assumptions
- [Assumptions]
- [Limitations]
- [Dependencies]

## Appendices

### Appendix A: Interface Drawing
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/f42d28f7-08bc-40da-bcf3-f9a06565b154" />


### Appendix B: Pin Lists

> Replace bracketed fields. Keep shield terminations consistent with EMI/EMC policy.

#### J1 — Power Connector *(MIL-DTL-38999, Series III, [shell/keying])*

| Pin | Signal        | Type   | Level/Spec | Wire (AWG) | Color | Notes                         |
| --- | ------------- | ------ | ---------- | ---------- | ----- | ----------------------------- |
| A   | +28VDC_MAIN   | Power  | 22–36 Vdc  | 16         | RED   | Feed from PSU A               |
| B   | RTN_MAIN      | Return | 0 V        | 16         | BLACK | Bond to **power return**      |
| C   | CHASSIS_GND   | Ground | —          | 18         | GREEN | To structure per bonding spec |
| D   | +28VDC_BACKUP | Power  | 22–36 Vdc  | 18         | ORG   | Optional                      |
| E   | RTN_BACKUP    | Return | 0 V        | 18         | BRN   | Optional                      |
| F   | DISCRETE_EN   | Input  | 28 Vdc     | 22         | YEL   | High = enable                 |
| G   | N/C           | —      | —          | —          | —     | Reserve                       |
| H   | N/C           | —      | —          | —          | —     | Reserve                       |

#### J2 — Data Bus *(ARINC 429, 2 channels)*

| Pin | Signal       | Type   | Dir | Level/Spec       | Cable           | Notes                      |
| --- | ------------ | ------ | --- | ---------------- | --------------- | -------------------------- |
| A   | TX1+         | Diff   | Out | ARINC 429 high   | 2× Twisted pair | Channel 1 TX               |
| B   | TX1−         | Diff   | Out | ARINC 429 low    |                 |                            |
| C   | RX1+         | Diff   | In  | ARINC 429 high   | 2× Twisted pair | Channel 1 RX               |
| D   | RX1−         | Diff   | In  | ARINC 429 low    |                 |                            |
| E   | TX2+         | Diff   | Out | ARINC 429 high   |                 | Channel 2 TX               |
| F   | TX2−         | Diff   | Out | ARINC 429 low    |                 |                            |
| G   | RX2+         | Diff   | In  | ARINC 429 high   |                 | Channel 2 RX               |
| H   | RX2−         | Diff   | In  | ARINC 429 low    |                 |                            |
| S   | SHIELD_DRAIN | Shield | —   | 360° @ backshell | Foil+braid      | To chassis at one end only |

Refs: **[STANDARDS/02-AIRCRAFT/AVIONICS_INTERFACES/](../../STANDARDS/02-AIRCRAFT/AVIONICS_INTERFACES/)**

#### J3 — Ethernet *(RJ45, T568B)*

| Pin | Signal | Dir | Notes                      |
| --- | ------ | --- | -------------------------- |
| 1   | BI_DA+ | ↔   | 100/1000BASE-T             |
| 2   | BI_DA− | ↔   |                            |
| 3   | BI_DB+ | ↔   |                            |
| 4   | BI_DC+ | ↔   | 1000BASE-T                 |
| 5   | BI_DC− | ↔   |                            |
| 6   | BI_DB− | ↔   |                            |
| 7   | BI_DD+ | ↔   | 1000BASE-T                 |
| 8   | BI_DD− | ↔   |                            |
| —   | SHELL  | —   | Shield to chassis via jack |

#### J4 — Discrete I/O *(Micro-D 25-pin)*

| Pin  | Signal  | Type     | Level/Spec | Dir | Pull | Notes         |
| ---- | ------- | -------- | ---------- | --- | ---- | ------------- |
| 1    | DO1     | Discrete | 0/28 Vdc   | Out | —    | High-side     |
| 2    | DO2     | Discrete | 0/28 Vdc   | Out | —    |               |
| 3    | DI1     | Discrete | 0/28 Vdc   | In  | 10k  | Active-high   |
| 4    | DI2     | Discrete | 0/28 Vdc   | In  | 10k  |               |
| 5    | BIT_OUT | Status   | Open-drain | Out | —    | Built-in test |
| 6    | REF_GND | Return   | 0 V        | —   | —    | I/O return    |
| 7–25 | N/C     | —        | —          | —   | —    | Reserve       |

---

#### Shielding and Grounding Rules

* 360° shield termination at connector backshell; single-point bond strategy per EMI plan.
* Power return and chassis ground separation per ICD Section 5.5; bond at designated star point.
* Maintain pair twist to within 13 mm of contacts for ARINC/Ethernet.
* Label cables with **PN/SN** and **length**; record in **[CONFIG_MGMT/08-ITEM_MASTER/](../08-ITEM_MASTER/)**.

#### Cable Assembly BOM (extract)

| Item PN | Description             | Qty    | Spec/Std      | Notes |
| ------- | ----------------------- | ------ | ------------- | ----- |
| [PN-C1] | 38999 plug, size [x]    | 1      | MIL-DTL-38999 | J1    |
| [PN-C2] | Micro-D 25 plug         | 1      | MIL-DTL-83513 | J4    |
| [PN-W1] | 2× Twisted Pair, shield | As req | ARINC cable   | J2    |
| [PN-B1] | Backshell, shield clamp | 2      | EMI 360°      | J1/J2 |

#### Compliance references

* EMI/EMC: **[STANDARDS/02-AIRCRAFT/ENVIRONMENTAL_TEST/](../../STANDARDS/02-AIRCRAFT/ENVIRONMENTAL_TEST/)** · **[STANDARDS/03-SPACECRAFT/ELECTRICAL_EMC/](../../STANDARDS/03-SPACECRAFT/ELECTRICAL_EMC/)**
* Avionics links: **[STANDARDS/02-AIRCRAFT/AVIONICS_INTERFACES/](../../STANDARDS/02-AIRCRAFT/AVIONICS_INTERFACES/)**

> Lock final pin maps at **[CONFIG_MGMT/04-BASELINES/](../04-BASELINES/)** and route changes via **[../06-CHANGES/ECR/](../06-CHANGES/ECR/)** → **[../06-CHANGES/ECO/](../06-CHANGES/ECO/)**.


### Appendix C: Signal Timing Diagrams
<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/ac989ab1-34ca-47ef-96f5-70357d1c5795" />
This image displays four distinct **Signal Timing Diagrams** for common digital communication protocols, labeled a) through d). Here's a breakdown of each:

---

### **a) SPI Mode 0 Timing**

*   **Signals:** SCLK (Serial Clock), MOSI (Master Out Slave In), MISO (Master In Slave Out)
*   **Mode 0 Characteristics:**
    *   **Clock Polarity (CPOL):** SCLK is idle LOW.
    *   **Clock Phase (CPHA):** Data is sampled on the **rising edge** of SCLK and changed on the falling edge.
*   **Timing Parameters Shown:**
    *   `S_u` (Setup Time): The minimum time data (MOSI/MISO) must be stable *before* the active clock edge (rising edge for Mode 0).
    *   `t_H` (Hold Time): The minimum time data (MOSI/MISO) must remain stable *after* the active clock edge (rising edge for Mode 0).

---

### **b) I²C Timing**

*   **Signals:** SDA (Serial Data Line), UART (likely meant to represent SCL - Serial Clock Line; "UART" here is probably a labeling error or placeholder for the clock signal in this context).
*   **Key Events:**
    *   **Start Condition:** SDA transitions from HIGH to LOW while SCL is HIGH.
    *   **Stop Condition:** SDA transitions from LOW to HIGH while SCL is HIGH.
    *   **Acknowledge (Ack):** After receiving a byte, the slave pulls SDA LOW during the 9th clock pulse (while SCL is HIGH) to acknowledge receipt. If SDA remains HIGH, it's a Not Acknowledge (NACK).
*   **Timing Parameter Shown:**
    *   `t_CLL` (Clock Low Time): The minimum duration the SCL line must remain LOW during a clock cycle.

---

### **c) UART Timing**

*   **Configuration:** "8 N 1" indicates 8 data bits, No parity, 1 stop bit.
*   **Frame Structure:**
    *   A frame starts with a **START bit** (LOW).
    *   Followed by 8 **DATA bits** (transmitted LSB first).
    *   Ends with a **STOP bit** (HIGH).
*   **Timing Parameters Shown:**
    *   **Bit Period:** The duration of one bit (start, data, or stop bit). This defines the baud rate (`Baud Rate = 1 / Bit Period`).
    *   **Frame:** The complete transmission unit, encompassing the start bit, data bits, and stop bit.

---

### **d) ARINC 429 Word**

*   **Word Structure:** An ARINC 429 word consists of 32 bits transmitted serially.
*   **Fields:**
    *   **Sync Gap:** A period before the word transmission begins, often used for synchronization or indicating the end of the previous word. (Note: The diagram shows a gap *before* the label field, which is consistent with the sync gap being part of the word structure or inter-word spacing).
    *   **5 Label:** 5 bits identifying the type of data contained in the word.
    *   **24 Data:** 24 bits containing the actual data payload.
    *   **Parity:** 1 bit (usually odd parity) for error detection over the entire 32-bit word.
*   **Timing Parameter Shown:**
    *   **Bit Time:** The duration of one bit within the ARINC 429 word. The standard bit rate is typically 12.5 kbps or 100 kbps, defining this time.

---

These diagrams are essential references for understanding the electrical and temporal characteristics required for implementing or debugging these communication interfaces.

### Appendix D: Test Procedures

Scope: verify Party A ⇄ Party B interface meets functional, electrical, timing, EMC, and environmental requirements defined in this ICD.

#### D.1 References

* Functional/req trace: **[../10-TRACEABILITY/](../10-TRACEABILITY/)**
* Rigs/ATE, procedures, reports: **[../../INDUSTRIALISATION/10-TEST_INSPECTION/](../../INDUSTRIALISATION/10-TEST_INSPECTION/)**
* DO-160 env/EMI: **[../../STANDARDS/02-AIRCRAFT/ENVIRONMENTAL_TEST/](../../STANDARDS/02-AIRCRAFT/ENVIRONMENTAL_TEST/)**
* ECSS EMC: **[../../STANDARDS/03-SPACECRAFT/ELECTRICAL_EMC/](../../STANDARDS/03-SPACECRAFT/ELECTRICAL_EMC/)**
* Templates: **[../../INDUSTRIALISATION/18-TEMPLATES/](../../INDUSTRIALISATION/18-TEMPLATES/)**

#### D.2 Configuration Under Test (CUT)

* HW: ICD-XXXX, Rev [X]; cable PN [ ], length [ ].
* SW/FW: build [ ], checksum [ ].
* Baseline: **[../04-BASELINES/CDR/](../04-BASELINES/CDR/)** or later.
* Instrumentation: scope, logic analyzer, PSU, EMC probes.

#### D.3 Test Setup

* Topology: A ⇄ harness ⇄ B; star ground per §5.5.
* Power: 28 Vdc (22–36 V) with current limit.
* Clocks/time: PTP/1 PPS if required.
* Shield terminations: 360° at backshell; single-point bond.

#### D.4 Test Matrix (sample)

| ID    | Objective           | Method                             | Limits                     | Evidence    |
| ----- | ------------------- | ---------------------------------- | -------------------------- | ----------- |
| TP-01 | Power-up sequencing | Apply 0→28 V, log inrush, brownout | I_inrush ≤ [ ] A; no reset | CSV + scope |
| TP-02 | Link bring-up       | ARINC/CAN/Eth handshake            | Link up ≤ [ ] ms           | PCAP/log    |
| TP-03 | Latency             | Step input → output time           | ≤ [ ] ms @ [rate]          | Time log    |
| TP-04 | Throughput          | Sustained data rate                | ≥ [ ] bps w/ BER≤1e-9      | PCAP/BER    |
| TP-05 | Error handling      | CRC/frame faults                   | Detect/log within [ ] ms   | Fault log   |
| TP-06 | Power margins       | 22/36 V, ±10% freq (if AC)         | Pass functional            | Checklist   |
| TP-07 | Cable/continuity    | Pin map, shield                    | Per Appendix B             | Report      |
| TP-08 | Environmental       | DO-160/ECSS per profile            | Pass criteria              | Lab report  |
| TP-09 | EMC                 | Emissions/immunity                 | Per spec                   | EMC report  |
| TP-10 | Safety interlocks   | Faults inhibited                   | No unsafe actuation        | Test log    |

#### D.5 Procedure Template (example TP-02)

1. Pre-reqs: calibration in date; CUT identity recorded; ESD controls set.
2. Configure A/B to nominal; connect analyzer.
3. Apply power; start capture.
4. Issue link init; record time to “LINK_UP”.
5. Verify message format per §6; check heartbeat loss behavior.
6. Restore to safe; archive artifacts.
   Acceptance: link ≤ [ ] ms; no protocol errors > [ ] per [min].

#### D.6 Environmental & EMC

* Run per profile mapped from requirements. Use chambers/EMI facilities listed in **[../../INDUSTRIALISATION/10-TEST_INSPECTION/NDT/](../../INDUSTRIALISATION/10-TEST_INSPECTION/NDT/)** and **FUNCTIONAL_TEST**.
* Capture chamber setpoints, dwell, tolerances. Link formal reports.

#### D.7 Fault Injection

* Power dips (−[ ]% for [ ] ms), line shorts/opens, stuck-at bits, packet loss [ ]%.
* Criteria: safe state within [ ] ms; flags raised; recovery without manual reset unless specified.

#### D.8 Data Capture & Records

* Store raw PCAP/CSV, scope traces, configs, photos.
* Name: `ICD-XXXX_TP-##_[date]_Rev[X]`.
* Register all artifacts under release: **[../07-RELEASES/](../07-RELEASES/)** and trace in **[../10-TRACEABILITY/](../10-TRACEABILITY/)**.

#### D.9 Nonconformance & Changes

* Log NCRs in **[../../QUALITY_QMS/06-NCR_CAPA/NCR/](../../QUALITY_QMS/06-NCR_CAPA/NCR/)**.
* Required design/process updates via **[../06-CHANGES/ECR/](../06-CHANGES/ECR/)** → **[../06-CHANGES/ECO/](../06-CHANGES/ECO/)**, then re-test.

#### D.10 Test Readiness & Completion

* TRR package: procedures, hazards, FMEA excerpt, calibration, waivers → **[../04-BASELINES/TRR/](../04-BASELINES/TRR/)**.
* Completion: signed report, results matrix, deviations, final disposition; file under **[../11-AUDITS/](../11-AUDITS/)**.

> Lock this appendix at baseline; any edits require CCB approval (**[../05-CCB/](../05-CCB/)**).


---

**Maintained By:** Interface parties & **[Configuration Management](../)**  
**Review Frequency:** [Quarterly or as needed]
```

