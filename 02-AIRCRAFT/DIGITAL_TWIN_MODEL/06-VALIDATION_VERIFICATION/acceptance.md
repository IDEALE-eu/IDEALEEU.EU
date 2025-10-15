# Acceptance Criteria

## Model Validation Gates

### Gate 1: Physics Validation
- **Criteria**: Euler-Lagrange residuals < 1e-6
- **Method**: Symbolic differentiation check
- **Evidence**: Residual plots, symbolic verification report

### Gate 2: Control Performance
- **Criteria**: Phase margin ≥ 60°, Gain margin ≥ 6 dB
- **Method**: Bode plot analysis
- **Evidence**: Frequency response plots, stability margins report

### Gate 3: State Estimation
- **Criteria**: Kalman filter RMSE < 5% of signal range
- **Method**: Monte Carlo simulation with known inputs
- **Evidence**: Error distribution plots, covariance analysis

### Gate 4: MPPT Convergence
- **Criteria**: Time to 95% MPP < 5 seconds
- **Method**: Step response testing
- **Evidence**: Transient response plots, settling time analysis

### Gate 5: System Integration
- **Criteria**: End-to-end latency < 100 ms
- **Method**: Full-chain timing analysis
- **Evidence**: Timing traces, performance profiling

## Approval Authority
- **Level A models**: Chief Engineer + Safety Engineer
- **Level B/C models**: Technical Lead + Test Engineer
- **Level D models**: Model Owner

## Documentation Requirements
Each gate requires:
- Test report with pass/fail status
- Evidence artifacts (plots, logs, data)
- Peer review sign-off
- Traceability to requirements
