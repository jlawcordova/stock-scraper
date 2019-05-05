from typing import Iterable
from bs4 import BeautifulSoup

from core.financial_row import FinancialRow

class Financial(object):
    def __init__(self):
        self.year : int = 0
        self.sales : int = 0
        self.income : int = 0
        self.assets  : int = 0
        self.expense  : int = 0
        self.inventories : int = 0
        self.accounts_receivable : int = 0
        self.liabilities : int = 0
        self.equity : int = 0
        self.shareholders_equity : int = 0

    def __repr__(self):
        return "<Financial year:%s>" % (self.year)

    def __str__(self):
        return "Financial (Year %s)" % (self.year)

    @staticmethod
    def from_soup(soup: BeautifulSoup) -> Iterable['Financial']:
        # Income statement
        income_annual = soup.find(id = "incomeAnnual")
        income_annual_table = income_annual.table

        years_row = income_annual_table.thead.tr.contents[1:6]
        sales_row = FinancialRow.from_data_ref(income_annual_table, "ratio-salesOrRevenue")
        income_row = FinancialRow.from_data_ref(income_annual_table, "ratio-netIncome")

        # Balance sheet
        income_annual = soup.find(id = "balanceSheetAnnual")
        income_annual_tables = income_annual.find_all("table")

        assets_row = FinancialRow.from_data_ref(income_annual_tables[1], "ratio-totalAssets")
        inventories_row = FinancialRow.from_row_title(income_annual_tables[0], "Inventories")
        accounts_receivable_row = FinancialRow.from_data_ref(income_annual_tables[0], "ratio-totalAccountsReceivable")
        liabilities_row = FinancialRow.from_row_title(income_annual_tables[2], "Total Liabilities")
        equity_row = FinancialRow.from_row_title(income_annual_tables[2], "Total Equity")
        shareholders_equity_row = FinancialRow.from_row_title(income_annual_tables[2], "Total Shareholders' Equity")

        financials:  Iterable[Financial] = []
        for i in range(0, 5):
            financial = Financial()
            financial.year = int(years_row[i].string.replace(',', ''))
            financial.sales = int(sales_row[i].string.replace(',', ''))
            financial.income = int(income_row[i].string.replace(',', ''))
            financial.assets = int(assets_row[i].string.replace(',', ''))
            financial.expense = financial.sales - financial.income
            financial.inventories = int(inventories_row[i].string.replace(',', ''))
            financial.accounts_receivable = int(accounts_receivable_row[i].string.replace(',', ''))
            financial.liabilities = int(liabilities_row[i].string.replace(',', ''))
            financial.equity = int(equity_row[i].string.replace(',', ''))
            financial.shareholders_equity = int(shareholders_equity_row[i].string.replace(',', ''))

            financials.append(financial)

        return financials