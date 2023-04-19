from abc import ABC, abstractmethod
import requests


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
            HTTPError: Si se produce un error al hacer la solicitud HTTP.
        """
        response = requests.get(url)
        response.raise_for_status()
        return response.text
