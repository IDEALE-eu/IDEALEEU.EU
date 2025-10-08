# ANALYTICS_CONSUMPTION

**📍 [IDEALE-EU](../../../) > [01-FLEET](../../) > [OPERATIONAL_DATA_HUB](../) > ANALYTICS_CONSUMPTION**

Data consumption layer with contracts, APIs, and integration specifications.

## Purpose

Defines how downstream consumers access and use operational data:
- **Data Contracts**: SLAs and schemas per data product
- **Federated Learning Inputs**: Training data for FL models
- **Digital Twin Retraining**: Real-world data feedback
- **MRO Prediction Feed**: Predictive maintenance integration
- **Design Feedback Packs**: Performance data for next-gen design

## Contents

- [**00-README.md**](00-README.md) - This file
- [**DATA_CONTRACTS/**](DATA_CONTRACTS/) - Per-product data contracts
  - **usage_profiles_contract.yaml**
  - **anomaly_feed_contract.yaml**
- [**FEDERATED_LEARNING_INPUTS/**](FEDERATED_LEARNING_INPUTS/) - → [../FEDERATED_LEARNING/](../../FEDERATED_LEARNING/)
- [**DIGITAL_TWIN_RETRAINING/**](DIGITAL_TWIN_RETRAINING/) - Digital twin model updates
- [**MRO_PREDICTION_FEED/**](MRO_PREDICTION_FEED/) - Maintenance prediction data
- [**DESIGN_FEEDBACK_PACKS/**](DESIGN_FEEDBACK_PACKS/) - Design engineering insights

## Data Contracts

See [**DATA_CONTRACTS/**](DATA_CONTRACTS/)

**Purpose**: Explicit agreements between data producers and consumers

**Contract Elements**:
- **Schema**: Field definitions, types, ranges
- **SLA**: Refresh frequency, latency, availability
- **Quality Guarantees**: Completeness, accuracy, timeliness
- **Compatibility**: Backward/forward compatibility policy
- **Deprecation**: Notice period before removal

**Example Contract**:
```yaml
# usage_profiles_contract.yaml
product: usage_profiles
version: 1.2.0
owner: Data Engineering Team

consumers:
  - Fleet Operations Dashboard
  - ML Training Pipeline
  - Performance Analysis Team

sla:
  refresh_frequency: daily
  max_latency: 24 hours
  availability: 99.5%
  data_quality_threshold: 99%

schema:
  format: parquet
  compression: snappy
  location: s3://ideale-curated/usage_profiles/
  partitioning: dt=YYYY-MM-DD

  fields:
    - name: date
      type: date
      nullable: false
    - name: platform_id
      type: string
      nullable: false
    - name: flight_hours
      type: double
      range: [0, 24]
    - name: fuel_consumed_kg
      type: double
      range: [0, 50000]

backward_compatibility: FULL
deprecation_notice_days: 90
```

## Consumption Patterns

### Batch Consumption
- **Use Case**: Daily reports, trend analysis
- **Access Method**: S3 batch read (Spark, Pandas)
- **Latency**: Hours to days
- **Example**: Fleet performance dashboard

### Streaming Consumption
- **Use Case**: Real-time alerts, live monitoring
- **Access Method**: Kafka consumer
- **Latency**: Seconds
- **Example**: Anomaly alerting system

### API Consumption
- **Use Case**: Ad-hoc queries, external integrations
- **Access Method**: REST API
- **Latency**: Sub-second to seconds
- **Example**: Third-party analytics tools

## Consumer Integration Specifications

### Federated Learning Inputs

See [**FEDERATED_LEARNING_INPUTS/**](FEDERATED_LEARNING_INPUTS/)

**Purpose**: Provide training data for FL models

**Data Flow**:
```
Operational Data Hub
  → Curated Datasets
  → Privacy-Preserving Aggregation
  → Federated Learning Inputs
  → FL Training Pipeline
```

**Contract**: See [../FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/](../../FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/)

---

### Digital Twin Retraining

See [**DIGITAL_TWIN_RETRAINING/**](DIGITAL_TWIN_RETRAINING/)

**Purpose**: Update digital twin models with real-world data

**Data Flow**:
```
Operational Data Hub
  → Anomalies + Performance Deltas
  → Digital Twin Parameter Tuning
  → Updated Digital Twin Models
```

**Integration**: [../../00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/](../../../00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/)

---

### MRO Prediction Feed

See [**MRO_PREDICTION_FEED/**](MRO_PREDICTION_FEED/)

**Purpose**: Feed predictive maintenance models

**Data Flow**:
```
Operational Data Hub
  → Anomaly Reports + Reliability Datasets
  → MRO Prediction Models
  → Maintenance Recommendations
```

**Integration**: [../../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/](../../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/)

---

### Design Feedback Packs

See [**DESIGN_FEEDBACK_PACKS/**](DESIGN_FEEDBACK_PACKS/)

**Purpose**: Inform next-generation design

**Data Flow**:
```
Operational Data Hub
  → Performance Benchmarks + Failure Modes
  → Design Engineering Analysis
  → Updated Requirements / FMEA
```

**Integration**: [../../00-PROGRAM/REQUIREMENTS/](../../../00-PROGRAM/REQUIREMENTS/) and [../../02-AIRCRAFT/](../../../02-AIRCRAFT/)

## Data Access APIs

### REST API Endpoints

```
# List available data products
GET /api/v1/data-products

# Get data product schema
GET /api/v1/data-products/{product_id}/schema

# Query data product
POST /api/v1/data-products/{product_id}/query
Body: {
  "date_range": ["2024-01-01", "2024-01-31"],
  "filters": {"platform_id": "AC-H2-001"},
  "format": "json"
}

# Get data contract
GET /api/v1/contracts/{product_id}

# Subscribe to streaming updates
POST /api/v1/subscriptions
Body: {
  "product_id": "anomaly_reports",
  "webhook_url": "https://consumer.example.com/webhook"
}
```

### Python SDK

```python
from ideale_data_hub import DataHubClient

# Initialize client
client = DataHubClient(api_key="your_api_key")

# Query data product
df = client.get_data_product(
    product_id="usage_profiles",
    date_range=("2024-01-01", "2024-01-31"),
    filters={"platform_id": "AC-H2-001"}
)

# Stream real-time data
for anomaly in client.stream("anomaly_reports"):
    process_anomaly(anomaly)
```

## Consumer Onboarding

### Step 1: Discover Data Products
- Browse data catalog
- Review available data products
- Check data contracts and schemas

### Step 2: Request Access
- Submit access request via RBAC matrix
- Specify use case and justification
- Obtain manager approval

### Step 3: Integrate
- Implement data consumer using SDK or API
- Test with sample data
- Deploy to production

### Step 4: Monitor Usage
- Track data quality metrics
- Monitor query performance
- Report issues to data steward

## Monitoring and SLA Enforcement

**Consumer Metrics**:
- Query latency (p50, p95, p99)
- Data freshness (time since last refresh)
- Error rate (failed queries)
- Data quality scores

**Producer Metrics**:
- SLA compliance rate
- Data product availability
- Schema drift incidents
- Consumer satisfaction (NPS)

**Alerts**:
- SLA violation (latency, availability)
- Data quality below threshold
- Contract breaking change detected

## Related Documents

- [**../05-DATA_PRODUCTS/**](../05-DATA_PRODUCTS/00-README.md) - Data product catalog
- [**../07-INTEGRATIONS/**](../07-INTEGRATIONS/00-README.md) - Integration specifications
- [**../../FEDERATED_LEARNING/**](../../FEDERATED_LEARNING/) - FL integration
- [**../../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/**](../../MRO_STRATEGY/04-PREDICTIVE_MAINTENANCE/) - Maintenance integration

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial consumption layer       | Data Engineering Team |
