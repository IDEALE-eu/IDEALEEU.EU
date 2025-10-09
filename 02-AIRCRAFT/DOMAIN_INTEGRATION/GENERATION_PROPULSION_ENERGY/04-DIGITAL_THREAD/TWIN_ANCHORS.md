# Digital Twin Anchors

## Overview

This document defines the Key Performance Indicators (KPIs) and data anchors for the Digital Twin integration of the GENERATION_PROPULSION_ENERGY domain.

## Power Generation KPIs

### Electrical Power
- **Total Generation Capacity**: Real-time kVA from all generators
- **Generation Utilization**: Percentage of total capacity in use
- **Generator Efficiency**: Power output vs fuel consumption
- **Bus Voltage**: AC and DC bus voltages (real-time)
- **Bus Current**: Load currents on all buses
- **Power Quality**: Frequency, voltage regulation, THD

### Energy Storage
- **Battery State of Charge (SOC)**: Percentage remaining
- **Battery Health**: Capacity fade, internal resistance
- **Charging/Discharging Rate**: Current flow (A)
- **Battery Temperature**: Thermal monitoring

## Propulsion KPIs

### Engine Performance
- **Thrust Output**: Real-time thrust (lbf or kN)
- **N1 Speed**: Fan rotor speed (% RPM)
- **N2 Speed**: Core rotor speed (% RPM)
- **EGT**: Exhaust Gas Temperature (°C)
- **Fuel Flow**: Real-time consumption (lb/hr or kg/hr)
- **Specific Fuel Consumption (SFC)**: Fuel efficiency

### APU Performance
- **APU Run Time**: Operating hours
- **APU Load**: Electrical and pneumatic load
- **APU Fuel Consumption**: Fuel used
- **APU EGT**: Exhaust temperature

## Thermal KPIs

- **Oil Temperature**: Engine and APU oil (°C)
- **Fuel Temperature**: Main fuel system (°C)
- **Bleed Air Temperature**: HP and LP bleed (°C)
- **Generator Temperature**: Winding and oil temperatures
- **Compartment Temperatures**: APU bay, engine nacelle

## Reliability and Health KPIs

- **Mean Time Between Failures (MTBF)**: System reliability
- **Component Life Remaining**: Based on cycles and hours
- **Fault Rate**: Faults per flight hour
- **Dispatch Reliability**: Percentage of successful dispatches

## Digital Twin Data Contracts

See `DATA_CONTRACTS/` directory for detailed telemetry specifications.

---

**Last Updated**: 2024-01-15
