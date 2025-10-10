# 97-50 · CLAMPS_BRACKETS_STRESS_RELIEF — EBOM LINKS (Q10)

**Scope:** Cable support hardware: clamps, brackets, strain relief, and routing guides.  
**Rule:** Physical HW lives here (97-50). Routing design in **97-70**. No code stored here.

---

## 1) Assemblies (97-50 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 97-50-ASSY-CLAMP-KIT   | Cable Clamp Kit (mixed sizes)                | ASSY  | `CAx/CAD/assy_clamp_kit.step`         | REL    |
| 97-50-ASSY-BRACKET-MTG | Mounting Bracket Assembly                    | ASSY  | `CAx/CAD/assy_bracket_mtg.step`       | REL    |
| 97-50-ASSY-STRAIN-RELF | Strain Relief Assembly                       | ASSY  | `CAx/CAD/assy_strain_relf.step`       | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 97-50-CLAMP-CABLE-25MM  | Cable clamp 25mm diameter             | CLAMP-KIT         | `CAx/CAD/clamp_cable_25mm.step`    | Cushioned       |
| 97-50-BRACKET-AL-MTG    | Aluminum mounting bracket             | BRACKET-MTG       | `CAx/CAD/bracket_al_mtg.step`      | Anodized        |
| 97-50-GROMMET-RUBBER    | Rubber grommet (strain relief)        | STRAIN-RELF       | `CAx/CAD/grommet_rubber.step`      | Panel entry     |
| 97-50-TIE-MOUNT         | Cable tie mount (adhesive)            | CLAMP-KIT         | `CAx/CAD/tie_mount.step`           | Reusable        |

---

## 3) Cross-references
- **Clamp spacing**: `CAx/CMP/clamp_spacing_criteria.pdf`
- **Vibration analysis**: `CAx/CAE/vibration_harness_Q10.xlsx`
- **Installation procedure**: See **97-70_SCHEMATICS_ROUTING_INSTALLATION**

---

## 4) Configuration notes
- Clamp spacing: < 150 mm for unsupported runs
- Material: Aluminum or plastic (non-metallic for EMI isolation)
- Strain relief: Provided at all connectors and panel entries
- Vibration: Designed to survive 14.1 Grms (random)
