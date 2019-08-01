from models.graph import Graph


class Graphene:
    def __init__(self, parser):
        self.template_path = template_path
        self.parser = parser
        self._graph = Graph()

    def load_graph(self):
        self.parser.parse()
        nodes = self.parser.nodes
        self._graph.insert_nodes(nodes)
        edges = self.parser.edges
        self._graph.insert_edge(edges)

        # destroy redudant memory copy of the data
        self.parser = None
