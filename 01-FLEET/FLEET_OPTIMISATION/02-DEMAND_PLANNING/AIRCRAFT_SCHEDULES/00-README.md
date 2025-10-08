# AIRCRAFT_SCHEDULES


[← Back to 02-DEMAND_PLANNING](../00-README.md)

Flight schedules, route planning, and aircraft assignment optimization.

## Overview

Aircraft scheduling encompasses the development, optimization, and management of flight schedules that balance demand, fleet availability, crew resources, and operational constraints to maximize efficiency and profitability.

## Schedule Development Process

### 1. Network Planning
- Route selection and prioritization
- Frequency determination
- Seasonal adjustments
- Hub-and-spoke vs. point-to-point strategies

### 2. Fleet Assignment
- Match aircraft type to route demand and characteristics
- Optimize utilization and load factors
- Balance maintenance requirements
- Consider crew base locations

### 3. Aircraft Routing
- Multi-day routing patterns
- Minimize deadhead positioning
- Maximize utilization while respecting duty limits
- Maintenance opportunity integration

### 4. Schedule Optimization
- Integer programming and heuristic algorithms
- Revenue optimization
- Cost minimization
- Constraint satisfaction

## Schedule Types

### Published Schedule
- Customer-facing flight schedule
- Advance publication (6-12 months)
- Seasonal schedules (IATA seasons)
- Stable for booking and planning

### Operational Schedule
- Day-of-operations executable schedule
- Real-time updates for disruptions
- Crew and aircraft assignments
- Ground resource coordination

### Contingency Schedule
- Irregular operations (IROPS) recovery
- Weather and disruption scenarios
- Reserve capacity deployment
- Customer rebooking priorities

## Key Components

### Flight Leg
- Origin and destination
- Scheduled departure and arrival times
- Aircraft type assignment
- Flight number and marketing info

### Aircraft Rotation
- Sequence of flights assigned to a specific aircraft
- Overnight (RON) positioning
- Maintenance opportunity windows
- Multi-day patterns

### Block Time
- Scheduled flight time (gate-to-gate)
- Includes taxi time
- Buffer for weather and traffic
- Historical performance-based

### Ground Time
- Turnaround time between flights
- Station-specific minimums
- Through flights vs. terminating
- Maintenance and servicing requirements

## Constraints and Considerations

### Operational Constraints
- Aircraft availability and maintenance windows
- Crew availability and duty time regulations
- Airport/airspace capacity and slots
- Ground handling and gate availability
- Curfews and noise restrictions

### Commercial Constraints
- Demand patterns and market requirements
- Competitive positioning
- Connecting bank structures (for hubs)
- Codeshare and alliance coordination
- Contractual commitments

### Economic Factors
- Route profitability and yield
- Operating costs (fuel, crew, handling)
- Load factor and revenue optimization
- Seasonal demand variations

## Schedule Metrics

### Utilization
- Block hours per aircraft per day
- Daily cycles per aircraft
- Annual utilization per aircraft

### Efficiency
- Average stage length
- Turn time performance
- On-time performance (OTP)
- Misconnections and disruptions

### Financial
- Revenue per available seat-kilometer (RASK)
- Cost per available seat-kilometer (CASK)
- Load factor
- Yield per passenger-kilometer

## Schedule Management

### Planning Horizon
- **Long-term** (12+ months): Network planning, fleet requirements
- **Medium-term** (3-12 months): Detailed schedule development
- **Short-term** (0-3 months): Final adjustments and optimization
- **Day-of-operations**: Real-time execution and disruption management

### Update Cycle
- Annual schedule planning
- Seasonal schedule updates (IATA summer/winter)
- Monthly rolling updates
- Daily operational adjustments

### Tools and Systems
- Schedule optimization software
- Crew pairing and rostering integration
- Flight operations systems
- Dispatch and flight planning systems

## Integration

### Crew Scheduling
- Coordinate with **03-RESOURCES_OPTIMISATION/CREW_SCHEDULING/**
- Ensure crew availability for all flights
- Optimize crew productivity and costs
- Comply with duty time regulations

### Maintenance Planning
- Align with **04-MAINTENANCE_PLANNING/**
- Schedule maintenance windows
- Balance utilization with maintenance needs
- Minimize out-of-service time

### Ground Operations
- Coordinate with **03-RESOURCES_OPTIMISATION/GROUND_CREW_ROSTERING/**
- Ensure ground handling capacity
- Gate and stand allocation
- Turnaround time optimization

## Best Practices

- Data-driven demand forecasting
- Continuous optimization and improvement
- Scenario planning and contingency preparation
- Cross-functional coordination
- Performance monitoring and feedback
- Industry benchmarking

## References

- Capacity forecasting: **[CAPACITY_FORECASTING.md](../CAPACITY_FORECASTING.md)**
- Utilization policy: **01-STRATEGY/UTILISATION_POLICY.md**
- Crew scheduling: **03-RESOURCES_OPTIMISATION/CREW_SCHEDULING/**
- Operational performance: **05-OPERATIONAL_PERFORMANCE/**
