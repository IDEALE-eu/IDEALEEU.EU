# LIBRARY — Standard Parts and Reusable Components

## Purpose

This directory contains libraries of standard parts, hardware, and reusable components that are used across the 53-10 Center Body design. These standardized elements ensure consistency, reduce design time, and support maintainability.

## Organization

Library content is organized by component type:

- **STANDARD_PARTS/** — Standard mechanical components and hardware
- **FASTENERS/** — Bolts, screws, rivets, and fastening hardware

## Naming Convention

Use the following pattern for library items:
```
LIB_<CATEGORY>_<STANDARD>_<DESCRIPTION>_<SIZE>.<ext>
```

Examples:
- `LIB_FASTENER_NAS1234_HEX-BOLT_0.25IN.CATPart`
- `LIB_STANDARD_MS24694_WASHER_10MM.prt`
- `LIB_FASTENER_BACR15CE_RIVET_5-32.sldprt`

## STANDARD_PARTS Directory

Contains standard mechanical components:
- Washers, nuts, and spacers
- Bushings and inserts
- Grommets and seals
- Clips and clamps
- Standard brackets
- Wire rope terminals
- Turnbuckles

Organization:
- Group by standard (NAS, MS, AN, AS, etc.)
- Include specification documents
- Provide material and finish variants

## FASTENERS Directory

Contains fastening hardware:
- Bolts and screws (hex, socket, pan head, etc.)
- Rivets (solid, blind, Hi-Lok, etc.)
- Nuts (hex, self-locking, plate, etc.)
- Pins (clevis, cotter, taper, etc.)
- Special fasteners (Jo-Bolts, Monobolt, etc.)

Organization:
- Group by fastener type
- Organize by size within type
- Include grip length variants for bolts
- Provide material/finish callouts

## Metadata

Each library item should include:
- Part number and specification
- Material and finish
- Weight per piece
- Supplier information
- Certification requirements
- Usage notes and restrictions

## Usage Guidelines

When using library parts:
- Always use library parts when available
- Do not modify library parts (create variants if needed)
- Reference parts, don't copy them
- Report missing standard parts for addition to library
- Follow proper fastener selection per design rules

## Library Management

Library maintenance:
- Parts are controlled and version-managed
- Only authorized personnel can add/modify
- Updates must be communicated to users
- Obsolete parts moved to archive
- Regular audits for completeness

## File Formats

Library parts stored as:
- Native CAD format (primary)
- Neutral formats (STEP, IGES) for exchange
- Lightweight representations for assemblies
- Symbol/block definitions where applicable

## Related Documentation

- **Design rules**: [`../CONFIG/DESIGN_RULES/`](../CONFIG/DESIGN_RULES/)
- **Standards**: [`../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/`](../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/)
- **Part specifications**: [`../METADATA/`](../METADATA/)
- **Templates**: [`../TEMPLATES/`](../TEMPLATES/)

## Quality Requirements

Library parts must:
- [ ] Conform to published standards
- [ ] Include complete metadata
- [ ] Be validated for accuracy
- [ ] Have lightweight representations
- [ ] Be properly categorized and named
