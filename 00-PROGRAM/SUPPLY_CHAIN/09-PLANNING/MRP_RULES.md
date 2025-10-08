# Material Requirements Planning (MRP) Rules

## Overview

MRP parameters and rules for material planning and procurement.

## MRP Parameters by Part

### Lead Time
- **Procurement Lead Time:** Time from PO to receipt
- **Manufacturing Lead Time:** Production time
- **Cumulative Lead Time:** Total supply chain time
- Regular review and update based on actual performance

### Lot Sizing Rules

**Lot-for-Lot (L4L):**
- Order exactly what's needed
- Used for expensive or low-volume items
- Minimizes inventory

**Fixed Order Quantity (FOQ):**
- Standard order quantity (e.g., MOQ, carton qty)
- Simplifies ordering
- May create excess inventory

**Economic Order Quantity (EOQ):**
- Balances order costs and carrying costs
- Formula: EOQ = √(2DS/H) where D=demand, S=order cost, H=holding cost
- Used for high-volume items

**Period Order Quantity (POQ):**
- Orders to cover fixed time period (e.g., 2 months)
- Balances ordering frequency and inventory

### Safety Stock
- Buffer against demand variability and supply uncertainty
- Calculated based on service level target
- Formula: SS = Z × σ × √LT
  - Z = service level factor (e.g., 1.65 for 95%)
  - σ = demand standard deviation
  - LT = lead time in same units

### Reorder Point
- Triggers replenishment order
- Formula: ROP = (Demand per day × Lead time) + Safety stock
- Dynamic adjustment based on actual consumption

## Planning Strategies

### Make-to-Stock (MTS)
- Forecast-driven production
- Standard products, known demand
- MRP based on forecast and safety stock
- Inventory cushion

### Make-to-Order (MTO)
- Customer order-driven
- Custom or low-volume products
- MRP based on actual orders
- Minimal finished goods inventory

### Assemble-to-Order (ATO)
- Component inventory, final assembly to order
- Postponement strategy
- MRP for components, assembly schedule to order
- Flexibility with lower inventory

## Netting Logic

### Gross Requirements
- Customer orders
- Forecasted demand
- Interplant transfers
- Safety stock replenishment

### Scheduled Receipts
- Open purchase orders
- Open production orders
- In-transit inventory

### Projected On-Hand
- Available inventory
- After allocations and reservations

### Net Requirements
- Net Requirements = Gross Requirements - Scheduled Receipts - Projected On-Hand
- If positive, generate planned order

## Exception Messages

### Action Notices
- **Expedite:** Scheduled receipt needed sooner
- **De-expedite:** Scheduled receipt can be delayed
- **Cancel:** Scheduled receipt no longer needed
- **Release:** Planned order ready to release
- **Reschedule:** Change due date of order

### Planning Alerts
- Past due orders
- Late supplier deliveries
- Forecast vs. actual variance
- Excess inventory
- Slow-moving items
- Obsolescence risk

## MRP Run Frequency
- Daily incremental MRP (changes only)
- Weekly full regenerative MRP
- Exception-based expedite runs
- After significant demand or supply changes
