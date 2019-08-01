class GraphException(Exception):
    pass


class InvalidEdgeError(GraphException):
    pass


class DuplicateNodeError(GraphException):
    pass


class RedundantEdge(GraphException):
    pass


class ParserNotFound(GraphException):
    pass
