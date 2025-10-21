"""
Address-Event Representation (AER) Encoder for CSDB Events

Converts CSDB events (CRUD operations, validations, workflow changes) 
into spike trains for the Spiking Neural Network.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import time


class EventType(Enum):
    """CSDB event types"""
    CREATE = "create"
    EDIT = "edit"
    VALIDATE = "validate"
    VALIDATION_FAIL = "validation_fail"
    DEPENDENCY_CHANGE = "dependency_change"
    PUBLICATION_REQUEST = "publication_request"
    EFFECTIVITY_CHANGE = "effectivity_change"
    QA_RETURN = "qa_return"
    APPROVE = "approve"
    REJECT = "reject"


@dataclass
class CSDBEvent:
    """CSDB event structure"""
    event_id: str
    event_type: EventType
    dmc: str  # Data Module Code
    timestamp: float
    urgency: float  # 0.0 to 1.0
    criticality: float  # 0.0 to 1.0
    affected_nodes: List[str]  # DMCs, illustrations, etc.
    metadata: Dict


@dataclass
class AERSpike:
    """Address-Event Representation spike"""
    address: int  # Node address in graph
    timestamp: float  # Spike time
    intensity: float  # Spike intensity (0.0 to 1.0)


class AEREncoder:
    """
    Encodes CSDB events into Address-Event Representation spikes
    
    Encoding strategies:
    - Time-to-first-spike: Urgency/criticality → earlier spikes
    - Population coding: Event type → different neuron populations
    - Rate coding: Intensity → spike frequency
    - Windowing: Burst patterns for cascading events
    """
    
    def __init__(
        self,
        node_mapping: Dict[str, int],
        window_size_ms: float = 100.0,
        max_spike_rate_hz: float = 100.0
    ):
        """
        Args:
            node_mapping: Map from DMC/node ID to graph node index
            window_size_ms: Time window for spike bursts (ms)
            max_spike_rate_hz: Maximum spike rate for encoding
        """
        self.node_mapping = node_mapping
        self.window_size_ms = window_size_ms
        self.max_spike_rate_hz = max_spike_rate_hz
        
    def encode_event(self, event: CSDBEvent) -> List[AERSpike]:
        """
        Encode single CSDB event into AER spikes
        
        Args:
            event: CSDB event to encode
            
        Returns:
            List of AER spikes
        """
        spikes = []
        
        # Get node address
        if event.dmc not in self.node_mapping:
            # Unknown DMC, skip
            return spikes
            
        node_addr = self.node_mapping[event.dmc]
        
        # Time-to-first-spike encoding based on urgency/criticality
        # Higher urgency/criticality → earlier spike
        urgency_factor = (event.urgency + event.criticality) / 2.0
        delay_ms = (1.0 - urgency_factor) * self.window_size_ms
        spike_time = event.timestamp + delay_ms / 1000.0
        
        # Base spike for primary node
        spikes.append(AERSpike(
            address=node_addr,
            timestamp=spike_time,
            intensity=urgency_factor
        ))
        
        # Event-type specific encoding
        if event.event_type == EventType.VALIDATION_FAIL:
            # High-priority burst for validation failures
            for i in range(3):
                spikes.append(AERSpike(
                    address=node_addr,
                    timestamp=spike_time + i * 2.0 / 1000.0,  # 2ms intervals
                    intensity=1.0
                ))
                
        elif event.event_type == EventType.DEPENDENCY_CHANGE:
            # Cascade to affected nodes
            for affected_dmc in event.affected_nodes:
                if affected_dmc in self.node_mapping:
                    affected_addr = self.node_mapping[affected_dmc]
                    cascade_delay = delay_ms + 10.0  # 10ms cascade delay
                    spikes.append(AERSpike(
                        address=affected_addr,
                        timestamp=event.timestamp + cascade_delay / 1000.0,
                        intensity=urgency_factor * 0.8  # Attenuated cascade
                    ))
                    
        elif event.event_type == EventType.PUBLICATION_REQUEST:
            # Multiple spikes for high-priority requests
            for i in range(2):
                spikes.append(AERSpike(
                    address=node_addr,
                    timestamp=spike_time + i * 5.0 / 1000.0,
                    intensity=0.9
                ))
                
        elif event.event_type == EventType.QA_RETURN:
            # Negative spike (inhibitory) for QA returns
            spikes.append(AERSpike(
                address=node_addr,
                timestamp=spike_time,
                intensity=-0.5  # Negative intensity for inhibition
            ))
        
        return spikes
    
    def encode_event_stream(
        self,
        events: List[CSDBEvent]
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Encode stream of events into spike tensor
        
        Args:
            events: List of CSDB events (time-ordered)
            
        Returns:
            (spike_tensor, spike_times)
            spike_tensor: [num_nodes, num_timesteps]
            spike_times: [num_timesteps] in seconds
        """
        if not events:
            return np.zeros((len(self.node_mapping), 1)), np.array([0.0])
        
        # Determine time range
        t_start = min(e.timestamp for e in events)
        t_end = max(e.timestamp for e in events)
        duration = max(t_end - t_start, 1.0)  # At least 1 second
        
        # Create time bins (1ms resolution)
        dt_ms = 1.0
        num_timesteps = int((duration * 1000.0) / dt_ms) + 1
        spike_tensor = np.zeros((len(self.node_mapping), num_timesteps))
        spike_times = np.linspace(t_start, t_end, num_timesteps)
        
        # Encode all events
        for event in events:
            event_spikes = self.encode_event(event)
            
            for spike in event_spikes:
                # Find time bin
                time_idx = int((spike.timestamp - t_start) * 1000.0 / dt_ms)
                if 0 <= time_idx < num_timesteps:
                    spike_tensor[spike.address, time_idx] += spike.intensity
        
        # Clip to valid spike range
        spike_tensor = np.clip(spike_tensor, -1.0, 1.0)
        
        return spike_tensor, spike_times
    
    def encode_population(
        self,
        events: List[CSDBEvent],
        population_type: str
    ) -> np.ndarray:
        """
        Encode events for specific population (module type, domain, phase)
        
        Args:
            events: List of CSDB events
            population_type: Population identifier (e.g., "descriptive", "airframe")
            
        Returns:
            Population spike vector [num_nodes]
        """
        spike_vector = np.zeros(len(self.node_mapping))
        
        # Filter events by population type
        filtered_events = [
            e for e in events
            if e.metadata.get("population") == population_type
        ]
        
        # Encode filtered events
        for event in filtered_events:
            if event.dmc in self.node_mapping:
                node_addr = self.node_mapping[event.dmc]
                urgency_factor = (event.urgency + event.criticality) / 2.0
                spike_vector[node_addr] += urgency_factor
        
        # Normalize
        spike_vector = np.clip(spike_vector, 0.0, 1.0)
        
        return spike_vector


