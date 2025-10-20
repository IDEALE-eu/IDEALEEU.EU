"""
Policy Layer for Workflow Orchestration

Converts SNN outputs into discrete workflow actions:
- Routing: Assign reviewers/approvers
- Prioritization: Set temporal scaling and SLAs
- Impact Analysis: Identify affected DMCs
- Guards: Block on BREX violations
- Explainability: Provide decision rationale
"""

import numpy as np
import torch
import torch.nn as nn
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class PolicyAction(Enum):
    """Workflow policy actions"""
    ROUTE = "route"
    PRIORITIZE = "prioritize"
    ANALYZE_IMPACT = "analyze_impact"
    GUARD = "guard"
    EXPLAIN = "explain"


@dataclass
class RoutingDecision:
    """Routing action output"""
    reviewers: List[str]
    sequence: List[int]  # Order of review
    confidence: float


@dataclass
class PriorityDecision:
    """Priority action output"""
    urgency_level: int  # 1-5
    suggested_sla_hours: float
    temporal_scaling: float  # Multiplier for time estimates
    confidence: float


@dataclass
class ImpactDecision:
    """Impact analysis output"""
    affected_dmcs: List[str]
    dependency_depth: int
    cascading_changes: bool
    confidence: float


@dataclass
class GuardDecision:
    """Guard action output"""
    should_block: bool
    violated_rules: List[str]
    risk_level: float  # 0.0 to 1.0
    reason: str


@dataclass
class ExplanationDecision:
    """Explanation output"""
    top_k_nodes: List[Tuple[str, float]]  # (node_id, contribution)
    top_k_edges: List[Tuple[str, str, float]]  # (source, target, contribution)
    spike_trace_summary: str
    decision_rationale: str


