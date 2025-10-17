# A360 API Specifications

**Version:** 1.0  
**Base URL:** `https://api.a360.idealeeu.eu/v1`  
**UTCS:** `utcs://BUSINESS/A360-EXCHANGES-TT/API`

## Overview

RESTful API specifications for all A360 platform services. All endpoints follow common patterns:
- Authentication via Bearer token or API key
- Standard HTTP status codes
- JSON request/response bodies
- Rate limiting: 1000 requests/hour (standard), 10000/hour (premium)

## Authentication

```http
Authorization: Bearer <jwt_token>
X-API-Key: <api_key>
```

## Common Response Format

### Success Response
```json
{
  "status": "success",
  "data": { ... },
  "metadata": {
    "timestamp": "2025-10-17T13:00:00Z",
    "request_id": "req_abc123"
  }
}
```

### Error Response
```json
{
  "status": "error",
  "error": {
    "code": "ERR_CODE",
    "message": "Human readable error",
    "details": { ... }
  },
  "metadata": {
    "timestamp": "2025-10-17T13:00:00Z",
    "request_id": "req_abc123"
  }
}
```

## Market API (`/market`)

### Create Listing

**Endpoint:** `POST /market/list`

**Request:**
```json
{
  "asset_uuid": "550e8400-e29b-41d4-a716-446655440000",
  "serial": "SN123456",
  "price": 50000.00,
  "lot": 1,
  "listing_type": "fixed_price",
  "condition": {
    "SoH": 0.95,
    "hours_remaining": 5000
  }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "listing_id": "LST-2025-001234",
    "state": "active",
    "created_at": "2025-10-17T13:00:00Z",
    "expires_at": "2025-11-17T13:00:00Z"
  }
}
```

### Place Bid

**Endpoint:** `POST /market/bid`

**Request:**
```json
{
  "listing_id": "LST-2025-001234",
  "amount": 48000.00,
  "quantity": 1
}
```

### Match Orders

**Endpoint:** `POST /market/match`

**Request:**
```json
{
  "listing_id": "LST-2025-001234",
  "bid_id": "BID-2025-005678"
}
```

### Settle Transaction

**Endpoint:** `POST /market/settle`

**Request:**
```json
{
  "transaction_id": "TXN-2025-009876",
  "custody_proof": "0x1234567890abcdef..."
}
```

## Lease API (`/lease`)

### Get Lease Quote

**Endpoint:** `POST /lease/quote`

**Request:**
```json
{
  "asset_uuid": "550e8400-e29b-41d4-a716-446655440000",
  "serial": "SN123456",
  "term_months": 12,
  "usage_caps": {
    "max_hours": 2000,
    "max_cycles": 5000
  },
  "collateral_tt": 10000
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "quote_id": "QTE-2025-001234",
    "rates": {
      "base_rate_eur_per_day": 50.00,
      "usage_rate_eur_per_hour": 5.00
    },
    "collateral_required": {
      "EUR": 25000.00,
      "TT": 10000.00,
      "haircut_applied": 0.15
    },
    "total_estimated_cost": 21900.00,
    "valid_until": "2025-10-24T13:00:00Z"
  }
}
```

### Underwrite Lease

**Endpoint:** `POST /lease/underwrite`

**Request:**
```json
{
  "quote_id": "QTE-2025-001234",
  "lessee_id": "ORG-12345",
  "start": "2025-11-01T00:00:00Z",
  "collateral_deposit": {
    "EUR": 25000.00,
    "TT": 10000.00
  }
}
```

### Report Usage

**Endpoint:** `POST /lease/post-usage`

**Request:**
```json
{
  "lease_id": "LSE-2025-001234",
  "period": "2025-11",
  "usage": {
    "hours": 150,
    "cycles": 380,
    "kWh": 2250
  },
  "telemetry_hash": "0xabcdef1234567890..."
}
```

### Settle Lease

**Endpoint:** `POST /lease/settle`

**Request:**
```json
{
  "lease_id": "LSE-2025-001234",
  "final_usage": {
    "hours": 1950,
    "cycles": 4800,
    "kWh": 29250
  },
  "condition_on_return": {
    "SoH": 0.92,
    "damage_notes": ""
  }
}
```

