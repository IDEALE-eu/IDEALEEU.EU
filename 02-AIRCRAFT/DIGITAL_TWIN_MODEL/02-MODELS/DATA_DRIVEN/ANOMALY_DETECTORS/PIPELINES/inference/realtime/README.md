# 📡 REAL-TIME INFERENCE

**Path**: `PIPELINES/inference/realtime/`  
**Purpose**: Real-time anomaly detection from streaming sensor data

---

## 🎯 Overview

This directory contains scripts and configurations for **real-time inference** on streaming sensor data from aircraft via MQTT/data bus integration.

## 📂 Contents

```
realtime/
├── configs/
│   ├── realtime_config.yaml     # Real-time inference configuration
│   └── mqtt_config.yaml         # MQTT broker settings
├── adapter_databus.py           # Data bus adapter (MQTT/ARINC/AFDX)
├── inference_service.py         # Inference service (loads model, runs predictions)
├── alerting.py                  # Alert generation and dispatch
├── monitoring.py                # Performance monitoring
└── README.md (this file)
```

## 🔄 Real-Time Architecture

```
Aircraft Sensors → Data Bus (ARINC/AFDX) → Ground Station
                                                ↓
                                           MQTT Broker
                                                ↓
                                      adapter_databus.py
                                                ↓
                                   Windowing + Preprocessing
                                                ↓
                                      inference_service.py
                                                ↓
                                        ONNX Model Inference
                                                ↓
                                         Anomaly Score
                                                ↓
                            ┌───────────────────┴──────────────────┐
                            ↓                                      ↓
                       Threshold Check                        Log to Database
                            ↓
                       Alert Generated
                            ↓
               ┌────────────┼────────────┐
               ↓            ↓            ↓
           Email        Slack       MRO System
```

## 📝 Script Descriptions

### `adapter_databus.py`

**Purpose**: Connect to data bus and ingest streaming data

**Features**:
- MQTT subscriber for aircraft telemetry
- Data validation against contract
- Buffer management (10s windows)
- Preprocessing (outlier removal, interpolation)

**Usage**:
```bash
python adapter_databus.py --config configs/realtime_config.yaml
```

**What it does**:
1. Connects to MQTT broker
2. Subscribes to aircraft topics (e.g., `aircraft/AC001/engine/vibration`)
3. Buffers incoming data (10-second sliding window)
4. Validates data quality
5. Passes windows to inference service

---

### `inference_service.py`

**Purpose**: Run ONNX model inference on streaming windows

**Features**:
- ONNX model loading
- Real-time feature extraction
- Anomaly scoring
- Latency tracking (<50ms target)

**Usage**:
```bash
python inference_service.py --config configs/realtime_config.yaml
```

**What it does**:
1. Loads ONNX model and scaler
2. Receives window from adapter
3. Extracts features (RMS, FFT, etc.)
4. Normalizes features
5. Runs ONNX inference
6. Computes anomaly score
7. Compares to threshold
8. Triggers alert if anomaly detected

---

### `alerting.py`

**Purpose**: Generate and dispatch alerts

**Features**:
- Multi-channel alerting (email, Slack, PagerDuty)
- Alert deduplication (cooldown period)
- Severity-based routing
- Alert history logging

**Alert Levels**:
| Severity | Threshold | Action |
|----------|-----------|--------|
| Minor | 3.5-5.0 | Log only |
| Moderate | 5.0-8.0 | Email maintenance team |
| Severe | >8.0 | PagerDuty on-call, email safety team |

---

### `monitoring.py`

**Purpose**: Monitor inference performance

**Metrics Tracked**:
- **Latency**: Inference time per window (target: <50ms)
- **Throughput**: Windows processed per second
- **Error Rate**: Failed inferences
- **Anomaly Rate**: % of windows flagged as anomalous
- **Model Drift**: Feature distribution drift (PSI)

**Dashboard**: Grafana dashboard showing real-time metrics

---

## ⚙️ Configuration

### `realtime_config.yaml`

