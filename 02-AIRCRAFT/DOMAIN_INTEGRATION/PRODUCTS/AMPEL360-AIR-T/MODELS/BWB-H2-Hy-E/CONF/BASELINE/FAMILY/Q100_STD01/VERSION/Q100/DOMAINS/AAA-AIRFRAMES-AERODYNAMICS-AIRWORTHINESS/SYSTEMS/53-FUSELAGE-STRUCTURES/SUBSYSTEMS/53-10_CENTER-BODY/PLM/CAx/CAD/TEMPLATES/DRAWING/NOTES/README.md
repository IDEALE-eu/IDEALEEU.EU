# NOTES — Standard Notes Library

## Purpose

Reusable standard notes and callouts for common requirements on engineering drawings.

## Contents

Standard note libraries organized by category:
- **General notes**: Common to all drawings
- **Material notes**: Material specifications and requirements
- **Process notes**: Manufacturing process requirements
- **Quality notes**: Inspection and quality requirements
- **Surface finish notes**: Surface texture and finish callouts
- **Assembly notes**: Assembly instructions and requirements

## Standard Note Categories

### General Notes
```
1. INTERPRET DIMENSIONS AND TOLERANCES PER ASME Y14.5-2018
2. REMOVE ALL BURRS AND SHARP EDGES
3. BREAK SHARP CORNERS 0.5mm MAX UNLESS OTHERWISE SPECIFIED
4. ALL DIMENSIONS IN MILLIMETERS UNLESS OTHERWISE NOTED
5. THIRD ANGLE PROJECTION
6. DO NOT SCALE DRAWING
```

### Material Notes
```
1. MATERIAL: [MATERIAL SPECIFICATION]
2. MATERIAL CERTIFICATION REQUIRED
3. HEAT TREAT: [HEAT TREATMENT SPECIFICATION]
4. MATERIAL TRACEABILITY REQUIRED PER AS9100
5. SUBSTITUTE MATERIALS REQUIRE ENGINEERING APPROVAL
```

### Manufacturing Process Notes
```
1. DEBURR AND BREAK EDGES 0.1-0.3mm
2. CLEAN PER [CLEANING SPECIFICATION]
3. PRIME AND PAINT PER [COATING SPECIFICATION]
4. ANODIZE TYPE II CLASS 2 PER MIL-A-8625
5. PASSIVATE PER AMS 2700
6. PLATING: CADMIUM, TYPE II, CLASS 3 PER QQ-P-416
```

### Quality and Inspection Notes
```
1. 100% INSPECTION REQUIRED
2. FIRST ARTICLE INSPECTION REQUIRED PER AS9102
3. CRITICAL CHARACTERISTICS IDENTIFIED WITH ◆
4. DOCUMENT INSPECTION RESULTS
5. SUPPLIER TO PROVIDE COC WITH EACH SHIPMENT
6. IN-PROCESS INSPECTION REQUIRED AT OPERATIONS MARKED ★
```

### Surface Finish Notes
```
1. SURFACE FINISH: Ra 3.2 UNLESS OTHERWISE SPECIFIED
2. MACHINED SURFACES: Ra 1.6
3. GROUND SURFACES: Ra 0.8
4. POLISHED SURFACES: Ra 0.4
5. AS-FABRICATED SURFACES: Ra 6.3 MAX
```

### Assembly Notes
```
1. TORQUE FASTENERS PER [TORQUE SPECIFICATION]
2. APPLY SEALANT PER [SEALANT SPECIFICATION]
3. APPLY LUBRICANT TO THREADS PER [LUBE SPECIFICATION]
4. LOCK WIRE FASTENERS PER MS 21256
5. ASSEMBLY SEQUENCE: SEE ASSEMBLY PROCEDURE [DOC NUMBER]
6. INSTALL FASTENERS PER PATTERN SHOWN
```

### Structural Notes (53-10 Specific)
```
1. STRUCTURAL COMPONENT - NO SUBSTITUTIONS WITHOUT STRESS ANALYSIS
2. CRITICAL LOAD PATH COMPONENT
3. FASTENER PATTERN IS CRITICAL - DO NOT ALTER
4. MAINTAIN EDGE DISTANCE PER DESIGN REQUIREMENTS
5. INSPECT PER STRUCTURAL INSPECTION PLAN [DOC NUMBER]
```

## Naming Convention

```
NOTE_<category>_<description>.txt
```

Examples:
- `NOTE_General_Standard_Drawing_Notes.txt`
- `NOTE_Material_Aluminum_Certification.txt`
- `NOTE_Process_Anodize_Type_II.txt`
- `NOTE_Assembly_Torque_Requirements.txt`

## Usage Guidelines

### Adding Notes to Drawings
1. Select appropriate notes from library
2. Place notes in standard note area on drawing
3. Number notes sequentially (1, 2, 3, etc.)
4. Reference notes from features as needed (e.g., "SEE NOTE 3")
5. Customize notes only when standard notes don't apply

### Creating Custom Notes
1. Check if similar standard note exists first
2. Write clearly and concisely
3. Use approved terminology and abbreviations
4. Reference applicable standards
5. Submit for inclusion in standard library if reusable

### Note Placement
- **General notes**: Lower left or lower right of drawing
- **Local notes**: Near applicable feature with leader line
- **Table notes**: Below or adjacent to table
- **Continuation**: "NOTES CONTINUED ON SHEET X" if multiple sheets

## Standard Abbreviations

Common abbreviations used in notes:
- **ASSY**: Assembly
- **DIA**: Diameter
- **MATL**: Material
- **REQD**: Required
- **TYP**: Typical
- **REF**: Reference
- **MIN**: Minimum
- **MAX**: Maximum
- **APPX**: Approximate
- **CRES**: Corrosion Resistant Steel
- **FAI**: First Article Inspection
- **COC**: Certificate of Conformance

## References

- Parent directory: [`../README.md`](../README.md)
- Drawing standards: [`../../DRAWINGS/README.md`](../../DRAWINGS/README.md)
- Materials: [`../../MATERIALS/README.md`](../../MATERIALS/README.md)
- ASME Y14.38 — Abbreviations and Acronyms
- Company drafting manual
