# REFERENCE_ARCHITECTURE

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 01-ARCHITECTURE > REFERENCE_ARCHITECTURE**

Digital twin reference architecture defining layers, data flows, and integration with digital thread.

## Purpose

This document describes the technical architecture of the aircraft digital twin, including its layered structure, data flows, and integration with the broader digital thread ecosystem.

## Architecture Overview

The digital twin follows a four-layer architecture aligned with ISO 23247 and the program's digital thread architecture (see `00-PROGRAM/DIGITAL_THREAD/03-ARCHITECTURE/`):

```
┌─────────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER (L4)                        │
│  Fleet Dashboards │ Predictive Maintenance │ Mission Planning   │
└─────────────────────────────────────────────────────────────────┘
                              ▲ │
                    REST/gRPC API, WebSocket
                              │ ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SERVICE LAYER (L3)                          │
│  Twin API Gateway │ Analytics Engine │ Orchestration Service    │
│  Auth/AuthZ │ Rate Limiting │ Caching │ Load Balancing         │
└─────────────────────────────────────────────────────────────────┘
                              ▲ │
                    Internal APIs, Message Queue
                              │ ▼
┌─────────────────────────────────────────────────────────────────┐
│                       MODEL LAYER (L2)                           │
│  Physics Models │ Behavioral Models │ Data-Driven Models        │
│  Co-Simulation Orchestrator │ Model Registry │ Version Control  │
└─────────────────────────────────────────────────────────────────┘
                              ▲ │
                    Model I/O, FMI, ONNX Runtime
                              │ ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DATA LAYER (L1)                           │
│  Telemetry Ingestion │ Config DB │ Time-Series Store │ Blob     │
│  Data Validation │ Schema Registry │ Lineage Tracking          │
└─────────────────────────────────────────────────────────────────┘
```

## Layer Descriptions

### L1: Data Layer

**Purpose**: Data ingestion, storage, validation, and provenance

**Components**:
- **Telemetry Ingestion**: Real-time and batch ingestion from aircraft via secure channels
  - Protocols: MQTT (edge), Kafka (ground), REST (batch)
  - Rate: 10-1000 Hz (critical sensors), 1 Hz (normal), event-driven (discrete states)
  - Validation: Schema validation, range checks, outlier detection
  
- **Configuration Database**: As-built, as-maintained configuration
  - Source: Configuration Management baseline (`00-PROGRAM/CONFIG_MGMT/04-BASELINES/`)
  - Format: Structured (relational DB), versioned with git_sha
  - Access: Read-only for twin, write via CM process
  
- **Time-Series Store**: Historical telemetry and model predictions
  - Technology: InfluxDB, TimescaleDB, or equivalent
  - Retention: 7 days (hot), 2 years (warm), 10 years (cold/archive)
  - Indexing: Aircraft ID, timestamp, signal ID
  
- **Blob Storage**: Large artifacts (CAE meshes, ML models, reports)
  - Format: ONNX (ML models), HDF5 (CAE data), PDF (reports)
  - Versioning: Immutable with content-addressable storage
  - Access Control: Role-based (RBAC)

**Data Interfaces**:
- **Input**: Telemetry from `01-FLEET/OPERATIONAL_DATA_HUB/`, configuration from CM
- **Output**: Validated data to Model Layer (L2)
- **Integration**: See `03-INTERFACES_APIS/STREAMS/INPUTS/TELEMETRY_MAP.csv`

### L2: Model Layer

**Purpose**: Execution of physics, behavioral, and data-driven models

**Components**:
- **Physics Model Runtime**:
  - **Aerodynamics**: CFD surrogates (ROM, GPR), polars, loads
    - Linked to `02-MODELS/PHYSICS/AERODYNAMICS/`
    - ATA-27 (Flight Controls), ATA-57 (Wings)
  - **Structures**: FEM solvers, fatigue calculators, margins
    - Linked to `02-MODELS/PHYSICS/STRUCTURES/`
    - ATA-51 (Structures), ATA-53 (Fuselage), ATA-55 (Stabilizers), ATA-57 (Wings)
  - **Thermal**: Cryo tank models, heat exchangers, cabin thermal
    - Linked to `02-MODELS/PHYSICS/THERMAL/`
    - ATA-21 (Air Conditioning), ATA-28 (Fuel - H₂), ATA-36 (Pneumatic)
  - **Propulsion**: Engine/motor performance, FADEC plants
    - Linked to `02-MODELS/PHYSICS/PROPULSION/`
    - ATA-70 (Engine - General), ATA-71-79 (Engine systems), ATA-80 (Starting)
  - **H₂ Energy**: Tank models, BOP, boil-off, leak detection
    - Linked to `02-MODELS/PHYSICS/ENERGY_H2/`
    - ATA-28 (Fuel)
  - **Environment**: Atmosphere (ISA, non-standard), mission profiles
    - Linked to `02-MODELS/PHYSICS/ENVIRONMENT/`
  
