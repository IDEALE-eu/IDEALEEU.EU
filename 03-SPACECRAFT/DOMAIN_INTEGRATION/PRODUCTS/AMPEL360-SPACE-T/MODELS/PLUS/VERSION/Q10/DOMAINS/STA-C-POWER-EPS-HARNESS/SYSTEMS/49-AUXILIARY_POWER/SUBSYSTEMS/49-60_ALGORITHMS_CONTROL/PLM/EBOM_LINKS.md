# 49-60 ALGORITHMS & CONTROL — LOGICAL COMPONENT REGISTRY  
*(Not an EBOM — No Physical Parts Owned)*

> **📌 Ownership Principle**:  
> All hardware and flight software reside with their **host LRUs**.  
> **49-60 owns only**:  
> - Algorithm specifications  
> - Configuration data  
> - Verification evidence (CMP artifacts)

---

## 1. Hosted Hardware Components (Owned by Other Subsystems)

| Part Number  | Description                        | Host LRU                   | EBOM Path                                                                                      | Status        |
|--------------|------------------------------------|----------------------------|------------------------------------------------------------------------------------------------|---------------|
| MCU-FC-001   | Fuel Cell Control MCU              | 49-10_FUEL_CELLS           | [`../49-10_FUEL_CELLS/PLM/EBOM_LINKS.md`](../49-10_FUEL_CELLS/PLM/EBOM_LINKS.md)               | WIP           |

---

## 2. Algorithm Specifications (Owned by 49-60)

| Algorithm ID     | Description                              | Type              | Documentation                        | Status   |
|------------------|------------------------------------------|-------------------|--------------------------------------|----------|
| ALG-FC-CTRL-001  | Fuel Cell Load Management                | Control           | `CAx/CMP/spec_fc_ctrl_v1.0.pdf`      | WIP      |
| ALG-H2-FLOW-001  | Hydrogen Flow Control                    | Control           | `CAx/CMP/spec_h2_flow_v1.0.pdf`      | WIP      |

---

## 3. Configuration Parameters (Owned by 49-60)

| Parameter ID      | Description                         | Default Value | Range         | Unit | Documentation                     |
|-------------------|-------------------------------------|---------------|---------------|------|-----------------------------------|
| PARAM-FC-TEMP     | Fuel cell operating temperature     | 70            | 60 – 80       | °C   | `CAx/CMP/params_fc.xlsx`          |
| PARAM-H2-PRESS    | H2 supply pressure                  | 3.0           | 2.5 – 4.0     | bar  | `CAx/CMP/params_h2.xlsx`          |

---

## 4. Notes

1. **No Physical Parts**: This subsystem owns no physical hardware.
2. **Algorithm Authority**: 49-60 is the SSOT for auxiliary power control algorithms.
