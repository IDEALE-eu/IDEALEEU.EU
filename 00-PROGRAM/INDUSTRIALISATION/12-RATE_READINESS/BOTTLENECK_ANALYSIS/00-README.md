# BOTTLENECK_ANALYSIS

Bottleneck identification and mitigation strategies.

## Overview

Bottlenecks are constraint operations limiting overall production throughput. Focusing on bottleneck improvement yields maximum benefit.

## Bottleneck Identification

### Capacity Analysis
- Calculate capacity at each work center
- Bottleneck = highest utilization
- May change with product mix or volume

### Observation
- WIP accumulates before bottleneck
- Bottleneck operates continuously (high utilization)
- Downstream operations starved for work

## Bottleneck Management

### Protect the Bottleneck
- Ensure material always available
- Preventive maintenance to avoid downtime
- Highest skill operators
- Buffer inventory before bottleneck

### Exploit the Bottleneck
- Maximize uptime (reduce setup, breaks on bottleneck)
- Run bottleneck during breaks/lunch (stagger crew)
- Improve quality at bottleneck (no scrap or rework)
- Optimize batch sizes for bottleneck

### Elevate the Bottleneck
- Add capacity (equipment, shifts, overtime)
- Reduce cycle time (process improvement, automation)
- Offload work (outsource or alternate routing)

### Subordinate Non-Bottlenecks
- Pace non-bottlenecks to bottleneck rate
- Don't overproduce (creates WIP)
- Focus improvement efforts on bottleneck first

## Theory of Constraints (TOC)

1. **Identify** the constraint (bottleneck)
2. **Exploit** the constraint (maximize its output)
3. **Subordinate** everything else to the constraint
4. **Elevate** the constraint (add capacity)
5. **Repeat:** New bottleneck emerges, start over

## Bottleneck Mitigation Strategies

### Short-Term
- Add shifts or overtime at bottleneck
- Transfer operators to bottleneck
- Defer non-bottleneck maintenance
- Rush parts through bottleneck

### Long-Term
- Invest in additional equipment
- Automate bottleneck operation
- Redesign process to reduce cycle time
- Outsource bottleneck operation

## Links

- To **CAPACITY_MODEL/** for capacity analysis
- To **TAKT_OEE/** for performance data
- To **02-FACTORY_DESIGN/LINE_DESIGN/** for line layout
- To **04-MBOM_ROUTINGS/LINE_BALANCING/** for balancing
