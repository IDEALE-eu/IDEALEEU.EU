# Interphase API - cURL Examples

## Overview

This document provides practical cURL examples for common Interphase API operations. All examples assume:

- **API Base URL**: `https://api.interphase.ap-aero.portfolio/v1`
- **Authentication**: Bearer token via OIDC
- **Content-Type**: `application/json`

## Setup

```bash
# Set environment variables
export API="https://api.interphase.ap-aero.portfolio/v1"
export TOK="your-oidc-bearer-token"
export PROGRAM_ID="ampel360-bwb-q100"
```

---

## Program Operations

### Create a Program

```bash
curl -sS -X POST "$API/programs" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "name": "AMPEL360 BWB Q100",
    "utcs": "utcs://AIRCRAFT/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01",
    "tenant": "ampel-aerospace"
  }' | jq .
```

**Expected Response** (201 Created):
```json
{
  "id": "ampel360-bwb-q100",
  "name": "AMPEL360 BWB Q100",
  "utcs": "utcs://AIRCRAFT/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01",
  "tenant": "ampel-aerospace",
  "status": "Active",
  "createdAt": "2025-10-14T10:00:00Z",
  "updatedAt": "2025-10-14T10:00:00Z"
}
```

### Get Program Details

```bash
curl -sS -X GET "$API/programs/$PROGRAM_ID" \
  -H "Authorization: Bearer $TOK" | jq .
```

---

## Context Operations

### Freeze Current Context

Create an immutable snapshot of the current program state:

```bash
curl -sS -X POST "$API/programs/$PROGRAM_ID/contexts/freeze" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "phase": "CAD",
    "gate": "CB",
    "manifestPath": "PLM/CAx/CAD/MANIFEST.csv",
    "comment": "Design review v3 approved"
  }' | jq .
```

**Expected Response** (201 Created):
```json
{
  "id": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "programId": "ampel360-bwb-q100",
  "phase": "CAD",
  "gate": "CB",
  "utcs": "utcs://AIRCRAFT/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/CAD/FROZEN/20251014",
  "checksum": "sha256:abc123def456...",
  "frozenAt": "2025-10-14T12:00:00Z",
  "manifestPath": "PLM/CAx/CAD/MANIFEST.csv",
  "artifactCount": 1247,
  "sizeBytes": 5368709120
}
```

---

## Gate Operations

### Approve a Phase Gate

Record an approval decision for a phase gate:

```bash
curl -sS -X POST "$API/programs/$PROGRAM_ID/phases/CAD/gates/CB/decision" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -d '{
    "decision": "Approve",
    "decidedBy": "ccb-179",
    "evidence": [
      "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/design-review-v3.pdf",
      "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/validation-results.json"
    ],
    "comment": "All validation checks passed. Design review completed."
  }' | jq .
```

**Expected Response** (200 OK):
```json
{
  "decision": "Approve",
  "decidedBy": "ccb-179",
  "evidence": [
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/design-review-v3.pdf",
    "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/validation-results.json"
  ],
  "comment": "All validation checks passed. Design review completed.",
  "decidedAt": "2025-10-14T14:30:00Z"
}
```

### Reject a Phase Gate

```bash
curl -sS -X POST "$API/programs/$PROGRAM_ID/phases/CAD/gates/CB/decision" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -d '{
    "decision": "Reject",
    "decidedBy": "ccb-179",
    "evidence": [
      "utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/validation-failures.json"
    ],
    "comment": "3 validation checks failed. Rework required."
  }' | jq .
```

### Hold a Phase Gate

```bash
curl -sS -X POST "$API/programs/$PROGRAM_ID/phases/CAD/gates/CB/decision" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -d '{
    "decision": "Hold",
    "decidedBy": "ccb-179",
    "evidence": [],
    "comment": "Awaiting additional analysis results."
  }' | jq .
```

---

## Transition Operations

### Execute Phase Transition

Initiate a transition from CAD to CAE:

```bash
SNAPSHOT_ID="c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a"

curl -sS -X POST "$API/transitions" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "snapshotId": "'"$SNAPSHOT_ID"'",
    "to": {
      "phase": "CAE",
      "gate": "CB"
    }
  }' | jq .
```

**Expected Response** (202 Accepted):
```json
{
  "id": "9e3f0e02-4g3e-6f25-1h0g-2e5fd5e8g6e4",
  "from": {
    "phase": "CAD",
    "gate": "CB"
  },
  "to": {
    "phase": "CAE",
    "gate": "CB"
  },
  "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "status": "Running",
  "startedAt": "2025-10-14T15:00:00Z"
}
```

