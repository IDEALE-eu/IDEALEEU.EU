# 21-10 · RADIATORS_HEAT_EXCHANGERS — EBOM LINKS (Q10)

**Scope:** Spacecraft thermal hardware for heat rejection and transfer: external radiators, embedded heat-pipe radiators, liquid plate heat exchangers (LPHX), coldplates, manifolds integral to HX assemblies, mounts, TIMs, and coating stacks.  
**Rule:** Physical HW lives here (21-10). Stand-alone pipes/straps/lines in **21-40**. Heaters in **21-30** (or 30-20 if anti-fog). Sensors in **21-60**. Algorithms/FSW evidence elsewhere (no code here).

---

## 0) Engineering BOM References (authoritative)
| ERP Item | P/N (21-10)           | Description                         | Config Baseline | PLM UID           | Status |
|---------:|------------------------|-------------------------------------|-----------------|-------------------|--------|
| ERP-21-10-001 | 21-10-ASSY-RAD-PANEL-L1 | Left radiator panel assembly            | Q10             | PLM:UID:RAD-L1    | RVW    |
| ERP-21-10-002 | 21-10-ASSY-RAD-PANEL-R1 | Right radiator panel assembly           | Q10             | PLM:UID:RAD-R1    | RVW    |
| ERP-21-10-010 | 21-10-ASSY-RAD-HP-EMB   | Embedded heat-pipe radiator (panel)     | Q10             | PLM:UID:RAD-HP    | REL    |
| ERP-21-10-020 | 21-10-ASSY-LPHX-AV      | Avionics liquid plate heat exchanger    | Q10             | PLM:UID:LPHX-AV   | REL    |
| ERP-21-10-030 | 21-10-ASSY-COLDPLATE    | Coldplate, generic avionics             | Q10             | PLM:UID:CPL-STD   | REL    |
| ERP-21-10-040 | 21-10-KIT-MOUNTING      | Mount kit, shims, fasteners             | Q10             | PLM:UID:MKIT-21   | REL    |
| ERP-21-10-050 | 21-10-KIT-COATING       | Optical coating stack (prep+finish)     | Q10             | PLM:UID:COAT-21   | RVW    |

> SSOT = ERP + this EBOM. All EM/QM/FM variants tracked via derived P/N suffixes.

---

## 1) Assemblies (21-10 EBOM SSOT)
| P/N                     | Description                                   | Level | CAx (design)                          | Notes |
|-------------------------|-----------------------------------------------|-------|---------------------------------------|-------|
| 21-10-ASSY-RAD-PANEL-L1 | Radiator panel, port side                     | ASSY  | `CAx/CAD/assy_rad_panel_L1.step`      | May include embedded HP |
| 21-10-ASSY-RAD-PANEL-R1 | Radiator panel, starboard                     | ASSY  | `CAx/CAD/assy_rad_panel_R1.step`      | — |
| 21-10-ASSY-RAD-HP-EMB   | Panel with embedded heat pipes                | ASSY  | `CAx/CAD/assy_rad_hp.step`            | HP routing locked here |
| 21-10-ASSY-LPHX-AV      | Liquid plate heat exchanger (avionics loop)   | ASSY  | `CAx/CAD/assy_lphx_av.step`           | Inlet/outlet IF defined |
| 21-10-ASSY-COLDPLATE    | Coldplate generic                             | ASSY  | `CAx/CAD/assy_coldplate.step`         | Serpentine channel       |
| 21-10-ASSY-MOUNT-TIM    | Mounts + shims + TIM                          | ASSY  | `CAx/CAD/assy_mount_tim.step`         | To 51/06 datums          |
| 21-10-ASSY-COAT-STACK   | Coating/finish stack                          | ASSY  | `CAx/CAP/coat_stack.yaml`             | α/ε certified in CMP     |

---

