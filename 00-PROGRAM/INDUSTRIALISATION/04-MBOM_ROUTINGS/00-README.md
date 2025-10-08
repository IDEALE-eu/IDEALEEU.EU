# 04-MBOM_ROUTINGS

Manufacturing Bill of Materials (MBOM), routings, and line balancing documentation.

## Contents

- **00-README.md** - This file
- **MBOM/** - Manufacturing Bill of Materials
- **ROUTINGS/** - Manufacturing routings and operation sequences
- **LINE_BALANCING/** - Line balancing analysis and optimization

## Overview

MBOM and routings define what components are needed and how they flow through manufacturing operations. This information drives MRP (Material Requirements Planning), shop floor execution, and capacity planning.

## MBOM vs. EBOM

### EBOM (Engineering BOM)
- Design intent and functional decomposition
- "What" the product is designed to be
- Managed in PLM/PDM system
- Engineering change control

### MBOM (Manufacturing BOM)
- How the product is built
- "How" the product is assembled
- Manufacturing sequence and groupings
- Includes manufacturing aids (fixtures, tooling)

### EBOM → MBOM Transformation
- Re-structure for manufacturing sequence
- Add phantom assemblies for sub-assembly
- Include consumables (fasteners, sealant, etc.)
- Add manufacturing aids not in EBOM

## Key Components

### MBOM Structure
- **Part Number:** Unique identifier
- **Quantity:** Per assembly
- **Unit of Measure:** EA, LB, FT, etc.
- **Lead Time:** Procurement or manufacturing lead time
- **Source:** Make vs. Buy
- **Level:** Assembly hierarchy level

### Routing
- **Operation Number:** Sequential (10, 20, 30...)
- **Operation Description:** What is done
- **Work Center:** Where it is done
- **Standard Time:** Setup and run time
- **Tooling:** Required tools and fixtures
- **Materials:** Components consumed
- **Quality:** Inspection requirements

## Integration with ERP

### MRP (Material Requirements Planning)
- MBOM drives material demand
- Routing drives capacity requirements
- Lead times for scheduling
- Make/buy decisions

### Shop Floor Control
- Work orders generated from MBOM/routing
- Material kitting and staging
- Operation tracking and labor reporting
- Quality data collection

## Line Balancing

### Objectives
- Achieve target takt time
- Minimize idle time and WIP
- Balance workload across stations
- Maximize efficiency

### Methodology
- List all tasks and times
- Calculate takt time from demand
- Group tasks into stations
- Iteratively optimize balance

## References

- Link to **01-STRATEGY/MAKE_BUY.md** for sourcing decisions
- Link to **03-PROCESS_PLANNING/PROCESS_FLOW.md** for operation details
- Link to **16-IT_INTEGRATION/ERP/** for system integration
- Link to **12-RATE_READINESS/** for capacity planning
