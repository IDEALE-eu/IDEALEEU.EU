# SUPPLIERS — Supplier BOM Packages and Acknowledgments

## Purpose

This directory manages supplier-related BOM documentation, including supplier-specific BOM packages and receipt acknowledgments.

## Directory Structure

```
SUPPLIERS/
├── PACKAGES/  — Supplier BOM packages and specifications
└── ACK/       — Supplier acknowledgments and confirmations
```

## Contents

### Supplier Documentation
- Supplier-specific BOMs
- Material specifications
- Packaging requirements
- Delivery schedules
- Quality requirements

### Communication Records
- Purchase order BOMs
- Supplier acknowledgments
- Clarification requests
- Technical responses

## Supplier BOM Packages

Supplier packages should include:
- Complete part BOM
- Technical specifications
- Quality requirements
- Inspection criteria
- Delivery schedules
- Packaging instructions

## File Naming Convention

```
53-10_SUPPLIER_<supplier-name>_<part-id>_<date>.<ext>
```

Examples:
- `53-10_SUPPLIER_ACME-MFG_BULKHEAD_20240315.pdf`
- `53-10_SUPPLIER_FASTENERS-INC_HW-PKG-001_20240320.xlsx`

## Supplier Management

### Package Distribution
1. Extract relevant BOM subset
2. Add supplier-specific requirements
3. Include quality specifications
4. Send to supplier for quotation
5. Track in PACKAGES/ directory

### Acknowledgment Tracking
1. Receive supplier acknowledgment
2. Store in ACK/ directory
3. Verify against original package
4. Resolve any discrepancies
5. Update procurement records

## Quality Requirements

Supplier BOMs must specify:
- Material certifications
- Inspection requirements
- Acceptance criteria
- Test reports needed
- Traceability requirements

## Procurement Integration

### Purchase Orders
- Link BOM to purchase order
- Include part specifications
- Reference quality standards
- Specify delivery terms

### Receipt Verification
- Match received items to BOM
- Verify quantities and specifications
- Confirm material certifications
- Document acceptance

## Supplier Communication

### Initial Package
- Technical specifications
- Quality requirements
- Delivery schedule
- Commercial terms

### Acknowledgment Review
- Verify understanding
- Confirm capabilities
- Resolve questions
- Clarify requirements

## Related Directories

- **Parts**: [../PARTS/](../PARTS/) — Individual part BOMs
- **Installation**: [../INSTALLATION/](../INSTALLATION/) — Installation hardware
- **Templates**: [../TEMPLATES/](../TEMPLATES/) — Supplier package templates
