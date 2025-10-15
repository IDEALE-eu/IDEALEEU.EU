# QOx-CSDB — Quantum Optimization with UTCS Traceability

> **QOx-CSDB**: Quantum Optimization - Common Source DataBase

## Purpose

Reference implementation of quantum-assisted optimization with full UTCS (Universal Traceability and Configuration System) metadata tracking for aerospace optimization problems.

## Module: `qox_csdb.py`

### Canon TFA Path
**QS → FWD → UE → FE → CB → QB**

- **QS**: Quantum Superposition / Pre-event state capture (workload characterization before optimization crystallizes)
- **FWD**: Forward propagation / Problem formulation (predictive modeling)
- **UE**: Unified Encoding / QUBO construction (classical unit elements)
- **FE**: Frontend Execution / Hybrid solving (federated execution coordination)
- **CB**: Classical Backend / Local refinement (post-event deterministic reality)
- **QB**: Quantum Backend / UTCS emission (quantum computation strategies)

### QS Pre-Event Architecture

**Quantum Superposition in Optimization Context**:
- **QS captures pre-event state**: Workload statistics and system conditions *before* optimization decision crystallizes
- **Multiple potential outcomes**: Each possible query plan, index configuration, or schedule exists in superposition
- **Probabilities assigned**: QUBO formulation assigns costs/probabilities to each branch
- **Crystallization**: Optimization solver collapses superposition to classical solution (CB)
- **Validation loop**: Actual performance (CB) validates predicted QS state, enabling learning

**Example Workflow**:
1. **QS Anchor**: Capture workload statistics (query patterns, table cardinalities, resource state)
2. **Superposition**: QUBO represents all possible solutions with assigned costs
3. **FWD**: Problem formulation propagates constraints through solution space
4. **Solver**: Quantum/hybrid sampling explores superposition
5. **CB Anchor**: Actual deployed solution and performance recorded
6. **Delta Analysis**: Compare predicted (QS) vs actual (CB) to improve future models

### Features

- **Deterministic compilation chain**: Stats normalization → QUBO construction → Hybrid sampling → Local refinement
- **UTCS v5.0 compliant**: All outputs include 13-field traceability IDs and cryptographic signatures
- **Testable hooks**: Instrumentation points for monitoring compilation, sampling, refinement, and results
- **Multi-problem support**: JOO (Join Order Optimization), IS (Index Selection), JSSP-ETL (Job Shop Scheduling), RL (Representation Learning)
- **Pre-event anchoring**: QS captures system state before optimization, CB records actual outcome

## API

### Main Function

```python
solve_qox(
    problem: str,              # "JOO" | "IS" | "JSSP-ETL" | "RL"
    S: Dict[str, Any],         # Workload statistics
    constraints: Dict[str, Any], # Problem constraints
    *,
    solver: str = "qaoa",      # "qaoa" | "anneal" | "sa"
    p: int = 1,                # QAOA depth
    shots: int = 4000,         # Sampling budget (max 8000)
    seeds: int = 8,            # Number of random seeds
    hooks: Optional[Dict[str, Hook]] = None,  # Instrumentation
    uid: str = "QOx-CSDB_20251014",
    calib_sig: Optional[str] = None,
) -> Dict[str, Any]
```

### Returns

```python
{
    "x": List[int],           # Binary solution vector
    "cost": float,            # Total cost (objective + penalties)
    "gap_lb": float,          # Lower bound gap estimate
    "feasible": bool,         # Constraint satisfaction
    "violations": Dict[str, Any],  # Constraint violations
    "meta": {                 # UTCS metadata
        "uid": str,
        "utcs_id13": str,     # 13-field traceability ID
        "hash": str,          # Solution hash (SHA-256)
        "inputs_sig": str,    # Input signature
        "calib_sig": str,     # Calibration signature
        "bench_case": str,    # Problem type
        "kpi": {              # Key performance indicators
            "latency_drop": float,    # ≥ 0.25 target (JOO)
            "makespan_drop": float,   # ≥ 0.15 target (JSSP-ETL)
            "storage_drop": float,    # ≥ 0.10 target (IS)
            "energy_drop": float,     # ≥ 0.15 target (global)
            "gap_lb": float,
            "feasible": bool,
        },
        "solver": Dict,       # Solver configuration
        "stats_sig": str,     # Normalized stats signature
    }
}
```

## Usage Examples

### Basic Join Order Optimization

