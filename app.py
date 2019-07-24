from models.graph import Graph


class Graphene:
    def __init__(self, parser):
        self.template_path = template_path
        self.parser = parser
        self._graph = Graph()

    def populate_nodes(self):
        for node in self.parser.parse_nodes():
            self._graph.insert_node(node)

    def populate_edges(self):
        for edge in self.parser.parse_edges():
            self._graph.insert_edge(edge)
