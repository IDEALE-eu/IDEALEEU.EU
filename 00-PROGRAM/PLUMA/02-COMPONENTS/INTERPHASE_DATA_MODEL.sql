-- Interphase API - Data Model (SQL)
-- PostgreSQL schema for PLUMA Interphase component
-- Version: 1.0
-- Date: 2025-10-14

-- ============================================================================
-- TABLES
-- ============================================================================

-- Programs table
-- Stores all programs managed by PLUMA
CREATE TABLE programs (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    utcs TEXT NOT NULL,
    tenant TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Active', 'Frozen', 'Archived')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    metadata JSONB DEFAULT '{}'::JSONB
);

-- Context snapshots table
-- Stores frozen context snapshots at phase/gate boundaries
CREATE TABLE context_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    program_id TEXT NOT NULL REFERENCES programs(id) ON DELETE CASCADE,
    phase TEXT NOT NULL CHECK (phase IN ('CAD', 'CAE', 'CAI', 'CAO', 'CAM', 'CAP', 'CAV', 'CMP', 'CAS')),
    gate TEXT NOT NULL CHECK (gate IN ('QS', 'FWD', 'UE', 'FE', 'CB', 'QB')),
    utcs TEXT NOT NULL,
    checksum TEXT NOT NULL,
    frozen_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    manifest_path TEXT,
    artifact_count INTEGER,
    size_bytes BIGINT,
    comment TEXT,
    metadata JSONB DEFAULT '{}'::JSONB,
    
    -- Ensure one snapshot per program/phase/gate combination
    UNIQUE (program_id, phase, gate)
);

-- Gate decisions table
-- Records approval/rejection/hold decisions for phase gates
CREATE TABLE gate_decisions (
    program_id TEXT NOT NULL REFERENCES programs(id) ON DELETE CASCADE,
    phase TEXT NOT NULL CHECK (phase IN ('CAD', 'CAE', 'CAI', 'CAO', 'CAM', 'CAP', 'CAV', 'CMP', 'CAS')),
    gate TEXT NOT NULL CHECK (gate IN ('QS', 'FWD', 'UE', 'FE', 'CB', 'QB')),
    decision TEXT NOT NULL CHECK (decision IN ('Approve', 'Reject', 'Hold')),
    decided_by TEXT NOT NULL,
    decided_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    evidence JSONB NOT NULL DEFAULT '[]'::JSONB,
    comment TEXT,
    metadata JSONB DEFAULT '{}'::JSONB,
    
    -- One decision per program/phase/gate
    PRIMARY KEY (program_id, phase, gate)
);

-- Transitions table
-- Tracks phase/gate transitions
CREATE TABLE transitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    snapshot_id UUID NOT NULL REFERENCES context_snapshots(id) ON DELETE RESTRICT,
    from_phase TEXT NOT NULL CHECK (from_phase IN ('CAD', 'CAE', 'CAI', 'CAO', 'CAM', 'CAP', 'CAV', 'CMP', 'CAS')),
    from_gate TEXT NOT NULL CHECK (from_gate IN ('QS', 'FWD', 'UE', 'FE', 'CB', 'QB')),
    to_phase TEXT NOT NULL CHECK (to_phase IN ('CAD', 'CAE', 'CAI', 'CAO', 'CAM', 'CAP', 'CAV', 'CMP', 'CAS')),
    to_gate TEXT NOT NULL CHECK (to_gate IN ('QS', 'FWD', 'UE', 'FE', 'CB', 'QB')),
    status TEXT NOT NULL CHECK (status IN ('Planned', 'Running', 'Succeeded', 'Failed')),
    started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    finished_at TIMESTAMPTZ,
    error_message TEXT,
    metadata JSONB DEFAULT '{}'::JSONB
);

-- Validation runs table
-- Stores validation execution records
CREATE TABLE validation_runs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    utcs TEXT NOT NULL,
    target TEXT NOT NULL CHECK (target IN ('Structure', 'Links', 'Schema', 'KPIs')),
    status TEXT NOT NULL CHECK (status IN ('Queued', 'Running', 'Passed', 'Failed')),
    started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    report_url TEXT,
    errors JSONB DEFAULT '[]'::JSONB,
    metadata JSONB DEFAULT '{}'::JSONB
);

