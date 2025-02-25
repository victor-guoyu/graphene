from parsers import ParserFactory, ParserType
from renderer import PngRender
from app import Graphene


def main(template_path='./Template.xlsx', output_path='./dist/test.png'):
    parser = ParserFactory.get_parser(
        parser_type=ParserType.EXCEL,
        template_path=template_path
    )
    renderer = PngRender(output_path)
    graphene = Graphene(parser=parser, renderer=renderer)
    graphene.load_graph()
    graphene.render()


if __name__ == "__main__":
    main()
