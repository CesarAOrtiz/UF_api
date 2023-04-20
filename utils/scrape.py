from datetime import datetime
from typing import List
from bs4 import BeautifulSoup, ResultSet, Tag
from fastapi import HTTPException
from services import RequestsHttpClient, BeautifulsoupHtmlParser, WebScraper
from utils.errors import HTTPRequestError

Data = dict[str, List[str]]

base_url = "https://www.sii.cl/valores_y_fechas/uf/uf{}.htm"
min_date = datetime.strptime("01-01-2013", "%d-%m-%Y")

http_client = RequestsHttpClient()
html_parser = BeautifulsoupHtmlParser()
scraper = WebScraper(http_client, html_parser)


def validate_date(date: str) -> datetime:
    """
    Valida que la fecha ingresada esté dentro del rango permitido y la devuelve como un objeto datetime.

    Args:
        date (str): Fecha en formato 'dd-mm-yyyy' a validar.

    Returns:
        datetime: Objeto datetime correspondiente a la fecha ingresada.

    Raises:
        HTTPException(400): Si la fecha ingresada no está dentro del rango permitido.
    """
    try:
        date_obj = datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        raise HTTPException(
            status_code=400, detail="La fecha ingresada no está en el formato esperado (dd-mm-yyyy)")

    max_date = datetime.today()
    if date_obj < min_date or date_obj > max_date:
        raise HTTPException(
            status_code=400, detail=f"La fecha ingresada no está dentro del rango permitido {min_date.strftime('%d-%m-%Y')} - {max_date.strftime('%d-%m-%Y')}")
    return date_obj


def get_soup(date: datetime) -> BeautifulSoup:
    """
    Obtiene un objeto BeautifulSoup con el contenido HTML de la página que muestra los valores de la UF
    correspondientes a la fecha ingresada.

    Args:
        date (datetime): Fecha para la cual se desea obtener el contenido HTML de la página correspondiente.

    Returns:
        BeautifulSoup: Objeto BeautifulSoup con el contenido HTML de la página de valores de la UF.

    Raises:
        HTTPException: Si ocurre un error al obtener la página HTML de la URL especificada.
    """
    try:
        url = base_url.format(date.year)
        return scraper.scrape(url)
    except HTTPRequestError:
        raise HTTPException(
            status_code=500, detail="No se pudo obtener la página HTML de la URL especificada.")


def get_rows(soup: BeautifulSoup) -> ResultSet[Tag]:
    """
    La siguiente función recibe un objeto BeautifulSoup y retorna una lista de filas de una tabla HTML especificada por el selector CSS '#table_export tbody tr'.

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup que representa el árbol DOM del documento HTML.

    Returns:
        ResultSet[Tag]: Un conjunto de objetos Tag que representa las filas de la tabla especificada por el selector CSS.

    Raises:
        HTTPException: Si la tabla no se encuentra en la página HTML.
    """
    uf_table = soup.select_one('#table_export tbody')
    if uf_table is None:
        raise HTTPException(
            status_code=500, detail="No se pudo encontrar la tabla de valores de la UF en la página HTML.")
    return uf_table.select('tr')


def get_uf_data(rows: ResultSet[Tag]) -> Data:
    """
    Obtiene un diccionario con los valores de la UF para todos los días del mes correspondiente a la fecha ingresada.

    Args:
        rows (ResultSet[Tag]): Un conjunto de objetos Tag que representa las filas de la tabla especificada por el selector CSS.

    Returns:
        Data: Diccionario con los valores de la UF para todos los días del mes correspondiente a la fecha ingresada.
    """

    data = {}
    for uf in rows:
        if type(day := uf.find("th")) == Tag:
            months = [x.text for x in uf.find_all("td")]
            data[day.text] = months
    return data


def get_uf_for_date(data: Data, date_obj: datetime) -> str:
    """
    Obtiene el valor de la UF correspondiente a una fecha específica.

    Args:
        data (Data): Diccionario con los valores de la UF para todos los días del mes correspondiente a la fecha ingresada.
        date_obj (datetime): Fecha para la cual se desea obtener el valor de la UF.

    Returns:
        str: Valor de la UF correspondiente a la fecha ingresada.

    Raises:
        HTTPException(400): Si no hay un valor de UF correspondiente a la fecha ingresada.
    """
    try:
        day, month = date_obj.date().day, date_obj.date().month
        return data[str(day)][month-1]

    except KeyError:
        raise HTTPException(
            status_code=400, detail="No hay un valor de UF correspondiente a el día de la fecha ingresada.")

    except IndexError:
        raise HTTPException(
            status_code=400, detail="No hay un valor de UF correspondiente a el mes de la fecha ingresada.")
