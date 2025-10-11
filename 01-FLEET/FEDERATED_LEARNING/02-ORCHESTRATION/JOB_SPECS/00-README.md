# JOB_SPECS

Federated learning job specifications and configuration templates.

## Purpose

This directory contains FL job specifications that define training rounds, model configurations, hyperparameters, and data contracts for each federated learning experiment or production deployment.

## Contents

This directory contains the declarative control plane for federated learning jobs, including schemas, templates, examples, and validation tools.

### Directory Structure

```
JOB_SPECS/
├── REGISTRY/
│   └── index.yaml                    # Central job registry and catalog
├── SCHEMAS/
│   ├── job_spec.schema.json          # Job specification validation schema
│   ├── client_selector.schema.json   # Client selection configuration schema
│   └── rollout.schema.json           # Deployment rollout policy schema
├── TEMPLATES/
│   ├── train_job.example.yaml        # Training job template
│   ├── eval_job.example.yaml         # Evaluation job template
│   ├── aggregate_job.example.yaml    # Aggregation job template
│   ├── client_selector.example.yaml  # Client selector template
│   ├── rollout_policy.example.yaml   # Rollout policy template
│   └── schedule.cron.example.yaml    # Cron schedule template
├── K8S/
│   ├── argo_workflow.example.yaml    # Argo Workflows integration
│   └── cronjob.example.yaml          # Kubernetes CronJob example
├── EXAMPLES/
│   └── aircraft_accel_v1/            # Complete example: IMU drift detection
│       ├── job.yaml                  # Job specification
│       ├── selector.yaml             # Client selector
│       ├── rollout.yaml              # Rollout policy
│       └── schedule.yaml             # Training schedule
└── TESTS/
    └── validate_job_specs.py         # Validation script (CI/CD gatekeeper)
```

### Key Components

