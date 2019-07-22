class Node:
    def __init__(self, size, color, label):
        self.size = size
        self.color = color
        self.label = label

    def __hash__(self):
        return hash((self.size, self.color, self.label))

    def __eq__(self, other_node):
        return (self.size, self.color, self.label) == \
            (other_node.size, other_node.color, other_node.label)

    def __repr__(self):
        return f'[Node]: label: {self.label}, color: {self.color}, size: {self.size}'
