import xlrd
from parsers.base import (ParserType, Parser, EDGE_SHEET, NODE_SHEET)
from models.node import Node


class ExcelParser(Parser):
    type = ParserType.EXCEL

    def __init__(self, file_path):
        self.workbook = xlrd.open_workbook(filename=file_path, on_demand=True)

    def parse_nodes(self):
        node_sheet = self.workbook.sheet_by_name(NODE_SHEET)
        rows = node_sheet.get_rows()
        rows.next()  # skip header row
        for each_row in node_sheet.get_rows():
            node_name = each_row[0].value
            size = each_row[1].value
            node =

    def parse_edges(self):
        edge_sheet = self.workbook.sheet_by_name(EDGE_SHEET)
