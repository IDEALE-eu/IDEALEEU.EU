# XML — Extensible Markup Language BOMs

## Purpose

This directory contains BOMs in XML (Extensible Markup Language) format, designed for PLM system integration, data exchange, and structured validation.

## Format Characteristics

### Advantages
- **Structured**: Hierarchical and well-defined
- **Validated**: Schema-based validation
- **Standard**: Industry-standard format
- **Extensible**: Support for custom data
- **System integration**: PLM/ERP compatible

### Use Cases
- PLM system import/export
- System-to-system integration
- Automated data validation
- Industry standard compliance
- Long-term archival

## XML Schema

### Standard BOM XML Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<BillOfMaterials xmlns="http://ideale.eu/schema/bom/v1">
  <Header>
    <PartNumber>53-10-CENTER-BODY</PartNumber>
    <Description>Center Body Assembly</Description>
    <Revision>002</Revision>
    <Status>RELEASED</Status>
    <Date>2024-03-15</Date>
  </Header>
  <Items>
    <Item>
      <PartNumber>53-10-001</PartNumber>
      <Description>Center Frame Assembly</Description>
      <Quantity>1</Quantity>
      <UOM>EA</UOM>
      <Material>AL7075-T6</Material>
      <Mass unit="kg">125.5</Mass>
      <Source>MAKE</Source>
      <FindNumber>1</FindNumber>
    </Item>
    <!-- Additional items -->
  </Items>
  <Summary>
    <TotalItems>45</TotalItems>
    <TotalMass unit="kg">850.5</TotalMass>
  </Summary>
</BillOfMaterials>
```

## File Naming Convention

```
53-10_BOM_<assembly-id>_<bom-type>_<revision>.xml
```

Examples:
- `53-10_BOM_CENTER-BODY_EBOM_r002.xml`
- `53-10_BOM_FRAME-F05_MBOM_r003.xml`

## Validation

### Schema Validation
- Validate against XSD schema
- Check required elements
- Verify data types
- Enforce constraints

### Schema Location
Reference BOM schema:
```xml
<BillOfMaterials 
  xmlns="http://ideale.eu/schema/bom/v1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://ideale.eu/schema/bom/v1 bom-schema.xsd">
```

## PLM Integration

### Import/Export
- Compatible with major PLM systems
- Standard data exchange format
- Automated import workflows
- Batch processing support

### PLM Systems
- Siemens Teamcenter
- PTC Windchill
- Dassault ENOVIA
- SAP PLM
- Aras Innovator

## Processing

### Parsing XML BOMs
```python
import xml.etree.ElementTree as ET

tree = ET.parse('53-10_BOM_CENTER-BODY_EBOM_r002.xml')
root = tree.getroot()

for item in root.findall('.//Item'):
    part_number = item.find('PartNumber').text
    quantity = int(item.find('Quantity').text)
    # Process BOM data
```

## Standards Compliance

XML BOMs should comply with:
- **ISO 10303 (STEP)**: Product data representation
- **PLCS**: Product Life Cycle Support
- **S1000D**: XML schema for technical publications

## Best Practices

### Structure
- Use clear element names
- Maintain consistent hierarchy
- Include namespaces
- Document custom extensions

### Data
- UTF-8 encoding
- Well-formed XML
- Schema-validated
- Include metadata

## Related Directories

- **JSON**: [../JSON/](../JSON/) — JSON format BOMs
- **CSV**: [../CSV/](../CSV/) — CSV format BOMs
- **Templates**: [../../TEMPLATES/](../../TEMPLATES/) — XML BOM templates
