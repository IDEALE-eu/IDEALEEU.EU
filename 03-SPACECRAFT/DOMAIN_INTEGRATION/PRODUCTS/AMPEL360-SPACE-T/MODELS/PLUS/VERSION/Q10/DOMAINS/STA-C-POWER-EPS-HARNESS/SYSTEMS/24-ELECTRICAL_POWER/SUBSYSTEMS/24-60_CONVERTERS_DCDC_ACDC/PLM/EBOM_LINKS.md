# 24-60 · CONVERTERS_DCDC_ACDC — EBOM LINKS (Q10)

**Ámbito:** Convertidores ACDC/DCDC del EPS.  
**Regla:** El HW de convertidor vive en 24-60. SW/firmware: evidencia en 40/42; parámetros en 24-70. Sin código aquí.

---

## 1) Conjuntos de referencia (SSOT de EBOM 24-60)
| P/N                | Descripción                                | Nivel | CAx (diseño)                         | Estado |
|--------------------|--------------------------------------------|-------|--------------------------------------|--------|
| 24-60-ASSY-DC28-1k | DCDC 270V→28V 1 kW, aislado                | ASSY  | `CAx/CAD/assy_dc28_1k.step`          | REL    |
| 24-60-ASSY-DCBAT-2k| DCDC 28V↔Bat 2 kW (bi-dir)                 | ASSY  | `CAx/CAD/assy_bidir_2k.step`         | RVW    |
| 24-60-ASSY-ACDC-3k | ACDC 115 VAC→28 V 3 kW PFC                 | ASSY  | `CAx/CAD/assy_acdc_3k.step`          | WIP    |

**Variantes:** EM/QM/FM por P/N derivado (sufijos `-EM`, `-QM`, `-FM`).

---

## 2) Despiece principal por conjunto
| P/N                     | Descripción                              | Pertenece a             | CAx / docs                          | Nota |
|-------------------------|------------------------------------------|-------------------------|-------------------------------------|------|
| 24-60-PCB-CTRL-MCU      | Placa control MCU/FPGA                   | ASSY*                   | `CAx/CAD/pcb_ctrl.brd`              | FW evid. en 42/40 |
| 24-60-PCB-POWER-HS      | Etapa potencia half-bridge               | ASSY*                   | `CAx/CAD/pcb_power.brd`             | Derating CMP     |
| 24-60-MAG-TRF-700k      | Trafo alta freq                          | ASSY*                   | `CAx/CAD/trf_700k.step`             | Hipótesis CAE    |
| 24-60-MAG-IND-OUT       | Inductor salida                          | ASSY*                   | `CAx/CAD/ind_out.step`              | Saturación CAE   |
| 24-60-FILT-EMI-LC       | Filtro EMI entrada LC                    | ASSY*                   | `CAx/CAD/filt_emi.step`             | EMC compliance   |
| 24-60-MOSFET-SIC-xxx    | MOSFET SiC xxx mΩ                        | PCB-POWER-HS            | `CAx/CAD/mosfet_sic.step`           | Tj max 150°C     |
| 24-60-CAP-BULK-xxx      | Capacitor bulk xxx µF                    | ASSY*                   | `CAx/CAD/cap_bulk.step`             | ESR, ripple      |

---

## 3) Referencias cruzadas
- **Análisis térmico**: `CAx/CAE/thermal_converter_Q10.xlsx`
- **Topología**: `CAx/CAI/topology_diagram.pdf`
- **Presupuesto de eficiencia**: `CAx/CMP/efficiency_budget.xlsx`
- **Control MPPT**: Ver **24-70_ALGORITHMS_CONTROL**

---

## 4) Notas de configuración
- Eficiencia: > 92% a carga nominal
- Rizado de salida: < 2% Vout
- Frecuencia de conmutación: 100–700 kHz (depende de topología)
- Aislamiento galvánico: > 1 kV DC (DCDC aislados)
