# CONSTRAINTS — Optimization Constraints

## Purpose
Define structural and system constraints for center body optimization to ensure safe, certifiable, and manufacturable designs.

## Subdirectories

### STRENGTH/ — Strength Constraints
Structural strength requirements:
- Ultimate load capability (1.5 × limit loads)
- Material allowables (yield, ultimate, bearing)
- Margin of safety requirements
- Static strength verification
- Reserve factors per CS-25

### BUCKLING/ — Buckling Constraints
Stability requirements:
- Panel buckling (local and global)
- Column buckling of stiffeners
- Skin-stringer stability
- Crippling of stiffeners
- Buckling margins and knockdown factors

### PRESSURIZATION/ — Pressurization Constraints
Pressure vessel requirements:
- Cabin pressure differential (8.6 psi per Q100 config)
- Hoop stress limits
- Longitudinal stress limits
- Fatigue life under pressurization cycles
- Crack propagation limits

### CG/ — Center of Gravity Constraints
Mass distribution requirements:
- CG location envelope
- Moment of inertia limits
- Balance requirements
- Loading scenarios

### ACCESS/ — Access and Maintainability Constraints
Design for maintenance:
- Minimum access panel sizes
- Inspection point accessibility
- Tool clearance requirements
- Maintenance task compatibility

### CLEARANCES/ — Clearance Constraints
Geometric and interference constraints:
- Structural member clearances
- System routing clearances
- Deflection limits
- Assembly clearances
- Installation clearances

## Guidelines
- Reference applicable regulations (CS-25, CS-E, etc.)
- Document constraint sensitivity
- Maintain traceability to requirements
- Update when loads or requirements change
- Include both hard and soft constraints
- Document constraint relaxation rationale if applicable
