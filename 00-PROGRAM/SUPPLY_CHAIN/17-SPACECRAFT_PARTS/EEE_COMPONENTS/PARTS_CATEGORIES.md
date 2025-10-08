# EEE Parts Categories

## Passive Components

### Resistors
- Film resistors (preferred for space)
- Wirewound resistors
- Derating: 50-70% of rated power
- Stability over temperature and radiation

### Capacitors
- Ceramic capacitors (Class II for space)
- Tantalum capacitors (wet slug, solid, polymer)
- Film capacitors
- Aluminum electrolytic (limited use)
- Voltage derating: 50-60%
- Tantalum risk: infant mortality, voltage transients

### Inductors and Transformers
- Wirewound inductors
- Magnetic materials (ferrite, powdered iron)
- Transformers for power conversion
- Current derating for temperature rise

## Semiconductors

### Diodes
- Silicon diodes (signal, switching, power)
- Schottky diodes
- Zener diodes
- Radiation effects: TID degradation, SEE concerns
- Derating: current, voltage, junction temperature

### Transistors
- Bipolar Junction Transistors (BJT)
- MOSFETs (careful selection for radiation)
- JFETs
- Power transistors
- Radiation effects: gain degradation (BJT), threshold shift (MOSFET), SEE

### Integrated Circuits
- Digital logic (CMOS, TTL)
- Microprocessors and microcontrollers
- Memory (SRAM, EEPROM, Flash)
- Analog ICs (op-amps, comparators, voltage references)
- Power management ICs
- Radiation-hardened vs. radiation-tolerant
- SEE susceptibility (SEU, SEL, SEFI)

### Power Devices
- Power MOSFETs
- IGBTs
- Power diodes and rectifiers
- Switching regulators
- High current and voltage handling

## Optoelectronics

### LEDs
- Indicator LEDs
- Display LEDs
- Infrared LEDs
- Radiation effects: output degradation

### Photodetectors
- Photodiodes
- Phototransistors
- Optical sensors
- Radiation darkening concerns

### Optocouplers
- Signal isolation
- Galvanic isolation
- Radiation effects: CTR (Current Transfer Ratio) degradation

## Connectors and Relays

### Connectors
- Micro-D connectors
- Space-qualified connectors (AS39029, etc.)
- Pins, sockets, backshells
- Sealing and contamination control
- Mating cycles and reliability

### Relays
- Latching relays (preferred for space - no continuous power)
- Non-latching relays
- Reed relays
- Solid-state relays (SSR)
- Contact ratings and life cycles
- Hermetic sealing

## Oscillators and Timing

### Crystal Oscillators
- Quartz crystals
- Temperature compensated (TCXO)
- Oven controlled (OCXO)
- Frequency stability over temperature and radiation

### Timing Circuits
- Real-time clocks (RTC)
- Timing generators
- Frequency synthesizers

## Sensors

### Temperature Sensors
- Thermistors
- RTDs (Resistance Temperature Detectors)
- IC temperature sensors

### Pressure Sensors
- Piezoresistive sensors
- Capacitive sensors
- Space-qualified pressure transducers

### Other Sensors
- Accelerometers
- Gyroscopes
- Magnetometers
- Sun sensors
- Star trackers

## Part Selection Criteria

### Heritage
- Flight-proven parts (preferred)
- Similar mission experience
- Known radiation performance
- Reliability database

### Availability
- Lead times (often 52+ weeks for space parts)
- Multiple sources (if possible)
- Obsolescence risk
- Lifetime buy considerations

### Cost
- Space-grade parts are expensive
- Balance cost vs. risk
- Budget allocation
- Long lead time carrying costs

### Performance
- Electrical specifications
- Temperature range
- Radiation tolerance
- Reliability predictions

## Approved Manufacturer Lists (AML)

Maintain AML for each part number:
- Qualified manufacturers
- Manufacturer part numbers
- Qualification status (space, military, industrial)
- Radiation test data
- Availability and lead time
- Preferred and acceptable sources

See: **13-DATA_MODELS/INSTANCES/AML_APPROVED_MFR_LIST.csv**
