# UTCS Registry - AAMMPP Asset Passport Master Index

**Purpose:** Master index of all aerospace component digital passports managed by AAMMPP.

**UTCS Namespace:** `utcs://AAMMPP/<TFA>/<ASSET_TYPE>/<ASSET_ID>`

---

## Overview

The UTCS Registry is the central repository for all aerospace component digital passports within the AAMMPP platform. Each registered asset carries a complete lifecycle record from procurement through retirement, anchored using the QS→CB evidence flow.

---

## Registry Structure

```
UTCS_REGISTRY/
├── README.md                    # This file
├── SCHEMA/                      # UTCS schema definitions
│   ├── utcs-aammpp-v1.1.yaml   # AAMMPP-specific UTCS schema
│   └── validation-rules.yaml    # Schema validation rules
├── INDEX/                       # Asset passport index
│   ├── BY_TFA/                 # Organized by TFA domain
│   │   ├── AAA/                # Airframes-Aerodynamics-Airworthiness
│   │   ├── LIB/                # Logistics-Inventory-Blockchain
│   │   ├── MMM/                # Mechanical-Material-Modules
│   │   └── ...                 # Other TFA domains
│   ├── BY_SUPPLIER/            # Organized by supplier/OEM
│   └── BY_STATUS/              # Organized by lifecycle status
├── TEMPLATES/                   # UTCS passport templates
│   ├── component-template.yaml
│   ├── assembly-template.yaml
│   └── consumable-template.yaml
└── EXAMPLES/                    # Example UTCS passports
    ├── wing-spar-example.yaml
    ├── avionics-module-example.yaml
    └── hydraulic-pump-example.yaml
```

---

## UTCS Passport Lifecycle States

| State | Code | Description |
|-------|------|-------------|
| **Quantum Superposition** | QS | Pre-event state with multiple possible outcomes |
| **Forward Wave Dynamics** | FWD | Predictive modeling and simulation |
| **Unit Element** | UE | Classical fundamental unit definition |
| **Federation Entanglement** | FE | Multi-party coordination and updates |
| **Classical Bit** | CB | Actual event crystallization |
| **Qubit Optimization** | QB | Quantum-optimized recommendations |

---

## Passport Registration Process

### 1. Initial Registration (QS State)
```yaml
# New asset enters system in QS state
lifecycle_state: QS
procurement:
  potential_suppliers: [ACME, VENDOR_B, SUPPLIER_C]
  quote_range_usd: [8000, 12000]
  lead_time_range_days: [14, 45]
```

### 2. Quotation (QS→FWD)
```yaml
# Multiple quotes received, predictive modeling
lifecycle_state: FWD
procurement:
  quotes:
    - supplier: ACME
      price_usd: 9500
      lead_days: 21
    - supplier: VENDOR_B
      price_usd: 11200
      lead_days: 14
```

### 3. Purchase Order (CB State)
```yaml
# PO issued, event crystallized
lifecycle_state: CB
procurement:
  selected_supplier: ACME
  po_ref: PO-2025-8891
  price_usd: 9500
  delivery_date: 2025-11-08
```

### 4. Receipt & Installation (UE)
```yaml
# Asset received with serial number
lifecycle_state: UE
asset_identity:
  serial_number: SN-787-SPAR-001234
  receipt_date: 2025-11-05
  install_date: 2025-11-10
  install_location: A/C-MSN-50123-LEFT-WING
```

### 5. In-Service Operations (FE)
```yaml
# Federated updates from maintenance, operations
lifecycle_state: FE
maintenance:
  flight_hours: 2450
  flight_cycles: 1820
  next_inspection: 2026-08-15
  sb_compliance: [SB-787-28-0042, SB-787-28-0043]
```

### 6. Optimization (QB)
```yaml
# Quantum optimization for next lifecycle event
lifecycle_state: QB
quantum:
  recommendation: "Exchange recommended in 180 days"
  confidence: 0.87
  cost_benefit_analysis:
    current_maintenance_cost: 2400
    new_component_cost: 9200
    reliability_improvement: 0.15
```

---

## TFA Domain Classification

Assets are classified into one of 15 TFA domains:

### Primary Domains for AAMMPP

| Code | Domain | Common Assets |
|------|--------|---------------|
| **AAA** | Airframes-Aerodynamics-Airworthiness | Wing spars, fuselage sections, control surfaces |
| **LIB** | Logistics-Inventory-Blockchain | Warehouse systems, tracking devices, blockchain anchors |
| **MMM** | Mechanical-Material-Modules | Hydraulic pumps, actuators, mechanical assemblies |
| **PPP** | Propulsion-Power-Plants | Engine components, fuel systems, APU parts |
| **EDI** | Electronics-Digital-Instruments | Avionics modules, sensors, displays |
| **EEE** | Electrical-Endocircular-Energization | Power distribution, batteries, generators |

