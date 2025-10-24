# 01-GEOMETRY_DEFINITIONS

**Purpose**  
Master geometry files and coordinate-frame definitions used by design, PLM, CAE and manufacturing. This folder contains canonical CAD exports, neutral STEP AP242 packages with PMI, reference datum and stationing definitions, and metadata linking geometry to EBOM/PLM.

---

## Required contents
- `reference_datum.md` — authoritative coordinate system, datum, stationing, BL/WL conventions and examples.  
- `native/` — native CAD files organized by part/assembly. Each entry must include `metadata.yaml` adjacent to the native file. Use Git LFS for large binaries.  
- `step_ap242/` — STEP AP242 exports with PMI for each released item (one STEP per part/assembly). Include `export_recipe.txt` describing CAD system and exact STEP settings.  
- `neutral/` — other neutral exports as required (Parasolid, IGES).  
- `previews/` — PNG/JPEG thumbnails (512×512) and exploded-view images.  
- `meshes/` (optional) — canonical analytic meshes used by CAE teams, with mesh quality report.  
- `TEMPLATE_METADATA.yaml` — canonical metadata template to copy for each file.  
- `META.json` — folder-level metadata (owner, contact, baseline id).

## File naming conventions
Use the project-wide pattern:
```
{PART_ID}-{DESCRIPTION}_R{REV:03d}.{ext}
```
Example:
```
24-06-001-Fuselage_ReferenceDatum_R001.step
```

## Geometry export rules
- **STEP AP242 with PMI** is mandatory for released geometry. Ensure PMI contains datum references and GD&T for datum features used in manufacturing.  
- Include mass properties and bounding box in native files and in `metadata.yaml`.  
- Each exported neutral file must reference the `reference_datum` and `ebom_id` in its metadata.

## Metadata & PLM linkage
- Every native and STEP file must have a `metadata.yaml` adjacent that follows `TEMPLATE_METADATA.yaml` fields.  
- `ebom_id`, `part_id`, `revision` and `cad_system/version` are mandatory. PLM ingestion scripts rely on these fields.

## Change control
- Geometry changes must follow CMP process. Update `REVISION_HISTORY` and create ECN records in `../06-REVISIONS/` when publishing new baselines.

## QA
- Each geometry release requires:
  - STEP AP242 export with PMI verified.
  - One thumbnail (512×512).
  - `metadata.yaml` present and validated by `SCRIPTS/check_metadata.py`.
  - EBOM mapping verified.

## Notes
- Units: **mm** for linear dimensions (see `reference_datum.md` for full unit policy).  
- Coordinate system must match `reference_datum.md`. Conversion scripts must be provided if external tools use a different convention.
