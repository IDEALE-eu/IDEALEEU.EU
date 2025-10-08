# MAKE_BUY

Make versus buy analysis and decisions for components and assemblies.

## Make/Buy Strategy

### Strategic Objectives

1. **Focus on Core Competencies** - Make what differentiates our products
2. **Cost Optimization** - Buy where suppliers have economies of scale
3. **Risk Management** - Balance supply chain risk with control
4. **IP Protection** - Retain critical intellectual property in-house
5. **Quality Assurance** - Ensure supplier capability for critical items

## Make/Buy Decision Framework

### Make Decision Criteria
- **Core Technology** - Strategic IP or differentiation
- **Cost Advantage** - Lower cost to make internally
- **Quality Control** - Requires tight process control
- **Availability** - Not available from qualified suppliers
- **Capacity Utilization** - Effective use of internal resources

### Buy Decision Criteria
- **Commodity Items** - Standard, available from multiple sources
- **Specialized Capability** - Supplier has superior technology/capability
- **Cost Disadvantage** - Supplier economies of scale
- **Non-Core** - Does not provide competitive advantage
- **Capital Avoidance** - Avoid large equipment investments

## Component Categories

### Category 1: Strategic Make Items
**Criteria:** Core IP, critical to performance, competitive differentiation

**Aircraft Examples:**
- Wing spar integration (proprietary design)
- Flight control actuation systems (core technology)
- Hydrogen fuel system integration (differentiation)
- Final assembly and system integration

**Spacecraft Examples:**
- Propulsion system integration (core technology)
- GNC algorithm implementation (strategic IP)
- Spacecraft bus integration (differentiation)
- AIT (Assembly, Integration, Test) processes

**Rationale:** These items contain core intellectual property and provide competitive differentiation. Internal control ensures quality and protects IP.

### Category 2: Tactical Make Items
**Criteria:** Cost-effective to make, utilize internal capacity, quality critical

**Aircraft Examples:**
- Simple machined brackets
- Wire harness assembly (EWIS)
- Composite layup for non-critical structures
- Minor sub-assembly operations

**Spacecraft Examples:**
- Harness integration
- Simple mechanical assemblies
- Thermal blanket integration
- GSE (Ground Support Equipment) adapters

**Rationale:** Cost-effective to produce internally, helps maintain workforce utilization, and provides flexibility.

### Category 3: Strategic Buy Items
**Criteria:** Specialized supplier capability, proven reliability, non-core

**Aircraft Examples:**
- Landing gear (specialized supplier)
- Avionics systems (certified suppliers)
- Engines/propulsion units (OEM)
- Environmental control systems

**Spacecraft Examples:**
- Reaction wheels (specialized supplier)
- Solar panels (proven supplier)
- Star trackers (certified supplier)
- Batteries (specialized technology)

**Rationale:** Suppliers have specialized capabilities, certifications, and proven track records. Leverage their expertise and economies of scale.

### Category 4: Commodity Buy Items
**Criteria:** Standard items, multiple sources, cost-effective

**Aircraft Examples:**
- Standard fasteners and hardware
- Electrical connectors (standard)
- Hydraulic fittings (standard)
- Sealants and adhesives

**Spacecraft Examples:**
- Standard fasteners (space-rated)
- Electrical connectors (standard)
- Thermal interface materials
- Multilayer insulation (MLI) materials

**Rationale:** Readily available from multiple suppliers, no competitive advantage to making internally, cost-effective to buy.

## Make/Buy Matrix

| Component/Assembly | Category | Decision | Supplier Count | Risk Level |
|-------------------|----------|----------|----------------|------------|
| Wing structure | Strategic Make | Make | N/A | Low |
| Landing gear | Strategic Buy | Buy | 2 | Medium |
| Avionics | Strategic Buy | Buy | 3 | Medium |
| Fasteners | Commodity Buy | Buy | 5+ | Low |
| Wire harness | Tactical Make | Make | N/A | Low |
| Composite panels | Tactical Make | Make | N/A | Low |
| Hydraulic actuators | Strategic Buy | Buy | 2 | Medium |
| Propulsion (S/C) | Strategic Buy | Buy | 1 | High |
| GNC software | Strategic Make | Make | N/A | Low |
| Solar arrays | Strategic Buy | Buy | 2 | Medium |

## Supplier Management Strategy

### Single Source Items (High Risk)
- Develop close partnership with supplier
- Implement APQP and PPAP rigorously
- Consider second source qualification
- Maintain strategic inventory buffer

### Dual Source Items (Medium Risk)
- Qualify multiple suppliers
- Split production to maintain competition
- Use APQP for both suppliers
- Monitor performance metrics

### Multi-Source Items (Low Risk)
- Competitive bidding process
- Performance-based supplier selection
- Standard PPAP requirements
- Market-based pricing

## Cost Analysis Considerations

### Make Cost Components
1. **Direct Material** - Raw material costs
2. **Direct Labor** - Manufacturing labor with burden
3. **Overhead** - Factory overhead allocation
4. **Equipment Depreciation** - Capital equipment costs
5. **Quality/Rework** - Scrap and rework costs
6. **Inventory Carrying** - WIP and raw material inventory

### Buy Cost Components
1. **Purchase Price** - Supplier quoted price
2. **Transportation** - Inbound freight
3. **Receiving Inspection** - Incoming quality costs
4. **Supplier Management** - APQP, audits, supplier quality
5. **Inventory Carrying** - Safety stock and buffer inventory
6. **Risk Premium** - Supply chain disruption risk

## Decision Review Process

### Annual Review Cycle
- Review all make/buy decisions annually
- Assess cost changes and market conditions
- Evaluate supplier performance
- Consider new technologies and capabilities
- Update make/buy matrix

### Triggered Reviews
- Significant cost variance (>10%)
- Quality issues or supplier problems
- Technology changes
- Capacity constraints
- Business strategy changes

## Transition Planning

### Make-to-Buy Transition
1. Qualify suppliers (APQP process)
2. Parallel production phase
3. Process validation (PPAP)
4. Transfer production knowledge
5. Phase out internal production
6. Manage equipment disposition

### Buy-to-Make Transition
1. Technology/process development
2. Equipment procurement and installation
3. Workforce hiring and training
4. Process validation and qualification
5. Supplier phase-out plan
6. Production ramp-up

## Metrics

### Make/Buy Performance Metrics
- **Cost Variance:** Target vs. Actual (Make and Buy)
- **Quality:** Defect rates for make vs. buy items
- **Delivery:** On-time delivery performance
- **Lead Time:** Make cycle time vs. buy lead time
- **Flexibility:** Response to engineering changes
- **Capacity Utilization:** Internal equipment and labor utilization

## References

- Link to **07-SUPPLIER_INDUSTRIALISATION** for buy item management
- Link to **15-COSTING_STD_TIMES** for cost analysis
- Link to **03-PROCESS_PLANNING** for make item processes
- Link to **12-RATE_READINESS** for capacity planning