- **Behavioral Model Runtime**:
  - **State Machines**: SysML state charts, Stateflow (e.g., IMA health, fuel sequencing)
    - Linked to `02-MODELS/BEHAVIORAL/STATE_MACHINES/`
  - **Control Logic**: Autopilot, EMS interfaces, mode management
    - Linked to `02-MODELS/BEHAVIORAL/CONTROL_LOGIC/`
    - ATA-22 (Auto Flight), ATA-76 (Engine Controls)
  
- **Data-Driven Model Runtime**:
  - **ONNX Runtime**: Inference engine for ML models (CPU/GPU)
    - Models: Anomaly detectors, surrogates, regressors
    - Linked to `02-MODELS/DATA_DRIVEN/ONNX_MODELS/`
  - **Model Registry**: Version control, A/B testing, canary deployment
    - Metadata: Model Card, training data provenance, performance metrics
    - Linked to `04-VERSIONING_CONFIG/MODEL_MANIFEST.yaml`
  
- **Co-Simulation Orchestrator**:
  - **FMU Manager**: Load/unload FMUs (FMI 3.0 compliant)
    - Linked to `02-MODELS/CO_SIMULATION/FMU_FMI/`
  - **Master Algorithm**: Fixed-step or adaptive, error control
    - Linked to `02-MODELS/CO_SIMULATION/ORCHESTRATION.md`
  - **Data Exchange**: Variable mapping, unit conversion, interpolation

**Model Interfaces**:
- **Input**: Validated telemetry, configuration parameters, initial conditions
- **Output**: State predictions, KPIs, alerts, diagnostic codes
- **Integration**: Model I/O defined in `03-INTERFACES_APIS/`

### L3: Service Layer

**Purpose**: Expose twin capabilities via APIs, orchestrate analytics workflows

**Components**:
- **Twin API Gateway**:
  - **REST API**: CRUD operations, query historical data, trigger what-if scenarios
    - Spec: `03-INTERFACES_APIS/TWIN_API_SPEC.yaml`
    - Auth: OAuth2 + mTLS, rate limiting (100 req/min per client)
    - Versioning: Semantic versioning (v1, v2), backward compatibility
  - **gRPC API**: Low-latency streaming for real-time telemetry
    - Use case: Edge-to-ground sync, real-time dashboards
  - **WebSocket**: Pub/sub for alerts, model updates
    - Topics: anomalies, KPIs, system health
  
- **Analytics Engine**:
  - **Batch Analytics**: Daily/weekly reports, trend analysis, fleet benchmarking
  - **Real-Time Analytics**: Anomaly detection, threshold monitoring, alerts
  - **Interactive Analytics**: What-if scenarios, sensitivity analysis (user-triggered)
  
- **Orchestration Service**:
  - **Workflow Engine**: Airflow, Prefect, or equivalent
    - Workflows: Data ingestion → model execution → validation → storage
  - **Job Scheduler**: Cron-based or event-driven (e.g., post-flight analysis)
  - **Error Handling**: Retry logic, dead-letter queues, alerting
  
- **Cross-Cutting Concerns**:
  - **Authentication/Authorization**: OAuth2, RBAC, audit logging
  - **Rate Limiting**: Token bucket, per-client quotas
  - **Caching**: Redis for frequently accessed data (config, recent predictions)
  - **Load Balancing**: Distribute requests across model runtime instances

**Service Interfaces**:
- **Input**: API requests from applications (L4), internal triggers
- **Output**: API responses, streamed telemetry, alerts
- **Integration**: See `03-INTERFACES_APIS/TWIN_API_SPEC.yaml`

### L4: Application Layer

**Purpose**: End-user applications consuming twin services

**Applications**:
- **Fleet Management Dashboard**:
  - Real-time fleet health overview (map, health scores, alerts)
  - Aircraft drill-down (performance trends, maintenance status)
  - Linked to `01-FLEET/OPERATIONAL_DATA_HUB/06-ANALYTICS_CONSUMPTION/`
  
