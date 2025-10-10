# 24-70 ALGORITHMS & CONTROL — LOGICAL COMPONENT REGISTRY  
*(Not an EBOM — No Physical Parts Owned)*

> **📌 Ownership Principle**:  
> All hardware and flight software reside with their **host LRUs**.  
> **24-70 owns only**:  
> - Algorithm specifications  
> - Configuration data  
> - Interface control definitions (ICDs)  
> - Verification evidence (CMP artifacts)

---

## 1. Hosted Hardware Components (Owned by Other Subsystems)

| Part Number  | Description                        | Host LRU                   | EBOM Path                                                                                                                                      | Status        |
|--------------|------------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| CTRL-FPU-001 | Floating Point Processing Unit     | 42-10_OBC_MAIN_BACKUP      | [`../../STA-F-AVIONICS-FSW-DATABUS/SYSTEMS/42-AVIONICS_COMPUTERS_IMA/SUBSYSTEMS/42-10_OBC_MAIN_BACKUP/PLM/EBOM_LINKS.md`](../../STA-F-AVIONICS-FSW-DATABUS/SYSTEMS/42-AVIONICS_COMPUTERS_IMA/SUBSYSTEMS/42-10_OBC_MAIN_BACKUP/PLM/EBOM_LINKS.md) | RELEASED      |
| FPGA-PWR-001 | Power Management FPGA              | 24-60_CONVERTERS_DCDC_ACDC | [`../24-60_CONVERTERS_DCDC_ACDC/PLM/EBOM_LINKS.md`](../24-60_CONVERTERS_DCDC_ACDC/PLM/EBOM_LINKS.md)                                            | IN_PRODUCTION |
| MEM-DDR-001  | DDR4 Memory Module 8GB             | 42-10_OBC_MAIN_BACKUP      | *(same as CTRL-FPU-001)*                                                                                                                       | RELEASED      |
| ADC-HS-001   | High-Speed ADC 16-bit              | 24-30_POWER_DISTRIBUTION   | [`../24-30_POWER_DISTRIBUTION/PLM/EBOM_LINKS.md`](../24-30_POWER_DISTRIBUTION/PLM/EBOM_LINKS.md)                                                | RELEASED      |

---

## 2. Algorithm Specifications (Owned by 24-70)

| Algorithm ID     | Description                              | Type              | Documentation                        | Status   |
|------------------|------------------------------------------|-------------------|--------------------------------------|----------|
| ALG-MPPT-001     | Maximum Power Point Tracking             | Control           | `CAx/CMP/spec_mppt_v2.1.pdf`         | RELEASED |
| ALG-BATCHG-001   | Battery Charge Management                | Control           | `CAx/CMP/spec_batchg_v1.3.pdf`       | RELEASED |
| ALG-LOADSHD-001  | Load Shedding Priority Logic             | FDIR              | `CAx/CMP/spec_loadshd_v1.0.pdf`      | REVIEW   |
| ALG-PWRBUDG-001  | Real-time Power Budget Monitor           | Monitoring        | `CAx/CMP/spec_pwrbudg_v1.1.pdf`      | RELEASED |
| ALG-SAFEPWR-001  | Safe Mode Power Configuration            | FDIR              | `CAx/CMP/spec_safepwr_v2.0.pdf`      | RELEASED |

---

## 3. Configuration Parameters (Owned by 24-70)

| Parameter ID      | Description                         | Default Value | Range         | Unit | Documentation                     |
|-------------------|-------------------------------------|---------------|---------------|------|-----------------------------------|
| PARAM-MPPT-STEP   | MPPT voltage step size              | 0.5           | 0.1 – 2.0     | V    | `CAx/CMP/params_mppt.xlsx`        |
| PARAM-BAT-VMAX    | Battery max charge voltage          | 33.6          | 32.0 – 34.0   | V    | `CAx/CMP/params_battery.xlsx`     |
| PARAM-BAT-VMIN    | Battery min discharge voltage       | 24.0          | 22.0 – 25.0   | V    | `CAx/CMP/params_battery.xlsx`     |
| PARAM-LOAD-CRIT   | Critical load current threshold     | 15.0          | 10.0 – 20.0   | A    | `CAx/CMP/params_loadshed.xlsx`    |
| PARAM-PWR-MARGIN  | Power budget safety margin          | 15            | 10 – 25       | %    | `CAx/CMP/params_budget.xlsx`      |

