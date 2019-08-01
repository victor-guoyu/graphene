from models.graph import Graph


class Graphene:
    def __init__(self, parser, renderer):
        self.parser = parser
        self.renderer = renderer
        self._graph = Graph()

    def load_graph(self):
        self.parser.parse()
        nodes = self.parser.nodes
        self._graph.insert_nodes(nodes)
        edges = self.parser.edges
        self._graph.insert_edge(edges)

        # destroy redudant memory copy of the data
        self.parser = None

    def render(self):
        self.render.draw(self._graph)