- **Predictive Maintenance App**:
  - RUL predictions, maintenance recommendations, work order generation
  - Integration with MRO system (see `09-INTEGRATIONS/MRO_LINKS.md`)
  - Linked to `01-FLEET/MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/`
  
- **Mission Planning Tool**:
  - Flight profile optimization (speed, altitude, routing)
  - H₂ consumption prediction, range analysis
  - Weather integration (winds aloft, icing conditions)
  
- **Engineering Analysis Suite**:
  - What-if scenario explorer (design mods, failure modes)
  - Correlation studies (predicted vs. actual)
  - Certification evidence generation
  
- **Mobile Pilot Assistant**:
  - Pre-flight checks, performance calculations
  - Real-time advisory (fuel efficiency tips)
  - Limited to non-safety-critical recommendations

**Application Interfaces**:
- **Input**: User interactions, external data sources (weather, NOTAMs)
- **Output**: Visualizations, reports, alerts
- **Integration**: Consume L3 APIs, no direct access to L1/L2

## Data Flow Diagrams

### Real-Time Telemetry Flow

```
[Aircraft Sensors] → [ACMS/FDAU] → [Datalink (Satcom/Cell)] 
                                          ↓
                              [API Gateway + Auth]
                                          ↓
                          [Telemetry Ingestion Service]
                                    ↓         ↓
                      [Schema Validation]  [Outlier Detection]
                                    ↓         ↓
                         [Time-Series DB]  [Message Queue]
                                               ↓
                              [Model Runtime (Real-Time Models)]
                                               ↓
                              [KPI Calculation + Alerts]
                                               ↓
                         [WebSocket Push to Dashboards]
```

### Batch Analytics Flow

```
[Time-Series DB] → [Scheduled Job (Daily 02:00 UTC)]
                              ↓
                    [Data Aggregation Service]
                              ↓
                    [Model Runtime (Batch Models)]
                              ↓
        [Performance Trends] [Fleet Benchmarking] [Certification Reports]
                              ↓
                    [Report Generation Service]
                              ↓
              [Blob Storage] + [Notification Service]
```

### What-If Scenario Flow

```
[User Request (API)] → [API Gateway + Auth]
                              ↓
                    [Scenario Validation Service]
                              ↓
            [Config DB: Load Baseline + Apply Delta]
                              ↓
                    [Co-Simulation Orchestrator]
                              ↓
        [Physics Models] [Behavioral Models] [Environment Models]
                              ↓
                    [Result Aggregation Service]
                              ↓
              [User Response (JSON/Plot)]
```

## Integration with Digital Thread

This twin architecture is a component of the broader digital thread (see `00-PROGRAM/DIGITAL_THREAD/03-ARCHITECTURE/`):

### Upstream Integrations
- **MBSE Models** (`04-MBSE/`): System architecture → twin structure, requirements → validation test cases
- **CAD/CAE** (PLM): Geometry → aerodynamics, FEM results → structures models
- **Configuration Management** (`CONFIG_MGMT/04-BASELINES/`): As-designed baseline → twin parameters

### Downstream Integrations
- **Test & Validation**: Twin predictions → test cases, test results → calibration data
- **Manufacturing**: Process parameters → as-built configuration
- **Operations** (`01-FLEET/`): Fleet data → twin updates, twin predictions → maintenance scheduling

### Bidirectional Integrations
- **Operational Data Hub** (`01-FLEET/OPERATIONAL_DATA_HUB/`):
  - ODH → Twin: Real-time telemetry, maintenance events
  - Twin → ODH: Predictions, alerts, KPIs
- **MRO Strategy** (`01-FLEET/MRO_STRATEGY/`):
  - MRO → Twin: Maintenance actions (e.g., part replacement)
  - Twin → MRO: RUL predictions, maintenance recommendations

## Deployment Architectures

### Edge Deployment (On-Aircraft)

```
┌─────────────────────────────────────┐
│   Aircraft IMA (Integrated Modular  │
│        Avionics)                     │
│                                      │
│  ┌────────────────────────────────┐ │
│  │ ACMS (Aircraft Condition       │ │
│  │       Monitoring System)       │ │
│  └────────────────────────────────┘ │
│              │                       │
│              ▼                       │
│  ┌────────────────────────────────┐ │
│  │ Twin Edge Runtime              │ │
│  │ - Real-time models (ONNX)      │ │
│  │ - Anomaly detection            │ │
│  │ - Local caching                │ │
│  │ - Secure boot, signed models   │ │
│  └────────────────────────────────┘ │
│              │                       │
│              ▼                       │
│  ┌────────────────────────────────┐ │
│  │ Datalink Interface             │ │
│  │ (Satcom, 4G/5G)                │ │
│  └────────────────────────────────┘ │
└─────────────────────────────────────┘
              │
              ▼ (intermittent)
   [Ground Operations Center]
```

