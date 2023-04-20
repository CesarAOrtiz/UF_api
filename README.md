# Obtención del valor de la Unidad de Fomento (UF)

Este proyecto busca obtener el valor de la Unidad de Fomento (UF) para una fecha específica en Chile. La UF es una unidad de medida indexada al valor de la inflación que se utiliza en Chile para determinar precios y valores de bienes y servicios.

Para obtener el valor de la UF, se hace un web scraping al sitio del Servicio de Impuestos Internos (SII) de Chile, que publica diariamente el valor de la UF.

## Ejecutar localmente

Clonar el proyecto

```bash
  git clone https://github.com/CesarAOrtiz/UF_api.git
```

Ir al directorio del proyecto

```bash
  cd UF_api
```

Crear un entorno virtual

```bash
  python3 -m venv env
```

Activar el entorno virtual

```bash
  env/bin/activate
```

Instalar dependecias

```bash
  pip install -r requirements.txt
```

Iniciar el servidor

```bash
  uvicorn main:app --reload
```

Este comando iniciará el servidor y lo mantendrá escuchando en http://localhost:8000. El parámetro --reload hace que el servidor se recargue automáticamente cuando detecta cambios en el código.

Abre un navegador web y navega a http://localhost:8000/docs para ver la documentación de la API y probar los endpoints.

## Referencia del API

#### Obtener unidad de fomento para una fecha

```http
  GET /api/uf
```

| Parametros | Tipo     | Descripción                                 |
| :--------- | :------- | :------------------------------------------ |
| `date`     | `string` | **Requerido**. Fecha con formato dd-mm-yyyy |

## Recursos

- [Unidad de Fomento](https://www.sii.cl/valores_y_fechas/uf/uf2023.htm)
