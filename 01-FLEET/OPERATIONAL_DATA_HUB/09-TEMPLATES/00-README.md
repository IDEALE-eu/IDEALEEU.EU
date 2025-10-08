# TEMPLATES

**📍 [IDEALE-EU](../../../) > [01-FLEET](../../) > [OPERATIONAL_DATA_HUB](../) > TEMPLATES**

Standardized templates for schemas, contracts, reports, and processes.

## Purpose

Provides reusable templates to ensure consistency across:
- Telemetry schema definitions
- Anomaly reports
- Data sharing agreements
- Retention schedules
- Data contracts
- Schema change requests

## Contents

- [**00-README.md**](00-README.md) - This file
- [**TELEMETRY_SCHEMA_TEMPLATE.json**](TELEMETRY_SCHEMA_TEMPLATE.json) - Schema definition template
- [**ANOMALY_REPORT_TEMPLATE.yaml**](ANOMALY_REPORT_TEMPLATE.yaml) - Anomaly report format
- [**DATA_SHARING_AGREEMENT.md**](DATA_SHARING_AGREEMENT.md) - Data sharing template
- [**RETENTION_SCHEDULE_TEMPLATE.csv**](RETENTION_SCHEDULE_TEMPLATE.csv) - Retention policy template
- [**DATA_CONTRACT_TEMPLATE.yaml**](DATA_CONTRACT_TEMPLATE.yaml) - Standardized data contract
- [**SCHEMA_CHANGE_RFC.md**](SCHEMA_CHANGE_RFC.md) - Schema change request process

## Template Usage

### 1. Telemetry Schema Template

**Use Case**: Register new telemetry signal in Schema Registry

**Steps**:
1. Copy `TELEMETRY_SCHEMA_TEMPLATE.json`
2. Fill in signal details (name, type, unit, range, EBOM reference)
3. Validate schema with `avro-tools`
4. Submit PR to Schema Registry

**Reference**: [../02-DATA_INGESTION/SCHEMA_REGISTRY/](../02-DATA_INGESTION/SCHEMA_REGISTRY/00-README.md)

---

### 2. Anomaly Report Template

**Use Case**: Define anomaly output format for new detector

**Steps**:
1. Copy `ANOMALY_REPORT_TEMPLATE.yaml`
2. Customize fields for detector output
3. Document anomaly types and severity levels
4. Register format in data catalog

**Reference**: [../05-DATA_PRODUCTS/ANOMALY_REPORTS/](../05-DATA_PRODUCTS/00-README.md)

---

### 3. Data Sharing Agreement

**Use Case**: Share operational data with external partner

**Steps**:
1. Copy `DATA_SHARING_AGREEMENT.md`
2. Fill in partner details, data scope, terms
3. Review with legal and security teams
4. Obtain signatures and store in repository

**Reference**: [../04-DATA_SECURITY_COMPLIANCE/](../04-DATA_SECURITY_COMPLIANCE/00-README.md)

---

### 4. Retention Schedule Template

**Use Case**: Define custom retention policy for new data type

**Steps**:
1. Copy `RETENTION_SCHEDULE_TEMPLATE.csv`
2. Define retention periods per data category
3. Justify retention decisions
4. Submit for data steward approval

**Reference**: [../03-DATA_STORAGE/RETENTION_POLICY.md](../03-DATA_STORAGE/RETENTION_POLICY.md)

---

### 5. Data Contract Template

**Use Case**: Create data contract for new data product

**Steps**:
1. Copy `DATA_CONTRACT_TEMPLATE.yaml`
2. Define schema, SLA, quality guarantees
3. Identify consumers and stakeholders
4. Review with data steward and consumers
5. Publish contract in `../06-ANALYTICS_CONSUMPTION/DATA_CONTRACTS/`

**Reference**: [../06-ANALYTICS_CONSUMPTION/DATA_CONTRACTS/](../06-ANALYTICS_CONSUMPTION/DATA_CONTRACTS/)

---

### 6. Schema Change RFC

**Use Case**: Propose breaking change to existing schema

**Steps**:
1. Copy `SCHEMA_CHANGE_RFC.md`
2. Document change rationale and impact
3. Assess affected consumers
4. Submit ECR (Engineering Change Request)
5. Obtain CCB approval

**Reference**: [../07-INTEGRATIONS/CONFIG_MGMT_LINKS.md](../07-INTEGRATIONS/CONFIG_MGMT_LINKS.md)

## Template Governance

### Template Updates
- Templates versioned in Git
- Changes require PR + data steward approval
- Breaking changes to templates require ECR

### Template Compliance
- All new schemas/contracts must use templates
- Non-compliance flagged in PR reviews
- Template usage tracked as quality metric

## Quick Start Examples

### Create New Telemetry Schema
```bash
# Copy template
cp 09-TEMPLATES/TELEMETRY_SCHEMA_TEMPLATE.json my_signal.schema.json

# Edit with signal details
# ...

# Validate schema
avro-tools validate my_signal.schema.json

# Submit PR
git add my_signal.schema.json
git commit -m "Add new telemetry schema for my_signal"
git push
```

### Create New Data Contract
```bash
# Copy template
cp 09-TEMPLATES/DATA_CONTRACT_TEMPLATE.yaml my_product_contract.yaml

# Fill in product details
# ...

# Submit for review
git add my_product_contract.yaml
git commit -m "Add data contract for my_product"
git push
```

## Related Documents

- [**../02-DATA_INGESTION/SCHEMA_REGISTRY/**](../02-DATA_INGESTION/SCHEMA_REGISTRY/00-README.md) - Schema registration
- [**../06-ANALYTICS_CONSUMPTION/DATA_CONTRACTS/**](../06-ANALYTICS_CONSUMPTION/DATA_CONTRACTS/) - Data contracts
- [**../07-INTEGRATIONS/CONFIG_MGMT_LINKS.md**](../07-INTEGRATIONS/CONFIG_MGMT_LINKS.md) - Schema change process

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial template library        | Data Engineering Team |