- **REGISTRY/index.yaml**: Central catalog of all jobs (active, draft, completed, failed) with metadata and references
- **SCHEMAS/**: JSON Schema definitions that enforce structure and validation
- **TEMPLATES/**: Production-ready templates for creating new jobs
- **K8S/**: Kubernetes/Argo orchestration examples showing how specs translate to execution
- **EXAMPLES/aircraft_accel_v1/**: End-to-end example for aircraft accelerometer drift prediction
- **TESTS/validate_job_specs.py**: Python script that validates all specs against schemas

### Quick Start

1. **Create a new job**: Copy from `TEMPLATES/train_job.example.yaml`
2. **Define client selection**: Use `TEMPLATES/client_selector.example.yaml`
3. **Set rollout policy**: Use `TEMPLATES/rollout_policy.example.yaml`
4. **Configure schedule**: Use `TEMPLATES/schedule.cron.example.yaml`
5. **Validate**: Run `python TESTS/validate_job_specs.py --path your-job.yaml`
6. **Deploy**: Submit to orchestrator after validation passes

## Job Specification Structure

### Required Fields

```yaml
job_metadata:
  job_id: <unique_identifier>
  name: <human_readable_name>
  description: <purpose_and_goals>
  owner: <team_or_person>
  created_at: <ISO8601_timestamp>
  
model_config:
  architecture: <model_type>
  version: <model_version>
  input_schema: <path_to_data_contract>
  output_schema: <path_to_output_spec>
  
training_config:
  algorithm: <FL_algorithm>
  hyperparameters: <dict_of_params>
  local_epochs: <int>
  batch_size: <int>
  
orchestration_config:
  schedule: <weekly|bi_weekly|on_demand>
  client_selection: <algorithm>
  min_clients: <int>
  max_clients: <int>
  
privacy_config:
  differential_privacy: <enabled|disabled>
  epsilon: <float>
  delta: <float>
  secure_aggregation: <enabled|disabled>
```

### Optional Fields

```yaml
deployment_config:
  canary_clients: <list_of_client_ids>
  rollout_strategy: <canary|blue_green|progressive>
  
validation_config:
  holdout_dataset: <path_or_reference>
  metrics: <list_of_metrics>
  thresholds: <dict_of_min_values>
  
compliance_config:
  certification_level: <DO-178C_level>
  audit_trail: <enabled|disabled>
  export_control: <ITAR|EAR|none>
```

## Job Lifecycle

### 1. Job Definition

**Created By**: AI/ML Team  
**Approval**: MAL-FE (Fleet Experiments) Policy (see [10-GOVERNANCE/MAL-FE/POLICY.md](10-GOVERNANCE/MAL-FE/POLICY.md))

### 2. Job Submission

**API Endpoint**: `/api/v1/jobs` (POST)  
**Authentication**: JWT token with FL_ENGINEER role  
**Validation**: Schema compliance, data contract verification

### 3. Job Scheduling

**Scheduler**: See 02-ORCHESTRATION/SCHEDULER.md  
**Client Selection**: See 02-ORCHESTRATION/CLIENT_SELECTION.md

### 4. Job Execution

**Orchestrator**: Distributed FL controller (Flower, PySyft, or custom)  
**Monitoring**: Real-time metrics to 12-METRICS/

### 5. Job Completion

**Artifacts**:
- Trained global model (versioned in 06-MODELS/REGISTRY.md)
- Training metrics (logged to 12-METRICS/TRAINING_METRICS.csv)
- Validation results (logged to 08-VALIDATION_VVP/)

**Approval for Deployment**:
- CCB approval required (see [10-GOVERNANCE/CCB_HANDOFF.md](10-GOVERNANCE/CCB_HANDOFF.md))
- Safety gate checks (see [08-VALIDATION_VVP/SAFETY_GATES.md](08-VALIDATION_VVP/SAFETY_GATES.md))

## Job Templates

### Predictive Maintenance Job

**Use Case**: Predict engine bearing failure 100 flight hours in advance

```yaml
job_metadata:
  job_id: pm-engine-bearing-v1
  name: "Predictive Maintenance - Engine Bearing Wear"
  description: "Binary classifier for engine bearing failure prediction"
  owner: "AI/ML Team - Predictive Maintenance"
  created_at: "2024-11-01T00:00:00Z"
  
model_config:
  architecture: "LSTM"
  version: "1.0.0"
  input_schema: "01-ARCHITECTURE/DATA_CONTRACTS/TELEMETRY_SCHEMA.yaml#engine_vibration"
  output_schema: "binary_classification"  # 0 = healthy, 1 = failure imminent
  
training_config:
  algorithm: "FedAvg"
  hyperparameters:
    learning_rate: 0.001
    optimizer: "Adam"
  local_epochs: 5
  batch_size: 32
  
orchestration_config:
  schedule: "weekly"
  client_selection: "random"
  min_clients: 10
  max_clients: 50
  
privacy_config:
  differential_privacy: true
  epsilon: 1.0
  delta: 1e-5
  secure_aggregation: false
```

### Anomaly Detection Job

**Use Case**: Detect sensor drift or system faults in real-time

```yaml
job_metadata:
  job_id: ad-sensor-drift-v1
  name: "Anomaly Detection - Sensor Drift"
  description: "Autoencoder for sensor anomaly detection"
  owner: "AI/ML Team - Safety Systems"
  created_at: "2024-11-01T00:00:00Z"
  
model_config:
  architecture: "Autoencoder"
  version: "1.0.0"
  input_schema: "01-ARCHITECTURE/DATA_CONTRACTS/TELEMETRY_SCHEMA.yaml#all_signals"
  output_schema: "reconstruction_error"
  
training_config:
  algorithm: "FedProx"
  hyperparameters:
    learning_rate: 0.0005
    optimizer: "SGD"
    mu: 0.01  # FedProx proximal term
  local_epochs: 10
  batch_size: 64
  
orchestration_config:
  schedule: "weekly"
  client_selection: "importance_sampling"
  min_clients: 15
  max_clients: 75
  
privacy_config:
  differential_privacy: true
  epsilon: 2.0
  delta: 1e-5
  secure_aggregation: true  # High sensitivity use case
```

## Job Validation

The validation script (`TESTS/validate_job_specs.py`) acts as a CI/CD gatekeeper to ensure all job specifications are well-formed before deployment.

### Usage

```bash
# Validate a specific job spec
python TESTS/validate_job_specs.py --path EXAMPLES/aircraft_accel_v1/job.yaml

# Validate all examples and templates
python TESTS/validate_job_specs.py --validate-all

# Validate with a specific schema
python TESTS/validate_job_specs.py --path job.yaml --schema job_spec
```

### Pre-Submission Checks

- [ ] **Schema validation**: YAML syntax correct, all required fields present
- [ ] **Data contract verification**: Input/output schemas exist and are valid
- [ ] **Hyperparameter sanity**: Learning rate, batch size within reasonable ranges
- [ ] **Privacy budget check**: ε and δ within approved limits (see [05-PRIVACY_SECURITY/DP_SGD.md](05-PRIVACY_SECURITY/DP_SGD.md))
- [ ] **Resource estimation**: Model size, memory, CPU fit client constraints

### Post-Submission Checks

- [ ] **MAL-FE approval**: Fleet experiments policy compliance
- [ ] **CCB review**: Configuration management approval (if production deployment)
- [ ] **Security review**: Export control, threat model assessment
- [ ] **Safety review**: No flight-critical system interference

## Federated Job Orchestration Workflow

This structure enables a powerful and automated workflow:

### 1. Definition
An ML engineer defines a new federated task by creating a set of spec files, starting from the TEMPLATES:

- **job.yaml**: Specifies the model to train (e.g., from the ONNX_MODELS registry), hyperparameters, and aggregation strategy. Crucially references a specific Data Contract (e.g., `aircraft_telemetry_v1:1.0.0`) to ensure data-model compatibility.
- **selector.yaml**: Defines which aircraft are eligible for the task (e.g., "all A320s with more than 100 hours of flight data in the last week").
- **rollout.yaml**: Controls the deployment strategy (e.g., "run on 10% of the selected fleet first, then expand to 100% if successful").
- **schedule.yaml**: Sets the trigger (e.g., a nightly cron schedule).

### 2. Validation
Before deployment, the `validate_job_specs.py` script is run (typically in CI/CD) to ensure all files are syntactically correct and adhere to the defined schemas. This prevents runtime errors due to misconfiguration.

### 3. Execution
The orchestrator (like Argo Workflows) reads the validated specs:
- Uses `selector.yaml` to query fleet status and compile a list of target clients
- Dispatches the training job according to the `rollout.yaml` policy
- Manages the entire process: sending the model to clients, waiting for local training, receiving encrypted model updates, and executing the aggregation job

### 4. Monitoring
The orchestrator tracks progress through:
- Real-time metrics to `12-METRICS/`
- Client participation and training loss
- Privacy budget consumption
- Model performance and drift detection

This declarative approach separates the "what" from the "how," making the entire federated learning system more robust, auditable, and scalable.

## Job Monitoring

### Real-Time Metrics

- **Client participation**: Count of active clients in current round
- **Training loss**: Per-client and global loss curves
- **Communication overhead**: Bytes uploaded/downloaded per client
- **Round time**: Duration from model distribution to aggregation

### Post-Training Metrics

- **Model accuracy**: Validation set performance
- **Fairness metrics**: Disaggregated performance by client group
- **Privacy budget consumed**: Cumulative ε and δ
- **Drift detection**: Model performance degradation over time

**Dashboards**: Grafana (see [12-METRICS/KPI_DEFINITIONS.md](12-METRICS/KPI_DEFINITIONS.md))

## Job Archiving

### Retention Policy

- **Active jobs**: Kept indefinitely (in production)
- **Completed jobs**: Archived after 2 years
- **Failed jobs**: Retained for 6 months (for postmortem analysis)
- **Experimental jobs**: Retained for 1 year

### Archive Location

- **Primary**: `06-MODELS/REGISTRY.md` (model artifacts)
- **Secondary**: `07-EXPERIMENTS/TRACKING.md` (experiment logs)
- **Backup**: Cold storage (S3 Glacier, Azure Cool Blob)

## Related Documents

- [**REGISTRY/index.yaml**](REGISTRY/index.yaml) - Central job registry
- [**SCHEMAS/**](SCHEMAS/) - JSON Schema validation definitions
- [**TEMPLATES/**](TEMPLATES/) - Job specification templates
- [**EXAMPLES/aircraft_accel_v1/**](EXAMPLES/aircraft_accel_v1/) - Complete example implementation
- [**K8S/**](K8S/) - Kubernetes/Argo orchestration examples
- [**TESTS/validate_job_specs.py**](TESTS/validate_job_specs.py) - Validation script
- [**SCHEDULER.md**](../SCHEDULER.md) - Training round scheduling
- [**CLIENT_SELECTION.md**](../CLIENT_SELECTION.md) - Client eligibility and fairness
- [**10-GOVERNANCE/MAL-FE/POLICY.md**](../../10-GOVERNANCE/MAL-FE/POLICY.md) - Fleet experiments approval process
- [**04-ALGORITHMS/**](../../04-ALGORITHMS/) - FL algorithms (FedAvg, FedProx, etc.)
- [**09-DEPLOYMENT/ROLLOUT_STRATEGY.md**](../../09-DEPLOYMENT/ROLLOUT_STRATEGY.md) - Deployment strategies

## Change History

| Version | Date    | Changes                     | Author    |
|---------|---------|----------------------------|-----------|
| 1.0     | 2024-Q4 | Initial job specs structure| AI/ML Team|
