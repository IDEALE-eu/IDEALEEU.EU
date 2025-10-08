# Software Change Log

> Location: `CONFIG_MGMT/06-CHANGES/11-SOFTWARE_CHANGES/SW_CHANGE_LOG.md`

## Purpose

Track all software changes including version control integration, requirements traceability, and DO-178C compliance.

## Software Change Management

Software changes follow standard ECR/ECO process with additional DO-178C requirements:
- Requirements traceability (Req ↔ Code ↔ Test)
- Structural coverage analysis
- Tool qualification impact
- Configuration management per DO-178C Section 7

## Version Control Integration

Git integration per **[../../12-CI_CD_RULES/BRANCHING_MODEL.md](../../12-CI_CD_RULES/BRANCHING_MODEL.md)**

**Branch naming:** `ecr/[number]-[description]` or `eco/[number]-[description]`

**Commit message format:**
```
<type>(scope): <subject>

<body>

ECR-YYYY-#### or ECO-YYYY-####
Reviewed-by: [Name]
```

## Software Change Log

| ECO Number | Description | Software Version | Git Tag | DO-178C Level | Verification Status |
|------------|-------------|------------------|---------|---------------|---------------------|
| ECO-2025-0007 | Flight control algorithm update | v2.1.0 | v2.1.0 | Level A | Complete |

## Traceability

See **[TRACEABILITY.json](./TRACEABILITY.json)** for detailed Req ↔ Code ↔ Test mapping.

## Tool Qualification

Tool changes tracked per DO-178C requirements.
See **[TOOLING.md](./TOOLING.md)** for tool qualification status.
