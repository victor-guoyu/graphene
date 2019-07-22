class Edge:
    def __init__(self, reference_node, treatment_node, weight, color, text):
        self.reference_node = reference_node
        self.treatment_node = treatment_node
        self.weight = weight
        self.color = color
        self.text = text

    def __repr__(self):
        return f'[Edge]: ref: {self.reference_node}, treatment: {self.treatment_node}, text: {self.text}, color: {self.color}, weight: {self.weight}'
