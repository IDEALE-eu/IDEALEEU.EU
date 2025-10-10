# 49-10 · FUEL_CELLS — EBOM LINKS (Q10)

**Scope:** Fuel cell power generation systems: PEM fuel cells, reactant management, water management, and thermal systems.  
**Rule:** Physical HW lives here (49-10). Control algorithms in **49-60**. FSW in **42**. No code stored here.

---

## 1) Assemblies (49-10 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 49-10-ASSY-FC-STACK    | PEM Fuel Cell Stack (1 kW)                   | ASSY  | `CAx/CAD/assy_fc_stack.step`          | WIP    |
| 49-10-ASSY-H2-TANK     | Hydrogen Storage Tank                        | ASSY  | `CAx/CAD/assy_h2_tank.step`           | RVW    |
| 49-10-ASSY-O2-TANK     | Oxygen Storage Tank                          | ASSY  | `CAx/CAD/assy_o2_tank.step`           | RVW    |
| 49-10-ASSY-WATER-MGT   | Water Management System                      | ASSY  | `CAx/CAD/assy_water_mgt.step`         | WIP    |
| 49-10-ASSY-THERMAL     | Fuel Cell Thermal Management                 | ASSY  | `CAx/CAD/assy_thermal.step`           | RVW    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 49-10-CELL-PEM          | PEM fuel cell (single cell)           | FC-STACK          | `CAx/CAD/cell_pem.step`            | 0.7V @ 1A/cm²   |
| 49-10-MEMB-NAFION       | Nafion membrane                       | CELL-PEM          | `CAx/CAD/membrane.step`            | Proton conductor|
| 49-10-VALVE-H2-REG      | H2 pressure regulator valve           | H2-TANK           | `CAx/CAD/valve_h2_reg.step`        | 350 bar → 3 bar |
| 49-10-PUMP-WATER        | Water circulation pump                | WATER-MGT         | `CAx/CAD/pump_water.step`          | 100 mL/min      |

---

## 3) Cross-references
- **Electrochemistry model**: `CAx/CAE/fc_model_Q10.xlsx`
- **Hydrogen safety**: `CAx/CMP/h2_safety_analysis.pdf`
- **Performance curves**: `CAx/CMP/fc_performance_curves.pdf`

---

## 4) Configuration notes
- Type: Proton Exchange Membrane (PEM) fuel cell
- Power output: 1 kW continuous
- Efficiency: 50–60% (HHV basis)
- Operating temperature: 60–80°C
- Reactants: H2 (350 bar), O2 (or air cathode)
