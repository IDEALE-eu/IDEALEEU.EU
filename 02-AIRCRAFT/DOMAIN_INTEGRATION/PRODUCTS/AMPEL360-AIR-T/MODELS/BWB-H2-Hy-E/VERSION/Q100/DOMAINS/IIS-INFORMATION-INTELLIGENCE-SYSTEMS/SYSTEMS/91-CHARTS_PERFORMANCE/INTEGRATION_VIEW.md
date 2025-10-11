# 91-CHARTS_PERFORMANCE — Integration View

## Functional Role

The Charts & Performance system serves as the authoritative source for aircraft performance data, operational charts, and flight planning information. It integrates performance calculations with real-time operational data to support safe and efficient flight operations.

## System Boundaries

**In Scope:**
- Aircraft performance calculations and models
- Flight planning charts and data
- Performance data export to operational systems
- Regulatory compliance reporting
- Performance monitoring and analysis

**Out of Scope:**
- Real-time flight control (ATA 22)
- Navigation computation (ATA 34)
- Flight management execution (ATA 22)
- Weather sensing (ATA 31)

## Key Dependencies

### Data Sources
- **71/72** — Powerplant/Engine: Thrust, fuel flow, operating limits
- **31** — Instruments: Environmental conditions, altitude, speed
- **34** — Navigation: Position, track, groundspeed
- **24** — Electrical Power: System availability and power consumption
- **25** — Equipment/Furnishings: Weight and balance data

### Data Consumers
- **46** — Information Systems: Data storage, distribution, and archival
- **42** — Integrated Modular Avionics: Performance data integration
- **93** — Ground Support Equipment: Pre-flight planning tools
- **94** — Training: Simulator performance models

## Operational Modes

### Normal Mode
- Continuous performance monitoring
- Real-time chart generation
- Data export to flight planning systems
- Performance trend analysis

### Dispatch Mode
- Pre-flight performance calculations
- Weight and balance verification
- Takeoff/landing performance computation
- Fuel planning and optimization

### Maintenance Mode
- Performance degradation analysis
- System health monitoring
- Compliance verification
- Audit report generation

### Training Mode
- Simulator performance data feed
- Training scenario generation
- Performance example cases

## Interface Strategy

### Data Bus Integration
- Primary: ARINC 664 (AFDX) for high-bandwidth data distribution
- Secondary: ARINC 429 for discrete performance parameters
- Ground: Ethernet TCP/IP for ground-based planning tools

### Interface Control Documents
- ICD-IIS-91-001: Performance Data Exchange Protocol
- ICD-IIS-91-002: Chart Data Format Specification
- ICD-IIS-91-003: Training Data Interface
- ICD-IIS-91-004: Ground Systems API

See `INTERFACE_MATRIX/` for detailed interface specifications.

## Verification Approach

- Model validation against flight test data
- Chart accuracy verification
- Data integrity validation
- Performance calculation benchmarking
- Regulatory compliance audits

## Related Documentation

- System README: `README.md`
- Interface Matrix: `INTERFACE_MATRIX/`
- Subsystems: `SUBSYSTEMS/*/README.md`
