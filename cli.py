from parsers import ParserFactory, ParserType
from app import Graphene


def main():
    parser = ParserFactory.get_parser(ParserType.EXCEL)
    graphene = Graphene(parser=parser)
    graphene.load_graph()


if __name__ == "__main__":
    main()
