# 39-60 ALGORITHMS & CONTROL — LOGICAL COMPONENT REGISTRY  
*(Not an EBOM — No Physical Parts Owned)*

> **📌 Ownership Principle**:  
> All hardware and flight software reside with their **host LRUs**.  
> **39-60 owns only**:  
> - Algorithm specifications  
> - Configuration data  
> - Interface control definitions (ICDs)  
> - Verification evidence (CMP artifacts)

---

## 1. Hosted Hardware Components (Owned by Other Subsystems)

| Part Number  | Description                        | Host LRU                   | EBOM Path                                                                                      | Status        |
|--------------|------------------------------------|----------------------------|------------------------------------------------------------------------------------------------|---------------|
| MCU-RPC-001  | RPC Control MCU                    | 39-40_RPC                  | [`../39-40_REMOTE_POWER_CONTROLLERS_RPC/PLM/EBOM_LINKS.md`](../39-40_REMOTE_POWER_CONTROLLERS_RPC/PLM/EBOM_LINKS.md) | RELEASED      |
| FPGA-SEQ-001 | Sequencing FPGA                    | 39-10_PCU                  | [`../39-10_POWER_CONTROL_UNITS_PCU/PLM/EBOM_LINKS.md`](../39-10_POWER_CONTROL_UNITS_PCU/PLM/EBOM_LINKS.md)           | RELEASED      |

---

## 2. Algorithm Specifications (Owned by 39-60)

| Algorithm ID     | Description                              | Type              | Documentation                        | Status   |
|------------------|------------------------------------------|-------------------|--------------------------------------|----------|
| ALG-PWRSEQ-001   | Power Sequencing Logic                   | Control           | `CAx/CMP/spec_pwrseq_v1.0.pdf`       | RELEASED |
| ALG-LOADSHD-001  | Load Shedding Priority Management        | FDIR              | `CAx/CMP/spec_loadshd_v1.2.pdf`      | RELEASED |
| ALG-XSTR-001     | Cross-strapping Decision Logic           | FDIR              | `CAx/CMP/spec_xstr_v1.0.pdf`         | RELEASED |
| ALG-RPC-RETRY-001| RPC Retry Logic                          | FDIR              | `CAx/CMP/spec_rpc_retry_v1.1.pdf`    | RELEASED |

---

## 3. Configuration Parameters (Owned by 39-60)

| Parameter ID      | Description                         | Default Value | Range         | Unit | Documentation                     |
|-------------------|-------------------------------------|---------------|---------------|------|-----------------------------------|
| PARAM-SEQ-DELAY   | Inter-step sequencing delay         | 100           | 10 – 1000     | ms   | `CAx/CMP/params_sequencing.xlsx`  |
| PARAM-RPC-ILIM    | RPC current limit threshold         | 10.0          | 1.0 – 50.0    | A    | `CAx/CMP/params_rpc.xlsx`         |
| PARAM-RETRY-MAX   | Maximum retry attempts              | 3             | 0 – 10        | -    | `CAx/CMP/params_fdir.xlsx`        |
| PARAM-XSTR-TIME   | Cross-strap transfer time           | 50            | 10 – 200      | ms   | `CAx/CMP/params_xstr.xlsx`        |

---

## 4. Interface Control Documents (ICDs)

| ICD ID          | Title                                    | Version | Interfaces              | Documentation                     |
|-----------------|------------------------------------------|---------|-------------------------|-----------------------------------|
| ICD-RPC-CDH-001 | RPC ↔ C&DH Command Interface             | 1.0     | 39-60 ↔ 31-xx           | `CAx/CAI/icd_rpc_cdh_v1.0.pdf`    |
| ICD-PCU-FDIR-001| PCU FDIR Event Protocol                  | 1.1     | 39-60 ↔ 31-xx           | `CAx/CAI/icd_pcu_fdir_v1.1.pdf`   |

---

## 5. Verification Evidence (CMP Artifacts)

| Evidence ID      | Description                              | Type          | Location                              | Status   |
|------------------|------------------------------------------|---------------|---------------------------------------|----------|
| VER-SEQ-SIM-001  | Power Sequencing Simulation              | Simulation    | `CAx/CMP/ver_seq_simulink.slx`        | VERIFIED |
| VER-FDIR-HIL-001 | FDIR Hardware-in-Loop Test               | HIL Test      | `CAx/CMP/ver_fdir_hil_report.pdf`     | VERIFIED |

---

## 6. Notes

1. **No Physical Parts**: This subsystem owns no physical hardware.
2. **Algorithm Authority**: 39-60 is the SSOT for power control algorithms.
3. **Configuration Management**: Parameter changes require CCB approval.
