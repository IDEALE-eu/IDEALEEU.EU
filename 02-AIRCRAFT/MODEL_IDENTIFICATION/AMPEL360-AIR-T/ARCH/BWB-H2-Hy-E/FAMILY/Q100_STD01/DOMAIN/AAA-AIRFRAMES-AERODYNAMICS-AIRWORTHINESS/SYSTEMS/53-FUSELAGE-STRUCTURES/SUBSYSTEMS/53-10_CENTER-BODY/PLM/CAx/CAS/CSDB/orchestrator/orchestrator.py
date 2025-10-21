#!/usr/bin/env python3
"""
S1000D Neuromorphic Workflow Orchestrator - Main Entry Point

Integrates all components:
- CSDB event listener
- AER encoder
- Spiking GNN
- Policy layer
- Workflow orchestrator interface
"""

import argparse
import logging
import yaml
import torch
from pathlib import Path
from typing import Optional

from graph_builder import CSDBGraphBuilder
from aer_encoder import AEREncoder, create_node_mapping, parse_csdb_event_log
from snn_core import create_default_snn, STDPLearning
from policy_layer import PolicyLayer, ExplainabilityEngine


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class S1000DOrchestrator:
    """Main orchestrator class"""
    
    def __init__(self, config_path: str):
        """Initialize orchestrator with configuration"""
        logger.info(f"Loading configuration from {config_path}")
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.graph = None
        self.snn_model = None
        self.policy_layer = None
        self.aer_encoder = None
        self.explainability = None
        
    def build_graph(self, csdb_path: Optional[str] = None):
        """Build CSDB graph"""
        csdb_path = csdb_path or self.config['csdb']['root_path']
        logger.info(f"Building CSDB graph from {csdb_path}")
        
        builder = CSDBGraphBuilder(csdb_path)
        self.graph = builder.build_graph()
        
        logger.info(f"Graph built: {self.graph.number_of_nodes()} nodes, "
                   f"{self.graph.number_of_edges()} edges")
        
        return self.graph
    
    def initialize_models(self):
        """Initialize SNN and policy layer"""
        logger.info("Initializing neural models...")
        
        num_nodes = self.graph.number_of_nodes() if self.graph else 500
        
        # Create SNN
        self.snn_model = create_default_snn(num_csdb_nodes=num_nodes)
        logger.info(f"SNN created with {sum(p.numel() for p in self.snn_model.parameters())} parameters")
        
        # Create policy layer
        hidden_dim = self.config['snn']['hidden_dim']
        self.policy_layer = PolicyLayer(hidden_dim=hidden_dim)
        logger.info("Policy layer initialized")
        
        # Create AER encoder
        node_ids = list(self.graph.nodes()) if self.graph else []
        node_mapping = create_node_mapping(node_ids)
        self.aer_encoder = AEREncoder(
            node_mapping=node_mapping,
            window_size_ms=self.config['aer']['window_size_ms']
        )
        logger.info(f"AER encoder initialized for {len(node_mapping)} nodes")
        
        # Create explainability engine
        self.explainability = ExplainabilityEngine(
            graph=self.graph,
            node_ids=node_ids
        )
        logger.info("Explainability engine initialized")
        
    def load_model(self, checkpoint_path: str):
        """Load trained model from checkpoint"""
        logger.info(f"Loading model from {checkpoint_path}")
        
        checkpoint = torch.load(checkpoint_path)
        self.snn_model.load_state_dict(checkpoint['snn_state_dict'])
        self.policy_layer.load_state_dict(checkpoint['policy_state_dict'])
        
        logger.info(f"Model loaded (epoch {checkpoint.get('epoch', 'unknown')})")
        
    def process_event(self, event):
        """Process single CSDB event through the pipeline"""
        # Encode event to spikes
        spikes = self.aer_encoder.encode_event(event)
        
        # Convert to tensor
        spike_tensor = torch.zeros(len(self.aer_encoder.node_mapping))
        for spike in spikes:
            if 0 <= spike.address < len(spike_tensor):
                spike_tensor[spike.address] = spike.intensity
        
        # Run through SNN
        spike_tensor = spike_tensor.unsqueeze(0)  # Add batch dim
        snn_output, spike_traces = self.snn_model(spike_tensor, num_steps=100)
        
        # Get policy decisions
        policy_outputs = self.policy_layer(snn_output)
        
        # Decode decisions
        node_ids = list(self.aer_encoder.node_mapping.keys())
        
        routing = self.policy_layer.decode_routing(
            policy_outputs['routing'][0],
            reviewer_ids=[f"reviewer_{i}" for i in range(10)]
        )
        
        priority = self.policy_layer.decode_priority(
            policy_outputs['priority'][0]
        )
        
        impact = self.policy_layer.decode_impact(
            policy_outputs['impact'][0],
            dmc_ids=node_ids
        )
        
        guard = self.policy_layer.decode_guard(
            policy_outputs['guard'][0],
            brex_violations=[]  # Would check BREX in real implementation
        )
        
        explanation = self.explainability.explain_decision(
            snn_output[0],
            spike_traces
        )
        
        return {
            'routing': routing,
            'priority': priority,
            'impact': impact,
            'guard': guard,
            'explanation': explanation
        }
    
    def run_shadow_mode(self, event_log_path: str):
        """Run in shadow mode (compare with baseline)"""
        logger.info(f"Running shadow mode on {event_log_path}")
        
        events = parse_csdb_event_log(event_log_path)
        logger.info(f"Loaded {len(events)} events")
        
        results = []
        for i, event in enumerate(events[:100]):  # Limit for demo
            if i % 10 == 0:
                logger.info(f"Processing event {i}/{len(events[:100])}")
            
            decision = self.process_event(event)
            results.append({
                'event': event,
                'decision': decision
            })
        
        logger.info(f"Shadow mode complete: {len(results)} events processed")
        return results
    
    def start_realtime(self):
        """Start real-time event processing"""
        logger.info("Starting real-time orchestrator...")
        logger.info("  Mode: " + self.config['policy']['mode'])
        logger.info("  CSDB URL: " + self.config['csdb']['event_stream_url'])
        
        # This would connect to CSDB event stream
        # For now, just a placeholder
        logger.info("Real-time mode not yet implemented")
        logger.info("Use shadow mode for testing: --mode shadow --events <log_file>")


