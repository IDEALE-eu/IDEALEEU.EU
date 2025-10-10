# 39-20 · SWITCHGEAR_RELAYS_CONTACTORS — EBOM LINKS (Q10)

**Scope:** Electromechanical switching devices: relays, contactors, switches for high-reliability power control.  
**Rule:** Physical HW lives here (39-20). Solid-state switching in **39-40**. Control logic in **39-60**. No code stored here.

---

## 1) Assemblies (39-20 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 39-20-ASSY-RELAY-BANK  | Relay Bank Assembly (8 channels)             | ASSY  | `CAx/CAD/assy_relay_bank.step`        | REL    |
| 39-20-ASSY-CONT-PWR    | Power Contactor Assembly                     | ASSY  | `CAx/CAD/assy_cont_pwr.step`          | REL    |
| 39-20-ASSY-SW-MANUAL   | Manual Override Switch Panel                 | ASSY  | `CAx/CAD/assy_sw_manual.step`         | RVW    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 39-20-RELAY-LATCH-28V   | Latching relay 28V 10A                | RELAY-BANK        | `CAx/CAD/relay_latch.step`         | Magnetic latch  |
| 39-20-CONT-50A          | Power contactor 50A                   | CONT-PWR          | `CAx/CAD/contactor_50a.step`       | Arc suppression |
| 39-20-SW-TOGGLE         | Toggle switch (manual override)       | SW-MANUAL         | `CAx/CAD/sw_toggle.step`           | MIL-PRF-8805    |

---

## 3) Cross-references
- **Relay selection criteria**: `CAx/CMP/relay_selection.pdf`
- **Life cycle testing**: `CAx/CAV/relay_life_test.xlsx`
- **Arc suppression**: `CAx/CAE/arc_suppression_analysis.pdf`

---

## 4) Configuration notes
- Relay types: Latching (power-efficient), non-latching (fail-safe)
- Contact rating: 10–50 A depending on application
- Cycle life: > 100,000 operations
- Response time: < 10 ms
