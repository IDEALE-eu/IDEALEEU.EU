# 97-40 · EMI_EMC_SHIELDING_BONDING — EBOM LINKS (Q10)

**Scope:** EMI/EMC protection: cable shielding, bonding straps, EMI gaskets, and grounding hardware.  
**Rule:** Physical HW lives here (97-40). EMI testing in **97-80**. No code stored here.

---

## 1) Assemblies (97-40 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 97-40-ASSY-SHIELD-KIT  | Cable Shielding Kit                          | ASSY  | `CAx/CAD/assy_shield_kit.step`        | REL    |
| 97-40-ASSY-BOND-STRAP  | Bonding Strap Assembly                       | ASSY  | `CAx/CAD/assy_bond_strap.step`        | REL    |
| 97-40-ASSY-EMI-FILT    | EMI Filter Assembly                          | ASSY  | `CAx/CAD/assy_emi_filt.step`          | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 97-40-BRAID-SHIELD-CU   | Copper braided shield                 | SHIELD-KIT        | `CAx/CAD/braid_shield_cu.step`     | 95% coverage    |
| 97-40-STRAP-BOND-CU     | Copper bonding strap                  | BOND-STRAP        | `CAx/CAD/strap_bond_cu.step`       | Low impedance   |
| 97-40-GASKET-EMI-CU     | Conductive EMI gasket                 | SHIELD-KIT        | `CAx/CAD/gasket_emi_cu.step`       | Shielding >60dB |
| 97-40-FILT-FEEDTHRU     | EMI feedthrough filter                | EMI-FILT          | `CAx/CAD/filt_feedthru.step`       | Pi-filter       |

---

## 3) Cross-references
- **EMC requirements**: `CAx/CMP/emc_requirements_Q10.pdf`
- **Shielding effectiveness**: `CAx/CAV/shielding_effectiveness_test.pdf`
- **Bonding impedance**: `CAx/CAV/bonding_impedance_test.xlsx`

---

## 4) Configuration notes
- Shielding effectiveness: > 60 dB (30 MHz – 1 GHz)
- Bonding impedance: < 2.5 mΩ (DC to 10 MHz)
- Grounding: Single-point ground reference
- EMI filters: Installed at panel entries