---

## 4. Interface Control Documents (ICDs)

| ICD ID          | Title                                    | Version | Interfaces              | Documentation                     |
|-----------------|------------------------------------------|---------|-------------------------|-----------------------------------|
| ICD-PWR-CDH-001 | Power ↔ C&DH Data Interface              | 2.1     | 24-70 ↔ 31-xx           | `CAx/CAI/icd_pwr_cdh_v2.1.pdf`    |
| ICD-PWR-THERM-001| Power ↔ Thermal Telemetry               | 1.0     | 24-70 ↔ 42-xx           | `CAx/CAI/icd_pwr_therm_v1.0.pdf`  |
| ICD-PWR-FDIR-001| Power FDIR Event Protocol                | 1.2     | 24-70 ↔ 31-xx           | `CAx/CAI/icd_pwr_fdir_v1.2.pdf`   |

---

## 5. Flight Software Components (Owned by Host Systems)

| SW Module ID    | Description                         | Host System             | FSW Repository                                | Status   |
|-----------------|-------------------------------------|-------------------------|-----------------------------------------------|----------|
| FSW-MPPT-001    | MPPT Control Loop                   | 42-10_OBC_MAIN_BACKUP   | `git://repo/fsw-eps-mppt.git`                 | RELEASED |
| FSW-BATMGMT-001 | Battery Management FSW              | 42-10_OBC_MAIN_BACKUP   | `git://repo/fsw-eps-batmgmt.git`              | RELEASED |
| FSW-PWRMON-001  | Power Monitoring & Telemetry        | 42-10_OBC_MAIN_BACKUP   | `git://repo/fsw-eps-monitor.git`              | RELEASED |

*All FSW is version-controlled externally. Evidence artifacts (test reports, V&V) stored in `CAx/CMP/`.*

---

## 6. Verification Evidence (CMP Artifacts)

| Evidence ID      | Description                              | Type          | Location                              | Status   |
|------------------|------------------------------------------|---------------|---------------------------------------|----------|
| VER-MPPT-SIM-001 | MPPT Algorithm MATLAB/Simulink Model     | Simulation    | `CAx/CMP/ver_mppt_simulink.slx`       | VERIFIED |
| VER-BATCHG-HIL-001| Battery Charge HIL Test Results         | HIL Test      | `CAx/CMP/ver_batchg_hil_report.pdf`   | VERIFIED |
| VER-LOADSHD-FTA-001| Load Shedding Fault Tree Analysis       | Safety        | `CAx/CMP/ver_loadshd_fta.xlsx`        | REVIEW   |
| VER-PWRBUDG-LOG-001| Power Budget Telemetry Logs (Flight)    | Flight Data   | `CAx/CMP/ver_pwrbudg_flight_logs.csv` | ARCHIVED |

---

## 7. Cross-References

- **Host Hardware EBOMs**: See links in Section 1
- **FSW Repositories**: See Section 5
- **Algorithm Baseline**: `CAx/CMP/algorithm_baseline_Q10.pdf`
- **Traceability Matrix**: `CAx/CAI/traceability_matrix_24-70.xlsx`

---

## 8. Notes

1. **No Physical Parts**: This subsystem owns no physical hardware. All HW is referenced from host subsystems.
2. **Algorithm Authority**: 24-70 is the Single Source of Truth (SSOT) for algorithm specifications and parameters.
3. **FSW Hosting**: All executable code resides in 42-10 (OBC) or distributed controllers in 24-60.
4. **Configuration Management**: Parameter changes require formal CCB approval and version control.
5. **Verification**: CMP directory contains all V&V evidence for algorithm performance and safety.
