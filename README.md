# IDEALEEU

> Unified, audit‑ready platform for multi‑vehicle aerospace programs. Modules: **AMSDP** (Aerospace Material & Software Digital Passports) and **AAMMPP** (Aerospace Assets Management, Maintenance & Procurement Platform).

### What IDEALEEU is

An ESG‑first framework to design next‑generation aerospace systems and models. It uses common LLMs via a provider‑agnostic gateway, with retrieval and guardrails, and includes AMSDP and AAMMPP as reference applications implementing the framework.

---

## Badges

[![Status](https://img.shields.io/badge/status-alpha-yellow)](#)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

<!-- Add real CI badges once pipelines are enabled -->

---

## TL;DR

IDEALE‑EU is a design and governance framework that turns ESG principles into executable data contracts, workflows, and models. It composes reference services (AMSDP, AAMMPP) and an LLM layer that runs on commodity models through RAG and policy guardrails. Result: auditable architectures, artifacts, and APIs reusable across programs.

### Principles

* ESG‑first: evidence and metrics embedded in every artifact.
* LLM‑enabled, model‑agnostic: common models via a provider‑neutral gateway.
* Standards‑anchored: W3C VC, EPCIS, S‑Series, ISO 15288.
* Replaceable components: stores, queues, and models are swappable.

---

## Positioning — what IDEALE‑EU is

**What it is**

* An open, modular framework to **design responsibly**: architectures, models, and processes with ESG principles embedded by default.
* A set of **methods and data contracts** that make traceability, auditability, and lifecycle stewardship measurable.
* A **governance layer** (MAL) that encodes policy, risk controls, and evidence collection.

**What it is not**

* Not an aircraft or engine program; no product claims.
* Not a certification declaration; it **collects evidence** to support audits.
* Not a token or marketplace; commercial exchanges (A360Exchanges‑TT) are adjunct, not core.

**ESG‑first principles**

1. **Environment**: decarbonization, energy efficiency, circularity, end‑of‑life.
2. **Social**: safety, human‑in‑the‑loop oversight, fair labor, accessibility.
3. **Governance**: transparency, explainability, anti‑tamper audit, supply‑chain trust.

**Value**

* Unified digital thread from requirements to operations.
* Interoperability with industry standards; vendor‑neutral interfaces.
* **Responsible AI**: QPLC human‑governed automation with guardrails and evidence.
* Lower cost‑of‑change via versioned contracts and contract tests.

**Primary users**

* OEMs, Tier‑n suppliers, MROs, regulators, and research programs.

**Success metrics**

* Verified emissions impact, safety outcomes, interop conformance, audit completeness, time‑to‑evidence, and total cost of quality.

**Tagline**: *Design responsibly. Prove it.*

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
* [Sustainable energy systems](#sustainable-energy-systems-for-passenger-aircraft)
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

## Packs & Engineering Constructs

Canonical packs used across design, analysis, production, integration, and service. Packs act as reusable building blocks in TFA domains and appear as tags in schemas and repository paths.

| Code    | Name                                      | Description / Notes                                                                                 |
| ------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------- |
| CAx     | Computer‑Aided X                          | Umbrella for CAD/CAE/CAM/CFD; shared data patterns and exchange.                                    |
| QOx     | Quantum Optimizations                     | Variational, annealing, and quantum‑inspired optimization for design, routing, scheduling, packing. |
| PAx     | Packaging & Assemblies                    | **ONB** = Onboard, **OUT** = Offboard, **BDG** = Bridge.                                            |
| CAD     | Computer‑Aided Design                     | Geometry, parametrics, drawings.                                                                    |
| CAE     | Computer‑Aided Engineering                | Analysis and simulation.                                                                            |
| CAM     | Computer‑Aided Manufacturing              | NC/toolpaths and manufacturing plans.                                                               |
| CAI     | Computer‑Aided Integration & Installation | Integration, installation, testing, tooling.                                                        |
| CFD     | Computational Fluid Dynamics              | Flow and thermal simulation.                                                                        |
| CMP     | Configuration Management Program          | Plans, baselines, effectivity, change control.                                                      |
| CQA     | Certification, V&V and Quality Assurance  | Compliance, verification, validation, QA.                                                           |
| MRO     | Maintenance, Repair, Overhaul             | Service operations with evidence capture.                                                           |
| ALAR‑CC | As Low As Reasonable Chain Complexity     | Supply services, chain traceability, ESG.                                                           |

**Usage**

* **Schemas**: `component.packs[]` and `workflow.packs[]` support the codes above.
* **Paths**: `.../PACKS/<Code>/...` optional folder to co‑locate artifacts.
* **Interoperability**: CAx aligns with STEP/ JT/ glTF; CMP and CQA map to governance docs.

---

### ALAR‑CC — As Low As Reasonable Chain Complexity

| Code | Name                                     | Description / Notes                                                                                 |
| ---- | ---------------------------------------- | --------------------------------------------------------------------------------------------------- |
| CAx  | Computer‑Aided Data Exchange             | Umbrella for shared data patterns and exchange.                                                     |
| QOx  | Quantum Optimizations                    | Variational, annealing, and quantum‑inspired optimization for design, routing, scheduling, packing. |
| PAx  | Packaging & Assemblies                   | Orientation markers: **ONB** = Onboard, **OUT** = Outboard.                                         |
| CAD  | Computer‑Aided Design                    | Geometry, parametrics, drawings.                                                                    |
| CAE  | Computer‑Aided Engineering               | Analysis and simulation, including FEM, CFD, FMEA, etc.                                             |
| CAM  | Computer‑Aided Manufacturing             | NC/toolpaths and manufacturing plans. Integration, installation, testing, tooling.                  |
| CAI  | Computer‑Aided Industrialization         | Entry‑into‑service (EIS), production plan, marketing.                                               |
| CMP  | Configuration Management Program         | Baselines, effectivity, change control. Continuous Airworthiness.                                   |
| CAV  | Certification, V&V and Quality Assurance | Compliance, verification, validation, QA.                                                           |
| CAS  | Computer‑Aided Services                  | Maintenance, Repair, Overhaul. Service operations, supply services, chain traceability, ESG.        |

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

## Sustainable energy systems for passenger aircraft

The platform tracks energy architectures across hydrogen, battery‑electric, SAF, and advanced propulsion. This section summarizes the state and references a multi‑energy architecture proposal for integration into product roadmaps and certification planning.

| **Energy Technology**               | **Description**                                                                           | **Target Aircraft / Routes**                    | **Key Developments & Challenges**                                                                                                        |
| :---------------------------------- | :---------------------------------------------------------------------------------------- | :---------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Hydrogen Power**                  | Powers aircraft via hydrogen combustion engines or fuel cells, emitting only water vapor. | Short‑ to medium‑haul regional aircraft.        | High development and infrastructure costs; challenges with lightweight hydrogen storage. Airbus ZEROe program faces delays.              |
| **Battery‑Electric**                | Uses lithium‑ion or advanced batteries to power electric motors for propulsion.           | Short‑haul routes under ~500 km (~310 miles).   | Limited by low energy density; batteries are ~50x heavier than jet fuel for same energy. New fuel cell research aims for higher density. |
| **Sustainable Aviation Fuel (SAF)** | Drop‑in biofuel from renewable sources; works with existing jet engines.                  | All aircraft types, especially long‑haul.       | Scalable but limited sustainable feedstock supply. Current focus for near‑term emissions reduction.                                      |
| **Advanced Propulsion**             | New engine core designs like **Open Fan**.                                                | Next‑generation aircraft across various ranges. | Targets >20% fuel‑burn and CO₂ reduction vs. current efficient engines. Compatible with SAF and future hydrogen use.                     |

### Supporting ecosystem and challenges

* **Airports as energy hubs**: high‑power charging can require **≥ 1 MW per charger**; on‑site generation and storage improve resilience and economics.
* **Innovation landscape**: OEMs iterate existing platforms; startups drive radical concepts but face capital and certification risk.
* **Policy drivers**: tighter CO₂ standards, fossil jet‑fuel taxation, and R&D funding accelerate adoption.

**TFA mapping**: CQH (Cryogenics–Quantum–H₂), EEE (Electrical–Energization), PPP (Propulsion–Power–Plants), IIF (Infrastructure).

### Technical Note: Multi‑Energy‑Agnostic Architecture for Sustainable Aeronautical Propulsion (AMPAS)

#### 1. Introduction

This document presents a conceptual model for a **multi‑energy‑agnostic propulsion architecture (AMPAS)** aimed at full decarbonization of commercial and regional aircraft by jointly integrating **solid‑state batteries, liquid hydrogen (LH₂), sustainable aviation fuels (SAF/e‑SAF)**, and high‑efficiency **Open Fan** systems.
The framework draws on recent work and programs from *Clean Aviation JU*, *Avio Aero–GE Aerospace*, *Airbus ZEROe*, *Safran–ONERA*, and *Capgemini Engineering*.[1][2][6][7][10]

#### 2. System overview

AMPAS combines four complementary energy subsystems:

* **Electric energy module**: **solid‑state battery** packs with > 600 Wh/kg, high peak power, and long life. Primary role: assist power peaks at takeoff, auxiliary thrust, and emergency reserves.[1]
* **Cryogenic liquid‑hydrogen module (LH₂)**: integrated CRYOSTAR‑type tanks with low‑permeability composites feeding fuel cells or direct‑burners in modified turbines. Enables long‑range autonomy with zero CO₂.[10][1]
* **SAF/e‑SAF subsystem**: energy backup and thermal support, stabilizing the hybrid thermodynamic cycle and assisting prolonged cruise. Compatible with **Open Fan** cores such as CFM RISE and upgraded CATALYST turbines.[2][11]
* **Open Fan propulsive module**: contra‑rotating, unshrouded fans with > 20% efficiency gains versus conventional Brayton‑cycle engines. Accepts mixed SAF/H₂/electric supply.[7][12]

#### 3. Functional architecture

A **parallel‑hybrid** system with centralized digital management:

1. **Takeoff**: solid‑state batteries + H₂ (fuel cells) → maximum thrust with reduced thermal spikes.
2. **Climb and initial cruise**: transition to Open Fan on H₂ or SAF; electric support for stability.
3. **Optimized cruise**: high‑efficiency thermal mode (H₂ or SAF) with kinetic‑energy recovery (MECS).
4. **Descent and taxi**: partial regeneration and recharge via reverse thrust and auxiliary turbines.

The **EDPICS** (distributed energy control system) coordinates power flows, regulates cryogenics, and manages gaseous‑H₂ recirculation, achieving system efficiencies > 70%.

#### 4. Structural integration

Tri‑axial placement: cryogenic tanks (central fuselage), battery packs (wing‑root), and Open Fan modules (tail or mixed nacelles). Multilayer thermal isolation and ultra‑light ceramic composites. Lower specific mass than all‑electric setups with energy density comparable to kerosene.[6][9]

#### 5. Benefits and technological challenges

**Benefits**

* Up to **85% CO₂ and NOₓ** reduction with SAF, and **> 95%** with green H₂.
* **20–25%** lower overall consumption versus LEAP‑1A turbines.
* Multimodal flexibility by energy availability.
* Aligned with circular‑energy strategies.

**Challenges**

* Thermal management across cryogenic zones (−253 °C) and hot‑fuel circuits (SAF ≈ 200 °C).
* Certification baselines not yet consolidated for hybrid‑cryogenic systems.
* Mechanical and acoustic complexity of Open Fan modules.
* Dual airport infrastructure (SAF liquids + hydrogen, optional LOHC).

#### 6. Conclusion and outlook

Agnostic integration of **solid‑state batteries, liquid hydrogen, SAF, and Open Fan** defines a viable path for **100–200‑seat** aircraft with **transcontinental** range by **2040–2045**.
Programs **AMBER**, **LEIA**, and **CRYOSTAR** indicate maturity (TRL 5–6) of individual blocks and support **zero‑emission aviation** based on energy modularity, interoperability, and intelligent thermal management.[2][6][7][10][1]

**References**

1. [https://fly-news.es/sostenibilidad/borrador-automaticoclean-aviation-nuevos-programas-descarbonizacion-aviacion-comercial/](https://fly-news.es/sostenibilidad/borrador-automaticoclean-aviation-nuevos-programas-descarbonizacion-aviacion-comercial/)
2. [https://www.airline92.com/noticias/industria-aeronautica/avio-aero-lidera-programa-amber-propulsion-hibrido-electrica/](https://www.airline92.com/noticias/industria-aeronautica/avio-aero-lidera-programa-amber-propulsion-hibrido-electrica/)
3. [https://www.pressreleasefinder.com/Avio_Aero/GEAAPR001/es/](https://www.pressreleasefinder.com/Avio_Aero/GEAAPR001/es/)
4. [https://elperiodicodelaenergia.com/la-implementacion-de-la-tecnologia-saf-principal-obstaculo-para-la-descarbonizacion-en-aviacion/](https://elperiodicodelaenergia.com/la-implementacion-de-la-tecnologia-saf-principal-obstaculo-para-la-descarbonizacion-en-aviacion/)
5. [https://hidrogeno-verde.es/arquitectura-propulsion-aeronaves-hidrogeno/](https://hidrogeno-verde.es/arquitectura-propulsion-aeronaves-hidrogeno/)
6. [https://www.aviacionnews.com/2025/03/airbus-summit-2025-saf-hidrogeno-y-la-proxima-generacion-de-aeronaves/](https://www.aviacionnews.com/2025/03/airbus-summit-2025-saf-hidrogeno-y-la-proxima-generacion-de-aeronaves/)
7. [https://www.avionrevue.com/industria/safran-y-onera-inician-las-pruebas-en-tunel-aerodinamico-del-futuro-open-fan/](https://www.avionrevue.com/industria/safran-y-onera-inician-las-pruebas-en-tunel-aerodinamico-del-futuro-open-fan/)
8. [https://www.bbva.com/es/sostenibilidad/estas-son-las-tecnologias-mas-comunes-para-producir-combustibles-saf/](https://www.bbva.com/es/sostenibilidad/estas-son-las-tecnologias-mas-comunes-para-producir-combustibles-saf/)
9. [https://www.investigacion.us.es/noticias/una-innovadora-arquitectura-de-propulsion-de-aeronaves-mediante-hidrogeno-nacida-en-la-etsi](https://www.investigacion.us.es/noticias/una-innovadora-arquitectura-de-propulsion-de-aeronaves-mediante-hidrogeno-nacida-en-la-etsi)
10. [https://www.capgemini.com/es-es/investigacion/perspectivas-de-expertos/sistemas-de-energia-en-las-aeronaves-del-futuro-basados-en-hidrogeno/](https://www.capgemini.com/es-es/investigacion/perspectivas-de-expertos/sistemas-de-energia-en-las-aeronaves-del-futuro-basados-en-hidrogeno/)
11. [https://fuelnature.es/saf-sintetico-y-e-saf-el-papel-del-hidrogeno-verde-en-la-aviacion-del-futuro/](https://fuelnature.es/saf-sintetico-y-e-saf-el-papel-del-hidrogeno-verde-en-la-aviacion-del-futuro/)
12. [https://www.aviacionline.com/airbus-prueba-el-motor-open-fan-de-cfm-en-un-a380-para-avanzar-hacia-una-aviacion-mas-eficiente](https://www.aviacionline.com/airbus-prueba-el-motor-open-fan-de-cfm-en-un-a380-para-avanzar-hacia-una-aviacion-mas-eficiente)

---

## Extended materials (full reference)

### Packs & Engineering Constructs

| Code     | Name                                      | Description / Notes                                                                                 |
| -------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------- |
| CAx      | Computer‑Aided X                          | Umbrella for CAD/CAE/CAM/CFD; shared data patterns and exchange.                                    |
| QOx      | Quantum Optimizations                     | Variational, annealing, and quantum‑inspired optimization for design, routing, scheduling, packing. |
| PAx      | Packaging & Assemblies                    | Orientation markers: **ONB** = Onboard, **OUT** = Outboard.                                         |
| CAD      | Computer‑Aided Design                     | Geometry, parametrics, drawings.                                                                    |
| CAE      | Computer‑Aided Engineering                | Analysis and simulation.                                                                            |
| CAM      | Computer‑Aided Manufacturing              | NC/toolpaths and manufacturing plans.                                                               |
| CAI      | Computer‑Aided Integration & Installation | Integration, installation, testing, tooling.                                                        |
| CFD      | Computational Fluid Dynamics              | Flow and thermal simulation.                                                                        |
| CMP      | Configuration Management Program          | Plans, baselines, effectivity, change control.                                                      |
| CQA      | Certification, V&V and Quality Assurance  | Compliance, verification, validation, QA.                                                           |
| MRO      | Maintenance, Repair, Overhaul             | Service operations with evidence capture.                                                           |
| ALAR‑CC  | As Low As Reasonable Chain Complexity     | Supply services, chain traceability, ESG.                                                           |
| OB / OFF | Onboard / Outboard                        | Orientation tags used in PAx and tech pubs.                                                         |

---

### TFA Canonical Domains

| Code | Domain                                 | Focus                                                   |
| ---- | -------------------------------------- | ------------------------------------------------------- |
| AAA  | Airframes‑Aerodynamics‑Airworthiness   | Structure, aero, certification                          |
| AAP  | Airport‑Adaptable‑Platforms            | Ground ops, GSE                                         |
| CCC  | Cockpit‑Cabin‑Cargo                    | Flight deck, passenger, freight                         |
| CQH  | Cryogenics‑Quantum‑H2                  | H₂ systems, quantum tech                                |
| DDD  | Drainage‑Dehumidification‑Drying       | Moisture control                                        |
| EDI  | Electronics‑Digital‑Instruments        | Avionics, sensors                                       |
| EEE  | Electrical‑Endocircular‑Energization   | Power, energy harvesting                                |
| EER  | Environmental‑Emissions‑Remediation    | Fire, pollution, sustainability                         |
| IIF  | Industrial‑Infrastructure‑Facilities   | Manufacturing, tooling                                  |
| IIS  | Information‑Intelligence‑Systems       | Software, AI, cybersecurity                             |
| LCC  | Linkages‑Control‑Communications        | Flight controls, datalinks                              |
| LIB  | Logistics‑Inventory‑Blockchain         | Supply chain, evidence anchoring                        |
| MMM  | Mechanical‑Material‑Modules            | Materials, mechanical, MRO                              |
| OOO  | Operations‑Optimizations‑Orchestration | Fleet ops, Quantum Opt Material, Designs, Backends, UIs |
| PPP  | Propulsion‑Power‑Plants                | Engines, thrust, fuel                                   |

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



