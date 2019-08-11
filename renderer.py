import networkx as nx
import matplotlib.pyplot as plt


class BaseRenderer:
    pass


class PngRender(BaseRenderer):
    def __init__(self, output_path):
        self.output_path = output_path

    def draw(self, graph):
        nx.draw(graph.nx_graph)
        plt.savefig(self.output_path)
