# IDEALEEU

> Unified, audit‑ready platform for multi‑vehicle aerospace programs. Modules: **AMSDP** (Aerospace Material & Software Digital Passports) and **AAMMPP** (Aerospace Assets Management, Maintenance & Procurement Platform).

---

## Badges

[![Status](https://img.shields.io/badge/status-alpha-yellow)](#)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

<!-- Add real CI badges once pipelines are enabled -->

---

## TL;DR

IDEALEEU provides a verifiable digital thread from requirements to fleet operations. **AMSDP** issues and verifies digital passports for materials, parts, and software. **AAMMPP** manages the canonical item master, configuration, maintenance, and procurement workflows. Together they deliver trusted, interoperable exchanges across OEMs, suppliers, operators, and regulators.

### Summary

Unified platform connecting manufacturers, operators, network suppliers, and component vendors **not only to exchange data**, but also to **repair, refurbish, requalify, and reintroduce parts** with traceable evidence in digital passports. Includes **governed redistribution of mixed DevOps licenses** (seats + usage) for cross‑company collaboration without IP leakage.

---

## Table of contents

* [Mission & Scope](#mission--scope)
* [Core Capabilities](#core-capabilities)
* [Architecture Overview](#architecture-overview)
* [Standards & Interop Targets](#standards--interop-targets)
* [Repository Layout](#repository-layout)
* [Quickstart (Developer)](#quickstart-developer)
* [Configuration](#configuration)
* [Component taxonomy](#component-taxonomy)
* [Circularity and MRO](#circularity-and-mro)
* [Data Contracts](#data-contracts)
* [APIs](#apis)
* [Security Model](#security-model)
* [CI/CD](#cicd)
* [Releases & Changelog](#releases--changelog)
* [LLM Playground](#llm-playground)
* [Collaborative DevOps licensing](#collaborative-devops-licensing)
* [Deployment](#deployment)
* [Operations](#operations)
* [Governance](#governance)
* [Contributing](#contributing)
* [Roadmap](#roadmap)
* [License](#license)
* [Security Policy](#security-policy)
* [Support](#support)
* [Extended materials](#extended-materials)

---

## Mission & Scope

**Mission**: Deliver certified, serial‑ready aerospace systems with a closed‑loop digital thread from concept to fleet operations.

**Scope**: End‑to‑end lifecycle: requirements → design → verification & certification → industrialization & production → operations → continuous improvement.

---

## Core Capabilities

* **Traceability & Provenance**: Part pedigree, software build lineage, conformity statements, audit trails.
* **Configuration Control**: Baselines, EOs/ECNs, effectivity, serialization, configuration state.
* **Digital Passports (AMSDP)**: Issue, verify, revoke, and transfer credentials for material/part/software.
* **Lifecycle Ops (AAMMPP)**: Item master, maintenance plans, work orders, reliability, inventory, procurement.
* **Data Contracts**: Typed schemas with versioning, backward‑compat rules, conformance tests.
* **Interoperability**: Opinionated mappings to aerospace and supply‑chain standards.
* **Audit‑Ready**: Tamper‑evident logs, SBOMs, build provenance, retention policies.
* **Circularity & MRO**: Repair, rework, requalification, return‑to‑service with evidence written to passports and configuration.
* **Collaborative DevOps licensing**: Mixed seat+usage entitlements with governed redistribution across partner orgs.

---

## Architecture Overview

* **Identity & Trust**: Issuer registry, key management, verifiable attestations, RBAC/ABAC.
* **Control Layer (MAL)**: Master Application Layer/Logic acting as the PLC of each domain; orchestrates workflows and policies.
* **Data Plane**: Schema registry, contract testing, lineage catalog, event store.
* **Services**:

  * **AMSDP**: Credential service, passport vault, verifier, revocation registry.
  * **AAMMPP**: Item master, configuration, MRO, procurement, inventory.
  * **API Gateway**: REST/GraphQL ingress, OAuth2/OIDC.
  * **Events**: Async bus for integrations and workflows.
* **Storage**: OLTP store, object storage for artifacts, append‑only audit log.
* **Integrations**: PLM/ERP/MES, certification authorities, supplier portals, operator systems.

> See `/docs/architecture/` for diagrams and sequence flows.

---

## Standards & Interop Targets

* **Identity & Credentials**: W3C Verifiable Credentials/Presentations.
* **Supply Chain Events**: GS1 EPCIS 2.0 + CBV.
* **Tech Pubs & Procurement**: ASD S‑Series (S1000D, S2000M).
* **Software Assurance**: SBOM (CycloneDX), SLSA provenance attestations.
* **Lifecycle & Systems**: ISO/IEC/IEEE 15288, INCOSE guidance.
* **Aero Certification References**: DO‑178C/DO‑330, DO‑254, ARP4754A/ARP4761 (alignment targets, not declarations of compliance).

---

## Repository Layout

```
/                      # Monorepo root
/docs/                 # Documentation site and guides
/00-PROGRAM/           # Governance and engineering core
  platform/            # Executable platform (code & services)
    amsdp/             # Digital passports (issue/verify/revoke)
    aammpp/            # Item master, maintenance, procurement
    api/               # OpenAPI, GraphQL schemas, gateway config
    schemas/           # JSON/Avro/Proto contracts + tests
    clients/           # SDKs and examples
    infra/             # IaC, Docker, Helm, GH Actions
    tools/             # CLIs, generators, loaders
    llm/               # Provider-agnostic gateway, guardrails, eval
      gateway/
      embed/
      rag/
      guardrails/
      eval/
    playground-ui/     # Tenant playground (UI)
    vector/            # Vector DB adapters (pgvector, Qdrant)
    service/           # RMA, repair, requalification, RTS flows
    licensing/         # Entitlements, allocations, transfers
/01-FLEET/             # Operational data hub, MRO, federated learning
/02-AIRCRAFT/          # AIR-T baselines, domain integration, twin
/03-SPACECRAFT/        # STA baselines, domain integration, AIT/mission
/04-SATELLITES/        # Satellite product structures
/05-TELESCOPES/        # Observatory payload/domain structures
/06-PROBES/            # Deep-space probes
/07-DRONES/            # UAS/UAM product lines
/08-LAUNCHERS/         # Launch vehicles
/09-STM-SPACE-STATION-MODULES/ # Station modules/segments
/10-BUSINESS/          # Market, partnerships, finance
```

> Platform lives under `/00-PROGRAM/platform`. PLM and MRO are distributed per product under `/0X-*/…/{PLM|MRO}/`.

---

## Quickstart (Developer)

### Prerequisites

* Git, Docker, Docker Compose, Make
* Node 20+ and Python 3.11+ (tooling and SDKs)

### Bootstrap

```bash
git clone https://github.com/IDEALE-eu/IDEALEEU
cd IDEALEEU
make bootstrap        # install tooling, pre-commit hooks
make build            # docker compose build
make up               # docker compose up -d
make test             # run unit and contract tests
```

### Useful Targets

```bash
make up down logs lint fmt test test-contracts sbom provenance release
```

---

## Configuration

Set via environment or `.env`.

```ini
IDEALE_ENV=dev
IDEALE_LOG_LEVEL=info
IDEALE_DB_URL=postgresql://user:pass@db:5432/ideale
IDEALE_OBJECT_STORE=s3://bucket/prefix
OIDC_ISSUER_URL=https://auth.example.com/
OIDC_AUDIENCE=ideale-api
JWT_SIGNING_KEY=change-me
EVENT_BUS_URL=nats://nats:4222
```

Secrets must be injected via the orchestrator secret store; do not commit secrets.

---

## Component taxonomy

Canonical classes and required passport claims.

### Classes (enum)

* `primary_structure`
* `secondary_structure`
* `installation_hardware`
* `information_hardware`
* `software`
* `model`
* `firmware`
* `sensor_antenna`

### Common identifiers

* `componentClass` (enum above)
* `componentType` (controlled vocab, e.g., `wing_spar`, `fastener_rivet`, `lru_fms`, `uC_firmware`, `fem_model`, `gnss_antenna`)
* `ciId` (configuration item ID)
* `partNumber` (canonical PN)
* `serialNumber` (where applicable)
* `effectivity` (tail numbers, lots, ranges)
* `asDesignedId` • `asPlannedId` • `asBuiltId`

### Minimum passport claims by class

**primary_structure**: Material spec/process, ply/stack or forging route; heat/lot; NDI results; dimensional report; CoC/CoA; stress justification ref; surface treatment.

**secondary_structure**: Material/finish, lot, inspection record; CoC; torque/installation spec if relevant.

**installation_hardware**: Standard ref (NAS/MS/EN/AS), grip/size/finish; lot/heat; torque/bakeout spec; CoC.

**information_hardware**: LRU model/P/N, CPU/FPGA ID, interfaces, PSU range; firmware baseline; calibration certs; environmental quals (DO‑160/EN 2282) refs.

**software**: Version, build hash, target LRU(s); SBOM (CycloneDX) and SLSA provenance; safety level target (e.g., DO‑178C A–E) and approval trail.

**model**: Model type (CAD/FEM/CFD/MBSE), toolchain/version; source dataset; V&V evidence; export‑control tag.

**firmware**: Target device, bootloader reqs, image digest; SBOM/provenance; signing chain; rollback policy.

**sensor_antenna**: Type, band, pattern/ref; calibration certificate; serial; environmental quals.

### Lifecycle states (all classes)

`draft` → `released` → `fabricated_or_loaded` → `inspected` → `installed` → `in_service` → `retired_or_scrapped`

### Relationships

Assemblies ↔ subassemblies ↔ parts via EBOM/MBOM. Serialized BOM for `asBuilt` with trace to passports and work orders.

### Schemas and location

* `/00-PROGRAM/platform/schemas/components/common/Component.v1.json` (base)
* `/00-PROGRAM/platform/schemas/components/<class>/Passport.v1.json` (per class)
* `/00-PROGRAM/platform/schemas/bom/` (EBOM/MBOM/SerializedBOM)

---

## Circularity and MRO

**Distributed model**: MRO data and procedures live under each product portfolio path, not centrally.

Portfolio placement per product:

```
/0X-*/DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT>/MODELS/<MODEL>/VERSION/<Qn>/MRO/
```

Service and circularity flow:

1. **Repair order / RMA** → intake and diagnostics.
2. **Repair / rework** under approved procedures.
3. **Tests / NDI** and functional verification.
4. **Requalification / recertification** with e‑signatures and SOF.
5. **Digital passport update** and configuration state update.
6. **Release** and **return to service**; order closure.

Minimum evidence: inspection reports, NDI results, calibration certificates, firmware/software baseline, **SBOM + provenance**, hours/cycles, and EBOM/MBOM impact.

Supported operations: rotable pools, controlled cannibalization, redistribution across fleets, CCB approval, segregation of duties.

EPCIS events: *Commission*, *Observation*, *Transformation*, *Aggregation* for each transition.

---

## Data Contracts

* Contracts live in `/00-PROGRAM/platform/schemas` with versioned folders.
* Compatibility policy: **backward‑compatible minor**, **breaking major**.
* Contract tests run in CI; producers and consumers must pass.

Example: minimal material passport (JSON)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "MaterialPassport.v1",
  "type": "object",
  "required": ["materialId", "lot", "issuer", "claims"],
  "properties": {
    "materialId": {"type": "string"},
    "lot": {"type": "string"},
    "issuer": {"type": "string", "format": "uri"},
    "claims": {"type": "object"}
  }
}
```

**New contracts**

* `/00-PROGRAM/platform/schemas/service/RMA.v1.json`
* `/00-PROGRAM/platform/schemas/service/RepairOrder.v1.json`
* `/00-PROGRAM/platform/schemas/service/RequalificationReport.v1.json`
* `/00-PROGRAM/platform/schemas/service/Reintroduction.v1.json`
* `/00-PROGRAM/platform/schemas/licensing/Entitlement.v1.json`
* `/00-PROGRAM/platform/schemas/licensing/Assignment.v1.json`
* `/00-PROGRAM/platform/schemas/licensing/Transfer.v1.json`

---

## APIs

* **REST/GraphQL** via gateway. OpenAPI in `/00-PROGRAM/platform/api/openapi.yaml`. Async events in `/00-PROGRAM/platform/api/asyncapi.yaml`.
* Example flow:

  1. Obtain token via OIDC.
  2. `POST /amsdp/v1/passports` to issue.
  3. `POST /amsdp/v1/verify` with credential or reference.
  4. `POST /amsdp/v1/revoke` to revoke.

**Service & Licensing endpoints**

* `POST /service/v1/rma` — create return‑material authorization
* `POST /service/v1/repairs` — register repair/rework
* `POST /service/v1/requalifications` — attach test results and approvals
* `POST /service/v1/reintroductions` — mark return‑to‑service
* `GET  /service/v1/work-orders/{id}` — status and evidence bundle
* `POST /licensing/v1/entitlements` — declare entitlements (seat/usage)
* `POST /licensing/v1/allocations` — allocate to users/orgs/projects
* `POST /licensing/v1/transfers` — governed redistribution between partners
* `GET  /licensing/v1/entitlements/{id}` — retrieve entitlement state

---

## Security Model

* Zero‑trust defaults; least‑privilege RBAC/ABAC.
* Keys managed via KMS/HSM; rotation enforced.
* Tamper‑evident append‑only audit log.
* Supply‑chain hardening: SBOM, vuln scanning, provenance attestations on releases.
* Threat modeling with STRIDE; findings tracked in `SECURITY.md`.
* **Crypto**: PQC‑ready design; see `SECURITY.md` for concrete algorithms and status.

> This repository does **not** assert regulatory compliance. Evidence and alignment targets support audits.

---

## CI/CD

* GitHub Actions: build, lint, tests, contract tests, CodeQL, container scan.
* Release: semantic versioning, changelog, signed containers/artifacts, SBOM attach, SLSA provenance.

---

## Releases & Changelog

See `CHANGELOG.md` and GitHub Releases.

---

## LLM Playground

Multi‑tenant sandbox for trained, contextualized, embedded AI over IDEALE‑EU data.

* **Components**: `/00-PROGRAM/platform/playground-ui`, `/00-PROGRAM/platform/llm/gateway`, `/00-PROGRAM/platform/llm/embed`, `/00-PROGRAM/platform/llm/rag`, `/00-PROGRAM/platform/llm/guardrails`, `/00-PROGRAM/platform/vector`.
* **APIs**: `POST /llm/chat`, `POST /llm/embed`, `POST /knowledge/sync`, `POST /contexts`.
* **Security**: tenant/project namespaces; KMS‑backed keys; full prompt/tool/output audit.
* **Eval**: golden sets, EM/F1, groundedness, latency, cost; shadow runs.

---

## Collaborative DevOps licensing

* Mixed seats+usage with budgets per project and phase.
* Governed redistribution of rights across program partners; traceable and expiring.
* Isolation by `{tenant}/{project}`; scopes by repo/pipeline/environment.
* Full audit of assignments and usage; only entitlement metadata shared.

---

## Deployment

### Local (docker compose)

```bash
docker compose up -d
```

### Images

* ghcr.io/ideale-eu/idealeeu-api:latest
* ghcr.io/ideale-eu/idealeeu-gateway:latest
* ghcr.io/ideale-eu/idealeeu-playground:latest

> Replace with your registry if different.

### Kubernetes (Helm)

```bash
helm repo add ideale https://ideale-eu.github.io/charts
helm upgrade --install ideale ideale/ideale-eu \
  --namespace ideale --create-namespace \
  -f infra/helm/values.dev.yaml
```

Readiness/liveness probes, HPA, and resource limits are defined in the Helm chart.

---

## Operations

* **Observability**: Structured logs, metrics, traces. Prometheus and OTLP exporters by default.
* **Backups & DR**: PITR for databases; object store lifecycle rules.
* **Retention**: Defaults in `/docs/governance/retention.md`.
* **Runbooks**: `/docs/runbooks/` for common incidents.

---

## Governance

* **CODEOWNERS** for critical paths.
* **ADRs** in `/docs/adr/` with status and decision context.
* **Change Control**: RFC issue template, review gates, affected‑system checklist.
* **Commit Convention**: Conventional Commits.

---

## Contributing

See `CONTRIBUTING.md` for setup, coding standards, commit rules, and DCO/CLA if applicable.

---

## Roadmap

* v0.1: Public repo, schemas, bootstrap, compose, basic AMSDP issue/verify.
* v0.2: AAMMPP item master, inventory, basic work orders, GraphQL façade.
* v0.3: EPCIS event ingest, supplier onboarding flows.
* v1.0: Pilot hardening, signed releases, docs and runbooks.

> Detailed milestones tracked in GitHub Projects.

---

## License

Apache‑2.0. See `LICENSE`.

---

## Security Policy

Report security issues to **[security@idealeeu.eu](mailto:security@idealeeu.eu)**. Do not file public issues. See `SECURITY.md`.

---

## Support

Questions: open a GitHub Discussion or an issue using the template.

---

## Extended materials (full reference)

### Features and demos

* **Digital Passport Dashboard**: Interactive web app for browsing and managing aerospace component digital passports. *Demo URL placeholder; see docs.*
* **9‑Phase CAx Lifecycle**: CAD→CAE→CAM→CAI→CAV→CAP→CAS→CMP with “to‑scale” methodology.
* **PLUMA Automation**: Product Lifecycle UiX Management Automation.
* **Federated Learning**: Privacy‑preserving fleet‑wide intelligence.
* **H₂ Systems Support** and energy‑harvesting for long‑life sensors.

### Documentation links

* Digital Passport Dashboard → `/docs/digital-passport/`
* Quick Start Guide → `/docs/quick-start/`
* TFA Domains Reference → `/docs/tfa/domains.md`
* CAx Lifecycle Overview → `/docs/cax-lifecycle/`
* API Reference → `/docs/api/`

---

### TFA Canonical Domains

| Code | Domain                               | Focus                            |
| ---- | ------------------------------------ | -------------------------------- |
| AAA  | Airframes‑Aerodynamics‑Airworthiness | Structure, aero, certification   |
| AAP  | Airport‑Adaptable‑Platforms          | Ground ops, GSE                  |
| CCC  | Cockpit‑Cabin‑Cargo                  | Flight deck, passenger, freight  |
| CQH  | Cryogenics‑Quantum‑H2                | H₂ systems, quantum tech         |
| DDD  | Drainage‑Dehumidification‑Drying     | Moisture control                 |
| EDI  | Electronics‑Digital‑Instruments      | Avionics, sensors                |
| EEE  | Electrical‑Endocircular‑Energization | Power, energy harvesting         |
| EER  | Environmental‑Emissions‑Remediation  | Fire, pollution, sustainability  |
| IIF  | Industrial‑Infrastructure‑Facilities | Manufacturing, tooling           |
| IIS  | Information‑Intelligence‑Systems     | Software, AI, cybersecurity      |
| LCC  | Linkages‑Control‑Communications      | Flight controls, datalinks       |
| LIB  | Logistics‑Inventory‑Blockchain       | Supply chain, evidence anchoring |
| MMM  | Mechanical‑Material‑Modules          | Materials, mechanical, MRO       |
| OOO  | Operations‑Optimization‑Outcomes     | Fleet ops, analytics             |
| PPP  | Propulsion‑Power‑Plants              | Engines, thrust, fuel            |

---

### QPLC: Human‑Governed AI Framework

**Core principles**

* Human sovereignty. Ethics engine enforces human‑first rules.
* Safety‑bounded: quantum outputs validated against certified classical controllers.
* Full traceability to UTCS manifests. Federated ethics learning.

**Key components**

| Component           | Description                  | Location                                                                |
| ------------------- | ---------------------------- | ----------------------------------------------------------------------- |
| QPLC Definition     | Framework spec               | `/00-PROGRAM/GOVERNANCE/QPLC_DEFINITION.md`                             |
| EPE Rules           | Ethical Policy Engine schema | `/00-PROGRAM/GOVERNANCE/MAL-EEM/ETHICAL_POLICIES/EPE-v1.0.yaml`         |
| Human‑First Policy  | Ethical principles           | `/00-PROGRAM/GOVERNANCE/MAL-EEM/ETHICAL_POLICIES/HUMAN_FIRST_POLICY.md` |
| Human Review Portal | Interface spec               | `/00-PROGRAM/GOVERNANCE/QPLC_GOVERNANCE/HUMAN_REVIEW_PORTAL.md`         |
| PLUMA Integration   | Workflow orchestration       | `/00-PROGRAM/GOVERNANCE/QPLC_GOVERNANCE/PLUMA_INTEGRATION.md`           |

**EPE rules (excerpt)**

* HUM‑SAFE‑01 Safety > cost/schedule
* PRIVACY‑05 Data minimization
* TRANS‑06 Explainability for human‑impact decisions
* AUTON‑09 Human oversight for critical decisions

**Example implementations**: AGI‑QPLC‑CTRL (IIS), PROP‑QPLC (PPP), PWR‑QPLC (EEE), H2‑QPLC (CQH).

**Compliance refs**: DO‑178C, EU AI Act (high‑risk), ISO/IEC 24027, CS‑25.1309.

---

### Program folders

* **/00-PROGRAM/** Governance, CM, QMS, standards, supply chain

  * **/00-PROGRAM/BUSINESS/AAMMPP/** Aerospace Assets Mgmt, Maintenance & Procurement (canonical)
* **/01-FLEET/** Operational data hub, MRO, federated learning
* **/02‑AIRCRAFT/** AIR‑T baselines, domain integration, twin
* **/03‑SPACECRAFT/** STA baselines, domain integration, AIT/mission
* **/04‑SATELLITES/** Satellite product structures
* **/05‑TELESCOPES/** Observatory payload/domain structures
* **/06‑PROBES/** Deep‑space probes
* **/07‑DRONES/** UAS/UAM product lines
* **/08‑LAUNCHERS/** Launch vehicles
* **/09‑STM‑SPACE‑STATION‑MODULES/** Station modules/segments
* **/10‑BUSINESS/** Market, partnerships, finance

  * **/10‑BUSINESS/A360‑EXCHANGES‑TT/** Commercial layer on AAMMPP

**Core patterns**

```
DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT>/MODELS/<MODEL>/VERSION/<Qn>/SYSTEMS/…
```

Example

```
/02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/
  MODELS/BWB-H2-Hy-E/VERSION/Q100/
```

**ESG and Green Performant Tools (GPT)**

```
/00-PROGRAM/COMPLIANCE/12-ESG_SUSTAINABILITY/
  ├── 01-ESG_FRAMEWORK/
  ├── 02-GREEN_PERFORMANT_TOOLS/
  ├── 03-KEY_INDICATORS/
  ├── 04-TRANSFORMATION_VALUE/
  ├── 05-REPORTING/
  └── 06-CERTIFICATIONS/
```

---

### Repository Index and Navigation

**Purpose**: Navigate top‑level folders for governance, product structures, digital threads, and ops data.

**Top‑Level Directories**

* [/00‑PROGRAM](./00-PROGRAM/) · [/01‑FLEET](./01-FLEET/) · [/02‑AIRCRAFT](./02-AIRCRAFT/) · [/03‑SPACECRAFT](./03-SPACECRAFT/)
* [/04‑SATELLITES](./04-SATELLITES/) · [/05‑TELESCOPES](./05-TELESCOPES/) · [/06‑PROBES](./06-PROBES/)
* [/07‑DRONES](./07-DRONES/) · [/08‑LAUNCHERS](./08-LAUNCHERS/) · [/09‑STM‑SPACE‑STATION‑MODULES](./09-STM-SPACE-STATION-MODULES/) · [/10‑BUSINESS](./10-BUSINESS/)

**Key reference points**

* Governance & Policy: [`/00-PROGRAM/GOVERNANCE/`](./00-PROGRAM/GOVERNANCE/) · Config Mgmt: [`/00-PROGRAM/CONFIG_MGMT/`](./00-PROGRAM/CONFIG_MGMT/)
* Changes: ECR/ECO/CCB → see `06-CHANGES/` and `05-CCB/`
* Digital Thread: MBSE → `/00-PROGRAM/DIGITAL_THREAD/04-MBSE/` · Digital Twin → `/00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/`
* Traceability: UTCS Registry → `/00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`

**Index types**

* Master repo index (this block), domain indices under each subsystem, UTCS index under `.../UTCS/INDEX/`.

**Navigation pattern**

```
DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT>/MODELS/<MODEL>/VERSION/<Qn>/DOMAINS/<DOMAIN>/SYSTEMS/<SYSTEM>/SUBSYSTEMS/<SUBSYSTEM>/PLM/CAx/
```

**Maintenance**

* Automated updates with structure changes; manual review quarterly; baseline snapshots at milestones.


## Detailed Directory Index

---

## 00-PROGRAM
- [COMPLIANCE](./00-PROGRAM/COMPLIANCE/)
- [CONFIG_MGMT](./00-PROGRAM/CONFIG_MGMT/)
  - [04-BASELINES](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/)
    - [CDR](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/CDR/)
    - [COMMON](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/COMMON/) · [CHECKLISTS](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/COMMON/CHECKLISTS/) · [TEMPLATES](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/COMMON/TEMPLATES/)
    - [FRR](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/FRR/)
    - [MCR](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/MCR/)
    - [ORR_EIS](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/ORR_EIS/)
    - [PDR](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/PDR/)
    - [PRR](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/PRR/)
    - [SRR](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/SRR/)
    - [TRR](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/TRR/)
  - [05-CCB](./00-PROGRAM/CONFIG_MGMT/05-CCB/) · [02-MINUTES](./00-PROGRAM/CONFIG_MGMT/05-CCB/02-MINUTES/)
  - [06-CHANGES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
    - [01-POLICY](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/01-POLICY/)
    - [02-WORKFLOW](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/02-WORKFLOW/)
    - [03-REGISTERS](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/03-REGISTERS/)
    - [04-TEMPLATES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/04-TEMPLATES/) · [CHECKLISTS](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/04-TEMPLATES/CHECKLISTS/)
    - [05-ECR](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/) · [ACTIVE](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/ACTIVE/) · [CLOSED](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/CLOSED/) · [INBOX](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/INBOX/)
    - [06-ECO](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/06-ECO/) · [ACTIVE](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/06-ECO/ACTIVE/) · [CLOSED](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/06-ECO/CLOSED/)
    - [07-DEVIATIONS](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/07-DEVIATIONS/) · [OPEN](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/07-DEVIATIONS/OPEN/) · [CLOSED](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/07-DEVIATIONS/CLOSED/)
    - [08-WAIVERS](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/08-WAIVERS/) · [OPEN](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/08-WAIVERS/OPEN/) · [CLOSED](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/08-WAIVERS/CLOSED/)
    - [09-MRB](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/09-MRB/) · [DECISIONS](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/09-MRB/DECISIONS/)
    - [10-IMPACTS](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/10-IMPACTS/) · [CERTIFICATION](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/10-IMPACTS/CERTIFICATION/) · [COST_SCHEDULE](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/10-IMPACTS/COST_SCHEDULE/) · [INTERFACES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/10-IMPACTS/INTERFACES/) · [SAFETY](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/10-IMPACTS/SAFETY/) · [SUPPLY_CHAIN](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/10-IMPACTS/SUPPLY_CHAIN/)
    - [11-SOFTWARE_CHANGES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/11-SOFTWARE_CHANGES/)
    - [12-INTERFACE_CHANGES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/12-INTERFACE_CHANGES/)
    - [13-AUTOMATION](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/13-AUTOMATION/) · [SCRIPTS](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/13-AUTOMATION/SCRIPTS/)
    - [14-METRICS](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/14-METRICS/)
    - [15-AUDIT](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/15-AUDIT/) · [SNAPSHOTS](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/15-AUDIT/SNAPSHOTS/)
    - [16-CHANGE_PACKAGES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/16-CHANGE_PACKAGES/)
    - [17-NOTICES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/17-NOTICES/) · [CUSTOMER_NOTICES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/17-NOTICES/CUSTOMER_NOTICES/) · [REGULATORY_NOTICES](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/17-NOTICES/REGULATORY_NOTICES/)
  - [07-RELEASES](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/)
    - [01-POLICY](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/01-POLICY/) · [02-WORKFLOW](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/02-WORKFLOW/) · [03-REGISTERS](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/03-REGISTERS/) · [04-TEMPLATES](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/04-TEMPLATES/) · [05-AIRCRAFT](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/05-AIRCRAFT/) · [06-SPACECRAFT](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/06-SPACECRAFT/) · [07-COMMON](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/07-COMMON/) · [08-COMPLIANCE](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/08-COMPLIANCE/) · [09-DISTRIBUTION](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/09-DISTRIBUTION/) · [10-METRICS](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/10-METRICS/) · [11-ARCHIVE](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/11-ARCHIVE/) · [12-AUTOMATION](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/12-AUTOMATION/) · [SCRIPTS](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/12-AUTOMATION/SCRIPTS/)
  - [08-ITEM_MASTER](./00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/)
  - [09-INTERFACES](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
  - [10-TRACEABILITY](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/) · [UTCS](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/) · [INDEX](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/INDEX/) · [SCHEMAS](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/SCHEMAS/) · [UTCS_THREADS](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS_THREADS/)
  - [11-AUDITS](./00-PROGRAM/CONFIG_MGMT/11-AUDITS/)
  - [11-BADGES](./00-PROGRAM/CONFIG_MGMT/11-BADGES/) · [LOG](./00-PROGRAM/CONFIG_MGMT/11-BADGES/LOG/) · [TEMPLATES](./00-PROGRAM/CONFIG_MGMT/11-BADGES/TEMPLATES/)
  - [12-CI](./00-PROGRAM/CONFIG_MGMT/12-CI/) · [12-CI_CD_RULES](./00-PROGRAM/CONFIG_MGMT/12-CI_CD_RULES/)
  - [13-TEMPLATES](./00-PROGRAM/CONFIG_MGMT/13-TEMPLATES/)
- [DIGITAL_THREAD](./00-PROGRAM/DIGITAL_THREAD/)
  - [01-STRATEGY](./00-PROGRAM/DIGITAL_THREAD/01-STRATEGY/) · [02-STANDARDS](./00-PROGRAM/DIGITAL_THREAD/02-STANDARDS/) · [03-ARCHITECTURE](./00-PROGRAM/DIGITAL_THREAD/03-ARCHITECTURE/) · [DATA_FLOW_DIAGRAMS](./00-PROGRAM/DIGITAL_THREAD/03-ARCHITECTURE/DATA_FLOW_DIAGRAMS/)
  - [04-MBSE](./00-PROGRAM/DIGITAL_THREAD/04-MBSE/) · [INTERFACE_DEFINITIONS](./00-PROGRAM/DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/) · [MODEL_BASELINES](./00-PROGRAM/DIGITAL_THREAD/04-MBSE/MODEL_BASELINES/) · [SYSML_MODELS](./00-PROGRAM/DIGITAL_THREAD/04-MBSE/SYSML_MODELS/)
  - [05-DIGITAL_TWIN](./00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/) · [AIRCRAFT_TWIN](./00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/AIRCRAFT_TWIN/) · [SPACECRAFT_TWIN](./00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/SPACECRAFT_TWIN/) · [TWIN_VALIDATION](./00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/TWIN_VALIDATION/)
  - [06-DATA_MANAGEMENT](./00-PROGRAM/DIGITAL_THREAD/06-DATA_MANAGEMENT/) · [METADATA_REGISTRY](./00-PROGRAM/DIGITAL_THREAD/06-DATA_MANAGEMENT/METADATA_REGISTRY/)
  - [07-INTEGRATIONS](./00-PROGRAM/DIGITAL_THREAD/07-INTEGRATIONS/)
  - [08-AUTOMATION](./00-PROGRAM/DIGITAL_THREAD/08-AUTOMATION/)
  - [09-GOVERNANCE](./00-PROGRAM/DIGITAL_THREAD/09-GOVERNANCE/) · [10-METRICS](./00-PROGRAM/DIGITAL_THREAD/10-METRICS/)
- [GOVERNANCE](./00-PROGRAM/GOVERNANCE/) · [MAL-EEM](./00-PROGRAM/GOVERNANCE/MAL-EEM/) · [bias_fairness](./00-PROGRAM/GOVERNANCE/MAL-EEM/bias_fairness/) · [data_sheets](./00-PROGRAM/GOVERNANCE/MAL-EEM/data_sheets/) · [examples](./00-PROGRAM/GOVERNANCE/MAL-EEM/examples/) · [model_cards](./00-PROGRAM/GOVERNANCE/MAL-EEM/model_cards/) · [red_team](./00-PROGRAM/GOVERNANCE/MAL-EEM/red_team/) · [risk_assessments](./00-PROGRAM/GOVERNANCE/MAL-EEM/risk_assessments/) · [safety_case](./00-PROGRAM/GOVERNANCE/MAL-EEM/safety_case/) · [scriptbook](./00-PROGRAM/GOVERNANCE/MAL-EEM/scriptbook/)
- [INDUSTRIALISATION](./00-PROGRAM/INDUSTRIALISATION/)
- [QUALITY_QMS](./00-PROGRAM/QUALITY_QMS/)
- [REVIEW_BOARDS](./00-PROGRAM/REVIEW_BOARDS/) · [CCB](./00-PROGRAM/REVIEW_BOARDS/CCB/) · [DATA_PROTECTION](./00-PROGRAM/REVIEW_BOARDS/DATA_PROTECTION/) · [ETHICS](./00-PROGRAM/REVIEW_BOARDS/ETHICS/) · [SAFETY](./00-PROGRAM/REVIEW_BOARDS/SAFETY/)
- [SECURITY](./00-PROGRAM/SECURITY/)
- [STANDARDS](./00-PROGRAM/STANDARDS/) · [01-REGISTER](./00-PROGRAM/STANDARDS/01-REGISTER/) · [02-AIRCRAFT](./00-PROGRAM/STANDARDS/02-AIRCRAFT/) · [03-SPACECRAFT](./00-PROGRAM/STANDARDS/03-SPACECRAFT/) · [04-CROSS_CUTTING](./00-PROGRAM/STANDARDS/04-CROSS_CUTTING/) · [05-MAPPINGS](./00-PROGRAM/STANDARDS/05-MAPPINGS/) · [06-INTERPRETATIONS](./00-PROGRAM/STANDARDS/06-INTERPRETATIONS/) · [07-LINKS](./00-PROGRAM/STANDARDS/07-LINKS/)
- [SUPPLY_CHAIN](./00-PROGRAM/SUPPLY_CHAIN/)
- [TEMPLATES](./00-PROGRAM/TEMPLATES/) · [DPIA](./00-PROGRAM/TEMPLATES/DPIA/) · [IEF](./00-PROGRAM/TEMPLATES/IEF/) · [MAL-EEM](./00-PROGRAM/TEMPLATES/MAL-EEM/) · [NCR_CAPA](./00-PROGRAM/TEMPLATES/NCR_CAPA/) · [SBOM_VEX](./00-PROGRAM/TEMPLATES/SBOM_VEX/)

---

## 01-FLEET
- [FEDERATED_LEARNING](./01-FLEET/FEDERATED_LEARNING/)
  - [01-ARCHITECTURE](./01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/) · [DATA_CONTRACTS](./01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/)
  - [02-ORCHESTRATION](./01-FLEET/FEDERATED_LEARNING/02-ORCHESTRATION/) · [JOB_SPECS](./01-FLEET/FEDERATED_LEARNING/02-ORCHESTRATION/JOB_SPECS/)
  - [03-CLIENTS](./01-FLEET/FEDERATED_LEARNING/03-CLIENTS/) · [AIRCRAFT_EDGE](./01-FLEET/FEDERATED_LEARNING/03-CLIENTS/AIRCRAFT_EDGE/) · [GROUND_STATIONS](./01-FLEET/FEDERATED_LEARNING/03-CLIENTS/GROUND_STATIONS/) · [SIM_RIGS](./01-FLEET/FEDERATED_LEARNING/03-CLIENTS/SIM_RIGS/)
  - [04-ALGORITHMS](./01-FLEET/FEDERATED_LEARNING/04-ALGORITHMS/) · [05-PRIVACY_SECURITY](./01-FLEET/FEDERATED_LEARNING/05-PRIVACY_SECURITY/) · [06-MODELS](./01-FLEET/FEDERATED_LEARNING/06-MODELS/) · [MODEL_CARDS](./01-FLEET/FEDERATED_LEARNING/06-MODELS/MODEL_CARDS/) · [SBOM](./01-FLEET/FEDERATED_LEARNING/06-MODELS/SBOM/) · [07-EXPERIMENTS](./01-FLEET/FEDERATED_LEARNING/07-EXPERIMENTS/) · [08-VALIDATION_VVP](./01-FLEET/FEDERATED_LEARNING/08-VALIDATION_VVP/) · [09-DEPLOYMENT](./01-FLEET/FEDERATED_LEARNING/09-DEPLOYMENT/) · [10-GOVERNANCE](./01-FLEET/FEDERATED_LEARNING/10-GOVERNANCE/) · [11-COMPLIANCE](./01-FLEET/FEDERATED_LEARNING/11-COMPLIANCE/) · [12-METRICS](./01-FLEET/FEDERATED_LEARNING/12-METRICS/) · [13-CI_CD](./01-FLEET/FEDERATED_LEARNING/13-CI_CD/) · [PIPELINES](./01-FLEET/FEDERATED_LEARNING/13-CI_CD/PIPELINES/) · [14-INTEGRATIONS](./01-FLEET/FEDERATED_LEARNING/14-INTEGRATIONS/) · [15-TEMPLATES](./01-FLEET/FEDERATED_LEARNING/15-TEMPLATES/) · [16-INCIDENT_RESPONSE](./01-FLEET/FEDERATED_LEARNING/16-INCIDENT_RESPONSE/) · [AUDIT_LOGS](./01-FLEET/FEDERATED_LEARNING/16-INCIDENT_RESPONSE/AUDIT_LOGS/) · [POSTMORTEMS](./01-FLEET/FEDERATED_LEARNING/16-INCIDENT_RESPONSE/POSTMORTEMS/)
- [FLEET_OPTIMISATION](./01-FLEET/FLEET_OPTIMISATION/)
- [MRO_STRATEGY](./01-FLEET/MRO_STRATEGY/)
- [OPERATIONAL_DATA_HUB](./01-FLEET/OPERATIONAL_DATA_HUB/)

---

### 02-AIRCRAFT · CONFIGURATION_BASE
- [00-COMMON](./02-AIRCRAFT/CONFIGURATION_BASE/00-COMMON/)
  · [SCHEMAS](./02-AIRCRAFT/CONFIGURATION_BASE/00-COMMON/SCHEMAS/)
  · [TEMPLATES](./02-AIRCRAFT/CONFIGURATION_BASE/00-COMMON/TEMPLATES/)
  · [UTCS_INDEX](./02-AIRCRAFT/CONFIGURATION_BASE/00-COMMON/UTCS_INDEX/)

- [ATA-05_TIME_LIMITS_MAINT_CHECKS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-05_TIME_LIMITS_MAINT_CHECKS/)
  · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-05_TIME_LIMITS_MAINT_CHECKS/BASELINE/)
  · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-05_TIME_LIMITS_MAINT_CHECKS/CHANGE_LOG/)
  · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-05_TIME_LIMITS_MAINT_CHECKS/HW_CONFIG/)
  · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-05_TIME_LIMITS_MAINT_CHECKS/ICD/)
  · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-05_TIME_LIMITS_MAINT_CHECKS/PARAMS/)
  · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-05_TIME_LIMITS_MAINT_CHECKS/SW_BASELINE/)
  · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-05_TIME_LIMITS_MAINT_CHECKS/VERIFICATION/)

- [ATA-06_DIMENSIONS_AREAS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-06_DIMENSIONS_AREAS/)
  · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-06_DIMENSIONS_AREAS/BASELINE/)
  · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-06_DIMENSIONS_AREAS/CHANGE_LOG/)
  · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-06_DIMENSIONS_AREAS/HW_CONFIG/)
  · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-06_DIMENSIONS_AREAS/ICD/)
  · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-06_DIMENSIONS_AREAS/PARAMS/)
  · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-06_DIMENSIONS_AREAS/SW_BASELINE/)
  · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-06_DIMENSIONS_AREAS/VERIFICATION/)

- [ATA-08_LEVELING_WEIGHING](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-08_LEVELING_WEIGHING/)
  · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-08_LEVELING_WEIGHING/BASELINE/)
  · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-08_LEVELING_WEIGHING/CHANGE_LOG/)
  · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-08_LEVELING_WEIGHING/HW_CONFIG/)
  · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-08_LEVELING_WEIGHING/ICD/)
  · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-08_LEVELING_WEIGHING/PARAMS/)
  · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-08_LEVELING_WEIGHING/SW_BASELINE/)
  · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-08_LEVELING_WEIGHING/VERIFICATION/)

- [ATA-11_PLACARDS_MARKINGS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-11_PLACARDS_MARKINGS/)
  · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-11_PLACARDS_MARKINGS/BASELINE/)
  · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-11_PLACARDS_MARKINGS/CHANGE_LOG/)
  · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-11_PLACARDS_MARKINGS/HW_CONFIG/)
  · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-11_PLACARDS_MARKINGS/ICD/)
  · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-11_PLACARDS_MARKINGS/PARAMS/)
  · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-11_PLACARDS_MARKINGS/SW_BASELINE/)
  · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-11_PLACARDS_MARKINGS/VERIFICATION/)

- [ATA-12_SERVICING](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-12_SERVICING/)
  · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-12_SERVICING/BASELINE/)
  · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-12_SERVICING/CHANGE_LOG/)
  · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-12_SERVICING/HW_CONFIG/)
  · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-12_SERVICING/ICD/)
  · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-12_SERVICING/PARAMS/)
  · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-12_SERVICING/SW_BASELINE/)
  · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-12_SERVICING/VERIFICATION/)

- [ATA-20_STANDARD_PRACTICES](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-20_STANDARD_PRACTICES/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-20_STANDARD_PRACTICES/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-20_STANDARD_PRACTICES/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-20_STANDARD_PRACTICES/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-20_STANDARD_PRACTICES/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-20_STANDARD_PRACTICES/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-20_STANDARD_PRACTICES/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-20_STANDARD_PRACTICES/VERIFICATION/)
- [ATA-21_AIR_CONDITIONING](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-21_AIR_CONDITIONING/VERIFICATION/)
- [ATA-22_AUTO_FLIGHT](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/VERIFICATION/)
- [ATA-23_COMMUNICATIONS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-23_COMMUNICATIONS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-23_COMMUNICATIONS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-23_COMMUNICATIONS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-23_COMMUNICATIONS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-23_COMMUNICATIONS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-23_COMMUNICATIONS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-23_COMMUNICATIONS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-23_COMMUNICATIONS/VERIFICATION/)
- [ATA-24_ELECTRICAL_POWER](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/VERIFICATION/)
- [ATA-25_EQUIPMENT_FURNISHINGS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/VERIFICATION/)
- [ATA-26_FIRE_PROTECTION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/VERIFICATION/)
- [ATA-27_FLIGHT_CONTROLS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/VERIFICATION/)
- [ATA-28_FUEL](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-28_FUEL/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-28_FUEL/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-28_FUEL/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-28_FUEL/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-28_FUEL/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-28_FUEL/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-28_FUEL/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-28_FUEL/VERIFICATION/)
- [ATA-29_HYDRAULIC_POWER](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-29_HYDRAULIC_POWER/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-29_HYDRAULIC_POWER/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-29_HYDRAULIC_POWER/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-29_HYDRAULIC_POWER/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-29_HYDRAULIC_POWER/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-29_HYDRAULIC_POWER/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-29_HYDRAULIC_POWER/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-29_HYDRAULIC_POWER/VERIFICATION/)
- [ATA-30_ICE_RAIN_PROTECTION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-30_ICE_RAIN_PROTECTION/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-30_ICE_RAIN_PROTECTION/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-30_ICE_RAIN_PROTECTION/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-30_ICE_RAIN_PROTECTION/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-30_ICE_RAIN_PROTECTION/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-30_ICE_RAIN_PROTECTION/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-30_ICE_RAIN_PROTECTION/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-30_ICE_RAIN_PROTECTION/VERIFICATION/)
- [ATA-31_INDICATING_RECORDING](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/VERIFICATION/)
- [ATA-32_LANDING_GEAR](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-32_LANDING_GEAR/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-32_LANDING_GEAR/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-32_LANDING_GEAR/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-32_LANDING_GEAR/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-32_LANDING_GEAR/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-32_LANDING_GEAR/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-32_LANDING_GEAR/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-32_LANDING_GEAR/VERIFICATION/)
- [ATA-33_LIGHTS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-33_LIGHTS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-33_LIGHTS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-33_LIGHTS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-33_LIGHTS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-33_LIGHTS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-33_LIGHTS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-33_LIGHTS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-33_LIGHTS/VERIFICATION/)
- [ATA-34_NAVIGATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-34_NAVIGATION/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-34_NAVIGATION/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-34_NAVIGATION/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-34_NAVIGATION/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-34_NAVIGATION/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-34_NAVIGATION/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-34_NAVIGATION/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-34_NAVIGATION/VERIFICATION/)
- [ATA-35_OXYGEN](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-35_OXYGEN/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-35_OXYGEN/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-35_OXYGEN/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-35_OXYGEN/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-35_OXYGEN/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-35_OXYGEN/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-35_OXYGEN/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-35_OXYGEN/VERIFICATION/)
- [ATA-36_PNEUMATIC](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-36_PNEUMATIC/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-36_PNEUMATIC/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-36_PNEUMATIC/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-36_PNEUMATIC/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-36_PNEUMATIC/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-36_PNEUMATIC/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-36_PNEUMATIC/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-36_PNEUMATIC/VERIFICATION/)
- [ATA-38_WATER_WASTE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-38_WATER_WASTE/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-38_WATER_WASTE/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-38_WATER_WASTE/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-38_WATER_WASTE/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-38_WATER_WASTE/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-38_WATER_WASTE/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-38_WATER_WASTE/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-38_WATER_WASTE/VERIFICATION/)
- [ATA-42_INTEGRATED_MODULAR_AVIONICS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/VERIFICATION/)
- [ATA-44_CABIN_SYSTEMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/VERIFICATION/)
- [ATA-45_CENTRAL_MAINTENANCE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-45_CENTRAL_MAINTENANCE/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-45_CENTRAL_MAINTENANCE/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-45_CENTRAL_MAINTENANCE/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-45_CENTRAL_MAINTENANCE/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-45_CENTRAL_MAINTENANCE/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-45_CENTRAL_MAINTENANCE/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-45_CENTRAL_MAINTENANCE/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-45_CENTRAL_MAINTENANCE/VERIFICATION/)
- [ATA-46_INFORMATION_SYSTEMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-46_INFORMATION_SYSTEMS/VERIFICATION/)
- [ATA-47_INERT_GAS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-47_INERT_GAS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-47_INERT_GAS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-47_INERT_GAS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-47_INERT_GAS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-47_INERT_GAS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-47_INERT_GAS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-47_INERT_GAS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-47_INERT_GAS/VERIFICATION/)
- [ATA-49_APU](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-49_APU/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-49_APU/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-49_APU/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-49_APU/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-49_APU/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-49_APU/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-49_APU/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-49_APU/VERIFICATION/)
- [ATA-50_CARGO_LOAD_SYSTEMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/VERIFICATION/)
- [ATA-51_STRUCTURES_GENERAL](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_STRUCTURES_GENERAL/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_STRUCTURES_GENERAL/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_STRUCTURES_GENERAL/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_STRUCTURES_GENERAL/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_STRUCTURES_GENERAL/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_STRUCTURES_GENERAL/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_STRUCTURES_GENERAL/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_STRUCTURES_GENERAL/VERIFICATION/)
- [ATA-52_DOORS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-52_DOORS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-52_DOORS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-52_DOORS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-52_DOORS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-52_DOORS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-52_DOORS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-52_DOORS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-52_DOORS/VERIFICATION/)
- [ATA-53_FUSELAGE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-53_FUSELAGE/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-53_FUSELAGE/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-53_FUSELAGE/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-53_FUSELAGE/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-53_FUSELAGE/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-53_FUSELAGE/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-53_FUSELAGE/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-53_FUSELAGE/VERIFICATION/)
- [ATA-54_NACELLES_PYLONS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-54_NACELLES_PYLONS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-54_NACELLES_PYLONS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-54_NACELLES_PYLONS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-54_NACELLES_PYLONS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-54_NACELLES_PYLONS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-54_NACELLES_PYLONS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-54_NACELLES_PYLONS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-54_NACELLES_PYLONS/VERIFICATION/)
- [ATA-55_STABILIZERS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-55_STABILIZERS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-55_STABILIZERS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-55_STABILIZERS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-55_STABILIZERS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-55_STABILIZERS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-55_STABILIZERS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-55_STABILIZERS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-55_STABILIZERS/VERIFICATION/)
- [ATA-56_WINDOWS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-56_WINDOWS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-56_WINDOWS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-56_WINDOWS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-56_WINDOWS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-56_WINDOWS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-56_WINDOWS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-56_WINDOWS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-56_WINDOWS/VERIFICATION/)
- [ATA-57_WINGS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-57_WINGS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-57_WINGS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-57_WINGS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-57_WINGS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-57_WINGS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-57_WINGS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-57_WINGS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-57_WINGS/VERIFICATION/)
- [ATA-70_POWERPLANT_PRACTICES](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-70_POWERPLANT_PRACTICES/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-70_POWERPLANT_PRACTICES/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-70_POWERPLANT_PRACTICES/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-70_POWERPLANT_PRACTICES/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-70_POWERPLANT_PRACTICES/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-70_POWERPLANT_PRACTICES/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-70_POWERPLANT_PRACTICES/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-70_POWERPLANT_PRACTICES/VERIFICATION/)
- [ATA-71_POWERPLANT](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-71_POWERPLANT/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-71_POWERPLANT/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-71_POWERPLANT/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-71_POWERPLANT/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-71_POWERPLANT/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-71_POWERPLANT/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-71_POWERPLANT/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-71_POWERPLANT/VERIFICATION/)
- [ATA-72_ENGINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-72_ENGINE/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-72_ENGINE/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-72_ENGINE/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-72_ENGINE/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-72_ENGINE/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-72_ENGINE/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-72_ENGINE/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-72_ENGINE/VERIFICATION/)
- [ATA-73_ENGINE_FUEL_CONTROL](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-73_ENGINE_FUEL_CONTROL/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-73_ENGINE_FUEL_CONTROL/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-73_ENGINE_FUEL_CONTROL/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-73_ENGINE_FUEL_CONTROL/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-73_ENGINE_FUEL_CONTROL/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-73_ENGINE_FUEL_CONTROL/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-73_ENGINE_FUEL_CONTROL/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-73_ENGINE_FUEL_CONTROL/VERIFICATION/)
- [ATA-74_IGNITION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-74_IGNITION/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-74_IGNITION/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-74_IGNITION/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-74_IGNITION/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-74_IGNITION/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-74_IGNITION/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-74_IGNITION/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-74_IGNITION/VERIFICATION/)
- [ATA-75_BLEED_AIR](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-75_BLEED_AIR/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-75_BLEED_AIR/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-75_BLEED_AIR/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-75_BLEED_AIR/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-75_BLEED_AIR/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-75_BLEED_AIR/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-75_BLEED_AIR/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-75_BLEED_AIR/VERIFICATION/)
- [ATA-76_ENGINE_CONTROLS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-76_ENGINE_CONTROLS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-76_ENGINE_CONTROLS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-76_ENGINE_CONTROLS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-76_ENGINE_CONTROLS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-76_ENGINE_CONTROLS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-76_ENGINE_CONTROLS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-76_ENGINE_CONTROLS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-76_ENGINE_CONTROLS/VERIFICATION/)
- [ATA-77_ENGINE_INDICATING](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-77_ENGINE_INDICATING/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-77_ENGINE_INDICATING/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-77_ENGINE_INDICATING/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-77_ENGINE_INDICATING/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-77_ENGINE_INDICATING/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-77_ENGINE_INDICATING/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-77_ENGINE_INDICATING/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-77_ENGINE_INDICATING/VERIFICATION/)
- [ATA-78_EXHAUST](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-78_EXHAUST/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-78_EXHAUST/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-78_EXHAUST/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-78_EXHAUST/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-78_EXHAUST/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-78_EXHAUST/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-78_EXHAUST/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-78_EXHAUST/VERIFICATION/)
- [ATA-79_OIL](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-79_OIL/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-79_OIL/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-79_OIL/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-79_OIL/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-79_OIL/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-79_OIL/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-79_OIL/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-79_OIL/VERIFICATION/)
- [ATA-80_STARTING](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-80_STARTING/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-80_STARTING/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-80_STARTING/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-80_STARTING/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-80_STARTING/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-80_STARTING/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-80_STARTING/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-80_STARTING/VERIFICATION/)
- [ATA-92_EWIS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/) · [BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/BASELINE/) · [CHANGE_LOG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/CHANGE_LOG/) · [HW_CONFIG](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/HW_CONFIG/) · [ICD](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/ICD/) · [PARAMS](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/PARAMS/) · [SW_BASELINE](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/SW_BASELINE/) · [VERIFICATION](./02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/VERIFICATION/)

---

### 02-AIRCRAFT · CROSS_SYSTEM_INTEGRATION
- [01-ARCHITECTURE_END2END](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/01-ARCHITECTURE_END2END/)
  · [FUNCTIONAL_CHAINS](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/01-ARCHITECTURE_END2END/FUNCTIONAL_CHAINS/)
  · [INTERFACE_MATRIX](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/01-ARCHITECTURE_END2END/INTERFACE_MATRIX/)
  · [SYSTEM_CONTEXT](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/01-ARCHITECTURE_END2END/SYSTEM_CONTEXT/)
- [02-NETWORKS_DATA_BUS](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/02-NETWORKS_DATA_BUS/)
  · [LOGICAL](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/02-NETWORKS_DATA_BUS/LOGICAL/)
  · [PHYSICAL](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/02-NETWORKS_DATA_BUS/PHYSICAL/)
  · [QOS_TIMING](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/02-NETWORKS_DATA_BUS/QOS_TIMING/)
- [03-TIME_SYNCHRONISATION](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/03-TIME_SYNCHRONISATION/)
- [04-POWER_THERMAL_CROSSLOAD](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/04-POWER_THERMAL_CROSSLOAD/)
- [05-IMA_INTEGRATION](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/05-IMA_INTEGRATION/)
  · [SCHEDULE_TABLES](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/05-IMA_INTEGRATION/SCHEDULE_TABLES/)
- [06-SOFTWARE_INTEGRATION](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/06-SOFTWARE_INTEGRATION/)
- [07-INTEGRATION_TEST](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/07-INTEGRATION_TEST/)
- [08-SAFETY_SECURITY](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/08-SAFETY_SECURITY/)
- [09-CONFIG_BASELINES_HANDOFF](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/09-CONFIG_BASELINES_HANDOFF/)
  · [INTEGRATION_BASELINES](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/09-CONFIG_BASELINES_HANDOFF/INTEGRATION_BASELINES/)
  · [IBL-2025-Q3](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/09-CONFIG_BASELINES_HANDOFF/INTEGRATION_BASELINES/IBL-2025-Q3/)
  · [LINKS_TO_ATA](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/09-CONFIG_BASELINES_HANDOFF/LINKS_TO_ATA/)
- [10-ICD_LINKS](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/10-ICD_LINKS/)
- [11-MODELS_SIMULATION](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/11-MODELS_SIMULATION/)
- [12-OPERATIONS_FLEET_FEEDBACK](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/12-OPERATIONS_FLEET_FEEDBACK/)
- [13-DATA](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/13-DATA/) · [SCHEMAS](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/13-DATA/SCHEMAS/)
- [14-METRICS](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/14-METRICS/)
- [15-AUTOMATION](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/15-AUTOMATION/) · [SCRIPTS](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/15-AUTOMATION/SCRIPTS/)
- [16-COMPLIANCE](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/16-COMPLIANCE/) · [AUDIT_CHECKLISTS](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/16-COMPLIANCE/AUDIT_CHECKLISTS/)
- [17-LINKS](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/17-LINKS/)

---

### 02-AIRCRAFT · DIGITAL_TWIN_MODEL
- [01-ARCHITECTURE](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/)
  · [analysis](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/analysis/)
  · [notebooks](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/analysis/notebooks/)
  · [scripts](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/analysis/scripts/)
  · [api](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/api/)
  · [grpc](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/api/grpc/)
  · [rest](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/api/rest/)
  · [ci](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/ci/)
  · [compliance](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/compliance/) · [IEF](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/compliance/IEF/)
  · [configuration](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/configuration/) · [calibration](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/configuration/calibration/)
  · [coords](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/coords/) · [transforms](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/coords/transforms/)
  · [data_contracts](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/data_contracts/) · [api](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/data_contracts/api/) · [schemas](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/data_contracts/schemas/)
  · [execution](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/execution/) · [docker](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/execution/docker/) · [orchestration](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/execution/orchestration/)
  · [interfaces](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/interfaces/) · [dds](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/interfaces/dds/) · [idl](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/interfaces/dds/idl/) · [icd](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/interfaces/icd/) · [ros2](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/interfaces/ros2/) · [msg](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/interfaces/ros2/msg/)
  · [kpis](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/kpis/)
  · [mapping](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/mapping/)
  · [models](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/models/) · [fmu](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/models/fmu/) · [modelica](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/models/modelica/) · [simulink](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/models/simulink/)
  · [ontologies](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/ontologies/)
  · [packaging](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/packaging/) · [sbom](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/packaging/sbom/)
  · [requirements](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/requirements/)
  · [security](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/security/)
  · [validation](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/validation/) · [reports](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/01-ARCHITECTURE/validation/reports/)
- [02-MODELS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/)
  · [BEHAVIORAL](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/BEHAVIORAL/) · [CONTROL_LOGIC](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/BEHAVIORAL/CONTROL_LOGIC/) · [STATE_MACHINES](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/BEHAVIORAL/STATE_MACHINES/)
  · [CO_SIMULATION](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/CO_SIMULATION/) · [FMU_FMI](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/CO_SIMULATION/FMU_FMI/)
  · [DATA_DRIVEN](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/DATA_DRIVEN/) · [ANOMALY_DETECTORS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/DATA_DRIVEN/ANOMALY_DETECTORS/) · [ONNX_MODELS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/DATA_DRIVEN/ONNX_MODELS/) · [SURROGATES](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/DATA_DRIVEN/SURROGATES/)
  · [PHYSICS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/PHYSICS/) · [AERODYNAMICS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/PHYSICS/AERODYNAMICS/) · [ENERGY_H2](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/PHYSICS/ENERGY_H2/) · [ENVIRONMENT](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/PHYSICS/ENVIRONMENT/) · [PROPULSION](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/PHYSICS/PROPULSION/) · [STRUCTURES](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/PHYSICS/STRUCTURES/) · [THERMAL](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/02-MODELS/PHYSICS/THERMAL/)
- [03-INTERFACES_APIS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/03-INTERFACES_APIS/)
  · [STREAMS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/03-INTERFACES_APIS/STREAMS/) · [INPUTS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/03-INTERFACES_APIS/STREAMS/INPUTS/) · [OUTPUTS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/03-INTERFACES_APIS/STREAMS/OUTPUTS/)
- [04-VERSIONING_CONFIG](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/04-VERSIONING_CONFIG/)
  · [PARAMETER_SETS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/04-VERSIONING_CONFIG/PARAMETER_SETS/) · [BASELINE](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/04-VERSIONING_CONFIG/PARAMETER_SETS/BASELINE/) · [VARIANTS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/04-VERSIONING_CONFIG/PARAMETER_SETS/VARIANTS/)
  · [SERIALIZED_INSTANCES](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/04-VERSIONING_CONFIG/SERIALIZED_INSTANCES/)
- [05-CALIBRATION_ALIGNMENT](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/05-CALIBRATION_ALIGNMENT/)
  · [ALIGNMENT_REPORTS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/05-CALIBRATION_ALIGNMENT/ALIGNMENT_REPORTS/)
  · [DATASETS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/05-CALIBRATION_ALIGNMENT/DATASETS/) · [FLIGHT_TEST](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/05-CALIBRATION_ALIGNMENT/DATASETS/FLIGHT_TEST/) · [GROUND_TEST](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/05-CALIBRATION_ALIGNMENT/DATASETS/GROUND_TEST/) · [LAB_RIG](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/05-CALIBRATION_ALIGNMENT/DATASETS/LAB_RIG/)
- [06-VALIDATION_VERIFICATION](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/06-VALIDATION_VERIFICATION/)
  · [RESULTS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/06-VALIDATION_VERIFICATION/RESULTS/)
  · [TEST_CASES](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/06-VALIDATION_VERIFICATION/TEST_CASES/)
- [07-RUNTIME_DEPLOYMENT](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/07-RUNTIME_DEPLOYMENT/)
  · [RUNTIME_PROFILES](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/07-RUNTIME_DEPLOYMENT/RUNTIME_PROFILES/) · [EDGE](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/07-RUNTIME_DEPLOYMENT/RUNTIME_PROFILES/EDGE/) · [GROUND](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/07-RUNTIME_DEPLOYMENT/RUNTIME_PROFILES/GROUND/)
- [08-SYNCHRONISATION](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/08-SYNCHRONISATION/)
- [09-INTEGRATIONS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/09-INTEGRATIONS/)
- [10-METRICS](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/10-METRICS/)
- [11-SAFETY_COMPLIANCE](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/11-SAFETY_COMPLIANCE/) · [ASSURANCE_CASE](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/11-SAFETY_COMPLIANCE/ASSURANCE_CASE/)
- [12-CODE](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/12-CODE/) · [CI_CD](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/12-CODE/CI_CD/) · [INFERENCE_RUNTIME](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/12-CODE/INFERENCE_RUNTIME/) · [PACKAGING](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/12-CODE/PACKAGING/)
- [13-TEMPLATES](./02-AIRCRAFT/DIGITAL_TWIN_MODEL/13-TEMPLATES/)

### 02-AIRCRAFT › [MODEL_IDENTIFICATION](./02-AIRCRAFT/MODEL_IDENTIFICATION/)
- [AMPEL360-AIR-T](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/)
  - [ARCH](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/)
    - [BWB-H2-Hy-E](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/)
      - [FAMILY](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/)
        - [Q100_STD01](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/)
          - [00-CONFIG](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/00-CONFIG/)
            - [CONFIG_SETS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/00-CONFIG/CONFIG_SETS/)
            - [SCHEMAS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/00-CONFIG/SCHEMAS/)
          - [01-EFFECTIVITY](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/01-EFFECTIVITY/)
            - [BLOCKS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/01-EFFECTIVITY/BLOCKS/)
            - [MODS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/01-EFFECTIVITY/MODS/)
          - [02-RELEASE_TAGS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/02-RELEASE_TAGS/)
          - [03-TRACEABILITY](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/03-TRACEABILITY/)
          - [04-ICD_LINKS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/04-ICD_LINKS/)
          - [DOMAIN](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/)
            - **AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/)
                - [06-DIMENSIONS-STATIONS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/)
                  - [INTERFACE_MATRIX](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/INTERFACE_MATRIX/)
                  - [SUBSYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/SUBSYSTEMS/)
                    - [06-00_GENERAL › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-00_GENERAL/PLM/CAx/)
                    - [06-20_FUSELAGE_STATIONS_FS › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-20_FUSELAGE_STATIONS_FS/PLM/CAx/)
                    - [06-30_WATERLINES_WL › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-30_WATERLINES_WL/PLM/CAx/)
                    - [06-40_BUTTOCK_LINES_BL › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-40_BUTTOCK_LINES_BL/PLM/CAx/)
                    - [06-50_WING_STATIONS_WS › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-50_WING_STATIONS_WS/PLM/CAx/)
                    - [06-60_LDG_GEAR_REF_POINTS › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-60_LDG_GEAR_REF_POINTS/PLM/CAx/)
                    - [06-90_TOOLS_FIXTURES_GSE › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-90_TOOLS_FIXTURES_GSE/PLM/CAx/)
                - [51-STRUCTURES-GENERAL](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/51-STRUCTURES-GENERAL/)
                  - [INTERFACE_MATRIX](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/51-STRUCTURES-GENERAL/INTERFACE_MATRIX/)
                  - [SUBSYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/51-STRUCTURES-GENERAL/SUBSYSTEMS/)
                    - [51-00_GENERAL › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/PLM/CAx/)
            - **AAP-AIRPORT-ADAPTABLE-PLATFORMS**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAP-AIRPORT-ADAPTABLE-PLATFORMS/SYSTEMS/)
                - [10-PARKING.MOORING](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAP-AIRPORT-ADAPTABLE-PLATFORMS/SYSTEMS/10-PARKING.MOORING/)
                  - [INTERFACE_MATRIX](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAP-AIRPORT-ADAPTABLE-PLATFORMS/SYSTEMS/10-PARKING.MOORING/INTERFACE_MATRIX/)
                  - [SUBSYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAP-AIRPORT-ADAPTABLE-PLATFORMS/SYSTEMS/10-PARKING.MOORING/SUBSYSTEMS/)
                    - [10-10_MOORING_ANCHORS › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAP-AIRPORT-ADAPTABLE-PLATFORMS/SYSTEMS/10-PARKING.MOORING/SUBSYSTEMS/10-10_MOORING_ANCHORS/PLM/CAx/)
            - **CCC-COCKPIT-CABIN-CARGO**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/CCC-COCKPIT-CABIN-CARGO/SYSTEMS/)
                - [25-EQUIPMENT_FURNISHINGS › SUBSYSTEMS › 25-10_SEATS_PASSENGER › PLM](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/CCC-COCKPIT-CABIN-CARGO/SYSTEMS/25-EQUIPMENT_FURNISHINGS/SUBSYSTEMS/25-10_SEATS_PASSENGER/PLM/)
            - **CQH-CRYOGENICS-QUANTUM-H2**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/CQH-CRYOGENICS-QUANTUM-H2/SYSTEMS/)
                - [47-20_LH2_AUX_THERMAL_CONDITIONING › SUBSYSTEMS › 47-21_SUBCOOLER_COLD_BOX › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/CQH-CRYOGENICS-QUANTUM-H2/SYSTEMS/47-20_LH2_AUX_THERMAL_CONDITIONING/SUBSYSTEMS/47-21_SUBCOOLER_COLD_BOX/PLM/CAx/)
            - **DDD-DRAINAGE-DEHUMIDIFICATION-DRYING**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/DDD-DRAINAGE-DEHUMIDIFICATION-DRYING/SYSTEMS/)
                - [21-DEHUMIDIFICATION_ECS › SUBSYSTEMS › 21-10_AIR_DRYERS_DESICCANT_PACKS › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/DDD-DRAINAGE-DEHUMIDIFICATION-DRYING/SYSTEMS/21-DEHUMIDIFICATION_ECS/SUBSYSTEMS/21-10_AIR_DRYERS_DESICCANT_PACKS/PLM/CAx/)
            - **EDI-ELECTRONICS-DIGITAL-INSTRUMENTS**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EDI-ELECTRONICS-DIGITAL-INSTRUMENTS/SYSTEMS/)
                - [31-INDICATING_RECORDING › SUBSYSTEMS › 31-30_RECORDERS_FDR_CVR › PLM](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EDI-ELECTRONICS-DIGITAL-INSTRUMENTS/SYSTEMS/31-INDICATING_RECORDING/SUBSYSTEMS/31-30_RECORDERS_FDR_CVR/PLM/)
            - **EEE-ELECTRICAL-ENDOCIRCULAR-ENERGIZATION**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EEE-ELECTRICAL-ENDOCIRCULAR-ENERGIZATION/SYSTEMS/)
                - [24-ELECTRICAL-POWER](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EEE-ELECTRICAL-ENDOCIRCULAR-ENERGIZATION/SYSTEMS/24-ELECTRICAL-POWER/)
                  - [INTEGRATION_VIEW.md](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EEE-ELECTRICAL-ENDOCIRCULAR-ENERGIZATION/SYSTEMS/24-ELECTRICAL-POWER/INTEGRATION_VIEW.md)
                  - [INTERFACE_MATRIX](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EEE-ELECTRICAL-ENDOCIRCULAR-ENERGIZATION/SYSTEMS/24-ELECTRICAL-POWER/INTERFACE_MATRIX/)
                  - [SUBSYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EEE-ELECTRICAL-ENDOCIRCULAR-ENERGIZATION/SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/)
                    - [24-00_STANDARDS_GENERAL › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EEE-ELECTRICAL-ENDOCIRCULAR-ENERGIZATION/SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-00_STANDARDS_GENERAL/PLM/CAx/)
            - **EER-ENVIRONMENTAL-EMISSIONS-REMEDIATION**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EER-ENVIRONMENTAL-EMISSIONS-REMEDIATION/SYSTEMS/)
                - [26-FIRE_PROTECTION › SUBSYSTEMS › 26-20_SUPPRESSION_BOTTLES_LINES › PLM](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EER-ENVIRONMENTAL-EMISSIONS-REMEDIATION/SYSTEMS/26-FIRE_PROTECTION/SUBSYSTEMS/26-20_SUPPRESSION_BOTTLES_LINES/PLM/)
            - **IIF-INDUSTRIAL-INFRASTRUCTURE-FACILITIES**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/IIF-INDUSTRIAL-INFRASTRUCTURE-FACILITIES/SYSTEMS/)
                - [07-LIFTING-SHORING › SUBSYSTEMS › 07-10_AIRCRAFT_TRIPOD_JACKS › PLM](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/IIF-INDUSTRIAL-INFRASTRUCTURE-FACILITIES/SYSTEMS/07-LIFTING-SHORING/SUBSYSTEMS/07-10_AIRCRAFT_TRIPOD_JACKS/PLM/)
            - **IIS-INFORMATION-INTELLIGENCE-SYSTEMS**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/IIS-INFORMATION-INTELLIGENCE-SYSTEMS/SYSTEMS/)
                - [46-INFORMATION-SYSTEMS › SUBSYSTEMS › 46-10_NETWORK › PLM](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/IIS-INFORMATION-INTELLIGENCE-SYSTEMS/SYSTEMS/46-INFORMATION-SYSTEMS/SUBSYSTEMS/46-10_NETWORK/PLM/)
            - **LCC-LINKAGES-CONTROL-COMMUNICATIONS**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/LCC-LINKAGES-CONTROL-COMMUNICATIONS/SYSTEMS/)
                - [22-AUTO_FLIGHT › SUBSYSTEMS › 22-10_AFCS_FLIGHT_CONTROL_COMPUTERS › PLM](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/LCC-LINKAGES-CONTROL-COMMUNICATIONS/SYSTEMS/22-AUTO_FLIGHT/SUBSYSTEMS/22-10_AFCS_FLIGHT_CONTROL_COMPUTERS/PLM/)
            - **LIB-LOGISTICS-INVENTORY-BLOCKCHAIN**
              - [SYSTEMS](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/LIB-LOGISTICS-INVENTORY-BLOCKCHAIN/SYSTEMS/)
                - [01-INTRODUCTION › SUBSYSTEMS › 01-00_STANDARDS_GENERAL › PLM › CAx](./02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/LIB-LOGISTICS-INVENTORY-BLOCKCHAIN/SYSTEMS/01-INTRODUCTION/SUBSYSTEMS/01-00_STANDARDS_GENERAL/PLM/CAx/)

              
* [03-SPACECRAFT](./03-SPACECRAFT)
  * [DOMAIN_INTEGRATION](./03-SPACECRAFT/DOMAIN_INTEGRATION)
    * [PRODUCTS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS)
      * [AMPEL360-SPACE-T](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T)
        * [MODELS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS)
          * [PLUS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS)
            * [VERSION](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION)
              * [Q10](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10)
                * [DOMAINS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS)
                  * [STA-A-STRUCTURES-MECHANISMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS)
                      * [06_DIMENSIONS_ALIGNMENTS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/06_DIMENSIONS_ALIGNMENTS)
                      * [50_PAYLOAD_STRUCTURES](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/50_PAYLOAD_STRUCTURES)
                      * [51_PRIMARY_STRUCTURE](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/51_PRIMARY_STRUCTURE)
                      * [52_DOORS_HATCHES](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/52_DOORS_HATCHES)
                      * [53_STRUCTURAL_BODY](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/53_STRUCTURAL_BODY)
                      * [55_ADCS_STRUCTURES](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/55_ADCS_STRUCTURES)
                      * [56_WINDOWS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/56_WINDOWS)
                      * [57_SOLAR_ARRAYS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/57_SOLAR_ARRAYS)
                      * [66_MECHANISMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/66_MECHANISMS)
                      * [94_QUALIFICATION_ACCEPTANCE](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-A-STRUCTURES-MECHANISMS/SYSTEMS/94_QUALIFICATION_ACCEPTANCE)
                  * [STA-B-THERMAL-TPS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-B-THERMAL-TPS)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-B-THERMAL-TPS/SYSTEMS)
                      * [21-THERMAL_CONTROL](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-B-THERMAL-TPS/SYSTEMS/21-THERMAL_CONTROL)
                      * [30-ICE_DEW_PREVENTION](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-B-THERMAL-TPS/SYSTEMS/30-ICE_DEW_PREVENTION)
                  * [STA-C-POWER-EPS-HARNESS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-C-POWER-EPS-HARNESS)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-C-POWER-EPS-HARNESS/SYSTEMS)
                      * [24-ELECTRICAL_POWER](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-C-POWER-EPS-HARNESS/SYSTEMS/24-ELECTRICAL_POWER)
                      * [39-POWER_CONTROL_PANELS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-C-POWER-EPS-HARNESS/SYSTEMS/39-POWER_CONTROL_PANELS)
                      * [49-AUXILIARY_POWER](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-C-POWER-EPS-HARNESS/SYSTEMS/49-AUXILIARY_POWER)
                      * [97-HARNESS_EWIS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-C-POWER-EPS-HARNESS/SYSTEMS/97-HARNESS_EWIS)
                  * [STA-D-COMMUNICATIONS-TTANDC](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-D-COMMUNICATIONS-TTANDC)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-D-COMMUNICATIONS-TTANDC/SYSTEMS)
                      * [23-COMMUNICATIONS_RF_LINKS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-D-COMMUNICATIONS-TTANDC/SYSTEMS/23-COMMUNICATIONS_RF_LINKS)
                      * [33-TELEMETRY_TELECOMMAND](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-D-COMMUNICATIONS-TTANDC/SYSTEMS/33-TELEMETRY_TELECOMMAND)
                      * [48-ANTENNAS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-D-COMMUNICATIONS-TTANDC/SYSTEMS/48-ANTENNAS)
                  * [STA-E-NAVIGATION-TIME-DATA](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-E-NAVIGATION-TIME-DATA)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-E-NAVIGATION-TIME-DATA/SYSTEMS)
                      * [31_NAV_SENSORS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-E-NAVIGATION-TIME-DATA/SYSTEMS/31_NAV_SENSORS)
                      * [34_NAVIGATION_COMPUTATION](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-E-NAVIGATION-TIME-DATA/SYSTEMS/34_NAVIGATION_COMPUTATION)
                      * [41_TIME_SYNCHRONIZATION](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-E-NAVIGATION-TIME-DATA/SYSTEMS/41_TIME_SYNCHRONIZATION)
                  * [STA-F-AVIONICS-FSW-DATABUS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-F-AVIONICS-FSW-DATABUS)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-F-AVIONICS-FSW-DATABUS/SYSTEMS)
                      * [40-FLIGHT_SOFTWARE](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-F-AVIONICS-FSW-DATABUS/SYSTEMS/40-FLIGHT_SOFTWARE)
                      * [42-AVIONICS_COMPUTERS_IMA](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-F-AVIONICS-FSW-DATABUS/SYSTEMS/42-AVIONICS_COMPUTERS_IMA)
                      * [93-DATABUS_NETWORKS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-F-AVIONICS-FSW-DATABUS/SYSTEMS/93-DATABUS_NETWORKS)
                  * [STA-G-CONTROL-AUTONOMY-FDIR](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-G-CONTROL-AUTONOMY-FDIR)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-G-CONTROL-AUTONOMY-FDIR/SYSTEMS)
                      * [22-AUTONOMY_MODES](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-G-CONTROL-AUTONOMY-FDIR/SYSTEMS/22-AUTONOMY_MODES)
                      * [44-GNC_GUIDANCE_NAV_CONTROL](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-G-CONTROL-AUTONOMY-FDIR/SYSTEMS/44-GNC_GUIDANCE_NAV_CONTROL)
                      * [45-FDIR_FAULT_PROTECTION](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-G-CONTROL-AUTONOMY-FDIR/SYSTEMS/45-FDIR_FAULT_PROTECTION)
                  * [STA-H-ECLSS-CREW-PAYLOAD](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-H-ECLSS-CREW-PAYLOAD)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-H-ECLSS-CREW-PAYLOAD/SYSTEMS)
                      * [25_ECLSS_CABIN_ENVIRONMENT](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-H-ECLSS-CREW-PAYLOAD/SYSTEMS/25_ECLSS_CABIN_ENVIRONMENT)
                  * [STA-I-PROPULSION-FLUIDS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-I-PROPULSION-FLUIDS)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-I-PROPULSION-FLUIDS/SYSTEMS)
                      * [28-PROPELLANT_SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-I-PROPULSION-FLUIDS/SYSTEMS/28-PROPELLANT_SYSTEMS)
                      * [29-PNEUMATIC_HYDRAULIC_POWER](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-I-PROPULSION-FLUIDS/SYSTEMS/29-PNEUMATIC_HYDRAULIC_POWER)
                      * [54-PROPULSION_STRUCTURES](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-I-PROPULSION-FLUIDS/SYSTEMS/54-PROPULSION_STRUCTURES)
                      * [61-RCS_ATTITUDE_CONTROL](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-I-PROPULSION-FLUIDS/SYSTEMS/61-RCS_ATTITUDE_CONTROL)
                      * [72-PROPULSION_THRUST_DEVICES](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-I-PROPULSION-FLUIDS/SYSTEMS/72-PROPULSION_THRUST_DEVICES)
                      * [84-ELECTRIC_PROPULSION](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-I-PROPULSION-FLUIDS/SYSTEMS/84-ELECTRIC_PROPULSION)
                  * [STA-J-DOCKING-SAMPLING-ROBOTICS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-J-DOCKING-SAMPLING-ROBOTICS)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-J-DOCKING-SAMPLING-ROBOTICS/SYSTEMS)
                      * [58-DOCKING_SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-J-DOCKING-SAMPLING-ROBOTICS/SYSTEMS/58-DOCKING_SYSTEMS)
                      * [59-SAMPLING_ROBOTICS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-J-DOCKING-SAMPLING-ROBOTICS/SYSTEMS/59-SAMPLING_ROBOTICS)
                  * [STA-K-ENVIRONMENT-SAFETY-TRAFFIC](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-K-ENVIRONMENT-SAFETY-TRAFFIC)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-K-ENVIRONMENT-SAFETY-TRAFFIC/SYSTEMS)
                      * [15_ENVIRONMENT_CONTROL_MONITORING](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-K-ENVIRONMENT-SAFETY-TRAFFIC/SYSTEMS/15_ENVIRONMENT_CONTROL_MONITORING)
                      * [26_FIRE_SAFETY_ORDNANCE](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-K-ENVIRONMENT-SAFETY-TRAFFIC/SYSTEMS/26_FIRE_SAFETY_ORDNANCE)
                      * [86_PLANETARY_PROTECTION](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-K-ENVIRONMENT-SAFETY-TRAFFIC/SYSTEMS/86_PLANETARY_PROTECTION)
                      * [87_RADIATION_ENVIRONMENT](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-K-ENVIRONMENT-SAFETY-TRAFFIC/SYSTEMS/87_RADIATION_ENVIRONMENT)
                      * [90_SPACE_TRAFFIC_MANAGEMENT](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-K-ENVIRONMENT-SAFETY-TRAFFIC/SYSTEMS/90_SPACE_TRAFFIC_MANAGEMENT)
                  * [STA-L-GROUND-INTEGRATION-OPS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-L-GROUND-INTEGRATION-OPS)
                    * [SYSTEMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-L-GROUND-INTEGRATION-OPS/SYSTEMS)
                      * [07-GSE_HANDLING_LIFTING](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-L-GROUND-INTEGRATION-OPS/SYSTEMS/07-GSE_HANDLING_LIFTING)
                      * [10-EGSE_POWER_COMMS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-L-GROUND-INTEGRATION-OPS/SYSTEMS/10-EGSE_POWER_COMMS)
                      * [16-INTEGRATION_AND_TEST](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-L-GROUND-INTEGRATION-OPS/SYSTEMS/16-INTEGRATION_AND_TEST)
                      * [32-EDL_LANDING_OPERATIONS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-L-GROUND-INTEGRATION-OPS/SYSTEMS/32-EDL_LANDING_OPERATIONS)
                      * [46-GROUND_MOC_INTERFACE](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-L-GROUND-INTEGRATION-OPS/SYSTEMS/46-GROUND_MOC_INTERFACE)
                      * [92-CALIBRATION_DATA_ARCHIVAL](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-L-GROUND-INTEGRATION-OPS/SYSTEMS/92-CALIBRATION_DATA_ARCHIVAL)
                  * [STA-M-PROGRAM-COMPLIANCE-RECORDS](./03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10/DOMAINS/STA-M-PROGRAM-COMPLIANCE-RECORDS)


### 10-BUSINESS
- [10-BUSINESS](./10-BUSINESS/)
  - Market analysis and business development
  - Partnership agreements
  - Financial models and projections

### scripts
- [scripts](./scripts/)
  - Automation and utility scripts
  - Index generation tools
  - Validation and reporting scripts

### tools
- [tools](./tools/)
  - Development and analysis tools
  - Configuration utilities
  - Documentation generators

---

## Index Usage Guidelines

### For New Users
1. **Start here**: Review this index to understand repository structure
2. **Check governance**: Read [GOVERNANCE.md](./00-PROGRAM/GOVERNANCE.md) for policies
3. **Review CM plan**: See [CM Plan](./00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md) for processes
4. **Find templates**: Use [TEMPLATES](./00-PROGRAM/TEMPLATES/) for standard documents

### For Contributors
1. **File changes**: Start with [ECR process](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/)
2. **Check interfaces**: Review [ICD templates](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
3. **Follow standards**: Consult [STANDARDS](./00-PROGRAM/STANDARDS/) register
4. **Track traceability**: Use [UTCS](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/) for passports

### For System Engineers
1. **MBSE models**: Access at [DIGITAL_THREAD/MBSE](./00-PROGRAM/DIGITAL_THREAD/04-MBSE/)
2. **Digital twins**: See [DIGITAL_TWIN](./00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/)
3. **Integration**: Check [CROSS_SYSTEM_INTEGRATION](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/)
4. **Baselines**: Track at [BASELINES](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/)

### For Auditors
1. **Audit logs**: Check [AUDITS](./00-PROGRAM/CONFIG_MGMT/11-AUDITS/)
2. **Compliance records**: See [COMPLIANCE](./00-PROGRAM/COMPLIANCE/)
3. **Change history**: Review [CHANGE_LOG](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/03-REGISTERS/)
4. **Traceability**: Verify [TRACEABILITY](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)

## Search and Query

### Common Searches
- **Find a system**: Use Ctrl+F with ATA/STA chapter number (e.g., "ATA-24", "STA-A")
- **Locate documents**: Search by document type (ICD, ECR, BOM, etc.)
- **Check domains**: Look for domain abbreviations (AAA, CCC, EDI, etc.)
- **Find subsystems**: Search by subsystem code (e.g., "53-10", "24-30")

### Path Patterns
- **Program-level**: `00-PROGRAM/<functional-area>/`
- **Fleet ops**: `01-FLEET/<capability>/`
- **Aircraft**: `02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/<product>/MODELS/<model>/VERSION/<Qn>/`
- **Spacecraft**: `03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/<product>/MODELS/<model>/VERSION/<Qn>/`

## Integration with Other Systems

### PLM/PDM
- Assembly indices available in PLM/CAx/ASSEMBLIES/INDEX/
- Part master data in [ITEM_MASTER](./00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/)
- BOM structures in PLM/CAx/ASSEMBLIES/DOCS/BOM/

### Version Control
- Git repository provides version history
- Baselines tracked in [BASELINES](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/)
- Releases managed in [RELEASES](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/)

### UTCS Integration
- Each system declares UTCS namespace: `utcs://<PRODUCT>/<SYSTEM>/<Qn>`
- Registry maintained at [UTCS](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/)
- Schemas and threads tracked in UTCS subdirectories

## Best Practices

### Index Maintenance
- Update index when adding new top-level directories
- Verify links during quarterly reviews
- Document major structural changes in change logs
- Keep deprecated paths for reference with clear markings

### Navigation
- Use bookmark/favorites for frequently accessed areas
- Leverage IDE/editor navigation features for local searches
- Keep this index open as reference during navigation
- Use relative links when creating cross-references

### Documentation
- Each major directory should contain a README.md
- INDEX/ directories for complex subsystems
- Link to parent and sibling directories
- Include purpose, contents, and usage guidelines

## Related Documentation

- [GOVERNANCE.md](./00-PROGRAM/GOVERNANCE.md) — Program governance framework
- [CM Plan](./00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md) — Configuration management plan
- [Standards Register](./00-PROGRAM/STANDARDS/01-REGISTER/) — Applicable standards catalog
- [Glossary](#glossary-scoped) — Key terms and abbreviations (see above)

## Index Metadata

- **Index Type**: Master Repository Index
- **Coverage**: Complete top-level and major subsystem directories
- **Maintenance**: Manual with quarterly review
- **Last Updated**: Maintained continuously
- **Owner**: Program & Configuration Management
- **Status**: Current

---

**Back to top**: [↑ Repository Index](#repository-index-and-navigation)

