---
layout: page
title: "API Documentation"
description: "REST API reference for IDEALE-EU platform"
---

# API Documentation

Complete REST API reference with authentication, endpoints, and code examples for integrating with the IDEALE-EU platform.

> **Status**: Coming soon. This page will be updated with comprehensive API documentation including authentication flows, endpoint specifications, and code examples in Python, Java, JavaScript, and C++.

---

## Overview

The IDEALE-EU API provides programmatic access to:
- **Digital passport** CRUD operations
- **QS anchoring** APIs
- **Search and query** endpoints
- **Webhook** integrations
- **GraphQL** interface

---

## Authentication

### API Key Authentication
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.ideale-eu.aero/v1/passports
```

### OAuth 2.0 Flow
Coming soon: Support for OAuth 2.0 authentication for third-party applications.

---

## Quick Start

### Python SDK
```python
from ideale_eu import Client, DigitalPassport

# Initialize client
client = Client(api_key="your_api_key")

# Create digital passport
passport = DigitalPassport.create(
    part_number="AAA-12345",
    domain="AAA",
    material="AL-7075-T6"
)

# QS anchor
passport.qs_anchor(description="Initial design release")

# Retrieve passport
retrieved = DigitalPassport.get("PP-AAA-2025-001234")
print(f"Status: {retrieved.status}")
```

### JavaScript SDK
```javascript
import { IdealEUClient, DigitalPassport } from '@ideale-eu/sdk';

// Initialize client
const client = new IdealEUClient({ apiKey: 'your_api_key' });

// Create digital passport
const passport = await DigitalPassport.create({
  partNumber: 'AAA-12345',
  domain: 'AAA',
  material: 'AL-7075-T6'
});

// QS anchor
await passport.qsAnchor('Initial design release');

// Retrieve passport
const retrieved = await DigitalPassport.get('PP-AAA-2025-001234');
console.log(`Status: ${retrieved.status}`);
```

### Java SDK
```java
import eu.ideale.sdk.IdealEUClient;
import eu.ideale.sdk.DigitalPassport;

// Initialize client
IdealEUClient client = new IdealEUClient("your_api_key");

// Create digital passport
DigitalPassport passport = DigitalPassport.create()
    .partNumber("AAA-12345")
    .domain("AAA")
    .material("AL-7075-T6")
    .build();

// QS anchor
passport.qsAnchor("Initial design release");

// Retrieve passport
DigitalPassport retrieved = DigitalPassport.get("PP-AAA-2025-001234");
System.out.println("Status: " + retrieved.getStatus());
```

### C++ SDK
```cpp
#include <ideale_eu/client.hpp>
#include <ideale_eu/digital_passport.hpp>

using namespace ideale_eu;

int main() {
    // Initialize client
    Client client("your_api_key");
    
    // Create digital passport
    auto passport = DigitalPassport::create(
        "AAA-12345",  // part_number
        "AAA",        // domain
        "AL-7075-T6"  // material
    );
    
    // QS anchor
    passport.qs_anchor("Initial design release");
    
    // Retrieve passport
    auto retrieved = DigitalPassport::get("PP-AAA-2025-001234");
    std::cout << "Status: " << retrieved.status() << std::endl;
    
    return 0;
}
```

---

## Core API Endpoints

### Digital Passports

#### Create Passport
```http
POST /api/v1/passports
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY

{
  "part_number": "AAA-12345",
  "domain": "AAA",
  "description": "Wing leading edge assembly",
  "material": "AL-7075-T6",
  "owner": "engineering@company.com"
}
```

**Response**:
```json
{
  "passport_id": "PP-AAA-2025-001234",
  "part_number": "AAA-12345",
  "domain": "AAA",
  "status": "active",
  "created_at": "2025-01-15T14:30:00Z",
  "url": "https://portal.ideale-eu.aero/passports/PP-AAA-2025-001234"
}
```

#### Get Passport
```http
GET /api/v1/passports/{passport_id}
Authorization: Bearer YOUR_API_KEY
```

#### Update Passport
```http
PATCH /api/v1/passports/{passport_id}
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY

{
  "description": "Updated description",
  "status": "approved"
}
```

#### List Passports
```http
GET /api/v1/passports?domain=AAA&status=active&page=1&per_page=50
Authorization: Bearer YOUR_API_KEY
```

---

### QS Anchoring

#### Create QS State
```http
POST /api/v1/qs/create
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY

