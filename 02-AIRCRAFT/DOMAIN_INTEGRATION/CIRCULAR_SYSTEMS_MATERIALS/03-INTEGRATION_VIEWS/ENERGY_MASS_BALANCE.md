# Energy and Mass Balance - Circular Systems Domain

## Overview

This document provides the energy and mass balance analysis for the CIRCULAR_SYSTEMS_MATERIALS domain, quantifying the flows of energy, water, hydrogen, and materials across the integrated systems.

## Global Energy Balance

### Total Energy Flows (Typical Mission Profile)

```
┌────────────────────────────────────────────────────────────┐
│                    ENERGY BALANCE                           │
│               (Cruise Conditions, FL350)                    │
└────────────────────────────────────────────────────────────┘

INPUTS                          OUTPUTS
┌──────────────────┐           ┌──────────────────┐
│ Electrical Power │──────────►│ Mechanical Work  │
│   50 kW          │           │   35 kW          │
├──────────────────┤           ├──────────────────┤
│ Bleed Air        │──────────►│ Cabin Conditioning│
│   100 kW thermal │           │   70 kW          │
├──────────────────┤           ├──────────────────┤
│ H₂ Chemical      │──────────►│ Propulsion       │
│   2000 kW        │           │   1600 kW        │
└──────────────────┘           ├──────────────────┤
                               │ Waste Heat       │
                               │   445 kW         │
                               └──────────────────┘

Efficiency: 85% (vs. 70% conventional)
```

### Energy Flow Breakdown by System

| System | Input (kW) | Useful Output (kW) | Waste Heat (kW) | Efficiency |
|--------|------------|-------------------|-----------------|------------|
| ATA-21 ECS | 100 (bleed) + 20 (electric) | 85 (conditioning) | 35 | 71% |
| ATA-28 H₂ | 2000 (chemical) | 1600 (propulsion) | 400 | 80% |
| ATA-38 Water | 5 (electric) | 4 (pumping) | 1 | 80% |
| MTL Circularity | N/A (lifecycle) | N/A | N/A | N/A |

## Thermal Energy Recovery

### Heat Recovery Opportunities

```
┌─────────────────────────────────────────────────────────────┐
│                   HEAT RECOVERY CASCADE                      │
└─────────────────────────────────────────────────────────────┘

High-Grade Heat (400-600°C)
  │  ├─► Engine exhaust → [Future: ORC or Stirling cycle]
  │  └─► Not currently recovered
  ▼
Mid-Grade Heat (100-200°C)
  │  ├─► Avionics cooling → Cabin heating (winter)
  │  └─► Recovery: 10 kW
  ▼
Low-Grade Heat (20-80°C)
     ├─► ECS condensate → Water heating
     ├─► ECS heat rejection → H₂ boil-off management
     └─► Recovery: 15 kW

Total Heat Recovery: 25 kW (from 445 kW available)
Recovery Efficiency: 5.6% (target: 10% by 2030)
```

### Thermal Integration Benefits

| Integration | Heat Recovered (kW) | Energy Saved (kW electric) | CO₂ Reduction (kg/hr) |
|-------------|---------------------|----------------------------|----------------------|
| ECS → H₂ boil-off | 15 | 5 | 1.5 |
| Avionics → Cabin heating | 10 | 3 | 0.9 |
| ECS → Water heating | 5 | 2 | 0.6 |
| **Total** | **30** | **10** | **3.0** |

## Mass Balance

### Water System Mass Balance

```
┌─────────────────────────────────────────────────────────────┐
│              WATER MASS BALANCE (per flight)                 │
└─────────────────────────────────────────────────────────────┘

INPUTS                          OUTPUTS
┌──────────────────┐           ┌──────────────────┐
│ Fresh Water      │           │ Consumed         │
│   100 L          │           │   80 L           │
├──────────────────┤           ├──────────────────┤
│ ECS Condensate   │           │ Greywater        │
│   50 L           │──────────►│   70 L           │
└──────────────────┘           ├──────────────────┤
                               │ Reclaimed        │
                               │   50 L (reused)  │
                               └──────────────────┘

Net Fresh Water: 100 L (vs. 150 L conventional, 33% savings)
```

### Water Flow Rates

| Source/Sink | Flow Rate | Duration | Total Volume |
|-------------|-----------|----------|--------------|
| **Inputs** |
| Fresh water tank | Variable | Full flight | 100 L |
| ECS condensate | 5-10 L/hr | 6 hrs | 40-60 L |
| **Outputs** |
| Galley consumption | 2-3 L/hr | 6 hrs | 12-18 L |
| Lavatory consumption | 8-12 L/hr | 6 hrs | 48-72 L |
| Greywater to treatment | 10-15 L/hr | 6 hrs | 60-90 L |
| **Reclamation** |
| Treated greywater | 7-10 L/hr | 6 hrs | 42-60 L |
| Reuse efficiency | 70% | - | - |

### Hydrogen Mass Balance

```
┌─────────────────────────────────────────────────────────────┐
│              HYDROGEN MASS BALANCE (per flight)              │
└─────────────────────────────────────────────────────────────┘

INPUTS                          OUTPUTS
┌──────────────────┐           ┌──────────────────┐
│ LH₂ at Departure │           │ Engine Combustion│
│   1000 kg        │──────────►│   970 kg         │
└──────────────────┘           ├──────────────────┤
                               │ Boil-off (vented)│
                               │   15 kg          │
                               ├──────────────────┤
                               │ Boil-off (used)  │
                               │   15 kg          │
                               └──────────────────┘

Boil-off Rate: 3% (vs. 5% without ECS integration)
Boil-off Utilization: 50% (engine/fuel cell)
Net H₂ Efficiency: 97% (vs. 95% conventional)
```

