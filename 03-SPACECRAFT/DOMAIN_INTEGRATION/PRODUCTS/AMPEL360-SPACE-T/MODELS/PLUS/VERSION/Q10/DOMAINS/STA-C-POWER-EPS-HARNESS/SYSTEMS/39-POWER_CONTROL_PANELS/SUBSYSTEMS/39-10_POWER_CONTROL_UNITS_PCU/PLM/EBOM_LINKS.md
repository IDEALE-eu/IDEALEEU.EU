# 39-10 · POWER_CONTROL_UNITS_PCU — EBOM LINKS (Q10)

**Scope:** Central power control units (PCUs) providing master control, sequencing, and coordination of spacecraft power distribution.  
**Rule:** Physical HW lives here (39-10). Remote switching in **39-40**. Algorithms in **39-60**. FSW in **42**. No code stored here.

---

## 1) Assemblies (39-10 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 39-10-ASSY-PCU-MAIN    | Main Power Control Unit                      | ASSY  | `CAx/CAD/assy_pcu_main.step`          | REL    |
| 39-10-ASSY-PCU-RED     | Redundant Power Control Unit                 | ASSY  | `CAx/CAD/assy_pcu_red.step`           | REL    |
| 39-10-ASSY-CTRL-IF     | Control Interface Board                      | ASSY  | `CAx/CAD/assy_ctrl_if.step`           | REL    |
| 39-10-ASSY-PWR-SEQ     | Power Sequencing Module                      | ASSY  | `CAx/CAD/assy_pwr_seq.step`           | RVW    |
| 39-10-ASSY-XSTR-SW     | Cross-strapping Switch Matrix                | ASSY  | `CAx/CAD/assy_xstr_sw.step`           | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 39-10-MCU-CTRL          | Control MCU (ARM Cortex-M7)           | PCU-MAIN          | `CAx/CAD/mcu_ctrl.step`            | Redundant pair  |
| 39-10-FPGA-SEQ          | Power sequencing FPGA                 | PWR-SEQ           | `CAx/CAD/fpga_seq.step`            | Custom logic    |
| 39-10-RELAY-XSTR        | Cross-strapping relay (latching)      | XSTR-SW           | `CAx/CAD/relay_xstr.step`          | 50A rated       |
| 39-10-IC-CAN-TRANS      | CAN transceiver IC                    | CTRL-IF           | `CAx/CAD/ic_can_trans.step`        | Isolated        |
| 39-10-CONN-CMD          | Command interface connector           | CTRL-IF           | `CAx/CAD/conn_cmd.step`            | MIL-DTL-38999   |

---

## 3) Cross-references
- **Control architecture**: `CAx/CAI/control_architecture.pdf`
- **Sequencing logic**: `CAx/CMP/sequencing_logic.xlsx`
- **FDIR implementation**: See **39-60_ALGORITHMS_CONTROL**
- **Interface to CDH**: `CAx/CAI/icd_pcu_cdh_v1.2.pdf`

---

## 4) Configuration notes
- Redundancy: Hot-swap redundant PCUs with automatic failover
- Command interface: CAN bus (1 Mbps) + SpaceWire backup
- Sequencing: Programmable power-up/down sequences (up to 32 steps)
- Fault detection: <100 ms response time
- Cross-strapping: Automatic bus transfer on primary bus failure