-- Clone operations table
-- Tracks program cloning operations
CREATE TABLE clone_operations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    snapshot_id UUID NOT NULL REFERENCES context_snapshots(id) ON DELETE RESTRICT,
    target_program_id TEXT NOT NULL,
    target_name TEXT NOT NULL,
    params JSONB NOT NULL,
    tenant TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Queued', 'Running', 'Succeeded', 'Failed')),
    started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    finished_at TIMESTAMPTZ,
    error_message TEXT,
    metadata JSONB DEFAULT '{}'::JSONB
);

-- Webhook endpoints table
-- Stores registered webhook endpoints for event notifications
CREATE TABLE webhook_endpoints (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant TEXT NOT NULL,
    url TEXT NOT NULL,
    events TEXT[] NOT NULL,
    secret_hash TEXT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_delivery_at TIMESTAMPTZ,
    failure_count INTEGER NOT NULL DEFAULT 0,
    metadata JSONB DEFAULT '{}'::JSONB,
    
    -- Ensure unique URL per tenant
    UNIQUE (tenant, url)
);

-- Event log table
-- Audit trail of all events published
CREATE TABLE event_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id UUID NOT NULL UNIQUE,
    event_type TEXT NOT NULL,
    program_id TEXT REFERENCES programs(id) ON DELETE SET NULL,
    phase TEXT,
    gate TEXT,
    snapshot_id UUID REFERENCES context_snapshots(id) ON DELETE SET NULL,
    utcs TEXT,
    occurred_at TIMESTAMPTZ NOT NULL,
    evidence JSONB DEFAULT '[]'::JSONB,
    metadata JSONB DEFAULT '{}'::JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================================
-- INDEXES
-- ============================================================================

-- Programs
CREATE INDEX idx_programs_tenant ON programs(tenant);
CREATE INDEX idx_programs_status ON programs(status);
CREATE INDEX idx_programs_created_at ON programs(created_at DESC);

-- Context snapshots
CREATE INDEX idx_context_snapshots_program_id ON context_snapshots(program_id);
CREATE INDEX idx_context_snapshots_phase_gate ON context_snapshots(phase, gate);
CREATE INDEX idx_context_snapshots_frozen_at ON context_snapshots(frozen_at DESC);
CREATE INDEX idx_context_snapshots_utcs ON context_snapshots(utcs);

-- Gate decisions
CREATE INDEX idx_gate_decisions_program_id ON gate_decisions(program_id);
CREATE INDEX idx_gate_decisions_decided_at ON gate_decisions(decided_at DESC);
CREATE INDEX idx_gate_decisions_decision ON gate_decisions(decision);

-- Transitions
CREATE INDEX idx_transitions_snapshot_id ON transitions(snapshot_id);
CREATE INDEX idx_transitions_status ON transitions(status);
CREATE INDEX idx_transitions_started_at ON transitions(started_at DESC);
CREATE INDEX idx_transitions_from_to ON transitions(from_phase, from_gate, to_phase, to_gate);

-- Validation runs
CREATE INDEX idx_validation_runs_utcs ON validation_runs(utcs);
CREATE INDEX idx_validation_runs_status ON validation_runs(status);
CREATE INDEX idx_validation_runs_started_at ON validation_runs(started_at DESC);
CREATE INDEX idx_validation_runs_target ON validation_runs(target);

-- Clone operations
CREATE INDEX idx_clone_operations_snapshot_id ON clone_operations(snapshot_id);
CREATE INDEX idx_clone_operations_target_program_id ON clone_operations(target_program_id);
CREATE INDEX idx_clone_operations_status ON clone_operations(status);
CREATE INDEX idx_clone_operations_started_at ON clone_operations(started_at DESC);

-- Webhook endpoints
CREATE INDEX idx_webhook_endpoints_tenant ON webhook_endpoints(tenant);
CREATE INDEX idx_webhook_endpoints_active ON webhook_endpoints(active);

-- Event log
CREATE INDEX idx_event_log_program_id ON event_log(program_id);
CREATE INDEX idx_event_log_event_type ON event_log(event_type);
CREATE INDEX idx_event_log_occurred_at ON event_log(occurred_at DESC);
CREATE INDEX idx_event_log_snapshot_id ON event_log(snapshot_id);

-- ============================================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- ============================================================================

