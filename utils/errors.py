class HTTPRequestError(Exception):
    """
    Clase de error personalizada para manejar excepciones de HTTPRequest.
    """
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f"{self.status_code}: {self.message}"
