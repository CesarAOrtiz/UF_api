from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from utils import (ErrorResponse, Response, get_rows, get_soup,
                   get_uf_data, get_uf_for_date, validate_date)

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(req: Request, exc: StarletteHTTPException) -> JSONResponse:
    response = ErrorResponse(
        success=False, message=exc.detail, status_code=exc.status_code)
    return JSONResponse(response.dict(), status_code=exc.status_code)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/uf", tags=["Unidad de Fomento"])
async def uf(date: str) -> Response[str]:
    date_obj = validate_date(date)
    soup = get_soup(date_obj)
    uf_rows = get_rows(soup)
    uf_data = get_uf_data(uf_rows)
    response = get_uf_for_date(uf_data, date_obj)
    return Response(data=response)
