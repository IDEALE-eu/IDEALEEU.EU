# SUBSYSTEM: 48-10_CAMERA_MOUNTS_IF_TEMPLATES

**Under System:** 48-OPTICAL_VIDEO_PLATFORM • **Architecture:** AIR-T (ATA) • **Domain:** OOO-OS-ONTOLOGIES-OFFICE

## Purpose

Implements the sub-assembly with full PLM artifacts.

## Folder Contract

- `PLM/CAx/*` → design / reports / MOCs
- `PLM/EBOM_LINKS.md` → packaging / on & off-board bundles
- `META.json` + `inherit.json` → CAD/CAE/CAM only here

## Rules

- **Verification:** see `README.md` + template provenance
- **ICDs:** see traceability in `INTERFACE_MATRIX`
- **Sourcing:** see `PLM/EBOM_LINKS.md`

## How to Contribute

- Keep SW in its host LRU chapter
- EWIS lives in ATA-92; reference via interfaces *.
- Update `META.json` with owner & status
