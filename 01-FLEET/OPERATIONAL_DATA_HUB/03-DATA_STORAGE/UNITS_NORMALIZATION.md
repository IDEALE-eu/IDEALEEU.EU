# UNITS_NORMALIZATION

Standard units for telemetry signals and documented exceptions.

## Purpose

Ensures consistency in unit representation across all telemetry sources to:
- Prevent unit conversion errors
- Simplify data analysis and ML model training
- Enable cross-platform comparisons
- Reduce ambiguity in data contracts

## Standard: SI Units

**Default**: All signals use SI (Système International) units unless documented exception.

### SI Base Units

| Quantity | SI Unit | Symbol |
|----------|---------|--------|
| Length | meter | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric Current | ampere | A |
| Temperature | kelvin | K |
| Amount of Substance | mole | mol |
| Luminous Intensity | candela | cd |

### Common Derived SI Units

| Quantity | SI Unit | Symbol | Derivation |
|----------|---------|--------|------------|
| Force | newton | N | kg⋅m/s² |
| Pressure | pascal | Pa | N/m² = kg/(m⋅s²) |
| Energy | joule | J | N⋅m = kg⋅m²/s² |
| Power | watt | W | J/s = kg⋅m²/s³ |
| Frequency | hertz | Hz | s⁻¹ |
| Velocity | meter per second | m/s | - |
| Acceleration | meter per second squared | m/s² | - |
| Electric Potential | volt | V | W/A = kg⋅m²/(s³⋅A) |
| Electric Resistance | ohm | Ω | V/A = kg⋅m²/(s³⋅A²) |

## Documented Exceptions

### Aviation Industry Standards

For legacy compatibility and pilot familiarity:

| Quantity | Standard Unit | Symbol | SI Equivalent | Justification |
|----------|---------------|--------|---------------|---------------|
| Altitude | feet | ft | 1 ft = 0.3048 m | FAA/EASA standard, pilot displays |
| Airspeed | knots | kt | 1 kt = 0.514444 m/s | Aviation industry standard |
| Vertical Speed | feet per minute | ft/min | 1 ft/min = 0.00508 m/s | Pilot displays, ATC communication |
| Distance (Navigation) | nautical miles | NM | 1 NM = 1852 m | Aviation/maritime standard |
| Pressure (Altitude) | inches of mercury | inHg | 1 inHg = 3386.39 Pa | Barometric pressure (US) |
| Fuel Flow | pounds per hour | lb/h | 1 lb/h = 0.000126 kg/s | US aviation standard |

**Note**: Dual reporting required for safety-critical parameters (SI + exception unit).

### Hydrogen Propulsion System

| Quantity | Standard Unit | Symbol | SI Equivalent | Justification |
|----------|---------------|--------|---------------|---------------|
| Pressure (H2 Tank) | bar | bar | 1 bar = 100,000 Pa | Industry standard for compressed gas |
| Flow Rate (H2) | standard liters per minute | SLPM | Varies with P, T | Industry standard for gas flow |

**Note**: SLPM normalized to 0°C, 1 atm (STP conditions).

### Spacecraft Systems

| Quantity | Standard Unit | Symbol | SI Equivalent | Justification |
|----------|---------------|--------|---------------|---------------|
| Temperature (Space) | Celsius | °C | K = °C + 273.15 | Engineering convention |
| Radiation Dose | gray | Gy | 1 Gy = 1 J/kg | SI unit for absorbed dose |
| Angular Velocity | degrees per second | °/s | 1 °/s = 0.0174533 rad/s | Attitude control convention |

## Unit Conversion Functions

### Provided Conversions

All unit conversions provided as standard functions:

```python
# Example conversion library
from ideale.units import convert

# Convert feet to meters
altitude_m = convert(altitude_ft, from_unit="ft", to_unit="m")

# Convert knots to m/s
airspeed_ms = convert(airspeed_kt, from_unit="kt", to_unit="m/s")

# Convert bar to Pa
pressure_pa = convert(pressure_bar, from_unit="bar", to_unit="Pa")
```

### Metadata-Driven Conversion

Units stored in schema metadata:

```json
{
  "signal": "altitude_msl",
  "unit": "ft",
  "si_unit": "m",
  "conversion_factor": 0.3048,
  "conversion_formula": "m = ft * 0.3048"
}
```

## Unit Validation

### At Ingestion
- Schema specifies expected unit
- Validation rule checks unit field matches schema
- Conversion to SI for storage (optional, configurable)

### In Data Contracts
```yaml
signal: h2_tank_pressure_fwd
unit: bar
si_unit: Pa
range: [0, 350]  # bar
si_range: [0, 35000000]  # Pa
```

## Unit Handling in ML Models

### Training Data
- **Option 1**: Normalize all inputs to SI units
- **Option 2**: Keep exception units but document in data contract

### Inference
- Model input schema specifies expected units
- Automatic conversion if needed

### Example
```yaml
# Model input contract
inputs:
  - name: altitude
    unit: m  # Model expects SI units
    range: [0, 15240]  # 0-50,000 ft in meters
```

## Best Practices

### 1. Always Specify Units
```yaml
# Good
signal: pressure
value: 285.3
unit: bar

# Bad (ambiguous)
signal: pressure
value: 285.3
```

### 2. Document Exceptions
- All non-SI units must be documented in schema
- Include conversion formula to SI

### 3. Dual Reporting for Safety-Critical
```json
{
  "altitude_ft": 35000,
  "altitude_m": 10668,
  "unit_primary": "ft",
  "unit_si": "m"
}
```

### 4. Avoid Unit Mixing
- Don't mix units within same signal over time
- Breaking change if unit changes (requires new schema version)

### 5. Use Conversion Library
- Centralized conversion functions
- Unit-tested and validated
- Version-controlled

## Common Mistakes to Avoid

### Mistake 1: Ambiguous Unit Labels
```yaml
# Bad
signal: speed
unit: mph  # Miles per hour? Meters per hour?

# Good
signal: ground_speed
unit: m/s
unit_exception: kt
conversion_factor: 0.514444
```

### Mistake 2: Implicit Unit Assumptions
```python
# Bad
altitude = read_sensor()  # What unit???

# Good
altitude_ft = read_sensor(unit="ft")
altitude_m = convert(altitude_ft, from_unit="ft", to_unit="m")
```

### Mistake 3: Lossy Conversions
```python
# Bad (precision loss)
pressure_pa = int(pressure_bar * 100000)

# Good (preserve precision)
pressure_pa = pressure_bar * 100000.0
```

## Unit Abbreviations

### Approved Abbreviations

| Unit | Abbreviation | Notes |
|------|--------------|-------|
| meter | m | SI base |
| kilometer | km | Not K or KM |
| kilogram | kg | Not K or KG |
| second | s | Not sec |
| minute | min | Not m |
| hour | h | Not hr |
| degree Celsius | °C | Not C or deg |
| kelvin | K | Not k or deg K |
| bar | bar | Not B |
| pascal | Pa | Not pa |
| knots | kt | Not kts or kn |
| feet | ft | Not f or ' |
| pounds per hour | lb/h | Not lbs/hr |

## Related Documents

- **METADATA_REGISTRY/DATA_DICTIONARY.csv** - Signal catalog with units
- **../02-DATA_INGESTION/SCHEMA_REGISTRY/** - Schema definitions
- **../01-FLEET/FEDERATED_LEARNING/01-ARCHITECTURE/DATA_CONTRACTS/** - ML data contracts

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial unit normalization spec | Data Engineering Team |
