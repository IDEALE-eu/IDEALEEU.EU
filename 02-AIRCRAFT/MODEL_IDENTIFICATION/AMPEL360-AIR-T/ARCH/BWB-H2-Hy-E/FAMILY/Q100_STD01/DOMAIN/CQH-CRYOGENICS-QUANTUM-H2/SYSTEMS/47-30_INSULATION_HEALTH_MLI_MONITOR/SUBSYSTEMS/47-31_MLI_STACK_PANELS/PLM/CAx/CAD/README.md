# CAD

**Purpose**  
Repository of CAD deliverables for this subsystem. Holds assemblies, parts, neutral exports, manufacturing drawings, models and templates required for PLM/CAx traceability and release.

## Top-level layout
- `ASSEMBLIES/`  
  Complete assembly models and subassembly folders. Each assembly must include a native assembly file, exploded view, and a `metadata.yaml`.  
- `PARTS/`  
  Individual part files and single-part assemblies. Include native part, 2D drawing (if applicable), and `metadata.yaml`.  
- `MODELS/`  
  Supporting models used for simulation, kinematic assemblies, fixtures, and reference geometry. Document model purpose in an accompanying README per model.  
- `DRAWINGS/`  
  Released 2D drawings in PDF and native CAD-drawing formats. Drawings must carry GD&T per ASME Y14.5 and reference the associated part/assembly.  
- `EXPORTS/`  
  Neutral exchange files intended for downstream consumers: `STEP AP242` (with PMI), `Parasolid`, `IGES`. Put one export per part/assembly and include an `export_recipe.txt` describing software and export settings.  
- `TEMPLATES/`  
  Metadata, titleblock, release checklist and template files:  
  - `TEMPLATE_METADATA.yaml` (required fields below)  
  - `TEMPLATE_TITLEBLOCK.<slddrw|drw|pdf>`  
  - `RELEASE_CHECKLIST.md`  
- `README.md`  
  This file.

## Required metadata (`metadata.yaml` / `.json`)
Every part/assembly must include a metadata file adjacent to the CAD file containing:
```yaml
part_id: string
description: string
revision: string   # R001
author: string
cad_system: string # e.g., SolidWorks 2023
mass_kg: number
material: string
ebom_id: string
approval_status: string
last_updated: YYYY-MM-DD
```

## Naming convention

`{PART_ID}-{DESCRIPTION}_R{REV:03d}.{ext}`
Example: `24-80-001-Battery_Assembly_R001.step`

## File format rules

* Native CAD: keep editable native files. Include mass properties.
* STEP AP242: mandatory for released items. Must include PMI for tolerances and annotations.
* PDF: release copies of drawings.
* STL: only for prototyping, with resolution stated in `metadata.yaml`.
* Use Git LFS for native and large binaries.

## Release checklist (minimum)

* Native CAD saved and checked in.
* STEP AP242 export with PMI.
* 2D PDF drawing with GD&T (if applicable).
* `metadata.yaml` present and complete.
* Thumbnail: `thumbnail_512x512.png` next to assembly.
* EBOM mapping updated (`EBOM_MAPPING.csv` in parent PLM/CAx folder).
* Approvals recorded in metadata.

## Export recipes

Include `EXPORTS/export_recipe.txt` describing:

* CAD system and version used.
* Exact export steps and settings (STEP AP242 options).
* Any post-processing used (heal, repair).

## Sizes and limits

* Native CAD files: prefer < 100 MB. If larger, store in PLM or LFS.
* STEP files: prefer < 50 MB.

## Quality & standards

* ASME Y14.5 for GD&T.
* STEP AP242 / ISO 10303-242 for neutral exchange.
* AS9100 traceability and release control for aerospace deliverables.

## Traceability & EBOM

* Ensure `ebom_id` in every `metadata.yaml`.
* Maintain `EBOM_MAPPING.csv` at `PLM/CAx/` level with fields `part_id,plm_id,revision,comment`.

## Ownership & contacts

* CAD Owner: *Name* — *email*
* PLM Owner: *Name* — *email*
* CAE Owner (for models): *Name* — *email*

## Notes

* Document any deviation from these rules in `TEMPLATES/DEVIATIONS.md` and obtain approver sign-off.
* Update this `README.md` whenever conventions change.

*Last updated: 2025-10-23*

