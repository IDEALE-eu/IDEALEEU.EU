# API Bindings

**Document Number:** QMS-DT-002
**Revision:** 1.0
**Date:** 2025-01-01

## Purpose

Define API specifications for QMS integration with PLM/PDM and digital thread systems.

## API Architecture

### RESTful APIs
- JSON format for data exchange
- OAuth 2.0 authentication
- HTTPS encryption
- Rate limiting and throttling

### API Endpoints

#### Document Management
- `GET /api/documents/{doc_id}` - Retrieve document metadata
- `GET /api/documents/{doc_id}/content` - Retrieve document content
- `GET /api/documents?status=active` - List active documents
- `POST /api/documents/{doc_id}/revisions` - Create new revision

#### Change Management
- `GET /api/changes/{eco_id}` - Retrieve change order
- `GET /api/changes?status=open` - List open change orders
- `POST /api/changes` - Create new change order
- `PUT /api/changes/{eco_id}/approve` - Approve change order

#### Non-Conformance
- `GET /api/ncrs/{ncr_id}` - Retrieve NCR
- `GET /api/ncrs?status=open` - List open NCRs
- `POST /api/ncrs` - Create new NCR
- `PUT /api/ncrs/{ncr_id}/disposition` - Update MRB disposition

#### CAPA
- `GET /api/capas/{capa_id}` - Retrieve CAPA
- `GET /api/capas?priority=high` - List high priority CAPAs
- `POST /api/capas` - Create new CAPA
- `PUT /api/capas/{capa_id}/verify` - Record verification

#### Calibration
- `GET /api/calibration/equipment/{equip_id}` - Equipment calibration status
- `GET /api/calibration/due?days=30` - List equipment due for calibration
- `POST /api/calibration/certificates` - Upload calibration certificate

#### Traceability
- `GET /api/traceability/serial/{serial_no}` - Product history and records
- `GET /api/traceability/requirements/{req_id}` - Requirements trace
- `GET /api/traceability/bom/{part_no}` - BOM and configuration

#### Training
- `GET /api/training/personnel/{emp_id}` - Training records
- `GET /api/training/certifications?expiring=30` - Expiring certifications
- `POST /api/training/records` - Add training record

## Data Models

### Document
```json
{
  "doc_id": "PRO-001",
  "title": "Document and Data Control",
  "type": "Procedure",
  "revision": "1.0",
  "status": "Active",
  "owner": "Quality Manager",
  "issue_date": "2025-01-01",
  "review_due": "2026-01-01"
}
```

### NCR
```json
{
  "ncr_id": "NCR-2025-001",
  "date": "2025-01-15",
  "part_no": "AC-WING-001",
  "serial_no": "S/N 00045",
  "description": "Dimension out of tolerance",
  "severity": "Minor",
  "status": "Open",
  "disposition": null
}
```

## Security

- API key authentication for service accounts
- OAuth 2.0 for user-based access
- Role-based access control (RBAC)
- Audit logging of all API calls

## Integration Points

### PLM/PDM Systems
- Windchill, Teamcenter, ENOVIA, etc.
- CAD file management
- BOM management
- Change orders

### ERP/MES Systems
- SAP, Oracle, etc.
- Work orders
- Inventory
- Production tracking

### QMS Software
- Dedicated QMS platforms
- Document management
- NCR/CAPA tracking
- Audit management

## Implementation

API implementation planned for Q2 2025. Initial focus on document management and change management integration.

## Related Documents

- TRACEABILITY_RULES.md
- PRO-001_DOC_CONTROL
- Section 00-PROGRAM/DIGITAL_THREAD/
