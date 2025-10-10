# 97-80 · TESTING_CONTINUITY_HIPOT — EBOM LINKS (Q10)

**Scope:** Ground support equipment for harness testing: continuity testers, hipot testers, insulation resistance testers.  
**Ownership Principle:** 97-80 does not own flight hardware. All items are test-specific assets.

---

## 1. Test Articles (Referenced, Not Owned by 97-80)

| TA P/N        | Description                         | Host EBOM (SSOT)                                                                                      | Type | Status  |
|---------------|-------------------------------------|--------------------------------------------------------------------------------------------------------|------|---------|
| TA-97-10-EM01 | Main Trunk Harness EM               | [`../97-10_MAIN_HARNESS_BACKBONE/PLM/EBOM_LINKS.md`](../97-10_MAIN_HARNESS_BACKBONE/PLM/EBOM_LINKS.md) | EM   | IN_TEST |

---

## 2. EGSE - Electrical Ground Support Equipment (Owned by 97-80)

| Part Number              | Description                                  | Qty | PLM_UID        | CAx Ref(s)                        | Status |
|--------------------------|----------------------------------------------|-----|----------------|-----------------------------------|--------|
| EGSE-CONT-TEST-001       | Continuity Tester (automated)                | 1   | PLM-97-80-001  | `CAx/CAD/egse_cont_test.step`     | REL    |
| EGSE-HIPOT-5KV-001       | Hipot Tester 5 kV                            | 1   | PLM-97-80-002  | `CAx/CAD/egse_hipot_5kv.step`     | REL    |
| EGSE-INSUL-1GIG-001      | Insulation Resistance Tester (1 GΩ range)   | 1   | PLM-97-80-003  | `CAx/CAD/egse_insul_test.step`    | REL    |

---

## 3. Test Procedures (CMP Artifacts)

| Test ID         | Title                                     | DUT(s)          | Procedure                            | Status   |
|-----------------|-------------------------------------------|-----------------|--------------------------------------|----------|
| TP-97-80-001    | Harness Continuity Test                   | TA-97-10-EM01   | `CAx/CMP/tp_continuity_v1.0.pdf`     | COMPLETE |
| TP-97-80-002    | Harness Hipot Test (1 kV)                 | TA-97-10-EM01   | `CAx/CMP/tp_hipot_v1.0.pdf`          | COMPLETE |
| TP-97-80-003    | Insulation Resistance Test                | TA-97-10-EM01   | `CAx/CMP/tp_insul_res_v1.0.pdf`      | COMPLETE |

---

## 4. Notes

1. **Continuity**: < 1 Ω end-to-end for power wires, < 5 Ω for signal wires
2. **Hipot**: 1 kV DC for 1 minute (no breakdown)
3. **Insulation**: > 100 MΩ @ 500 V DC
4. **Safety**: High voltage testing requires certified operators
