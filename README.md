# Portfolio de Python · Miguel García Castañeda

Página web de portfolio hecha con Python y Flask. Incluye una calculadora interactiva que envía las operaciones a un backend Python.

## Requisitos
- Python 3.10 o posterior
- pip

## Ejecutar en Windows
1. Descomprime la carpeta.
2. Abre una terminal dentro de `portfolio_python_web`.
3. Instala las dependencias:
   `py -m pip install -r requirements.txt`
4. Arranca la web:
   `py app.py`
5. Abre en el navegador: http://127.0.0.1:5000

## Ejecutar en Linux/macOS
`python3 -m pip install -r requirements.txt`
`python3 app.py`

## Contenido
- Portfolio responsive con acento morado `#B22AE6`.
- Fotografía integrada como archivo local.
- Calculadora funcional conectada al backend Python.
- Proyectos basados en los scripts del ZIP aportado.
- No se presenta la calculadora de nóminas como un programa terminado.

La aplicación está preparada para uso local. Antes de desplegarla públicamente, configura un servidor WSGI y desactiva el modo debug.