### Get Transition Status

```bash
TRANSITION_ID="9e3f0e02-4g3e-6f25-1h0g-2e5fd5e8g6e4"

curl -sS -X GET "$API/transitions/$TRANSITION_ID" \
  -H "Authorization: Bearer $TOK" | jq .
```

**Expected Response** (200 OK):
```json
{
  "id": "9e3f0e02-4g3e-6f25-1h0g-2e5fd5e8g6e4",
  "from": {
    "phase": "CAD",
    "gate": "CB"
  },
  "to": {
    "phase": "CAE",
    "gate": "CB"
  },
  "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
  "status": "Succeeded",
  "startedAt": "2025-10-14T15:00:00Z",
  "finishedAt": "2025-10-14T15:05:00Z",
  "validationResults": [
    {
      "id": "f7e8d9c0-1a2b-3c4d-5e6f-7a8b9c0d1e2f",
      "target": "Structure",
      "status": "Passed"
    },
    {
      "id": "g8f9e0d1-2b3c-4d5e-6f7a-8b9c0d1e2f3g",
      "target": "Links",
      "status": "Passed"
    }
  ]
}
```

---

## Validation Operations

### Run Validation Checks

```bash
curl -sS -X POST "$API/validations/run" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "utcs": "utcs://AIRCRAFT/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/CAD",
    "checks": ["Structure", "Links", "KPIs"]
  }' | jq .
```

**Expected Response** (202 Accepted):
```json
{
  "id": "f7e8d9c0-1a2b-3c4d-5e6f-7a8b9c0d1e2f",
  "target": "Structure",
  "status": "Queued",
  "reportUrl": "https://reports.interphase.ap-aero.portfolio/validations/f7e8d9c0-1a2b-3c4d-5e6f-7a8b9c0d1e2f"
}
```

### Get Validation Results

```bash
VALIDATION_ID="f7e8d9c0-1a2b-3c4d-5e6f-7a8b9c0d1e2f"

curl -sS -X GET "$API/validations/$VALIDATION_ID" \
  -H "Authorization: Bearer $TOK" | jq .
```

**Expected Response** (200 OK):
```json
{
  "id": "f7e8d9c0-1a2b-3c4d-5e6f-7a8b9c0d1e2f",
  "target": "Structure",
  "status": "Passed",
  "reportUrl": "https://reports.interphase.ap-aero.portfolio/validations/f7e8d9c0-1a2b-3c4d-5e6f-7a8b9c0d1e2f",
  "startedAt": "2025-10-14T11:50:00Z",
  "completedAt": "2025-10-14T11:55:00Z"
}
```

---

## Clone Operations

### Clone Program from Snapshot

Create a new program by cloning a frozen context with parameter overrides:

```bash
curl -sS -X POST "$API/clones" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "snapshotId": "c9c1b4f0-5e0a-4b8c-9a21-6f6b0b3b5b5a",
    "targetName": "ampel360-bwb-q200",
    "params": {
      "wing_span_m": 45,
      "passenger_capacity": 350,
      "mtow_kg": 240000,
      "engines": 4
    },
    "tenant": "ampel-aerospace"
  }' | jq .
```

**Expected Response** (202 Accepted):
```json
{
  "id": "h9g0f1e2-3c4d-5e6f-7a8b-9c0d1e2f3g4h",
  "status": "Running",
  "targetProgramId": "ampel360-bwb-q200"
}
```

---

## Webhook Operations

### Register a Webhook

```bash
curl -sS -X POST "$API/webhooks/endpoints" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://webhook.example.com/pluma/events",
    "events": [
      "context.frozen",
      "gate.decision",
      "transition.succeeded",
      "transition.failed"
    ],
    "secret": "your-webhook-secret-key"
  }' | jq .
```

**Expected Response** (201 Created):
```json
{
  "id": "i0h1g2f3-4d5e-6f7a-8b9c-0d1e2f3g4h5i",
  "url": "https://webhook.example.com/pluma/events",
  "events": [
    "context.frozen",
    "gate.decision",
    "transition.succeeded",
    "transition.failed"
  ],
  "active": true
}
```

### List Webhooks

```bash
curl -sS -X GET "$API/webhooks/endpoints" \
  -H "Authorization: Bearer $TOK" | jq .
```

---

## Health Check

### Liveness Check

```bash
curl -sS -X GET "$API/healthz" -w "\nHTTP Status: %{http_code}\n"
```

