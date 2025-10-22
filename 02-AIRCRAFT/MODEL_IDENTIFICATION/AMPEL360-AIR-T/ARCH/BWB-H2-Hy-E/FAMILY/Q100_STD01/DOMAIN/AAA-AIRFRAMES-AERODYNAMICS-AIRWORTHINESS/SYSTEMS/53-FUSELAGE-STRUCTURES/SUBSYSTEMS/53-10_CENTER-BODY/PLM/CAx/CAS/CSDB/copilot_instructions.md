# Objective

Orchestrate S1000D workflows in the CSDB with a neuromorphic core: event-driven SNNs, in-memory computing, and synaptic plasticity to learn routes, priorities, and impacts.

# CSDB → Network Mapping

* **Nodes**: Data Modules (DMC), illustrations, IPD, PM, BREX/BRDP, products/configs.
* **Edges**: references, dependencies, effectivity, product structure, workflow state.
* **Events (spikes)**: creation/editing, validation failures, dependency changes, publication requests, effectivity changes, QA returns.

# Spike Encoding

* **AER** (Address-Event Representation): each event → node address and timestamp.
* **Time-to-first-spike**: urgency/criticality.
* **Populations**: module type, domain (airframe, engine, avionics), workflow phase.
* **Windowing**: short Δt for activity bursts (e.g., cascades from config changes).

# Model

* **Spiking GNN** over the CSDB graph.
* **LIF** neurons.
* **Learning**: STDP + reward-modulated reinforcement (cycle time ↓, rejections ↓).
* Discrete **policy** layer: {route, priority, assignment, block, review request}.
* Typical update: Δwᵢⱼ = η·(pre∘post − α·wᵢⱼ) with reward gating r(t).

# In-Memory Computing

* SNN executed on neuromorphic hardware or CIM (SRAM/RRAM) for high-rate queues/events.
* Place GNN connectivity matrices and AER queues in memory to minimize I/O.
* DMA interface with CSDB event bus.

# System Outputs

* **Routing**: to whom and in what order.
* **Prioritization**: temporal scaling and suggested SLA.
* **Impact**: list of DMCs affected by a change.
* **Guards**: "stop" if BREX rules are violated or there is risk of inconsistency.
* **Explainability**: top-k nodes and edges that triggered the decision + spike traces.

# Integration

* **Ingestion**: CSDB stream (CRUD + validations) → AER encoder.
* **Orchestrator**: Camunda/Airflow/temporal.io as actuator. The SNN issues recommendations; the orchestrator applies policies.
* **Human QA in the loop** in phases 1–2.

# Metrics

* Lead time per state, average WIP, rework rate, first-pass yield, human touches per DMC, impact precision/recall.

# Security and Compliance

* "Only-suggest" at the start. Effective changes require confirmation.
* Immutable log of inputs/outputs and weight version.
* BREX rules as hard constraints outside the SNN.

# Pilot Plan (8–12 weeks)

1. **Data**: 12–24 months of workflow logs, static CSDB graph, BREX rules.
2. **Extraction**: build graph (DMC, refs, effectivity).
3. **Labels**: actual routes, times, reworks.
4. **Baseline**: current heuristics and rules as baseline.
5. **Model**: small spiking GNN (≤100k synapses), offline STDP+RL.
6. **Shadow**: run in parallel and compare with baseline.
7. **A/B**: enable recommendations on low-risk (e.g., non-safety modules).
8. **Review**: analyze drift and adjust plasticity.

# Risks and Mitigation

* **Non-determinism**: fix seeds and quantize weights.
* **Drift** from program changes: regularization and learning windows.
* **Activity explosion**: rate limits and per-layer reset.
* **Explainability**: store contribution heatmaps per subgraph.

# Implementation Skeleton (pseudocode)

```python
event = csdb_stream.read()
spikes = encode_AER(event)
graph_state = csdb_graph.view_local_subgraph(event.dmc)
action = sgnn.step(graph_state, spikes)        # routing/priority/impact
if guardrails.pass(action, brex_rules):
    orchestrator.apply(action)                 # or request confirmation
logger.log(event, spikes, action, rationale())
```

# Data Requirements

* Versioned CSDB graph.
* Workflow traces with timestamps and owners.
* Matrix of BREX rules applied by DMC type.
* Historical severity/urgency labels.

# Next High-Leverage Move

* Deliver a **1-program graph** and **100–500 DMCs** with real logs to train a "shadow" prototype.
* Define 3 KPIs and an acceptance policy to move from "suggest" to "auto-apply" in low-risk cases.