def main():
    parser = argparse.ArgumentParser(
        description="S1000D Neuromorphic Workflow Orchestrator"
    )
    
    parser.add_argument(
        '--config',
        type=str,
        default='config.yaml',
        help='Configuration file path'
    )
    
    parser.add_argument(
        '--mode',
        type=str,
        choices=['shadow', 'realtime', 'train'],
        default='shadow',
        help='Operating mode'
    )
    
    parser.add_argument(
        '--csdb-path',
        type=str,
        help='Path to CSDB root directory'
    )
    
    parser.add_argument(
        '--events',
        type=str,
        help='Path to event log file (for shadow mode)'
    )
    
    parser.add_argument(
        '--checkpoint',
        type=str,
        help='Path to model checkpoint'
    )
    
    args = parser.parse_args()
    
    # Create orchestrator
    orchestrator = S1000DOrchestrator(args.config)
    
    # Build graph
    orchestrator.build_graph(args.csdb_path)
    
    # Initialize models
    orchestrator.initialize_models()
    
    # Load checkpoint if provided
    if args.checkpoint:
        orchestrator.load_model(args.checkpoint)
    
    # Run based on mode
    if args.mode == 'shadow':
        if not args.events:
            logger.error("--events required for shadow mode")
            return 1
        
        results = orchestrator.run_shadow_mode(args.events)
        
        # Print sample results
        logger.info("\nSample decision:")
        sample = results[0]
        logger.info(f"  Event: {sample['event'].event_type.value} on {sample['event'].dmc}")
        logger.info(f"  Routing: {sample['decision']['routing'].reviewers}")
        logger.info(f"  Priority: Level {sample['decision']['priority'].urgency_level} "
                   f"(SLA: {sample['decision']['priority'].suggested_sla_hours}h)")
        logger.info(f"  Impact: {len(sample['decision']['impact'].affected_dmcs)} DMCs affected")
        logger.info(f"  Guard: {'BLOCKED' if sample['decision']['guard'].should_block else 'ALLOWED'}")
        
    elif args.mode == 'realtime':
        orchestrator.start_realtime()
        
    elif args.mode == 'train':
        logger.info("Training mode not yet implemented")
        logger.info("Use external training script")
    
    return 0


if __name__ == "__main__":
    exit(main())
