# PLUMA Workflow Hooks - AAMMPP

**PLUMA** = Product Lifecycle User Made Automation

This directory contains workflow automation specifications for AAMMPP platform events.

---

## Overview

PLUMA workflows automate key processes in the AAMMPP lifecycle:
- RFQ creation and TFA classification
- Asset receipt and certification validation
- Service bulletin notifications
- Quote expiry and re-sourcing
- Maintenance scheduling
- Component exchange tracking

---

## Workflow Architecture

```
Event → PLUMA Hook → Workflow Engine → Actions → State Update
```

### Components
1. **Event Sources**: RFQ creation, asset receipt, SB issuance, time-based triggers
2. **PLUMA Hooks**: Event listeners defined in this directory
3. **Workflow Engine**: Executes automation logic
4. **Actions**: Update UTCS, send notifications, trigger QSH jobs
5. **State Update**: Reflect changes in asset passports and system state

---

## Available Workflows

### 1. RFQ Creation Workflow
**Trigger:** New RFQ created in procurement system  
**File:** [rfq-creation-workflow.yaml](rfq-creation-workflow.yaml)

**Actions:**
- Auto-generate UTCS draft passport (QS state)
- Classify component into TFA domain
- Create digital passport badge
- Initialize procurement tracking
- Notify potential suppliers

**Example:**
```yaml
trigger:
  event: rfq.created
  source: /02-PROCUREMENT/RFQ/
actions:
  - create_utcs_draft:
      state: QS
      tfa_domain: auto_classify(component_description)
  - generate_badge:
      format: AAMMPP-{TFA}-{TYPE}-{ID}
  - notify_suppliers:
      count: 3
      criteria: [tfa_expertise, rating, location]
```

### 2. Asset Receipt Workflow
**Trigger:** Component received at warehouse  
**File:** [asset-receipt-workflow.yaml](asset-receipt-workflow.yaml)

**Actions:**
- Validate airworthiness certificates (FAA 8130-3, EASA Form 1)
- Update UTCS passport with serial number (QS→UE transition)
- Trigger MRO baseline inspection
- Update inventory system
- Link to A360Exchanges-TT if applicable

**Example:**
```yaml
trigger:
  event: asset.received
  source: /04-LOGISTICS/TRACKING/
actions:
  - validate_certificates:
      required: [FAA_8130-3, EASA_FORM_1]
      fail_action: quarantine
  - update_utcs:
      lifecycle_state: UE
      asset_identity.serial_number: from_receipt_doc
  - schedule_baseline_inspection:
      type: initial_acceptance
      due_days: 7
```

### 3. Service Bulletin Notification Workflow
**Trigger:** New service bulletin issued by OEM  
**File:** [service-bulletin-workflow.yaml](service-bulletin-workflow.yaml)

**Actions:**
- Scan UTCS registry for affected components
- Notify operators and MRO providers
- Create compliance tracking records
- Schedule maintenance actions
- Update asset passports with SB applicability

**Example:**
```yaml
trigger:
  event: service_bulletin.issued
  source: /03-MAINTENANCE/SERVICE_BULLETINS/
actions:
  - scan_registry:
      filter:
        part_number_prefix: from_sb.applicability
        lifecycle_state: [UE, FE, CB]
  - notify_stakeholders:
      recipients: [operators, mro_providers]
      urgency: from_sb.category
  - update_compliance:
      add_sb: from_sb.number
      schedule_compliance_check: true
```

### 4. Quote Expiry Re-sourcing Workflow
**Trigger:** Quote expiry date approaching or passed  
**File:** [quote-expiry-workflow.yaml](quote-expiry-workflow.yaml)

**Actions:**
- Identify expiring quotes
- Re-run QSH optimization job
- Request new quotes from suppliers
- Update UTCS passport with new quote data
- Notify procurement team

**Example:**
```yaml
trigger:
  event: quote.expiring
  schedule: daily_check
  condition: quote_valid_until < (now + 7_days)
actions:
  - trigger_qsh_job:
      job_type: sourcing_optimization
      include_new_suppliers: true
  - request_quotes:
      suppliers: from_qsh.recommendations
      component_spec: from_utcs
  - notify_procurement:
      urgency: medium
      action_required: review_quotes
```

### 5. MRO Exchange Workflow
**Trigger:** Component exchange requested  
**File:** [mro-exchange-workflow.yaml](mro-exchange-workflow.yaml)

**Actions:**
- Verify replacement component compatibility
- Update custody chain in UTCS
- Create exchange record with traceability
- Update maintenance records
- Trigger A360Exchanges-TT transaction if marketplace-sourced

**Example:**
```yaml
trigger:
  event: mro.exchange_requested
  source: /03-MAINTENANCE/EXCHANGES/
actions:
  - verify_compatibility:
      original: from_request.original_component
      replacement: from_request.replacement_component
      check: [part_number, interchangeability, certification]
  - update_custody:
      original: mark_removed
      replacement: mark_installed
  - create_exchange_record:
      include: [removal_reason, replacement_sn, technician, timestamp]
  - update_aircraft_config:
      registration: from_request.aircraft
      position: from_request.location
```

### 6. Predictive Maintenance Workflow
**Trigger:** Quantum optimization recommends maintenance  
**File:** [predictive-maintenance-workflow.yaml](predictive-maintenance-workflow.yaml)

**Actions:**
- Analyze QB recommendations from QSH jobs
- Schedule maintenance if confidence > threshold
- Reserve replacement parts
- Notify maintenance planning
- Update asset passport with prediction