-- Enable RLS on all tables
ALTER TABLE programs ENABLE ROW LEVEL SECURITY;
ALTER TABLE context_snapshots ENABLE ROW LEVEL SECURITY;
ALTER TABLE gate_decisions ENABLE ROW LEVEL SECURITY;
ALTER TABLE transitions ENABLE ROW LEVEL SECURITY;
ALTER TABLE validation_runs ENABLE ROW LEVEL SECURITY;
ALTER TABLE clone_operations ENABLE ROW LEVEL SECURITY;
ALTER TABLE webhook_endpoints ENABLE ROW LEVEL SECURITY;
ALTER TABLE event_log ENABLE ROW LEVEL SECURITY;

-- Policy: Users can only access data from their tenant
CREATE POLICY tenant_isolation_programs ON programs
    FOR ALL
    USING (tenant = current_setting('app.current_tenant')::TEXT);

CREATE POLICY tenant_isolation_context_snapshots ON context_snapshots
    FOR ALL
    USING (
        EXISTS (
            SELECT 1 FROM programs
            WHERE programs.id = context_snapshots.program_id
            AND programs.tenant = current_setting('app.current_tenant')::TEXT
        )
    );

CREATE POLICY tenant_isolation_gate_decisions ON gate_decisions
    FOR ALL
    USING (
        EXISTS (
            SELECT 1 FROM programs
            WHERE programs.id = gate_decisions.program_id
            AND programs.tenant = current_setting('app.current_tenant')::TEXT
        )
    );

CREATE POLICY tenant_isolation_transitions ON transitions
    FOR ALL
    USING (
        EXISTS (
            SELECT 1 FROM context_snapshots
            JOIN programs ON programs.id = context_snapshots.program_id
            WHERE context_snapshots.id = transitions.snapshot_id
            AND programs.tenant = current_setting('app.current_tenant')::TEXT
        )
    );

CREATE POLICY tenant_isolation_clone_operations ON clone_operations
    FOR ALL
    USING (tenant = current_setting('app.current_tenant')::TEXT);

CREATE POLICY tenant_isolation_webhook_endpoints ON webhook_endpoints
    FOR ALL
    USING (tenant = current_setting('app.current_tenant')::TEXT);

CREATE POLICY tenant_isolation_event_log ON event_log
    FOR ALL
    USING (
        program_id IS NULL OR
        EXISTS (
            SELECT 1 FROM programs
            WHERE programs.id = event_log.program_id
            AND programs.tenant = current_setting('app.current_tenant')::TEXT
        )
    );

-- ============================================================================
-- FUNCTIONS & TRIGGERS
-- ============================================================================

-- Function: Update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger: Auto-update updated_at for programs
CREATE TRIGGER update_programs_updated_at
    BEFORE UPDATE ON programs
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Trigger: Auto-update updated_at for webhook_endpoints
CREATE TRIGGER update_webhook_endpoints_updated_at
    BEFORE UPDATE ON webhook_endpoints
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Function: Validate phase transition sequence
CREATE OR REPLACE FUNCTION validate_phase_transition()
RETURNS TRIGGER AS $$
DECLARE
    valid_transitions TEXT[][] := ARRAY[
        ARRAY['CAD', 'CAE'],
        ARRAY['CAE', 'CAI'],
        ARRAY['CAI', 'CAO'],
        ARRAY['CAO', 'CAM'],
        ARRAY['CAM', 'CAP'],
        ARRAY['CAP', 'CAV'],
        ARRAY['CAV', 'CMP'],
        ARRAY['CMP', 'CAS']
    ];
    is_valid BOOLEAN := FALSE;
    transition TEXT[];
BEGIN
    -- Check if transition is in valid list
    FOREACH transition SLICE 1 IN ARRAY valid_transitions
    LOOP
        IF NEW.from_phase = transition[1] AND NEW.to_phase = transition[2] THEN
            is_valid := TRUE;
            EXIT;
        END IF;
    END LOOP;
    
    -- Allow same phase transitions (gate changes)
    IF NEW.from_phase = NEW.to_phase THEN
        is_valid := TRUE;
    END IF;
    
    IF NOT is_valid THEN
        RAISE EXCEPTION 'Invalid phase transition: % -> %', NEW.from_phase, NEW.to_phase;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger: Validate transitions before insert
CREATE TRIGGER validate_transition_before_insert
    BEFORE INSERT ON transitions
    FOR EACH ROW
    EXECUTE FUNCTION validate_phase_transition();

-- Function: Log events automatically
CREATE OR REPLACE FUNCTION log_event(
    p_event_type TEXT,
    p_program_id TEXT,
    p_phase TEXT,
    p_gate TEXT,
    p_snapshot_id UUID,
    p_utcs TEXT,
    p_evidence JSONB,
    p_metadata JSONB
)
RETURNS UUID AS $$
DECLARE
    v_event_id UUID;
