# 24-10 · POWER_GENERATION — EBOM LINKS (Q10)

**Scope:** Photovoltaic power generation hardware: solar wings/panels, PV strings, bypass/blocking devices, array harness, slip-ring feedthroughs, and thermal hardware attached to panels.  
**Rule:** Physical HW lives here (24-10). Regulation/MPPT lives in **24-60**. Protection in **24-50**. Algorithms/limits in **24-70**. FSW in **42**. No code stored here.

---

## 1) Assemblies (24-10 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 24-10-ASSY-SOL-WING-L  | Left solar array wing assembly               | ASSY  | `CAx/CAD/assy_sol_wing_L.step`        | RVW    |
| 24-10-ASSY-SOL-WING-R  | Right solar array wing assembly              | ASSY  | `CAx/CAD/assy_sol_wing_R.step`        | RVW    |
| 24-10-ASSY-PANEL       | Panel laminate (cell substrate + interconnect)| ASSY | `CAx/CAD/assy_panel.step`             | REL    |
| 24-10-ASSY-STRING      | PV string subassembly (cells + diodes)       | ASSY  | `CAx/CAD/assy_pv_string.step`         | REL    |
| 24-10-ASSY-ARRAY-HAR   | Solar array harness & feedthrough            | ASSY  | `CAx/CAD/assy_array_harness.step`     | REL    |
| 24-10-ASSY-SLIPRING    | Slip-ring/rotary feed (if rotating drive)    | ASSY  | `CAx/CAD/assy_slipring.step`          | WIP    |
| 24-10-ASSY-THERM-KIT   | Thermal kit (radiators/heat spreaders/TIM)   | ASSY  | `CAx/CAD/assy_therm_kit.step`         | RVW    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 24-10-CELL-TRIPLE-xxx   | Triple-junction GaAs solar cell       | ASSY-STRING       | `CAx/CAD/cell.step`                | Efficiency spec in CMP |
| 24-10-DIODE-BYPASS      | Bypass diode (Schottky)               | ASSY-STRING       | `CAx/CAD/diode_bypass.step`        | Reverse breakdown |
| 24-10-SUBS-CFRP         | CFRP substrate panel                  | ASSY-PANEL        | `CAx/CAD/substrate.step`           | Thermal expansion |
| 24-10-CONN-ARRAY-PWR    | Array power connector (high voltage)  | ASSY-ARRAY-HAR    | `CAx/CAD/conn_array.step`          | 120 V rated |
| 24-10-HINGE-DEPLOY      | Deployment hinge mechanism            | ASSY-SOL-WING-*   | `CAx/CAD/hinge.step`               | Spring release |
| 24-10-RADIATOR-OSR      | Optical solar reflector coating      | ASSY-THERM-KIT    | `CAx/CAE/radiator_osr.pdf`         | Emissivity data |

---

## 3) Cross-references
- **Thermal analysis**: `CAx/CAE/thermal_solar_array_Q10.xlsx`
- **Deployment kinematics**: `CAx/CAI/deployment_sequence.pdf`
- **Power output budget**: `CAx/CMP/power_budget_Q10.xlsx`
- **MPPT control interface**: See **24-60_CONVERTERS_DCDC_ACDC** and **24-70_ALGORITHMS_CONTROL**

---

## 4) Configuration notes
- Solar cell efficiency: 30% BOL, 24% EOL (5-year degradation)
- Array voltage: 80–120 V nominal (temp compensated)
- Total wing area: 12 m² deployed
- Deployment time: < 60 s per wing
