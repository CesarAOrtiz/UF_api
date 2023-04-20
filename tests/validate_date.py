import unittest
from datetime import datetime
from fastapi import HTTPException
from utils.scrape import validate_date


class TestValidateDate(unittest.TestCase):
    def test_valid_date(self):
        # Testeamos la función validate_date con casos válidos e inválidos
        date = "10-04-2023"

        # Caso válido
        expected_output = datetime(2023, 4, 10)
        self.assertEqual(validate_date(date), expected_output)

        # Caso inválido - fecha con formato incorrecto
        date = "2023-04-10"
        with self.assertRaises(HTTPException):
            validate_date(date)

        # Caso inválido - fecha fuera del rango permitido
        date = "10-04-1900"
        with self.assertRaises(HTTPException):
            validate_date(date)
