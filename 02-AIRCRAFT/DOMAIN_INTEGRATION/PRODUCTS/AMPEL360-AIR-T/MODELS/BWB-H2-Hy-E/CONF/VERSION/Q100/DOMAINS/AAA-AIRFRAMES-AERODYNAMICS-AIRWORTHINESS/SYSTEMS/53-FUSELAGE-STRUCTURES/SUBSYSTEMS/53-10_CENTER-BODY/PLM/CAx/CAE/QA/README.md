# QA — Quality Assurance

## Purpose
Quality assurance activities for CAE models and analyses.

## Subdirectories

### VERIFICATION/ — Verification Cases
Model verification against analytical solutions and benchmarks:
- Element verification tests
- Mesh convergence studies
- Solver verification cases
- Known analytical solutions
- Code-to-code comparisons
- Benchmark problems from literature
- Unit tests for custom procedures

**Purpose**: Ensure mathematical model is solved correctly

### VALIDATION/ — Validation Cases
Model validation against physical test data:
- Correlation with component tests
- Correlation with full-scale tests
- Material test validation
- Load calibration tests
- Environmental testing correlation
- Certification test correlation
- Model updates based on test data

**Purpose**: Ensure model represents physical reality

## Guidelines
- Document all verification and validation activities
- Maintain traceability to requirements
- Archive test data with validation cases
- Include acceptance criteria for V&V
- Update V&V cases when models change
- Reference CS-25 § 25.1529 (certification by analysis)
- Provide summary reports of V&V status

## Standards
- ASME V&V 10 — Computational Solid Mechanics
- ASME V&V 20 — Computational Fluid Dynamics
- NASA-STD-7009 — Standard for Models and Simulations
