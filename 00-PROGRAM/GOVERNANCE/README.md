# 00-PROGRAM / GOVERNANCE

Program governance, compliance, and decision rights for **AMPEL360** (Q-baselines).

> **Canon**: TFA flow = **QS → FWD → UE → FE → CB → QB**  
> * **QS** (Quantum Superposition): Pre-event state capture with multiple potential outcomes
> * **FWD** (Future/Waves Dynamics): Predictive/retrodictive modeling
> * **UE** (Unit Element): Classical fundamental units
> * **FE** (Federation Entanglement): Distributed multi-party coordination
> * **CB** (Classical Bit): Post-event deterministic reality anchoring
> * **QB** (Qubit): Quantum computation strategies
>
> **UTCS** = UiX Threading Context/Content/Cache and Structure/Style/Sheet

---

## 1. Scope

- Configuration Management (CM), Quality Management System (QMS), Security, Ethics  
- Governance Boards: CCB, Safety Board, Data Protection Office (DPO), Ethics Committee  
- Artifacts and gates controlling release to fleet/mission

---

## 2. Structure

```
00-PROGRAM/
├── GOVERNANCE/               # This README, policies, codes of conduct
│   ├── README.md
│   └── MAL-EEM/              # ML Ethics & Empathy Modules (authoritative artifacts)
│       ├── README.md
│       ├── model_cards/
│       ├── data_sheets/
│       ├── risk_assessments/
│       ├── bias_fairness/
│       ├── safety_case/
│       ├── scriptbook/
│       ├── red_team/
│       └── examples/
├── CONFIG_MGMT/              # CM plan, baselines, changes, traceability
│   ├── 01-CM_PLAN.md
│   ├── 04-BASELINES/
│   ├── 09-INTERFACES/
│   └── 10-TRACEABILITY/      # UTCS threads, link maps, evidence indexes
├── QUALITY/                  # QMS, audits, NCR/CAPA
├── SECURITY/                 # Risk, keys, SBOM/VEX, incident response
├── COMPLIANCE/               # Standards mapping, declarations
├── REVIEW_BOARDS/            # Charters, minutes, decisions
│   ├── CCB/
│   │   ├── charter.md
│   │   ├── minutes/
│   │   └── decisions/
│   ├── SAFETY/
│   ├── DATA_PROTECTION/
│   └── ETHICS/
└── TEMPLATES/                # Forms and checklists
    ├── MAL-EEM/
    ├── IEF/
    ├── DPIA/
    ├── NCR_CAPA/
    ├── SBOM_VEX/
    └── Board-Minutes.md
```

**Cross-References**  
- CM Plan → [`../CONFIG_MGMT/01-CM_PLAN.md`](../CONFIG_MGMT/01-CM_PLAN.md)  
- Baselines → [`../CONFIG_MGMT/04-BASELINES/`](../CONFIG_MGMT/04-BASELINES/)  
- Interfaces → [`../CONFIG_MGMT/09-INTERFACES/`](../CONFIG_MGMT/09-INTERFACES/)  
- Traceability / UTCS → [`../CONFIG_MGMT/10-TRACEABILITY/`](../CONFIG_MGMT/10-TRACEABILITY/)

---

## 3. Top-Level Policies

- **Release Integrity**: Signatures, hashes, and IEF manifests required for `REL`  
- **Separation of Concerns**: HW/SW artifacts live with host LRUs; other subsystems link to evidence only  
- **Safety First**: Hazard closure required before operational exposure  
- **Data Minimization**: Collect only what's necessary; document purpose and retention  
- **Explainability**: ML decisions impacting operations must expose rationale or uncertainty bounds  
- **Auditability**: Every `REL` is reproducible from CB/QB using UTCS evidence

---

## 4. MAL-EEM — Machine Learning Ethics & Empathy Modules

Authoritative policy for ML features and any "empathy/affect" behavior.

### 4.1 Definitions
- **MAL**: Machine-Assisted Learning used in design, test, or operations  
- **EEM**: Empathy/Emotion-like Modules (tone, de-escalation, user guidance). EEM is *presentation only*, not cognition

### 4.2 Allow / Disallow
| Allowed | Disallowed |
|--------|-----------|
| Safety prompts | Simulated consciousness |
| Respectful tone control | Deceptive anthropomorphism |
| Accessibility aids | Covert persuasion |
| Human-in-the-loop copilots | Medical/legal advice without human sign-off |
| Post-incident coaching | Hidden data capture |

