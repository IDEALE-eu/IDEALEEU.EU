# 📦 BATCH INFERENCE

**Path**: `PIPELINES/inference/batch/`  
**Purpose**: Batch anomaly detection for historical analysis and digital twin replay

---

## 🎯 Overview

This directory contains scripts for **batch inference** on historical flight data, used for:
- Post-flight analysis
- Fleet-wide health trending
- Digital twin replay validation
- Model performance evaluation
- Retrospective anomaly detection

## 📂 Contents

```
batch/
├── run_batch.py               # Main batch inference script
├── parallel_processor.py      # Multi-core parallel processing
├── results_aggregator.py      # Aggregate results across flights
└── README.md (this file)
```

## 🔄 Batch Processing Architecture

```
Historical Data (Parquet) → Batch Loader → Parallel Processing
                                                 ↓
                                         ┌───────┼───────┐
                                         ↓       ↓       ↓
                                    Worker 1  Worker 2  Worker N
                                         ↓       ↓       ↓
                                    ONNX Model (per worker)
                                         ↓       ↓       ↓
                                    Anomaly Scores
                                                 ↓
                                        Results Aggregator
                                                 ↓
                                    ┌────────────┴────────────┐
                                    ↓                         ↓
                            Parquet Results            Summary Reports
```

## 📝 Script Descriptions

### `run_batch.py`

**Purpose**: Main batch inference orchestrator

**Usage**:
```bash
python run_batch.py \
    --model ../../MODELS/engine_vibration_detector/1.0.0/ \
    --data ../../DATA/raw/engine_vibration/2025-10/ \
    --output results_2025-10.parquet \
    --workers 8
```

**Arguments**:
- `--model`: Path to model directory (contains model.onnx, scaler.pkl)
- `--data`: Path to input data (directory of Parquet files)
- `--output`: Output file path
- `--workers`: Number of parallel workers (default: CPU count)
- `--batch-size`: Batch size for inference (default: 128)
- `--filter`: Optional filter (e.g., `aircraft_id==AC001`)

**What it does**:
1. Discovers all Parquet files in data directory
2. Loads ONNX model and scaler
3. Distributes files across workers
4. Each worker:
   - Reads file
   - Applies preprocessing (windowing, feature extraction)
   - Runs inference
   - Saves anomaly scores
5. Aggregates results
6. Generates summary report

**Output Schema**:
```python
{
    "window_id": str,
    "aircraft_id": str,
    "flight_id": str,
    "timestamp": datetime64[ns],
    "anomaly_score": float32,
    "is_anomaly": bool,
    "anomaly_severity": uint8,
    "inference_latency_ms": float32
}
```

---

### `parallel_processor.py`

**Purpose**: Multi-core parallel processing utilities

**Features**:
- Worker pool management
- Load balancing across cores
- Progress tracking
- Error handling and retry logic

**Usage** (imported by `run_batch.py`):
```python
from parallel_processor import ParallelProcessor

processor = ParallelProcessor(
    model_path="...",
    num_workers=8
)
results = processor.process_files(file_list)
```

---

### `results_aggregator.py`

**Purpose**: Aggregate and summarize batch results

**Features**:
- Per-flight summary statistics
- Fleet-wide anomaly rates
- Time-series trending
- Export to various formats (Parquet, CSV, JSON)

**Usage**:
```bash
python results_aggregator.py \
    --input results_2025-10.parquet \
    --output summary_2025-10.json \
    --group-by aircraft_id
```

**Example Output** (`summary_2025-10.json`):
```json
{
  "total_windows": 500000,
  "total_flights": 500,
  "date_range": ["2025-10-01", "2025-10-31"],
  "anomaly_rate": 0.027,
  
  "by_aircraft": {
    "AC001": {
      "flights": 20,
      "windows": 20000,
      "anomaly_rate": 0.025,
      "max_anomaly_score": 8.2
    },
    "AC002": {
      "flights": 18,
      "windows": 18000,
      "anomaly_rate": 0.031,
      "max_anomaly_score": 12.5
    }
  },
  
  "by_date": {
    "2025-10-01": {"anomaly_rate": 0.021},
    "2025-10-02": {"anomaly_rate": 0.029},
    ...
  }
}
```

---

## 🚀 Quick Start

### Basic Batch Inference

