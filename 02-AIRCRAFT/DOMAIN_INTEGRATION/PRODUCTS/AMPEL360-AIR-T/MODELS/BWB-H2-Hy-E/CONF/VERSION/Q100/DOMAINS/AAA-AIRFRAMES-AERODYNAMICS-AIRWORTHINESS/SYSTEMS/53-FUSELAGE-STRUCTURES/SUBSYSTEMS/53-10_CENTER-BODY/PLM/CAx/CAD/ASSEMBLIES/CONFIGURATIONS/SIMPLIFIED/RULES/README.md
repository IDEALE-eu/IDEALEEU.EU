# RULES — Simplification Rules and Guidelines

## Purpose

This directory contains rules, guidelines, and procedures for creating and managing simplified assembly configurations.

## Contents

### Rule Types
- **Simplification rules**: Guidelines for reducing model complexity
- **Approval criteria**: Requirements for using simplified models
- **Level of detail rules**: Definitions for LOD1-LOD4
- **Quality standards**: Validation requirements

## Simplification Rules

### LOD1 — Envelope Only
**Purpose**: Outer boundary representation only

**Rules**:
- Represent component as single bounding box or envelope
- Maintain external interfaces and mounting points
- No internal features or details
- Single solid or surface body
- Mass properties maintained

**Use cases**:
- Space claim analysis
- High-level layout reviews
- Preliminary clearance checks

### LOD2 — Major Components
**Purpose**: Simplified major subassemblies

**Rules**:
- Major components represented with simplified geometry
- Internal features removed
- Fasteners replaced with symbolic representations
- Complex surfaces simplified to basic shapes
- Mass properties maintained

**Use cases**:
- Executive design reviews
- Stakeholder presentations
- Early-stage analysis

### LOD3 — Moderate Detail
**Purpose**: Reduced detail for technical reviews

**Rules**:
- Recognizable component shapes
- Critical features retained
- Non-critical features suppressed
- Fasteners simplified but visible
- Sufficient detail for engineering review

**Use cases**:
- Technical design reviews
- Interface coordination
- Assembly sequence planning

### LOD4 — Full Detail Reference
**Purpose**: Full detail retained (reference only)

**Rules**:
- All features present
- Full detail maintained
- Used as baseline reference
- Not intended for performance improvement

**Use cases**:
- Detailed analysis requiring full geometry
- Manufacturing planning
- As-designed documentation

## Feature Simplification Rules

### Geometry Features
- **Remove**: Fillets < 5mm radius, chamfers < 2mm
- **Simplify**: Complex curves to simple arcs or lines
- **Combine**: Multiple small features into single bodies
- **Replace**: Detailed components with proxy shapes

### Fasteners
- **LOD1**: No fasteners shown
- **LOD2**: Symbolic representation only
- **LOD3**: Simplified fastener geometry
- **LOD4**: Full fastener detail

### Internal Components
- **LOD1-2**: Remove all internal components
- **LOD3**: Show major internal structures only
- **LOD4**: All internal components

## Approval Requirements

### Model Validation
Before approving simplified model:
- [ ] Verify external interfaces unchanged
- [ ] Confirm mass properties within 5% of detailed model
- [ ] Check for geometric errors (gaps, overlaps)
- [ ] Validate performance in target use case
- [ ] Document simplifications applied

### Usage Approval
Each simplified model requires:
- **Creator**: Designer who created simplified model
- **Reviewer**: Senior engineer review
- **Approver**: Chief engineer or designee
- **Use case**: Intended applications documented
- **Restrictions**: Limitations clearly stated

## Documentation Requirements

Each simplified configuration must document:
- Level of detail applied (LOD1-4)
- Simplification techniques used
- Reference to detailed baseline model
- Mass property comparison
- Approved use cases
- Usage restrictions and limitations
- Validation results
- Approval signatures and dates

## Quality Standards

### Geometric Quality
- No invalid geometry (gaps, overlaps, bad edges)
- Surfaces properly trimmed and joined
- Coordinate system aligned with baseline
- Units consistent (millimeters)

### Performance Criteria
- File size reduced by minimum 50% (LOD1-2)
- Load time reduced by minimum 30%
- Visual quality appropriate for use case
- Mass properties within 5% of baseline

## Change Control

### Version Management
- New version required for any geometry change
- Document changes in version history
- Maintain traceability to baseline
- Tag major revisions

### Baseline Synchronization
When detailed baseline changes:
- Review simplified models for impacts
- Update simplified models if interfaces affected
- Re-validate simplified models
- Update documentation

## Related Directories

- **Assemblies**: [`../ASM/`](../ASM/) — Simplified assembly files
- **Parts**: [`../PARTS/`](../PARTS/) — Simplified component parts
- **Documentation**: [`../DOCS/`](../DOCS/) — Approval documentation
- **Baseline**: [`../../../TOP_LEVEL/`](../../../TOP_LEVEL/) — Detailed assemblies
