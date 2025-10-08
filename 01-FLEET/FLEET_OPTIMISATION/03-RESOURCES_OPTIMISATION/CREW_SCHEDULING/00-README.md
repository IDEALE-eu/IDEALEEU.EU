# CREW_SCHEDULING


[← Back to 03-RESOURCES_OPTIMISATION](../00-README.md)

Flight crew and mission operations crew scheduling, pairing, and rostering optimization.

## Overview

Crew scheduling encompasses the complex optimization of assigning qualified personnel to flights and missions while respecting regulatory requirements, contractual obligations, operational needs, and quality of life considerations.

## Scope

### Aircraft Operations
- Flight crew (pilots, flight engineers)
- Cabin crew (flight attendants, pursers)
- Dispatch and flight planning crew
- Operations control center personnel

### Spacecraft Operations
- Mission operations crew (flight directors, controllers)
- Ground station operators
- Launch operations crew
- Mission specialists and payload operators

## Scheduling Process

### 1. Crew Pairing
- Create sequences of flights/shifts assigned to a crew
- Optimize for efficiency and regulation compliance
- Multi-day trips with layovers
- Deadhead positioning when needed
- Training and simulator events integration

### 2. Crew Rostering (Bidding)
- Assign pairings to individual crew members
- Consider crew preferences and seniority
- Balance workload across crew base
- Optimize for cost and quality of life
- Reserve crew allocation

### 3. Real-Time Adjustments
- Irregular operations (IROPS) crew recovery
- Sick calls and absences
- Qualification and currency events
- Training and check ride scheduling

## Constraints and Rules

### Regulatory Requirements (Aircraft)
- Flight Duty Period (FDP) limits
- Rest period requirements
- Maximum flight time (daily, monthly, annual)
- Night operations restrictions
- Time zone and circadian rhythm considerations
- Recency and currency requirements (landings, approaches, routes)

### Regulatory Requirements (Spacecraft)
- Console duty time limits
- Rest between shifts
- Maximum consecutive days on console
- Training and certification currency
- Critical operations manning requirements

### Contractual Obligations
- Union agreements and work rules
- Seniority and bidding systems
- Pay and credit time rules
- Minimum days off and vacation
- Base assignments and commuting

### Operational Requirements
- Qualification requirements (aircraft type, airport, special operations)
- Crew composition (captain, first officer, purser, etc.)
- Language requirements
- Security clearances
- Medical and fitness standards

## Optimization Objectives

### Primary Objectives
- **Safety**: Ensure crew rest and fitness for duty
- **Compliance**: Meet all regulatory and contractual requirements
- **Coverage**: Provide crew for all scheduled operations
- **Cost**: Minimize crew costs (flight pay, per diem, hotel, deadheads)

### Secondary Objectives
- **Quality of Life**: Maximize crew satisfaction and work-life balance
- **Efficiency**: Maximize productive time, minimize idle time
- **Flexibility**: Maintain reserve capacity for disruptions
- **Stability**: Provide predictable schedules

## Crew Pairing Optimization

### Pairing Construction
- Start and end at crew base
- Sequence of flight legs
- Layover locations and durations
- Sit times and ground times
- Deadhead positioning flights

### Pairing Metrics
- **Credit time**: Pay credit hours for the pairing
- **Block time**: Actual flight time
- **Duty time**: FDP for regulatory compliance
- **Time away from base (TAFB)**: Total elapsed time
- **Cost**: Total cost including pay, per diem, hotel, deadheads

### Optimization Techniques
- Set partitioning or set covering formulations
- Column generation and branch-and-price
- Heuristic methods for large problems
- Rolling horizon optimization

## Crew Rostering Optimization

### Roster Construction
- Assign pairings to crew members
- Monthly or bi-weekly roster periods
- Cover all pairings exactly once
- Respect individual constraints (vacation, training, days off)
- Balance workload and flying time

### Bidding Systems
- Crew members bid for pairings or schedules
- Seniority-based or preferential bidding
- Automated bid processing and assignment
- Fallback rules for uncovered pairings

### Metrics
- **Flying hours per crew**: Balance across crew
- **Days off**: Ensure minimum and distribution
- **Work patterns**: Variety and desirability
- **Crew cost**: Total crew expenses
- **Crew satisfaction**: Measure of preference fulfillment

## Reserve Crew Management

### Reserve Types
- **Airport reserve**: On-call at base, short callout
- **Home reserve**: On-call from home, longer callout
- **Long-call reserve**: Advance notice (24+ hours)

### Reserve Sizing
- Historical analysis of crew utilization and disruptions
- Probabilistic modeling of absences and IROPS
- Balance between reserve cost and operational risk
- Seasonal and day-of-week patterns

## Training and Currency

### Recurrent Training
- Annual or periodic simulator training
- Line checks and proficiency checks
- Ground school and regulatory updates
- Schedule integration with operational flying

### Currency Maintenance
- Landings and takeoffs within time period
- Instrument approaches and procedures
- Route and airport qualifications
- Special operations (ETOPS, RVSM, category II/III)

### Training Scheduling
- Coordinate with simulator and instructor availability
- Minimize impact on operational flying
- Clustered training for efficiency
- Just-in-time currency maintenance

## Tools and Systems

### Optimization Software
- Crew pairing optimizer
- Crew rostering and bidding systems
- Reserve management tools
- Qualification and training tracking

### Integration
- Flight schedule interface
- Crew qualification database
- Payroll and timekeeping systems
- Crew communication and mobile apps

## Performance Metrics

### Operational
- Coverage rate (pairings assigned)
- Reserve utilization
- Open time and unfilled flying
- IROPS crew recovery time

### Financial
- Crew cost per block hour
- Per diem and hotel costs
- Deadhead costs
- Overtime and premium pay

### Quality of Life
- Average days off per crew per month
- TAFB per crew per month
- Commutable pairings percentage
- Crew satisfaction surveys

## Best Practices

- Early and frequent optimization runs
- What-if analysis and scenario planning
- Collaborative decision-making with crew representatives
- Continuous improvement based on feedback
- Industry benchmarking
- Technology adoption and automation

## References

- Operational schedules: **02-DEMAND_PLANNING/AIRCRAFT_SCHEDULES/**, **[SPACECRAFT_MISSION_PLAN/](../../02-DEMAND_PLANNING/SPACECRAFT_MISSION_PLAN)**
- Utilization policy: **01-STRATEGY/UTILISATION_POLICY.md**
- Operational performance: **05-OPERATIONAL_PERFORMANCE/**
- Regulations: FAA Part 117, EASA FTL, company policies
