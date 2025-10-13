# JSON — JavaScript Object Notation BOMs

## Purpose

This directory contains BOMs in JSON (JavaScript Object Notation) format, optimized for modern web applications, APIs, and digital tools.

## Format Characteristics

### Advantages
- **Lightweight**: Compact and efficient
- **Modern**: Native to web technologies
- **Flexible**: Dynamic structure support
- **Web-friendly**: Direct JavaScript integration
- **API-ready**: RESTful API compatible

### Use Cases
- Web-based BOM viewers
- REST API data exchange
- Digital manufacturing tools
- Real-time dashboards
- Mobile applications

## JSON Structure

### Standard BOM JSON Format
```json
{
  "bom": {
    "header": {
      "partNumber": "53-10-CENTER-BODY",
      "description": "Center Body Assembly",
      "revision": "002",
      "status": "RELEASED",
      "date": "2024-03-15",
      "bomType": "EBOM"
    },
    "items": [
      {
        "partNumber": "53-10-001",
        "description": "Center Frame Assembly",
        "quantity": 1,
        "uom": "EA",
        "material": "AL7075-T6",
        "mass": {
          "value": 125.5,
          "unit": "kg"
        },
        "source": "MAKE",
        "findNumber": 1,
        "reference": "DWG-53-10-001"
      },
      {
        "partNumber": "53-10-002",
        "description": "Bulkhead Forward",
        "quantity": 2,
        "uom": "EA",
        "material": "AL2024-T3",
        "mass": {
          "value": 45.2,
          "unit": "kg"
        },
        "source": "MAKE",
        "findNumber": 2,
        "reference": "DWG-53-10-002"
      }
    ],
    "summary": {
      "totalItems": 45,
      "totalMass": {
        "value": 850.5,
        "unit": "kg"
      },
      "makeItems": 23,
      "buyItems": 22
    }
  }
}
```

## File Naming Convention

```
53-10_BOM_<assembly-id>_<bom-type>_<revision>.json
```

Examples:
- `53-10_BOM_CENTER-BODY_EBOM_r002.json`
- `53-10_BOM_FRAME-F05_MBOM_r003.json`

## Best Practices

### Formatting
- Use proper indentation (2 or 4 spaces)
- Consistent property naming (camelCase)
- UTF-8 encoding
- Pretty-print for readability

### Structure
- Keep hierarchy logical
- Use objects for complex data
- Arrays for lists of items
- Include metadata

### Data Types
- Numbers without quotes
- Booleans as true/false
- Null for missing values
- Strings in quotes

## Validation

### JSON Schema
Define and validate against JSON schema:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "bom": {
      "type": "object",
      "required": ["header", "items"],
      "properties": {
        "header": {...},
        "items": {...}
      }
    }
  }
}
```

## API Integration

### RESTful API Endpoints
```
GET /api/bom/53-10-CENTER-BODY/r002
POST /api/bom/validate
PUT /api/bom/53-10-CENTER-BODY/r002
```

### Response Format
```json
{
  "status": "success",
  "data": { /* BOM data */ },
  "metadata": {
    "timestamp": "2024-03-15T10:30:00Z",
    "version": "1.0"
  }
}
```

## Processing

### JavaScript Example
```javascript
fetch('53-10_BOM_CENTER-BODY_EBOM_r002.json')
  .then(response => response.json())
  .then(data => {
    const bom = data.bom;
    console.log(`Total items: ${bom.summary.totalItems}`);
    bom.items.forEach(item => {
      console.log(`${item.partNumber}: ${item.description}`);
    });
  });
```

### Python Example
```python
import json

with open('53-10_BOM_CENTER-BODY_EBOM_r002.json', 'r') as f:
    data = json.load(f)
    bom = data['bom']
    for item in bom['items']:
        print(f"{item['partNumber']}: {item['quantity']} {item['uom']}")
```

## Web Integration

JSON BOMs are ideal for:
- Single-page applications (SPA)
- Progressive web apps (PWA)
- Real-time data visualization
- Interactive BOM viewers
- Mobile-responsive tools

## Related Directories

- **XML**: [../XML/](../XML/) — XML format BOMs
- **CSV**: [../CSV/](../CSV/) — CSV format BOMs
- **Templates**: [../../TEMPLATES/](../../TEMPLATES/) — JSON BOM templates
