"""
Spiking Neural Network Core Implementation

Implements Leaky Integrate-and-Fire (LIF) neurons with STDP learning
for S1000D workflow orchestration.
"""

import numpy as np
import torch
import torch.nn as nn
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class LIFConfig:
    """Configuration for LIF neurons"""
    v_rest: float = -70.0  # Resting potential (mV)
    v_reset: float = -75.0  # Reset potential after spike (mV)
    v_thresh: float = -55.0  # Spike threshold (mV)
    tau_mem: float = 20.0  # Membrane time constant (ms)
    tau_syn: float = 5.0  # Synaptic time constant (ms)
    refractory_period: float = 2.0  # Refractory period (ms)
    dt: float = 1.0  # Time step (ms)


class LIFNeuron(nn.Module):
    """Leaky Integrate-and-Fire neuron model"""
    
    def __init__(self, config: LIFConfig):
        super().__init__()
        self.config = config
        self.reset_state()
        
    def reset_state(self):
        """Reset neuron state"""
        self.v_mem = self.config.v_rest
        self.i_syn = 0.0
        self.refractory_counter = 0.0
        
    def forward(self, i_input: float) -> Tuple[float, bool]:
        """
        Simulate one time step
        
        Args:
            i_input: Input current
            
        Returns:
            (membrane_voltage, spike_occurred)
        """
        # Update refractory period
        if self.refractory_counter > 0:
            self.refractory_counter -= self.config.dt
            return self.v_mem, False
        
        # Synaptic current decay
        self.i_syn += (-self.i_syn / self.config.tau_syn + i_input) * self.config.dt
        
        # Membrane potential integration
        dv = (-(self.v_mem - self.config.v_rest) + self.i_syn) / self.config.tau_mem
        self.v_mem += dv * self.config.dt
        
        # Spike detection
        if self.v_mem >= self.config.v_thresh:
            self.v_mem = self.config.v_reset
            self.refractory_counter = self.config.refractory_period
            return self.v_mem, True
            
        return self.v_mem, False


class SpikingGNN(nn.Module):
    """
    Spiking Graph Neural Network for CSDB workflow orchestration
    
    Architecture:
    - Input layer: CSDB events (encoded as spikes)
    - Hidden layers: LIF neurons arranged by graph structure
    - Output layer: Policy decisions (routing, priority, impact)
    """
    
    def __init__(
        self,
        num_nodes: int,
        hidden_dim: int = 256,
        num_layers: int = 3,
        lif_config: Optional[LIFConfig] = None
    ):
        super().__init__()
        
        self.num_nodes = num_nodes
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.lif_config = lif_config or LIFConfig()
        
        # Graph connectivity (learned)
        self.adjacency = nn.Parameter(
            torch.randn(num_nodes, num_nodes) * 0.01
        )
        
        # Hidden layer weights
        self.layers = nn.ModuleList([
            nn.Linear(num_nodes if i == 0 else hidden_dim, hidden_dim)
            for i in range(num_layers)
        ])
        
        # Output layer for policy decisions
        self.policy_head = nn.Linear(hidden_dim, 5)  # 5 policy actions
        
        # LIF neurons for each layer
        self.lif_neurons = nn.ModuleList([
            nn.ModuleList([LIFNeuron(self.lif_config) for _ in range(hidden_dim)])
            for _ in range(num_layers)
        ])
        
    def reset_neurons(self):
        """Reset all neuron states"""
        for layer in self.lif_neurons:
            for neuron in layer:
                neuron.reset_state()
                
    def forward(
        self,
        node_spikes: torch.Tensor,
        num_steps: int = 100
    ) -> Tuple[torch.Tensor, List[torch.Tensor]]:
        """
        Forward pass through spiking GNN
        
        Args:
            node_spikes: Initial spike input [num_nodes]
            num_steps: Number of simulation timesteps
            
        Returns:
            (policy_logits, spike_traces)
        """
        batch_size = node_spikes.shape[0]
        device = node_spikes.device
        
        # Track spikes over time
        spike_traces = []
        
        # Initialize hidden state
        hidden = torch.zeros(batch_size, self.hidden_dim, device=device)
        
        # Simulate for num_steps timesteps
        for t in range(num_steps):
            layer_spikes = []
            
            # Input layer: propagate through graph
            graph_input = torch.matmul(node_spikes, self.adjacency)
            
            # Process through layers
            x = graph_input
            for layer_idx, (linear, neurons) in enumerate(
                zip(self.layers, self.lif_neurons)
            ):
                # Linear transformation
                x = linear(x)
                
                # LIF neuron dynamics
                layer_spike = torch.zeros(batch_size, self.hidden_dim, device=device)
                for neuron_idx, neuron in enumerate(neurons):
                    # Simplified batched neuron update
                    i_input = x[:, neuron_idx]
                    # Note: This is simplified; proper implementation would
                    # handle batch processing more efficiently
                    for b in range(batch_size):
                        v, spike = neuron(i_input[b].item())
                        layer_spike[b, neuron_idx] = float(spike)
                
                x = layer_spike
                layer_spikes.append(layer_spike)
            
            # Accumulate spikes
            hidden += x
            spike_traces.append(x)
            
        # Policy head on accumulated spikes
        policy_logits = self.policy_head(hidden / num_steps)
        
        return policy_logits, spike_traces


