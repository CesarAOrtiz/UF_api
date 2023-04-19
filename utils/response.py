from typing import Optional, Generic, TypeVar
from fastapi import status
from pydantic.generics import GenericModel

T = TypeVar('T')


class Response(GenericModel, Generic[T]):
    """
    Modelo genérico para las respuestas de la API.

    Args:
        T: Tipo de dato que se espera que se incluya en la propiedad `data`.

    Atributos:
        success (bool): Indica si la acción se realizó correctamente.
        status_code (int): Código de estado HTTP de la respuesta.
        message (str): Mensaje de éxito o error de la respuesta.
        data (T, opcional): Datos adicionales de la respuesta.

    Ejemplo:
        >>> response = Response[int](data=42)
    """
    success: bool = True
    status_code: int = status.HTTP_200_OK
    message: str = "La acción se ha realizado correctamente"
    data: Optional[T] = None


class ErrorResponse(Response[T], Generic[T]):
    """
    Modelo genérico para las respuestas de error de la API.

    Args:
        T: Tipo de dato que se espera que se incluya en la propiedad `data`.

    Atributos:
        success (bool): Indica si la acción se realizó correctamente.
        status_code (int): Código de estado HTTP de la respuesta.
        message (str): Mensaje de error de la respuesta.
        data (T, opcional): Datos adicionales de la respuesta.

    Ejemplo:
        >>> error = ErrorResponse[int](message="Ocurrió un error")
    """
    success: bool = False
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = "Error en la acción"
