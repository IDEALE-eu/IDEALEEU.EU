# SPARES_INVENTORY_OPTIMISATION


[← Back to 03-RESOURCES_OPTIMISATION](../00-README.md)

Spare parts inventory optimization, positioning, and logistics for fleet maintenance support.

## Overview

Spares inventory optimization ensures the availability of spare parts to support maintenance operations while minimizing inventory carrying costs, through strategic positioning, inventory level optimization, and efficient logistics.

## Objectives

### Operational
- Ensure spare parts availability to prevent AOG (Aircraft on Ground) / SOG (Spacecraft on Ground)
- Minimize maintenance delays due to parts unavailability
- Support scheduled and unscheduled maintenance
- Enable rapid response to operational needs

### Financial
- Minimize total inventory investment
- Reduce inventory carrying costs
- Optimize obsolescence and excess risk
- Maximize inventory turns
- Balance holding costs vs. shortage costs

### Strategic
- Strategic positioning of high-value and critical spares
- Pooling and sharing arrangements
- Supplier partnerships and consignment
- Lifecycle inventory planning

## Inventory Categories

### Rotable Components
- High-value repairable items (engines, landing gear, APUs, avionics)
- Repairable and cycle through overhaul/repair
- Managed as pool of serviceable and unserviceable assets
- Tracking and forecasting of repair turnaround time (TAT)

### Expendable Parts
- Consumable items replaced during maintenance
- Low to medium value, not repairable
- Fasteners, seals, filters, fluids, consumables
- Economic order quantity (EOQ) and reorder point models

### Insurance Spares
- High-value, long lead time, low failure rate items
- Held as insurance against rare but critical failures
- Shared across fleet or industry through pooling
- Expensive to hold but catastrophic if unavailable

### Consumables
- Fluids (oil, hydraulic, coolant)
- Cleaning and servicing materials
- Safety and protective equipment
- Regular replenishment based on usage

## Inventory Optimization Models

### Reorder Point / Safety Stock
```
Reorder Point = (Average Demand × Lead Time) + Safety Stock
Safety Stock = Z × σ × √(Lead Time)

Where:
- Z = Service level factor (e.g., 1.65 for 95% service level)
- σ = Standard deviation of demand
- Lead Time = Procurement or repair lead time
```

### Economic Order Quantity (EOQ)
```
EOQ = √((2 × Annual Demand × Order Cost) / Holding Cost per Unit)
```

### Multi-Echelon Optimization
- Optimize inventory across multiple locations (bases, hubs, central warehouse)
- Balance centralized vs. decentralized inventory
- Lateral transshipment and emergency pooling
- Network design and inventory positioning

### Rotable Pool Sizing
```
Pool Size = Flight Line Demand + Repair Pipeline + Safety Stock
Where:
- Flight Line Demand = Fleet size × Installation rate
- Repair Pipeline = Removal rate × Repair TAT
- Safety Stock = Buffer for variability in removals and TAT
```

## Spare Parts Positioning

### Geographic Distribution
- **Central Warehouse**: Low-frequency, high-value items
- **Regional Hubs**: Medium-frequency items for multiple bases
- **Base Stock**: High-frequency, quick-turnaround items
- **Aircraft/Spacecraft**: Consumables and critical spares carried on vehicle

### Pooling Strategies
- **Fleet Pooling**: Share spares across own fleet
- **Airline/Operator Pooling**: Consortiums for common types
- **OEM Pooling**: Manufacturer-managed spare parts programs
- **Exchange and Loaner Programs**: Temporary spares for AOG

### Strategic Pre-Positioning
- High-demand stations and hubs
- Remote or difficult-to-reach locations
- Seasonal demand considerations
- New route or mission startup inventory

## Demand Forecasting

### Deterministic Demand
- Scheduled maintenance and life-limited parts
- Known replacement intervals
- Planned modifications and upgrades
- Predictable based on flight hours or cycles

### Stochastic Demand
- Unscheduled maintenance and random failures
- Forecast based on historical failure rates
- Reliability data (MTBF, Weibull distribution)
- Variability and uncertainty modeling

### Forecasting Methods
- Exponential smoothing for stable demand
- Moving averages for seasonal demand
- Regression models for trend and drivers (e.g., flight hours)
- Reliability-based prediction (survival analysis)

## Supply Chain and Logistics

### Procurement
- Lead time management and reduction
- Supplier performance and reliability
- Make-or-buy decisions
- Strategic sourcing and partnerships

### Replenishment
- Automatic reorder triggers
- Expedited and AOG procurement
- Kanban and visual management
- Vendor-managed inventory (VMI)