See [TFA Domains Reference](../../../../README.md#tfa-canonical-domains) for complete list.

---

## Passport Attributes

### Mandatory Fields
- `utcs_ref` - Unique UTCS reference identifier
- `utcs_schema` - Schema version (currently 1.1.0)
- `type` - Asset type (aerospace-component, assembly, consumable)
- `anchor` - AAMMPP asset anchor path
- `tfa_domain` - TFA domain classification
- `lifecycle_state` - Current lifecycle state (QS/FWD/UE/FE/CB/QB)

### Procurement Section
- `last_quote_usd` - Most recent quote value
- `quote_valid_until` - Quote validity date
- `supplier` - Supplier/OEM identifier
- `po_ref` - Purchase order reference

### Maintenance Section
- `next_inspection` - Next scheduled inspection
- `total_cycles` - Total operational cycles
- `total_hours` - Total operational hours
- `sb_compliance` - Applicable service bulletins

### Logistics Section
- `current_location` - Current physical location
- `last_movement` - Last movement date
- `condition` - Current condition (serviceable, repairable, condemned)

### Digital Passport Section
- `registry` - Digital passport registry (HUELLΔ)
- `badge` - AAMMPP badge identifier
- `verification_url` - URL for passport verification

### Quantum Section (Optional)
- `qsh_job` - Associated QSH job identifier
- `qb_recommendation` - Quantum optimization recommendation

---

## Integration with A360Exchanges-TT

AAMMPP UTCS passports are integrated with A360Exchanges-TT marketplace:

```yaml
# A360Exchanges-TT extension
exchange:
  platform: A360Exchanges-TT
  marketplace_status: available  # available, listed, leased, in_repair
  last_transaction: 2025-10-18T14:30:00Z
  token_reward_earned_tt: 42.5
  circularity_score: 0.87
  dpp_id: DPP-A360EX-787-SPAR-001234
```

---

## Search and Query

### By TFA Domain
```bash
# Find all assets in AAA domain
find INDEX/BY_TFA/AAA/ -name "*.yaml"
```

### By Lifecycle State
```bash
# Find all assets in CB state
grep -r "lifecycle_state: CB" INDEX/BY_STATUS/
```

### By Supplier
```bash
# Find all assets from ACME
grep -r "supplier: ACME" INDEX/BY_SUPPLIER/
```

### By Next Inspection
```bash
# Find assets requiring inspection in next 30 days
# (requires custom script or database query)
```

---

## Validation Rules

All UTCS passports must:
1. Conform to `utcs-aammpp-v1.1.yaml` schema
2. Have valid TFA domain classification
3. Include complete procurement history
4. Link to valid digital passport in HUELLΔ registry
5. Maintain QS→CB state transition integrity

See [validation-rules.yaml](SCHEMA/validation-rules.yaml) for detailed rules.

---

## API Access

### Read Passport
```http
GET /aammpp/registry/{utcs_ref}
Authorization: Bearer {token}
```

### Update Passport
```http
PATCH /aammpp/registry/{utcs_ref}
Authorization: Bearer {token}
Content-Type: application/yaml

maintenance:
  total_cycles: 4250
  last_inspection: 2025-10-15
```

### Search Registry
```http
POST /aammpp/registry/search
Authorization: Bearer {token}
Content-Type: application/json

{
  "tfa_domain": "AAA",
  "lifecycle_state": "CB",
  "supplier": "ACME"
}
```

---

## Compliance

AAMMPP UTCS Registry maintains compliance with:
- **AS9120** - Aerospace quality management
- **FAA 8130-3** - Airworthiness approval tags
- **EASA Form 1** - Authorized release certificate
- **ATA iSpec 2000** - Component data exchange
- **S1000D** - Technical publication standards

---

## References

- [UTCS Framework](../../../CONFIG_MGMT/10-TRACEABILITY/UTCS/)
- [AAMMPP Platform](../)
- [A360Exchanges-TT](../../../../10-BUSINESS/A360-EXCHANGES-TT/)
- [Digital Passport Dashboard](../../../../digital-passport/)

---

**Owner:** AAMMPP Registry Administrator  
**Last Updated:** 2025-10-18  
**Next Review:** 2025-11-18
