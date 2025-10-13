# Q100 Configuration Rules

## Version Class: Q100

**Passenger Capacity Range:** 96-110 passengers

## Performance Envelope

### Weight Limits
- **MTOW (Maximum Takeoff Weight):** 72,000 - 76,000 kg
- **MLW (Maximum Landing Weight):** 68,000 - 72,000 kg
- **OEW (Operating Empty Weight):** 42,000 - 46,000 kg
- **Max Payload:** 12,000 - 15,000 kg

### Range and Performance
- **Design Range:** 3,200 - 3,800 nautical miles
- **Service Ceiling:** 41,000 - 43,000 ft
- **Cruise Speed:** Mach 0.78 - 0.82
- **Takeoff Distance (MTOW, ISA, SL):** ≤ 2,400 m
- **Landing Distance (MLW, ISA, SL):** ≤ 1,800 m

### Fuel System
- **H₂ Tank Capacity:** 4,500 - 5,500 kg LH₂
- **Fuel Cell Power:** 1.2 - 1.5 MW
- **Battery Backup:** 150 - 200 kWh

## Cabin Configuration

### Passenger Arrangements (Q100)
- **Single Class:** 100-106 seats @ 32" pitch
- **Dual Class:** 96-100 seats (12 Business @ 38" + Economy @ 32")
- **Aisle Width:** ≥ 20 inches
- **Seat Width:** 18-19 inches (Economy), 20-22 inches (Business)

### Exits and Safety
- **Type A Exits:** 2 (forward doors)
- **Type III Exits:** 4 (overwing emergency exits)
- **Lavatories:** 3-4
- **Galley Positions:** Forward + Aft

### Cargo
- **Forward Cargo Hold:** 8-10 m³
- **Aft Cargo Hold:** 12-15 m³
- **Bulk Cargo:** 2-3 m³

## System Configuration Rules

### ATA 24 — Electrical Power
- Primary power from fuel cells (1.2-1.5 MW)
- Battery backup minimum 150 kWh
- Redundant power distribution (dual bus)

### ATA 28 — Fuel (H₂)
- LH₂ tanks integrated in BWB structure
- Boil-off management system required
- Minimum 10% ullage for thermal expansion

### ATA 32 — Landing Gear
- Main gear: Dual-wheel bogie configuration
- Nose gear: Dual-wheel steerable
- Tire pressure: 180-200 psi (main), 160-180 psi (nose)

### ATA 34 — Navigation
- Dual AHRS/IRS
- Dual GNSS with SBAS/GBAS capability
- Required Navigation Performance (RNP) ≤ 0.3

### ATA 51-57 — Structures
- BWB configuration with blended fuselage-wing
- Composite primary structure (CFRP)
- Aluminum alloys for secondary structure
- Pressurization: 8.6 psi differential

### ATA 71 — Power Plant
- Fuel cell stacks: 1.2-1.5 MW total
- Electric motors: 2 × 600-750 kW ducted fans
- Redundant thermal management

## Modification States

### Baseline (MOD-BASE)
Standard Q100 configuration as delivered.

### Mod Level 1 (MOD-M1)
Enhanced avionics and cabin interior upgrades.

## Compliance

- **Certification Basis:** CS-25 (EASA) / FAR Part 25 (FAA)
- **Environmental:** ICAO Annex 16, Volume II (CO₂ and NOx)
- **Safety:** ARP4754A, ARP4761
- **H₂ Safety:** ISO 19880-8, SAE J2719

## Validation

All configurations must:
1. Pass schema validation (`SCHEMAS/config-set.schema.json`)
2. Be within performance envelope defined above
3. Comply with structural and systems constraints
4. Meet certification requirements

## Change Control

Changes to these rules require:
- CCB (Configuration Control Board) approval
- Impact assessment on existing configurations
- Update to affected configuration sets
- Traceability update in `03-TRACEABILITY/CONFIG_TO_REQ_MAP.md`

## References

- **S.1000D:** ATA iSpec 2200 Specification
- **CS-25:** Certification Specifications for Large Aeroplanes
- **ARP4754A:** Guidelines for Development of Civil Aircraft and Systems
