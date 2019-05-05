from typing import Iterable
from bs4 import BeautifulSoup

from core.financial import Financial

class Stock(object):
    def __init__(self, name: str, symbol: str, financials: Iterable[Financial]):
        self.name : str = name
        self.symbol : str = symbol
        self.financials : Iterable['Financial']= financials

    def __repr__(self):
        return "<Stock symbol:%s>" % (self.symbol)

    def __str__(self):
        return "%s : %s" % (self.name, self.symbol)

    @classmethod
    def from_soup(cls, soup: BeautifulSoup):
        name = soup.find(class_ = "quoteHeader__commonName").string
        symbol = soup.find(class_ = "quoteHeader__ticker").string
        financials = Financial.from_soup(soup)

        return cls(name, symbol, financials)