### Hydrogen Boil-off Management

| Condition | Boil-off Rate | Active Cooling | Net Boil-off | BOG Utilization |
|-----------|---------------|----------------|--------------|-----------------|
| Ground operations | 5% /day | No | 5% /day | 20% |
| Cruise (no ECS integration) | 3% /day | No | 3% /day | 50% |
| Cruise (with ECS integration) | 3% /day | Yes | 1.5% /day | 90%+ |

## Material Flow Analysis

### Lifecycle Material Flows (per aircraft)

```
┌─────────────────────────────────────────────────────────────┐
│               MATERIAL LIFECYCLE FLOWS                       │
│                  (20-year service life)                      │
└─────────────────────────────────────────────────────────────┘

Virgin Materials → Production → Aircraft (40,000 kg)
    ▲                 │                │
    │                 │                ▼
    │                 │           Use Phase (20 years)
    │                 │                │
    │                 │                ▼
    │                 │         End-of-Life (40,000 kg)
    │                 │          │         │         │
    │                 │          ▼         ▼         ▼
    │                 │        Reuse    Repair   Refurbish
    │                 │       (12,000)  (8,000)   (6,000)
    │                 │                           │
    │                 └───────────────────────────┘
    │                             │
    └─────────────────────── Recycle (14,000 kg)
                              Recovery Rate: 80%
```

### Material Recovery Rates

| Material Category | Aircraft Mass (kg) | Recovery Rate | Recovered (kg) | Recycled to Virgin |
|-------------------|-------------------|---------------|----------------|-------------------|
| Aluminum alloys | 18,000 | 90% | 16,200 | 12,150 (75%) |
| Titanium alloys | 2,000 | 85% | 1,700 | 1,360 (80%) |
| CFRP composites | 8,000 | 40% | 3,200 | 960 (30%) |
| Thermoplastics | 1,000 | 80% | 800 | 640 (80%) |
| Copper/brass | 500 | 95% | 475 | 451 (95%) |
| Other materials | 10,500 | 60% | 6,300 | 3,780 (60%) |
| **Total** | **40,000** | **72.5%** | **29,000** | **19,341 (66%)** |

*Target: 80% recovery rate by 2030*

## Energy Payback Analysis

### Lifecycle Energy Balance

| Phase | Energy Input (GJ) | Notes |
|-------|-------------------|-------|
| **Production** |
| Virgin materials | 150,000 | Aluminum, titanium, composites |
| Recycled materials (30%) | -45,000 | Energy credit for recycling |
| Manufacturing | 50,000 | Assembly, finishing |
| **Use Phase (20 years)** |
| Fuel (H₂) | 1,200,000 | 20 years × 300 flights/yr × 200 GJ/flight |
| Maintenance | 20,000 | Parts, repairs, inspections |
| **End-of-Life** |
| Disassembly | 2,000 | Labor, tooling |
| Recycling | 10,000 | Energy to recycle materials |
| **Total Lifecycle** | **1,387,000 GJ** | **vs. 1,450,000 GJ conventional (4.3% savings)** |

### Energy Recovery Payback

| Investment | Energy Saved (GJ/yr) | Payback Period (years) | 20-Year Savings (GJ) |
|------------|---------------------|------------------------|----------------------|
| Thermal integration (ECS↔H₂) | 1,500 | 2 | 30,000 |
| Water reclamation system | 500 | 4 | 10,000 |
| Material recycling infrastructure | 1,000 | 5 | 20,000 |
| **Total** | **3,000** | **3.3 avg** | **60,000** |

## Performance Targets vs. Baseline

### System Performance Summary

| Metric | Baseline | Current Target | 2030 Goal | Improvement |
|--------|----------|----------------|-----------|-------------|
| **Energy** |
| Overall efficiency | 70% | 85% | 90% | +20% |
| Heat recovery | 0% | 5.6% | 10% | N/A |
| **Water** |
| Fresh water (L/flight) | 150 | 100 | 80 | -33% |
| Reuse rate | 0% | 70% | 80% | N/A |
| **Hydrogen** |
| Boil-off rate | 3% /day | 1.5% /day | 1% /day | -50% |
| BOG utilization | 50% | 90% | 95% | +40pp |
| **Materials** |
| Recovery rate | 60% | 72.5% | 80% | +12.5pp |
| Recycled content | 10% | 30% | 50% | +20pp |

## Sensitivity Analysis

### Key Assumptions and Sensitivities

| Parameter | Baseline | Range | Impact on Overall Efficiency |
|-----------|----------|-------|------------------------------|
| Flight duration | 6 hrs | 3-12 hrs | ±5% |
| Passenger load | 150 pax | 100-200 pax | ±3% |
| ECS cooling load | 100 kW | 80-120 kW | ±2% |
| H₂ boil-off rate | 3% /day | 2-5% /day | ±4% |
| Water reuse efficiency | 70% | 50-90% | ±1% |
| Material recovery rate | 72.5% | 60-85% | ±1% (lifecycle) |

## Digital Thread Links

- **MBSE Model**: [04-DIGITAL_THREAD/MBSE_BINDINGS.md](../04-DIGITAL_THREAD/MBSE_BINDINGS.md)
- **Digital Twin**: Real-time energy and mass balance monitoring
- **Telemetry**: [04-DIGITAL_THREAD/DATA_CONTRACTS/](../04-DIGITAL_THREAD/DATA_CONTRACTS/)

## References

- [SYSTEM_OF_SYSTEMS.md](SYSTEM_OF_SYSTEMS.md) - System integration architecture
- [00-README.md](../00-README.md) - Domain overview
- [05-VERIFICATION/](../05-VERIFICATION/) - Test and verification data