class PolicyLayer(nn.Module):
    """
    Policy layer that converts SNN outputs to discrete workflow actions
    """
    
    def __init__(
        self,
        hidden_dim: int,
        num_reviewers: int = 10,
        num_dmcs: int = 500
    ):
        super().__init__()
        
        self.hidden_dim = hidden_dim
        self.num_reviewers = num_reviewers
        self.num_dmcs = num_dmcs
        
        # Routing head
        self.route_head = nn.Sequential(
            nn.Linear(hidden_dim, 128),
            nn.ReLU(),
            nn.Linear(128, num_reviewers)
        )
        
        # Priority head
        self.priority_head = nn.Sequential(
            nn.Linear(hidden_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 5)  # 5 priority levels
        )
        
        # Impact analysis head
        self.impact_head = nn.Sequential(
            nn.Linear(hidden_dim, 128),
            nn.ReLU(),
            nn.Linear(128, num_dmcs)
        )
        
        # Guard head
        self.guard_head = nn.Sequential(
            nn.Linear(hidden_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )
        
    def forward(
        self,
        snn_output: torch.Tensor
    ) -> Dict[str, torch.Tensor]:
        """
        Convert SNN output to policy decisions
        
        Args:
            snn_output: Hidden state from SNN [batch_size, hidden_dim]
            
        Returns:
            Dict of policy outputs
        """
        outputs = {}
        
        # Routing probabilities
        outputs['routing'] = torch.softmax(self.route_head(snn_output), dim=-1)
        
        # Priority scores
        outputs['priority'] = torch.softmax(self.priority_head(snn_output), dim=-1)
        
        # Impact scores (which DMCs affected)
        outputs['impact'] = torch.sigmoid(self.impact_head(snn_output))
        
        # Guard score (should block?)
        outputs['guard'] = self.guard_head(snn_output)
        
        return outputs
    
    def decode_routing(
        self,
        routing_probs: torch.Tensor,
        reviewer_ids: List[str],
        top_k: int = 3
    ) -> RoutingDecision:
        """Decode routing probabilities into reviewer assignments"""
        probs = routing_probs.detach().cpu().numpy()
        
        # Get top-k reviewers
        top_indices = np.argsort(probs)[-top_k:][::-1]
        top_reviewers = [reviewer_ids[i] for i in top_indices]
        
        # Sequence is by probability (highest first)
        sequence = list(range(top_k))
        confidence = float(probs[top_indices[0]])
        
        return RoutingDecision(
            reviewers=top_reviewers,
            sequence=sequence,
            confidence=confidence
        )
    
    def decode_priority(
        self,
        priority_probs: torch.Tensor
    ) -> PriorityDecision:
        """Decode priority probabilities into SLA suggestion"""
        probs = priority_probs.detach().cpu().numpy()
        
        # Select priority level (1-5)
        urgency_level = int(np.argmax(probs)) + 1
        
        # Map to SLA hours (higher urgency = shorter SLA)
        sla_mapping = {1: 168, 2: 72, 3: 48, 4: 24, 5: 8}  # hours
        suggested_sla = sla_mapping[urgency_level]
        
        # Temporal scaling (higher urgency = faster processing)
        temporal_scaling = 1.0 / urgency_level
        
        confidence = float(probs[urgency_level - 1])
        
        return PriorityDecision(
            urgency_level=urgency_level,
            suggested_sla_hours=suggested_sla,
            temporal_scaling=temporal_scaling,
            confidence=confidence
        )
    
    def decode_impact(
        self,
        impact_scores: torch.Tensor,
        dmc_ids: List[str],
        threshold: float = 0.5
    ) -> ImpactDecision:
        """Decode impact scores into affected DMC list"""
        scores = impact_scores.detach().cpu().numpy()
        
        # Get DMCs above threshold
        affected_indices = np.where(scores > threshold)[0]
        affected_dmcs = [dmc_ids[i] for i in affected_indices]
        
        # Estimate dependency depth (simplified)
        dependency_depth = len(affected_dmcs) // 10 + 1
        
        # Cascading if many DMCs affected
        cascading_changes = len(affected_dmcs) > 10
        
        # Confidence is mean score of affected DMCs
        confidence = float(np.mean(scores[affected_indices])) if len(affected_indices) > 0 else 0.0
        
        return ImpactDecision(
            affected_dmcs=affected_dmcs,
            dependency_depth=dependency_depth,
            cascading_changes=cascading_changes,
            confidence=confidence
        )
    
    def decode_guard(
        self,
        guard_score: torch.Tensor,
        brex_violations: List[str]
    ) -> GuardDecision:
        """Decode guard score into block decision"""
        score = float(guard_score.detach().cpu().item())
        
        # Block if guard score high OR BREX violations exist
        should_block = score > 0.5 or len(brex_violations) > 0
        
        if len(brex_violations) > 0:
            reason = f"BREX violations: {', '.join(brex_violations)}"
            risk_level = 1.0
        elif score > 0.5:
            reason = f"SNN risk score: {score:.2f}"
            risk_level = score
        else:
            reason = "No blocking conditions"
            risk_level = score
        
        return GuardDecision(
            should_block=should_block,
            violated_rules=brex_violations,
            risk_level=risk_level,
            reason=reason
        )


class ExplainabilityEngine:
    """Generate explanations for policy decisions"""
    
    def __init__(self, graph, node_ids: List[str]):
        self.graph = graph
        self.node_ids = node_ids
        
    def explain_decision(
        self,
        snn_output: torch.Tensor,
        spike_traces: List[torch.Tensor],
        top_k: int = 5
    ) -> ExplanationDecision:
        """
        Generate explanation for decision
        
        Args:
            snn_output: SNN hidden state
            spike_traces: Recorded spike activity
            top_k: Number of top contributors to return
            
        Returns:
            Explanation with contributing nodes/edges
        """
        # Compute node contributions (simplified)
        # In real implementation, use attention mechanisms or integrated gradients
        node_contributions = {}
        
        output_np = snn_output.detach().cpu().numpy()
        for i, node_id in enumerate(self.node_ids[:len(output_np)]):
            contribution = float(abs(output_np[i]))
            node_contributions[node_id] = contribution
        
        # Get top-k nodes
        sorted_nodes = sorted(
            node_contributions.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_k]
        
        # Get top-k edges (from graph structure)
        top_edges = []
        for node_id, _ in sorted_nodes[:3]:
            if node_id in self.graph:
                for neighbor in list(self.graph.neighbors(node_id))[:2]:
                    edge_weight = self.graph[node_id][neighbor].get('weight', 1.0)
                    top_edges.append((node_id, neighbor, edge_weight))
        
        # Spike trace summary
        total_spikes = sum(t.sum().item() for t in spike_traces)
        spike_trace_summary = f"Total spikes: {int(total_spikes)} across {len(spike_traces)} timesteps"
        
        # Decision rationale
        top_node_names = [n for n, _ in sorted_nodes]
        decision_rationale = (
            f"Decision primarily influenced by nodes: {', '.join(top_node_names[:3])}. "
            f"Spike activity indicates {'high' if total_spikes > 100 else 'moderate'} urgency."
        )
        
        return ExplanationDecision(
            top_k_nodes=sorted_nodes,
            top_k_edges=top_edges,
            spike_trace_summary=spike_trace_summary,
            decision_rationale=decision_rationale
        )


if __name__ == "__main__":
    # Example usage
    print("Policy Layer for S1000D Orchestration")
    
    # Create policy layer
    policy = PolicyLayer(hidden_dim=256, num_reviewers=10, num_dmcs=500)
    
    # Dummy SNN output
    snn_output = torch.randn(1, 256)
    
    # Get policy outputs
    outputs = policy(snn_output)
    
    print("\nPolicy outputs:")
    print(f"  Routing shape: {outputs['routing'].shape}")
    print(f"  Priority shape: {outputs['priority'].shape}")
    print(f"  Impact shape: {outputs['impact'].shape}")
    print(f"  Guard shape: {outputs['guard'].shape}")
    
    # Decode example
    reviewer_ids = [f"reviewer_{i}" for i in range(10)]
    routing = policy.decode_routing(outputs['routing'][0], reviewer_ids)
    print(f"\nRouting decision: {routing.reviewers[:3]}")
    print(f"  Confidence: {routing.confidence:.2f}")
