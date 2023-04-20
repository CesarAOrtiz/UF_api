import unittest
from bs4 import BeautifulSoup
from fastapi import HTTPException
from utils import get_rows


class TestGetRows(unittest.TestCase):
    def test_get_rows(self):
        # Testeamos la función get_rows con una tabla válida e inválida

        # Caso válido
        html = "<table id='table_export'><tbody><tr><th>1</th><td>1000</td><td>2000</td></tr></tbody></table>"
        soup = BeautifulSoup(html, "html.parser")
        expected_output = soup.select("tr")
        self.assertEqual(get_rows(soup), expected_output)

        # Caso inválido - tabla no encontrada
        html = "<html><body><h1>Test HTML</h1></body></html>"
        soup = BeautifulSoup(html, "html.parser")
        with self.assertRaises(HTTPException):
            get_rows(soup)
