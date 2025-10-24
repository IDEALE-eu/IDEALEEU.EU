# Reference Datum, Coordinate System and Stationing Conventions

This document is the authoritative reference for coordinate frames, stationing (FS/BL/WL), axis orientation, units and example conversions used across ATA-06 geometry products.

---

## Coordinate system (canonical)
- **Type:** Right-handed Cartesian aircraft coordinate system.  
- **Axes (positive directions):**
  - **X**: forward along fuselage centerline (positive toward nose → tail direction is positive aft).  
  - **Y**: lateral to the right side of aircraft when looking forward (positive to right).  
  - **Z**: vertical, **positive upward** (Z-up).  
- **Handedness:** X × Y = Z (right-hand rule). This matches project CAD convention: *Right-handed, Z-axis vertical*.

> Note: if any legacy tool uses Z-down, a transformation must be provided and recorded in metadata.

---

## Datum reference
- **Datum plane / origin:** fuselage station 0 (FS 0) defined at the aft face of the nose equipment bay bulkhead (or the project-specified datum point). The canonical origin coordinates are recorded in each released `metadata.yaml` (`datum_origin_mm`).  
- **Datum orientation:** X axis runs positive aft from datum; Y right; Z up.  
- **Datum features:** Primary datum must be a rigid structural surface. Datum feature identifiers (DFx) used for GD&T must be present in STEP PMI.

---

## Stationing & conventions
- **Fuselage Station (FS):** scalar measured along the X axis from datum.  
  - `FS (mm) = X_global_mm - X_datum_origin_mm`  
  - FS values increase aft. Typical published FS are in millimetres (or decimetres in legacy tables). Use mm for all CAD and PLM exchanges.
- **Buttock Line (BL):** lateral offset from centerline, positive to the right.  
  - `BL (mm) = Y_global_mm - Y_centerline_mm` (normally Y_centerline_mm == 0).
- **Waterline (WL):** vertical offset from reference plane, positive **upwards**.  
  - `WL (mm) = Z_global_mm - Z_datum_origin_mm`
- **Example:** A point with global coordinates (X=5000 mm, Y=200 mm, Z=1200 mm) and datum origin X_datum=0 yields FS=5000 mm, BL=200 mm, WL=1200 mm.

---

## Units and tolerancing
- **Units:** SI. Length = **millimetres (mm)**. Angles = degrees. Mass = kilograms (kg).  
- **Geometric tolerances:** record GD&T in STEP PMI per ASME Y14.5 or project standard. Manufacturing-critical features should include tolerance band in `metadata.yaml`.  
- **Coordinate precision:** release coordinates with **0.1 mm** nominal precision unless otherwise stated.

---

## File coordinate mapping
- Native CAD coordinate origin and STEP coordinate origin must be identical. If a translation/rotation is applied during export, record the transform in `metadata.yaml` under:
```yaml
export_transform:
  translation_mm: [tx, ty, tz]
  rotation_deg: [rx, ry, rz]   # applied in order roll(X), pitch(Y), yaw(Z)
```

---

## Stationing table format

Provide FS/BL/WL tables as CSV with columns:

```
point_id, X_mm, Y_mm, Z_mm, FS_mm, BL_mm, WL_mm, description
```

Example:

```
FS000, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "Datum origin: nose bulkhead aft face"
```

---

## Linkage to PLM and CAE

* Each geometry file must include `datum_reference` and `stationing_table` references in its `metadata.yaml`. CAE and PLM tools rely on these to align assemblies and run thermal/structural analyses.

---

## Conventions summary

* Right-handed, X forward (aft positive), Y right, Z up.
* FS increases aft, BL increases right, WL increases up.
* Units = mm. Precision 0.1 mm. STEP AP242 must carry PMI datum references and GD&T.
