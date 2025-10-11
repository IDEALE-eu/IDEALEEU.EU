# Aerodynamics API

## Overview

The aerodynamics block computes aerodynamic coefficients and loads at 200 Hz using bilinear interpolation over α–Mach tables plus linear derivatives and control effectiveness terms.

## Input Processing

**Flight State Inputs:**
- `alpha_rad` - Angle of attack (radians)
- `beta_rad` - Sideslip angle (radians)
- `mach` - Mach number
- `qbar_pa` - Dynamic pressure (Pascals)
- `rho_kgpm3` - Air density (kg/m³)
- `tas_mps` - True airspeed (m/s)

**Control Surface Inputs:**
- `delta_e_rad` - Elevator deflection (radians)
- `delta_a_rad` - Aileron deflection (radians)
- `delta_r_rad` - Rudder deflection (radians)

## Computation Flow

### 1. Base Coefficient Lookup

Perform bilinear interpolation on α–Mach tables:
- `CL_base = interp2d(alpha, mach, CL_alpha_mach.csv)`
- `CD_base = interp2d(alpha, mach, CD_alpha_mach.csv)`
- `Cm_base = interp2d(alpha, mach, Cm_alpha_mach.csv)`

### 2. Add Linear Derivatives

From `coeffs_airframe.yaml`, add linear contributions:
- `CL = CL_base + CL_alpha * alpha + CL_q_hat * q_hat`
- `CD = CD_base + CD0`
- `Cm = Cm_base + Cm_alpha * alpha + Cm_q_hat * q_hat`
- `CY = CY_beta * beta`
- `Cl = Cl_beta * beta + Cl_p_hat * p_hat`
- `Cn = Cn_beta * beta + Cn_r_hat * r_hat`

Where:
- `q_hat = q * c_ref / (2 * V)` (pitch rate, normalized)
- `p_hat = p * b_ref / (2 * V)` (roll rate, normalized)
- `r_hat = r * b_ref / (2 * V)` (yaw rate, normalized)

### 3. Add Control Effectiveness

From `control_effectiveness.yaml`:
- `CL += CL_delta_e * delta_e`
- `Cm += Cm_delta_e * delta_e`
- `Cl += Cl_delta_a * delta_a`
- `Cn += Cn_delta_r * delta_r`

Apply nonlinear scaling factors if specified.

### 4. Compute Forces and Moments

Convert coefficients to forces and moments in body frame:

**Forces:**
- `FX_N = -qbar_pa * S_ref_m2 * CD`
- `FY_N = qbar_pa * S_ref_m2 * CY`
- `FZ_N = -qbar_pa * S_ref_m2 * CL`

**Moments:**
- `MX_Nm = qbar_pa * S_ref_m2 * b_ref_m * Cl`
- `MY_Nm = qbar_pa * S_ref_m2 * c_ref_m * Cm`
- `MZ_Nm = qbar_pa * S_ref_m2 * b_ref_m * Cn`

## Outputs

**Coefficients:**
- `CL` - Lift coefficient
- `CD` - Drag coefficient
- `CY` - Side force coefficient
- `Cl` - Rolling moment coefficient
- `Cm` - Pitching moment coefficient
- `Cn` - Yawing moment coefficient

**Forces (N):**
- `FX_N` - X-axis force (body frame)
- `FY_N` - Y-axis force (body frame)
- `FZ_N` - Z-axis force (body frame)

**Moments (N·m):**
- `MX_Nm` - Rolling moment
- `MY_Nm` - Pitching moment
- `MZ_Nm` - Yawing moment

## Notes

- ISA atmosphere model and dynamic pressure (q̄) calculation are performed upstream
- This block does NOT compute atmospheric properties
- All angles in radians, forces in Newtons, moments in Newton-meters
- Reference geometry from `INTERFACES/signals.yaml`: S_ref_m2=16.2, c_ref_m=1.9, b_ref_m=10.8