### Logistics and Distribution
- Transportation modes and costs (air, ground, sea)
- Expedited shipping for AOG situations
- Customs and international shipments
- Reverse logistics for repairs and returns

### Repair and Overhaul
- In-house vs. outsourced repair
- Repair turnaround time (TAT) management
- Beyond economical repair (BER) decisions
- Component reliability improvement

## Inventory Control Policies

### Service Level Targets
- **Critical Parts**: 95-99% availability (no stockouts)
- **Routine Parts**: 90-95% availability
- **Low-Priority Parts**: 85-90% availability

### ABC Classification
- **A Items**: High value, tight control, frequent review
- **B Items**: Moderate value and control
- **C Items**: Low value, simple replenishment rules

### Inventory Review
- Continuous review (reorder point triggered)
- Periodic review (fixed intervals, order-up-to level)
- Hybrid approaches

## Cost Components

### Holding Costs
- Capital cost (cost of money tied up in inventory)
- Warehousing and storage costs
- Insurance and taxes
- Obsolescence and deterioration risk
- Typical: 15-30% of inventory value per year

### Ordering Costs
- Purchase order processing
- Transportation and logistics
- Inspection and receiving
- Typical: Fixed cost per order

### Shortage Costs
- AOG/SOG costs (lost revenue, recovery costs)
- Maintenance delay costs
- Expedited procurement and shipping
- Customer dissatisfaction and penalties

## Performance Metrics

### Availability
- **Fill rate**: Percentage of demand met from stock
- **Backorder rate**: Percentage of demand not immediately satisfied
- **AOG/SOG incidents**: Number and duration of grounding events

### Financial
- **Inventory investment**: Total value of inventory
- **Inventory turns**: Annual usage / average inventory value
- **Days of supply**: Inventory on hand / average daily demand
- **Carrying cost**: Annual cost as % of inventory value
- **Excess and obsolete (E&O)**: Value of aged or surplus inventory

### Efficiency
- **Order fulfillment time**: Time from requisition to delivery
- **Emergency procurement rate**: Percentage of expedited orders
- **Stock accuracy**: Physical vs. system inventory match
- **Supplier performance**: On-time delivery, quality

## Technology and Systems

### Inventory Management Systems
- ERP integration (SAP, Oracle)
- Specialized aerospace MRO systems (Ramco, IFS)
- Warehouse management systems (WMS)
- Mobile devices and barcode/RFID tracking

### Analytics and Optimization
- Demand forecasting algorithms
- Multi-echelon inventory optimization software
- Monte Carlo simulation for uncertainty
- Machine learning for failure prediction

### Integration
- Maintenance planning systems: **04-MAINTENANCE_PLANNING/**
- Operational data: **01-FLEET/OPERATIONAL_DATA_HUB/**
- Procurement systems: **00-PROGRAM/SUPPLY_CHAIN/04-PROCUREMENT/**
- Financial systems: Budgeting and cost tracking

## Best Practices

### Planning and Optimization
- Use data-driven models, not intuition alone
- Balance service level and cost trade-offs
- Continuously refine forecasts with actual data
- Scenario analysis and sensitivity testing

### Execution and Control
- Accurate and timely data capture
- Real-time visibility across supply chain
- Exception management and alerts
- Periodic physical inventory audits

### Collaboration
- Cross-functional planning (ops, maintenance, procurement, finance)
- Supplier partnerships and VMI programs
- Industry pooling and consortiums
- Share best practices and benchmarks

### Continuous Improvement
- Review metrics and KPIs regularly
- Root cause analysis of stockouts and excess
- Implement lean and Six Sigma principles
- Technology adoption and automation

## Special Topics

### New Aircraft/Spacecraft Introduction
- Initial provisioning and ramp-up inventory
- Uncertain demand and reliability data
- Higher safety stock during maturation
- Rapid adjustment as data becomes available

### Fleet Retirement
- Wind-down inventory planning
- Last-time-buy decisions
- Disposal or resale of excess inventory
- Parts support for legacy systems

### Predictive Maintenance Impact
- Shift from reactive to proactive parts demand
- Reduced unscheduled maintenance and surprise failures
- Better demand predictability
- Potential inventory reduction opportunity

## References

- Maintenance planning: **04-MAINTENANCE_PLANNING/**
- Operational data: **01-FLEET/OPERATIONAL_DATA_HUB/**
- Procurement: **00-PROGRAM/SUPPLY_CHAIN/04-PROCUREMENT/**
- Demand planning: **00-PROGRAM/SUPPLY_CHAIN/09-PLANNING/**
- Template: **11-TEMPLATES/SPARES_OPTIMISATION_INPUTS.csv**
