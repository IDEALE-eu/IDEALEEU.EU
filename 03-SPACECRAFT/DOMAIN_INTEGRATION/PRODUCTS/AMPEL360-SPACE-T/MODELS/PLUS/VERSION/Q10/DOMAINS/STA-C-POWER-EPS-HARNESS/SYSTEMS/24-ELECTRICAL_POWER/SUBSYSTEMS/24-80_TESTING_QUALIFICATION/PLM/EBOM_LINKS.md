# 24-80 · TESTING & QUALIFICATION — ENGINEERING BOM LINKS (Q10)

**Scope:** This document lists the Engineering Bill of Materials (EBOM) for Ground Support Equipment (GSE), fixtures, and instrumentation owned by subsystem 24-80. Its purpose is the Assembly, Integration, and Test (AIT) of the Electrical Power System (EPS).

**Ownership Principle:** 24-80 does not own flight hardware. All items listed here are test-specific assets. Flight hardware is referenced from its authoritative subsystem EBOM for test context only.

---

## 1. Test Articles (Referenced, Not Owned by 24-80)

*These items are the Devices Under Test (DUT). Configuration and serial numbers are controlled by the host EBOM (Single Source of Truth - SSOT).*

| TA P/N        | Description                         | Host EBOM (SSOT)                                                                                      | Type | Status  |
|---------------|-------------------------------------|--------------------------------------------------------------------------------------------------------|------|---------|
| TA-24-30-EM01 | Power Distribution Unit EM          | [`../24-30_POWER_DISTRIBUTION/PLM/EBOM_LINKS.md`](../24-30_POWER_DISTRIBUTION/PLM/EBOM_LINKS.md)                                                       | EM   | IN_TEST |
| TA-24-60-QM01 | DCDC Converter QM                   | [`../24-60_CONVERTERS_DCDC_ACDC/PLM/EBOM_LINKS.md`](../24-60_CONVERTERS_DCDC_ACDC/PLM/EBOM_LINKS.md)                                                     | QM   | RVW     |
| TA-39-40-EM01 | Remote Power Controller Module EM   | [`../../39-POWER_CONTROL_PANELS/SUBSYSTEMS/39-40_REMOTE_POWER_CONTROLLERS_RPC/PLM/EBOM_LINKS.md`](../../39-POWER_CONTROL_PANELS/SUBSYSTEMS/39-40_REMOTE_POWER_CONTROLLERS_RPC/PLM/EBOM_LINKS.md)           | EM   | REL     |

---

## 2. EGSE - Electrical Ground Support Equipment (Owned by 24-80)

| Part Number              | Description                                  | Qty | PLM_UID        | CAx Ref(s)                        | Status |
|--------------------------|----------------------------------------------|-----|----------------|-----------------------------------|--------|
| EGSE-PSU-HV-001          | High-Voltage Power Supply (0–150 V, 50 A)    | 2   | PLM-24-80-001  | `CAx/CAD/egse_psu_hv.step`        | REL    |
| EGSE-PSU-28V-002         | 28 V Bus Simulator (0–35 V, 100 A)           | 1   | PLM-24-80-002  | `CAx/CAD/egse_psu_28v.step`       | REL    |
| EGSE-LOAD-PROG-001       | Programmable Electronic Load Bank (5 kW)     | 1   | PLM-24-80-003  | `CAx/CAD/egse_load_bank.step`     | REL    |
| EGSE-BAT-SIM-001         | Battery Simulator (Li-ion profile)           | 1   | PLM-24-80-004  | `CAx/CAD/egse_bat_sim.step`       | RVW    |
| EGSE-SOLAR-SIM-001       | Solar Array Simulator (I-V curve)            | 1   | PLM-24-80-005  | `CAx/CAD/egse_solar_sim.step`     | REL    |

---

## 3. Test Fixtures and Adapters (Owned by 24-80)

| Part Number              | Description                                  | Qty | PLM_UID        | CAx Ref(s)                        | Status |
|--------------------------|----------------------------------------------|-----|----------------|-----------------------------------|--------|
| FIX-PDU-IF-001           | PDU Interface Test Fixture                   | 1   | PLM-24-80-010  | `CAx/CAD/fix_pdu_if.step`         | REL    |
| FIX-DCDC-THERMAL-001     | DCDC Thermal Test Chamber Adapter            | 2   | PLM-24-80-011  | `CAx/CAD/fix_dcdc_thermal.step`   | REL    |
| FIX-HARNESS-CONT-001     | Harness Continuity Test Fixture              | 1   | PLM-24-80-012  | `CAx/CAD/fix_harness_cont.step`   | REL    |
| ADAPT-CONN-28V-001       | 28 V Connector Adapter (flight to EGSE)      | 5   | PLM-24-80-013  | `CAx/CAD/adapt_conn_28v.step`     | REL    |

---

## 4. Instrumentation and Data Acquisition (Owned by 24-80)

