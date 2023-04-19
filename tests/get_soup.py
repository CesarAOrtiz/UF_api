import unittest
from datetime import datetime
from bs4 import BeautifulSoup
from fastapi import HTTPException
from utils.scrape import get_soup


class TestGetSoup(unittest.TestCase):
    def test_get_soup(self):
        # Testeamos la función get_soup con una URL válida e inválida

        # Caso válido
        date = datetime.today()
        expected_output = BeautifulSoup(
            "<html><body><h1>Test HTML</h1></body></html>", "html.parser")
        self.assertEqual(get_soup(date), expected_output)

        # Caso inválido - URL no existente
        date = datetime(2023, 1, 1)
        with self.assertRaises(HTTPException):
            get_soup(date)
