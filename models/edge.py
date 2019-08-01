class Edge:
    def __init__(self, reference_node_name, treatment_node_name, weight, color, label):
        self.reference_node_name = reference_node_name
        self.treatment_node_name = treatment_node_name
        self.weight = weight
        self.color = color
        self.label = label

    def __repr__(self):
        return f'[Edge]: ref: {self.reference_node_name}, treatment: {self.treatment_node_name}, label: {self.label}, color: {self.color}, weight: {self.weight}'