## 2) Key parts by assembly
| P/N                      | Description                           | Belongs to            | CAx / Docs                       | Note |
|--------------------------|---------------------------------------|-----------------------|----------------------------------|------|
| 21-10-FS-CFRP            | CFRP facesheet                        | RAD-PANEL*            | `CAx/CAD/facesheet_cfrp.step`    | Mass-critical |
| 21-10-CORE-ALHC          | Al honeycomb core                     | RAD-PANEL*            | `CAx/CAD/honeycomb.step`         | Cell size per CMP |
| 21-10-HP-AL/AMM          | Heat pipe (Al housing, NH3/prop)      | RAD-HP-EMB            | `CAx/CAD/heatpipe.step`          | Embedded only |
| 21-10-TUBE-TI            | Ti serpentine tube                    | LPHX/COLDPLATE        | `CAx/CAD/ti_tube.step`           | Proof/burst in CMP |
| 21-10-FIN-AL             | Al fin stack                          | LPHX                  | `CAx/CAD/fin_stack.step`         | — |
| 21-10-MAN-INT            | Integral manifold                      | LPHX                  | `CAx/CAD/manifold.step`          | Ports G1/8 or custom |
| 21-10-COAT-SSM/AZ        | SSM film / white paint (AZ-xx)        | COAT-STACK            | `CAx/CAD/coat_layers.step`       | α/ε in CMP |
| 21-10-TIM-PAD            | Thermal interface pad                  | MOUNT-TIM             | `CAx/CAD/tim_pad.step`           | To 21-30 heaters if used |
| 21-10-SHIM-KIT           | Precision shims                        | MOUNT-TIM             | `CAx/CAD/shims.step`             | Build tolerances |
| 21-10-FAST-M6            | Fasteners M6 ECSS set                  | MOUNT-TIM             | `CAx/CAD/fasteners.step`         | Torque spec in CAP |
| 21-10-SENS-PT1000        | Embedded RTD (if integral to coldplate)| COLDPLATE             | `CAx/CAD/rtd_pt1000.step`        | Cal in 21-60/92 |

> Stand-alone lines/straps/valves live in 21-40; only **integral** manifolds/tubes are owned here.

---

## 3) Cross-links (ownership elsewhere)
- **21-30 HEATERS:** [EBOM links](../21-30_HEATERS/PLM/EBOM_LINKS.md)
- **21-40 PIPES_HEAT_STRAPS:** [EBOM links](../21-40_PIPES_HEAT_STRAPS/PLM/EBOM_LINKS.md)
- **21-60 SENSORS:** [EBOM links](../21-60_SENSORS/PLM/EBOM_LINKS.md)
- **24-ELECTRICAL_POWER (STA-C):** [System EBOM](../../STA-C-POWER-EPS-HARNESS/SYSTEMS/24-ELECTRICAL_POWER/PLM/EBOM_LINKS.md)
- **39-POWER_CONTROL_PANELS / 39-40 RPC (STA-C):** [Subsystem EBOM](../../STA-C-POWER-EPS-HARNESS/SYSTEMS/39-POWER_CONTROL_PANELS/SUBSYSTEMS/39-40_REMOTE_POWER_CONTROLLERS/PLM/EBOM_LINKS.md)
- **30-20 ICE/DEW HEATERS (STA-B):** [EBOM links](../30-ICE_DEW_PREVENTION/SUBSYSTEMS/30-20_HEATERS_ANTIFOG_ANTICE/PLM/EBOM_LINKS.md)
- **21-80 TVAC TESTING:** [EBOM links](../21-80_TVAC_TESTING/PLM/EBOM_LINKS.md)
- **42 AVIONICS (STA-F):** [System root](../../../STA-F-AVIONICS-FSW-DATABUS/SYSTEMS/42-AVIONICS_COMPUTERS_IMA/)
- **93 DATABUS NETWORKS (STA-F):** [System root](../../../STA-F-AVIONICS-FSW-DATABUS/SYSTEMS/93-DATABUS_NETWORKS/)

