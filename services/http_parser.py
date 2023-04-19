from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class IHtmlParser(ABC):
    """
    Interfaz para un parser HTML que puede extraer elementos de una cadena HTML.
    """

    @abstractmethod
    def parse(self, html: str) -> BeautifulSoup:
        """
        Extrae elementos de una cadena HTML y devuelve un objeto BeautifulSoup.

        Args:
            html: Una cadena que contiene HTML.

        Returns:
            Un objeto BeautifulSoup que representa la estructura del HTML.
        """
        pass


class BeautifulsoupHtmlParser(IHtmlParser):
    def parse(self, html: str) -> BeautifulSoup:
        return BeautifulSoup(html, 'html.parser')
