import networkx as nx
import matplotlib.pyplot as plt


class BaseRenderer:
    pass


class PngRender(BaseRenderer):
    def __init__(self, output_path):
        self.output_path = output_path

    def draw(self, graph):
        edge_labels = graph.get_edge_labels()
        node_colors = graph.get_node_colors()
        nx_graph = graph.nx_graph
        pos = nx.circular_layout(nx_graph)
        nx.draw(nx_graph, pos=pos, node_color=node_colors, node_size=80)
        nx.draw_networkx_edge_labels(
            nx_graph, pos, edge_labels=edge_labels,
            label_pos=0.3, font_size=3, alpha=0.8
        )
        plt.savefig(self.output_path, dpi=1024)
