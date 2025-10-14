# PLUMA Components

## Overview

PLUMA consists of five core components that work together to provide industrial-scale automation for aerospace lifecycle management.

---

## 1. PPUI — Parametric Documentation Generator

### Purpose

Generate parametric documentation from templates with high reuse ratios across programs.

### Key Features

- **Template Library**: 50+ parametric templates covering all CAx phases
- **Conversational AI**: Natural language interface for template instantiation
- **Parameter Validation**: Type-safe parameter definitions with validation rules
- **Version Control**: Git-based template versioning
- **Context Reuse**: 65% average reuse ratio across programs

### Architecture

```
┌──────────────────────────────────────────────────────┐
│              PPUI Frontend (React)                   │
│  - Conversational interface                          │
│  - Template browser                                  │
│  - Parameter editor                                  │
└──────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│           PPUI Engine (Python/FastAPI)               │
│  - Template rendering (Jinja2)                       │
│  - Parameter validation                              │
│  - AI/LLM integration                                │
└──────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│          Template Repository (Git)                   │
│  - Version-controlled templates                      │
│  - Template metadata                                 │
│  - Parameter schemas                                 │
└──────────────────────────────────────────────────────┘
```

### API Endpoints

```yaml
POST /api/v1/templates/instantiate
  - Instantiate template with parameters
  
GET /api/v1/templates/{template_id}
  - Retrieve template definition
  
POST /api/v1/templates/validate
  - Validate parameters against schema
  
GET /api/v1/templates/search
  - Search template library
```

### Metrics

- Template instantiation time: <30 seconds (p95)
- Context reuse ratio: 65% (target: >70%)
- Template library size: 50+ templates
- User satisfaction: 4.2/5.0

---

## 2. Interphase Control

### Purpose

Orchestrate phase transitions and gate approvals at scale with parallel processing.

### API Specification

Complete API specification available: [Interphase API Spec (OpenAPI 3.1)](./INTERPHASE_API_SPEC.yaml)

**Quick Links**:
- [Event Contracts](./INTERPHASE_EVENT_CONTRACTS.md) - Kafka topics and webhook schemas
- [cURL Examples](./INTERPHASE_CURL_EXAMPLES.md) - Practical API usage examples
- [Data Model](./INTERPHASE_DATA_MODEL.sql) - PostgreSQL schema

**API Base URL**: `https://api.interphase.ap-aero.portfolio/v1`

**Authentication**: OIDC (Bearer tokens) + mTLS for service-to-service

**Key Operations**:
- Freeze contexts: `POST /programs/{programId}/contexts/freeze`
- Gate decisions: `POST /programs/{programId}/phases/{phaseId}/gates/{gateId}/decision`
- Transitions: `POST /transitions`
- Validations: `POST /validations/run`
- Cloning: `POST /clones`

### Key Features

- **Phase Gate Workflows**: Automated approval chains
- **Parallel Processing**: Multiple phase gates in parallel
- **Capacity Planning**: Resource forecasting for next phases
- **Frozen Contexts**: State snapshots at phase transitions
- **Audit Trail**: Complete history of phase transitions

### Architecture

```
┌──────────────────────────────────────────────────────┐
│         Interphase Control Dashboard (React)         │
│  - Phase timeline view                               │
│  - Gate approval interface                           │
│  - Capacity planning view                            │
└──────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│      Workflow Engine (Temporal/Cadence)              │
│  - Phase transition workflows                        │
│  - Approval orchestration                            │
│  - Validation execution                              │
└──────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│         State Management (PostgreSQL)                │
│  - Phase states                                      │
│  - Gate approvals                                    │
│  - Validation results                                │
└──────────────────────────────────────────────────────┘
```

### Phase Transition Workflow

```yaml
workflow: phase_transition
inputs:
  - from_phase: CAI
  - to_phase: CAO
  - program_id: AMPEL360-BWB-Q100
  
steps:
  1. validate_phase_completion:
      - Check all artifacts present
      - Verify validation passes
      - Confirm deliverables complete
      
  2. capacity_check:
      - Forecast resource needs
      - Check resource availability
      - Alert if capacity insufficient
      
  3. approval_gate:
      - Notify stakeholders
      - Collect approvals (parallel)
      - Timeout: 7 days
      
  4. create_frozen_context:
      - Snapshot current state
      - Tag as phase boundary
      - Create UTCS anchor
      
  5. initialize_next_phase:
      - Provision resources
      - Clone templates
      - Notify team
```

### Metrics

- Phase transition time: <2 weeks (target: <1 week)
- Approval cycle time: <7 days
- Automated validation coverage: >90%
- Phase gate success rate: 92%

---

## 3. Metabuilder Middleware

### Purpose

Auto-generate UIs from backend schemas with <5 minute regeneration time.

### Key Features

