# 🚨 DRIFT ALERTS

**Path**: `DRIFT_MONITORING/alerts/`  
**Purpose**: Store drift detection alerts and notifications

---

## 🎯 Overview

This directory stores **drift monitoring alerts** generated when data drift or concept drift is detected. Alerts trigger investigation and potential model retraining.

## 📂 Directory Structure

```
alerts/
├── data_drift/
│   ├── 2025-10-11_psi_alert.json
│   ├── 2025-10-12_ks_test_alert.json
│   └── ...
├── concept_drift/
│   ├── 2025-10-15_adwin_alert.json
│   ├── 2025-10-20_performance_alert.json
│   └── ...
├── drift_visualizations/
│   ├── feature_drift_heatmap_2025-10.png
│   ├── psi_trend_2025-10.png
│   └── ...
└── README.md (this file)
```

## 🔔 Alert Types

### 1. Data Drift Alerts

**Trigger**: Feature distribution changes (PSI > 0.25)

**Example**: `data_drift/2025-10-11_psi_alert.json`
```json
{
  "alert_id": "DRIFT_001_20251011",
  "alert_type": "data_drift",
  "detection_method": "PSI",
  "timestamp": "2025-10-11T14:30:00Z",
  "model_id": "ANOMALY_DETECTOR_ENGINE_VIB_V1.0.0",
  
  "drift_details": {
    "feature": "vib_fan_rms",
    "psi_score": 0.28,
    "threshold": 0.25,
    "severity": "WARNING"
  },
  
  "reference_period": ["2025-09-01", "2025-09-30"],
  "production_period": ["2025-10-01", "2025-10-11"],
  
  "statistics": {
    "reference_mean": 2.35,
    "production_mean": 2.58,
    "reference_std": 0.82,
    "production_std": 0.95,
    "shift_magnitude": "9.8%"
  },
  
  "actions_required": [
    "Investigate cause of distribution shift",
    "Review recent maintenance activities",
    "Check sensor calibration dates",
    "Consider retraining if drift persists >7 days"
  ],
  
  "notification_sent": {
    "email": ["datascience@ideale.eu"],
    "slack": ["#ml-alerts"],
    "pagerduty": false
  }
}
```

---

### 2. Concept Drift Alerts

**Trigger**: Model performance degradation (AUC < 0.85)

**Example**: `concept_drift/2025-10-15_adwin_alert.json`
```json
{
  "alert_id": "DRIFT_002_20251015",
  "alert_type": "concept_drift",
  "detection_method": "ADWIN",
  "timestamp": "2025-10-15T09:15:00Z",
  "model_id": "ANOMALY_DETECTOR_ENGINE_VIB_V1.0.0",
  
  "drift_details": {
    "metric": "reconstruction_error",
    "change_detected": true,
    "adwin_delta": 0.002,
    "severity": "CRITICAL"
  },
  
  "performance_degradation": {
    "baseline_auc": 0.92,
    "current_auc": 0.83,
    "degradation": "9.8%",
    "threshold": 0.85,
    "status": "BELOW_THRESHOLD"
  },
  
  "affected_segments": {
    "by_flight_phase": {
      "cruise": {"auc": 0.85, "degradation": "8.6%"},
      "takeoff": {"auc": 0.79, "degradation": "13.2%"}
    }
  },
  
  "actions_required": [
    "URGENT: Investigate performance drop",
    "Analyze recent false negatives",
    "Review labeled data for new fault types",
    "Initiate retraining workflow",
    "Consider rollback to previous version"
  ],
  
  "notification_sent": {
    "email": ["datascience@ideale.eu", "safety@ideale.eu"],
    "slack": ["#ml-alerts", "#safety-critical"],
    "pagerduty": true
  }
}
```

---

## 📊 Alert Severity Levels

| Severity | Trigger | Action | Notification |
|----------|---------|--------|--------------|
| **INFO** | Minor deviation | Log only | None |
| **WARNING** | Threshold exceeded | Monitor closely | Email |
| **CRITICAL** | Severe drift / performance drop | Immediate investigation | Email + Slack + PagerDuty |

