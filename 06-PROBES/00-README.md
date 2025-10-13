---
owner: "<TEAM>"
status: "InWork"
last_reviewed: "YYYY-MM-DD"
utcs_anchor: "utcs://PROBES"
tfa_flow: "QS→FWD→UE→FE→CB→QB"
---

# 06-PROBES

Space probe design, systems engineering, and mission definition per ECSS. Uses SPACE-T (STA) chapter sets.

## Contents
- `DOMAIN_INTEGRATION/` — products, models, versions by STA A–M
- `CONFIGURATION_BASE/` — baseline and change control
- `MISSION_DEFINITION/` — objectives, requirements, CONOPS

## STA (A–M)
A Structures & Mechanisms · B Thermal · C Power/EPS · D Comm/TT&C  
E Nav/Time/TDH · F Avionics/FSW · G Control/Autonomy/FDIR  
H ECLSS/Payload · I Propulsion/Fluids · J Sampling/Robotics  
K Environment/Safety/STM · L Ground/Integration/Ops · M Program/Compliance

## ECSS
ECSS-E Engineering · ECSS-M Management · ECSS-Q Quality · ECSS-S System

## Directory skeleton
```

DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT-ID>/MODELS/<MODEL-ID>/VERSION/<TAG>/SYSTEMS/
STA-XX_NAME/
INTEGRATION_VIEW.md
INTERFACE_MATRIX/XX↔OTHERS.csv
SUBSYSTEMS/XX-YY_SUBSYS/
README.md
DELs/
PAx/{ONB,OUT}/
PLM/CAx/{CAD,CAE,CAM,CAI,CAO,CAP,CAS,CAV,CMP}/
SUPPLIERS/
policy/
tests/
META.json

```

## Compliance and evidence
- ECSS coverage matrix: `DOMAIN_INTEGRATION/.../<TAG>/COVERAGE/ECSS_STA_MATRIX.csv`
- V&V evidence: `.../tests/` and `.../PLM/CAx/*`
- ICDs: `INTERFACE_MATRIX/*.csv` with links to ICD docs

## Change control
- Baselines and CCB records live in `CONFIGURATION_BASE/`.

> Note: product-level collapsible synopses must label **“Tailing Functional Architecture”**.
```

