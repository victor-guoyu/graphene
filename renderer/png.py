import networkx as nx
import matplotlib.pyplot as plt
from renderer.base import BaseRenderer


class PngRender(BaseRenderer):
    def __init__(self, output_path):
        self.output_path = output_path

    def draw(self, graph):
        import ipdb
        ipdb.set_trace()
        nx.draw(graph.nx_graph)
        plt.savefig(self.output_path)
