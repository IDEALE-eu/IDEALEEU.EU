# DATA_CONTRACTS

Data schemas and contracts for federated learning telemetry and labels.

## Purpose

This directory defines standardized data contracts for telemetry signals, event labels, and model inputs/outputs. Data contracts ensure consistency across aircraft, ground stations, and simulation rigs, enabling reliable model training and inference.

## Contents

- [**00-README.md**](00-README.md) - This file
- [**REGISTRY/**](REGISTRY/) - Central registry of all data contracts
  - [**index.yaml**](REGISTRY/index.yaml) - Contract registry with metadata and governance
- [**TEMPLATES/**](TEMPLATES/) - Templates for creating new data contracts
  - [**data_contract.example.yaml**](TEMPLATES/data_contract.example.yaml) - Main contract template
  - [**schema.avsc**](TEMPLATES/schema.avsc) - Avro schema template
  - [**constraints.example.yaml**](TEMPLATES/constraints.example.yaml) - Quality constraints template
  - [**pii_map.example.yaml**](TEMPLATES/pii_map.example.yaml) - PII mapping template
  - [**dp_policy.example.yaml**](TEMPLATES/dp_policy.example.yaml) - Differential privacy policy template
  - [**slas.example.yaml**](TEMPLATES/slas.example.yaml) - Service level agreements template
  - [**messages.proto**](TEMPLATES/messages.proto) - Protocol Buffers schema template
- [**CONTRACTS/**](CONTRACTS/) - Registered data contracts
  - [**aircraft_telemetry_v1/1.0.0/**](CONTRACTS/aircraft_telemetry_v1/1.0.0/) - Aircraft telemetry contract
- **TELEMETRY_SCHEMA.yaml** - Legacy signal definitions (superseded by CONTRACTS/)
- **LABELS_EVENTS_SCHEMA.yaml** - Legacy event definitions (superseded by CONTRACTS/)

## Data Contract Principles

### Design Goals
1. **Alignment with EBOM** - Signal names match Engineering Bill of Materials identifiers
2. **Traceability** - Links to requirements, NCRs, and system specifications
3. **Versioning** - Semantic versioning for schema changes (v1.2.0)
4. **Backward compatibility** - Graceful handling of schema evolution
5. **Privacy by design** - No PII, pseudonymisation enforced

### Schema Governance
- **Owner**: AI/ML Team (Data Engineering)
- **Approver**: Configuration Control Board (CCB)
- **Review Cycle**: Quarterly or upon significant system changes
- **Change Process**: ECR (Engineering Change Request) required for breaking changes

## Data Contract System Architecture

The data contract system is the bedrock of trustworthy federated learning, providing:

### Contract Definition
Data owners define new contracts using **TEMPLATES/** which specify:
- **Schema**: Avro/Protobuf definitions for data structure
- **Constraints**: Quality rules (range, rate-of-change, consistency)
- **Privacy Policies**: PII mapping and differential privacy configuration
- **SLAs**: Availability, latency, and quality guarantees

### Validation & Registration
1. Contracts are **tested** using automated validation (e.g., `contract_test.py`)
2. Contracts pass **quality gates** (schema, privacy, security reviews)
3. Contracts are **registered** in `REGISTRY/index.yaml` with CCB approval

### Producer-Side Enforcement
On each aircraft (edge device), a client-side agent:
1. **Validates** local telemetry against the contract
2. **Quarantines** data that fails validation
3. **Applies** privacy policies (pseudonymization, DP)
4. **Ensures** only high-quality, compliant data is used for training

Example: `CONTRACTS/aircraft_telemetry_v1/1.0.0/tests/contract_test.py` validates:
- Schema compliance (Avro deserialization)
- Range constraints (e.g., engine temperature 0-1200°C)
- PII detection (no cleartext tail numbers)
- Completeness (max 5% missing per signal)

### Privacy by Design
The contract automatically configures FL clients to apply:
- **Pseudonymization**: `platform_id = SHA-256(tail_number + salt)`
- **Differential Privacy**: DP-SGD with ε=1.0, δ=1e-5
- **Data Minimization**: Exclude PII, only collect required signals

### Consumer-Side Trust
The central FL server aggregating model updates can trust:
- All clients provide data adhering to the **same standard**
- Data quality meets **SLA requirements** (>95% completeness, <1% errors)
- Privacy is **guaranteed** (DP, pseudonymization, no raw PII)

This prevents the "garbage in, garbage out" problem at massive scale across heterogeneous aircraft.

### Contract Lifecycle

```
1. DRAFT → 2. TEST → 3. REVIEW → 4. APPROVE → 5. ACTIVE → 6. DEPRECATED → 7. ARCHIVED
   ↓         ↓          ↓           ↓            ↓            ↓              ↓
   Template  Validation CCB/Privacy CCB         Production   Superseded     Retired
   Creation  Tests      Review      Approval     Use          by newer       (2+ years)
```

### Example: aircraft_telemetry_v1

The `CONTRACTS/aircraft_telemetry_v1/1.0.0/` contract demonstrates:

**Constraint Definition** (`constraints.yaml`):
- Engine exhaust gas temperature: 0-1200°C (physically plausible range)
- H2 tank pressure: 0-350 bar (per AS-5780 hydrogen storage standard)
- Rate-of-change: EGT max 100°C/s (detects abnormal combustion)

**Privacy Policy** (`pii_map.yaml`, `dp_policy.yaml`):
- Pseudonymize aircraft tail numbers via SHA-256
- Apply DP-SGD with ε=1.0 privacy budget
- Exclude crew/pilot PII entirely

**Validation** (`tests/contract_test.py`):
- Automated tests validate sample data (20/20 messages pass)
- Checks schema, constraints, PII detection, completeness
- Runs on edge devices before data enters training pipeline

## Schema Structure

### Telemetry Schema (TELEMETRY_SCHEMA.yaml)

Defines continuous sensor signals and system parameters:

```yaml
signals:
  - name: airspeed_indicated
    unit: knots
    sample_rate: 10 Hz
    range: [0, 350]
    ebom_ref: ATA-34-12-001
    description: Indicated airspeed from pitot-static system
```

### Labels Schema (LABELS_EVENTS_SCHEMA.yaml)

Defines discrete events, fault codes, and maintenance tags:

```yaml
events:
  - name: engine_oil_pressure_low
    code: ENG-001
    severity: warning
    ncr_link: NCR-2024-123
    description: Engine oil pressure below threshold
```

## Data Quality Requirements

### Completeness
- **Missing data**: Max 5% missing values per signal per flight
- **Interpolation**: Linear interpolation for gaps < 10 seconds
- **Imputation**: No imputation for gaps > 10 seconds (mark as missing)

### Accuracy
- **Sensor calibration**: Annual calibration records required
- **Outlier detection**: 3-sigma rule or IQR method
- **Validation**: Cross-check with redundant sensors (if available)

### Timeliness
- **Latency**: Telemetry timestamps within ±1 second of UTC
- **Synchronization**: GPS time sync required for all clients
- **Staleness**: Data older than 30 days flagged for retention review

## Privacy and Security

### Pseudonymisation
- **Aircraft ID**: `sha256(tail_number + salt)` - no clear-text tail numbers
- **Flight ID**: `sha256(flight_number + date + salt)`
- **Crew ID**: Not collected (no PII)

### Data Minimization
- Only signals relevant to FL use cases are collected
- Retention policy: 90 days for raw telemetry, 2 years for aggregated metrics

### Consent and Rights
- GDPR Art. 6(1)(f) - Legitimate interest (safety, maintenance optimization)
- Right to erasure: Clients can opt-out; gradients deleted within 30 days

## Integration Points

### Upstream Sources
- [**02-AIRCRAFT/DOMAIN_INTEGRATION/INFO_COMM_AVIONICS/**](02-AIRCRAFT/DOMAIN_INTEGRATION/INFO_COMM_AVIONICS/) -  Avionics data buses
- [**01-FLEET/OPERATIONAL_DATA_HUB/**](01-FLEET/OPERATIONAL_DATA_HUB/) -  Fleet telemetry aggregation
- [**00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/**](00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/) -  EBOM references

### Downstream Consumers
- [**03-CLIENTS/**](03-CLIENTS/) -  Client-side data ingestion and preprocessing
- [**04-ALGORITHMS/**](04-ALGORITHMS/) -  Feature engineering and model training
- [**06-MODELS/DATASETS_INDEX.md**](06-MODELS/DATASETS_INDEX.md) - Dataset provenance tracking

## Validation and Testing

### Schema Validation
- **Syntax**: YAML linting (yamllint)
- **Semantics**: Unit consistency, range checks
- **Compatibility**: Backward compatibility tests

### Data Validation
- **Pre-flight**: Schema compliance checks before aircraft deployment
- **Runtime**: Validation at data ingestion (client-side)
- **Post-flight**: Quality metrics reported to 12-METRICS/

## Related Documents

- [**FL_TOPOLOGY.md**](FL_TOPOLOGY.md) - Communication patterns for data transmission
- [**CLIENT_TYPES.md**](CLIENT_TYPES.md) - Client-specific data access permissions
- [**06-MODELS/DATASETS_INDEX.md**](06-MODELS/DATASETS_INDEX.md) - Dataset provenance and lineage
- [**11-COMPLIANCE/PRIVACY.md**](11-COMPLIANCE/PRIVACY.md) - GDPR compliance for telemetry data
- [**REGISTRY/index.yaml**](REGISTRY/index.yaml) - Contract registry with governance policies
- [**../02-ORCHESTRATION/**](../02-ORCHESTRATION/) - Integration with FL orchestration

## Integration with Orchestration

The `02-ORCHESTRATION` component uses data contracts to initiate and manage FL training jobs.

### Job Submission Workflow

1. **AI/ML Team defines FL job** in `02-ORCHESTRATION/JOB_SPECS/`:
   ```yaml
   job_metadata:
     job_id: "fl-pm-engine-oil-2024q4"
     name: "Predictive Maintenance - Engine Oil Pressure"
   
   model_config:
     architecture: "LSTM"
     input_schema: "01-ARCHITECTURE/DATA_CONTRACTS/CONTRACTS/aircraft_telemetry_v1/1.0.0/"
     # ↑ References the data contract
   
   training_config:
     algorithm: "FedAvg"
     local_epochs: 5
     batch_size: 32
   
   privacy_config:
     differential_privacy: true
     epsilon: 1.0  # Must match contract's dp_policy.yaml
   ```

2. **Orchestrator validates job against contract**:
   - Checks `data_contract.yaml` exists and is active
   - Verifies privacy budget (ε=1.0) matches `dp_policy.yaml`
   - Ensures SLAs in `slas.yaml` are achievable
   - Validates model input schema matches `schema.avsc`

3. **Scheduler selects training round time**:
   - Aligns with SATCOM windows (see `02-ORCHESTRATION/SCHEDULER.md`)
   - Ensures sufficient client availability per `CONNECTIVITY_PROFILES.md`

4. **Client selector identifies eligible clients**:
   - Checks data quality: clients must pass `contract_test.py` validation
   - Verifies constraint compliance rate > 99% (per `constraints.yaml`)
   - Ensures privacy budget not exhausted (tracks ε consumption per `dp_policy.yaml`)

5. **Model distribution to selected clients**:
   - Clients receive global model + contract reference
   - Clients validate local data against contract before training
   - Only compliant data enters local training loop

6. **Update collection**:
   - Clients upload gradients with DP noise (per `dp_policy.yaml`)
   - Gradients include validation report (from `contract_test.py`)
   - Server rejects updates from clients with low data quality

7. **Aggregation**:
   - Server weights updates by data quality score
   - Tracks cumulative privacy budget (ε consumed per round)
   - Halts training if privacy budget exhausted

8. **Validation**:
   - Model validated against holdout set (must match contract SLAs)
   - Checks for drift (model performance degradation)

9. **Deployment**:
   - If validation passes, new model distributed
   - Contract ensures reproducibility (same data standard across fleet)

### Example Orchestration Flow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Job Spec References Contract                             │
│    JOB_SPECS/predictive_maintenance.yaml                     │
│    → input_schema: "aircraft_telemetry_v1/1.0.0/"           │
└───────────────────┬─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Orchestrator Loads Contract                               │
│    CONTRACTS/aircraft_telemetry_v1/1.0.0/                    │
│    ├─ data_contract.yaml (metadata)                          │
│    ├─ constraints.yaml (quality rules)                       │
│    ├─ dp_policy.yaml (privacy config)                        │
│    └─ slas.yaml (performance targets)                        │
└───────────────────┬─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Client Selection (eligibility check)                      │
│    ✓ Data quality > 99% (per constraints.yaml)              │
│    ✓ Privacy budget available (ε remaining)                  │
│    ✓ Connectivity available (SATCOM window)                  │
│    → 30 clients selected from fleet of 100                   │
└───────────────────┬─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Client-Side Validation (before training)                  │
│    Each aircraft runs: tests/contract_test.py                │
│    ✓ Schema compliance (Avro)                                │
│    ✓ Range constraints (engine temp 0-1200°C)               │
│    ✓ No PII in cleartext                                     │
│    → Only valid data enters training                         │
└───────────────────┬─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Local Training with Privacy (per dp_policy.yaml)          │
│    ✓ Gradient clipping (max_norm=1.0)                       │
│    ✓ Noise addition (noise_multiplier=1.1)                  │
│    ✓ Privacy accounting (ε=0.02 per round)                  │
└───────────────────┬─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────────┐
│ 6. Aggregation with Quality Weighting                        │
│    Server receives 30 gradient updates                       │
│    ✓ Weight by data quality score                           │
│    ✓ Track cumulative privacy budget                        │
│    ✓ Verify SLA compliance (latency, throughput)            │
└───────────────────┬─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────────┐
│ 7. Model Deployment (if validation passed)                   │
│    New global model distributed to fleet                     │
│    Contract ensures consistent data quality across updates   │
└─────────────────────────────────────────────────────────────┘
```

### Contract Enforcement Points

| **Component** | **Contract File** | **Enforcement** |
|---------------|-------------------|-----------------|
| **Data Ingestion** | `schema.avsc` | Avro deserialization, type checking |
| **Quality Validation** | `constraints.yaml` | Range, rate-of-change, consistency checks |
| **Privacy Enforcement** | `pii_map.yaml`, `dp_policy.yaml` | Pseudonymization, DP-SGD noise |
| **SLA Monitoring** | `slas.yaml` | Latency, availability, quality metrics |
| **Client Selection** | `data_contract.yaml` | Eligibility based on quality score |
| **Aggregation** | `dp_policy.yaml` | Privacy budget tracking, gradient validation |

### Benefits of Contract-Driven Orchestration

1. **Reproducibility**: Same data standard ensures consistent model behavior
2. **Quality Assurance**: Only high-quality data enters training (>99% compliance)
3. **Privacy Guarantees**: Automated DP enforcement prevents privacy leaks
4. **Trust**: Server trusts client data without raw access
5. **Scalability**: Contracts scale to 100+ aircraft without manual validation
6. **Auditability**: Contract registry provides audit trail (ECR, CCB approval)

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|-----------------|
| 2.0     | 2025-10-11 | Add contract system (REGISTRY, TEMPLATES, CONTRACTS) | AI/ML Data Team |
| 1.0     | 2024-Q4 | Initial schema definitions       | AI/ML Data Team |

## Quick Start: Creating a New Contract

### 1. Copy Template
```bash
cd 01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/CONTRACTS/
cp -r ../TEMPLATES/ my_contract_v1/1.0.0/
cd my_contract_v1/1.0.0/
mv data_contract.example.yaml data_contract.yaml
mv constraints.example.yaml constraints.yaml
mv pii_map.example.yaml pii_map.yaml
mv dp_policy.example.yaml dp_policy.yaml
mv slas.example.yaml slas.yaml
```

### 2. Customize Contract
Edit `data_contract.yaml`:
- Update `contract_id`, `description`, `owner`
- Define signals in `schema.avsc`
- Specify quality rules in `constraints.yaml`
- Configure privacy in `pii_map.yaml` and `dp_policy.yaml`
- Set SLA targets in `slas.yaml`

### 3. Add Examples and Tests
- Create sample data in `examples/sample.jsonl`
- Write validation tests in `tests/contract_test.py`
- Run tests: `python3 tests/contract_test.py`

### 4. Submit for Review
- Create ECR (Engineering Change Request)
- Submit to CCB for approval
- Security and privacy team review
- Register in `REGISTRY/index.yaml` upon approval

### 5. Deploy to Production
- Clients download contract from registry
- Orchestrator references contract in job specs
- Automated validation enforced at edge devices
