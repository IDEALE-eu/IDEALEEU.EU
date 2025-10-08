# Lifecycle Cost Model

## Overview

The lifecycle cost model provides a comprehensive framework for analyzing total cost of ownership (TCO) across the entire lifecycle of fleet vehicles, from acquisition through retirement, enabling informed decisions on fleet composition, utilization, and management strategies.

## Scope

This model covers all cost categories for both aircraft and spacecraft across their operational lifecycles, typically 20-30 years for aircraft and mission-dependent for spacecraft.

## Cost Categories

### 1. Acquisition Costs

#### Capital Costs
- **Purchase price** - Base vehicle cost
- **Modifications and customization** - Customer-specific changes
- **Initial spares and support equipment** - Ground support, tooling, initial spare parts inventory
- **Training** - Initial crew and maintenance training
- **Certification** - Type certification, airworthiness certificates

#### Financing Costs
- **Down payment** - Initial capital outlay
- **Interest and financing charges** - Cost of borrowed capital
- **Leasing costs** - Operating or capital lease payments

### 2. Operating Costs

#### Direct Operating Costs (DOC)
- **Fuel/propellant** - Consumption based on utilization
- **Crew costs** - Salaries, benefits, per diem, training currency
- **Consumables** - Fluids, oxygen, mission-specific consumables
- **Landing and navigation fees** - Airport/spaceport fees, air traffic control
- **Insurance** - Hull, liability, cargo insurance

#### Indirect Operating Costs (IOC)
- **Station and ground handling** - Ground crew, equipment, facilities
- **Passenger/payload services** - Catering, amenities, handling
- **Administration** - Flight operations management, crew scheduling
- **Sales and marketing** - Commercial operations support
- **General overhead** - Corporate allocation

### 3. Maintenance and Repair Costs

#### Scheduled Maintenance
- **Line maintenance** - Daily and weekly checks, minor repairs
- **Base maintenance** - A, B, C, D checks (aircraft) or equivalent
- **Component overhaul** - Engine, APU, landing gear, avionics overhaul
- **Modifications and upgrades** - Service bulletins, airworthiness directives

#### Unscheduled Maintenance
- **Corrective maintenance** - Unplanned repairs and troubleshooting
- **AOG (Aircraft on Ground) events** - Expedited repairs, emergency spares
- **Damage repair** - Foreign object damage, lightning strikes, incidents

#### MRO Support Costs
- **Spare parts inventory** - Rotables, consumables, insurance spares
- **Maintenance facilities** - Hangars, shops, equipment
- **Tooling and test equipment** - Special tools, GSE
- **Technical support** - Engineering, technical publications, OEM support

### 4. Depreciation and Residual Value

- **Depreciation method** - Straight-line, declining balance, or usage-based
- **Depreciation period** - Economic life (typically 15-25 years)
- **Residual value** - Estimated market value at retirement
- **Mid-life value** - Market value for potential sale or refinancing

### 5. End-of-Life Costs

- **Decommissioning** - Preparation for storage or disposal
- **Storage costs** - If parked before disposal
- **Disposal/recycling** - Dismantling, material recovery, disposal
- **Environmental remediation** - Hazardous materials handling
- **Contract/lease termination** - Return costs, penalties

## Cost Model Structure

### Total Cost of Ownership (TCO)

```
TCO = Acquisition Costs
      + Operating Costs × Utilization × Economic Life
      + Maintenance Costs × Utilization × Economic Life
      + Depreciation
      + End-of-Life Costs
      - Residual Value
```

### Cost per Flight Hour / Mission

```
Cost per Hour = (TCO - Residual Value) / Total Flight Hours over Economic Life
```

### Cost per Mission

```
Cost per Mission = Fixed Costs / Annual Missions
                   + Variable Costs × Mission Duration/Distance
```

## Cost Drivers and Assumptions

### Utilization Assumptions
- Annual flight hours/missions per vehicle
- Mission profile (range, payload, duration)
- Load factor (capacity utilization)

### Cost Escalation
- Fuel price escalation: [X]% per year
- Labor cost escalation: [Y]% per year
- Maintenance cost escalation: [Z]% per year
- General inflation rate: [W]% per year

### Discount Rate
- Weighted average cost of capital (WACC): [R]%
- Used for net present value (NPV) calculations

