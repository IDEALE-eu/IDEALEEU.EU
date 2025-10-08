# API Bindings and Integration Specifications

## Overview

API specifications for system integration and data exchange.

## API Architecture

### RESTful APIs
**Base URL:** `https://api.supply-chain.idealeeu.eu/v1/`

**Authentication:** OAuth 2.0 Bearer Token

**Response Format:** JSON

**Common Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
Accept: application/json
API-Version: 1.0
```

## API Endpoints

### Vendor Master API

**GET /vendors**
- List all vendors
- Query parameters: status, class, page, limit
- Response: Array of vendor objects

**GET /vendors/{vendorCode}**
- Get vendor details
- Path parameter: vendorCode
- Response: Vendor object

**POST /vendors**
- Create new vendor
- Request body: Vendor object
- Response: Created vendor with ID

**PUT /vendors/{vendorCode}**
- Update vendor
- Request body: Vendor object
- Response: Updated vendor

### Material Master API

**GET /materials**
- List all materials
- Query parameters: status, abc_class, page, limit
- Response: Array of material objects

**GET /materials/{partNumber}**
- Get material details
- Response: Material object including planning, costing, compliance data

**PUT /materials/{partNumber}/planning**
- Update planning parameters
- Request body: Planning object (lead time, MOQ, safety stock)

### Purchase Order API

**POST /purchase-orders**
- Create purchase order
- Request body: PO object with line items
- Response: PO number and confirmation

**GET /purchase-orders/{poNumber}**
- Get PO details and status
- Response: PO object

**PUT /purchase-orders/{poNumber}/acknowledge**
- Supplier acknowledges PO
- Request body: Acknowledgment with confirmed dates
- Response: Acknowledgment confirmation

**GET /purchase-orders/{poNumber}/status**
- Get delivery status
- Response: Status object with line item details

### Goods Receipt API

**POST /goods-receipts**
- Record goods receipt
- Request body: Receipt object (PO, quantities, quality status)
- Response: Receipt number

**GET /goods-receipts/{receiptNumber}**
- Get receipt details
- Response: Receipt object

### Quality API

**POST /inspections**
- Record inspection results
- Request body: Inspection object
- Response: Inspection ID

**POST /scars**
- Create SCAR
- Request body: SCAR object
- Response: SCAR number

**GET /scars/{scarNumber}**
- Get SCAR details and status
- Response: SCAR object

**PUT /scars/{scarNumber}/response**
- Supplier responds to SCAR
- Request body: Response with root cause and corrective actions
- Response: Response confirmation

### Performance API

**GET /scorecards/{vendorCode}/{period}**
- Get supplier scorecard
- Path parameters: vendorCode, period (YYYY-MM)
- Response: Scorecard object with metrics

**GET /metrics/otd**
- Get on-time delivery metrics
- Query parameters: start_date, end_date, vendor_code
- Response: Metrics summary

**GET /metrics/ppm**
- Get PPM defect metrics
- Response: Defect data

## Webhooks

### Event Notifications

**ECO Notification**
```
POST {subscriber_url}/webhooks/eco
{
  "event": "eco.published",
  "eco_number": "ECO-12345",
  "affected_parts": ["PN123-456", "PN789-012"],
  "effectivity": "2024-06-01",
  "description": "Material change from Al to Ti",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Quality Alert**
```
POST {subscriber_url}/webhooks/quality
{
  "event": "quality.alert",
  "alert_type": "scar_issued",
  "scar_number": "SCAR-2024-001",
  "vendor_code": "V000001",
  "part_number": "PN123-456",
  "severity": "major",
  "timestamp": "2024-01-15T14:20:00Z"
}
```

**Delivery Confirmation**
```
POST {subscriber_url}/webhooks/delivery
{
  "event": "delivery.confirmed",
  "po_number": "PO-2024-00123",
  "asn_number": "ASN-789456",
  "estimated_arrival": "2024-01-18T08:00:00Z",
  "carrier": "FedEx",
  "tracking": "1234567890",
  "timestamp": "2024-01-15T16:45:00Z"
}
```

## Data Models

### Vendor Object
```json
{
  "vendorCode": "V000001",
  "vendorName": "Supplier A Inc",
  "status": "Active",
  "class": "Strategic",
  "address": {...},
  "contacts": [...],
  "certifications": [...],
  "performanceRating": 92
}
```

### Material Object
```json
{
  "partNumber": "PN123-456",
  "revision": "B",
  "description": "Titanium Bracket",
  "uom": "EA",
  "planning": {...},
  "costing": {...},
  "quality": {...},
  "compliance": {...}
}
```

### Purchase Order Object
```json
{
  "poNumber": "PO-2024-00123",
  "vendorCode": "V000001",
  "poDate": "2024-01-15",
  "deliveryDate": "2024-03-01",
  "status": "Open",
  "lineItems": [
    {
      "lineNumber": 1,
      "partNumber": "PN123-456",
      "quantity": 100,
      "unitPrice": 241.28,
      "currency": "USD"
    }
  ],
  "totalValue": 24128.00,
  "currency": "USD",
  "incoterms": "FCA"
}
```

## Security

### Authentication
- OAuth 2.0 with JWT tokens
- Client credentials grant for system-to-system
- Authorization code grant for user-facing apps
- Token expiration: 1 hour (refresh tokens available)

### Authorization
- Role-based access control (RBAC)
- Scopes: read, write, admin
- Resource-level permissions
- Audit logging of all API calls

### Data Protection
- TLS 1.3 for all communications
- Data encryption at rest
- PII and sensitive data masking
- GDPR compliance (data subject rights)

## Rate Limiting

- 1000 requests per hour per client
- 50 requests per minute per endpoint
- HTTP 429 (Too Many Requests) response when exceeded
- Retry-After header indicates wait time

## Error Handling

### Error Response Format
```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Missing required field: partNumber",
    "details": [...],
    "timestamp": "2024-01-15T10:30:00Z",
    "request_id": "req-abc123"
  }
}
```

### Common Error Codes
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 409: Conflict
- 422: Unprocessable Entity
- 429: Too Many Requests
- 500: Internal Server Error
- 503: Service Unavailable

## Versioning

- Version in URL path: `/v1/`, `/v2/`
- Backward compatibility maintained within major version
- Deprecation notices 6 months in advance
- Migration guide provided for breaking changes

## Documentation

- Interactive API documentation: https://api.supply-chain.idealeeu.eu/docs
- OpenAPI/Swagger specification available
- SDKs: Python, JavaScript, Java
- Code examples and tutorials
- Postman collection for testing
