# S1000D Workflow Orchestrator - Neuromorphic SNN Implementation

## Overview

This implementation provides an event-driven Spiking Neural Network (SNN) based orchestrator for S1000D workflows in the CSDB (Common Source Database), as specified in [`../copilot_instructions.md`](../copilot_instructions.md).

## Architecture

The orchestrator uses neuromorphic computing principles to learn optimal routes, priorities, and impacts for S1000D Data Module workflows:

```
CSDB Events → AER Encoding → Spiking GNN → Policy Layer → Workflow Actions
     ↓              ↓              ↓             ↓              ↓
  CRUD ops    Spike trains   LIF neurons   Routing decisions  Orchestrator
```

## Components

### 1. Core Modules

- **`snn_core.py`**: Spiking Neural Network implementation with LIF neurons
- **`graph_builder.py`**: CSDB graph construction (DMCs, refs, effectivity)
- **`aer_encoder.py`**: Address-Event Representation encoder for CSDB events
- **`policy_layer.py`**: Discrete policy layer for routing/priority/impact decisions
- **`orchestrator_interface.py`**: Integration with Camunda/Airflow/temporal.io

### 2. Learning & Inference

- **`stdp_learning.py`**: Spike-Timing-Dependent Plasticity learning
- **`reward_modulation.py`**: Reward-modulated reinforcement learning
- **`inference_engine.py`**: Real-time inference for workflow recommendations

### 3. Integration

- **`csdb_listener.py`**: Event stream listener for CSDB (CRUD + validations)
- **`brex_guardrails.py`**: BREX rule enforcement as hard constraints
- **`explainability.py`**: Decision explanation with spike traces and subgraph heatmaps

### 4. Utilities

- **`metrics.py`**: Lead time, WIP, rework rate, first-pass yield tracking
- **`logging_audit.py`**: Immutable audit log for inputs/outputs and weights

## Implementation Details

### Spiking GNN Architecture

```python
# Network topology
Nodes: DMCs, Illustrations, IPD, PM, BREX, Product Configs
Edges: References, Dependencies, Effectivity, Workflow State

# Neuron model: Leaky Integrate-and-Fire (LIF)
τ dV/dt = -(V - V_rest) + I_syn
if V ≥ V_thresh: spike, V ← V_reset

# Learning: STDP + Reward Modulation
Δw_ij = η·(pre∘post - α·w_ij) · r(t)
```

### Event Encoding (AER)

- **Creation/Editing**: Time-to-first-spike based on urgency
- **Validation Failures**: High-priority spike bursts
- **Dependency Changes**: Cascade propagation through graph
- **Publication Requests**: Policy layer activation
- **QA Returns**: Negative reward signal

### Policy Layer Outputs

1. **Routing**: Which reviewers/approvers and in what sequence
2. **Prioritization**: Temporal scaling and SLA suggestions
3. **Impact Analysis**: List of affected DMCs (dependency propagation)
4. **Guards**: BREX violation detection → workflow blocking
5. **Explainability**: Top-k nodes/edges that triggered decision

## Quick Start

### Installation

```bash
cd orchestrator
pip install -r requirements.txt
```

### Training (Shadow Mode)

```bash
# Build CSDB graph from historical data
python scripts/build_graph.py --csdb-path ../DataModules --output graph.pkl

# Train SNN on workflow logs
python scripts/train_shadow.py \
  --graph graph.pkl \
  --logs workflow_logs_12mo.jsonl \
  --epochs 100 \
  --output model_checkpoint.pt
```

### Inference (Production)

```bash
# Start orchestrator listener
python scripts/run_orchestrator.py \
  --model model_checkpoint.pt \
  --csdb-url http://csdb.local/api \
  --mode suggest  # or auto-apply for low-risk
```

### Evaluation

```bash
# Compare with baseline heuristics
python scripts/evaluate.py \
  --model model_checkpoint.pt \
  --test-data workflow_logs_test.jsonl \
  --baseline baseline_heuristics.yaml
```

## Configuration

See `config/orchestrator_config.yaml` for:

- SNN hyperparameters (neurons, synapses, learning rates)
- CSDB connection settings
- BREX rule paths
- Workflow orchestrator endpoints (Camunda/Airflow)
- Logging and audit settings

## Monitoring

### KPIs Tracked

- **Lead time per workflow state**: DMC creation → publication
- **Average WIP**: Work-in-progress count
- **Rework rate**: % of DMCs requiring rework
- **First-pass yield**: % of DMCs approved on first review
- **Human touches per DMC**: Manual interventions required
- **Impact precision/recall**: Accuracy of dependency predictions

### Dashboards

Access metrics at: `http://localhost:8080/metrics`

- Real-time workflow state
- SNN activity visualizations
- Decision explanations
- Drift detection alerts

## Security & Compliance

### Phase 1-2: "Only-Suggest" Mode

- All recommendations require human confirmation
- Immutable audit log of all decisions
- BREX rules enforced as hard constraints outside SNN

### Phase 3+: "Auto-Apply" for Low-Risk

- Non-safety-critical DMCs only
- Automatic workflow progression
- Continuous human QA monitoring

## Development Roadmap

### Phase 1: Shadow Deployment (Weeks 1-4)

- [x] Core SNN implementation
- [x] CSDB graph builder
- [x] AER encoder
- [x] Baseline comparison framework
- [ ] Integration testing with sample CSDB

### Phase 2: Pilot Testing (Weeks 5-8)

- [ ] Deploy to staging environment
- [ ] A/B testing on low-risk modules
- [ ] Metrics collection and analysis
- [ ] Drift monitoring setup

### Phase 3: Production Rollout (Weeks 9-12)

- [ ] Production deployment
- [ ] Auto-apply for approved categories
- [ ] Continuous learning integration
- [ ] Performance optimization

## Testing

```bash
# Unit tests
pytest tests/unit/

# Integration tests
pytest tests/integration/

# End-to-end workflow simulation
pytest tests/e2e/test_workflow_simulation.py
```

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for development guidelines.

## License

Internal use only - AMPEL360 AIR-T Program

## References

- Parent specification: [`../copilot_instructions.md`](../copilot_instructions.md)
- CSDB structure: [`../DataModules/README.md`](../DataModules/README.md)
- BREX rules: [`../BREX/README.md`](../BREX/README.md)
- S1000D Issue 6.0: http://www.s1000d.org/
