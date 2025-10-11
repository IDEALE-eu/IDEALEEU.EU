# 🔄 DIGITAL TWIN REPLAY

**Path**: `EVALUATION/replay_dt/`  
**Purpose**: Validate models using digital twin replay of historical scenarios

---

## 🎯 Overview

This directory contains **digital twin replay evaluation** results. Models are tested against simulated scenarios in the digital twin to validate performance before real-world deployment.

## 📂 Directory Structure

```
replay_dt/
├── scenarios/
│   ├── normal_operations/
│   ├── known_anomalies/
│   ├── edge_cases/
│   └── stress_tests/
├── results/
│   ├── scenario_001_results.json
│   ├── scenario_002_results.json
│   └── ...
├── reports/
│   ├── replay_summary_report.md
│   └── validation_dashboard.html
└── README.md (this file)
```

## 🎬 Replay Scenarios

### 1. Normal Operations

**Purpose**: Verify no false alarms during healthy operation

**Scenarios**:
- `normal_cruise_10hrs.parquet`: 10-hour cruise flight
- `normal_taxi_takeoff_landing.parquet`: Complete flight profile
- `normal_varying_rpm.parquet`: Variable engine speeds

**Expected Result**: Anomaly rate < 5%

---

### 2. Known Anomalies

**Purpose**: Verify detection of confirmed faults

**Scenarios**:
- `bearing_wear_progressive.parquet`: Gradual bearing degradation
- `blade_imbalance_sudden.parquet`: Sudden blade damage
- `mounting_looseness.parquet`: Loose engine mount

**Expected Result**: Detection within X minutes of fault onset

**Example**: `bearing_wear_progressive.parquet`
```
Timeline:
0:00 - Normal operation
2:00 - Bearing wear begins (subtle)
5:00 - Wear progresses (moderate)
8:00 - Wear severe
10:00 - Bearing failure

Expected Detection: By 6:00 (before severe stage)
```

---

### 3. Edge Cases

**Purpose**: Test boundary conditions

**Scenarios**:
- `high_altitude_low_temp.parquet`: -50°C, 45,000 ft
- `rapid_throttle_changes.parquet`: Aggressive power changes
- `turbulence_high_vibration.parquet`: Normal vibration in rough air

**Challenge**: Distinguish anomalies from extreme normal conditions

---

### 4. Stress Tests

**Purpose**: Test model under challenging conditions

**Scenarios**:
- `sensor_dropouts.parquet`: Intermittent sensor failures
- `noisy_data.parquet`: High sensor noise (SNR = 5 dB)
- `multiple_anomalies.parquet`: Multiple concurrent faults

---

## 📊 Evaluation Metrics

### Per-Scenario Metrics

**Example**: `scenario_001_results.json`
```json
{
  "scenario_id": "bearing_wear_progressive",
  "scenario_type": "known_anomaly",
  "duration_minutes": 10,
  "anomaly_onset": "2:00",
  "expected_detection": "6:00",
  
  "model_performance": {
    "first_detection": "5:30",
    "detection_latency_minutes": 3.5,
    "total_alerts": 15,
    "false_alerts": 2,
    "true_alerts": 13,
    "precision": 0.867,
    "recall": 1.0
  },
  
  "result": "PASS",
  "notes": "Detected 30 minutes before expected, acceptable latency"
}
```

### Aggregate Metrics

**Example**: `reports/replay_summary_report.md`
```markdown
# Digital Twin Replay Validation Report

**Model**: engine_vibration_detector v1.0.0
**Date**: 2025-10-11
**Scenarios Tested**: 25

## Summary

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Normal Ops FAR** | 2.5% | <5% | ✅ PASS |
| **Anomaly Detection Rate** | 92% | >85% | ✅ PASS |
| **Avg Detection Latency** | 4.2 min | <10 min | ✅ PASS |
| **Edge Case Robustness** | 88% | >80% | ✅ PASS |

## Scenario Results

- Normal Operations: 10/10 passed
- Known Anomalies: 9/10 passed (1 late detection)
- Edge Cases: 4/5 passed (1 false alarm in turbulence)
- Stress Tests: 2/5 passed (sensor dropout challenges)

## Recommendation

**Deploy to shadow mode** - Model passes validation criteria. Monitor stress test scenarios in production.
```

---

## 🚀 Running Replay Evaluation

### Run Single Scenario

```bash
python ../../PIPELINES/inference/batch/run_batch.py \
    --model ../../MODELS/engine_vibration_detector/1.0.0/ \
    --data scenarios/bearing_wear_progressive.parquet \
    --output results/scenario_001_results.json
```

### Run All Scenarios

```bash
python run_replay_evaluation.py \
    --model ../../MODELS/engine_vibration_detector/1.0.0/ \
    --scenarios scenarios/ \
    --output results/
```

### Generate Summary Report

```bash
python generate_replay_report.py \
    --results results/ \
    --output reports/replay_summary_report.md
```

---

## 🔍 Scenario Creation

### Creating New Scenarios

1. **From Historical Data**:
```bash
# Extract confirmed anomaly event
python extract_scenario.py \
    --flight FL20251005-042 \
    --start "14:30:00" \
    --duration 15 \
    --output scenarios/blade_damage_20251005.parquet
```

2. **From Digital Twin Simulation**:
```bash
# Run digital twin with seeded fault
python ../../DIGITAL_TWIN_MODEL/run_simulation.py \
    --config bearing_wear_config.yaml \
    --duration 20 \
    --output scenarios/bearing_wear_simulated.parquet
```

3. **Synthetic Edge Cases**:
```bash
# Generate synthetic challenging scenario
python generate_synthetic_scenario.py \
    --type "high_noise" \
    --duration 10 \
    --output scenarios/noisy_data_synthetic.parquet
```

---

## 📋 Scenario Library

### Available Scenarios

| ID | Name | Type | Duration | Fault Type |
|----|------|------|----------|------------|
| 001 | Bearing wear progressive | Known | 10 min | Bearing wear |
| 002 | Blade imbalance sudden | Known | 5 min | Blade damage |
| 003 | Normal cruise | Normal | 60 min | None |
| 004 | High altitude flight | Edge | 30 min | None |
| 005 | Sensor dropout | Stress | 15 min | Sensor fault |

**Total**: 25 scenarios (10 normal, 10 known, 5 edge, 5 stress)

---

## ✅ Validation Criteria

Model passes replay validation if:

- [ ] Normal ops FAR < 5%
- [ ] Anomaly detection rate > 85%
- [ ] Avg detection latency < 10 minutes
- [ ] Edge case robustness > 80%
- [ ] Zero critical missed detections (severity = severe)

---

## 📚 Related Documentation

- **Offline Evaluation**: `../offline/README.md`
- **Digital Twin Model**: `../../DIGITAL_TWIN_MODEL/README.md`
- **Batch Inference**: `../../PIPELINES/inference/batch/README.md`

---

**Owner**: Data Science Team + Digital Twin Team  
**Contact**: datascience@ideale.eu, digitaltwin@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Active 🟢
