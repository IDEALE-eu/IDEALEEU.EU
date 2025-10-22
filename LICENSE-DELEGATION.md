# License Delegation Schema

## Overview

This repository follows a **delegated licensing model** to accommodate different licensing needs across various components and packages within the IDEALE-EU Aerospace Digital Passport Platform.

## General License

The repository root is licensed under the **Apache License 2.0** (see [LICENSE](LICENSE)). This license applies to:

- Repository structure and organization
- Documentation in the root `docs/` directory
- Build and utility scripts in `scripts/` and `tools/`
- Configuration files
- Any code or content not covered by a specific delegated license

## Delegated Licenses for Partitioned Packages

Individual packages and components within this repository may have their own specific licenses to accommodate different use cases, dependencies, or collaboration requirements. When a subdirectory contains its own LICENSE file, that license takes precedence for that specific package.

### Package-Specific Licenses

| Package/Directory | License | Notes |
|-------------------|---------|-------|
| `digital-passport/` | Apache-2.0 | Interactive web application for aerospace digital passports |
| Root utilities | Apache-2.0 | Structure scan tools, README maintenance utilities |

### Adding a Delegated License

When creating a new package or component that requires a different license:

1. **Create a LICENSE file** in the package directory:
   ```
   <package-directory>/LICENSE
   ```

2. **Update package.json** (if applicable) with the license field:
   ```json
   {
     "license": "MIT"
   }
   ```

3. **Update this document** by adding an entry to the table above

4. **Include a notice** in the package README:
   ```markdown
   ## License
   
   This package is licensed under the [LICENSE_TYPE] License - see the [LICENSE](LICENSE) file for details.
   
   Note: This package uses a delegated license that differs from the repository root license.
   ```

## License Hierarchy

The licensing hierarchy follows this precedence:

1. **Package-specific LICENSE file** - Takes highest precedence for files within that package
2. **Package.json license field** - Used when no LICENSE file exists in the package
3. **Repository root LICENSE** - Default license for all other content

## Compatibility Guidelines

When choosing a delegated license for a package:

- Ensure compatibility with the Apache-2.0 root license
- Consider dependencies and their licenses
- Respect any license requirements from third-party components
- Document any special licensing considerations in the package README

## Common License Options

For guidance, here are commonly used licenses appropriate for different scenarios:

- **Apache-2.0**: Permissive, patent grant, good for business-friendly projects
- **MIT**: Simple permissive license, minimal restrictions
- **GPL-3.0**: Copyleft license, requires derivative works to be open source
- **BSD-3-Clause**: Permissive with attribution requirements
- **Proprietary/UNLICENSED**: For internal packages not intended for external distribution

## Contact

For questions about licensing or to request a license delegation for a new package, please open an issue or contact the repository maintainers.

---

**Last Updated**: 2025-10-20