## Repair API (`/repair`)

### Create EU Repair Form

**Endpoint:** `POST /repair/create_form`

**Request:**
```json
{
  "serial": "SN123456",
  "reported_issue": "Power supply intermittent",
  "customer_id": "ORG-12345",
  "warranty_applicable": true
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "repair_id": "REP-2025-001234",
    "eu_form_id": "EU-FORM-2025-001234",
    "form_url": "https://a360.idealeeu.eu/repair/EU-FORM-2025-001234",
    "state": "form_submitted"
  }
}
```

### Get Repair Quote

**Endpoint:** `POST /repair/quote`

**Request:**
```json
{
  "repair_id": "REP-2025-001234",
  "diagnostic_summary": "Replace power regulator module",
  "parts": [
    {
      "part_no": "PWR-REG-500",
      "quantity": 1,
      "unit_cost": 150.00
    }
  ],
  "labor_hours": 4,
  "labor_rate": 75.00
}
```

### Approve Repair

**Endpoint:** `POST /repair/approve`

**Request:**
```json
{
  "repair_id": "REP-2025-001234",
  "quote_id": "RPQ-2025-005678",
  "approved": true
}
```

### Recertify Component

**Endpoint:** `POST /repair/recertify`

**Request:**
```json
{
  "repair_id": "REP-2025-001234",
  "test_results": {
    "functional_test": "pass",
    "performance_test": "pass",
    "safety_test": "pass"
  },
  "certifying_authority": "LAB-54321",
  "certificate_uri": "https://certs.a360.eu/CERT-2025-009876"
}
```

## DPP API (`/dpp`)

### Issue Passport

**Endpoint:** `POST /dpp/issue`

**Request:**
```json
{
  "asset_uuid": "550e8400-e29b-41d4-a716-446655440000",
  "serial": "SN123456",
  "manufacturer": "AeroTech Industries",
  "manufacture_date": "2025-01-15",
  "espr_fields": {
    "repairability_score": 8.5,
    "recyclability_score": 7.8,
    "carbon_footprint_kg": 125.5
  }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "DPP_id": "DPP-2025-123456",
    "qr_code_uri": "https://dpp.a360.eu/qr/DPP-2025-123456.png",
    "nfc_data": "nfc://dpp.a360.eu/DPP-2025-123456",
    "blockchain_anchor": "0x9876543210abcdef...",
    "fees": {
      "eur": 0.10,
      "tt": 0.05
    }
  }
}
```

### Read Passport

**Endpoint:** `GET /dpp/read/{dpp_id}`

**Response:**
```json
{
  "status": "success",
  "data": {
    "DPP_id": "DPP-2025-123456",
    "asset_uuid": "550e8400-e29b-41d4-a716-446655440000",
    "serial": "SN123456",
    "lifecycle_events": [...],
    "attestations": [...],
    "compliance_status": {
      "espr": "compliant",
      "cra": "compliant",
      "weee": "compliant"
    }
  }
}
```

### Add Attestation

**Endpoint:** `POST /dpp/attest`

**Request:**
```json
{
  "DPP_id": "DPP-2025-123456",
  "attestation_type": "performance_test",
  "attester_id": "LAB-54321",
  "test_results": {
    "voltage_stability": "pass",
    "thermal_performance": "pass"
  },
  "evidence_uri": "https://tests.a360.eu/TEST-2025-009876"
}
```

### Revoke Passport

**Endpoint:** `POST /dpp/revoke`

**Request:**
```json
{
  "DPP_id": "DPP-2025-123456",
  "reason": "Component decommissioned",
  "authority": "ORG-12345"
}
```

## Risk API (`/risk`)

### Calculate Health-Based Pricing

**Endpoint:** `POST /risk/price_health`

**Request:**
```json
{
  "asset_uuid": "550e8400-e29b-41d4-a716-446655440000",
  "serial": "SN123456",
  "base_price": 50000.00,
  "telemetry": {
    "SoH": 0.92,
    "hours": 3500,
    "error_count": 12,
    "thermal_events": 3
  }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "adjusted_price": 44800.00,
    "health_multiplier": 0.896,
    "factors": {
      "SoH_factor": 0.92,
      "usage_factor": 0.95,
      "reliability_factor": 0.98
    }
  }
}
```

