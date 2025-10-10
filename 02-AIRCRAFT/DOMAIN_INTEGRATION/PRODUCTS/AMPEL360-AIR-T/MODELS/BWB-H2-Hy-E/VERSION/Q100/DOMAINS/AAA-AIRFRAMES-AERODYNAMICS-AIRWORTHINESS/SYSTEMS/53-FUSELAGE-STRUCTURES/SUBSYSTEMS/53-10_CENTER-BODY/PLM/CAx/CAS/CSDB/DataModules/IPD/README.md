# Illustrated Parts Data (DMC: I)

## Purpose

This directory contains **Illustrated Parts Data (IPD)** modules for the AMPEL360 AIR-T 53-10 Center Body subsystem. IPD DMs provide parts catalogs with illustrations, part numbers, nomenclature, and applicability information.

## InfoCode Range

**800-899**: Illustrated Parts Data
- **800A**: General illustrated parts catalog
- **801A**: Hardware parts catalog
- **802A**: Electronic parts catalog
- **803A**: Structural parts catalog
- **804A**: System parts catalog
- **810A**: Parts by assembly
- **820A**: Parts by function

## DMC Naming Pattern

```
DMC-AMP360-AAA-53-10-<XX>-00A-<InfoCode><Var>-I_en-US_<Issue>-<InWork>.xml
```

Where:
- `<XX>` = Disassembly code (00=general, 10-99=specific assemblies)
- `<InfoCode>` = 800-899 for IPD
- `<Var>` = A-Z variant (usually A)
- `<Issue>` = 001, 002, 003...
- `<InWork>` = 00 (released) or 01-99 (draft)

## Examples

### General Center Body IPD
```
DMC-AMP360-AAA-53-10-00-00A-800A-I_en-US_001-00.xml
```
- Complete parts catalog for Center Body subsystem
- Disassembly code 00: General (all components)
- InfoCode 800A: General illustrated parts data

### Forward Bulkhead IPD
```
DMC-AMP360-AAA-53-10-10-00A-800A-I_en-US_001-00.xml
```
- Parts catalog for forward bulkhead assembly
- Disassembly code 10: Forward bulkhead
- InfoCode 800A: Illustrated parts data

### Center Body Fasteners
```
DMC-AMP360-AAA-53-10-00-00A-801A-I_en-US_001-00.xml
```
- Hardware and fasteners for Center Body
- InfoCode 801A: Hardware parts catalog

## Content Structure

### Illustrated Parts Breakdown
Each IPD DM typically contains:

1. **Assembly Illustration**
   - Exploded view or assembly view
   - Item numbers (balloons/callouts)
   - Clear identification of parts

2. **Parts List Table**
   - Item number
   - Part number (manufacturer P/N)
   - Nomenclature (part name/description)
   - Quantity per assembly
   - Unit of measure
   - Cage code (manufacturer identifier)
   - Remarks/notes

3. **Applicability Information**
   - Serial number ranges
   - Configuration options
   - Modification status
   - Optional equipment

4. **Cross-References**
   - Supersession information
   - Interchangeable parts
   - Related assemblies

## Parts List Format

Standard IPD table columns:

| Item | Part Number | Nomenclature | Qty | UoM | Cage | Remarks |
|------|-------------|--------------|-----|-----|------|---------|
| 1    | AMP-5310-001 | Bulkhead, Forward | 1 | EA | 12345 | Primary structure |
| 2    | AMP-5310-002 | Doubler, Bulkhead | 4 | EA | 12345 | Upper corners |
| 3    | MS20470AD4-6 | Rivet, Solid | 240 | EA | 96906 | Standard hardware |

### Column Definitions

- **Item**: Reference number from illustration (balloon number)
- **Part Number**: Manufacturer part number or specification
- **Nomenclature**: Clear, concise part description
- **Qty**: Quantity required for assembly
- **UoM**: Unit of measure (EA=each, LB=pound, FT=foot, etc.)
- **Cage**: Commercial and Government Entity code (manufacturer ID)
- **Remarks**: Applicability, notes, supersession info

