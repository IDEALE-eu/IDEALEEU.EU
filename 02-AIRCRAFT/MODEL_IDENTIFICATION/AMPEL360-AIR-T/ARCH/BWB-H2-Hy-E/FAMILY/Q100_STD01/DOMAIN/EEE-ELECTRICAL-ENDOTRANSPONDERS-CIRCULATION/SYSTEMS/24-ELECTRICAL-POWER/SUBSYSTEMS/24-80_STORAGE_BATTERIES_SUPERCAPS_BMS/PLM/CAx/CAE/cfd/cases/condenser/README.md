# Condenser CFD Case

## Overview

CHT simulation of CO₂ condenser with vapor → liquid phase change.

## Physics

- **Solver**: multiphaseEulerFoam or interCondensatingEvaporatingFoam
- **Phase Change**: Vapor → Liquid
- **Heat Transfer**: Forced convection + condensation

## Geometry

- Tube-in-tube heat exchanger or finned tube
- Coolant channel: Water or air cooling
- CO₂ channel: High-pressure vapor inlet

## Boundary Conditions

- **CO₂ Inlet**: Superheated vapor, high pressure
- **CO₂ Outlet**: Subcooled liquid, moderate pressure
- **Coolant**: Counterflow or crossflow cooling

## Key Outputs

- Condensation rate [kg/s]
- Heat removal [kW]
- Pressure drop [Pa]
- Condensation heat transfer coefficient

## Notes

- Film condensation modeling
- Non-condensable gas effects (if air present)
