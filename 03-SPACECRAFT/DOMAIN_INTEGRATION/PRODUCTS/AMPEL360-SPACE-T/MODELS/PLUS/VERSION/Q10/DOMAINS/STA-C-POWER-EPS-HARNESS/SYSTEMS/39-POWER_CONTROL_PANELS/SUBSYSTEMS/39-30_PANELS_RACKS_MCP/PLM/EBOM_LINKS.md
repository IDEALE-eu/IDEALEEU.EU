# 39-30 · PANELS_RACKS_MCP — EBOM LINKS (Q10)

**Scope:** Physical panels, racks, enclosures, and master control panels housing power control equipment.  
**Rule:** Physical HW lives here (39-30). Electronics in **39-10**, **39-20**, **39-40**. No code stored here.

---

## 1) Assemblies (39-30 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 39-30-ASSY-RACK-19IN   | 19-inch Equipment Rack                       | ASSY  | `CAx/CAD/assy_rack_19in.step`         | REL    |
| 39-30-ASSY-MCP         | Master Control Panel                         | ASSY  | `CAx/CAD/assy_mcp.step`               | REL    |
| 39-30-ASSY-ENCL-EXE    | Electronics Enclosure (explosion-proof)      | ASSY  | `CAx/CAD/assy_encl_exe.step`          | RVW    |
| 39-30-ASSY-BACKPLANE   | Backplane Assembly                           | ASSY  | `CAx/CAD/assy_backplane.step`         | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 39-30-PANEL-AL-6061     | Aluminum panel 6061-T6                | MCP               | `CAx/CAD/panel_al.step`            | Anodized finish |
| 39-30-RAIL-MOUNT        | DIN rail mounting system              | RACK-19IN         | `CAx/CAD/rail_mount.step`          | 35mm DIN rail   |
| 39-30-GASKET-EMI        | EMI gasket (conductive)               | ENCL-EXE          | `CAx/CAD/gasket_emi.step`          | Shielding >60dB |
| 39-30-CONN-BP-96P       | Backplane connector 96-pin            | BACKPLANE         | `CAx/CAD/conn_bp_96p.step`         | High-density    |

---

## 3) Cross-references
- **Structural analysis**: `CAx/CAE/structural_rack_Q10.pdf`
- **Thermal management**: `CAx/CAE/thermal_enclosure_Q10.xlsx`
- **EMI shielding**: `CAx/CAV/emi_test_report.pdf`

---

## 4) Configuration notes
- Rack standard: 19-inch EIA-310-D
- Material: Aluminum 6061-T6 (lightweight, corrosion resistant)
- EMI shielding: > 60 dB attenuation (30 MHz – 1 GHz)
- Thermal: Convection cooling with optional fans
