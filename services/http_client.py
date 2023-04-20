from abc import ABC, abstractmethod
import requests
from utils.errors import HTTPRequestError
import urllib.request


class IHttpClient(ABC):
    """
    Interfaz para un cliente HTTP que puede realizar solicitudes GET.
    """
    @abstractmethod
    def get(self, url: str) -> str:
        """
        Realiza una solicitud HTTP GET a la URL especificada.

        Args:
            url (str): URL a la cual se realizará la solicitud HTTP.

        Returns:
            str: El contenido de la respuesta HTTP como una cadena de texto.
        """
        pass


class RequestsHttpClient(IHttpClient):
    """
    Implementación de la interfaz IHttpClient utilizando la biblioteca requests.
    """

    def get(self, url: str) -> str:
        """
        Realiza una solicitud HTTP GET a la URL especificada utilizando la biblioteca requests.

        Args:
            url (str): URL a la cual se realizará la solicitud HTTP.

        Returns:
            str: El contenido de la respuesta HTTP como una cadena de texto.

        Raises:
            HTTPRequestError: Si se produce un error al hacer la solicitud HTTP.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.HTTPError as e:
            raise HTTPRequestError(
                e.response.status_code, e.response.text) from e


class UrllibHttpClient(IHttpClient):
    """
    Implementación de la interfaz IHttpClient utilizando la biblioteca urllib.
    """

    def get(self, url: str) -> str:
        """
        Realiza una solicitud HTTP GET a la URL especificada utilizando la biblioteca urllib.

        Args:
            url (str): URL a la cual se realizará la solicitud HTTP.

        Returns:
            str: El contenido de la respuesta HTTP como una cadena de texto.

        Raises:
            HTTPRequestError: Si se produce un error al hacer la solicitud HTTP.
        """
        with urllib.request.urlopen(url) as response:
            try:
                return response.read()
            except urllib.request.HTTPError as e:
                raise HTTPRequestError(e.code, e.reason) from e