**Example:**
```yaml
trigger:
  event: quantum.recommendation
  source: /08-QUANTUM/RESULTS/
  condition: recommendation_type == "maintenance"
actions:
  - evaluate_recommendation:
      confidence_threshold: 0.75
      cost_benefit_analysis: true
  - schedule_maintenance:
      if: confidence > threshold
      type: from_recommendation.maintenance_type
      due_date: from_recommendation.suggested_date
  - reserve_parts:
      components: from_recommendation.parts_list
      warehouse: closest_to_aircraft
```

---

## Workflow Execution

### Synchronous Workflows
Execute immediately and block until complete:
- Certificate validation
- TFA classification
- Custody chain updates

### Asynchronous Workflows
Execute in background:
- QSH job triggering
- Supplier notifications
- Report generation

### Scheduled Workflows
Execute on schedule:
- Quote expiry checks (daily)
- Inspection due reminders (daily)
- Performance metrics (weekly)

---

## State Transitions

PLUMA workflows manage QS→QB state transitions:

```
QS (Superposition)
  ↓ [RFQ Created] → PLUMA: Initialize passport
FWD (Forward Wave)
  ↓ [Quotes Received] → PLUMA: Analyze quotes, run QSH
UE (Unit Element)
  ↓ [Asset Received] → PLUMA: Validate, serialize
FE (Federation)
  ↓ [In Service] → PLUMA: Coordinate updates
CB (Classical Bit)
  ↓ [Event Occurred] → PLUMA: Crystallize state
QB (Qubit)
  ↓ [Optimization] → PLUMA: Apply recommendations
```

---

## Integration Points

### UTCS Registry
All workflows read/write to UTCS registry:
```
/01-ASSETS/UTCS_REGISTRY/
```

### Procurement System
Workflows integrate with:
```
/02-PROCUREMENT/RFQ/
/02-PROCUREMENT/PO/
/02-PROCUREMENT/SUPPLIERS/
```

### Maintenance System
Workflows integrate with:
```
/03-MAINTENANCE/MRO_WORK_ORDERS/
/03-MAINTENANCE/EXCHANGES/
/03-MAINTENANCE/SERVICE_BULLETINS/
```

### Quantum Engine
Workflows trigger and consume:
```
/08-QUANTUM/QSH_JOBS/
/08-QUANTUM/RESULTS/
```

### A360Exchanges-TT
Workflows synchronize with marketplace:
```
/10-BUSINESS/A360-EXCHANGES-TT/
```

---

## Configuration

### Workflow Configuration File
Each workflow has a YAML configuration:

```yaml
workflow:
  name: "RFQ Creation Workflow"
  version: "1.0.0"
  enabled: true
  priority: high

trigger:
  event: "rfq.created"
  source: "/02-PROCUREMENT/RFQ/"
  
conditions:
  - field: "procurement_type"
    operator: "in"
    value: ["new_buy", "replacement"]

actions:
  - action: "create_utcs_draft"
    parameters:
      state: "QS"
      tfa_domain: "{{ auto_classify(description) }}"
    
  - action: "notify_suppliers"
    parameters:
      count: 3
      criteria: ["rating", "location"]
    retry:
      max_attempts: 3
      backoff: exponential

notifications:
  on_success:
    - recipient: "procurement@example.com"
      template: "rfq_created"
  on_failure:
    - recipient: "admin@example.com"
      template: "workflow_failed"

metrics:
  track:
    - execution_time
    - success_rate
    - error_count
```

---

## Error Handling

### Retry Logic
- Transient failures: exponential backoff (3 attempts)
- Network errors: retry with 1s, 5s, 15s delays
- Validation errors: fail immediately, notify admin

### Rollback
- Failed workflows trigger rollback actions
- UTCS updates are transactional
- State changes can be reverted

### Alerts
- Critical failures: immediate email/SMS
- Repeated failures: escalate to admin
- Metrics anomalies: warning alerts

---

## Monitoring

### Workflow Metrics
- Execution count by workflow type
- Average execution time
- Success/failure rates
- Error types and frequencies

### Dashboard
View metrics at:
```
/00-PROGRAM/DIGITAL_THREAD/10-METRICS/PLUMA_WORKFLOWS/
```

---

## Development

### Creating New Workflows

1. **Define Trigger:**
```yaml
trigger:
  event: "custom.event"
  source: "/path/to/source/"
```

2. **Specify Actions:**
```yaml
actions:
  - action: "custom_action"
    parameters:
      param1: value1
```

3. **Add Validation:**
```yaml
validation:
  - required_fields: [field1, field2]
  - field_constraints:
      field1:
        type: string
        pattern: "^[A-Z]{3}-[0-9]+$"
```

4. **Test Workflow:**
```bash
pluma test workflow-name.yaml --dry-run
```

5. **Deploy:**
```bash
pluma deploy workflow-name.yaml
```

---

## Security

### Access Control
- Workflows run with service account credentials
- API keys stored in secure vault
- Audit log of all workflow executions

### Data Protection
- Sensitive data encrypted in transit and at rest
- PII handling complies with GDPR
- Export control checks for ITAR components

---

## References

- [PLUMA Framework](../../PLUMA/)
- [UTCS Registry](../../01-ASSETS/UTCS_REGISTRY/)
- [QS Framework](../../QS_FRAMEWORK/)
- [A360Exchanges-TT](../../../../10-BUSINESS/A360-EXCHANGES-TT/)

---

**Owner:** AAMMPP Platform Team  
**Last Updated:** 2025-10-18  
**Next Review:** 2025-11-18
