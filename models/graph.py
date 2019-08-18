import math
import networkx as nx
from exceptions import InvalidEdgeError, RedundantEdge, DuplicateNodeError


class Graph:
    def __init__(self, scale: int = 1):
        self.scale = scale
        self.nx_graph = nx.Graph()
        self._nodes_lookup_by_name = {}

    def insert_nodes(self, nodes):
        for each_node in nodes:
            if not self._nodes_lookup_by_name.get(each_node.label):
                self._nodes_lookup_by_name[each_node.label] = each_node
                self.nx_graph.add_node(
                    each_node.label,
                    color=each_node.color,
                    label=each_node.label,
                    size=each_node.size
                )
            else:
                raise DuplicateNodeError(
                    f'Node: {each_node.label} is already defined')

    def insert_edges(self, edges):
        for each_edge in edges:
            reference_node_name = each_edge.reference_node_name
            treatment_node_name = each_edge.treatment_node_name
            for each_edge_node_name in (reference_node_name, treatment_node_name):
                if not self._nodes_lookup_by_name.get(each_edge_node_name):
                    raise InvalidEdgeError(
                        f'Undefined node name {each_edge_node_name} in edge'
                    )

            if self.nx_graph.has_edge(reference_node_name, treatment_node_name):
                raise RedundantEdge

            self.nx_graph.add_edge(
                reference_node_name,
                treatment_node_name,
                label=each_edge.label
            )

    def get_edge_labels(self):
        return {
            (reference, treatment): label for (reference, treatment, label) in self.nx_graph.edges.data('label')
        }

    def get_node_colors(self):
        return [color for (_, color) in self.nx_graph.nodes.data('color')]

    def get_node_sizes(self):
        total_size = 0
        for (_, size) in self.nx_graph.nodes.data('size'):
            total_size += size

        average = math.ceil(total_size / self.nx_graph.number_of_nodes())

        sizes = []
        for (_, size) in self.nx_graph.nodes.data('size'):
            sizes.append(math.ceil(size / average) * 100)
        return sizes
