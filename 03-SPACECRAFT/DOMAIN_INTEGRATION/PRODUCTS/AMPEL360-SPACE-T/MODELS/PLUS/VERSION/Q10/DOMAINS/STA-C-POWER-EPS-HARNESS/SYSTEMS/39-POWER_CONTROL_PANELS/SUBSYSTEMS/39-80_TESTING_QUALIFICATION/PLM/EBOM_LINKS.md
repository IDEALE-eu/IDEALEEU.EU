# 39-80 · TESTING & QUALIFICATION — ENGINEERING BOM LINKS (Q10)

**Scope:** Ground support equipment (GSE), fixtures, and instrumentation for testing power control panels.  
**Ownership Principle:** 39-80 does not own flight hardware. All items are test-specific assets.

---

## 1. Test Articles (Referenced, Not Owned by 39-80)

| TA P/N        | Description                         | Host EBOM (SSOT)                                                                                      | Type | Status  |
|---------------|-------------------------------------|--------------------------------------------------------------------------------------------------------|------|---------|
| TA-39-10-EM01 | PCU EM                              | [`../39-10_POWER_CONTROL_UNITS_PCU/PLM/EBOM_LINKS.md`](../39-10_POWER_CONTROL_UNITS_PCU/PLM/EBOM_LINKS.md)     | EM   | IN_TEST |
| TA-39-40-QM01 | RPC 8-Channel QM                    | [`../39-40_REMOTE_POWER_CONTROLLERS_RPC/PLM/EBOM_LINKS.md`](../39-40_REMOTE_POWER_CONTROLLERS_RPC/PLM/EBOM_LINKS.md) | QM   | RVW     |

---

## 2. EGSE - Electrical Ground Support Equipment (Owned by 39-80)

| Part Number              | Description                                  | Qty | PLM_UID        | CAx Ref(s)                        | Status |
|--------------------------|----------------------------------------------|-----|----------------|-----------------------------------|--------|
| EGSE-RPC-LOAD-001        | RPC Load Simulator (8-channel)               | 2   | PLM-39-80-001  | `CAx/CAD/egse_rpc_load.step`      | REL    |
| EGSE-CMD-SIM-001         | Command Simulator (CAN/SpW)                  | 1   | PLM-39-80-002  | `CAx/CAD/egse_cmd_sim.step`       | REL    |

---

## 3. Test Procedures (CMP Artifacts)

| Test ID         | Title                                     | DUT(s)          | Procedure                            | Status   |
|-----------------|-------------------------------------------|-----------------|--------------------------------------|----------|
| TP-39-80-001    | RPC Switching Performance                 | TA-39-40-QM01   | `CAx/CMP/tp_rpc_switch_v1.0.pdf`     | COMPLETE |
| TP-39-80-002    | PCU Sequencing Verification               | TA-39-10-EM01   | `CAx/CMP/tp_pcu_seq_v1.0.pdf`        | IN_WORK  |

---

## 4. Notes

1. **COTS Equipment**: COTS instruments maintained per manufacturer recommendations.
2. **Test Article Ownership**: DUTs remain under control of host subsystem EBOMs.
