# 24-40 · ENERGY_STORAGE — EBOM LINKS (Q10)

**Scope:** Battery systems, cells, packs, BMS hardware, charge/discharge control electronics, and thermal management for energy storage.  
**Rule:** Physical HW lives here (24-40). Charge algorithms in **24-70**. Protection in **24-50**. FSW in **42**. No code stored here.

---

## 1) Assemblies (24-40 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 24-40-ASSY-BATT-PACK   | Battery Pack Assembly (Li-ion)               | ASSY  | `CAx/CAD/assy_batt_pack.step`         | REL    |
| 24-40-ASSY-BMS-MAIN    | Battery Management System (BMS) Main Board   | ASSY  | `CAx/CAD/assy_bms_main.step`          | REL    |
| 24-40-ASSY-CELL-MOD    | Cell Module (8S configuration)               | ASSY  | `CAx/CAD/assy_cell_mod_8s.step`       | REL    |
| 24-40-ASSY-BAL-BOARD   | Cell Balancing Board                         | ASSY  | `CAx/CAD/assy_bal_board.step`         | REL    |
| 24-40-ASSY-THERMAL-MGT | Battery Thermal Management Assembly          | ASSY  | `CAx/CAD/assy_thermal_mgt.step`       | RVW    |
| 24-40-ASSY-DISCONNECT  | Battery Disconnect/Isolation Switch          | ASSY  | `CAx/CAD/assy_disconnect.step`        | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 24-40-CELL-LIION-18650  | Li-ion cell 18650 3.6V 3.5Ah          | CELL-MOD          | `CAx/CAD/cell_18650.step`          | Cycle life > 1000 |
| 24-40-IC-BMS-AFE        | BMS Analog Front End IC               | BMS-MAIN          | `CAx/CAD/ic_bms_afe.step`          | 14-bit ADC      |
| 24-40-SENS-CURR-HALL    | Hall effect current sensor 50A        | BMS-MAIN          | `CAx/CAD/sens_curr_hall.step`      | Accuracy ±0.5%  |
| 24-40-MOSFET-N-BAL      | N-channel balancing MOSFET            | BAL-BOARD         | `CAx/CAD/mosfet_n_bal.step`        | Balancing 200mA |
| 24-40-CONT-PYRO         | Pyrotechnic disconnect contactor      | DISCONNECT        | `CAx/CAD/cont_pyro.step`           | One-shot device |
| 24-40-THERM-PAD-TIM     | Thermal interface material pad        | THERMAL-MGT       | `CAx/CAD/therm_pad.step`           | Conductivity 5W/mK |

---

## 3) Cross-references
- **Thermal analysis**: `CAx/CAE/thermal_battery_Q10.xlsx`
- **Charge/discharge curves**: `CAx/CMP/battery_curves.pdf`
- **State of Health (SOH) tracking**: `CAx/CMP/soh_tracking.xlsx`
- **BMS algorithms**: See **24-70_ALGORITHMS_CONTROL**

---

## 4) Configuration notes
- Battery chemistry: Li-ion 18650 cells
- Nominal voltage: 28.8 V (8S configuration)
- Capacity: 28 Ah (3.5 Ah per cell × 8)
- Charge rate: C/2 max (14 A)
- Discharge rate: 2C max (56 A)
- Operating temperature: -20°C to +60°C
- Cell balancing: Passive, 200 mA per cell
- BMS: Integrated SOC, SOH, thermal monitoring
