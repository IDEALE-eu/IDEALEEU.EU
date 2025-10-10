# 97-10 · MAIN_HARNESS_BACKBONE — EBOM LINKS (Q10)

**Scope:** Primary electrical harness backbone: main cable trunks, backbone routing, and primary interconnects.  
**Rule:** Physical HW lives here (97-10). Schematics in **97-70**. Testing in **97-80**. No code stored here.

---

## 1) Assemblies (97-10 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 97-10-ASSY-TRUNK-MAIN  | Main Trunk Harness Assembly                  | ASSY  | `CAx/CAD/assy_trunk_main.step`        | REL    |
| 97-10-ASSY-BACKBONE-FWD| Forward Backbone Section                     | ASSY  | `CAx/CAD/assy_backbone_fwd.step`      | REL    |
| 97-10-ASSY-BACKBONE-AFT| Aft Backbone Section                         | ASSY  | `CAx/CAD/assy_backbone_aft.step`      | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 97-10-CABLE-PWR-10AWG   | 10 AWG power cable (stranded)         | TRUNK-MAIN        | `CAx/CAD/cable_pwr_10awg.step`     | 30 A rating     |
| 97-10-CABLE-SIG-22AWG   | 22 AWG signal cable (twisted pair)    | TRUNK-MAIN        | `CAx/CAD/cable_sig_22awg.step`     | Shielded        |
| 97-10-CONN-MAIN-50P     | 50-pin main connector                 | TRUNK-MAIN        | `CAx/CAD/conn_main_50p.step`       | Mil-DTL-38999   |
| 97-10-SLEEVE-PROTECT    | Protective sleeve (braided)           | BACKBONE-*        | `CAx/CAD/sleeve_protect.step`      | Abrasion resist |

---

## 3) Cross-references
- **Routing diagram**: `CAx/CAI/routing_diagram_Q10.pdf`
- **Wire sizing**: `CAx/CMP/wire_sizing_calc.xlsx`
- **Schematics**: See **97-70_SCHEMATICS_ROUTING_INSTALLATION**

---

## 4) Configuration notes
- Total harness length: ~50 m (main trunk + branches)
- Power cables: 10–16 AWG depending on current
- Signal cables: 22–26 AWG twisted pair, shielded
- Connector standard: MIL-DTL-38999 (high reliability)
