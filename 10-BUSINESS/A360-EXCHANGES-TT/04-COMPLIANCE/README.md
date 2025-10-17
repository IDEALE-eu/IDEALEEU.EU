# A360 Compliance Framework

**Version:** 1.0  
**UTCS:** `utcs://BUSINESS/A360-EXCHANGES-TT/COMPLIANCE`

## Overview

The A360exchanges-TT platform is designed for EU-first deployment with full compliance to current and upcoming regulations. This document outlines compliance requirements and implementation strategies.

## Regulatory Landscape

### Primary Regulations

1. **ESPR** - Ecodesign for Sustainable Products Regulation
2. **DPP** - Digital Product Passport (part of ESPR)
3. **Right-to-Repair** - EU Right to Repair Directive
4. **CRA** - Cyber Resilience Act
5. **WEEE** - Waste Electrical and Electronic Equipment Directive

### Secondary Regulations

- GDPR - General Data Protection Regulation
- PSD2 - Payment Services Directive 2
- eIDAS - Electronic Identification and Trust Services
- AML/KYC - Anti-Money Laundering / Know Your Customer

## ESPR Compliance

### Requirements

The Ecodesign for Sustainable Products Regulation requires:
- Product durability information
- Repairability scores
- Recyclability data
- Carbon footprint disclosure
- Spare parts availability
- Software update commitment

### Implementation

**Data Model Integration:**
```json
{
  "espr_compliance": {
    "durability_rating": 8.5,
    "repairability_score": 7.8,
    "recyclability_pct": 85,
    "carbon_footprint_kg": 125.5,
    "expected_lifespan_years": 15,
    "spare_parts_available_until": "2040-12-31",
    "software_support_until": "2038-12-31"
  }
}
```

**Required Fields in Asset Model:**
- `espr_compliant`: Boolean flag
- `sustainability_metrics`: Object with ESPR fields
- `lifecycle_assessment_uri`: Link to full LCA report

**Validation:**
- All assets must have ESPR fields before listing
- Completeness check: ≥90% of required fields
- Annual review and update requirement

## Digital Product Passport (DPP)

### Requirements

Every component in the A360 marketplace must have a DPP containing:
- Unique identifier
- Manufacturer information
- Manufacturing date and location
- Material composition
- Repair history
- Recycling instructions
- End-of-life guidance

### Implementation

**Core DPP Structure:**
```json
{
  "DPP_id": "DPP-2025-123456",
  "identifier": {
    "gtin": "1234567890123",
    "serial": "SN123456",
    "batch": "BATCH-2025-001"
  },
  "manufacturer": {
    "name": "AeroTech Industries",
    "id": "EU123456789",
    "address": "...",
    "contact": "..."
  },
  "product_info": {
    "type": "avionics_computer",
    "model": "AC-500X",
    "manufacturing_date": "2025-01-15",
    "manufacturing_location": "Munich, Germany"
  },
  "materials": {
    "composition": [
      { "material": "aluminum_6061", "percentage": 45 },
      { "material": "copper", "percentage": 15 },
      { "material": "silicon", "percentage": 20 },
      { "material": "plastics_abs", "percentage": 20 }
    ],
    "hazardous_substances": []
  },
  "lifecycle": {
    "events": [...],
    "repairs": [...],
    "certifications": [...]
  },
  "eol_guidance": {
    "disassembly_instructions_uri": "...",
    "recycling_instructions_uri": "...",
    "takeback_program": "..."
  }
}
```

**QR/NFC Integration:**
- QR code generated at DPP issuance
- NFC tag embedded in physical component
- Both link to: `https://dpp.a360.idealeeu.eu/{DPP_id}`

**Update Triggers:**
- Component transfer (custody change)
- Repair completion
- Certification renewal
- Software/firmware update

## Right-to-Repair Compliance

### Requirements

The EU Right to Repair Directive mandates:
- Access to repair information
- Availability of spare parts (minimum 7-10 years)
- Fair pricing for spare parts
- Independent repair provider access
- Standard repair forms

### Implementation

**EU Repair Form API:**

The platform provides a standardized repair form endpoint:

```http
POST /repair/create_form
{
  "serial": "SN123456",
  "issue_description": "...",
  "customer_id": "...",
  "warranty_status": "active"
}
```

**Form Fields:**
- Product identification (serial, model)
- Issue description
- Customer information
- Warranty status
- Preferred repair center
- Timeline requirements
- Cost expectations

**Spare Parts Tracking:**
```json
{
  "part_no": "PWR-REG-500",
  "available_until": "2035-12-31",
  "suppliers": [
    {
      "id": "SUP-12345",
      "name": "OEM Direct",
      "price_eur": 150.00,
      "lead_time_days": 7
    },
    {
      "id": "SUP-67890",
      "name": "Certified Aftermarket",
      "price_eur": 120.00,
      "lead_time_days": 14
    }
  ],
  "repair_documentation_uri": "https://repair.a360.eu/docs/PWR-REG-500"
}
```

**Independent Repairer Access:**
- Public API for certified repair centers
- Documentation available to qualified repairers
- No discrimination in spare parts pricing
- Diagnostic tool availability

## CRA (Cyber Resilience Act)

### Requirements

The Cyber Resilience Act requires:
- Software Bill of Materials (SBOM)
- Vulnerability disclosure process
- Mandatory security updates
- Incident reporting
- Support timeline declaration

### Implementation

**SBOM Integration:**

Every component with software/firmware must have an SBOM:

