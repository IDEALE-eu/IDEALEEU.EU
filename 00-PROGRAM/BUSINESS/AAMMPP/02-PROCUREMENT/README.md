# AAMMPP Procurement Module

**Purpose:** End-to-end procurement lifecycle management for aerospace components from RFQ through PO issuance and receipt.

---

## Overview

The AAMMPP Procurement module manages the full procurement lifecycle using QS→CB evidence flow:
- **QS (Quantum Superposition):** Multiple potential suppliers and quotes captured
- **FWD (Forward Wave Dynamics):** Predictive modeling and QSH optimization
- **CB (Classical Bit):** Actual PO issued and crystallized

---

## Directory Structure

```
02-PROCUREMENT/
├── RFQ/                    # Request for Quotation
│   ├── ACTIVE/            # Active RFQs awaiting quotes
│   ├── PENDING_AWARD/     # RFQs with quotes, awaiting decision
│   ├── AWARDED/           # RFQs awarded, PO issued
│   └── CANCELLED/         # Cancelled RFQs
├── PO/                     # Purchase Orders
│   ├── ACTIVE/            # Active POs awaiting delivery
│   ├── RECEIVED/          # POs with received goods
│   ├── COMPLETED/         # Fully completed POs
│   └── TEMPLATES/         # PO templates
└── SUPPLIERS/              # Verified vendor profiles
    ├── APPROVED/          # Approved supplier list
    ├── UNDER_REVIEW/      # Suppliers under evaluation
    └── SUSPENDED/         # Suspended suppliers
```

---

## Procurement Lifecycle

### 1. RFQ Creation (QS State)
**Trigger:** Component requirement identified

**Process:**
1. Create RFQ in `/RFQ/ACTIVE/`
2. PLUMA workflow auto-generates UTCS passport in QS state
3. TFA domain auto-classification
4. Identify qualified suppliers from `/SUPPLIERS/APPROVED/`
5. Notify suppliers via PLUMA workflow

**RFQ Structure:**
```yaml
rfq:
  id: RFQ-2025-1018
  component:
    part_number: "787-W-SPAR-57-2145"
    description: "Left Wing Main Spar - Boeing 787"
    tfa_domain: AAA
  quantity: 2
  required_date: "2026-06-30"
  technical_spec: "spec-787-spar-v2.pdf"
  status: active
  created: "2025-10-18T10:00:00Z"
  quote_deadline: "2025-11-01T17:00:00Z"
  utcs_ref: "UTCS-AAMMPP-AAA-WING-SPAR-787-001@1.0.0"
```

### 2. Quote Collection (FWD State)
**Trigger:** Quotes received from suppliers

**Process:**
1. Suppliers submit quotes via portal
2. UTCS passport updated with quotes (QS→FWD transition)
3. QSH optimization job triggered for supplier selection
4. Risk analysis and scenario simulation
5. Move RFQ to `/RFQ/PENDING_AWARD/`

**Quote Structure:**
```yaml
quote:
  id: QUOTE-2025-1018-001
  rfq_ref: RFQ-2025-1018
  supplier: ACME_AERO_SPARES
  price_usd: 12450.00
  lead_days: 90
  validity_date: "2026-01-31"
  payment_terms: "NET30"
  certifications: [FAA_8130-3, EASA_FORM_1]
  shipping_terms: "DAP Frankfurt"
  submitted: "2025-10-25T14:30:00Z"
```

### 3. Supplier Selection (FWD→CB)
**Trigger:** QSH optimization complete, decision ready

**Process:**
1. Review QSH recommendations (multi-objective optimization)
2. Evaluate: cost, risk, lead time, CO₂, reliability
3. Procurement team reviews and approves
4. Award decision made
5. Move RFQ to `/RFQ/AWARDED/`

**Decision Record:**
```yaml
decision:
  rfq_ref: RFQ-2025-1018
  selected_supplier: ACME_AERO_SPARES
  selected_quote: QUOTE-2025-1018-001
  justification: "Optimal balance of cost (40%), risk (30%), lead time (20%), CO₂ (10%)"
  qsh_job: QSH-SOURCING-2025-1018
  qb_recommendation: "Switch to ACME: 18% cost reduction, same DAL"
  confidence: 0.87
  approver: "J.Smith"
  approved_date: "2025-10-28T09:00:00Z"
```

### 4. PO Issuance (CB State)
**Trigger:** Supplier selected and approved

**Process:**
1. Generate PO from template in `/PO/TEMPLATES/`
2. UTCS passport updated (FWD→CB transition)
3. PO stored in `/PO/ACTIVE/`
4. Notify supplier and requestor
5. Schedule delivery tracking

**PO Structure:**
```yaml
po:
  number: PO-2025-8891
  rfq_ref: RFQ-2025-1018
  supplier: ACME_AERO_SPARES
  supplier_address: "123 Aero Drive, Seattle, WA 98101, USA"
  
  line_items:
    - line: 1
      part_number: "787-W-SPAR-57-2145"
      description: "Left Wing Main Spar - Boeing 787"
      quantity: 2
      unit_price_usd: 12450.00
      total_usd: 24900.00
      
  terms:
    payment: NET30
    delivery: "2026-06-30"
    shipping: "DAP Frankfurt Main Depot"
    incoterms: DAP
    
  certifications_required:
    - FAA_8130-3
    - EASA_FORM_1
    - Material_Test_Report
    
  issue_date: "2025-10-28T09:30:00Z"
  utcs_ref: "UTCS-AAMMPP-AAA-WING-SPAR-787-001@1.5.0"
  status: active
```

