"""
CSDB Graph Builder

Constructs a graph representation of the S1000D CSDB:
- Nodes: DMCs, Illustrations, IPD, PM, BREX, Product Configs
- Edges: References, Dependencies, Effectivity, Workflow State
"""

import os
import xml.etree.ElementTree as ET
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass, field
import networkx as nx
import pickle


@dataclass
class CSDBNode:
    """CSDB graph node"""
    node_id: str
    node_type: str  # DMC, ICN, PM, BREX, etc.
    metadata: Dict = field(default_factory=dict)


@dataclass
class CSDBEdge:
    """CSDB graph edge"""
    source: str
    target: str
    edge_type: str  # reference, dependency, effectivity, workflow
    weight: float = 1.0
    metadata: Dict = field(default_factory=dict)


class CSDBGraphBuilder:
    """Build graph from CSDB directory structure"""
    
    def __init__(self, csdb_root: str):
        """
        Args:
            csdb_root: Path to CSDB root directory
        """
        self.csdb_root = csdb_root
        self.graph = nx.DiGraph()
        self.nodes: Dict[str, CSDBNode] = {}
        self.edges: List[CSDBEdge] = []
        
    def build_graph(self) -> nx.DiGraph:
        """
        Build complete CSDB graph
        
        Returns:
            NetworkX directed graph
        """
        print("Building CSDB graph...")
        
        # Step 1: Discover all nodes
        self._discover_nodes()
        
        # Step 2: Extract edges from references
        self._extract_references()
        
        # Step 3: Build effectivity edges
        self._build_effectivity_edges()
        
        # Step 4: Add workflow state edges
        self._add_workflow_edges()
        
        # Step 5: Construct NetworkX graph
        self._construct_networkx_graph()
        
        print(f"Graph built: {self.graph.number_of_nodes()} nodes, "
              f"{self.graph.number_of_edges()} edges")
        
        return self.graph
    
    def _discover_nodes(self):
        """Discover all CSDB nodes (DMCs, ICNs, etc.)"""
        print("  Discovering nodes...")
        
        # Data Modules
        dm_path = os.path.join(self.csdb_root, "DataModules")
        if os.path.exists(dm_path):
            for root, dirs, files in os.walk(dm_path):
                for file in files:
                    if file.endswith(".xml"):
                        dmc = self._extract_dmc_from_filename(file)
                        if dmc:
                            self.nodes[dmc] = CSDBNode(
                                node_id=dmc,
                                node_type="DMC",
                                metadata={
                                    "file_path": os.path.join(root, file),
                                    "category": self._categorize_dmc(file)
                                }
                            )
        
        # Illustrations (ICN)
        icn_path = os.path.join(self.csdb_root, "Illustrations")
        if os.path.exists(icn_path):
            for root, dirs, files in os.walk(icn_path):
                for file in files:
                    if file.startswith("ICN-") and file.endswith((".svg", ".png")):
                        icn = os.path.splitext(file)[0]
                        self.nodes[icn] = CSDBNode(
                            node_id=icn,
                            node_type="ICN",
                            metadata={"file_path": os.path.join(root, file)}
                        )
        
        # Publication Modules
        pm_path = os.path.join(self.csdb_root, "PM")
        if os.path.exists(pm_path):
            for file in os.listdir(pm_path):
                if file.endswith(".xml"):
                    pm_id = os.path.splitext(file)[0]
                    self.nodes[pm_id] = CSDBNode(
                        node_id=pm_id,
                        node_type="PM",
                        metadata={"file_path": os.path.join(pm_path, file)}
                    )
        
        # BREX
        brex_path = os.path.join(self.csdb_root, "BREX")
        if os.path.exists(brex_path):
            for file in os.listdir(brex_path):
                if file.endswith(".xml"):
                    brex_id = os.path.splitext(file)[0]
                    self.nodes[brex_id] = CSDBNode(
                        node_id=brex_id,
                        node_type="BREX",
                        metadata={"file_path": os.path.join(brex_path, file)}
                    )
        
        print(f"    Found {len(self.nodes)} nodes")
    
    def _extract_references(self):
        """Extract reference edges from DMC XML files"""
        print("  Extracting references...")
        
        for node_id, node in self.nodes.items():
            if node.node_type != "DMC":
                continue
                
            xml_path = node.metadata.get("file_path")
            if not xml_path or not os.path.exists(xml_path):
                continue
            
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                
                # Find dmRef elements (Data Module references)
                for dm_ref in root.findall(".//{*}dmRef"):
                    ref_dmc = self._extract_dmc_from_element(dm_ref)
                    if ref_dmc and ref_dmc in self.nodes:
                        self.edges.append(CSDBEdge(
                            source=node_id,
                            target=ref_dmc,
                            edge_type="reference",
                            weight=1.0
                        ))
                
                # Find graphic references
                for graphic in root.findall(".//{*}graphic"):
                    icn_id = graphic.get("infoEntityIdent")
                    if icn_id and icn_id in self.nodes:
                        self.edges.append(CSDBEdge(
                            source=node_id,
                            target=icn_id,
                            edge_type="reference",
                            weight=0.5  # Lower weight for illustrations
                        ))
                        
            except Exception as e:
                print(f"    Warning: Could not parse {xml_path}: {e}")
        
        print(f"    Extracted {len(self.edges)} reference edges")
    
    def _build_effectivity_edges(self):
        """Build edges based on effectivity (ACT)"""
        print("  Building effectivity edges...")
        
        # Parse ACT if exists
        act_path = os.path.join(self.csdb_root, "ACT", "act.xml")
        if not os.path.exists(act_path):
            print("    No ACT found, skipping")
            return
        
        try:
            tree = ET.parse(act_path)
            # Extract effectivity relationships
            # This is simplified; real implementation would parse ACT structure
            # and create edges between DMCs with same effectivity
            pass
        except Exception as e:
            print(f"    Warning: Could not parse ACT: {e}")
    
    def _add_workflow_edges(self):
        """Add edges representing workflow dependencies"""
        print("  Adding workflow edges...")
        
        # Example: Descriptive DMCs must be reviewed before Procedural
        descriptive = [n for n in self.nodes.values() if "descriptive" in n.metadata.get("category", "").lower()]
        procedural = [n for n in self.nodes.values() if "procedural" in n.metadata.get("category", "").lower()]
        
        # Create workflow dependencies (simplified)
        for desc in descriptive[:5]:  # Limit for demo
            for proc in procedural[:5]:
                self.edges.append(CSDBEdge(
                    source=desc.node_id,
                    target=proc.node_id,
                    edge_type="workflow",
                    weight=0.3
                ))
    
    def _construct_networkx_graph(self):
        """Construct NetworkX graph from nodes and edges"""
        print("  Constructing NetworkX graph...")
        
        # Add nodes
        for node_id, node in self.nodes.items():
            self.graph.add_node(
                node_id,
                node_type=node.node_type,
                **node.metadata
            )
        
        # Add edges
        for edge in self.edges:
            self.graph.add_edge(
                edge.source,
                edge.target,
                edge_type=edge.edge_type,
                weight=edge.weight,
                **edge.metadata
            )
    
    def _extract_dmc_from_filename(self, filename: str) -> Optional[str]:
        """Extract DMC from filename"""
        if filename.startswith("DMC-") and filename.endswith(".xml"):
            return os.path.splitext(filename)[0]
        return None
    
    def _categorize_dmc(self, filename: str) -> str:
        """Categorize DMC by type"""
        if "/Descriptive/" in filename:
            return "descriptive"
        elif "/Procedural/" in filename:
            return "procedural"
        elif "/IPD/" in filename:
            return "ipd"
        elif "/Wiring/" in filename:
            return "wiring"
        elif "/FunctionalTest/" in filename:
            return "test"
        return "unknown"
    
    def _extract_dmc_from_element(self, element: ET.Element) -> Optional[str]:
        """Extract DMC from XML element"""
        # Simplified DMC extraction
        dmc_code = element.get("dmCode")
        return dmc_code
    
    def save_graph(self, output_path: str):
        """Save graph to pickle file"""
        with open(output_path, 'wb') as f:
            pickle.dump(self.graph, f)
        print(f"Graph saved to {output_path}")
    
    @staticmethod
    def load_graph(input_path: str) -> nx.DiGraph:
        """Load graph from pickle file"""
        with open(input_path, 'rb') as f:
            graph = pickle.load(f)
        print(f"Graph loaded from {input_path}")
        return graph


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python graph_builder.py <csdb_path> [output_path]")
        sys.exit(1)
    
    csdb_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "csdb_graph.pkl"
    
    builder = CSDBGraphBuilder(csdb_path)
    graph = builder.build_graph()
    builder.save_graph(output_path)
    
    # Print statistics
    print("\nGraph Statistics:")
    print(f"  Nodes: {graph.number_of_nodes()}")
    print(f"  Edges: {graph.number_of_edges()}")
    print(f"  Avg degree: {sum(dict(graph.degree()).values()) / graph.number_of_nodes():.2f}")
    print(f"  Connected components: {nx.number_weakly_connected_components(graph)}")
