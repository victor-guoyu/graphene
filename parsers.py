from abc import ABC, abstractmethod
from enum import Enum, auto, unique
from exceptions import ParserNotFound


@unique
class ParserType(Enum):
    EXCEL = auto()
    CSV = auto()


class Parser(ABC):
    type = None

    @abstractmethod
    def parse_nodes(self):
        raise NotImplementedError

    @abstractmethod
    def parse_edges(self):
        raise NotImplementedError


class ExcelParser(Parser):
    type = ParserType.EXCEL

    def parse_nodes(self):
        pass

    def parse_edges(self):
        pass


class ParserFactory:
    @staticmethod
    def get_parser(type: ParserType) -> Parser:
        for each_parser in Parser.__subclasses__():
            if each_parser.type == type:
                return each_parser()

        raise ParserNotFound
