from core.PSE import PSE, PSEFinancialTemplate, PSEDocument
from models.quarterly_report import QuarterlyReport
from typing import Iterable

print("Searching reports...")
results = PSE.search('MEG', PSEFinancialTemplate.QUARTERLY,
                     '05-05-2017', '05-05-2019')

i: int = 0
quarterly_reports: Iterable[QuarterlyReport] = []
for result in results:
    i = i + 1
    print("Getting report (%s/%s)..." % (i, len(results)))

    quarterly_report: QuarterlyReport = PSEDocument.get_quarterly_report(
        result.document_id)
    quarterly_reports.append(quarterly_report)

print(quarterly_reports)
