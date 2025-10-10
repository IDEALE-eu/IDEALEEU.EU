# 97-60 · LABELING_MARKING_CONFIGURATION — EBOM LINKS (Q10)

**Scope:** Wire identification, cable labels, configuration management, and traceability marking.  
**Rule:** Physical HW lives here (97-60). Schematics in **97-70**. Configuration data in CMP. No code stored here.

---

## 1) Assemblies (97-60 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 97-60-ASSY-LABEL-KIT   | Wire Label Kit (adhesive)                    | ASSY  | `CAx/CAD/assy_label_kit.step`         | REL    |
| 97-60-ASSY-MARKER-WRAP | Marker Wrap Kit (heat-shrink)                | ASSY  | `CAx/CAD/assy_marker_wrap.step`       | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 97-60-LABEL-WIRE-ADHES  | Adhesive wire label                   | LABEL-KIT         | `CAx/CAD/label_wire_adhes.step`    | Printable       |
| 97-60-MARKER-HEAT-SHRINK| Heat-shrink wire marker               | MARKER-WRAP       | `CAx/CAD/marker_heat_shrink.step`  | Pre-printed     |
| 97-60-TAG-ID-METAL      | Metal identification tag              | LABEL-KIT         | `CAx/CAD/tag_id_metal.step`        | Permanent       |

---

## 3) Cross-references
- **Labeling standard**: `CAx/CMP/labeling_standard_Q10.pdf`
- **Wire ID list**: `CAx/CMP/wire_id_list_Q10.xlsx`
- **Configuration database**: `CAx/CMP/harness_config_db.xlsx`

---

## 4) Configuration notes
- Label format: [System]-[Wire#]-[Function] (e.g., 24-PWR-001-28V)
- Label material: Polyester (temperature resistant, -55°C to +150°C)
- Placement: At both ends of wire and every 1 m along run
- Traceability: Serial number on each harness assembly
