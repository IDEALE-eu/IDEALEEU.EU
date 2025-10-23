# BWB-H2-Hy-E Schema Definitions

**Version:** 1.1.0  
**Date:** 2025-10-23  
**Status:** Active  

---

## Overview

This directory contains schema definitions for the BWB-H2-Hy-E (Blended Wing Body with Hydrogen Hybrid Electric propulsion) architecture. These schemas define the data models and contracts for a **multi-energy agnostic propulsion system** including hydrogen, SAF/e-SAF fuels, solid-state batteries, and Open Fan technology.

---

## Schema Files

### 1. `hydrogen-subsystem.yaml`
**Purpose:** Hydrogen fuel system components and safety monitoring  
**TFA Domain:** CQH (Cryogenics-Quantum-H2)  
**Version:** 1.0.0

Defines schema for:
- Hydrogen storage (cryogenic liquid, compressed gas)
- Distribution systems
- Safety interlocks and emergency venting
- Leak detection zones
- Thermal management
- Maintenance procedures
- Cryogenic seal inspection protocols

**Key Components:**
- Storage tanks (pressure vessels)
- Distribution pipelines
- Safety interlocks
- Leak detection sensors
- Emergency venting systems

### 2. `propulsion-system.yaml`
**Purpose:** Multi-energy agnostic propulsion system interfaces  
**TFA Domain:** PPP (Propulsion-Power-Plants)  
**Version:** 1.1.0

Defines schema for:
- Fuel cell systems (PEM, SOFC, AFC, PAFC)
- Battery systems (lithium-ion, **solid-state** >600 Wh/kg)
- Electric motors (PM synchronous, induction)
- **SAF/e-SAF fuel systems** (bio-SAF, e-SAF, blends)
- **Open Fan propulsion** (CFM RISE, CATALYST, counter-rotating)
- Power management and distribution
- Multi-energy agnostic management strategies
- Performance degradation tracking

**Key Components:**
- Fuel cell stacks
- Solid-state battery packs
- Electric motors
- SAF/e-SAF fuel tanks and distribution
- Open Fan systems (unducted fans)
- Power inverters
- Multi-energy management controllers

### 3. `thermal-management.yaml`
**Purpose:** Integrated thermal management data models  
**TFA Domains:** CQH, EEE, PPP  
**Version:** 1.0.0

Defines schema for:
- Cryogenic cooling systems
- Fuel cell cooling
- Battery thermal management
- Electronics cooling (avionics, power electronics)
- Integrated thermal bus architecture
- Heat rejection systems

**Key Components:**
- Cryocoolers
- Heat exchangers
- Coolant pumps
- Thermal sensors
- Phase change materials

### 4. `bwb-h2-hy-e-utcs-extension.yaml`
**Purpose:** UTCS schema extension for BWB-H2-Hy-E components  
**TFA Domains:** All relevant (AAA, CQH, PPP, EEE, etc.)  
**Version:** 1.0.0

Extends the base AAMMPP UTCS schema with BWB-H2-Hy-E specific attributes:
- Component categories
- Hydrogen storage tank passports
- Fuel cell stack passports
- Battery pack passports
- Electric motor passports
- BWB structural elements
- System interfaces (electrical, mechanical, fluid, data)
- Safety and certification extensions

---

## Schema Usage

### Validation

All schemas are defined using JSON Schema Draft 07 and can be validated using standard JSON Schema validators.

**Python Example:**
```python
import yaml
import jsonschema

# Load schema
with open('schemas/hydrogen-subsystem.yaml', 'r') as f:
    schema = yaml.safe_load(f)

# Load data
with open('data/tank-001.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Validate
jsonschema.validate(instance=data, schema=schema)
```

**JavaScript/TypeScript Example:**
```typescript
import Ajv from 'ajv';
import yaml from 'js-yaml';

const ajv = new Ajv();
const schema = yaml.load(fs.readFileSync('schemas/propulsion-system.yaml', 'utf8'));
const data = yaml.load(fs.readFileSync('data/fuelcell-001.yaml', 'utf8'));

const validate = ajv.compile(schema);
const valid = validate(data);
```

### Integration with UTCS

These schemas integrate with the IDEALE-EU UTCS (Universal Traceability and Configuration System):

1. All components require a valid `utcs_ref` following the pattern:
   ```
   UTCS-BWB-H2-HY-E-{TFA}-{COMPONENT}-{ID}@{VERSION}
   ```

2. Components are anchored to TFA domains:
   - **CQH**: Hydrogen storage and cryogenic systems
   - **PPP**: Propulsion and power systems
   - **EEE**: Electrical systems
   - **AAA**: Airframe structures

3. Lifecycle states follow QS→FWD→UE→FE→CB→QB flow

---

## Compliance & Standards

All schemas incorporate requirements from:

### Hydrogen Systems
- **SAE J2579** - Fuel Systems in Fuel Cell Vehicles
- **ISO 19881** - Gaseous hydrogen - Land vehicle fuel containers
- **ISO 19882** - Gaseous hydrogen - Thermally activated pressure relief devices
- **EASA SC-H2** - Special Conditions for Hydrogen Propulsion
- **FAA Special Conditions** - Hydrogen Fuel Systems

### Electrical Systems
- **DO-160** - Environmental Conditions for Airborne Equipment
- **DO-254** - Hardware Design Assurance
- **SAE ARP5150** - Safety Assessment for Civil Airborne Systems
- **MIL-STD-704** - Aircraft Electric Power Characteristics

### Airworthiness
- **EASA CS-25** - Large Aeroplanes
- **FAA 14 CFR Part 25** - Airworthiness Standards
- **AS9100** - Quality Management Systems for Aerospace

---

## Development Status

| Schema | Status | Coverage | Last Updated |
|--------|--------|----------|--------------|
| hydrogen-subsystem.yaml | ✅ Active | Complete | 2025-10-23 |
| propulsion-system.yaml | ✅ Active | Complete | 2025-10-23 |
| thermal-management.yaml | ✅ Active | Complete | 2025-10-23 |
| bwb-h2-hy-e-utcs-extension.yaml | ✅ Active | Complete | 2025-10-23 |

---

## Testing

Schema validation tests are located in `../tests/` directory. Run tests with:

```bash
pytest tests/ -v --cov=schemas
```

Target coverage: **>95%** (Level C certification requirement)

---

## Contributing

When modifying schemas:

1. Update schema version following semantic versioning
2. Add examples for new properties
3. Update this README with changes
4. Run validation tests
5. Update dependent digital passport templates
6. Document breaking changes

---

## References

- [AAMMPP UTCS Schema](../../../BUSINESS/AAMMPP/01-ASSETS/UTCS_REGISTRY/SCHEMA/utcs-aammpp-v1.1.yaml)
- [UTCS Framework](../../../CONFIG_MGMT/10-TRACEABILITY/UTCS/)
- [BWB-H2-Hy-E Architecture](../../../../02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/)
- [Digital Passport Platform](../../../../digital-passport/)

---

## Contact

- **Technical Lead:** IDEALE-EU Program Office
- **Schema Governance:** Configuration Management Board
- **Issues:** Report via GitHub Issues with label `schema:bwb-h2-hy-e`

---

**Built on UTCS Manifests | Evidence-First Architecture | QS Anchoring**
