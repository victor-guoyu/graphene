from exceptions import InvalidEdgeError, RedundantEdge, DuplicateNodeError


class Graph:
    def __init__(self, scale: int = 1):
        self.scale = scale
        self._graph = {}
        self._nodes_lookup_by_name = {}

    # {
    #     node_1_name: {
    #         node_2_name: edge
    #     }
    # }

    def insert_nodes(self, nodes):
        for each_node in nodes:
            if not self._nodes_lookup_by_name[each_node.label]:
                self._nodes_lookup_by_name[node.label] = each_node
                self._graph[each_node.label] = {}
            else:
                raise DuplicateNodeError(
                    f'Node: {each_node.label} is already defined')

    def insert_edges(self, edges):
        for each_edge in edges:
            reference_node_name = each_edge.reference_node_name
            treatment_node_name = each_edge.treatment_node_name
            for each_edge_node_name in (reference_node_name, treatment_node_name):
                if not self._nodes_lookup_by_name[each_edge_node_name]:
                    raise InvalidEdgeError(
                        f'Undefined node name {each_edge_node_name} in edge'
                    )

            if self._graph[reference_node_name][treatment_node_name]:
                raise RedundantEdge

            self._graph[reference_node_name][treatment_node_name] = each_edge
