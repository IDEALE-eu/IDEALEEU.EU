# Cross-Load Scenarios and Load-Shedding

## Overview

This document defines power cross-load scenarios, load-shedding sequences, and priority assignments for managing electrical system contingencies.

## Normal Operations

### Power Sources
- **Main Generator 1**: 30 kVA @ 115VAC 400Hz 3-phase
- **Main Generator 2**: 30 kVA @ 115VAC 400Hz 3-phase
- **APU Generator**: 20 kVA @ 115VAC 400Hz 3-phase
- **Battery**: 28 VDC, 40 Ah (emergency backup)
- **Ram Air Turbine (RAT)**: 15 kVA @ 115VAC 400Hz (emergency)

### Load Distribution
- **Total Aircraft Load**: ~2.5 kW DC + ~5 kW AC (nominal cruise)
- **Generator 1 Load**: ~12 kVA (40% capacity)
- **Generator 2 Load**: ~12 kVA (40% capacity)
- **Margin**: 20% per generator in normal ops

## Contingency Scenarios

### Scenario 1: Single Generator Failure
**Event**: Generator 1 fails, Generator 2 + APU available
**Action**:
1. Automatic bus tie closes, consolidates load on Generator 2
2. APU auto-start if on ground, crew-initiated if in flight
3. Non-essential loads shed if total load >80% Generator 2 capacity
4. Crew alerted via EICAS caution message

**Load Priority**:
- **Priority 1 (Critical - DAL A)**: Flight control, engine control, fire detection (never shed)
- **Priority 2 (Essential - DAL B)**: Navigation, displays, pressurization
- **Priority 3 (Non-Essential - DAL C/D)**: Galley, IFE, comfort systems

**Shed Sequence** (if required):
1. Shed galley loads (-3 kW)
2. Shed IFE systems (-2 kW)
3. Shed cabin lighting (50% reduction, -1 kW)
4. Shed one hydraulic pump (-2 kW)

### Scenario 2: Dual Generator Failure
**Event**: Both main generators fail, APU available
**Action**:
1. APU generator auto-connect to essential bus
2. Immediate load-shed of all non-essential and some essential loads
3. Battery backup for critical flight control if APU fails to start
4. RAT deployment if altitude and speed permit (emergency)
5. Crew alerted via EICAS warning message

**Load Priority**:
- **Priority 1 (Critical - DAL A)**: Flight control, engine FADEC, fire detection (~800 W)
- **Priority 2 (Essential)**: One display, one radio, essential instruments (~500 W)
- **Priority 3**: Shed everything else

**Shed Sequence**:
1. Immediate: Shed all Priority 3 loads (-8 kW)
2. Immediate: Shed hydraulic pumps (rely on engine-driven pumps)
3. Immediate: Shed 50% cabin systems
4. Maintain: Flight control, engine control, minimal avionics for safe landing

### Scenario 3: Total Electrical Failure (Emergency)
**Event**: All generators fail, APU fails, battery only
**Action**:
1. Battery powers critical flight control and engine FADECs
2. RAT deploys automatically if airspeed >140 kts
3. Battery runtime: 30 minutes at critical loads only
4. Emergency landing required, minimal instruments available

**Battery-Powered Systems**:
- FCC-1 and FCC-2 (flight control)
- FADEC-1 and FADEC-2 (engine control)
- One standby display (battery-powered)
- Standby radio (emergency comms)

**Duration**: 30 minutes to complete emergency landing

### Scenario 4: Brownout Condition
**Event**: Voltage sag to 20 VDC (from nominal 28 VDC) for >50ms
**Action**:
1. Critical LRUs (Priority 1) must continue operation per DO-160G
2. Non-critical LRUs may reset/reboot
3. Load-shed non-essential loads to reduce demand
4. Log event for maintenance investigation

**Tolerance Requirements**:
- **Priority 1 (DAL A)**: Must operate at 18 VDC for 50ms (per spec)
- **Priority 2 (DAL B)**: Should operate at 20 VDC for 100ms
- **Priority 3 (DAL C/D)**: May reset/reboot

