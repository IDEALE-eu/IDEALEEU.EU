# VIEW_STATES — Saved Display Configurations

## Purpose

This directory contains saved view states and display configurations for simplified assembly models to ensure consistent visualization across design reviews and presentations.

## Contents

### View State Types
- **Review views**: Standard views for design reviews
- **Presentation views**: Views optimized for stakeholder presentations
- **Analysis views**: Views highlighting specific analysis regions
- **Interface views**: Views showing system interfaces
- **Exploded views**: Assembly disassembly visualizations

## What Are View States?

View states (also called display states or visualization states) capture:
- **Camera position**: Viewing angle and zoom level
- **Component visibility**: Which parts are shown/hidden
- **Display mode**: Shaded, wireframe, or transparent
- **Section cuts**: Cross-section planes active
- **Colors/textures**: Custom coloring applied
- **Explode distance**: For exploded views

## Standard View Definitions

### Front View
- Camera: Looking at front of aircraft (+X direction)
- Components: All visible, standard colors
- Use: General arrangement review

### Top View
- Camera: Looking down from above (+Z direction)
- Components: All visible
- Use: Plan view, system routing

### Side View (Right)
- Camera: Looking from right side (+Y direction)
- Components: All visible
- Use: Profile view, height clearances

### Isometric View
- Camera: 45° angle showing front-right-top
- Components: All visible, shaded
- Use: General 3D visualization

### Interface View
- Camera: Focused on specific interface region
- Components: Interface components highlighted
- Display: Surrounding structure transparent
- Use: Interface coordination meetings

### Section View
- Camera: Perpendicular to section plane
- Components: Section cut active
- Display: Interior structure visible
- Use: Internal layout review

### Exploded View
- Components: Separated along logical assembly paths
- Explode distance: Adjustable (25%, 50%, 100%)
- Use: Assembly sequence understanding

## File Formats

### Native CAD Formats
- **CATIA**: Scene files (`.scn`), view sets
- **NX**: Part Navigator views, display states
- **SolidWorks**: Display states (`.sldasm`)
- **Creo**: Simplified reps, combined states

### Neutral Formats
- **JT**: Saved views in JT files
- **3D PDF**: Embedded views in PDF documents
- **Screenshots**: PNG/JPEG for documentation

## Naming Convention

Use the following pattern:
```
53-10_VIEW_<assembly-id>_<view-type>_LOD<level>_<version>.<ext>
```

Examples:
- `53-10_VIEW_CENTER-BODY_ISO_LOD2_v01.scn`
- `53-10_VIEW_FRAME-SECTION_SECTION_LOD3_v01.png`
- `53-10_VIEW_WING-ATTACH_INTERFACE_LOD2_v02.pdf`

## Organization

Organize view states by:
- Assembly or sub-assembly
- View type (iso, section, exploded, etc.)
- Level of detail (LOD1-LOD4)
- Version number

## View State Requirements

### Consistency
View states should:
- Use standard camera angles where possible
- Apply consistent component colors
- Maintain uniform explode distances
- Document any custom settings

### Documentation
Each view state should document:
- **Purpose**: Intended use case
- **Settings**: Camera position, display mode
- **Components**: Visibility states
- **Colors**: Custom coloring applied
- **Notes**: Special considerations

## Standard Color Schemes

### Material-Based Coloring
- **Aluminum alloys**: Light gray
- **Titanium**: Dark gray
- **Composites**: Carbon fiber texture
- **Steel**: Metallic gray

### Functional Coloring
- **Primary structure**: Blue
- **Secondary structure**: Green
- **Fasteners**: Yellow
- **Interfaces**: Red outline

### Status Coloring
- **Approved**: Green
- **In review**: Yellow
- **Not approved**: Red
- **Modified**: Orange

## Creating View States

### Best Practices
1. Start with standard view (front, top, side, iso)
2. Adjust camera for optimal visibility
3. Set component visibility as needed
4. Apply appropriate display mode
5. Add section cuts if required
6. Document settings
7. Save with descriptive name
8. Test loading and display

### Quality Checks
Before saving view state:
- [ ] Camera position optimized
- [ ] All intended components visible
- [ ] Display mode appropriate
- [ ] Colors/transparency correct
- [ ] Labels readable
- [ ] View loads quickly

## Use Cases

### Design Reviews
Create standard view set:
- Overall isometric view
- Front/top/side orthographic views
- Key interface views
- Section views through critical areas

### Stakeholder Presentations
Create presentation views:
- High-quality rendered views
- Appropriate transparency for clarity
- Professional color scheme
- Background/lighting optimized

### Manufacturing Planning
Create manufacturing views:
- Assembly sequence exploded views
- Access views for tooling
- Interface views for alignment
- Critical dimension views

### Documentation
Create documentation views:
- Standard orthographic views
- Section views for technical manuals
- Exploded views for parts catalogs
- Interface views for ICDs

## Export Requirements

### Screenshot Exports
- **Format**: PNG (preferred) or JPEG
- **Resolution**: Minimum 1920x1080 pixels
- **Quality**: High quality, anti-aliasing enabled
- **Background**: White or transparent as appropriate

### 3D PDF Exports
- Embed multiple view states
- Include measurement tools
- Enable part tree navigation
- Add annotations as needed

### JT Exports
- Include saved views
- Maintain PMI visibility
- Preserve component structure
- Document view metadata

## Version Control

### File Management
- Commit view state files to Git
- Version view states with assemblies
- Document changes in commit messages
- Tag major review milestones

### Synchronization
Keep view states synchronized with:
- Assembly model versions
- Component changes
- Interface updates
- Configuration changes

## Quality Standards

View states must:
- Load correctly in target CAD system
- Display components as documented
- Maintain performance (< 5 sec load time)
- Be validated before design reviews

## Related Directories

- **Assemblies**: [`../ASM/`](../ASM/) — Models using these view states
- **Documentation**: [`../DOCS/`](../DOCS/) — View state documentation
- **Exports**: [`../EXPORTS/`](../EXPORTS/) — Exported views and screenshots
- **Rules**: [`../RULES/`](../RULES/) — View state standards and guidelines