## Illustration Requirements

### ICN (Illustration Control Number) Format
```
ICN-53-10-EXPL-<SeqNum>-A.<format>
```

### Illustration Types
- **ISO**: Isometric 3D view
- **EXPL**: Exploded assembly view
- **SEC**: Cross-section view
- **ASSY**: Assembly view
- **DET**: Detail view

### Illustration Standards
- Clear item callouts (balloons)
- Sequential numbering
- High resolution (min 300 DPI)
- Vector format preferred (SVG)
- Proper scaling and dimensions

## Applicability

IPD modules must include applicability information:

### Serial Number Ranges
```xml
<serialNumberRange>
  <serialNumberStart>001</serialNumberStart>
  <serialNumberEnd>999</serialNumberEnd>
</serialNumberRange>
```

### Configuration Options
- Baseline configuration
- Customer options
- Modification kits
- Service bulletins

## Part Number Standards

### AMPEL360 Part Numbers
```
AMP-<SysCode><SubSys>-<SeqNum>
```
Example: `AMP-5310-001` (System 53, Subsystem 10, Part 001)

### Standard Parts
- MS (Military Standard)
- NAS (National Aerospace Standard)
- AN (Air Force-Navy)
- AS (Aerospace Standard)

### Commercial Parts
- Manufacturer part numbers
- CAGE code for traceability
- Specifications and standards

## Quality Checklist

- [ ] DMC follows naming convention
- [ ] Metadata complete and correct
- [ ] UTCS anchors included
- [ ] Illustrations clear and properly referenced
- [ ] Item callouts match table entries
- [ ] Part numbers accurate and current
- [ ] Nomenclature consistent
- [ ] Quantities verified
- [ ] CAGE codes correct
- [ ] Applicability clearly stated
- [ ] Cross-references validated
- [ ] Supersession info current
- [ ] BREX validation passed
- [ ] Engineering review completed
- [ ] Logistics review completed
- [ ] QA approval obtained

## Integration with CAD

IPD should be generated from:
- PLM system data (EBOM)
- CAD assembly structures
- Engineering change orders
- Configuration management records

### Data Sources
- **EBOM**: Engineering Bill of Materials
- **CAD**: 3D models and assemblies
- **PLM**: Product Lifecycle Management system
- **ERP**: Enterprise Resource Planning (procurement data)

## Maintenance Integration

IPD modules support:
- **Spare parts ordering** - Accurate part numbers
- **Inventory management** - Quantity and applicability
- **Maintenance planning** - Parts for scheduled tasks
- **Troubleshooting** - Component identification

## Validation

```bash
# Validate single IPD module
python ../../../VALIDATION/BREX/validate_brex.py DMC-*-I_*.xml

# Validate all IPD modules
python ../../../VALIDATION/BREX/validate_brex.py .
```

## Updates and Revisions

IPD modules must be updated when:
- New parts are added
- Parts are superseded or obsoleted
- Quantities change
- Configuration changes occur
- Engineering changes are released

### Revision Process
1. Engineering change notification
2. IPD update (increment inWork)
3. Illustration update (if needed)
4. Technical review
5. Logistics review
6. Quality approval
7. Release (set inWork=00)

## Related Resources

- **EBOM**: `../../../PLM/EBOM_LINKS.md`
- **CAD Models**: `../../../PLM/CAx/CAS/`
- **Style Guide**: `../../../GUIDES/StyleGuide.md`
- **Conventions**: `../../../GUIDES/Conventions.md`
- **BREX Rules**: `../../BREX/DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml`

## Logistics Support

IPD provides critical data for:
- Provisioning analysis
- Spares recommendations
- Maintenance planning
- Support equipment identification
- Technical order compliance
