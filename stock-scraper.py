#!/usr/bin/env python

from bs4 import BeautifulSoup
from requests import get
import sys
import csv

from core.stock import Stock

stockSymbol = sys.argv[1]


# Request
print("Retrieving data...")
url = 'https://www.barrons.com/quote/stock/ph/xphs/%s/financials' % (stockSymbol)
response = get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Parsing data...")
stock = Stock.from_soup(soup)

print("Generating file...")
f = open('%s.csv' % (stock.symbol), 'w', newline='')
with f:
    fnames = ['name', 'symbol', 'field']
    fields = ['sales', 'expense', 'income', \
        'assets' , 'inventories', 'accounts_receivable', 'liabilities', 'equity', 'shareholders_equity']
    years = []
    for financial in stock.financials:
        if financial.year not in years:
            years.append(financial.year)
    fnames.extend(years)

    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    for field in fields:
        row = {}
        row['name'] = stock.name
        row['symbol'] = stock.symbol
        row['field'] = field
        for year in years:
            for financial in stock.financials:
                if financial.year == year:
                    row[year] = vars(financial)[field]

        writer.writerow(row)

print("Scrape completed!")
