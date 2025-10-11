# Aerodynamic Coefficient Build-Up

## Overview

This document describes the mathematical formulation for computing aerodynamic coefficients from lookup tables, linear derivatives, and control effectiveness.

## 1. Base Coefficients from Tables

The base non-linear coefficients are obtained through bilinear interpolation:

```
CL_table(α, M) = bilinear_interp(α, M, CL_alpha_mach.csv)
CD_table(α, M) = bilinear_interp(α, M, CD_alpha_mach.csv)
Cm_table(α, M) = bilinear_interp(α, M, Cm_alpha_mach.csv)
```

### Bilinear Interpolation

For a grid point `(α_i, M_j)` and surrounding points:

```
f(α, M) = (1-t_α)(1-t_M) f(α_i, M_j) 
        + t_α(1-t_M) f(α_i+1, M_j)
        + (1-t_α)t_M f(α_i, M_j+1)
        + t_α t_M f(α_i+1, M_j+1)
```

where:
- `t_α = (α - α_i) / (α_i+1 - α_i)`
- `t_M = (M - M_j) / (M_j+1 - M_j)`

## 2. Linear Derivatives

Add linear contributions from stability derivatives (per radian):

### Longitudinal Coefficients

```
CL = CL_table(α, M) + CL_α · α + CL_q̂ · q̂
CD = CD_table(α, M) + CD0
Cm = Cm_table(α, M) + Cm_α · α + Cm_q̂ · q̂
```

### Lateral-Directional Coefficients

```
CY = CY_β · β
Cl = Cl_β · β + Cl_p̂ · p̂
Cn = Cn_β · β + Cn_r̂ · r̂
```

### Normalized Rates

```
q̂ = q · c_ref / (2 · V)    (pitch rate)
p̂ = p · b_ref / (2 · V)    (roll rate)
r̂ = r · b_ref / (2 · V)    (yaw rate)
```

Where:
- `q, p, r` are body angular rates (rad/s)
- `V` is true airspeed (m/s)
- `c_ref` is mean aerodynamic chord (m)
- `b_ref` is wing span (m)

## 3. Control Surface Effectiveness

Add control surface contributions:

```
CL += CL_δe · δe · scale_e(δe)
Cm += Cm_δe · δe · scale_e(δe)
Cl += Cl_δa · δa
Cn += Cn_δr · δr
```

### Nonlinear Scaling

For elevator, apply nonlinear scaling:

```
scale_e(δe) = piecewise_linear(δe, breakpoints_rad, scale_factors)
```

Example from `control_effectiveness.yaml`:
- At δe = -0.35 rad: scale = 0.7
- At δe = 0.0 rad: scale = 1.0
- At δe = 0.35 rad: scale = 0.85

This accounts for control surface stall and flow separation effects.

## 4. Force and Moment Calculation

Convert dimensionless coefficients to dimensional forces and moments:

### Forces (Body Frame)

```
F_X = -q̄ · S_ref · CD    (axial force, drag)
F_Y = q̄ · S_ref · CY     (side force)
F_Z = -q̄ · S_ref · CL    (normal force, lift)
```

### Moments (Body Frame)

```
M_X = q̄ · S_ref · b_ref · Cl    (rolling moment)
M_Y = q̄ · S_ref · c_ref · Cm    (pitching moment)
M_Z = q̄ · S_ref · b_ref · Cn    (yawing moment)
```

Where:
- `q̄ = ½ ρ V²` is dynamic pressure (Pa)
- `S_ref` is reference wing area (m²)
- `b_ref` is reference span (m)
- `c_ref` is reference chord (m)

## 5. Sign Conventions

### Angles
- α (alpha): positive nose-up
- β (beta): positive nose-right
- δe (elevator): positive trailing-edge down
- δa (aileron): positive right-down/left-up (right roll)
- δr (rudder): positive trailing-edge left

### Forces (Body Frame)
- F_X: positive forward
- F_Y: positive right
- F_Z: positive down

### Moments (Body Frame)
- M_X: positive right-wing down
- M_Y: positive nose-up
- M_Z: positive nose-right

## 6. Parameter Sources

- **Table Data**: `PARAMS/tables/*.csv`
- **Linear Derivatives**: `PARAMS/coeffs_airframe.yaml`
- **Control Effectiveness**: `PARAMS/control_effectiveness.yaml`
- **Reference Geometry**: `INTERFACES/signals.yaml`

## 7. Implementation Notes

### Performance
- Bilinear interpolation: O(1) operation with pre-computed indices
- Target execution time: <5 ms at 200 Hz update rate

### Validity Envelope
- α: -5° to +15° (-0.087 to 0.262 rad)
- M: 0.1 to 0.82
- Outside envelope: extrapolation with warning

### Extensions
Future enhancements may include:
- Compressibility corrections (Prandtl-Glauert)
- Flap/slat effects
- Ground effect
- Reynolds number corrections
