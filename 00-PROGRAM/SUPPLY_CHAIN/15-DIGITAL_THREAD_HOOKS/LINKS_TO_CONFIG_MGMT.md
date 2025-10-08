# Links to Configuration Management

## Overview

Integration between supply chain and configuration management systems.

## Key Integration Points

### Part Master Data
**From CONFIG_MGMT to SUPPLY_CHAIN:**
- Part number creation and updates
- Revision level changes
- Part status (active, obsolete, phase-out)
- Design specifications and drawings

**From SUPPLY_CHAIN to CONFIG_MGMT:**
- Supplier information (AVL)
- Lead times and availability
- Cost data for design decisions
- Alternate parts and sources

### Bill of Materials (BOM)
**Integration:**
- EBOM (Engineering BOM) from PLM/PDM
- MBOM (Manufacturing BOM) from ERP/MES
- Supplier BOM for purchased assemblies
- Costed BOM with supplier pricing

### Engineering Change Orders (ECOs)
**Workflow:**
1. ECO initiated in CONFIG_MGMT
2. Supplier impact assessment in SUPPLY_CHAIN
3. Supplier notification and quotes for changes
4. Lead time and cost impact analysis
5. ECO approval with supplier concurrence
6. Implementation coordination with suppliers

**Data Flow:**
- ECO details (part changes, effectivity)
- Supplier responses and quotes
- Implementation schedules
- Inventory and obsolescence impact

### Document Management
**Shared Documents:**
- Technical specifications
- Drawings and 3D models
- Material specifications
- Test procedures and reports
- Certifications and approvals

**Access Control:**
- Supplier portal access to authorized documents
- ITAR/Export control restrictions
- Version control and change tracking
- Audit trail of document access

## Traceability

### Serial Number Tracking
- Serialized parts from suppliers
- Lot/batch traceability
- Genealogy from raw material to final product
- Test history and certifications

### As-Built Configuration
- Actual configuration vs. design
- Supplier substitutions and deviations
- Quality dispositions
- Field changes and modifications

## Links to 00-PROGRAM/CONFIG_MGMT/

See also:
- **../CONFIG_MGMT/** for configuration management procedures
- **../CONFIG_MGMT/ECO_PROCESS.md** for engineering change procedures
- **../CONFIG_MGMT/PART_NUMBERING.md** for part number system
- **../CONFIG_MGMT/BOM_MANAGEMENT.md** for BOM control