## Load-Shedding Priorities

### Priority 1: Never Shed (Critical - DAL A)
- Flight Control Computers (FCC-1, FCC-2)
- Actuator Control Electronics (ACE-1, ACE-2)
- Engine FADEC and ECUs (FADEC-1, FADEC-2, ENG-ECU-1, ENG-ECU-2)
- Fire Detection and Suppression (FIRE-DET-1, FIRE-SUPP-1)
- Brake Control (BRAKE-CTRL-1)
- Air Data Computers (ADC-1, ADC-2)

### Priority 2: Shed in Dual Generator Failure (Essential - DAL B)
- Navigation Systems (GPS-1, GPS-2, IRS-1, IRS-2, FMS-1)
- Displays (DISPLAY-1 retained, DISPLAY-2 shed)
- Pressurization Control (PRESS-CTRL-1)
- Landing Gear Control (LG-CTRL-1)
- Oxygen Control (OXY-CTRL-1)

### Priority 3: Shed in Single Generator Failure (Non-Essential - DAL C/D)
- Weather Radar (WX-RADAR-1)
- Communications Radio 2 (retain COMMS-1 only)
- Fuel Management displays (retain control, shed displays)
- Cabin lighting (50% reduction acceptable)
- IFE systems
- Galley loads

### Priority 4: Immediate Shed (Comfort/Convenience)
- In-Flight Entertainment
- Galley equipment
- Cabin WiFi
- Passenger USB ports
- Mood lighting

## Load-Shedding Logic

### Automatic Load-Shedding
- Managed by Electrical Load Management System (ELMS)
- Monitors generator output, bus voltage, current
- Sheds loads automatically per priority when:
  - Total load exceeds 80% of available capacity
  - Bus voltage drops below 24 VDC for >5 seconds
  - Generator overload condition detected

### Manual Load-Shedding
- Crew can manually shed loads via overhead panel switches
- Procedures in Aircraft Flight Manual (AFM)
- Typically used for:
  - Pre-emptive load reduction before landing single-generator
  - Managing electrical smoke/fire situations
  - Reducing load for APU-only operations

## Recovery and Restoration

### Load Restoration Sequence
After contingency resolved (e.g., generator restarted):
1. Verify sufficient capacity available
2. Restore Priority 2 loads first (essential systems)
3. Wait 30 seconds for stabilization
4. Restore Priority 3 loads (non-essential)
5. Wait 30 seconds for stabilization
6. Restore Priority 4 loads (comfort systems)
7. Crew manually enables galley and IFE when ready

### Inrush Current Management
- Load restoration sequenced to avoid simultaneous inrush
- Maximum 30-second intervals between load additions
- Each load inrush <3x steady-state, <100ms duration

## Testing and Verification

### Ground Tests
- Simulate single generator failure, verify load-shed sequences
- Simulate dual generator failure, verify battery backup
- Measure inrush currents during load restoration
- Document all tests in [07-INTEGRATION_TEST/EVIDENCE/](../../07-INTEGRATION_TEST/EVIDENCE/)

### Flight Tests
- Intentional generator disconnect (single, then dual)
- Verify crew procedures and EICAS messaging
- Measure battery runtime under critical loads only
- Test RAT deployment and power generation

## Compliance

- **DO-160G Section 16**: Voltage spike and dropout tolerance
- **CS-25.1351**: Electrical system design requirements
- **CS-25.1309**: Safety assessment (failure scenarios)

## References

- **[POWER_BUDGET.csv](./POWER_BUDGET.csv)** - System power requirements
- **[THERMAL_BUDGET.csv](./THERMAL_BUDGET.csv)** - Thermal dissipation
- **[EMC_COUPLING_ASSESSMENT.md](./EMC_COUPLING_ASSESSMENT.md)** - EMC considerations

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | Electrical Systems Team | Initial cross-load scenarios |