- **Schema-Driven**: OpenAPI/GraphQL schemas as source of truth
- **Multiple Metabuilders**: 7+ specialized metabuilder types
- **Fast Regeneration**: <5 minutes from schema change to UI update
- **Zero Manual Coding**: Eliminates UI development bottleneck
- **Type Safety**: Strongly typed UI components

### Architecture

```
┌──────────────────────────────────────────────────────┐
│           Backend API (FastAPI/GraphQL)              │
│  - OpenAPI schema                                    │
│  - GraphQL schema                                    │
│  - Schema versioning                                 │
└──────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│         Metabuilder Engine (TypeScript)              │
│  - Schema parser                                     │
│  - UI component generator                            │
│  - React component builder                           │
└──────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│           Generated UI (React/Next.js)               │
│  - Type-safe components                              │
│  - Auto-generated forms                              │
│  - Validation logic                                  │
└──────────────────────────────────────────────────────┘
```

### Metabuilder Types

See [05-METABUILDERS/README.md](../05-METABUILDERS/README.md) for detailed specifications:

1. **Template Generator**: PPUI template instantiation
2. **Phase Gate Controller**: Approval workflows
3. **Validation Dashboard**: Test results and metrics
4. **Diff Viewer**: Change comparison
5. **Optimization Dashboard**: Trade study results
6. **Production Tracker**: Manufacturing status
7. **Capacity Planning Dashboard**: Resource forecasting

### Metrics

- UI regeneration time: 4.1 minutes (target: <5 minutes)
- Schema coverage: 100%
- Type safety: 100% (TypeScript strict mode)
- Manual UI code: 0%

---

## 4. Enterprise Memory

### Purpose

Federated knowledge management with context cloning and 99.999% durability.

### Key Features

- **Frozen Contexts**: Immutable state snapshots
- **Context Cloning**: Replicate knowledge across programs
- **Distributed Queries**: Fast queries across federated data
- **High Durability**: 11 nines durability (S3 + PostgreSQL)
- **Version Control**: Git-based artifact versioning

### Architecture

```
┌──────────────────────────────────────────────────────┐
│       Enterprise Memory API (GraphQL/REST)           │
│  - Context queries                                   │
│  - Artifact retrieval                                │
│  - Cloning operations                                │
└──────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│         Metadata Store (PostgreSQL)                  │
│  - Context metadata                                  │
│  - Artifact index                                    │
│  - Relationships                                     │
└──────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│        Artifact Storage (S3 + Git)                   │
│  - S3: Large files (CAD, analysis results)           │
│  - Git: Versioned documents and configs              │
│  - UTCS: Blockchain anchors                          │
└──────────────────────────────────────────────────────┘
```

### Frozen Context Structure

```yaml
frozen_context:
  id: AMPEL360-BWB-Q100-CAD-20251014
  program: AMPEL360-BWB-Q100
  phase: CAD
  timestamp: 2025-10-14T21:50:29Z
  status: frozen
  is_template: true
  
  artifacts:
    - type: cad_model
      path: s3://pluma-artifacts/ampel360-bwq100/cad/wing-v12.stp
      checksum: sha256:abc123...
      size_bytes: 125000000
      
    - type: document
      path: git://pluma-docs/ampel360-bwq100/design-spec-v3.md
      commit: d4f5e6...
      
  metadata:
    domains: [AAA, PPP, EDI]
    validation_status: passed
    approvals:
      - role: chief_engineer
        user: john.doe@ampel.aero
        timestamp: 2025-10-13T14:30:00Z
        
  parameters:
    wing_span_m: 40
    passenger_capacity: 250
    mtow_kg: 180000
```

### Context Cloning

```python
# Clone context with parameter overrides
new_context = enterprise_memory.clone_context(
    source="AMPEL360-BWB-Q100/CAD",
    target="AMPEL360-BWB-Q200/CAD",
    overrides={
        "wing_span_m": 45,
        "passenger_capacity": 350,
        "mtow_kg": 240000
    }
)

# What happens:
# 1. Copy metadata with parameter overrides
# 2. Clone artifacts (copy-on-write)
# 3. Update references and relationships
# 4. Create new frozen context
# 5. Validate cloned context
```

### Metrics

- Context query time: 0.7 seconds (target: <1 second)
- Durability: 99.999999999% (S3 standard)
- Context reuse ratio: 65% (target: >70%)
- Storage efficiency: 85% (deduplication)

---

## 5. Infranet Protocol

### Purpose

Multi-organization federation at scale with <2 second sync latency.

### Key Features

- **Elastic Sync**: Real-time change propagation
- **Export Rules**: Fine-grained access control
- **Multi-Tenant**: Isolated federation endpoints per organization
- **Security**: mTLS encryption and authentication
- **Monitoring**: Federation health dashboard

