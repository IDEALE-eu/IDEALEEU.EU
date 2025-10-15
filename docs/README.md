# IDEALE-EU Documentation

This directory contains comprehensive documentation for the IDEALE-EU platform.

## Documentation Structure

```
docs/
├── index.md                              # Main documentation index
├── quick-start/
│   └── index.md                          # Quick start guide
├── tfa-domains/
│   └── index.md                          # TFA domains reference
├── cax-lifecycle/
│   └── index.md                          # CAx lifecycle overview
├── technical/
│   └── qs-specification/
│       └── index.md                      # QS technical specification
├── glossary/
│   └── index.md                          # Glossary and acronyms
└── api/
    └── index.md                          # API documentation
```

## Accessing Documentation

- **Online**: Visit [https://idealeeu.eu/docs/](https://idealeeu.eu/docs/)
- **Local**: Use any markdown viewer or browser to view the `.md` files

## Documentation Sections

### 1. Quick Start Guide
Get started with IDEALE-EU in minutes. Covers account setup, role-specific workflows, CAD plugin installation, and first digital passport creation.

**Audience**: All users (Engineers, Program Managers, Auditors, Suppliers)

### 2. TFA Domains Reference
Deep dive into the 15 Threading Functional Architecture domains that structure aerospace lifecycle data.

**Audience**: Engineers, System Architects, Program Managers

### 3. CAx Lifecycle Overview
Understand the 9-phase Computer-Aided lifecycle with "to scale" methodology for non-linear physics.

**Audience**: Engineers, Designers, Analysts

### 4. QS Technical Specification
Mathematical formalization of Quantum Superposition (QS) for configuration management and evidence anchoring.

**Audience**: System Architects, Algorithm Developers, Certification Engineers

### 5. Glossary and Acronyms
Complete reference for all IDEALE-EU terminology with canonical definitions.

**Audience**: All users

### 6. API Documentation
REST API reference with authentication, endpoints, and code examples.

**Audience**: Developers, Integration Engineers

## Contributing

To contribute to the documentation:

1. **Edit Markdown Files**: Make changes to the appropriate `.md` file
2. **Follow Format**: Maintain consistent structure with YAML front matter
3. **Test Links**: Verify all internal links work correctly
4. **Submit PR**: Create a pull request with your changes

## Front Matter Format

All documentation pages include YAML front matter:

```yaml
---
layout: page
title: "Page Title"
description: "Brief description"
---
```

## Internal Links

Use absolute paths for internal links:
```markdown
[Link Text](/docs/section/page/)
```

Use anchor links for heading references:
```markdown
[Link to Section](/docs/page/#section-heading)
```

## Style Guidelines

- **Headings**: Use ATX-style headings (`#`, `##`, `###`)
- **Code Blocks**: Specify language for syntax highlighting
- **Lists**: Use `-` for unordered lists, `1.` for ordered lists
- **Emphasis**: Use `**bold**` for important terms, `*italic*` for emphasis
- **Links**: Use descriptive link text, not "click here"

## Maintenance

- Review documentation quarterly for accuracy
- Update version numbers and dates as needed
- Keep code examples up-to-date with API changes
- Maintain consistency across all sections

## Contact

For documentation questions or suggestions:
- **Email**: docs@ideale-eu.aero
- **Issues**: [GitHub Issues](https://github.com/IDEALE-eu/IDEALEEU.EU/issues)

---

*Last updated: 2025-01-15*
