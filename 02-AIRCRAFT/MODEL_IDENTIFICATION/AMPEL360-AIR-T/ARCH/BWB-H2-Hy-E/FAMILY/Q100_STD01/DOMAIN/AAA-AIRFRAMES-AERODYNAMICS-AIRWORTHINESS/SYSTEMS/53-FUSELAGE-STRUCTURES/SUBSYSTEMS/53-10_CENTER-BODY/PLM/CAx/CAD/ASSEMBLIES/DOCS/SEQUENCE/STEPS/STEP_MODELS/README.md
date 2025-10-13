# STEP_MODELS — Assembly Step 3D Models

## Purpose

This directory contains 3D models in STEP format (ISO 10303) that illustrate each assembly step for the 53-10 Center Body.

## Contents

### Model Types
- **Step configurations**: 3D models showing component positions at each step
- **Assembly sequences**: Progressive models showing build-up
- **Installation guides**: Models showing installation procedures
- **Exploded views**: Models showing component relationships

## Model Format

### File Format
- **Primary**: STEP (ISO 10303-242/AP242)
- **Extension**: `.step` or `.stp`
- Use lowercase for consistency: `.step`

### Model Contents
Each step model should include:
- Components installed up to that step
- Component orientation and position
- Reference geometry (datum planes, axes)
- Assembly features and interfaces
- Optional: tooling and fixture geometry

## Naming Convention

Use the following pattern:
```
53-10_STEP-MODEL_<step-number>_<description>_<version>.step
```

Examples:
- `53-10_STEP-MODEL_001_FRAME-F05-POSITIONED_v01.step`
- `53-10_STEP-MODEL_002_STRINGERS-ATTACHED_v02.step`
- `53-10_STEP-MODEL_003_SKIN-INSTALLED_v01.step`

## Model Best Practices

### Geometry Guidelines
- Include only necessary detail level
- Show assembly state at step completion
- Include critical reference geometry
- Maintain consistent coordinate system
- Simplify non-critical features

### Metadata
Include in STEP file header:
- Step number and description
- Assembly identification
- Model version
- Creation date
- Author/organization

## Usage

### Viewing
- Open in CAD viewers or systems
- Use for assembly planning
- Reference during build
- Training and documentation

### Validation
- Verify component fit and clearances
- Check installation sequences
- Validate tooling access
- Review with production team

## Related Directories

- **STEP_DRAWINGS**: [`../STEP_DRAWINGS/`](../STEP_DRAWINGS/) — 2D drawings of steps
- **Animations**: [`../../ANIMATIONS/`](../../ANIMATIONS/) — Animated assembly sequences
- **Assembly Models**: [`../../../TOP_LEVEL/`](../../../TOP_LEVEL/) — Complete assembly models