**Constraints**:
- CPU: <15% utilization (per safety-of-flight guardrails)
- Memory: <256 MB for twin runtime
- Storage: <1 GB for models + cache
- No remote updates during flight phases (only on ground, powered, parking brake set)

### Ground Deployment (Operations Center)

```
┌────────────────────────────────────────────────────────┐
│              Cloud / On-Premise Datacenter              │
│                                                          │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────┐│
│  │ API Gateway    │  │ Load Balancer  │  │ Auth      ││
│  │ (Kong, Apigee) │  │                │  │ (Keycloak)││
│  └────────────────┘  └────────────────┘  └───────────┘│
│            │                    │                       │
│            ▼                    ▼                       │
│  ┌──────────────────────────────────────────────────┐ │
│  │    Twin Service Layer (Kubernetes Pods)          │ │
│  │  - API Service (10 replicas)                     │ │
│  │  - Model Runtime (20 replicas, GPU-enabled)      │ │
│  │  - Analytics Engine (5 replicas)                 │ │
│  │  - Orchestration (2 replicas)                    │ │
│  └──────────────────────────────────────────────────┘ │
│            │                    │                       │
│            ▼                    ▼                       │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────┐│
│  │ Time-Series DB │  │ Config DB      │  │ Blob      ││
│  │ (InfluxDB)     │  │ (PostgreSQL)   │  │ (MinIO)   ││
│  └────────────────┘  └────────────────┘  └───────────┘│
└────────────────────────────────────────────────────────┘
```

**Scalability**:
- Horizontal scaling: Add model runtime pods for increased load
- Vertical scaling: GPU instances for compute-intensive models (CFD surrogates)
- Auto-scaling: CPU >70% or queue depth >100 triggers scale-up

## Security Architecture

See also `07-RUNTIME_DEPLOYMENT/CYBERSECURITY.md` for detailed controls.

### Defense in Depth

**Layer 1: Network**
- API Gateway with DDoS protection, rate limiting
- mTLS for all inter-service communication
- Network segmentation (DMZ, application, data layers)

**Layer 2: Authentication/Authorization**
- OAuth2 + OIDC for user authentication
- Service accounts with short-lived tokens for inter-service auth
- RBAC with least-privilege principle

**Layer 3: Data**
- Encryption at rest (AES-256) for all persistent storage
- Encryption in transit (TLS 1.3) for all network communication
- Data anonymization for non-essential uses (e.g., analytics)

**Layer 4: Application**
- Secure boot for edge runtime (TPM-backed)
- Model signing (GPG/SLSA) to prevent tampering
- Input validation (schema, range, rate checks)

**Layer 5: Audit/Monitoring**
- Comprehensive audit logging (who, what, when, where)
- Security Information and Event Management (SIEM) integration
- Intrusion detection (anomalous API patterns)

## Performance Requirements

| Metric | Edge | Ground (Interactive) | Ground (Batch) |
|--------|------|---------------------|----------------|
| **Latency** | <100ms (alerts) | <5s (API response) | <1hr (reports) |
| **Throughput** | 1000 msg/s | 10,000 req/s | N/A |
| **Availability** | 99.9% | 99.95% | 99.0% |
| **Data Freshness** | Real-time | <1 min | Daily |

## Disaster Recovery

- **Backup**: Daily snapshots of config DB, weekly for time-series (aggregated)
- **RTO (Recovery Time Objective)**: 4 hours for ground, N/A for edge (standalone)
- **RPO (Recovery Point Objective)**: 1 hour for critical data, 24 hours for non-critical
- **Failover**: Active-passive for ground services, automatic for edge (local redundancy)

## Related Documents

- **TWIN_SCOPE.md** - Use cases and operational modes
- **ASSUMPTIONS_LIMITATIONS.md** - Architecture assumptions and limitations
- **../02-MODELS/** - Model specifications and implementations
- **../03-INTERFACES_APIS/TWIN_API_SPEC.yaml** - API specification
- **../07-RUNTIME_DEPLOYMENT/** - Deployment profiles and security
- **../12-CODE/** - Implementation code and CI/CD
- **00-PROGRAM/DIGITAL_THREAD/03-ARCHITECTURE/** - Program-level digital thread architecture

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Digital Twin Team | Initial reference architecture |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
