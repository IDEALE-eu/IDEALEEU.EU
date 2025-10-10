# RES — Resources (CSS/XSL/Schematron)

## Purpose

This directory contains **transformation stylesheets, validation schemas, and presentation resources** for processing and validating S1000D Data Modules in the 21-10 Radiators & Heat Exchangers subsystem.

## Contents

### XSL/XSLT Stylesheets
- S1000D to HTML transformation
- S1000D to PDF (via XSL-FO)
- Custom rendering templates
- Publication module processors
- Cross-reference resolution

### CSS Stylesheets
- Web presentation styles
- IETP viewer styles
- Print media styles
- Responsive design rules

### Schematron Rules
- Business rule validation
- S1000D schema validation
- BREX rule implementation
- Content quality checks
- Cross-reference validation

### XML Schemas
- S1000D 6.0 XSD schemas
- Project-specific schema extensions
- BREX schema definitions

## Directory Structure

```
res/
├── xsl/                    # XSL/XSLT transformations
│   ├── s1000d-to-html.xsl
│   ├── s1000d-to-fo.xsl
│   └── pm-processor.xsl
├── css/                    # CSS stylesheets
│   ├── ietp-viewer.css
│   ├── print.css
│   └── responsive.css
├── schematron/             # Schematron validation
│   ├── brex-rules.sch
│   ├── quality-checks.sch
│   └── cross-ref.sch
└── xsd/                    # XML Schema definitions
    ├── s1000d-6.0/
    └── ampel360-extensions/
```

## XSL/XSLT Transformations

### HTML Output
Purpose: Generate web-viewable HTML from Data Modules
- Renders S1000D XML to HTML5
- Includes CSS styling references
- Processes ICN references
- Handles cross-references and links

### PDF Output (via XSL-FO)
Purpose: Generate print-ready PDF documents
- Transforms S1000D to XSL-FO
- Applies formatting for print
- Page breaks and layout
- Header/footer generation

### Publication Module Processing
Purpose: Assemble multiple DMs into publications
- Collects referenced Data Modules
- Orders content per Publication Module
- Resolves cross-references
- Generates table of contents

## CSS Stylesheets

### IETP Viewer Styles
- Navigation panel styling
- Content area layout
- ICN display formatting
- Responsive design rules

### Print Styles
- Page size and margins
- Font specifications
- Color vs. B&W rendering
- Page break control

## Schematron Validation

### BREX Rules
Purpose: Enforce business rules from BREX Data Module
- Project-specific constraints
- Metadata requirements
- Nomenclature standards
- Numbering conventions

### Quality Checks
Purpose: Content quality validation
- Completeness checks
- Consistency validation
- Cross-reference integrity
- Illustration link validation

## Usage Guidelines

### Applying Transformations

**HTML Generation**:
```bash
xsltproc -o output.html res/xsl/s1000d-to-html.xsl input-dm.xml
```

**PDF Generation** (two-step):
```bash
xsltproc -o temp.fo res/xsl/s1000d-to-fo.xsl input-dm.xml
fop -fo temp.fo -pdf output.pdf
```

### Running Validation

**Schematron Validation**:
```bash
xmllint --schematron res/schematron/brex-rules.sch input-dm.xml
```

**Schema Validation**:
```bash
xmllint --schema res/xsd/s1000d-6.0/dmodule.xsd input-dm.xml
```

## Development Guidelines

**DO**:
- Version control all resources
- Document custom templates
- Test transformations thoroughly
- Validate against multiple browsers
- Optimize for performance
- Follow S1000D standards

**DO NOT**:
- Modify standard S1000D schemas
- Break backward compatibility
- Ignore validation errors
- Hard-code project-specific values
- Skip testing on target platforms

## Customization

### Project-Specific Styles
- Company branding elements
- Custom color schemes
- Logo placement
- Footer/header content

### Custom Templates
- AMPEL360-specific formatting
- Subsystem-specific conventions
- Special rendering requirements

## Testing Requirements

Before deployment:
- [ ] Test on target IETP viewer
- [ ] Validate HTML output
- [ ] Check PDF rendering
- [ ] Verify cross-references
- [ ] Test on multiple browsers
- [ ] Validate against S1000D schemas

## Tools and Software

### XSLT Processors
- **Saxon**: Enterprise XSLT processor
- **Xalan**: Apache XSLT processor
- **xsltproc**: Command-line processor (libxslt)

### XSL-FO Processors
- **Apache FOP**: Open source FO processor
- **RenderX XEP**: Commercial processor
- **Antenna House**: High-quality PDF output

### Validation Tools
- **xmllint**: Schema and Schematron validation
- **Oxygen XML Editor**: Integrated validation
- **Schematron validators**: Various implementations

## Version Control

Track changes to:
- Stylesheet versions
- Schema updates
- Schematron rule modifications
- CSS revisions

Document:
- Change rationale
- Compatibility impacts
- Migration requirements

## Related Directories

- **[../../dm/](../../dm/)** — Data Modules to process
- **[../../brex/](../../brex/)** — BREX rules to enforce
- **[../../delivery/](../../delivery/)** — Output destination

---

**Last Updated**: 2025-10-11
