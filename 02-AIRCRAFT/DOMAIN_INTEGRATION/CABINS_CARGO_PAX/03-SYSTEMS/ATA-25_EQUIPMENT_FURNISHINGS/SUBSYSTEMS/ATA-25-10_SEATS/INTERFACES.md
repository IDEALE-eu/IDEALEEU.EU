# Interfaces - ATA-25-10 Seats

## Structural Interfaces (ATA-51)

### Seat Track Attachment
- **Type**: Mechanical, load-bearing
- **Interface**: Seat legs to floor-mounted seat tracks
- **Standard**: MS 25083 or equivalent
- **Load Requirements**:
  - 16g forward
  - 9g lateral
  - 10g vertical
  - Combined loading per FAR 25.561/562

### Floor Interface
- **Load Distribution**: Through seat tracks to floor structure
- **Footprint**: Per seat configuration
- **Protection**: Floor panels must support seat attachment without damage

## Electrical Interfaces (ATA-24)

### Seat Power
- **28V DC**: Seat mechanism motors, controls
- **Power**: 50W maximum per seat
- **Protection**: Circuit breaker per row

### USB Charging Ports
- **Voltage**: 5V DC
- **Current**: 2.4A per port (USB Type-A)
- **Current**: 3A per port (USB Type-C)
- **Protection**: Electronic overcurrent protection per port
- **Ports**: 2 per seat (economy), 4 per seat (premium)

### AC Power Outlets (Premium Classes)
- **Voltage**: 110V AC, 60Hz
- **Power**: 75W continuous per outlet
- **Standard**: NEMA 1-15 receptacle
- **Protection**: GFCI per outlet

## IFE Interface (ATA-44-20)

### Screen Mounting
- **Type**: Mechanical mount on seat back
- **Load**: 5 lbs screen weight + dynamic loading
- **Adjustment**: Tilt mechanism (±15°)
- **Cable Routing**: Through seat back structure

### Screen Power
- **Supply**: From IFE power distribution
- **Routing**: Through seat structure
- **Connector**: Supplier-specific quick disconnect

### Control Integration
- **Interface**: Touchscreen or handset
- **Mounting**: Armrest or seat back
- **Cabling**: Integrated with seat wiring

## Other Interfaces

### Cabin Furnishings
- **Tray Table**: Stowage in seat back
- **Magazine Pocket**: Seat back literature holder
- **Armrest**: Shared with adjacent seat or aisle

### Safety Equipment
- **Life Vest**: Under-seat storage provision
- **Seatbelt**: Integrated attachment points

## Interface Control

All interfaces managed through:
- ICD-25-10-51 (Structural)
- ICD-25-10-24 (Electrical)
- ICD-25-10-44 (IFE)

Located in: `/00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`

---

**Last Updated**: 2025-01-15
