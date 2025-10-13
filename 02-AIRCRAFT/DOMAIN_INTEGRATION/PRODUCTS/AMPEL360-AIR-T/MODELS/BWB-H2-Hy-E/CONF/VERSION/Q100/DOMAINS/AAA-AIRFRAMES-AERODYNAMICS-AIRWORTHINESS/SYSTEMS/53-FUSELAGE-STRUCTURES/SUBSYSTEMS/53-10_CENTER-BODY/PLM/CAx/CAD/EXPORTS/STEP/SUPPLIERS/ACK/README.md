# ACK — Supplier Acknowledgments

## Purpose

This directory contains **supplier acknowledgment files** including validated STEP files returned by suppliers confirming they can manufacture to specification.

## What to Store

- Supplier-validated STEP models
- As-interpreted geometry acknowledgments
- Manufacturing feasibility confirmations
- Supplier design review responses
- Capability study results

## Acknowledgment Process

1. **Send package**: Issue package from [**../PACKAGES/**](../PACKAGES/)
2. **Supplier review**: Supplier validates they can manufacture
3. **Return ACK**: Supplier returns validated STEP file here
4. **Engineering review**: Confirm supplier interpretation is correct
5. **Approve**: Proceed with manufacturing or resolve discrepancies

## File Naming Convention

```
<subsystem>_ACK_<supplier-name>_<package-id>_<date>.step
```

Example:
```
53-10_ACK_ACME-AERO_PKG-001_20250115.step
```

## What to Validate

When reviewing supplier ACK files:
- [ ] Geometry matches original intent
- [ ] Critical dimensions preserved
- [ ] GD&T interpreted correctly
- [ ] Material specifications understood
- [ ] Manufacturing processes feasible
- [ ] Supplier can meet tolerances

## Discrepancy Resolution

If supplier ACK differs from original:
1. Document discrepancies
2. Engineering review and assessment
3. Issue clarification or ECO if needed
4. Obtain revised ACK from supplier
5. Approve final interpretation

## Related Directories

- [**../PACKAGES/**](../PACKAGES/) — Original supplier packages
- [**../../QA/CHECKS/**](../../QA/CHECKS/) — Quality validation
- [**../../REVISIONS/**](../../REVISIONS/) — Configuration control
- [**../../INDEX/**](../../INDEX/) — Package tracking

## Procurement Coordination

- Track acknowledgment status
- Link to purchase orders
- Monitor supplier readiness
- Coordinate manufacturing schedule

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- Supplier management: `00-PROGRAM/PROCUREMENT/`
