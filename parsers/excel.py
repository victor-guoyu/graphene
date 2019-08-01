import xlrd
from parsers.base import (ParserType, Parser, EDGE_SHEET, NODE_SHEET)
from models.node import Node
from models.edge import Edge
from exceptions import DuplicateNodeError, InvalidEdgeError


class ExcelParser(Parser):
    type = ParserType.EXCEL

    def __init__(self, file_path):
        self.workbook = xlrd.open_workbook(filename=file_path, on_demand=True)
        self.nodes = []
        self.edges = []

    def _parse_nodes(self):
        node_sheet = self.workbook.sheet_by_name(NODE_SHEET)
        rows = node_sheet.get_rows()
        rows.next()  # skip header row
        for each_row in rows:
            label = each_row[0].value
            size = each_row[1].value
            color = each_row.get(3)
            node = Node(label=label, size=size, color=color)
            self.nodes.append(node)

    def _parse_edges(self):
        edges = []
        edge_sheet = self.workbook.sheet_by_name(EDGE_SHEET)
        rows = edge_sheet.get_rows()
        rows.next()
        for each_row in rows:
            reference_node_name = each_row[0].value
            treatment_node_name = each_row[1].value

            weight = each_row[2].value
            label = each_row[3].value
            edge = Edge(
                reference_node_name=reference_node_name,
                treatment_node_name=treatment_node_name,
                weight=weight,
                label=label
            )
            self.edges.append(edge)

    def parse(self):
        self._parse_nodes()
        self._parse_edges()
        # destroy lookup table to save memory
        self._name_to_node = None
