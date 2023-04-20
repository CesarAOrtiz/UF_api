import unittest
from datetime import datetime
from bs4 import BeautifulSoup
from fastapi import HTTPException
from utils import get_uf_data, get_uf_for_date, get_rows


class TestGetUfForDate(unittest.TestCase):
    def test_get_uf_data(self):
        # Testeamos la función get_uf_data con una tabla válida e inválida

        # Caso válido
        html = "<table id='table_export'><tbody><tr><th>1</th><td>1000</td><td>2000</td></tr></tbody></table>"
        soup = BeautifulSoup(html, "html.parser")
        rows = get_rows(soup)
        expected_output = {"1": ["1000", "2000"]}
        self.assertEqual(get_uf_data(rows), expected_output)

        # Caso inválido - tabla no encontrada
        html = "<html><body><h1>Test HTML</h1></body></html>"
        soup = BeautifulSoup(html, "html.parser")

        with self.assertRaises(HTTPException):
            rows = get_rows(soup)
            get_uf_data(rows)

    def test_get_uf_for_date(self):
        # Testeamos la función get_uf_for_date con casos válidos e inválidos

        # Caso válido
        data = {"1": ["1000", "2000"]}
        date_obj = datetime(2021, 1, 1)
        expected_output = "1000"
        self.assertEqual(get_uf_for_date(data, date_obj), expected_output)

        # Caso inválido - fecha no encontrada
        data = {"1": ["1000", "2000"]}
        date_obj = datetime(2021, 1, 2)
        with self.assertRaises(HTTPException):
            get_uf_for_date(data, date_obj)


if __name__ == '__main__':
    unittest.main()