### Reliability and Maintenance
- Mean time between failures (MTBF)
- Unscheduled maintenance rate
- Component time between overhaul (TBO)
- Age-related maintenance escalation factors

## Model Outputs

### Financial Metrics
- **Total cost of ownership (TCO)** - Lifecycle cost in nominal and NPV
- **Cost per flight hour** - Average and marginal cost
- **Cost per mission** - Fixed and variable components
- **Operating margin** - Revenue minus operating costs
- **Return on investment (ROI)** - For acquisition decisions
- **Payback period** - Time to recover initial investment

### Comparative Analysis
- TCO comparison across vehicle types
- Lease vs. buy analysis
- New vs. used vehicle economics
- In-house vs. outsourced maintenance

### Sensitivity Analysis
- Impact of utilization changes
- Fuel price sensitivity
- Maintenance cost variability
- Residual value scenarios
- Economic life variations

## Applications

### Fleet Planning
- Evaluate new vehicle acquisition business cases
- Compare alternative vehicle types and configurations
- Determine optimal fleet size and mix
- Plan fleet replacement cycles

### Financial Planning
- Annual budget development
- Cash flow forecasting
- Capital investment planning
- Debt and equity financing decisions

### Operational Decisions
- Utilization optimization
- Maintenance strategy selection (cost/reliability trade-offs)
- Life extension vs. replacement decisions
- Make-or-buy decisions for maintenance

### Commercial Decisions
- Pricing and revenue management
- Profitability analysis by route/mission
- Customer contract evaluation
- Outsourcing and partnership decisions

## Model Maintenance

### Data Sources
- Actual operating data from **OPERATIONAL_DATA_HUB/**
- Maintenance costs from **MRO_STRATEGY/** and **04-MAINTENANCE_PLANNING/**
- Market data (fuel prices, labor rates, residual values)
- OEM data (maintenance schedules, component life)
- Industry benchmarks (IATA, ATA, industry reports)

### Update Frequency
- **Monthly**: Actual costs vs. model for variance analysis
- **Quarterly**: Cost escalation factors and market data
- **Annually**: Full model review and recalibration
- **Ad-hoc**: For major decisions or changes

### Model Validation
- Compare model projections to actual costs
- Benchmark against industry data
- Sensitivity testing and scenario analysis
- Peer review and audit

## Governance

### Model Ownership
- Finance: Model maintenance and updates
- Operations: Utilization and operating cost inputs
- Maintenance: MRO cost data and assumptions
- Engineering: Technical parameters and reliability data

### Approval and Use
- Model changes: CFO approval
- Business cases: Must use approved model
- Assumptions: Documented and justified
- Audit trail: Version control and change log

## Best Practices

- Use conservative assumptions for uncertainty
- Conduct sensitivity analysis on key drivers
- Update regularly with actual data
- Benchmark against industry standards
- Consider total cost, not just acquisition price
- Include indirect and hidden costs
- Account for time value of money (discounting)
- Document all assumptions and sources

## Integration

### Upstream Inputs
- Fleet mix strategy: **[FLEET_MIX_STRATEGY.md](FLEET_MIX_STRATEGY.md)**
- Utilization policy: **[UTILISATION_POLICY.md](UTILISATION_POLICY.md)**
- Operational data: **[01-FLEET/OPERATIONAL_DATA_HUB/](../../OPERATIONAL_DATA_HUB/)**
- Maintenance programs: **[04-MAINTENANCE_PLANNING/](../04-MAINTENANCE_PLANNING/)**

### Downstream Outputs
- Cost targets: **[06-COST_OPTIMISATION/](../06-COST_OPTIMISATION/)**
- Financial reporting: **[10-REPORTING/](../10-REPORTING/)**
- Business case support: Executive decision-making
- Budgeting: Annual planning process

## References

- Industry costing standards (ATA, IATA)
- Accounting standards (GAAP, IFRS)
- Should-cost models: **[00-PROGRAM/SUPPLY_CHAIN/11-COSTING/SHOULD_COST_MODELS/](../../../00-PROGRAM/SUPPLY_CHAIN/11-COSTING/SHOULD_COST_MODELS/)**
- Financial planning: **00-PROGRAM/FINANCE/**