### 4.3 Required Artifacts → [`./MAL-EEM/`](./MAL-EEM/)
- Model Card (purpose, limits, evaluations)  
- Data Sheet (provenance, consent, license)  
- Risk Assessment (hazards, misuse, mitigations)  
- Bias/Fairness Report (metrics, slices, remediation)  
- Safety Case (claims, evidence, residual risk)  
- Human Factors Review (HCI, cognitive load)  
- EEM Scriptbook (phrasing rules, forbidden patterns)  
- Logging & Red-Team Report (scenarios, findings, fixes)

### 4.4 Process & Gates

| Gate | Inputs | Board | Exit | Pass Criteria |
|------|--------|-------|------|----------------|
| **P0 Charter** | Problem statement, harms | Ethics + Safety | Go/No-Go | Scope documented; harm taxonomy mapped; stakeholders named |
| **P1 Data** | Data Sheet, DPIA | DPO + Ethics | Data OK | Provenance complete; legal basis; PII minimized; retention ≤ policy |
| **P2 Model** | Model Card, eval plan | ML Lead + Safety | Train OK | Metrics ≥ thresholds; uncertainty spec; hazards linked |
| **P3 EEM** | Scriptbook, UX spec | Ethics + HF | UI OK | No anthropomorphism; accessibility passed; escalation path |
| **P4 Red-Team** | Red-team report, fixes | Security + Ethics | Pre-Deploy | High-risk findings closed; kill-switch validated |
| **REL** | Safety Case, sign-offs, IEF | CCB | Release | IEF complete; signatures verified; NCR-High = 0 |

Decisions logged in [`../REVIEW_BOARDS/`](../REVIEW_BOARDS/) with UTCS IDs.

### 4.5 Controls
- **Consent & Privacy**: Purpose, retention, and opt-out documented in DPIA  
- **Bias**: Parity metrics per slice; regression budget tracked  
- **Safety Interlocks**: Rate limits, safewords, human escalation  
- **Observability**: Opt-in telemetry with k-anonymity and deletion path  
- **Rollback**: Versioned models, fast revert, kill-switch runbook

### 4.6 EEM Guardrails
- ❌ No claims of feelings, embodiment, or self-awareness  
- ℹ️ Use disclaimers when guidance is non-deterministic  
- 📚 Provide citations or uncertainty ranges when applicable

**Templates**: [`../TEMPLATES/MAL-EEM/`](../TEMPLATES/MAL-EEM/)  
**Examples**: [`./MAL-EEM/examples/`](./MAL-EEM/examples/)

---

## 5. Roles & RACI

| Role | Accountabilities | R | A | C | I |
|------|------------------|---|---|---|---|
| Program Manager | Delivery, budget, staffing | | **A** | CCB, Safety, Ethics | Boards |
| CCB Chair | Configuration authority | **R** | **A** | Safety | All teams |
| Safety Lead | Hazard closure | **R** | | CCB | Ops, PM |
| Ethics Officer | MAL-EEM enforcement | **R** | | DPO, HF | CCB |
| DPO | Data protection, DPIA | **R** | | Ethics | PM |
| Security Lead | Threat modeling, SBOM/VEX | **R** | | CCB | PM |
| ML Lead | Model quality, monitoring | **R** | | Safety, Ethics | PM |

> **R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed

---

## 6. Evidence & Sign-off

- All `REL` packages must include `IEF/manifest.json`, SHA256 hashes, and cryptographic signatures  
- Approvals stored under [`../REVIEW_BOARDS/<board>/decisions/`](../REVIEW_BOARDS/) with UTCS thread IDs

### 6.1 IEF Manifest — Minimal JSON Schema