def create_node_mapping(dmcs: List[str]) -> Dict[str, int]:
    """
    Create mapping from DMC identifiers to graph node indices
    
    Args:
        dmcs: List of Data Module Codes in CSDB
        
    Returns:
        Mapping dict: DMC -> node_index
    """
    return {dmc: idx for idx, dmc in enumerate(sorted(dmcs))}


def parse_csdb_event_log(log_file: str) -> List[CSDBEvent]:
    """
    Parse CSDB event log file into CSDBEvent objects
    
    Args:
        log_file: Path to JSONL event log
        
    Returns:
        List of parsed events
    """
    import json
    
    events = []
    
    with open(log_file, 'r') as f:
        for line in f:
            data = json.loads(line)
            
            event = CSDBEvent(
                event_id=data['event_id'],
                event_type=EventType(data['event_type']),
                dmc=data['dmc'],
                timestamp=data['timestamp'],
                urgency=data.get('urgency', 0.5),
                criticality=data.get('criticality', 0.5),
                affected_nodes=data.get('affected_nodes', []),
                metadata=data.get('metadata', {})
            )
            
            events.append(event)
    
    # Sort by timestamp
    events.sort(key=lambda e: e.timestamp)
    
    return events


if __name__ == "__main__":
    # Example usage
    print("AER Encoder for S1000D CSDB Events")
    
    # Create sample DMC mapping
    sample_dmcs = [
        "DMC-AMP360-AAA-53-10-00-00A-040A-D",
        "DMC-AMP360-AAA-53-10-10-00A-310A-P",
        "DMC-AMP360-AAA-53-10-00-00A-800A-I",
    ]
    node_mapping = create_node_mapping(sample_dmcs)
    
    print(f"Created node mapping for {len(node_mapping)} DMCs")
    
    # Create encoder
    encoder = AEREncoder(node_mapping, window_size_ms=100.0)
    
    # Create sample event
    sample_event = CSDBEvent(
        event_id="evt_001",
        event_type=EventType.VALIDATION_FAIL,
        dmc=sample_dmcs[0],
        timestamp=time.time(),
        urgency=0.9,
        criticality=0.8,
        affected_nodes=[sample_dmcs[1]],
        metadata={"population": "descriptive"}
    )
    
    # Encode event
    spikes = encoder.encode_event(sample_event)
    print(f"\nEncoded event into {len(spikes)} AER spikes:")
    for spike in spikes:
        print(f"  Address: {spike.address}, Time: {spike.timestamp:.6f}, Intensity: {spike.intensity:.2f}")
