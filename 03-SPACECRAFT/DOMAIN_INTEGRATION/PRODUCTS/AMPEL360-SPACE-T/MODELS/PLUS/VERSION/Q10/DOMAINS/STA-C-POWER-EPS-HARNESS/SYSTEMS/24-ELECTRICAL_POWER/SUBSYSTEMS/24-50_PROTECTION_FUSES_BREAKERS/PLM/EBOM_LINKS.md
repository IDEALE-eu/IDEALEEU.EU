# 24-50 · PROTECTION_FUSES_BREAKERS — EBOM LINKS (Q10)

**Ámbito:** Fusibles, magnetotérmicos, limitadores e interfaces de protección del EPS.  
**Regla:** HW físico vive aquí (24-50). Lógica/curvas/umbrales parametrizados en **24-70**. FSW en **42**. Sin código en 24-50.

---

## 1) Conjuntos (SSOT EBOM 24-50)
| P/N                     | Descripción                                      | Nivel | CAx (diseño)                          | Estado |
|-------------------------|--------------------------------------------------|-------|---------------------------------------|--------|
| 24-50-ASSY-FUSEPANEL-28 | Panel de fusibles 28 V (distribución secundaria) | ASSY  | `CAx/CAD/assy_fusepanel_28.step`      | REL    |
| 24-50-ASSY-CB-PANEL     | Panel de magnetotérmicos/termales                | ASSY  | `CAx/CAD/assy_cb_panel.step`          | RVW    |
| 24-50-ASSY-SPD-TVS      | Módulo protección transitorios (TVS/DC)          | ASSY  | `CAx/CAD/assy_spd_tvs.step`           | REL    |
| 24-50-ASSY-INRUSH-LIM   | Módulo limitación de inrush                      | ASSY  | `CAx/CAD/assy_inrush.step`            | WIP    |
| 24-50-ASSY-GFDI         | Interface detección fallo a masa (GFDI)          | ASSY  | `CAx/CAD/assy_gfdi.step`              | RVW    |

---

## 2) Partes clave por conjunto
| P/N                    | Descripción                          | Pertenece a                 | CAx / Docs                         | Nota |
|------------------------|--------------------------------------|-----------------------------|------------------------------------|------|
| 24-50-FUSE-FAST-xxA    | Fusible rápido xx A                  | FUSEPANEL-28                | `CAx/CAD/fuse_fast.step`           | Curva I–t en CMP   |
| 24-50-FUSE-TD-xxA      | Fusible retardado xx A               | FUSEPANEL-28                | `CAx/CAD/fuse_td.step`             | Coordinación selectiva |
| 24-50-CB-THERM-xxA     | Breaker térmico xx A                 | CB-PANEL                    | `CAx/CAD/breaker_therm.step`       | Rearme manual      |
| 24-50-TVS-BIDIR-xxx    | TVS bidireccional xxx V              | SPD-TVS                     | `CAx/CAD/tvs_bidir.step`           | Clamp < 50 V       |
| 24-50-NTC-INRUSH       | NTC limitador de inrush              | INRUSH-LIM                  | `CAx/CAD/ntc_inrush.step`          | R(25°C) = 10 Ω     |
| 24-50-SENSOR-LEAK      | Sensor fuga a masa                   | GFDI                        | `CAx/CAD/sensor_leak.step`         | Sensibilidad < 1 mA|

---

## 3) Referencias cruzadas
- **Coordinación de protecciones**: `CAx/CAE/coordination_study_Q10.xlsx`
- **Curvas I–t**: `CAx/CMP/fuse_curves.pdf`
- **Matriz de fallos**: `CAx/CAI/fault_matrix.xlsx`
- **Umbrales SW**: Ver **24-70_ALGORITHMS_CONTROL**

---

## 4) Notas de configuración
- Selectividad: fusibles rápidos aguas abajo, retardados aguas arriba
- Protección de sobretensión: TVS en todas las entradas críticas
- GFDI: detección < 1 mA, aislamiento > 1 MΩ
- Coordinación con FDIR: trip flags a 31-Data Handling
