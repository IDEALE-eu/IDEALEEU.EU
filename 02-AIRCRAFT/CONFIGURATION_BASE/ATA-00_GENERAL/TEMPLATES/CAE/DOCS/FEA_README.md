# FEA Best Practices and Guidelines

## Overview

This document provides detailed guidance for FEA simulations including solver selection, element types, material models, and best practices.

## Solver Selection

### Abaqus
**Strengths**:
- Excellent nonlinear capabilities
- Robust contact algorithms
- Wide material library
- Industry standard

**Best for**:
- Nonlinear analysis
- Complex contact
- Composite materials
- Crash simulations

### ANSYS Mechanical
**Strengths**:
- Integrated CAD interface
- Good linear analysis
- Parametric studies
- Comprehensive GUI

**Best for**:
- Linear stress analysis
- Design optimization
- Parametric studies
- Modal analysis

### Nastran
**Strengths**:
- Linear analysis speed
- Large models
- Industry standard
- Excellent dynamics

**Best for**:
- Linear statics
- Modal analysis
- Frequency response
- Aerospace structures

## Element Selection

### Element Types

| Application | Element Type | Notes |
|-------------|--------------|-------|
| 3D stress | C3D8R, C3D10 | Reduced integration or 2nd order |
| Thin structures | S4R, S8R | Shell elements |
| Beams | B31, B32 | Timoshenko beam |
| Membranes | M3D4, M3D3 | No bending stiffness |
| Thermal | DC3D8, DC3D10 | Heat transfer |

### Element Order

**Linear (1st order)**:
- Faster, less memory
- More elements needed
- Acceptable for well-behaved problems
- Use reduced integration (C3D8R, S4R)

**Quadratic (2nd order)**:
- More accurate
- Fewer elements needed
- Better for stress concentrations
- More expensive per element
- Recommended for complex geometry

### Integration

**Full Integration**:
- More accurate stresses
- Prone to locking (use carefully)
- More expensive

**Reduced Integration**:
- Avoids locking
- Faster
- Check for hourglassing
- Recommended for most cases

## Mesh Generation

### Quality Metrics

| Metric | Good | Acceptable | Poor |
|--------|------|------------|------|
| Aspect ratio | < 3 | 3-10 | > 10 |
| Jacobian | > 0.7 | 0.5-0.7 | < 0.5 |
| Warping (shells) | < 10° | 10-20° | > 20° |
| Distortion | < 0.3 | 0.3-0.7 | > 0.7 |

### Mesh Refinement

Refine mesh at:
- Stress concentrations (holes, fillets)
- Load application points
- Boundary condition transitions
- Contact interfaces
- Regions of interest

### Mesh Independence

1. Start with coarse mesh
2. Refine by ~2× in critical regions
3. Compare peak stress/displacement
4. Continue until change < 5%
5. Document convergence study

## Material Models

### Linear Elastic

Use when:
- Small deformations (< 1% strain)
- Stresses below yield
- No time-dependent behavior

Properties needed:
- Young's modulus (E)
- Poisson's ratio (ν)
- Density (ρ)

### Elastic-Plastic

Use when:
- Stresses exceed yield
- Permanent deformation expected
- Forming simulations

Properties needed:
- Elastic properties
- Yield stress (σy)
- Plastic stress-strain curve
- Hardening behavior

### Hyperelastic (Rubber)

Use for:
- Rubber and elastomers
- Large strains
- Seals and gaskets

Models:
- Neo-Hookean: Simple, 2 parameters
- Mooney-Rivlin: 2-5 parameters
- Ogden: Most flexible, 6+ parameters

### Composite Materials

Specify:
- Ply properties (E1, E2, G12, ν12)
- Layup sequence
- Ply orientations
- Failure criteria

## Boundary Conditions

### Constraints

**Fixed Support**:
- All DOFs constrained
- Use sparingly (over-constrains)

**Symmetry**:
- Normal translation = 0
- Tangential rotations = 0

**Proper Constraints**:
- Allow thermal expansion
- Prevent rigid body motion
- Avoid over-constraint

### Loads

**Concentrated Force**:
- Causes stress singularity
- Use only for preliminary analysis
- Distribute over area for production

**Pressure**:
- Follows deformed surface (follower force)
- Specify on surfaces, not nodes

**Thermal Load**:
- Specify temperature field
- Include thermal expansion coefficient

## Contact Modeling

### Contact Types