## 4) Interfaces & ICD
- **ICD Matrix 21↔…:** [`../../INTERFACE_MATRIX/21↔06_24_30_31_39_40_42_51_60_80_93_97.csv`](../../INTERFACE_MATRIX/21↔06_24_30_31_39_40_42_51_60_80_93_97.csv)
  - **Thermal:** coldplate/TIM spec, allowable ∆T/gradients, heat load [W]
  - **Mechanical:** hole patterns, stiffness, flatness, CTE compatibility
  - **Fluid (LPHX only):** inlet/outlet size, pressure/temperature limits, leak rate
  - **Electrical (if embedded heaters/sensors):** 28 V channels via 39-40; RTD wiring via 97

---

## 5) Compliance & evidence (CAx/CMP)
| Topic                               | Reference          | Evidence (CMP)                          |
|-------------------------------------|--------------------|-----------------------------------------|
| Optical properties α/ε              | COAT-QUAL-21       | `CMP/radiator_coating_alpha_epsilon.pdf`|
| Thermal balance & radiator sizing   | THERM-BAL-21       | `CMP/radiator_sizing_calc__r01.xlsx`    |
| HP priming/transport limits         | HP-PROC-21         | `CMP/heatpipe_acceptance__r01.pdf`      |
| LPHX pressure proof/burst           | FLUID-PRS-21       | `CMP/lphx_proof_burst__r01.pdf`         |
| Leak rate (He)                      | LEAK-STD-ECSS      | `CMP/helium_leak_test__r01.pdf`         |
| Vibe/shock (panel & LPHX)           | ENV-VIB-STD        | `CMP/vibe_shock__r01.pdf`               |
| Outgassing/cleanliness              | MAT-OG-STD         | `CMP/outgassing_cleanliness__r01.pdf`   |
| Corrosion/coating adhesion          | COAT-ADH-21        | `CMP/coating_adhesion__r01.pdf`         |

---

## 6) Processes (CAx/CAP/CAM/CAI)
- `CAP/radiator_panel_layup__r01.yaml`
- `CAP/heatpipe_bondline_cure__r01.pdf`
- `CAP/lphx_braze_weld_spec__r01.yaml`
- `CAP/tim_application_torque__r01.pdf`
- `CAI/flatness_inspection_plan__r01.xlsx`
- `CAI/leak_test_procedure__r01.pdf`
- `CAM/drill_pattern_nc__r01.nc`
- `CAM/fin_stack_fixture__r01.step`

---

## 7) Sourcing Information
| Supplier | Supplier P/N     | Our P/N (21-10)        | Material/Spec           | Notes |
|---------|-------------------|------------------------|-------------------------|-------|
| TBD-COAT | SSM-AZ-xxx        | 21-10-COAT-SSM/AZ      | α/ε per COAT-QUAL-21    | Flight lot in CMP |
| TBD-CORE | HC-Al-3.2-xxx     | 21-10-CORE-ALHC        | 5052 Al, cell 3.2 mm    | Certificate in CMP |
| TBD-HP   | HP-AL-NH3-xxx     | 21-10-HP-AL/AMM        | NH3 working fluid       | Orientation limits |
| TBD-TI   | TUBE-Ti-x.y-xxx   | 21-10-TUBE-TI          | Ti Grade 2              | Cleanliness class |
| TBD-TIM  | TIM-Pad-xx        | 21-10-TIM-PAD          | k ≥ 6 W/m·K             | Thickness tolerance |

> All sourcing is configuration-controlled in ERP; this table mirrors the current Q10 baseline.

---

## 8) Versioning & UTCS/IEF
- **Baseline:** Q10-21-10  
- **UTCS:** `utcs://AMPEL360/21/10/Q10`  
- **IEF manifest:** `PLM/.ief/21-10-radiators_heat_exchangers.ief.json`

**Note:** No software or firmware binaries under 21-10. Any telemetry/controls are hosted in 42; parameter limits live with 21-30/21-60 evidence.
