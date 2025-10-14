---
area: "02-AIRCRAFT/.../DOMAIN/AAP"
title: "Airport Adaptable Platforms — Integration View"
owner: "Ground Ops & Interfaces"
status: "Baseline-Candidate"
baseline: "Q100_STD01"
effectivity: "MSN 0001–9999"
utcs_anchor: "utcs://AIRCRAFT/AMPEL360-AIR-T/AAP/Q100_STD01/INTEGRATION_VIEW"
confidentiality: "Internal"
---

# AAP · Airport Adaptable Platforms — Integration View

## 1. Purpose
Enable **BWB-H2-Hy-E** operation at **existing or minimally adapted airports**. Focus on **ground handling, power, data, hydrogen safety, time sync, and emergency interfaces**.

## 2. Scope
- **Inward**: aircraft systems for parking, mooring, H₂ handling, power, comms.
- **Outward**: GSE, terminal IT, ramp safety systems, master clock.
- **Out of scope**: airfield lighting, runway geometry, ATC airspace procedures.

## 3. TBUS convention
`TBUS-AIR-<CLASS>-<SUBCLASS>` (mechanical, power, gas-safety, data, time, safety-estop).

## 4. Key Interfaces (overview)
| IF ID     | Source (Aircraft)                | Sink (Airport/GSE)          | TBUS Type                 | Protocol/Standard                                        | Dir |
|-----------|----------------------------------|-----------------------------|---------------------------|----------------------------------------------------------|-----|
| AAP-IF-01 | Mooring Actuator                 | Automated Mooring Unit      | TBUS-AIR-MECH-DOCK        | AAP-DOCK-1001 geom & loads; IEC 61131-2 I/O              | Bi  |
| AAP-IF-02A| External Power Receptacle        | 115/200 VAC 400 Hz GPU      | TBUS-AIR-POWER-115/400    | ISO 6858; MIL-STD-704F                                   | In  |
| AAP-IF-02B| External Power Receptacle        | 28 VDC GPU                  | TBUS-AIR-POWER-28V        | ISO 6858; MIL-STD-704F                                   | In  |
| AAP-IF-03 | H₂ Purge & Vent Stack Telemetry  | H₂ Safety Monitoring Panel  | TBUS-AIR-GAS-SAFE         | ISO 19880-1/-3; IEC 60079-10-1; IEC 60079-29-1           | Out |
| AAP-IF-04 | Aircraft Health Monitor Gateway  | Ramp Operations Tablet      | TBUS-AIR-DATA-RAMP        | 802.11ax WPA3-Ent; HTTPS/REST (AFDX isolated behind GW)  | Out |
| AAP-IF-05 | Time Reference                   | Airport Master Clock        | TBUS-AIR-TIME             | IEEE 1588-2008 PTPv2; IRIG-B + 1 PPS fallback            | Bi  |
| AAP-IF-06 | Safety I/O (E-Stop input)        | Ramp Safety System          | TBUS-AIR-SAFETY-ESTOP     | ISO 13850 fail-safe dry contact, monitored loop          | In  |

> Full matrix: `INTERFACE_MATRIX/INTERFACE_MATRIX.csv`

## 5. CSV schema
`Interface_ID,Source,Sink,TBUS_Type,Protocol_Standard,Direction,Notes`

**Sample rows**
```

AAP-IF-01,Mooring Actuator,Automated Mooring Unit,TBUS-AIR-MECH-DOCK,"AAP-DOCK-1001; IEC 61131-2",Bi,"Docking geom + discrete I/O"
AAP-IF-02A,External Power Receptacle,115/200VAC 400Hz GPU,TBUS-AIR-POWER-115/400,"ISO 6858; MIL-STD-704F",In,"400 Hz preferred"
AAP-IF-02B,External Power Receptacle,28VDC GPU,TBUS-AIR-POWER-28V,"ISO 6858; MIL-STD-704F",In,"Optional DC supply"
AAP-IF-03,H2 Purge & Vent Stack Telemetry,H2 Safety Monitoring Panel,TBUS-AIR-GAS-SAFE,"ISO 19880-1/-3; IEC 60079-10-1; IEC 60079-29-1",Out,"Gas zoning + detectors"
AAP-IF-04,Aircraft Health Monitor GW,Ramp Ops Tablet,TBUS-AIR-DATA-RAMP,"802.11ax WPA3-Ent; HTTPS/REST",Out,"No direct AFDX on ramp"
AAP-IF-05,Time Reference,Airport Master Clock,TBUS-AIR-TIME,"IEEE 1588-2008; IRIG-B; 1PPS",Bi,"PTP primary"
AAP-IF-06,Safety I/O (E-Stop input),Ramp Safety System,TBUS-AIR-SAFETY-ESTOP,"ISO 13850",In,"Fail-safe, supervised"

```

## 6. Compliance anchors
- **Safety**: CS-25.1309; ARP4761A (FHA/PSSA/SSA for ground ops).
- **EMC/ESD/Lightning**: DO-160G Sec **20/21/22/19** per installation.
- **Hydrogen**: ISO 19880-1/-3; IEC 60079-10-1 (zoning); IEC 60079-29-1 (detectors).
- **Data security**: WPA3-Enterprise, TLS 1.3, cert pinning at ramp GW.

## 7. Verification
- **HIL**: mooring actuator + IEC 61131-2 I/O emulator; TBUS event logs.
- **Power**: load bank vs ISO 6858; transients per MIL-STD-704F.
- **Data**: RF survey, latency/throughput; ramp GW pen-test.
- **Time**: PTP GM/BC/OC conformance; IRIG-B holdover.
- **Safety**: injected H₂ leak → auto-purge + E-stop interlock timing.

## 8. Configuration
- **Product**: AMPEL360-AIR-T
- **Model**: BWB-H2-Hy-E
- **Version**: Q100_STD01
- **CMT-ID**: `AAP:Q100_STD01:R2`

## 9. Directory pointers
- `INTEGRATION_VIEW.md` (this file)
- `INTERFACE_MATRIX/INTERFACE_MATRIX.csv`
- `PLM/CAx/CAO/Mooring_Procedure_A3.pdf`
- `.../CONF/BASELINE/.../REQ_LINKS.csv` (AAP-REQ-001..042)

## 10. Change log
| Rev | Date       | Author     | Notes                                  |
|-----|------------|------------|----------------------------------------|
| R2  | 2025-10-14 | Interfaces | TBUS normalized; power/data/time/H₂ updated |
```

