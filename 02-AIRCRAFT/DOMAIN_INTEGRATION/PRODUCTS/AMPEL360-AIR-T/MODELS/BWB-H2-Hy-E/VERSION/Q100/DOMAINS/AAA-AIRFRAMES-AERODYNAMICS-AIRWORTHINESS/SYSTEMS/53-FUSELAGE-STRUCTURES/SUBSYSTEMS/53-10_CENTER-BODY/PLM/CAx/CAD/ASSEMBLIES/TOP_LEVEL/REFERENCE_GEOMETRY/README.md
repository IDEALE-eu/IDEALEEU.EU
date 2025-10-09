# REFERENCE_GEOMETRY — Reference Geometry Elements

## Purpose

This directory contains reference geometry used to position and orient the top-level assembly and its components.

## Contents

### Reference Elements
- **Coordinate systems**: [`COORDINATE_SYSTEMS/`](./COORDINATE_SYSTEMS/) — Global and local coordinate frames
- **Reference planes**: [`PLANES/`](./PLANES/) — Datum planes and construction surfaces
- **Datums**: [`DATUMS/`](./DATUMS/) — Datum features and geometric references

## Usage

Reference geometry is used for:
- **Component positioning**: Aligning parts in assembly
- **Interface definition**: Establishing mating surfaces
- **Analysis setup**: Defining load and boundary conditions
- **Manufacturing reference**: Tooling and fixture alignment

## Standards

Follow:
- **ASME Y14.5**: Geometric dimensioning and tolerancing
- **ISO 1101**: Geometrical tolerancing standards
- **ATA Chapter 06**: Dimensions and stations reference

## Related Systems

- **06-00 Dimensions & Stations**: Master coordinate system definition
- **CAE Models**: Analysis coordinate systems
- **Manufacturing**: Tooling reference frames

## Best Practices

- Use **consistent naming** for reference elements
- Document **origin and orientation** of coordinate systems
- Maintain **traceability** to master aircraft frame (GAF)
- Include **tolerance specifications** where applicable
