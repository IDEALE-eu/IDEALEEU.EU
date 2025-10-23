# Evaporator CFD Case

## Overview

CHT simulation of CO₂ evaporator with sublimation/evaporation heat transfer.

## Physics

- **Solver**: chtMultiRegionFoam
- **Phase Change**: Liquid → Vapor or Solid → Vapor
- **Heat Transfer**: Forced convection + phase change

## Geometry

- Channel: 10 mm × 10 mm × 200 mm
- Heating element: Electric heater or hot gas channel
- Heat exchanger walls: Aluminum or copper

## Boundary Conditions

- **Inlet**: Subcooled liquid or solid CO₂, low velocity
- **Outlet**: Superheated vapor, pressure outlet
- **Heater**: Constant power (500 W) or fixed temperature (80-150°C)

## Key Outputs

- Exit vapor quality
- Heat transfer coefficient [W/m²/K]
- Pressure drop [Pa]
- Thermal efficiency

## Notes

- Critical heat flux monitoring to avoid dry-out
- Two-phase flow modeling using VOF or Euler-Euler