BEGIN
    v_event_id := gen_random_uuid();
    
    INSERT INTO event_log (
        event_id, event_type, program_id, phase, gate,
        snapshot_id, utcs, occurred_at, evidence, metadata
    ) VALUES (
        v_event_id, p_event_type, p_program_id, p_phase, p_gate,
        p_snapshot_id, p_utcs, NOW(), p_evidence, p_metadata
    );
    
    RETURN v_event_id;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- VIEWS
-- ============================================================================

-- View: Active transitions with program details
CREATE VIEW active_transitions AS
SELECT
    t.id,
    t.snapshot_id,
    t.from_phase,
    t.from_gate,
    t.to_phase,
    t.to_gate,
    t.status,
    t.started_at,
    t.finished_at,
    p.id AS program_id,
    p.name AS program_name,
    p.tenant,
    cs.utcs AS snapshot_utcs
FROM transitions t
JOIN context_snapshots cs ON cs.id = t.snapshot_id
JOIN programs p ON p.id = cs.program_id
WHERE t.status IN ('Planned', 'Running');

-- View: Recent gate decisions
CREATE VIEW recent_gate_decisions AS
SELECT
    gd.program_id,
    p.name AS program_name,
    p.tenant,
    gd.phase,
    gd.gate,
    gd.decision,
    gd.decided_by,
    gd.decided_at,
    gd.comment
FROM gate_decisions gd
JOIN programs p ON p.id = gd.program_id
ORDER BY gd.decided_at DESC;

-- View: Program health summary
CREATE VIEW program_health_summary AS
SELECT
    p.id AS program_id,
    p.name AS program_name,
    p.tenant,
    p.status AS program_status,
    COUNT(DISTINCT cs.id) AS snapshot_count,
    COUNT(DISTINCT gd.phase || '-' || gd.gate) AS gate_decisions_count,
    MAX(cs.frozen_at) AS last_snapshot_at,
    MAX(gd.decided_at) AS last_decision_at
FROM programs p
LEFT JOIN context_snapshots cs ON cs.program_id = p.id
LEFT JOIN gate_decisions gd ON gd.program_id = p.id
GROUP BY p.id, p.name, p.tenant, p.status;

-- ============================================================================
-- SAMPLE QUERIES
-- ============================================================================

-- Query: Find all frozen contexts for a program
-- SELECT * FROM context_snapshots WHERE program_id = 'ampel360-bwb-q100' ORDER BY frozen_at DESC;

-- Query: Get transition history for a program
-- SELECT t.*, p.name FROM transitions t
-- JOIN context_snapshots cs ON cs.id = t.snapshot_id
-- JOIN programs p ON p.id = cs.program_id
-- WHERE p.id = 'ampel360-bwb-q100'
-- ORDER BY t.started_at DESC;

-- Query: Find pending validations
-- SELECT * FROM validation_runs WHERE status IN ('Queued', 'Running') ORDER BY started_at;

-- Query: Get gate decisions requiring action
-- SELECT * FROM gate_decisions WHERE decision = 'Hold' ORDER BY decided_at DESC;

-- Query: Find failed transitions in last 24 hours
-- SELECT * FROM transitions WHERE status = 'Failed' AND started_at > NOW() - INTERVAL '24 hours';

-- ============================================================================
-- COMMENTS
-- ============================================================================

COMMENT ON TABLE programs IS 'All programs managed by PLUMA platform';
COMMENT ON TABLE context_snapshots IS 'Immutable snapshots of program state at phase/gate boundaries';
COMMENT ON TABLE gate_decisions IS 'Phase gate approval/rejection/hold decisions';
COMMENT ON TABLE transitions IS 'Phase/gate transition execution records';
COMMENT ON TABLE validation_runs IS 'Validation check execution records';
COMMENT ON TABLE clone_operations IS 'Program cloning operation tracking';
COMMENT ON TABLE webhook_endpoints IS 'Registered webhook endpoints for event notifications';
COMMENT ON TABLE event_log IS 'Audit trail of all published events';

-- ============================================================================
-- GRANTS
-- ============================================================================

-- Grant permissions to application role
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO interphase_app;
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO interphase_app;
-- GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO interphase_app;

-- Grant read-only permissions to analytics role
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO interphase_analytics;

-- ============================================================================
-- END OF SCHEMA
-- ============================================================================
