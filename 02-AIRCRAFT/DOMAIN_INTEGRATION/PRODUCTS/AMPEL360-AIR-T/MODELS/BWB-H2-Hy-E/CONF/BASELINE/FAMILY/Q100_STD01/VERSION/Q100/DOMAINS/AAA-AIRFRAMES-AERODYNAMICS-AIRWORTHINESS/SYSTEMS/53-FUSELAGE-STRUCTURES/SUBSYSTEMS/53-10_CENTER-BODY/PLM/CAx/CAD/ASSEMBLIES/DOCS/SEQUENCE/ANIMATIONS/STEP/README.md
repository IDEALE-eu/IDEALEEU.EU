# STEP — STEP-Based Animations

## Purpose

This directory contains STEP-based animation files showing assembly sequences for the 53-10 Center Body.

## Contents

### Animation Files
- Sequential STEP files showing assembly progression
- Animated assembly models
- STEP animation sequences
- Time-based assembly models

## STEP Animation Format

### File Organization
STEP animations can be organized as:
- **Sequential files**: Series of STEP files showing progression
- **Single file**: STEP file with kinematic assembly
- **Model states**: Multiple configurations in STEP AP242

### File Format
- **Format**: STEP (ISO 10303-242/AP242)
- **Extension**: `.step` or `.stp`
- Use lowercase for consistency: `.step`

## Naming Convention

### Sequential Files
For series of STEP files:
```
53-10_ANIM-STEP_<sequence-id>_STEP-<number>_<version>.step
```

Examples:
- `53-10_ANIM-STEP_FRAME-ASSY_STEP-001_v01.step`
- `53-10_ANIM-STEP_FRAME-ASSY_STEP-002_v01.step`
- `53-10_ANIM-STEP_FRAME-ASSY_STEP-003_v01.step`

### Single Animation File
For single STEP animation:
```
53-10_ANIM-STEP_<sequence-id>_<description>_<version>.step
```

Example:
- `53-10_ANIM-STEP_COMPLETE-ASSY_KINEMATIC_v01.step`

## STEP Animation Types

### Sequential Model States
- Series of STEP files
- Each file shows one assembly state
- View in sequence to see assembly
- Easy to create and manage

### Kinematic Assembly
- Single STEP AP242 file
- Contains motion definitions
- Requires AP242-capable viewer
- Shows true assembly motion

### Configuration-Based
- STEP file with multiple configurations
- Switch between configurations
- Shows assembly progression
- Viewer-dependent

## Creating STEP Animations

### From CAD Systems
1. Create assembly in CAD
2. Define assembly sequence
3. Create snapshots at each step
4. Export each as STEP file
5. Number sequentially

### With AP242 Kinematics
1. Define assembly motion paths
2. Set time-based constraints
3. Export as STEP AP242
4. Include kinematic data

## Viewing STEP Animations

### Sequential Viewing
- Open STEP files in order
- View progression manually
- Use CAD viewers or systems
- Compare states

### Kinematic Playback
- Requires AP242-capable viewer
- Automatic playback
- Interactive control
- Realistic motion

## Related Directories

- **MP4 Animations**: [`../MP4/`](../MP4/) — Video format animations
- **Step Models**: [`../../STEPS/STEP_MODELS/`](../../STEPS/STEP_MODELS/) — Source 3D models