### Calculate Collateral Requirement

**Endpoint:** `POST /risk/calc_collateral`

**Request:**
```json
{
  "lease_value": 100000.00,
  "usage_horizon_months": 12,
  "asset_volatility": 0.15,
  "insurance_coverage": 80000.00
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "required_collateral": 25000.00,
    "var_95": 105000.00,
    "calculation": "VaR_95(105000) - insurance(80000) = 25000"
  }
}
```

### Trigger Slashing

**Endpoint:** `POST /risk/trigger_slash`

**Request:**
```json
{
  "stake_id": "STK-2025-001234",
  "violation": "sla_breach_major",
  "evidence": "https://evidence.a360.eu/EVD-2025-009876"
}
```

## Token API (`/tt`)

### Get Balances

**Endpoint:** `GET /tt/balances/{account_id}`

**Response:**
```json
{
  "status": "success",
  "data": {
    "account_id": "ACC-12345",
    "balance_tt": 50000.00,
    "staked_tt": 25000.00,
    "rewards_pending_tt": 125.50,
    "locked_until": "2026-01-15T00:00:00Z"
  }
}
```

### Stake Tokens

**Endpoint:** `POST /tt/stake`

**Request:**
```json
{
  "amount_tt": 25000.00,
  "role": "service_provider",
  "lock_period_days": 180
}
```

### Unstake Tokens

**Endpoint:** `POST /tt/unstake`

**Request:**
```json
{
  "stake_id": "STK-2025-001234",
  "amount_tt": 10000.00
}
```

### Execute Slash

**Endpoint:** `POST /tt/slash`

**Request:**
```json
{
  "stake_id": "STK-2025-001234",
  "slash_amount_tt": 2500.00,
  "reason": "sla_breach_major",
  "evidence_uri": "https://evidence.a360.eu/EVD-2025-009876"
}
```

### Get Rewards

**Endpoint:** `GET /tt/rewards/{account_id}`

**Response:**
```json
{
  "status": "success",
  "data": {
    "account_id": "ACC-12345",
    "total_rewards_tt": 1250.50,
    "breakdown": {
      "trading_fees": 500.25,
      "service_fees": 600.00,
      "attestation_fees": 150.25
    },
    "last_distribution": "2025-10-15T00:00:00Z"
  }
}
```

## Rate Limits

| Tier | Requests/Hour | Burst | Cost |
|------|---------------|-------|------|
| Free | 100 | 10 | Free |
| Standard | 1,000 | 50 | €50/month |
| Premium | 10,000 | 200 | €200/month |
| Enterprise | Unlimited | Custom | Contact sales |

## Error Codes

| Code | Description | HTTP Status |
|------|-------------|-------------|
| ERR_AUTH | Authentication failed | 401 |
| ERR_FORBIDDEN | Insufficient permissions | 403 |
| ERR_NOT_FOUND | Resource not found | 404 |
| ERR_VALIDATION | Request validation failed | 400 |
| ERR_RATE_LIMIT | Rate limit exceeded | 429 |
| ERR_SERVER | Internal server error | 500 |
| ERR_INSUFFICIENT_BALANCE | Insufficient TT balance | 402 |
| ERR_STAKE_LOCKED | Stake is locked | 423 |
| ERR_DPP_INVALID | DPP validation failed | 400 |

## Webhooks

Subscribe to events:
- `listing.created`
- `listing.sold`
- `lease.started`
- `lease.ended`
- `repair.completed`
- `dpp.issued`
- `stake.slashed`

## SDK Support

- Python: `pip install a360-sdk`
- Node.js: `npm install @a360/sdk`
- Go: `go get github.com/a360/sdk-go`

## OpenAPI Specification

Full OpenAPI 3.0 specification available at:
- [openapi.yaml](./openapi.yaml)
- [Swagger UI](https://api.a360.idealeeu.eu/docs)

## References

- [Data Models](../01-DATA-MODELS/)
- [Authentication Guide](./authentication.md)
- [Rate Limiting](./rate_limiting.md)
- [Webhooks Guide](./webhooks.md)
