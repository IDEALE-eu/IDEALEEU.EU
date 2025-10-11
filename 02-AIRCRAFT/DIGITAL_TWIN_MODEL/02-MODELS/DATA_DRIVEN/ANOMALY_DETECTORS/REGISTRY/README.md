# REGISTRY Directory

**Purpose**: Central catalog of all anomaly detection models, their status, and metadata.

## Contents

- **index.yaml**: Master registry of all models

## Registry Structure

The registry (`index.yaml`) tracks:

### Model Metadata
- Model ID, name, version
- Status (development, validation, shadow_mode, production, deprecated, retired)
- Criticality level (A, B, C, D per ARP4754A)
- ATA chapter and section

### Deployment Info
- Deployment date
- Environments (ground, edge, digital twin)
- Fleet coverage (% of aircraft)
- Aircraft count

### Paths
- Model file, scaler, signature, thresholds, metrics, card
- Data contract
- Training configuration

### Performance
- Key metrics (AUC, precision, recall, FAR, latency)
- Monitoring thresholds

### Ownership
- Model owner, domain expert, safety engineer
- Contact information

### Certification
- Requirements, hazards, certification memos
- Standards compliance

### Lifecycle
- Training date, validation date
- Shadow mode period
- Production release date
- Next review date
- Retraining schedule

## Model Statuses

| Status | Description | Deployment Allowed | Actions Enabled |
|--------|-------------|-------------------|-----------------|
| **development** | Model in active development | ❌ No | ❌ No |
| **validation** | Model undergoing validation | ❌ No | ❌ No |
| **shadow_mode** | Monitoring only, no actions | ✅ Yes | ❌ No |
| **production** | Fully operational | ✅ Yes | ✅ Yes |
| **deprecated** | Being phased out | ❌ No | ⚠️ Limited |
| **retired** | No longer in use | ❌ No | ❌ No |

## Criticality Levels (ARP4754A)

| Level | Description | Validation Requirements |
|-------|-------------|------------------------|
| **A** | Catastrophic | 5-fold CV, 30-day shadow (min 100 aircraft), FMEA+FTA, DO-178C Level A |
| **B** | Hazardous | 5-fold CV, 14-day shadow (min 50 aircraft), FMEA, DO-178C Level B |
| **C** | Major | 3-fold CV, 7-day shadow (min 20 aircraft), Hazard analysis |
| **D** | Minor | Test set validation, Offline validation sufficient |

## Usage

### Query Model Status
```bash
# Using yq (YAML query tool)
yq '.models[] | select(.model_id == "ANOMALY_DETECTOR_ENGINE_VIB_V1.0.0")' REGISTRY/index.yaml
```

### List Production Models
```bash
yq '.models[] | select(.status == "production") | .model_id' REGISTRY/index.yaml
```

### Find Models by ATA Chapter
```bash
yq '.models[] | select(.ata_chapter == "ATA-72")' REGISTRY/index.yaml
```

## Adding a New Model

1. Train and validate model
2. Export artifacts to `../MODELS/<detector>/<version>/`
3. Add entry to `index.yaml`:

```yaml
models:
  - model_id: ANOMALY_DETECTOR_MY_SYSTEM_V1.0.0
    model_name: My System Anomaly Detector
    version: 1.0.0
    status: development
    criticality: B
    ata_chapter: ATA-XX
    ata_section: XX-YY System
    
    deployment:
      deployed_date: null
      deployment_environments: []
      fleet_coverage: 0%
      aircraft_count: 0
    
    paths:
      model_file: MODELS/my_detector/1.0.0/model.onnx
      # ... other paths
    
    performance:
      auc: 0.XX
      # ... metrics
    
    # ... other sections
```

4. Update status as model progresses through lifecycle

## Status Transitions

```
development → validation → shadow_mode → production
                                ↓
                          deprecated → retired
```

**Approval Required**:
- `validation → shadow_mode`: Data Science Lead
- `shadow_mode → production`: CCB, Safety Engineer
- `production → deprecated`: CCB

## Integration

Registry is used by:
- CI/CD pipelines (deployment automation)
- Drift monitoring (performance tracking)
- Model governance (compliance audits)
- Operations dashboards (fleet health monitoring)

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
