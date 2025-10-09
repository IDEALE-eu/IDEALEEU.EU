# System of Systems - Circular Systems Integration

## Overview

This document describes the system-of-systems architecture for the CIRCULAR_SYSTEMS_MATERIALS domain, showing how ATA-21 (Air Conditioning), ATA-28 (Fuel/H₂), ATA-38 (Water/Waste), and MTL-CIRCULARITY interact to form closed-loop circular systems.

## System of Systems Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    CIRCULAR SYSTEMS DOMAIN                       │
└─────────────────────────────────────────────────────────────────┘
         │                    │                    │
    ┌────▼─────┐        ┌────▼─────┐        ┌────▼─────┐
    │  ATA-21  │        │  ATA-28  │        │  ATA-38  │
    │   ECS    │◄──────►│  Fuel/H₂ │◄──────►│Water/Waste│
    └────┬─────┘        └────┬─────┘        └────┬─────┘
         │                    │                    │
         │                    ▼                    │
         │           ┌─────────────────┐          │
         └──────────►│ MTL-CIRCULARITY │◄─────────┘
                     └─────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  Supply Chain    │
                    │ Reverse Logistics│
                    └──────────────────┘
```

## Closed-Loop Systems

### 1. Thermal Loop
**Purpose**: Optimize thermal energy management across systems

```
┌─────────────────────────────────────────────────────────────┐
│                     THERMAL LOOP                             │
└─────────────────────────────────────────────────────────────┘

Avionics Heat → ECS Cooling Loop → Heat Exchanger
                      │                    ▲
                      ▼                    │
                Cabin Heating         H₂ Pre-conditioning
                      │                    │
                      └─────► Waste Heat → Fuel/H₂ System
```

**Key Flows**:
- ECS rejects 10-20 kW to H₂ boil-off cooling
- H₂ pre-conditioning reduces boil-off by 30-50%
- Cabin waste heat used for water heating (ATA-38)
- Net thermal efficiency improvement: 15-20%

### 2. Water Loop
**Purpose**: Maximize water reuse and minimize fresh water requirement

```
┌─────────────────────────────────────────────────────────────┐
│                      WATER LOOP                              │
└─────────────────────────────────────────────────────────────┘

Fresh Water → Galleys/Lavatories → Usage
    ▲              │
    │              ▼
    │         Greywater → Treatment → Reclaimed Water
    │              │                        │
    │              ▼                        ▼
    │      Blackwater/Waste            Non-potable Use
    │                                   (toilets, cleaning)
    │
    └──────── ECS Condensate (5-10 L/hr)
```

**Key Flows**:
- ECS condensate: 5-10 L/hr (flight conditions dependent)
- Greywater treatment: 50 L/hr capacity
- Reclamation efficiency: 70% of greywater
- Fresh water reduction: 50-60% compared to baseline

### 3. Hydrogen Loop
**Purpose**: Optimize H₂ storage, distribution, and boil-off management

```
┌─────────────────────────────────────────────────────────────┐
│                     HYDROGEN LOOP                            │
└─────────────────────────────────────────────────────────────┘

LH₂ Tank → Boil-off Gas (BOG) → Priority: Engine/Fuel Cell
   │              │                      │
   │              └──► Secondary: Vent   │
   │                                     │
   └─► Thermal Integration ◄─────── ECS Heat Rejection
        (reduces BOG by 30-50%)
```

**Key Flows**:
- Passive boil-off: 1-3% per day
- Active cooling via ECS: reduces BOG to < 1.5% per day
- BOG utilization: 90%+ (engine, fuel cell, or controlled vent)
- Net H₂ efficiency improvement: 25-35%

### 4. Material Circularity Loop
**Purpose**: Maximize material reuse, repair, refurbishment, and recycling

```
┌─────────────────────────────────────────────────────────────┐
│                 MATERIAL CIRCULARITY LOOP                    │
└─────────────────────────────────────────────────────────────┘