```json
{
  "sbom_format": "CycloneDX",
  "sbom_version": "1.4",
  "components": [
    {
      "type": "library",
      "name": "openssl",
      "version": "3.0.8",
      "licenses": ["Apache-2.0"],
      "hashes": ["sha256:abc123..."]
    }
  ],
  "dependencies": [...],
  "vulnerabilities": []
}
```

**Stored at:** `Asset.SBOM_uri`

**CVD (Coordinated Vulnerability Disclosure):**

Security contact for each lease:

```json
{
  "lease_id": "LSE-2025-001234",
  "security_contact": "security@lessor.com",
  "disclosure_policy": "https://lessor.com/security-policy",
  "response_time_hours": 72,
  "patch_delivery_days": 30
}
```

**Update SLA:**

Mandatory for all leases:

```json
{
  "update_SLA": {
    "critical_update_hours": 24,
    "security_update_days": 7,
    "routine_update_days": 30,
    "maintenance_window": "Sundays 00:00-06:00 UTC"
  }
}
```

**Support Timeline:**

Declared in asset definition:

```json
{
  "support_timeline": {
    "security_updates_until": "2035-12-31",
    "feature_updates_until": "2030-12-31",
    "spare_parts_until": "2038-12-31",
    "eol_date": "2040-01-01"
  }
}
```

## WEEE Compliance

### Requirements

Waste Electrical and Electronic Equipment Directive:
- Product categorization
- Collection and recycling obligations
- Take-back schemes
- Recycling rate targets
- Hazardous substance restrictions (RoHS)

### Implementation

**WEEE Categorization:**

Automatic category assignment based on product type:

```json
{
  "WEEE_cat": "CAT-3",
  "category_name": "IT and telecommunications equipment",
  "recycling_target_pct": 85,
  "recovery_target_pct": 80
}
```

**Categories:**
- CAT-1: Temperature exchange equipment
- CAT-2: Screens and monitors
- CAT-3: Lamps
- CAT-4: Large equipment
- CAT-5: Small equipment
- CAT-6: Small IT and telecommunications equipment
- CAT-7: Photovoltaic panels

**Take-Back Routing:**

At RMA (Return Merchandise Authorization):

```json
{
  "rma_id": "RMA-2025-001234",
  "return_reason": "end_of_life",
  "weee_routing": {
    "category": "CAT-6",
    "recycler_id": "RCY-12345",
    "recycler_name": "EcoRecycle EU",
    "collection_date": "2025-11-01",
    "certificate_uri": "https://certs.a360.eu/WEEE-2025-001234"
  }
}
```

**Recycler Network:**

Platform maintains network of certified recyclers:

```json
{
  "recycler_id": "RCY-12345",
  "name": "EcoRecycle EU",
  "certifications": [
    "WEEELABEX",
    "ISO 14001",
    "R2v3"
  ],
  "accepted_categories": ["CAT-3", "CAT-5", "CAT-6"],
  "location": "Berlin, Germany",
  "recycling_rate_pct": 92
}
```

## Compliance Monitoring

### Automated Checks

**Pre-Listing Validation:**
```python
def validate_listing_compliance(listing):
    checks = {
        "dpp_exists": listing.asset.DPP_id is not None,
        "dpp_complete": listing.DPP_snapshot.completeness_pct >= 80,
        "espr_compliant": listing.asset.espr_compliant,
        "sbom_available": listing.asset.SBOM_uri is not None,
        "weee_categorized": listing.asset.WEEE_cat in VALID_CATEGORIES
    }
    return all(checks.values()), checks
```

**Periodic Audits:**
- Quarterly DPP completeness review
- Annual ESPR data refresh
- SBOM vulnerability scanning (weekly)
- Recycler certification verification (annual)

### Reporting

**Compliance Dashboard KPIs:**
- DPP completeness: ≥95% target
- ESPR compliance rate: 100% target
- WEEE take-back rate: ≥85% target
- CRA vulnerability response: <7 days average
- Right-to-Repair request fulfillment: <14 days average

### Penalties

**Non-Compliance Actions:**
1. **Warning** - First occurrence, 7-day cure period
2. **Listing Suspension** - Repeated violations
3. **Account Suspension** - Systemic non-compliance
4. **Regulatory Reporting** - Serious violations

## Integration with Platform

### Database Fields

All compliance data stored in appropriate models:
- `Asset.espr_compliant`, `Asset.SBOM_uri`, `Asset.WEEE_cat`
- `DPP.compliance_status`, `DPP.attestations`
- `Repair.EU_form`, `Repair.warranty`
- `Lease.update_SLA`, `Lease.security_contact`

### API Validation

All API endpoints validate compliance before transactions:
- Listing creation checks DPP completeness
- Lease underwriting checks CRA requirements
- Repair quotes include Right-to-Repair disclosures
- End-of-life processes route through WEEE system

### Audit Trail

Full traceability via UTCS:
- All compliance events logged
- Immutable audit trail
- Regulatory reporting capability

## References

- [EU ESPR Regulation](https://ec.europa.eu/environment/ecodesign/)
- [Digital Product Passport Guidelines](https://single-market-economy.ec.europa.eu/dpp)
- [Right to Repair Directive](https://ec.europa.eu/info/law/better-regulation/right-repair)
- [Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
- [WEEE Directive](https://ec.europa.eu/environment/waste/weee/)

---

**Compliance Officer:** IDEALE-EU Compliance Board  
**Last Review:** 2025-10-17  
**Next Review:** 2026-01-17
