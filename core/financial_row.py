from bs4 import BeautifulSoup

class FinancialRow():
    @staticmethod
    def from_data_ref(table: BeautifulSoup, data_ref: str) -> BeautifulSoup:
        return table.find("a", {
            "data-ref": data_ref
        }) \
        .parent.parent.contents[1:6]

    @staticmethod
    def from_row_title(table: BeautifulSoup, row_title: str) -> BeautifulSoup:
        return table.find("td", string=row_title, attrs={
            "class": "rowTitle"
        }) \
        .parent.contents[1:6]