from parsers import ParserFactory, ParserType
from renderer.png import PngRender
from app import Graphene


def main(template_path, output_path):
    parser = ParserFactory.get_parser(
        type=ParserType.EXCEL,
        template_path=template_path
    )
    renderer = PngRender(output_path)
    graphene = Graphene(parser=parser, renderer=renderer)
    graphene.load_graph()
    graphene.render()


if __name__ == "__main__":
    main()
