from bs4 import BeautifulSoup


class PSESearchResult(object):
    DOCUMENT_ID_INDEX = 1
    DATE_INDEX = 3

    def __init__(self, document_id: str, date: str):
        self.document_id: str = document_id
        self.date: str = date

    def __repr__(self):
        return "<PSESearchResult %s>" % (self.document_id)

    def __str__(self):
        return "<PSESearchResult %s>" % (self.document_id)

    @classmethod
    def from_soup(cls, soup: BeautifulSoup) -> 'PSESearchResult':
        data: BeautifulSoup = soup.find_all("td")

        # Trim the javascript function to get the document id.
        document_id = data[PSESearchResult.DOCUMENT_ID_INDEX].a['onclick'] \
            .replace("openPopup('", "") \
            .replace("');return false;", "")

        date = data[PSESearchResult.DATE_INDEX]

        return cls(document_id, date)

    @staticmethod
    def batch_from_soups(soups: BeautifulSoup):
        pse_search_results = []
        for soup in soups:
            search_result = PSESearchResult.from_soup(soup)
            pse_search_results.append(search_result)

        return pse_search_results