class STDPLearning:
    """
    Spike-Timing-Dependent Plasticity learning rule
    
    Implements: Δw_ij = η·(pre∘post - α·w_ij) · r(t)
    """
    
    def __init__(
        self,
        learning_rate: float = 0.001,
        decay_rate: float = 0.01,
        tau_plus: float = 20.0,  # STDP time constant for potentiation
        tau_minus: float = 20.0,  # STDP time constant for depression
    ):
        self.learning_rate = learning_rate
        self.decay_rate = decay_rate
        self.tau_plus = tau_plus
        self.tau_minus = tau_minus
        
    def compute_weight_update(
        self,
        pre_spike_times: np.ndarray,
        post_spike_times: np.ndarray,
        current_weight: float,
        reward: float
    ) -> float:
        """
        Compute weight update based on spike timing
        
        Args:
            pre_spike_times: Presynaptic spike times
            post_spike_times: Postsynaptic spike times
            current_weight: Current synaptic weight
            reward: Reward signal r(t)
            
        Returns:
            Weight update Δw
        """
        delta_w = 0.0
        
        # Compute all-to-all spike pair interactions
        for t_pre in pre_spike_times:
            for t_post in post_spike_times:
                dt = t_post - t_pre
                
                if dt > 0:
                    # Potentiation (post after pre)
                    delta_w += np.exp(-dt / self.tau_plus)
                else:
                    # Depression (pre after post)
                    delta_w -= np.exp(dt / self.tau_minus)
        
        # Weight decay term
        decay = -self.decay_rate * current_weight
        
        # Reward modulation
        delta_w = self.learning_rate * (delta_w + decay) * reward
        
        return delta_w
    
    def update_weights(
        self,
        model: SpikingGNN,
        spike_traces: List[torch.Tensor],
        reward: float
    ):
        """
        Update model weights based on STDP and reward
        
        Args:
            model: Spiking GNN model
            spike_traces: Recorded spike traces
            reward: Reward signal (e.g., cycle time reduction)
        """
        # Extract spike times from traces
        # This is a simplified version; full implementation would
        # track precise spike timing for each synapse
        
        with torch.no_grad():
            for param in model.parameters():
                if param.requires_grad:
                    # Simple reward-modulated update
                    # Real STDP would use precise spike timing
                    gradient = torch.randn_like(param) * 0.01  # Placeholder
                    param.data += self.learning_rate * gradient * reward


def create_default_snn(num_csdb_nodes: int) -> SpikingGNN:
    """
    Create SNN with default configuration for S1000D orchestration
    
    Args:
        num_csdb_nodes: Number of nodes in CSDB graph (DMCs, etc.)
        
    Returns:
        Configured SpikingGNN model
    """
    lif_config = LIFConfig(
        v_rest=-70.0,
        v_reset=-75.0,
        v_thresh=-55.0,
        tau_mem=20.0,
        tau_syn=5.0,
        refractory_period=2.0,
        dt=1.0
    )
    
    model = SpikingGNN(
        num_nodes=num_csdb_nodes,
        hidden_dim=256,
        num_layers=3,
        lif_config=lif_config
    )
    
    return model


if __name__ == "__main__":
    # Example usage
    print("Creating Spiking GNN for S1000D orchestration...")
    
    # Assume 500 DMCs in CSDB
    model = create_default_snn(num_csdb_nodes=500)
    
    print(f"Model created with {sum(p.numel() for p in model.parameters())} parameters")
    print(f"Graph connectivity: {model.adjacency.shape}")
    print(f"Ready for training on workflow logs")