```yaml
model:
  path: ../../MODELS/engine_vibration_detector/1.0.0/
  onnx_file: model.onnx
  scaler_file: scaler.pkl
  thresholds_file: thresholds.yaml

data:
  contract: ../../DATA/contracts/signals_engine_vibration.yaml
  window_size_seconds: 10
  buffer_size: 20  # Max windows in buffer

inference:
  batch_size: 1  # Real-time, no batching
  max_latency_ms: 50
  num_threads: 4

alerting:
  enabled: true
  channels:
    - email
    - slack
  cooldown_period_seconds: 300  # 5 min between alerts
  
monitoring:
  enabled: true
  log_interval_seconds: 60
  metrics_endpoint: http://prometheus:9090
```

### `mqtt_config.yaml`

```yaml
mqtt:
  broker: mqtt.ideale.eu
  port: 1883
  use_tls: true
  username: ${MQTT_USER}
  password: ${MQTT_PASSWORD}
  
  topics:
    - aircraft/+/engine/vibration
    - aircraft/+/engine/parameters
  
  qos: 1  # At least once delivery
  keepalive: 60
```

---

## 🚀 Quick Start

### 1. Start Inference Service

```bash
# Terminal 1: Start inference service
python inference_service.py --config configs/realtime_config.yaml

# Terminal 2: Start data adapter
python adapter_databus.py --config configs/realtime_config.yaml
```

### 2. Verify Operation

```bash
# Check logs
tail -f logs/inference_service.log

# Check metrics
curl http://localhost:8080/metrics
```

### 3. Test with Simulated Data

```bash
# Send test data via MQTT
python ../../TOOLS/simulate_stream.py \
    --aircraft AC001 \
    --duration 60 \
    --anomaly-at 30  # Inject anomaly at 30s
```

---

## 📊 Performance Requirements

| Metric | Target | Current |
|--------|--------|---------|
| **Latency (p50)** | <20ms | 12ms |
| **Latency (p99)** | <50ms | 25ms |
| **Throughput** | >100 windows/s | 150 windows/s |
| **Availability** | >99.9% | 99.95% |
| **False Alarm Rate** | <5% | 2.7% |

---

## 🔍 Monitoring & Debugging

### Check Inference Logs

```bash
tail -f logs/inference_service.log
```

**Example Output**:
```
2025-10-11 14:30:00 INFO: Window AC001_1728655800 received
2025-10-11 14:30:00 INFO: Features extracted (9 features)
2025-10-11 14:30:00 INFO: Inference latency: 12.3ms
2025-10-11 14:30:00 INFO: Anomaly score: 2.1 (threshold: 3.5)
2025-10-11 14:30:00 INFO: Result: NORMAL
```

### Check Metrics

```bash
curl http://localhost:8080/metrics
```

**Example Response**:
```json
{
  "inference_count": 45678,
  "latency_ms": {
    "p50": 12.1,
    "p95": 18.5,
    "p99": 24.8
  },
  "anomaly_rate": 0.027,
  "error_rate": 0.001,
  "uptime_seconds": 86400
}
```

---

## 🆘 Troubleshooting

### Issue: High Latency

**Possible Causes**:
- Model too large
- CPU overloaded
- Network delays

**Action**:
1. Check CPU usage (`top`, `htop`)
2. Optimize model (quantization, pruning)
3. Use GPU acceleration
4. Scale horizontally (multiple inference servers)

### Issue: Connection Drops

**Possible Causes**:
- MQTT broker issues
- Network instability
- Authentication failure

**Action**:
1. Check MQTT broker status
2. Verify credentials
3. Review network logs
4. Implement reconnection logic

### Issue: Alert Spam

**Possible Causes**:
- Threshold too low
- Transient events triggering alerts
- No cooldown period

**Action**:
1. Increase threshold
2. Implement persistence filter (3 consecutive anomalies)
3. Increase cooldown period

---

## 📚 Related Documentation

- **Batch Inference**: `../batch/README.md`
- **Model Deployment**: `../../MODELS/README.md`
- **Alert Configuration**: `configs/realtime_config.yaml`
- **Monitoring Dashboard**: Grafana dashboards

---

**Owner**: MLOps Team  
**Contact**: mlops@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Production 🟢
