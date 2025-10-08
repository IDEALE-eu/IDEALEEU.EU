# IDEALEEU.EU
www.idealeeu.eu

**PROGRAM CHARTER**

* Goal: design, certify, manufacture, and industrialise both vehicles.
* Success: flight‑ready prototypes, type certification/flight‑worthiness, serial ramp ≥ target rate, cost and safety KPIs met.
* Standards baseline: ARP4754A/ARP4761, DO‑178C/DO‑254/DO‑160, AS9100. ECSS for spacecraft. CS‑23/CS‑25 TBD.

**STAGE GATES**

* SRR → MCR → PDR → CDR → TRR → PRR → ORR/EIS (aircraft) / FRR (spacecraft).
* V&V: requirements trace, HARA/SSA, FTA/FMEA, flight/ground test, conformity.

**DIGITAL THREAD**

* PLM/PDM: CAD, CAE, CAO, CAM, CAI, CAV, CAS, CMP.
* MBSE: SysML, interface control, digital twin.
* MES/ERP/QMS: EBOM↔MBOM, routings, NCRs, CoC, traceability.

**INDUSTRIALISATION**

* DFM/DFA, tooling, supplier qualification, PPAP/FAI, rate readiness, MRO setup.

**REPO/PLM STRUCTURE (PROGRAM → AIRCRAFT | SPACECRAFT)**

```
IDEALEEU.EU/
├─ 00-PROGRAM/
│  ├─ README.md  ├─ GOVERNANCE.md  ├─ ROADMAP.md
│  ├─ STANDARDS/ (ARP4754A, ARP4761, DO-178C, DO-254, DO-160, ECSS, AS9100)
│  ├─ RISK_REGISTER.md  ├─ CONFIG_MGMT/  ├─ QUALITY_QMS/
│  ├─ SUPPLY_CHAIN/  ├─ INDUSTRIALISATION/  └─ DIGITAL_THREAD/
├─ 01-FLEET/                       # global ops, learning, strategy
│  ├─ OPERATIONAL_DATA_HUB/        # EIS, sensor logs, usage profiles
│  ├─ FEDERATED_LEARNING/          # fleet-wide models
│  ├─ MRO_STRATEGY/                # CAS/CMP policies
│  └─ FLEET_OPTIMISATION/          # scheduling, resources
├─ 02-AIRCRAFT/
│  ├─ 00-README.md  ├─ CONFIGURATION_BASE/  ├─ FINAL_ASSEMBLY_OPS/
│  ├─ CROSS_SYSTEM_INTEGRATION/  ├─ DIGITAL_TWIN_MODEL/
│  └─ DOMAIN_INTEGRATION/
│     ├─ AIRFRAMES/ (SYSTEMS_INTEGRATION_FE/ ZONES/.../PLM/)
│     ├─ MECHANICAL_CONTROL_SYSTEMS/ (LG/FC/HYD/…/PLM/)
│     ├─ CABINS_CARGO_PAX/ (PLM/)
│     ├─ INFO_COMM_AVIONICS/ (PLM/ QUANTUM_COMPUTING_CQH/)
│     ├─ CIRCULAR_SYSTEMS_MATERIALS/ (PLM/)
│     ├─ INFRASTRUCTURES/ (PLM/)
│     ├─ H2_THERMAL/ (PLM/)
│     └─ GENERATION_PROPULSION_ENERGY/ (PLM/)
├─ 03-SPACECRAFT/
│  ├─ 00-README.md  ├─ MISSION_DEFINITION/  ├─ CONFIGURATION_BASE/
│  ├─ SYSTEMS_ENGINEERING/ (ICDs, budgets, CONOPS, AIT)
│  ├─ AIT/ (Assembly, Integration, Test)  ├─ GSE/  ├─ GNC/
│  ├─ POWER_THERMAL/  ├─ PROPULSION/  ├─ AVIONICS_COMMS/
│  ├─ STRUCTURES/  ├─ SOFTWARE/  ├─ RADIATION/
│  └─ CERTIFICATION_AND_SAFETY/ (ECSS compliance, safety cases)
└─ 04-BUSINESS/
   ├─ MARKET/  ├─ PARTNERSHIPS/  ├─ IP_LICENSES/  └─ FINANCE/
```

**KEY INTERFACES**

* Aircraft↔Spacecraft shared tech: materials, thermal, avionics, propulsion test assets.
* Fleet layer supplies usage data and learning back into design.

**METRICS**

* Requirements coverage ≥ 99%. Defect escape rate ≤ target. Weight/mass budgets within margin. Schedule variance ≤ target. Cost per unit within target.
