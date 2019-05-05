from core.PSE import PSE, PSEFinancialTemplate, PSEDocument
from models.quarterly_report import QuarterlyReport, AnnualReport
from typing import Iterable
import csv


print("Searching reports...")
stock_symbol = 'ALI'
template = PSEFinancialTemplate.ANNUAL
results = PSE.search(stock_symbol, template,
                     '05-05-2017', '05-05-2019')

if template == PSEFinancialTemplate.QUARTERLY:
    i: int = 0
    quarterly_reports: Iterable[QuarterlyReport] = []
    for result in results:
        i = i + 1
        print("Getting report (%s/%s)..." % (i, len(results)))

        quarterly_report: QuarterlyReport = PSEDocument.get_quarterly_report(
            result.document_id)
        quarterly_reports.append(quarterly_report)

    print("Generating file...")
    f = open('%s-%s.csv' % (stock_symbol, template), 'w', newline='')
    with f:
        fnames = ['company_name', 'stock_symbol', 'field']
        balance_sheet_fields = ['current_assets', 'total_assets', 'current_liabilities', \
            'total_liabilities' , 'retained_earnings', 'stockholders_equity', \
            'stockholders_equity_parent', 'book_value_per_share']
        income_statement_fields = ['gross_revenue', 'gross_expense', 'non_operating_income', \
            'non_operating_expense' , 'income_before_tax', 'income_tax_expense', \
            'net_income', 'net_income_parent', 'earnings_per_share_basic', \
            'earnings_per_share_diluted']
        quarters = []
        for quarterly_report in quarterly_reports:
            if quarterly_report.quarter_end not in quarters:
                quarters.append(quarterly_report.quarter_end)
        fnames.extend(quarters)

        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        for field in balance_sheet_fields:
            row = {}
            row['company_name'] = quarterly_report.company_name
            row['stock_symbol'] = stock_symbol
            row['field'] = field
            for quarter in quarters:
                for quarterly_report in quarterly_reports:
                    if quarterly_report.quarter_end == quarter:
                        row[quarter] = vars(quarterly_report.balance_sheet)[field]
                        break

            writer.writerow(row)
        for field in income_statement_fields:
            row = {}
            row['company_name'] = quarterly_report.company_name
            row['stock_symbol'] = stock_symbol
            row['field'] = field
            for quarter in quarters:
                for quarterly_report in quarterly_reports:
                    if quarterly_report.quarter_end == quarter:
                        row[quarter] = vars(quarterly_report.income_statement)[field]
                        break

            writer.writerow(row)

if template == PSEFinancialTemplate.ANNUAL:
    i: int = 0
    annual_reports: Iterable[AnnualReport] = []
    for result in results:
        i = i + 1
        print("Getting report (%s/%s)..." % (i, len(results)))

        annual_report: AnnualReport = PSEDocument.get_annual_report(
            result.document_id)
        annual_reports.append(annual_report)

    print("Generating file...")
    f = open('%s-%s.csv' % (stock_symbol, template), 'w', newline='')
    with f:
        fnames = ['company_name', 'stock_symbol', 'field']
        balance_sheet_fields = ['current_assets', 'total_assets', 'current_liabilities', \
            'total_liabilities' , 'retained_earnings', 'stockholders_equity', \
            'stockholders_equity_parent', 'book_value_per_share']
        income_statement_fields = ['gross_revenue', 'gross_expense', 'non_operating_income', \
            'non_operating_expense' , 'income_before_tax', 'income_tax_expense', \
            'net_income', 'net_income_parent', 'earnings_per_share_basic', \
            'earnings_per_share_diluted']
        annuals = []
        for annual_report in annual_reports:
            if annual_report.year_end not in annuals:
                annuals.append(annual_report.year_end)
        fnames.extend(annuals)

        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        for field in balance_sheet_fields:
            row = {}
            row['company_name'] = annual_report.company_name
            row['stock_symbol'] = stock_symbol
            row['field'] = field
            for annual in annuals:
                for annual_report in annual_reports:
                    if annual_report.year_end == annual:
                        row[annual] = vars(annual_report.balance_sheet)[field]
                        break

            writer.writerow(row)
        for field in income_statement_fields:
            row = {}
            row['company_name'] = annual_report.company_name
            row['stock_symbol'] = stock_symbol
            row['field'] = field
            for annual in annuals:
                for annual_report in annual_reports:
                    if annual_report.year_end == annual:
                        row[annual] = vars(annual_report.income_statement)[field]
                        break

            writer.writerow(row)

print("Scrape completed!")