### 5. Receipt & Acceptance (CB→UE)
**Trigger:** Goods received at warehouse

**Process:**
1. Receipt inspection at warehouse
2. Certificate validation (FAA 8130-3, EASA Form 1)
3. UTCS passport updated with serial number (CB→UE)
4. Move PO to `/PO/RECEIVED/`
5. Trigger baseline inspection via PLUMA

**Receipt Record:**
```yaml
receipt:
  po_number: PO-2025-8891
  received_date: "2026-06-25T10:15:00Z"
  location: FRA_WAREHOUSE_A3
  inspector: "K.Johnson"
  
  items:
    - line: 1
      part_number: "787-W-SPAR-57-2145"
      serial_number: "SN-787-SPAR-001234"
      quantity_received: 2
      condition: acceptable
      certificates:
        - type: FAA_8130-3
          number: "8130-3-2023-787-W-001234"
        - type: EASA_FORM_1
          number: "EASA-F1-2023-787-001234"
          
  inspection:
    visual: pass
    dimensional: pass
    documentation: complete
    
  utcs_updated: true
  lifecycle_state: UE
```

---

## Supplier Management

### Approved Suppliers List (ASL)
Location: `/SUPPLIERS/APPROVED/`

**Criteria for Approval:**
- AS9120 certification (mandatory)
- AS9100 certification
- Minimum rating: 4.0/5.0
- Financial stability check
- Past performance record
- ITAR/EAR compliance

**Supplier Profile:**
```yaml
supplier:
  id: ACME_AERO_SPARES
  name: "ACME Aerospace Spares Inc."
  location: "Seattle, WA, USA"
  
  certifications:
    - type: AS9120
      number: "AS9120-2023-001"
      expiry: "2026-12-31"
    - type: AS9100
      number: "AS9100-2023-045"
      expiry: "2026-12-31"
      
  tfa_expertise:
    - AAA: [structural_components, wing_assemblies]
    - MMM: [hydraulic_systems, mechanical_assemblies]
    - PPP: [engine_components]
    
  rating: 4.5
  performance:
    on_time_delivery: 0.95
    quality_score: 0.92
    response_time_hours: 24
    
  contact:
    primary: "sales@acmeaero.com"
    technical: "engineering@acmeaero.com"
    quality: "quality@acmeaero.com"
    
  financial:
    credit_limit_usd: 500000
    payment_terms: [NET30, NET60]
    
  compliance:
    itar_registered: true
    ear_compliant: true
    
  approved_date: "2023-01-15"
  next_review: "2026-01-15"
```

---

## Integration Points

### UTCS Registry
- All procurement events update component UTCS passports
- State transitions: QS → FWD → CB → UE
- Link: `/01-ASSETS/UTCS_REGISTRY/`

### Quantum Optimization
- QSH jobs for supplier selection
- Multi-objective optimization
- Link: `/08-QUANTUM/QSH_JOBS/`

### A360Exchanges-TT
- Marketplace sourcing integration
- Circular economy components
- Link: `/10-BUSINESS/A360-EXCHANGES-TT/`

### Finance
- Cost tracking and budgets
- Invoice processing
- Link: `/05-FINANCE/`

---

## Automation (PLUMA)

### Automated Workflows
1. **RFQ Creation:** Auto-generate UTCS, classify TFA, notify suppliers
2. **Quote Expiry:** Daily check, trigger re-sourcing if needed
3. **Supplier Performance:** Monthly evaluation, rating updates
4. **PO Reminders:** Delivery date approaching notifications
5. **Receipt Validation:** Certificate checks, UTCS updates

See: [PLUMA Hooks](../06-INTEGRATION/PLUMA_HOOKS/)

---

## Compliance

### Standards
- **AS9120:** Aerospace distributor quality management
- **AS9100:** Aerospace quality management
- **ATA iSpec 2000:** Component data exchange
- **FAR Part 21:** Airworthiness standards

### Documentation
- All RFQs, quotes, POs retained for 7 years
- Certificate copies stored with each PO
- Audit trail maintained in UTCS
- Export control checks for ITAR components

See: [Compliance](../07-TRACEABILITY/COMPLIANCE/)

---

## Metrics & KPIs

### Procurement Performance
- **Fill Rate:** % of RFQs successfully fulfilled
- **Time to Award:** Average days from RFQ to PO
- **Cost Savings:** Actual vs. budget
- **Supplier Performance:** On-time delivery rate

### Dashboard
Location: `/00-PROGRAM/DIGITAL_THREAD/10-METRICS/PROCUREMENT/`

---

## References

- [AAMMPP Platform](../)
- [UTCS Registry](../01-ASSETS/UTCS_REGISTRY/)
- [QSH Jobs](../08-QUANTUM/QSH_JOBS/)
- [PLUMA Workflows](../06-INTEGRATION/PLUMA_HOOKS/)

---

**Owner:** AAMMPP Procurement Team  
**Last Updated:** 2025-10-18  
**Next Review:** 2025-11-18