**Expected Response** (204 No Content):
```
HTTP Status: 204
```

---

## Advanced Examples

### Complete Workflow: Freeze → Approve → Transition

```bash
#!/bin/bash
set -e

API="https://api.interphase.ap-aero.portfolio/v1"
TOK="your-oidc-bearer-token"
PROGRAM_ID="ampel360-bwb-q100"

# Step 1: Freeze CAD context
echo "==> Freezing CAD context..."
SNAPSHOT=$(curl -sS -X POST "$API/programs/$PROGRAM_ID/contexts/freeze" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "phase": "CAD",
    "gate": "CB",
    "manifestPath": "PLM/CAx/CAD/MANIFEST.csv"
  }')

SNAPSHOT_ID=$(echo "$SNAPSHOT" | jq -r '.id')
echo "Snapshot ID: $SNAPSHOT_ID"

# Step 2: Approve CAD gate
echo "==> Approving CAD gate..."
curl -sS -X POST "$API/programs/$PROGRAM_ID/phases/CAD/gates/CB/decision" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -d '{
    "decision": "Approve",
    "decidedBy": "ccb-179",
    "evidence": ["utcs://AIRCRAFT/AMPEL360-AIR-T/.../reports/validation-results.json"],
    "comment": "All checks passed"
  }' > /dev/null

echo "Gate approved"

# Step 3: Execute transition to CAE
echo "==> Transitioning to CAE..."
TRANSITION=$(curl -sS -X POST "$API/transitions" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "snapshotId": "'"$SNAPSHOT_ID"'",
    "to": {
      "phase": "CAE",
      "gate": "CB"
    }
  }')

TRANSITION_ID=$(echo "$TRANSITION" | jq -r '.id')
echo "Transition ID: $TRANSITION_ID"

# Step 4: Poll transition status
echo "==> Polling transition status..."
while true; do
  STATUS=$(curl -sS -X GET "$API/transitions/$TRANSITION_ID" \
    -H "Authorization: Bearer $TOK" | jq -r '.status')
  
  echo "Status: $STATUS"
  
  if [ "$STATUS" = "Succeeded" ]; then
    echo "==> Transition completed successfully!"
    break
  elif [ "$STATUS" = "Failed" ]; then
    echo "==> Transition failed!"
    exit 1
  fi
  
  sleep 5
done
```

### Batch Operations

```bash
# Run validations for multiple programs in parallel
PROGRAMS=("ampel360-bwb-q100" "gaia-quantum-sat" "ares-x-uas-swarm")

for prog in "${PROGRAMS[@]}"; do
  (
    curl -sS -X POST "$API/validations/run" \
      -H "Authorization: Bearer $TOK" \
      -H "Content-Type: application/json" \
      -H "Idempotency-Key: $(uuidgen)" \
      -d '{
        "utcs": "utcs://AIRCRAFT/'"$prog"'/CAD",
        "checks": ["Structure", "Links"]
      }' &
  )
done

wait
echo "All validations queued"
```

---

## Error Handling

### Handle 409 Conflict (Idempotency)

```bash
# First request
curl -sS -X POST "$API/programs/$PROGRAM_ID/contexts/freeze" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: freeze-cad-20251014" \
  -d '{"phase": "CAD", "gate": "CB"}'

# Retry with same idempotency key (safe)
curl -sS -X POST "$API/programs/$PROGRAM_ID/contexts/freeze" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: freeze-cad-20251014" \
  -d '{"phase": "CAD", "gate": "CB"}'
# Returns same result, no duplicate created
```

### Handle 422 Validation Failed

```bash
RESPONSE=$(curl -sS -X POST "$API/transitions" \
  -H "Authorization: Bearer $TOK" \
  -H "Content-Type: application/json" \
  -d '{
    "snapshotId": "invalid-snapshot",
    "to": {"phase": "CAE", "gate": "CB"}
  }')

ERROR_CODE=$(echo "$RESPONSE" | jq -r '.code')
if [ "$ERROR_CODE" = "validation_failed" ]; then
  echo "Validation failed:"
  echo "$RESPONSE" | jq -r '.details.errors[]'
fi
```

---

## Related Documentation

- [Interphase API Specification](./INTERPHASE_API_SPEC.yaml)
- [Interphase Event Contracts](./INTERPHASE_EVENT_CONTRACTS.md)
- [Interphase Data Model](./INTERPHASE_DATA_MODEL.sql)
- [PLUMA Integration Guide](../07-INTEGRATION/README.md)
