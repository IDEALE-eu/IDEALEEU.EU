# 97-20 · BRANCH_LOOMS_SUBHARNESSES — EBOM LINKS (Q10)

**Scope:** Branch harnesses and sub-looms: secondary distribution from main trunk to individual subsystems.  
**Rule:** Physical HW lives here (97-20). Main trunk in **97-10**. Schematics in **97-70**. No code stored here.

---

## 1) Assemblies (97-20 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 97-20-ASSY-LOOM-EPS    | EPS Branch Loom                              | ASSY  | `CAx/CAD/assy_loom_eps.step`          | REL    |
| 97-20-ASSY-LOOM-CDH    | C&DH Branch Loom                             | ASSY  | `CAx/CAD/assy_loom_cdh.step`          | REL    |
| 97-20-ASSY-LOOM-PAYLOAD| Payload Branch Loom                          | ASSY  | `CAx/CAD/assy_loom_payload.step`      | RVW    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 97-20-CABLE-BRANCH-14AWG| 14 AWG branch cable                   | LOOM-EPS          | `CAx/CAD/cable_branch_14awg.step`  | 15 A rating     |
| 97-20-CONN-BRANCH-20P   | 20-pin branch connector               | LOOM-*            | `CAx/CAD/conn_branch_20p.step`     | Circular        |
| 97-20-TIE-CABLE         | Cable tie (releasable)                | LOOM-*            | `CAx/CAD/tie_cable.step`           | Reusable        |

---

## 3) Cross-references
- **Branch routing**: `CAx/CAI/branch_routing_Q10.pdf`
- **Load allocation**: `CAx/CMP/branch_load_allocation.xlsx`

---

## 4) Configuration notes
- Branch lengths: 1–10 m typical
- Connectors: MIL-DTL-38999 series (compatible with main trunk)
- Segregation: Power and signal separated by > 50 mm
