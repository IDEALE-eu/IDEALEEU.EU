# RISK_REGISTER.md
**IDEALE EU Program – Enterprise Risk Management**

> **Classification**: Internal – ITAR/EAR Controlled  
> **Last Updated**: 2025-10-09  
> **Owner**: Program Risk Manager  
> **Review Cadence**: Bi-weekly (Program Sync), Monthly (Steering Board)  
> **Compliance Alignment**: ARP4761 (Safety), ECSS-Q-ST-80 (Risk), AS9100 §8.2

---

## Purpose
Single source of truth for program risks across engineering, supply chain, quality, and industrialisation. Gate enforcement per **[GOVERNANCE.md](./GOVERNANCE.md)**.

High/critical risks must be accepted, mitigated, or retired before progressing SRR→FRR.

---

## Risk Categories
Technical · Schedule · Cost · Supply chain · Certification · Safety.  
Supply chain risks federated from **[SUPPLY_CHAIN/08-RISK/RISK_REGISTER.csv](./SUPPLY_CHAIN/08-RISK/RISK_REGISTER.csv)**.

---

## Risk Assessment Matrix
| Probability \ Impact | **Low** | **Medium** | **High** |
|---|---|---|---|
| **High** | Medium | High | **Critical** |
| **Medium** | Low | Medium | High |
| **Low** | Low | Low | Medium |

- Low: <10% or minor impact
- Medium: 10–50% or moderate impact
- High: >50% or severe impact (safety, $10M+, ≥3-month slip)

**Critical/High require** mitigation plan, contingency, and Steering Board visibility.

---

## Risk Entry Template
```yaml
- id: RSK-2025-042
  title: "Single-source dependency on radiation-hardened FPGA"
  category: Supply Chain
  description: "Only one qualified vendor supplies RHBD FPGA for flight computer."
  root_cause: "Legacy design; radiation constraints limit market."
  probability: High
  impact: High
  risk_level: Critical
  detection_gate: CDR
  mitigation_plan: |
    - Engage Vendor X on capacity expansion (Q1 2026)
    - Qualify alternate FPGA (Vendor Y) via NRE-funded path
    - Track in SINGLE_SOURCE_LIST.csv with mitigation flag
  owner: Jane Doe (Supply Chain Lead)
  status: Active – Mitigation in Progress
  residual_risk: Medium
  linked_artifacts:
    - ./SUPPLY_CHAIN/08-RISK/SINGLE_SOURCE_LIST.csv
    - ./SUPPLY_CHAIN/17-SPACECRAFT_PARTS/EEE_COMPONENTS/RADIATION_DATA/
    - ./STANDARDS/03-SPACECRAFT/RADIATION/
  next_review: 2025-11-15
````

---

## Current Risk Summary (as of 2025-10-09)

| Level    | Count | Trend |
| -------- | ----: | ----- |
| Critical |     2 | ↓     |
| High     |     5 | →     |
| Medium   |    12 | ↑     |
| Low      |     8 | —     |

Full list maintained in YAML/CSV for dashboards and PLM.

---

## Integration Points

* **Stage Gates**: closure required for sign-off (**[GOVERNANCE.md](./GOVERNANCE.md)**)
* **Supply Chain**: auto-ingest **[SUPPLY_CHAIN/08-RISK/RISK_REGISTER.csv](./SUPPLY_CHAIN/08-RISK/RISK_REGISTER.csv)**
* **Safety**: HARA/SSA links in **[QUALITY_QMS/13-RISK_SAFETY/](./QUALITY_QMS/13-RISK_SAFETY/)**
* **Digital Thread**: IDs embedded in **[DIGITAL_THREAD/04-MBSE/](./DIGITAL_THREAD/04-MBSE/)**
* **ERP**: contingency costs tracked via WBS

---

## Export & Reporting

* Outputs: YAML (source), **[RISK_REGISTER.csv](./RISK_REGISTER.csv)** (analytics), PDF (audit)
* Destinations: Program dashboard, EASA/ECSS audit bundles, Steering Board deck

> To add/update a risk, follow **[CONFIG_MGMT/](./CONFIG_MGMT/)** change control. Re-assess at PDR, CDR, FRR.

````

```csv
# RISK_REGISTER.csv
risk_id,title,category,description,root_cause,probability,impact,risk_level,mitigation_plan,contingency,owner,status,residual_probability,residual_impact,residual_level,links,created_on,due_review,gating_dependency
````

```dax
-- RISK_DASHBOARD_MEASURES.dax

Risk Level = 'Risks'[probability] * 'Risks'[impact]

Critical Count =
COUNTROWS(
  FILTER('Risks', 'Risks'[probability] = 3 && 'Risks'[impact] = 3 )
)

High Count (non-critical) =
COUNTROWS(
  FILTER('Risks',
    'Risks'[probability] * 'Risks'[impact] >= 6 &&
    NOT('Risks'[probability] = 3 && 'Risks'[impact] = 3)
  )
)

Medium Count =
COUNTROWS(
  FILTER('Risks',
    'Risks'[probability] * 'Risks'[impact] IN {3,4}
  )
)

Low Count =
COUNTROWS(
  FILTER('Risks',
    'Risks'[probability] * 'Risks'[impact] IN {1,2}
  )
)

On-Time Reviews %
= DIVIDE(
    COUNTROWS(FILTER('Risks', 'Risks'[due_review] >= TODAY())),
    COUNTROWS('Risks')
  )

Mitigations Overdue
= COUNTROWS(
    FILTER('Risks',
      'Risks'[status] IN {"Planned","In-Progress"} &&
      'Risks'[due_review] < TODAY()
    )
  )
```
