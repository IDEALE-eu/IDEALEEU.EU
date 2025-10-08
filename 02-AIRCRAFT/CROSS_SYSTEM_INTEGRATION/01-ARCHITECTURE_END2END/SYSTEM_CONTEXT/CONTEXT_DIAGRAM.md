# System Context Diagram

## Overview

This document defines the aircraft system context, external interfaces, and operational modes using Mermaid and SysML-style diagrams.

## System Context

### Aircraft System Boundary

```mermaid
graph TB
    subgraph External Environment
        PILOT[Pilot]
        ATC[Air Traffic Control]
        GROUND[Ground Support Equipment]
        AIRPORT[Airport Infrastructure]
        GPS[GNSS Satellites]
        WEATHER[Weather Systems]
    end
    
    subgraph Aircraft System
        AVIONICS[Avionics Suite]
        FCS[Flight Control System]
        PROPULSION[Propulsion System]
        POWER[Power Generation & Distribution]
        COMMS[Communications]
        NAV[Navigation]
    end
    
    PILOT -->|Control Inputs| AVIONICS
    AVIONICS -->|Display/Alerts| PILOT
    ATC -->|Voice/Data Link| COMMS
    COMMS -->|Voice/Data Link| ATC
    GROUND -->|Maintenance Data| AVIONICS
    AVIONICS -->|Health Data| GROUND
    AIRPORT -->|ILS/VOR Signals| NAV
    GPS -->|Position/Time| NAV
    WEATHER -->|Conditions| AVIONICS
    
    AVIONICS -->|Commands| FCS
    FCS -->|Status| AVIONICS
    AVIONICS -->|Commands| PROPULSION
    PROPULSION -->|Status| AVIONICS
    POWER -->|Electrical Power| AVIONICS
    POWER -->|Electrical Power| FCS
    POWER -->|Electrical Power| COMMS
```

## External Interfaces

### Human Interfaces
- **Pilot** - Flight crew inputs and displays
- **Cabin Crew** - Passenger management and safety
- **Maintenance Personnel** - Ground maintenance and diagnostics

### Environmental Interfaces
- **GNSS** - GPS, Galileo, GLONASS positioning and time
- **Weather Systems** - Temperature, pressure, wind data
- **Electromagnetic Environment** - DO-160 compliance

### Infrastructure Interfaces
- **Air Traffic Control** - Voice and data link communications
- **Ground Support Equipment** - Maintenance, fueling, power
- **Airport Systems** - ILS, VOR, DME navigation aids

## Operational Modes

### Flight Modes

```mermaid
stateDiagram-v2
    [*] --> PowerOff
    PowerOff --> GroundOps: Power On
    GroundOps --> PreFlight: Crew Boarding
    PreFlight --> Taxi: Clearance
    Taxi --> Takeoff: Runway
    Takeoff --> Climb: Airborne
    Climb --> Cruise: Target Altitude
    Cruise --> Descent: Approach
    Descent --> Approach: Landing Clearance
    Approach --> Landing: Final Approach
    Landing --> Taxi: Touchdown
    Taxi --> GroundOps: Gate
    GroundOps --> PowerOff: Shutdown
    
    state GroundOps {
        [*] --> Maintenance
        Maintenance --> Preflight
        Preflight --> Ready
    }
    
    state Cruise {
        [*] --> Normal
        Normal --> Emergency: Failure
        Emergency --> Normal: Recovery
    }
```

### System Operating Modes
- **Normal** - All systems nominal
- **Degraded** - One or more system failures, reconfiguration active
- **Emergency** - Critical failure, emergency procedures active
- **Maintenance** - Ground mode, diagnostics and servicing
- **Safe Mode** - Minimal functionality, fail-safe state

## Functional Allocation

### Primary Functions
- **Navigation** - Position determination and guidance
- **Flight Control** - Attitude and trajectory control
- **Propulsion Management** - Thrust and fuel control
- **Power Management** - Electrical power generation and distribution
- **Communications** - Voice and data communications
- **Monitoring** - System health and flight parameters

### Cross-System Functions
- **Time Synchronization** - System-wide time reference (03-TIME_SYNCHRONISATION/)
- **Data Distribution** - Network backbone (02-NETWORKS_DATA_BUS/)
- **Health Monitoring** - System-wide FDIR (06-SOFTWARE_INTEGRATION/SAFETY_MONITORS.md)
- **Configuration Management** - Software and hardware baselines (09-CONFIG_BASELINES_HANDOFF/)

## Traceability

This context diagram satisfies:
- **System Requirements** - See [00-PROGRAM/DIGITAL_THREAD/04-MBSE/REQUIREMENTS_ALLOCATION.csv](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/REQUIREMENTS_ALLOCATION.csv)
- **Architecture Views** - See [00-PROGRAM/DIGITAL_THREAD/04-MBSE/SYSML_MODELS/](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/)
- **Interface Definitions** - See [10-ICD_LINKS/INDEX.md](../../10-ICD_LINKS/INDEX.md)

## References
- **ARP4754A** - Section 3, System Context
- **02-AIRCRAFT/00-README.md** - Aircraft domain overview
- **[ASSUMPTIONS_CONSTRAINTS.md](./ASSUMPTIONS_CONSTRAINTS.md)** - Design assumptions and constraints

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | Systems Architecture Team | Initial context diagram |
