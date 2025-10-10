# 24-30 · POWER_DISTRIBUTION — EBOM LINKS (Q10)

**Scope:** Main EPS distribution hardware: primary/secondary buses, busbars, isolation/transfer contactors, current/voltage sensing, power backplanes and PDUs.  
**Rule:** Physical HW lives here (24-30). Protection devices in **24-50**. Solid-state switching (RPC/SSPC) in **39-40**. Algorithms/limits in **24-70**. FSW in **42**. No code stored here.

---

## 1) Assemblies (24-30 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                         | Status |
|------------------------|----------------------------------------------|-------|--------------------------------------|--------|
| 24-30-ASSY-PDU-28V     | 28 V Power Distribution Unit (PDU)           | ASSY  | `CAx/CAD/assy_pdu_28v.step`          | REL    |
| 24-30-ASSY-MAIN-BUS    | Main Busbar Assembly                         | ASSY  | `CAx/CAD/assy_main_bus.step`         | REL    |
| 24-30-ASSY-BUS-ISO     | Bus Isolation & Transfer Contactor Module    | ASSY  | `CAx/CAD/assy_bus_isolation.step`    | RVW    |
| 24-30-ASSY-SENSE       | Voltage/Current Sensing Module               | ASSY  | `CAx/CAD/assy_sense_vi.step`         | REL    |
| 24-30-ASSY-ARRAY-OR    | Solar Array Output Router/Combiner           | ASSY  | `CAx/CAD/assy_array_or.step`         | WIP    |
| 24-30-ASSY-BATT-COUP   | Battery Coupling & Precharge Interface       | ASSY  | `CAx/CAD/assy_batt_couple.step`      | RVW    |

*Variants EM/QM/FM tracked per derived P/N suffix.*

---

## 2) Key parts by assembly
| P/N                      | Description                              | Belongs to          | CAx / Docs                          | Note |
|--------------------------|------------------------------------------|---------------------|-------------------------------------|------|
| 24-30-BUSBAR-CU-xxx      | Copper busbar, plated                    | MAIN-BUS            | `CAx/CAD/busbar.step`               | Current rating |
| 24-30-CONT-ISO-HV        | High-voltage isolation contactor         | BUS-ISO             | `CAx/CAD/contactor_iso.step`        | Arc suppression |
| 24-30-SENSE-VI-HALL      | Hall-effect current sensor               | SENSE               | `CAx/CAD/sensor_hall.step`          | Accuracy ±1% |
| 24-30-CONN-PDU-OUT       | PDU output connector                     | PDU-28V             | `CAx/CAD/conn_pdu_out.step`         | 28 V bus |
| 24-30-PRECHARGE-RES      | Battery precharge resistor               | BATT-COUP           | `CAx/CAD/precharge.step`            | Inrush limit |

---

## 3) Cross-references
- **Load analysis**: `CAx/CAE/load_analysis_Q10.xlsx`
- **Bus architecture**: `CAx/CAI/bus_architecture.pdf`
- **Power budget**: `CAx/CMP/power_distribution_budget.xlsx`
- **Protection coordination**: See **24-50_PROTECTION_FUSES_BREAKERS**

---

## 4) Configuration notes
- Primary bus: 28 V nominal (24–32 V operating range)
- Secondary buses: 5 V, 12 V regulated
- Bus redundancy: Dual redundant with cross-strapping
- Distribution efficiency: > 95% end-to-end
