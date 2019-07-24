from abc import ABC, abstractmethod
from enum import Enum, auto, unique
from exceptions import ParserNotFound

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
    def parse_nodes(self):
        raise NotImplementedError

    @abstractmethod
    def parse_edges(self):
        raise NotImplementedError


class ParserFactory:
    @staticmethod
    def get_parser(type: ParserType) -> Parser:
        for each_parser in Parser.__subclasses__():
            if each_parser.type == type:
                return each_parser()

        raise ParserNotFound
