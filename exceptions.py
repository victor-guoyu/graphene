class GraphException(Exception):
    pass


class InvalidEdgeError(GraphException):
    pass


class RedundantEdge(GraphException):
    pass

class ParserNotFound(GraphException):
    pass
