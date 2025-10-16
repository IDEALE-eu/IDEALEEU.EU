# MLQP for GENCMS + CSDB (starter)

Scope: qualify DM/PM/IETP through agents, dual control, audit, and evidence.

Layers:
1) Automated: Schema, BREX, DMRL, references, applicability previews.
2) Human: Reviewer + QA (dual approval, separation of duties).
3) Gating: Mixed-issue policy, classification ≤ clearance, audience scope.
4) Audit: Append-only JSON entries (see schemas/audit_log.schema.json).
5) Evidence: Bundle manifest for every build (see schemas/evidence_bundle.schema.json).
6) Escalation: SLA for reviews, threshold alerts, override logging.

Wire-in:
- Enforce RBAC via OPA policy (policies/rbac.rego).
- Emit evidence under ./evidence for pytest to assert.
- Use CI templates in ci/ to integrate gates.