**Bonded**:
- No separation or sliding
- Equivalent to shared nodes
- Use for adhesive, welds

**No Separation**:
- No separation, sliding allowed
- For compression-only interfaces

**Frictional**:
- Separation and sliding
- Specify friction coefficient
- Most realistic

**Frictionless**:
- Separation and sliding
- No tangential resistance
- Faster convergence

### Contact Settings

- **Hard contact**: No penetration (pressure)
- **Soft contact**: Penalty method (stiffness)
- **Surface-to-surface**: More accurate, use when possible
- **Node-to-surface**: Older, less accurate

## Nonlinear Analysis

### Geometric Nonlinearity

Include when:
- Large displacements (> 10% span)
- Large rotations
- Buckling analysis
- Flexible structures

### Material Nonlinearity

Include when:
- Plastic deformation
- Hyperelastic materials
- Creep or viscoelasticity
- Temperature-dependent properties

### Solution Control

For nonlinear:
- Use automatic time stepping
- Start with small load increments
- Increase increments after convergence
- Use line search for robustness

## Thermal Analysis

### Steady-State

Use when:
- Equilibrium temperature distribution
- Time-independent loads
- Faster solution

Boundary conditions:
- Temperature (Dirichlet)
- Heat flux (Neumann)
- Convection (Robin)

### Transient

Use when:
- Time-varying loads
- Thermal shock
- Phase change

Additional requirements:
- Initial conditions
- Time step size
- Total analysis time

## Dynamic Analysis

### Modal Analysis

Extracts natural frequencies and mode shapes.

Best practices:
- Use sufficient modes (up to 1.5× max frequency of interest)
- Check for rigid body modes (f ≈ 0)
- Validate with experimental data

### Frequency Response

Response to harmonic loading.

Settings:
- Frequency range
- Frequency resolution
- Damping (typically 1-5%)

### Transient Dynamic

Time-domain solution.

Requirements:
- Time step: Δt ≤ 1/(20×fmax)
- Total time: Several periods
- Damping definition

## Submodeling

Use when:
- Local refinement needed
- Different physics in region
- Large model, local detail

Steps:
1. Run global model
2. Extract boundary conditions
3. Run local refined model
4. Verify interface

## Optimization

### Design Variables
- Geometry (dimensions)
- Material properties
- Layup (composites)

### Objectives
- Minimize mass
- Minimize stress
- Maximize stiffness

### Constraints
- Stress limits
- Displacement limits
- Manufacturing constraints

## Quality Checks

### Before Analysis
- [ ] Units consistent
- [ ] Material properties correct
- [ ] Boundary conditions proper
- [ ] Loads applied correctly
- [ ] Mesh quality acceptable
- [ ] No unconstrained rigid body motion

### After Analysis
- [ ] Solution converged
- [ ] Results physically reasonable
- [ ] Reaction forces balance applied loads
- [ ] Stress singularities identified
- [ ] Deformed shape makes sense

## Common Errors

### Singularities
**Cause**: Point loads, sharp corners  
**Fix**: Distribute loads, add fillets, use sub-modeling

### Rigid Body Motion
**Cause**: Insufficient constraints  
**Fix**: Add constraints to prevent all rigid body motion

### Over-Constraint
**Cause**: Too many constraints  
**Fix**: Use minimum necessary constraints, allow expansion

### Poor Convergence
**Cause**: Large steps, poor contact, bad mesh  
**Fix**: Reduce step size, adjust contact, improve mesh

## Post-Processing

### Standard Outputs

Always check:
- Von Mises stress
- Maximum principal stress
- Displacements
- Reaction forces
- Safety factors

### Averaging

- **Unaveraged**: Shows element results (discontinuous)
- **Averaged**: Smooths across elements (continuous)
- Use unaveraged for checking convergence

### Stress Concentrations

- Identify locations
- Check mesh refinement
- Compare to analytical (if available)
- Document safety factors

## Documentation

Document:
- Analysis purpose
- Assumptions and simplifications
- Material properties and sources
- Boundary conditions and loads
- Mesh details
- Results summary
- Conclusions and recommendations

## References

- Abaqus Analysis User's Guide
- ANSYS Mechanical User's Guide
- Cook: Finite Element Modeling
- Zienkiewicz: The Finite Element Method
- Roark's Formulas for Stress and Strain

---

**Version:** 1.0  
**Last Updated:** 2025-10-23
