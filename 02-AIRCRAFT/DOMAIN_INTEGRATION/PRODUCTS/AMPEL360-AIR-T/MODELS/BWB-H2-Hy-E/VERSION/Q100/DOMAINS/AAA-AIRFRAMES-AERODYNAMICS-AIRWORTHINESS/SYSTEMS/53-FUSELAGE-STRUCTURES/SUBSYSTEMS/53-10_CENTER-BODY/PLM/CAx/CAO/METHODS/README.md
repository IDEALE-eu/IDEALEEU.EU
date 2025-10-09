# METHODS — Optimization Methods

## Purpose
Optimization algorithms and methodologies applied to center body structural design.

## Subdirectories

### TOPOLOGY/ — Topology Optimization
Material layout optimization:
- Density-based methods (SIMP, RAMP)
- Level-set methods
- Evolutionary structural optimization (ESO)
- Load path identification
- Conceptual structure generation
- Manufacturing constraint integration

**Application**: Early conceptual design phase for optimal material distribution

### SIZE/ — Sizing Optimization
Parametric sizing of existing structures:
- Cross-sectional dimension optimization
- Thickness distributions
- Stiffener sizing
- Gradient-based algorithms (SQP, MMA, CONLIN)
- Design sensitivity analysis
- Efficient for many design variables

**Application**: Detailed design phase for production structures

### SHAPE/ — Shape Optimization
Geometric boundary optimization:
- Structural contour optimization
- Surface shape refinement
- Curvature optimization
- Node-based shape variables
- Adjoint sensitivity methods
- Free-form deformation techniques

**Application**: Aerodynamic/structural integration, weight reduction

## Optimization Algorithms
- Gradient-based: Sequential Quadratic Programming (SQP), Method of Moving Asymptotes (MMA)
- Gradient-free: Genetic Algorithms, Particle Swarm Optimization (PSO), Simulated Annealing
- Hybrid approaches combining multiple methods
- Multi-fidelity optimization strategies

## Guidelines
- Select method appropriate to design phase
- Document algorithm settings and convergence criteria
- Validate results with higher-fidelity analysis
- Consider manufacturing constraints early
- Maintain design history and sensitivity data
- Benchmark against known solutions when possible
