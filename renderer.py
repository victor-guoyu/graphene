import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class BaseRenderer:
    pass


class PngRender(BaseRenderer):
    def __init__(self, output_path):
        self.output_path = output_path

    def draw(self, graph):
        edge_labels = graph.get_edge_labels()
        node_colors = graph.get_node_colors()
        node_sizes = graph.get_node_sizes()
        nx_graph = graph.nx_graph
        node_legends = []
        for (label, color) in nx_graph.nodes.data('color', 'label'):
            patch = mpatches.Patch(color=color, label=label)
            node_legends.append(patch)

        pos = nx.circular_layout(nx_graph)
        nx.draw(nx_graph, pos=pos, node_color=node_colors, node_size=node_sizes)
        nx.draw_networkx_edge_labels(
            nx_graph, pos, edge_labels=edge_labels,
            label_pos=0.3, font_size=3, alpha=0.8
        )
        plt.legend(
            handles=node_legends,
            fontsize='xx-small',
            loc='best'
        )
        plt.savefig(self.output_path, dpi=1024)
