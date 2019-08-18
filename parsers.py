import xlrd
from abc import ABC, abstractmethod
from enum import Enum, auto, unique
from utils import random_colors_generator
from models.node import Node
from models.edge import Edge
from exceptions import ParserNotFound, DuplicateNodeError, InvalidEdgeError

EDGE_SHEET = 'Edges'
NODE_SHEET = 'Nodes'


@unique
class ParserType(Enum):
    EXCEL = auto()
    CSV = auto()


class Parser(ABC):
    type = None

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def _parse_nodes(self):
        raise NotImplementedError

    @abstractmethod
    def _parse_edges(self):
        raise NotImplementedError

    @abstractmethod
    def parse(self):
        raise NotImplementedError


class ExcelParser(Parser):
    type = ParserType.EXCEL

    def __init__(self, file_path):
        self.workbook = xlrd.open_workbook(filename=file_path, on_demand=True)
        self.nodes = []
        self.edges = []

    def _parse_nodes(self):
        node_sheet = self.workbook.sheet_by_name(NODE_SHEET)
        rows = node_sheet.get_rows()
        for i, each_row in enumerate(rows):
            if i == 0:
                # skip header row
                continue
            label = each_row[0].value
            size = each_row[1].value
            try:
                color = each_row[2].value
            except IndexError:
                color = random_colors_generator()

            node = Node(label=label, size=size, color=color)
            self.nodes.append(node)

    def _parse_edges(self):
        edges = []
        edge_sheet = self.workbook.sheet_by_name(EDGE_SHEET)
        rows = edge_sheet.get_rows()
        for i, each_row in enumerate(rows):
            if i == 0:
                continue
            reference_node_name = each_row[0].value
            treatment_node_name = each_row[1].value

            weight = each_row[2].value
            label = each_row[3].value
            edge = Edge(
                reference_node_name=reference_node_name,
                treatment_node_name=treatment_node_name,
                weight=weight,
                label=label,
                color=None
            )
            self.edges.append(edge)

    def parse(self):
        self._parse_nodes()
        self._parse_edges()
        # destroy lookup table to save memory
        self._name_to_node = None


class ParserFactory:
    @staticmethod
    def get_parser(parser_type: ParserType, template_path: str) -> Parser:
        for each_parser in Parser.__subclasses__():
            if each_parser.type == parser_type:
                return each_parser(template_path)

        raise ParserNotFound
