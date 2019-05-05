from bs4 import BeautifulSoup


class QuarterlyReport(object):
    def __init__(self, quarter_end: str, company_name: str,
                 balance_sheet: 'BalanceSheet', income_statement: 'IncomeStatement'):
        self.quarter_end: str = quarter_end
        self.company_name: str = company_name
        self.balance_sheet: BalanceSheet = balance_sheet
        self.income_statement: IncomeStatement = income_statement

    def __repr__(self):
        return "<QuarterlyReport [%s]:[%s]>" % (self.company_name, self.quarter_end)

    @classmethod
    def from_soup(cls, soup: BeautifulSoup) -> 'QuarterlyReport':
        content_box: BeautifulSoup = soup.find("div", {
            'id': 'contentBox'
        })
        balance_sheet_table: BeautifulSoup = soup.find("table", {
            'id': 'BS'
        })
        income_statement_table: BeautifulSoup = soup.find("table", {
            'id': 'IS'
        })

        quarter_end = content_box.find_all("dd")[0] \
            .span.string
        company_name = content_box.find_all("dd")[3] \
            .span.string
        balance_sheet = BalanceSheet.from_soup(balance_sheet_table)
        income_statement = IncomeStatement.from_soup(income_statement_table)

        return cls(quarter_end, company_name, balance_sheet, income_statement)


class AnnualReport(object):
    def __init__(self, year_end: str, company_name: str,
                 balance_sheet: 'BalanceSheet', income_statement: 'IncomeStatement'):
        self.year_end: str = year_end
        self.company_name: str = company_name
        self.balance_sheet: BalanceSheet = balance_sheet
        self.income_statement: IncomeStatement = income_statement

    def __repr__(self):
        return "<QuarterlyReport [%s]:[%s]>" % (self.company_name, self.year_end)

    @classmethod
    def from_soup(cls, soup: BeautifulSoup) -> 'QuarterlyReport':
        content_box: BeautifulSoup = soup.find("div", {
            'id': 'contentBox'
        })
        balance_sheet_table: BeautifulSoup = soup.find("table", {
            'id': 'BS'
        })
        income_statement_table: BeautifulSoup = soup.find("table", {
            'id': 'IS'
        })

        year_end = content_box.find_all("dd")[0] \
            .span.string
        company_name = content_box.find_all("dd")[3] \
            .span.string
        balance_sheet = BalanceSheet.from_soup(balance_sheet_table)
        income_statement = IncomeStatement.from_soup(income_statement_table)

        return cls(year_end, company_name, balance_sheet, income_statement)


class BalanceSheet(object):
    PERIOD_ENDED_COLUMN_INDEX = 0
    PERIOD_END_INDEX = 1
    CURRENT_ASSETS_INDEX = 2
    TOTAL_ASSETS_INDEX = 3
    CURRENT_LIABILITIES_INDEX = 4
    TOTAL_LIABILITIES_INDEX = 5
    RETIANED_EARNINGS_INDEX = 6
    STOCKHOLDERS_EQUITY_INDEX = 7
    STOCKHOLDERS_EQUITY_PARENT_INDEX = 8
    BOOK_VALUE_PER_SHARE_INDEX = 9

    def __init__(self, period_end: int, current_assets: int, total_assets: int,
                 current_liabilities: int, total_liabilities: int,
                 retained_earnings: int, stockholders_equity: int,
                 stockholders_equity_parent: int, book_value_per_share: int):
        self.period_end: int = period_end
        self.current_assets: int = current_assets
        self.total_assets: int = total_assets
        self.current_liabilities: int = current_liabilities
        self.total_liabilities: int = total_liabilities
        self.retained_earnings: int = retained_earnings
        self.stockholders_equity: int = stockholders_equity
        self.stockholders_equity_parent: int = stockholders_equity_parent
        self.book_value_per_share: int = book_value_per_share

    def __repr__(self):
        return "<BalanceSheet [%s]>" % (self.period_end)

    @classmethod
    def from_soup(cls, soup: BeautifulSoup) -> 'BalanceSheet':
        rows: BeautifulSoup = soup.tbody.find_all("tr")

        period_end = rows[BalanceSheet.PERIOD_END_INDEX] \
            .find_all("td")[BalanceSheet.PERIOD_ENDED_COLUMN_INDEX].string
        current_assets = rows[BalanceSheet.CURRENT_ASSETS_INDEX] \
            .find_all("td")[BalanceSheet.PERIOD_ENDED_COLUMN_INDEX].string
        total_assets = rows[BalanceSheet.TOTAL_ASSETS_INDEX] \
            .find_all("td")[BalanceSheet.PERIOD_ENDED_COLUMN_INDEX].string
        current_liabilities = rows[BalanceSheet.CURRENT_LIABILITIES_INDEX] \
            .find_all("td")[BalanceSheet.PERIOD_ENDED_COLUMN_INDEX].string
        total_liabilities = rows[BalanceSheet.TOTAL_LIABILITIES_INDEX] \
            .find_all("td")[BalanceSheet.PERIOD_ENDED_COLUMN_INDEX].string
        retained_earnings = rows[BalanceSheet.RETIANED_EARNINGS_INDEX] \
            .find_all("td")[BalanceSheet.PERIOD_ENDED_COLUMN_INDEX].string
        stockholders_equity = rows[BalanceSheet.STOCKHOLDERS_EQUITY_INDEX] \
            .find_all("td")[BalanceSheet.PERIOD_ENDED_COLUMN_INDEX].string
        stockholders_equity_parent = rows[BalanceSheet.STOCKHOLDERS_EQUITY_PARENT_INDEX] \
            .find_all("td")[BalanceSheet.PERIOD_ENDED_COLUMN_INDEX].string
        book_value_per_share = rows[BalanceSheet.BOOK_VALUE_PER_SHARE_INDEX] \
            .find_all("td")[BalanceSheet.PERIOD_ENDED_COLUMN_INDEX].string

        return cls(period_end, current_assets, total_assets, current_liabilities,
                   total_liabilities, retained_earnings, stockholders_equity,
                   stockholders_equity_parent, book_value_per_share)


