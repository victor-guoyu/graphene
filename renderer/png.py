from renderer.base import BaseRenderer


class PngRender(BaseRenderer):
    def __init__(self, output_path):
        self.output_path = output_path

    def draw(self, graph):
        pass