Design → Production → Use → End-of-Life Assessment
  ▲          ▲         │            │
  │          │         └────────────┼───► Reuse (30%)
  │          │                      │
  │          │                      ├───► Repair (20%)
  │          │                      │
  │          └──────────────────────├───► Refurbish (15%)
  │                                 │
  └─────────────────────────────────┴───► Recycle (35%)
```

**Key Flows**:
- Material passports track composition for all components
- LCA/LCC models guide design decisions
- Reverse logistics for end-of-life component return
- Target: 80%+ material recovery rate

## Integration Points

### Thermal-H₂ Integration (ATA-21 ↔ ATA-28)
- **Heat Exchanger**: Glycol loop between ECS and H₂ tank
- **Control Strategy**: Maintain H₂ tank within -253°C to -250°C
- **Benefits**: 
  - Reduce H₂ boil-off by 30-50%
  - Reduce ECS cooling load by 10-15%
  - Improve overall system efficiency by 15-20%

### Water-ECS Integration (ATA-38 ↔ ATA-21)
- **Condensate Recovery**: ECS pack condensate → water treatment
- **Flow Rate**: 5-10 L/hr (varies with altitude, humidity)
- **Benefits**:
  - Reduce fresh water requirement by 10-15%
  - Reduce water tank size and weight
  - Improve overall water system efficiency

### Material-Design Integration (MTL ↔ All Systems)
- **Material Passports**: Track all components for end-of-life
- **LCA Integration**: Environmental impact in design decisions
- **Benefits**:
  - 80%+ material recyclability
  - 40% lifecycle CO₂ reduction target
  - Closed-loop material supply

## Performance Metrics

### System-Level KPIs

| Metric | Target | Baseline | Improvement |
|--------|--------|----------|-------------|
| Thermal efficiency | 80% | 65% | +15% |
| Water reuse rate | 70% | 0% | +70% |
| H₂ boil-off rate | < 1.5% /day | 2.5% /day | -40% |
| Material recyclability | > 80% | 60% | +20% |

### Energy and Mass Balance
See [ENERGY_MASS_BALANCE.md](ENERGY_MASS_BALANCE.md) for detailed analysis.

## Failure Modes and Redundancy

### Single-System Failures
- **ECS Failure**: Backup cooling via ambient heat exchanger
- **H₂ System Failure**: Switch to conventional fuel (if hybrid)
- **Water Treatment Failure**: Use fresh water reserves
- **Material Passport Unavailable**: Conservative end-of-life handling

### Cross-System Failures
- **ECS + H₂ Thermal Link Failure**: Independent cooling for H₂, reduced efficiency
- **ECS + Water Condensate Failure**: Use fresh water only
- **Multiple System Failures**: Safe degradation to basic functionality

## Digital Thread Integration

### MBSE Model
- System-of-systems architecture in SysML
- Interface requirements and allocations
- See [04-DIGITAL_THREAD/MBSE_BINDINGS.md](../04-DIGITAL_THREAD/MBSE_BINDINGS.md)

### Digital Twin
- Real-time system-of-systems monitoring
- Performance optimization algorithms
- See [04-DIGITAL_THREAD/TWIN_ANCHORS.md](../04-DIGITAL_THREAD/TWIN_ANCHORS.md)

### Telemetry and Data Contracts
- System-level telemetry schema
- Cross-system data exchange
- See [04-DIGITAL_THREAD/DATA_CONTRACTS/](../04-DIGITAL_THREAD/DATA_CONTRACTS/)

## Compliance and Certification

### System-of-Systems Certification
- **ARP4754A**: System development process
- **ARP4761**: Safety assessment process
- **CS-25**: Airworthiness standards

### Interface Certification
- Individual ICD compliance
- Integration testing and verification
- See [05-VERIFICATION/VVP_PLAN.md](../05-VERIFICATION/VVP_PLAN.md)

## References

- [00-README.md](../00-README.md) - Domain overview
- [02-INTERFACES/](../02-INTERFACES/) - Interface definitions
- [ENERGY_MASS_BALANCE.md](ENERGY_MASS_BALANCE.md) - Energy and mass balance
- [00-PROGRAM/DIGITAL_THREAD/](../../../00-PROGRAM/DIGITAL_THREAD/) - Digital thread framework
