# EDI Mappings

Electronic Data Interchange transaction set mappings.

## Overview

EDI standardizes electronic business documents between trading partners.

## Common EDI Transaction Sets

### X12 Standards (North America)

**Purchasing:**
- 850: Purchase Order
- 855: Purchase Order Acknowledgment
- 860: Purchase Order Change Request
- 865: Purchase Order Change Acknowledgment

**Shipping and Receiving:**
- 856: Advanced Shipping Notice (ASN)
- 810: Invoice
- 820: Payment Order/Remittance Advice
- 997: Functional Acknowledgment

**Forecasting and Planning:**
- 830: Planning Schedule with Release Capability
- 862: Shipping Schedule
- 866: Production Sequence

**Quality:**
- 836: Procurement Notices (for quality issues/SCARs)

### EDIFACT Standards (International)

- ORDERS: Purchase Order
- ORDRSP: Order Response
- DESADV: Despatch Advice (ASN)
- INVOIC: Invoice
- REMADV: Remittance Advice

## Implementation

### Trading Partner Agreements
- Data format and version
- Communication protocols (AS2, SFTP, VAN)
- Transaction sets supported
- Frequency and timing
- Error handling and acknowledgments
- Contact points for issues

### Data Mapping
- Map internal data fields to EDI segments and elements
- Transformation rules
- Data validation
- Code list management (qualifiers, codes)
- Default values and constants

### Testing
- Unit testing (individual transactions)
- Integration testing (end-to-end)
- Partner testing (with live partner connection)
- Certification (if required by partner or VAN)

### Monitoring
- Transaction volume and success rates
- Error rates and types
- Performance (transmission time, processing time)
- Compliance with partner SLAs
- Issue tracking and resolution

## Benefits of EDI

- Reduced manual data entry and errors
- Faster processing and order cycle times
- Improved data accuracy
- Lower administrative costs
- Better visibility and tracking
- Environmental benefits (paperless)
