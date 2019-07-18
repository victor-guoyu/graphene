class Node:
    def __init__(self, size, color, label):
        self.size = size
        self.color = color
        self.label = label
        self._edges = []

    @property
    def edges(self):
        return self._edges

    def add_edge(self, edge):
        self._edges.append(edge)

    def remove_edge(self, edge):
        self._edges.remove(edge)

    def has_edge(self, node) -> bool:
        return node in self._edges
