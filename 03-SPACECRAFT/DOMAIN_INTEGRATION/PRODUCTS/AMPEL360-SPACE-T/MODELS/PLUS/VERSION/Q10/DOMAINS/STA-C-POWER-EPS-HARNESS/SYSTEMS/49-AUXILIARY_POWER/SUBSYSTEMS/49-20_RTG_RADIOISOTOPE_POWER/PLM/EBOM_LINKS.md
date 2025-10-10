# 49-20 · RTG_RADIOISOTOPE_POWER — EBOM LINKS (Q10)

**Scope:** Radioisotope Thermoelectric Generator (RTG) systems for long-duration missions.  
**Rule:** Physical HW lives here (49-20). Nuclear safety in dedicated subsystem. No code stored here.

---

## 1) Assemblies (49-20 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 49-20-ASSY-RTG-UNIT    | RTG Assembly (Pu-238)                        | ASSY  | `CAx/CAD/assy_rtg_unit.step`          | REL    |
| 49-20-ASSY-THERMO-MOD  | Thermoelectric Module                        | ASSY  | `CAx/CAD/assy_thermo_mod.step`        | REL    |
| 49-20-ASSY-HEAT-SRC    | Heat Source (GPHS module)                    | ASSY  | `CAx/CAD/assy_heat_src.step`          | REL    |
| 49-20-ASSY-RAD-FIN     | Radiator Fin Assembly                        | ASSY  | `CAx/CAD/assy_rad_fin.step`           | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes. Pu-238 source requires special licensing.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 49-20-GPHS-MODULE       | General Purpose Heat Source module    | HEAT-SRC          | `CAx/CAD/gphs_module.step`         | 250 W thermal   |
| 49-20-TE-COUPLE-SIPTE   | SiGe thermoelectric couple            | THERMO-MOD        | `CAx/CAD/te_couple.step`           | Seebeck effect  |
| 49-20-FIN-AL-RADIATOR   | Aluminum radiator fin                 | RAD-FIN           | `CAx/CAD/fin_al.step`              | Thermal rejection|

---

## 3) Cross-references
- **Nuclear safety analysis**: `CAx/CMP/nuclear_safety_Q10.pdf`
- **Thermal model**: `CAx/CAE/thermal_rtg_Q10.xlsx`
- **Decay power curve**: `CAx/CMP/decay_power_pu238.pdf`

---

## 4) Configuration notes
- Isotope: Plutonium-238 (Pu-238)
- Thermal power: 4 × 250 W = 1000 W (BOL)
- Electrical output: 110 W (BOL), 100 W (EOL, 14 years)
- Efficiency: ~11% (thermoelectric)
- Half-life: 87.7 years (minimal decay over mission)
- Operating temperature: Hot junction 850°C, cold junction 250°C
