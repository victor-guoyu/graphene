from exceptions import InvalidEdgeError, RedundantEdge


class Graph:
    def __init__(self, scale: int):
        self.scale = scale
        self._graph = {}
        self._nodes = []

    # {
    #     node_1: {
    #         node_2: edge
    #     }
    # }

    def insert_node(self, node):
        if node not in self._nodes:
            self._nodes.append(node)
            self._graph[node] = {}

    def insert_edge(self, edge):
        reference_node = edge.reference_node
        treatment_node = edge.treatment_node
        for edge_node in (reference_node, treatment_node):
            if edge_node not in self._nodes:
                raise InvalidEdgeError

        if self._graph[reference_node][treatment_node]:
            raise RedundantEdge

        self._graph[reference_node][treatment_node] = edge

