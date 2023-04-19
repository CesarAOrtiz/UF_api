from .http_client import IHttpClient
from .http_parser import IHtmlParser
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class IWebScraper(ABC):
    """
    Interfaz para extraer datos de páginas web utilizando un cliente HTTP y un parser HTML.
    """
    @abstractmethod
    def scrape(self, url: str) -> BeautifulSoup:
        """
        Extrae texto de la página web en la URL proporcionada utilizando el parser HTML especificado.

        Args:
            url: URL de la página web a analizar.

        Returns:
            Lista de strings que contienen el texto de los elementos seleccionados.
        """
        pass


class WebScraper(IWebScraper):
    """
    Clase para extraer datos de páginas web utilizando un cliente HTTP y un parser HTML.
    """

    def __init__(self, http_client: IHttpClient, html_parser: IHtmlParser):
        """
        Inicializa un nuevo objeto WebScraper con el cliente HTTP y el parser HTML especificados.

        Args:
            http_client: Objeto que implementa la interfaz HttpClient para realizar las solicitudes HTTP.
            html_parser: Objeto que implementa la interfaz HtmlParser para analizar el HTML de la página web.
        """
        self.http_client = http_client
        self.html_parser = html_parser

    def scrape(self, url: str):
        """
        Extrae texto de la página web en la URL proporcionada utilizando el parser HTML especificado.

        Args:
            url: URL de la página web a analizar.

        Returns:
            Lista de strings que contienen el texto de los elementos seleccionados.

        Raises:
            HTTPError: Si se produce un error al hacer la solicitud HTTP.
        """
        html = self.http_client.get(url)
        soup = self.html_parser.parse(html)
        return soup
