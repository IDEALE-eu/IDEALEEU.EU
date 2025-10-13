# 53-10 · Bulkhead Modules — CAD assemblies

**Scope:** master and sub-assemblies for fuselage bulkheads in the center body.  
**Datums:** FS/BL/WL per [06-DIMENSIONS-STATIONS](../../../../../../../../../SYSTEMS/06-DIMENSIONS-STATIONS/).  
**Authority:** this folder is the SSOT for CAD geometry of bulkhead modules.

## Contents
- `BH-STAxxx_*` folders: one per station.  
- `SHARED/`: coordinates, libraries, neutral exports.  
- `TEMPLATES/`: starter files for new modules.  
- `index.csv`: registry with station, variant, status, REL tag.

## Model rules
- File prefix: `53-10-BH-STA<fs>`; suffix `_MASTER_ASM.asm`, `_SKEL.prt`, `_ENV.prt`.  
- Skeleton owns CSYS, planes, primary curves. No direct features on master asm.  
- Interfaces live under `IFC/` and are exported to `SHARED/IFC_EXPORTS`.

## Links
- Structure allowables: [`.../SYSTEMS/51-STRUCTURES-GENERAL/SUBSYSTEMS/51-10_MATERIALS_ALLOWABLES/`](../../../../../../../../../SYSTEMS/51-STRUCTURES-GENERAL/SUBSYSTEMS/51-10_MATERIALS_ALLOWABLES/)
- Doors/cutouts (if any): [`.../SYSTEMS/52-DOORS/`](../../../../../../../../../SYSTEMS/52-DOORS/)
