# Interface Matrix - ATA-50 Cargo & Load Systems

## Purpose

This document defines all interfaces between ATA-50 subsystems and external aircraft systems for cargo operations.

## Interface Overview Matrix

| ATA-50 Subsystem | External System | Interface Type | Criticality | ICD Reference |
|------------------|-----------------|----------------|-------------|---------------|
| Main Deck | ATA-51 (Structure) | Floor attachment | Critical | ICD-50-10-51 |
| Main Deck | ATA-24 (Electrical) | PDU power | Critical | ICD-50-10-24 |
| Lower Deck | ATA-51 (Structure) | Floor attachment | Critical | ICD-50-20-51 |
| Lower Deck | ATA-24 (Electrical) | PDU power | Critical | ICD-50-20-24 |
| ULD Locks | ATA-51 (Structure) | Mounting points | Critical | ICD-50-30-51 |
| PDUs | ATA-24 (Electrical) | Motor power | Critical | ICD-50-40-24 |
| Load Sensing | ATA-31 (Indicating) | Weight data | Critical | ICD-50-50-31 |
| Load Sensing | ATA-44 (CMS) | Monitoring display | Normal | ICD-50-50-44 |
| Control Electronics | ATA-24 (Electrical) | Control power | Critical | ICD-50-60-24 |
| Control Electronics | ATA-44 (CMS) | HMI interface | Normal | ICD-50-60-44 |
| All Compartments | ATA-26 (Fire) | Fire detection | Critical | ICD-50-26 |

## Interface Details

### ATA-24: Electrical Power

**PDU Motor Power:**
- **Voltage**: 115V AC, 400Hz (3-phase)
- **Power**: 5 kW per PDU motor
- **Start Current**: Up to 30A inrush
- **Protection**: Motor circuit breaker

**Control Power:**
- **Voltage**: 28V DC
- **Power**: 100W per control unit
- **Protection**: Circuit breaker per unit

**Load Cell Power:**
- **Voltage**: 28V DC
- **Power**: 5W per load cell
- **Accuracy**: Regulated supply for precise measurement

**Reference:**
- [ATA-24 Configuration](../../../../CONFIGURATION_BASE/ATA-24_ELECTRICAL_POWER/)

---

### ATA-26: Fire Protection

**Fire Detection Coverage:**
- Smoke detectors in each cargo compartment
- Temperature sensors
- Alert to flight deck and cabin crew

**Compartment Classification:**
- Class C or better for lower deck
- Fire suppression requirements
- Ventilation control coordination

**Detection Zones:**
- Forward cargo compartment: 4 detectors minimum
- Aft cargo compartment: 4 detectors minimum
- Bulk cargo: 2 detectors minimum

**Reference:**
- [ATA-26 Configuration](../../../../CONFIGURATION_BASE/ATA-26_FIRE_PROTECTION/)

---

### ATA-31: Indicating & Recording (Weight & Balance)

**Load Data Interface:**
- Real-time weight from load cells
- ULD position confirmation
- Cargo compartment total weight
- Center of gravity calculation

**Data Format:**
- Weight in kg (±1% accuracy)
- Position coordinates (x, y, z)
- Update rate: 1 Hz
- Data bus: ARINC 429 or AFDX

**Critical Functions:**
- Overload warning
- CG out-of-limits warning
- Load distribution advisory

**Reference:**
- [ATA-31 Configuration](../../../../CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/)

---

### ATA-44: Cabin Management System

**Monitoring Interface:**
- Cargo compartment status display
- Load distribution visualization
- ULD lock status indication
- Anomaly alerts

**HMI Functions:**
- Load planning tool
- Real-time load monitoring
- Historical data review
- System diagnostics

**Data Exchange:**
- Non-critical data path
- Informational only
- Does not affect cargo safety functions

**Reference:**
- [ATA-44 Cabin Systems](../ATA-44_CABIN_SYSTEMS/)

---

### ATA-51/52: Airframe Structure

**Floor Structure Interface:**
- **ULD Lock Mounting**: Floor track system
- **Load Transfer**: Through floor beams to frames
- **Load Paths**: Primary structure integration
- **Reinforcement**: High-stress areas

**Load Requirements:**
- **Forward Load**: 9g (emergency landing)
- **Lateral Load**: 3g
- **Vertical Load**: 6g
- **Combined Loading**: Per certification requirements

**Floor Track Specifications:**
- Track pitch: 1-inch or 60.96mm
- Track profile: Industry standard
- Material: Aluminum alloy or titanium
- Attachment: Bolted to floor structure

**Reference:**
- [Airframe Integration](../../AIRFRAMES/)

---

### ATA-92: EWIS

**Wiring Requirements:**
- PDU motor power cables
- Control signal wiring
- Load cell signal cables
- Sensor wiring

**Routing:**
- Floor routing channels
- Sidewall routing
- Protection from cargo damage
- EMI shielding

**Note:** Physical wiring documented in ATA-92.

**Reference:**
- [ATA-92 EWIS](../../../../CONFIGURATION_BASE/ATA-92_EWIS/)

---

## ULD Specifications

### Supported ULD Types
- **LD3**: Lower deck container
- **LD6**: Lower deck container
- **LD8**: Lower deck container
- **LD11**: Lower deck container
- **Pallets**: Main deck (if applicable)

### ULD Requirements
- IATA specifications compliance
- Maximum weight per ULD type
- Lock compatibility
- Dimensions and tolerances

## Safety Requirements

### Load Restraint
- ULD locks: Minimum 3 per ULD
- Locking force: 6,000 lbs minimum per lock
- Lock indication: Visual and electronic
- Emergency release: Manual override

### Fire Safety
- Detection: Full compartment coverage
- Response time: <30 seconds
- Suppression: Per compartment classification
- Ventilation: Smoke evacuation capability

### Structural Safety
- Load limits: Clearly marked
- Overload prevention: Electronic and mechanical
- Emergency egress: Accessible from outside
- Hazmat compatibility: Per regulations

## Operational Interfaces

### Ground Handling
- Loading equipment compatibility
- Ground power interface
- Communication with ground crew
- Safety interlocks during loading

### Flight Operations
- Pre-flight load verification
- In-flight monitoring
- Post-flight unloading
- Maintenance access

## Interface Change Control

Follow process in:
- [Change Rules](../../../01-GOVERNANCE/CHANGE_RULES.md)
- [Interface Management](../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)

## Interface Verification

1. Load path analysis and testing
2. ULD lock functional testing
3. Fire detection system testing
4. Load cell calibration
5. Integration testing
6. Flight testing

## References

- [Domain Dependencies](../../../02-ARCHITECTURE/DEPENDENCIES.md)
- [Safety Boundaries](../../../01-GOVERNANCE/SAFETY_BOUNDARIES.md)
- [ICD Index](../../../05-LINKS/ICD_INDEX.md)

---

**Last Updated**: 2025-01-15
