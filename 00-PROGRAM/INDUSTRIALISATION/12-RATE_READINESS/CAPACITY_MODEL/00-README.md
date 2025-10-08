# CAPACITY_MODEL

Production capacity modeling and analysis.

## Overview

Capacity models calculate theoretical and practical capacity for each work center, identifying constraints and investment needs.

## Capacity Model Components

### Work Center Capacity
- Equipment hours available (shifts × days × hours)
- Minus downtime (maintenance, changeovers, breaks)
- Equals net available capacity

### Operation Capacity
- Standard time per unit (from routing)
- Setup time (if applicable)
- Batch size effects

### Capacity Calculation
- **Theoretical capacity:** No downtime, 100% efficiency
- **Rated capacity:** Includes planned downtime, realistic efficiency
- **Demonstrated capacity:** Actual production experience

## Capacity Analysis

### Utilization
- Capacity utilization = Actual output / Rated capacity
- Target: 75-85% sustained (allows for variability and improvement)
- >90% indicates constraint, risk of delays

### Bottlenecks
- Work center with highest utilization
- Constrains overall production rate
- Focus improvement efforts here

## Capacity Planning

### Growth Scenarios
- Model capacity at different production rates
- Identify when additional capacity needed
- Plan equipment purchases and installations

### Investment Decisions
- Bottleneck relief (add equipment, reduce cycle time)
- Automation opportunities
- Additional shifts vs. equipment

## Links

- To **04-MBOM_ROUTINGS/ROUTINGS/** for standard times
- To **BOTTLENECK_ANALYSIS/** for constraint management
- To **TAKT_OEE/** for performance data
