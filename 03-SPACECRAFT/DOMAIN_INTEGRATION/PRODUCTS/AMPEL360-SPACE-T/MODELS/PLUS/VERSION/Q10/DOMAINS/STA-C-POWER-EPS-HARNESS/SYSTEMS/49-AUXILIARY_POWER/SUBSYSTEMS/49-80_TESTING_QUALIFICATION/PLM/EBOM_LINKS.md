# 49-80 · TESTING & QUALIFICATION — ENGINEERING BOM LINKS (Q10)

**Scope:** Ground support equipment for testing auxiliary power systems.  
**Ownership Principle:** 49-80 does not own flight hardware. All items are test-specific assets.

---

## 1. Test Articles (Referenced, Not Owned by 49-80)

| TA P/N        | Description                         | Host EBOM (SSOT)                                                                                      | Type | Status  |
|---------------|-------------------------------------|--------------------------------------------------------------------------------------------------------|------|---------|
| TA-49-10-EM01 | Fuel Cell Stack EM                  | [`../49-10_FUEL_CELLS/PLM/EBOM_LINKS.md`](../49-10_FUEL_CELLS/PLM/EBOM_LINKS.md)                       | EM   | IN_TEST |

---

## 2. EGSE - Electrical Ground Support Equipment (Owned by 49-80)

| Part Number              | Description                                  | Qty | PLM_UID        | CAx Ref(s)                        | Status |
|--------------------------|----------------------------------------------|-----|----------------|-----------------------------------|--------|
| EGSE-H2-SIM-001          | Hydrogen Supply Simulator                    | 1   | PLM-49-80-001  | `CAx/CAD/egse_h2_sim.step`        | WIP    |
| EGSE-LOAD-FC-001         | Fuel Cell Electronic Load                    | 1   | PLM-49-80-002  | `CAx/CAD/egse_load_fc.step`       | WIP    |

---

## 3. Notes

1. **Safety**: Hydrogen testing requires special safety protocols and ventilation.
2. **Nuclear**: RTG testing subject to nuclear regulatory requirements.
