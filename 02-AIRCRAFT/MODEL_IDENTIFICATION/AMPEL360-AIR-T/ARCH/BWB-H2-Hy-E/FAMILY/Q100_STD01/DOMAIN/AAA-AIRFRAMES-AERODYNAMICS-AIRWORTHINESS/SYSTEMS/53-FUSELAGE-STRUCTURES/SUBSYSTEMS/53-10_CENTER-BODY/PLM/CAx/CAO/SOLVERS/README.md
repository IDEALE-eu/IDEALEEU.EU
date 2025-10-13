# SOLVERS — Optimization Solvers

## Purpose
Computational solvers and platforms for executing optimization algorithms.

## Subdirectories

### [CLASSICAL/](CLASSICAL/) — Classical Optimization Solvers
Traditional optimization software and libraries:
- **Commercial Tools**:
  - Altair OptiStruct
  - ANSYS Mechanical APDL Optimization
  - MSC Nastran SOL 200
  - Abaqus Tosca
- **Open-Source Libraries**:
  - SciPy optimization module
  - NLopt
  - IPOPT
  - GCMMA

**Capabilities**: Gradient-based and gradient-free methods, handles thousands of variables

### [QUANTUM_OA/](QUANTUM_OA/) — Quantum-Assisted Optimization
Quantum and quantum-inspired algorithms for optimization:

#### [QUBO/](QUANTUM_OA/QUBO/) — Quadratic Unconstrained Binary Optimization
QUBO problem formulations:
- Binary variable encodings
- Penalty function formulations
- Ising model equivalents
- Problem reformulations

#### [MAPPING/](QUANTUM_OA/MAPPING/) — Problem Mapping
Mapping optimization problems to quantum hardware:
- Graph embeddings
- Minor embeddings for quantum annealers
- Qubit allocation strategies
- Problem decomposition techniques

#### [RUNS/](QUANTUM_OA/RUNS/) — Quantum Solver Runs
Execution records of quantum solvers:
- D-Wave quantum annealer runs
- Quantum Approximate Optimization Algorithm (QAOA) implementations
- Hybrid quantum-classical runs
- Run parameters and configurations

#### [LOGS/](QUANTUM_OA/LOGS/) — Quantum Solver Logs
Execution logs and diagnostics:
- Solver output logs
- Convergence histories
- Qubit statistics
- Solution quality metrics
- Comparison with classical solvers

## Guidelines
- Select solver appropriate to problem size and type
- Document solver version and settings
- Validate quantum results with classical benchmarks
- Monitor convergence and solution quality
- Archive solver input/output files
- Report computational cost and runtime
- Maintain solver configuration files