---

## 🔍 Alert Investigation Workflow

### Step 1: Review Alert

```bash
# Read alert details
cat alerts/data_drift/2025-10-11_psi_alert.json
```

### Step 2: Visualize Drift

```bash
# Generate drift visualization
python ../../TOOLS/visualize_drift.py \
    --alert alerts/data_drift/2025-10-11_psi_alert.json \
    --output alerts/drift_visualizations/
```

**Output**: `feature_drift_heatmap_2025-10.png`

### Step 3: Root Cause Analysis

**Common Causes**:

1. **Data Drift**:
   - Sensor calibration drift
   - Fleet composition change (new aircraft/engine types)
   - Seasonal effects (temperature, humidity)
   - Operational changes (new flight routes, procedures)

2. **Concept Drift**:
   - New fault types emerging
   - Maintenance procedures changed
   - Label quality issues
   - Model degradation over time

### Step 4: Decide Action

**Decision Tree**:
```
Alert Received
    ↓
Severity CRITICAL?
    ├─ Yes → Immediate investigation
    │         ├─ Performance drop?
    │         │   ├─ Yes → Consider rollback
    │         │   └─ No → Continue monitoring
    │         └─ Initiate retraining
    │
    └─ No → Monitor for X days
            ├─ Drift persists?
            │   ├─ Yes → Initiate retraining
            │   └─ No → Resolve, close alert
            └─ Document findings
```

---

## 📈 Drift Trends Dashboard

**Location**: Grafana dashboard (internal)

**Metrics Tracked**:
- PSI trend (7-day, 30-day)
- Feature drift heatmap
- Performance metrics (AUC, FAR)
- Alert frequency
- Time-to-resolution

**Sample Dashboard Panels**:
```
┌─────────────────────────────────────┐
│  PSI Trend (Last 30 Days)           │
│  ┌───────────────────────────────┐  │
│  │         ··············· 0.25   │  │
│  │    ·····                       │  │
│  │ ···                            │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  Feature Drift Heatmap               │
│  ┌───────────────────────────────┐  │
│  │ vib_fan_rms       [  HIGH  ]   │  │
│  │ vib_compressor    [  LOW   ]   │  │
│  │ n1                [MEDIUM ]   │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

---

## 🔧 Alert Configuration

**Config**: `../../DRIFT_MONITORING/data_drift.yaml`

```yaml
alert_rules:
  - condition: psi > 0.25
    duration: 1 day
    action: warning_notification
    
  - condition: psi > 0.25
    duration: 7 days
    action: retraining_trigger
    
  - condition: auc < 0.85
    duration: 3 days
    action: critical_alert
```

---

## 📊 Alert Statistics (Example)

**October 2025**:
```
Total Alerts: 15
├─ Data Drift: 10
│  ├─ Resolved: 8
│  ├─ Under Investigation: 2
│  └─ Escalated: 0
│
├─ Concept Drift: 5
│  ├─ Resolved: 3
│  ├─ Under Investigation: 1
│  └─ Escalated: 1 (retraining initiated)
│
└─ False Alarms: 2 (13%)
```

**Mean Time to Resolution**: 3.5 days

---

## ✅ Alert Lifecycle

```
Alert Generated
    ↓
Notification Sent
    ↓
Investigation Started
    ↓
Root Cause Identified
    ↓
Action Taken
    ├─ Retraining
    ├─ Sensor Recalibration
    ├─ Threshold Adjustment
    └─ False Alarm (document)
    ↓
Alert Resolved
    ↓
Post-Mortem (if critical)
```

---

## 📚 Related Documentation

- **Data Drift Config**: `../data_drift.yaml`
- **Concept Drift Config**: `../concept_drift.yaml`
- **Retraining Pipeline**: `../../PIPELINES/training/README.md`
- **Model Registry**: `../../REGISTRY/README.md`

---

**Owner**: MLOps Team + Data Science Team  
**Contact**: mlops@ideale.eu, datascience@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
