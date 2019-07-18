from parsers import ParserFactory, ParserType
from renderer.png import

def main():
    parser = ParserFactory.get_parser(ParserType.EXCEL)
    nodes = parser.parse_nodes()
    edges = parser.parse_edges()

    for each_edge in edges:
        pass
