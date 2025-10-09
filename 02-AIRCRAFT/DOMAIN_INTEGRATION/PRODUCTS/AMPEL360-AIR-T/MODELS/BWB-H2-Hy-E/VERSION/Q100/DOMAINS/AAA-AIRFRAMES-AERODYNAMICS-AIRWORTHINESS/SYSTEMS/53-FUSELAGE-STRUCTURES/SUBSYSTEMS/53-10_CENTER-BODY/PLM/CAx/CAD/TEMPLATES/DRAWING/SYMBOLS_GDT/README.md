# SYMBOLS_GDT — GD&T Symbols and Feature Control Frames

## Purpose

Geometric Dimensioning and Tolerancing (GD&T) symbol libraries and feature control frame templates.

## Contents

Standard GD&T symbols per ASME Y14.5 and ISO 1101:
- **Geometric characteristic symbols**
- **Material condition modifiers**
- **Feature control frames**
- **Datum feature symbols**
- **Datum reference frames**
- **Surface texture symbols**

## Geometric Characteristics

### Form Tolerances
- **Straightness** (⏤): Controls straightness of line elements
- **Flatness** (⏥): Controls flatness of surfaces
- **Circularity** (○): Controls roundness of circular features
- **Cylindricity** (⌭): Controls form of cylindrical surfaces

### Orientation Tolerances
- **Perpendicularity** (⊥): Controls perpendicularity to datum
- **Parallelism** (∥): Controls parallelism to datum
- **Angularity** (∠): Controls angular orientation to datum

### Location Tolerances
- **Position** (⊕): Controls location of features
- **Concentricity** (◎): Controls coaxiality of features
- **Symmetry** (⌯): Controls symmetry about datum plane

### Profile Tolerances
- **Profile of a line** (⌒): Controls profile of line elements
- **Profile of a surface** (⌓): Controls profile of surfaces

### Runout Tolerances
- **Circular runout** (↗): Controls runout of circular elements
- **Total runout** (↗↗): Controls total runout of entire surface

## Material Condition Modifiers

- **Maximum Material Condition (MMC)**: ⓜ
- **Least Material Condition (LMC)**: ⓛ
- **Regardless of Feature Size (RFS)**: (none) — default condition

## Datum Feature Symbols

Standard datum identifiers:
- Datum letters: A, B, C, D, etc.
- Datum feature symbol: Triangle with letter
- Datum targets: Point, line, or area targets

## Feature Control Frame Structure

```
┌─────┬─────┬─────┬─────┬─────┐
│ SYM │ TOL │ MOD │ DAT │ MOD │
└─────┴─────┴─────┴─────┴─────┘

SYM: Geometric characteristic symbol
TOL: Tolerance value
MOD: Material condition modifier
DAT: Datum reference(s)
```

## Naming Convention

```
GDT_<symbol-type>_<variant>.<ext>
```

Examples:
- `GDT_Position_MMC.dwg`
- `GDT_Profile_Surface.dwg`
- `GDT_Perpendicularity_RFS.dwg`
- `GDT_DatumFrame_ABC.dwg`

## Usage Guidelines

### Applying GD&T
1. Establish datum reference frame (primary, secondary, tertiary)
2. Identify functional requirements of features
3. Select appropriate geometric characteristic
4. Specify tolerance value based on function
5. Apply material condition modifiers as needed
6. Complete feature control frame

### Best Practices
- Use GD&T for functional requirements, not convenience
- Establish clear datum reference frames
- Apply MMC/LMC when appropriate for bonus tolerance
- Document critical characteristics on drawings
- Train team on GD&T interpretation
- Follow ASME Y14.5 or ISO 1101 consistently (don't mix)

### Common Applications
- **Position tolerances**: Hole patterns, mounting features
- **Profile tolerances**: Complex contours, aerodynamic surfaces
- **Perpendicularity**: Mating surfaces, structural interfaces
- **Parallelism**: Guide surfaces, bearing surfaces
- **Runout**: Rotating components, shaft surfaces

## References

- Parent directory: [`../README.md`](../README.md)
- ASME Y14.5-2018 — Dimensioning and Tolerancing
- ISO 1101:2017 — Geometrical tolerancing
- ASME Y14.43 — Dimensioning and Tolerancing Principles for Gages and Fixtures
- Company GD&T application guide
