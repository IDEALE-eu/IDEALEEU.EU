# 39-40 · REMOTE_POWER_CONTROLLERS_RPC — EBOM LINKS (Q10)

**Scope:** Distributed solid-state power controllers (RPCs/SSPCs) for load switching, current limiting, and fault isolation.  
**Rule:** Physical HW lives here (39-40). Control algorithms in **39-60**. FSW in **42**. No code stored here.

---

## 1) Assemblies (39-40 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 39-40-ASSY-RPC-8CH     | 8-Channel Remote Power Controller            | ASSY  | `CAx/CAD/assy_rpc_8ch.step`           | REL    |
| 39-40-ASSY-SSPC-SINGLE | Single-Channel Solid-State Power Controller  | ASSY  | `CAx/CAD/assy_sspc_single.step`       | REL    |
| 39-40-ASSY-CURR-LIM    | Current Limiter Module                       | ASSY  | `CAx/CAD/assy_curr_lim.step`          | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 39-40-MOSFET-N-100V     | N-channel MOSFET 100V 50A             | RPC-8CH           | `CAx/CAD/mosfet_n_100v.step`       | Rds(on) < 5mΩ   |
| 39-40-IC-GATE-DRV       | MOSFET gate driver IC                 | RPC-8CH           | `CAx/CAD/ic_gate_drv.step`         | Isolated        |
| 39-40-SENS-CURR-SHUNT   | Current shunt 0.1 mΩ 50A              | CURR-LIM          | `CAx/CAD/sens_curr_shunt.step`     | Accuracy 1%     |
| 39-40-IC-COMP-ILIM      | Current limit comparator IC           | CURR-LIM          | `CAx/CAD/ic_comp_ilim.step`        | Fast response   |

---

## 3) Cross-references
- **Thermal derating**: `CAx/CAE/thermal_rpc_Q10.xlsx`
- **Current limiting curves**: `CAx/CMP/current_limit_curves.pdf`
- **FDIR logic**: See **39-60_ALGORITHMS_CONTROL**
- **Fault injection testing**: `CAx/CAV/fault_injection_report.pdf`

---

## 4) Configuration notes
- Switching technology: N-channel MOSFETs (solid-state)
- Current range: 1–50 A per channel
- Trip time: < 10 µs (overcurrent)
- Retry logic: Configurable (0–3 retries with backoff)
- Telemetry: Per-channel current, voltage, temperature