```bash
# Process all October 2025 data
python run_batch.py \
    --model ../../MODELS/engine_vibration_detector/1.0.0/ \
    --data ../../DATA/raw/engine_vibration/2025-10/ \
    --output results_2025-10.parquet \
    --workers 8
```

### Filter by Aircraft

```bash
# Process only AC001
python run_batch.py \
    --model ../../MODELS/engine_vibration_detector/1.0.0/ \
    --data ../../DATA/raw/engine_vibration/2025-10/ \
    --output results_AC001_2025-10.parquet \
    --filter "aircraft_id==AC001"
```

### Generate Summary

```bash
# Aggregate results
python results_aggregator.py \
    --input results_2025-10.parquet \
    --output summary_2025-10.json \
    --group-by aircraft_id flight_id
```

---

## ⚡ Performance Optimization

### Parallelization

**Rule of Thumb**: Use `workers = CPU_cores - 1`

```bash
# Check CPU count
nproc  # Linux
sysctl -n hw.ncpu  # macOS

# Use 7 workers on 8-core machine
python run_batch.py --workers 7 ...
```

### Batch Size Tuning

Larger batch sizes → Better throughput, more memory

| Batch Size | Memory | Throughput |
|------------|--------|------------|
| 32 | ~500 MB | 100 windows/s |
| 128 | ~2 GB | 350 windows/s |
| 512 | ~8 GB | 600 windows/s |

**Recommended**: Start with 128, increase if memory allows

### Caching

```bash
# Cache preprocessed features
python run_batch.py \
    --data ../../DATA/raw/engine_vibration/2025-10/ \
    --cache-features \
    --cache-dir /tmp/feature_cache/ \
    ...
```

---

## 📊 Monitoring Progress

### Real-Time Progress

```bash
# Run with progress bar
python run_batch.py --verbose ...
```

**Example Output**:
```
Processing: 100%|████████████████| 500/500 [02:15<00:00, 3.7 files/s]
Total windows: 500,000
Anomalies detected: 13,500 (2.7%)
Avg inference time: 12.3ms/window
Total time: 2m 15s
```

### Log File

```bash
tail -f logs/batch_inference.log
```

---

## 🔍 Use Cases

### 1. Post-Flight Analysis

Analyze all flights from previous day:

```bash
python run_batch.py \
    --data ../../DATA/raw/engine_vibration/$(date -d "yesterday" +%Y-%m-%d)/ \
    --output results_$(date -d "yesterday" +%Y-%m-%d).parquet
```

### 2. Fleet Health Trending

Monthly trend analysis:

```bash
for month in 01 02 03 04 05 06 07 08 09 10 11 12; do
    python run_batch.py \
        --data ../../DATA/raw/engine_vibration/2025-$month/ \
        --output results_2025-$month.parquet
done

# Aggregate trends
python results_aggregator.py --input results_2025-*.parquet --output trend_2025.json
```

### 3. Digital Twin Replay

Replay historical scenarios in digital twin:

```bash
python run_batch.py \
    --data ../../EVALUATION/replay_dt/scenarios/ \
    --output replay_results.parquet
```

### 4. Model Comparison

Compare two model versions:

```bash
# Model v1.0.0
python run_batch.py --model .../1.0.0/ --data ... --output results_v1.0.parquet

# Model v1.1.0
python run_batch.py --model .../1.1.0/ --data ... --output results_v1.1.parquet

# Compare
python compare_results.py results_v1.0.parquet results_v1.1.parquet
```

---

## 🆘 Troubleshooting

### Issue: Out of Memory

**Action**:
- Reduce `--batch-size` (e.g., 128 → 32)
- Reduce `--workers` (e.g., 8 → 4)
- Process smaller date ranges

### Issue: Slow Processing

**Action**:
- Increase `--workers` (up to CPU count)
- Increase `--batch-size` (if memory allows)
- Use SSD for data storage
- Enable feature caching

### Issue: Inconsistent Results

**Action**:
- Verify same model and scaler used
- Check for data corruption
- Ensure deterministic preprocessing (fix random seeds)

---

## 📚 Related Documentation

- **Real-Time Inference**: `../realtime/README.md`
- **Model Deployment**: `../../MODELS/README.md`
- **Evaluation**: `../../EVALUATION/README.md`

---

**Owner**: MLOps Team  
**Contact**: mlops@ideale.eu  
**Last Updated**: 2025-10-11  
**Status**: Production 🟢