### Architecture

```
┌──────────────────────────────────────────────────────┐
│         Organization A (Prime Contractor)            │
│  ┌────────────────────────────────────────────────┐  │
│  │   FE Endpoint: fe://orgA.aero/program          │  │
│  │   - Export policies                            │  │
│  │   - Change publisher                           │  │
│  └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
                        │
                        ▼ (Apache Kafka)
┌──────────────────────────────────────────────────────┐
│             FE Message Bus (Kafka)                   │
│  - Change events                                     │
│  - Multi-tenant topics                               │
│  - Geo-replication                                   │
└──────────────────────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│         Organization B (Tier-1 Supplier)             │
│  ┌────────────────────────────────────────────────┐  │
│  │   FE Endpoint: fe://orgB.com/program           │  │
│  │   - Import subscriptions                       │  │
│  │   - Change consumer                            │  │
│  └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

### Federation Protocol

```yaml
# Change Event
event:
  type: artifact_updated
  source: fe://ampel.aero/programs/AMPEL360
  domain: CQH
  artifact_id: h2-tank-design-v5
  timestamp: 2025-10-14T21:50:29.123Z
  checksum: sha256:def456...
  
  routing:
    targets: [fe://cryotech.de/ampel360/h2-tanks]
    priority: high
    ttl_seconds: 300
    
  payload:
    change_type: update
    fields_changed: [pressure_rating, volume_liters]
    previous_checksum: sha256:abc123...
```

### Sync Latency Optimization

**Techniques**:
1. **WebSocket Push**: Real-time notifications
2. **Redis Caching**: Reduce database queries
3. **CDN**: Edge caching for artifacts
4. **Kafka Partitioning**: Parallel message processing
5. **Geo-Replication**: Regional Kafka clusters

### Metrics

- Sync latency (p99): 3.2 seconds (target: <2 seconds)
- Sync latency (avg): 1.8 seconds ✅
- Event throughput: 10,000 events/second
- Federation uptime: 99.95%

---

## Component Integration

### Data Flow

```
User Input
   │
   ▼
PPUI (Generate parametric docs)
   │
   ▼
Interphase Control (Orchestrate phase transitions)
   │
   ▼
Metabuilders (Generate UIs)
   │
   ▼
Enterprise Memory (Store frozen contexts)
   │
   ▼
Infranet Protocol (Federate across orgs)
   │
   ▼
External Systems (MAL/MAP services, Digital Twin, etc.)
```

### Communication Patterns

**1. Synchronous**:
- PPUI ↔ Template Engine
- Metabuilders ↔ Backend APIs
- Enterprise Memory ↔ Metadata Store

**2. Asynchronous**:
- Interphase Control ↔ Validation Services
- Enterprise Memory ↔ Artifact Storage
- Infranet Protocol ↔ Federation Partners

**3. Event-Driven**:
- Phase transitions → Workflow triggers
- Artifact changes → Federation events
- Validation results → Dashboard updates

### Technology Stack

| Component | Technologies |
|-----------|-------------|
| PPUI | React, FastAPI, Jinja2, LangChain |
| Interphase Control | Temporal, PostgreSQL, React |
| Metabuilders | TypeScript, React, OpenAPI, GraphQL |
| Enterprise Memory | PostgreSQL, S3, Git, GraphQL |
| Infranet Protocol | Kafka, WebSocket, Redis, mTLS |

### Deployment

All components deployed on Kubernetes with:
- Auto-scaling (HPA)
- Health monitoring (Prometheus/Grafana)
- Service mesh (Istio)
- GitOps (ArgoCD)
- Secrets management (HashiCorp Vault)

---

## Component Roadmap

### Q4 2025
- [ ] PPUI: AI-enhanced template generation
- [ ] Interphase Control: Parallel phase gates
- [ ] Metabuilders: 10+ metabuilder types
- [ ] Enterprise Memory: Cross-program search
- [ ] Infranet: <2 second sync latency

### Q1 2026
- [ ] PPUI: 100+ templates
- [ ] Interphase Control: Predictive phase planning
- [ ] Metabuilders: Custom metabuilder SDK
- [ ] Enterprise Memory: Time-travel queries
- [ ] Infranet: Multi-cloud federation

### Q2 2026
- [ ] Full multi-tenant isolation
- [ ] Global deployment (5 regions)
- [ ] 99.99% uptime SLA
- [ ] 200+ active users

---

## Related Documentation

- [Master Architecture](../01-ARCHITECTURE/MASTER_ARCHITECTURE_V1.1.md)
- [CAx Phases](../03-CAX_PHASES/README.md)
- [Scalability Pillars](../04-SCALABILITY/README.md)
- [Metabuilders](../05-METABUILDERS/README.md)
- [Success Metrics](../06-METRICS/README.md)
