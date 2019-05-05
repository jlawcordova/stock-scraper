from requests import get, post, Response
from bs4 import BeautifulSoup
from typing import Iterable

from models.pse_search_result import PSESearchResult
from models.quarterly_report import QuarterlyReport, AnnualReport


class PSE(object):
    SEARCH_URL = 'http://edge.pse.com.ph/financialReports/search.ax'

    @staticmethod
    def search(symbol: str, template: str, from_date: str,
               to_date: str) -> Iterable[PSESearchResult]:
        data = {
            'keyword': symbol,
            'tmplNm': template,
            'fromDate': from_date,
            'toDate': to_date
        }

        response: Response = post(PSE.SEARCH_URL, data)

        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        rows: BeautifulSoup = soup.tbody.find_all("tr")

        results: Iterable[PSESearchResult] = PSESearchResult.batch_from_soups(
            rows)

        return results


class PSEDocument(object):
    DOCUMENT_URL = 'http://edge.pse.com.ph/openDiscViewer.do'
    DOWNLOAD_FILE_URL = 'http://edge.pse.com.ph/downloadHtml.do'

    @staticmethod
    def get_quarterly_report(document_id):
        # First, get the file ID of the document.
        response: Response = get(PSEDocument.DOCUMENT_URL, {
            'edge_no': document_id
        })

        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        # Trim to get the quarterly report file id.
        file_id: str = soup.iframe['src'] \
            .replace('/downloadHtml.do?file_id=', '')

        # Second, get the quarterly report file itself.
        response: Response = get(PSEDocument.DOWNLOAD_FILE_URL, {
            'file_id': file_id
        })
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        return QuarterlyReport.from_soup(soup)

    @staticmethod
    def get_annual_report(document_id):
        # First, get the file ID of the document.
        response: Response = get(PSEDocument.DOCUMENT_URL, {
            'edge_no': document_id
        })

        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        # Trim to get the quarterly report file id.
        file_id: str = soup.iframe['src'] \
            .replace('/downloadHtml.do?file_id=', '')

        # Second, get the quarterly report file itself.
        response: Response = get(PSEDocument.DOWNLOAD_FILE_URL, {
            'file_id': file_id
        })
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        return AnnualReport.from_soup(soup)


class PSEFinancialTemplate(object):
    QUARTERLY = 'Quarterly'
    ANNUAL = 'Annual'