{
  "passport_id": "PP-AAA-2025-001234",
  "parameters": {
    "thickness": {"min": 2.0, "max": 5.0},
    "material": ["AL-7075-T6", "AL-2024-T3"]
  },
  "n_candidates": 100
}
```

#### Anchor QS State
```http
POST /api/v1/qs/freeze
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY

{
  "qs_state_id": "QS-2025-001234",
  "description": "Initial design release",
  "evidence": [
    "ipfs://Qm...",
    "ipfs://Qm..."
  ]
}
```

**Response**:
```json
{
  "manifest_id": "UTCS-2025-001234",
  "merkle_root": "0x1234567890abcdef...",
  "timestamp": "2025-01-15T14:30:00Z",
  "blockchain_tx": "0xabcdef1234567890..."
}
```

#### Verify Anchor
```http
GET /api/v1/qs/verify/{manifest_id}?evidence={evidence_uri}
Authorization: Bearer YOUR_API_KEY
```

---

### Search and Query

#### Search Passports
```http
GET /api/v1/search?q=wing+assembly&domain=AAA&type=passport
Authorization: Bearer YOUR_API_KEY
```

#### Advanced Query
```http
POST /api/v1/query
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY

{
  "filters": {
    "domain": ["AAA", "PPP"],
    "material": "AL-7075-T6",
    "created_after": "2025-01-01",
    "status": "active"
  },
  "sort": "created_at",
  "order": "desc",
  "page": 1,
  "per_page": 50
}
```

---

### Webhooks

#### Register Webhook
```http
POST /api/v1/webhooks
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY

{
  "url": "https://yourapp.com/webhook",
  "events": ["passport.created", "passport.updated", "qs.anchored"],
  "secret": "your_webhook_secret"
}
```

#### Webhook Events
- `passport.created`: New passport created
- `passport.updated`: Passport metadata updated
- `passport.approved`: Passport approved
- `qs.anchored`: QS state anchored
- `evidence.uploaded`: Evidence artifact uploaded

---

## GraphQL Interface

### Endpoint
```
https://api.ideale-eu.aero/graphql
```

### Example Query
```graphql
query GetPassport($id: ID!) {
  passport(id: $id) {
    id
    partNumber
    domain
    status
    material
    owner
    createdAt
    qsAnchors {
      manifestId
      merkleRoot
      timestamp
      description
    }
    evidence {
      type
      uri
      uploadedAt
    }
  }
}
```

### Example Mutation
```graphql
mutation CreatePassport($input: PassportInput!) {
  createPassport(input: $input) {
    id
    partNumber
    status
    url
  }
}
```

---

## Rate Limits

- **Free tier**: 100 requests/hour
- **Professional**: 1,000 requests/hour
- **Enterprise**: Custom limits

Rate limit headers:
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1642694400
```

---

## Error Handling

### HTTP Status Codes
- `200 OK`: Success
- `201 Created`: Resource created
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Missing or invalid API key
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

### Error Response Format
```json
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "Part number is required",
    "details": {
      "field": "part_number",
      "constraint": "required"
    }
  }
}
```

---

## SDK Installation

### Python
```bash
pip install ideale-eu-sdk
```

### JavaScript/TypeScript
```bash
npm install @ideale-eu/sdk
```

### Java
```xml
<dependency>
  <groupId>eu.ideale</groupId>
  <artifactId>ideale-eu-sdk</artifactId>
  <version>1.0.0</version>
</dependency>
```

### C++
```bash
# CMake
find_package(IdealEU REQUIRED)
target_link_libraries(your_app IdealEU::sdk)
```

---

## Support

For API support:
- **Email**: api-support@ideale-eu.aero
- **Documentation**: This page
- **Community**: [community.ideale-eu.aero](https://community.ideale-eu.aero)
- **Status**: [status.ideale-eu.aero](https://status.ideale-eu.aero)

---

## Coming Soon

- Complete endpoint reference
- Authentication flows (OAuth 2.0, JWT)
- Batch operations
- File upload API
- Real-time subscriptions
- API versioning strategy
- Changelog and migration guides

---

## Related Documentation

- [Quick Start Guide](/docs/quick-start/) - Getting started with the platform
- [QS Technical Specification](/docs/technical/qs-specification/) - QS anchoring details
- [Glossary](/docs/glossary/) - API terminology

---

*For the latest updates, subscribe to our [API changelog](https://api.ideale-eu.aero/changelog)*
