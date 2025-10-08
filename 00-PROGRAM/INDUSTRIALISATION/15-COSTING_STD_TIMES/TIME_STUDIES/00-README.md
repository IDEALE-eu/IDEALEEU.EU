# TIME_STUDIES

Standard time development through time studies and work measurement.

## Overview

Standard times are scientifically established times for operations, used for costing, scheduling, line balancing, and productivity measurement.

## Time Study Methods

### Stopwatch Time Study
- Observe and time actual operations
- Multiple cycles to get average
- Apply rating factor (operator speed vs. normal)
- Add allowances

### Predetermined Time Systems (PTS)
- MTM (Methods-Time Measurement)
- MOST (Maynard Operation Sequence Technique)
- Time based on elemental motions
- No actual timing needed

### Work Sampling
- Random observations of activities
- Determines % time on various activities
- Useful for indirect labor and utilization studies

## Time Study Process

1. **Select operation:** Define scope
2. **Break into elements:** Logical start/stop points
3. **Observe and time:** Multiple cycles (10-20 typical)
4. **Calculate average:** Remove outliers, average times
5. **Apply rating:** Adjust for operator speed (normal = 100%)
6. **Add allowances:** Personal (5%), delay (5%), fatigue (varies)
7. **Calculate standard:** Standard time = (avg time × rating + allowances)

## Rating Factor

- **100%:** Normal pace, sustainable all day
- **>100%:** Faster than normal
- **<100%:** Slower than normal
- Requires trained observer judgment

## Allowances

### Personal Allowance
- Rest room breaks, water, etc.
- Typical: 5%

### Delay Allowance
- Waiting for material, equipment delays
- Typical: 5%

### Fatigue Allowance
- Physical or mental fatigue
- Varies by task difficulty: 4-15%

## Standard Time Application

### Routing Standard Times
- Used in ERP for scheduling and costing
- Setup time + (run time × quantity)

### Line Balancing
- Tasks grouped to meet takt time
- Sum of task times ≤ takt time

### Productivity Measurement
- Standard hours earned / actual hours worked
- Efficiency = (standard hours / actual hours) × 100%
- Target: 85-100% efficiency

### Incentive Pay
- Pay based on standard hours earned
- Encourages productivity above standard

## Learning Curves

### Learning Effect
- As cumulative production increases, time decreases
- Typical aerospace: 80-85% learning curve
- 80% curve: Time reduces 20% per doubling

### Learning Curve Application
- Early units take much longer than mature production
- Plan labor and cost accordingly
- Track actual learning vs. plan

## Time Study Validation

- Multiple observers for consistency
- Re-study periodically (annual or after changes)
- Compare to historical data or benchmarks
- Adjust for process improvements

## Links

- To **SHOULD_COST/** for cost estimation
- To **04-MBOM_ROUTINGS/ROUTINGS/** for routing times
- To **04-MBOM_ROUTINGS/LINE_BALANCING/** for balancing
- To **12-RATE_READINESS/** for capacity planning
- To **19-METRICS/** for productivity tracking