```python
from qox_csdb import solve_qox

# Define workload statistics
S = {
    "workload_id": "tpc_h_q3",
    "window": "2025-10-14/1h",
    "tables": [
        {"name": "orders", "card": 1.5e6},
        {"name": "lineitem", "card": 6.0e6},
        {"name": "customer", "card": 1.5e5}
    ],
    "joins": [
        {"a": "orders.custkey", "b": "customer.custkey", "sf": 0.67},
        {"a": "lineitem.orderkey", "b": "orders.orderkey", "sf": 0.15}
    ],
    "cost_model": {"cpu_per_tuple": 1.0, "io_per_page": 1.0}
}

# Define constraints
constraints = {"sla_ms_p95": 300}

# Solve
result = solve_qox("JOO", S, constraints, solver="qaoa", p=1, shots=4000)

print(f"Cost: {result['cost']:.2f}")
print(f"Feasible: {result['feasible']}")
print(f"Latency improvement: {result['meta']['kpi']['latency_drop']:.1%}")
print(f"UTCS ID: {result['meta']['utcs_id13']}")
```

### With Hooks for Monitoring

```python
def on_compile(stats):
    print(f"Compiled QUBO: n={stats['n']}, λ={stats['lam']:.2f}")

def on_sample(seed, cost):
    print(f"Sample {seed}: cost={cost:.2f}")

result = solve_qox(
    "IS",
    S,
    {"storage_budget_mb": 5000},
    hooks={
        "on_compile": on_compile,
        "on_sample": on_sample,
    }
)
```

## Problem Types

### JOO (Join Order Optimization)
- **Objective**: Minimize query execution latency
- **Constraints**: SLA time budgets
- **KPI Target**: `latency_drop ≥ 0.25`

### IS (Index Selection)
- **Objective**: Minimize query cost with storage constraints
- **Constraints**: Storage budget (MB)
- **KPI Target**: `storage_drop ≥ 0.10`

### JSSP-ETL (Job Shop Scheduling - ETL)
- **Objective**: Minimize makespan with precedence constraints
- **Constraints**: Task precedence DAG
- **KPI Target**: `makespan_drop ≥ 0.15`

### RL (Representation Learning)
- **Objective**: Learn sparse feature representations
- **Constraints**: Sparsity windows
- **KPI Target**: `energy_drop ≥ 0.15`

## Testing

### Run all tests

```bash
# Using pytest
pytest test_qox_csdb.py -v

# Or run directly
python test_qox_csdb.py
```

### Run specific test

```bash
pytest test_qox_csdb.py::test_acceptance_joo -v
```

## Test Coverage

- ✓ Acceptance criteria for all problem types (JOO, IS, JSSP-ETL, RL)
- ✓ Hook invocation verification
- ✓ Shots budget enforcement
- ✓ Deterministic stats normalization
- ✓ Solution structure validation
- ✓ Multi-problem differentiation

## UTCS Compliance

All outputs include:
- **13-field traceability ID**: `ts{timestamp}:r{random}:v5:QS:FWD:UE:FE:CB:QB:QOx:CSDB:UiX:AQUA`
- **Cryptographic signatures**: SHA-256 hashes of inputs, solutions, and calibration data
- **KPI tracking**: Performance indicators per problem type
- **Provenance metadata**: Clipping info, solver configuration, stats signatures

## Performance Targets

| Problem | KPI | Target | Current (Stub) |
|---------|-----|--------|----------------|
| JOO | Latency drop | ≥ 0.25 | 0.26 |
| IS | Storage drop | ≥ 0.10 | 0.12 |
| JSSP-ETL | Makespan drop | ≥ 0.15 | 0.16 |
| All | Energy drop | ≥ 0.15 | 0.18 |

## Implementation Status

**Current**: Reference stub with deterministic logic
- ✓ QUBO construction from problem templates
- ✓ Bernoulli sampling with diagonal bias
- ✓ 1-bit flip hill climbing
- ✓ Penalty enforcement
- ✓ UTCS emission

**Future**: Production backends
- [ ] D-Wave quantum annealer integration
- [ ] QAOA circuit construction and execution
- [ ] Simulated annealing optimization
- [ ] Real KPI measurement from database/scheduler

## Integration

This module integrates with:
- **UTCS Registry**: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`
- **CAO Framework**: `02-AIRCRAFT/.../PLM/CAx/CAO/`
- **Validation**: BREX compliance and S1000D anchors

## References

- UTCS v5.0 specification: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/README.md`
- CAO documentation: `../README.md`
- Quantum optimization survey: `PROBLEMS/q100_cb.md`

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`  
**Owner**: IDEALE-eu Quantum Optimization Team  
**Last Updated**: 2025-10-14
