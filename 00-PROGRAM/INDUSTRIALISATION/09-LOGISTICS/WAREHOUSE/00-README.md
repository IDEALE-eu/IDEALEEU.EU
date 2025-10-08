# WAREHOUSE

Warehouse operations and inventory management.

## Overview

Warehouse stores raw materials, purchased components, WIP, and finished goods, managing inventory levels and accuracy.

## Warehouse Functions

- **Receiving:** Accept deliveries, verify quantity/quality
- **Put-away:** Store in designated locations
- **Storage:** Protect and preserve materials
- **Picking:** Retrieve for kitting or production
- **Packing:** Prepare finished goods for shipment
- **Shipping:** Load and dispatch to customers

## Warehouse Layout

- **Receiving area:** Incoming inspection and staging
- **Raw material storage:** By material type
- **Component storage:** By part number, velocity-based (ABC)
- **WIP storage:** Sub-assemblies in process
- **Finished goods:** Ready for shipment
- **Quarantine area:** Hold non-conforming material
- **Shipping area:** Packing and loading

## Inventory Management

### ABC Classification
- **A items:** High value, tight control, frequent counts
- **B items:** Moderate value and control
- **C items:** Low value, simple control

### Inventory Accuracy
- **Cycle counting:** Daily counts of selected items
- **Annual physical inventory:** Full count once per year
- **Target accuracy:** ≥ 99.5%

### FIFO Enforcement
- First-in, first-out to prevent obsolescence
- Especially critical for shelf-life materials (prepregs, adhesives)
- Date-coded storage and picking

## Warehouse Management System (WMS)

- Inventory tracking (quantity, location, lot/serial)
- Receiving and put-away transactions
- Picking and shipping transactions
- Cycle count management
- FIFO enforcement
- Integration with ERP

## Material Storage Requirements

### Environmental Control
- Temperature and humidity for sensitive materials
- Freezer storage for prepregs (0°F or colder)
- ESD protection for electronic components
- Flammable storage cabinets for hazardous materials

### Material Shelf Life
- Track expiration dates
- Alert for approaching expiration
- Reject expired materials
- FIFO picking to rotate stock

## Traceability

- Lot and serial number tracking
- Receiving documentation retained
- Material certifications linked to inventory
- Usage tracking (lot consumed on which assembly)

## Links

- To **TRACEABILITY_RFID/** for tracking systems
- To **MATERIAL_FLOW/** for material handling
- To **16-IT_INTEGRATION/ERP/** for WMS integration