See: [`../TEMPLATES/IEF/manifest.schema.json`](../TEMPLATES/IEF/manifest.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "IEF Manifest",
  "type": "object",
  "required": ["rel_id", "utcs", "artifacts", "hashes", "signatures", "provenance"],
  "properties": {
    "rel_id": {"type": "string"},
    "utcs": {"type": "string"},
    "artifacts": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "path", "sha256"],
        "properties": {
          "name": {"type": "string"},
          "path": {"type": "string"},
          "sha256": {"type": "string"},
          "sbom": {"type": "string"},
          "vex": {"type": "string"}
        }
      }
    },
    "hashes": {"type": "object"},
    "signatures": {"type": "array", "items": {"type": "string"}},
    "provenance": {
      "type": "object",
      "required": ["builder", "cb", "qb", "timestamp"],
      "properties": {
        "builder": {"type": "string"},
        "cb": {"type": "string"},
        "qb": {"type": "string"},
        "timestamp": {"type": "string", "format": "date-time"}
      }
    }
  }
}
```

### 6.2 Release Package Layout

```
REL-<id>/
├── IEF/
│   ├── manifest.json
│   └── manifest.json.sig
├── ARTIFACTS/
│   └── <LRU|SW|HW>/
├── EVIDENCE/
│   ├── safety_case/
│   └── test_reports/
├── SBOM/
└── VEX/
```

---

## 7. Metrics

* Evidence coverage ≥ **99%** mapped to UTCS threads
* Open **High** severity NCR = **0** for release
* MAL-EEM bias regression ≤ budget
* Mean time to rollback ≤ target
* Kill-switch activation → containment ≤ target

### 7.1 Example SLOs

| Metric               | Target    | Window                |
| -------------------- | --------- | --------------------- |
| MTTR (rollback)      | ≤ 30 min  | trailing 90 days      |
| Safety incident rate | 0 Class-A | trailing 12 months    |
| Bias parity Δ        | ≤ 1.5%    | per demographic slice |

---

## 8. Standards & Compliance Mapping

Maintain full matrix at [`../COMPLIANCE/standards-mapping.csv`](../COMPLIANCE/standards-mapping.csv)

| Control     | DO-178C | ARP4754A | ISO 27001 | ISO 14971     | GDPR    | Notes                     |
| ----------- | ------- | -------- | --------- | ------------- | ------- | ------------------------- |
| CM          | A-8     | 5.3      | A.8.32    | —             | —       | Baselines, change control |
| Safety case | —       | 5.5      | —         | Risk controls | —       | Hazard closure before ops |
| DPIA        | —       | —        | —         | —             | Art. 35 | DPO sign-off required     |
| SBOM/VEX    | —       | —        | A.5.33    | —             | —       | Supplier security         |
| ML evals    | —       | —        | —         | —             | —       | Tied to MAL-EEM           |

---

## 9. Security Essentials

* Threat model per LRU/SW unit
* Keys: custody, rotation, HSM if available
* SBOM required for all software; VEX for known issues
* Incident response runbook with comms and evidence capture
* All attestations stored under `SECURITY/`

---

## 10. Templates

* [`../TEMPLATES/Board-Minutes.md`](../TEMPLATES/Board-Minutes.md)
* [`../TEMPLATES/IEF/manifest.schema.json`](../TEMPLATES/IEF/manifest.schema.json)
* [`../TEMPLATES/DPIA/checklist.md`](../TEMPLATES/DPIA/checklist.md)
* [`../TEMPLATES/NCR_CAPA/form.md`](../TEMPLATES/NCR_CAPA/form.md)
* [`../TEMPLATES/SBOM_VEX/attestation.md`](../TEMPLATES/SBOM_VEX/attestation.md)
* [`../TEMPLATES/MAL-EEM/scriptbook.md`](../TEMPLATES/MAL-EEM/scriptbook.md)

---

## 11. Glossary

* **IEF**: Integrity & Evidence Framework
* **UTCS**: UiX Threading Context/Content/Cache and Structure/Style/Sheet
* **REL**: Released, immutable baseline
* **DPIA**: Data Protection Impact Assessment
* **LRU**: Line Replaceable Unit

---

## 12. Appendices

### A) Board Minutes Template

See: [`../TEMPLATES/Board-Minutes.md`](../TEMPLATES/Board-Minutes.md)

### B) DPIA Checklist (Excerpt)

* Purpose and legal basis recorded
* Data inventory and flows mapped
* Minimization validated
* Retention and deletion paths set
* DPO sign-off stored under `REVIEW_BOARDS/DATA_PROTECTION/`

### C) Signing Procedure

1. Compute `sha256` for each artifact
2. Generate `IEF/manifest.json` and validate against schema
3. Produce detached signatures
4. Store under `REL/IEF/` and record UTCS thread

### D) SBOM/VEX Requirements

* **SBOM format**: SPDX 2.3 or CycloneDX 1.5
* **VEX**: References SBOM components and CVEs with status, analysis, and remediation
