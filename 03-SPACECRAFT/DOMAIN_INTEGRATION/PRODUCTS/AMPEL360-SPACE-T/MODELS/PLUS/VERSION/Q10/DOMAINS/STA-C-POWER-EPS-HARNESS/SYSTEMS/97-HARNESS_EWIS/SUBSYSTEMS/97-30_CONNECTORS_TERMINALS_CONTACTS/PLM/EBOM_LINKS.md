# 97-30 · CONNECTORS_TERMINALS_CONTACTS — EBOM LINKS (Q10)

**Scope:** Electrical connectors, terminals, contacts, and mating hardware for all harness interfaces.  
**Rule:** Physical HW lives here (97-30). Harness assemblies in **97-10**, **97-20**. No code stored here.

---

## 1) Assemblies (97-30 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 97-30-ASSY-CONN-KIT    | Connector Kit (mixed types)                  | ASSY  | `CAx/CAD/assy_conn_kit.step`          | REL    |
| 97-30-ASSY-TERM-BLOCK  | Terminal Block Assembly                      | ASSY  | `CAx/CAD/assy_term_block.step`        | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 97-30-CONN-MIL-38999    | MIL-DTL-38999 connector               | CONN-KIT          | `CAx/CAD/conn_mil_38999.step`      | Various sizes   |
| 97-30-CONTACT-PIN-SOCKET| Pin/socket contact (crimp)            | CONN-MIL-38999    | `CAx/CAD/contact_pin.step`         | Size 20         |
| 97-30-TERM-RING-LUG     | Ring lug terminal                     | TERM-BLOCK        | `CAx/CAD/term_ring_lug.step`       | Crimp type      |
| 97-30-BOOT-PROTECT      | Connector protective boot             | CONN-MIL-38999    | `CAx/CAD/boot_protect.step`        | Rubber          |

---

## 3) Cross-references
- **Connector specifications**: `CAx/CMP/connector_specs.pdf`
- **Contact retention test**: `CAx/CAV/contact_retention_test.pdf`
- **Mating cycles**: `CAx/CMP/mating_cycle_life.xlsx`

---

## 4) Configuration notes
- Connector standard: MIL-DTL-38999 (space-grade)
- Contact size: 20 (signal), 12 (power)
- Mating cycles: > 500 cycles
- Contact resistance: < 5 mΩ