class IncomeStatement(object):
    CURRENT_YEAR_QUARTER_INDEX = 0
    GROSS_REVENUE_INDEX = 1
    GROSS_EXPENSE_INDEX = 2
    NON_OPERATING_INCOME_INDEX = 3
    NON_OPERATING_EXPENSE_INDEX = 4
    INCOME_BEFORE_TAX_INDEX = 5
    INCOME_TAX_EXPENSE_INDEX = 6
    NET_INCOME_INDEX = 7
    NET_INCOME_PARENT_INDEX = 8
    EARNINGS_PER_SHARE_BASIC_INDEX = 9
    EARNINGS_PER_SHARE_DILUTED_INDEX = 9

    def __init__(self, gross_revenue: int, gross_expense: int,
                 non_operating_income: int, non_operating_expense: int,
                 income_before_tax: int, income_tax_expense: int, net_income: int,
                 net_income_parent: int, earnings_per_share_basic: int,
                 earnings_per_share_diluted: int):
        self.gross_revenue: int = gross_revenue
        self.gross_expense: int = gross_expense
        self.non_operating_income: int = non_operating_income
        self.non_operating_expense: int = non_operating_expense
        self.income_before_tax: int = income_before_tax
        self.income_tax_expense: int = income_tax_expense
        self.net_income: int = net_income
        self.net_income_parent: int = net_income_parent
        self.earnings_per_share_basic: int = earnings_per_share_basic
        self.earnings_per_share_diluted: int = earnings_per_share_diluted

    @classmethod
    def from_soup(cls, soup: BeautifulSoup) -> 'BalanceSheet':
        rows: BeautifulSoup = soup.tbody.find_all("tr")

        gross_revenue = rows[IncomeStatement.GROSS_REVENUE_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string
        gross_expense = rows[IncomeStatement.GROSS_EXPENSE_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string
        non_operating_income = rows[IncomeStatement.NON_OPERATING_INCOME_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string
        non_operating_expense = rows[IncomeStatement.NON_OPERATING_EXPENSE_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string
        income_before_tax = rows[IncomeStatement.INCOME_BEFORE_TAX_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string
        income_tax_expense = rows[IncomeStatement.INCOME_TAX_EXPENSE_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string
        net_income = rows[IncomeStatement.NET_INCOME_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string
        net_income_parent = rows[IncomeStatement.NET_INCOME_PARENT_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string
        earnings_per_share_basic = rows[IncomeStatement.EARNINGS_PER_SHARE_BASIC_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string
        earnings_per_share_diluted = rows[IncomeStatement.EARNINGS_PER_SHARE_DILUTED_INDEX] \
            .find_all("td")[IncomeStatement.CURRENT_YEAR_QUARTER_INDEX].string

        return cls(gross_revenue, gross_expense, non_operating_income,
                   non_operating_expense, income_before_tax, income_tax_expense,
                   net_income, net_income_parent, earnings_per_share_basic,
                   earnings_per_share_diluted)