| Part Number              | Description                                  | Qty | PLM_UID        | CAx Ref(s)                        | Status |
|--------------------------|----------------------------------------------|-----|----------------|-----------------------------------|--------|
| INST-DMM-6.5D-001        | 6.5-digit Digital Multimeter                 | 4   | PLM-24-80-020  | *COTS: Keysight 34465A*           | REL    |
| INST-OSC-4CH-001         | 4-channel Oscilloscope (1 GHz BW)            | 2   | PLM-24-80-021  | *COTS: Tektronix MSO64*           | REL    |
| INST-PWR-METER-001       | Power Meter (DC, 0.1% accuracy)              | 2   | PLM-24-80-022  | *COTS: Yokogawa WT3000*           | REL    |
| INST-THERMAL-CAM-001     | Thermal Imaging Camera (IR)                  | 1   | PLM-24-80-023  | *COTS: FLIR A615*                 | REL    |
| DAQ-24BIT-001            | 24-bit Data Acquisition System (32 ch)       | 1   | PLM-24-80-024  | *COTS: NI cDAQ-9189*              | REL    |

---

## 5. Calibration Standards (Owned by 24-80)

| Part Number              | Description                                  | Qty | PLM_UID        | CAx Ref(s)                        | Status | Cal Due  |
|--------------------------|----------------------------------------------|-----|----------------|-----------------------------------|--------|----------|
| CAL-VOLT-REF-001         | Voltage Reference Standard (10 V, 1 ppm)     | 1   | PLM-24-80-030  | *COTS: Fluke 732B*                | REL    | 2025-Q2  |
| CAL-CURR-SHUNT-001       | Current Shunt Standard (100 A, 0.01%)        | 2   | PLM-24-80-031  | *COTS: Fluke A40B*                | REL    | 2025-Q3  |
| CAL-TEMP-RTD-001         | RTD Temperature Standard (-40 to +125°C)     | 1   | PLM-24-80-032  | *COTS: Fluke 5628*                | REL    | 2025-Q1  |

---

## 6. Test Procedures and Reports (CMP Artifacts)

| Test ID         | Title                                     | DUT(s)          | Test Stand     | Procedure                        | Report                          | Status   |
|-----------------|-------------------------------------------|-----------------|----------------|----------------------------------|---------------------------------|----------|
| TP-24-80-001    | PDU Functional Verification               | TA-24-30-EM01   | Stand A        | `CAx/CMP/tp_pdu_func_v1.2.pdf`   | `CAx/CMP/tr_pdu_func.pdf`       | COMPLETE |
| TP-24-80-002    | DCDC Thermal Qualification                | TA-24-60-QM01   | Chamber B      | `CAx/CMP/tp_dcdc_thermal_v1.0.pdf`| `CAx/CMP/tr_dcdc_thermal.pdf`   | COMPLETE |
| TP-24-80-003    | RPC Switching Performance                 | TA-39-40-EM01   | Stand C        | `CAx/CMP/tp_rpc_switch_v1.1.pdf` | `CAx/CMP/tr_rpc_switch.pdf`     | COMPLETE |
| TP-24-80-004    | EPS End-to-End Integration Test           | Multiple        | Stand D        | `CAx/CMP/tp_eps_e2e_v2.0.pdf`    | `CAx/CMP/tr_eps_e2e.pdf`        | IN_WORK  |

---

## 7. Test Stand Configurations

| Stand ID | Description                              | Location     | Key EGSE                                    | Status   |
|----------|------------------------------------------|--------------|---------------------------------------------|----------|
| Stand A  | PDU/Distribution Test Stand              | Lab 101      | EGSE-PSU-28V-002, EGSE-LOAD-PROG-001        | ACTIVE   |
| Stand B  | DCDC Converter Thermal Chamber           | Lab 102      | FIX-DCDC-THERMAL-001, INST-THERMAL-CAM-001  | ACTIVE   |
| Stand C  | RPC Switching Test Stand                 | Lab 101      | EGSE-PSU-28V-002, INST-OSC-4CH-001          | ACTIVE   |
| Stand D  | EPS End-to-End Integration Test Stand    | Integration  | EGSE-SOLAR-SIM-001, EGSE-BAT-SIM-001        | ACTIVE   |

---

## 8. Cross-References

- **Flight Hardware EBOMs**: See Section 1 links
- **Test Matrix**: `CAx/CAI/test_matrix_24-80.xlsx`
- **Qualification Plan**: `CAx/CMP/qual_plan_eps_Q10.pdf`
- **Calibration Schedule**: `CAx/CMP/calibration_schedule.xlsx`

---

## 9. Notes

1. **COTS Equipment**: Commercial Off-The-Shelf (COTS) instruments are maintained per manufacturer recommendations.
2. **Calibration**: All instrumentation calibrated annually by ISO 17025 accredited lab.
3. **Test Article Ownership**: DUTs remain under control of their host subsystem EBOMs.
4. **Configuration Control**: EGSE modifications require CCB approval (minor) or MRB (major).
5. **Safety**: All test stands comply with IEC 61010-1 electrical safety requirements.
