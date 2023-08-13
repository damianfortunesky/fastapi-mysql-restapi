from fastapi import FastAPI
from routes.user import user

app = FastAPI(
        openapi_tags=[{
                "name": "users",
                "descripcion": "rutas de usuarios"
        }]
) 

app.include_router(user)

@app.get('/')
def helloword():
        return "Raiz"


# Crear proyecto: "fastapi-mysql-restapi"

# Crear entorno virtual para el proyecto: 

        # Abrimos Anaconda Prompt -> cd E:\Escritorio\fastapi-mysql-restapi

        # Creamos -> conda create --name  fastapi-mysql python=3 conda create --name  fastapi-mysql python=3

        # Activar entorno -> conda activate fastapi-mysql

        # Seleccionar entorno creado -> Ctrl + P -> >Python: Select Interpreter 

# Instalar paquetes FastAPI

    # pip install fastapi uvicorn

    # conda install pymysql

    # pip install sqlalchemy

    # pip install cryptography

    # Crear estructura proyecto:

        # routes -> sirve para crear urls para acceder a los recursos
        # models -> sirve para guardar modelos de datos que definen la estructura del almacenamiento
        # schemas -> sirve para definir que datos devuelvo y recibo del cliente
        # config -> configurar la conexion a db

# server  -> uvicorn app:app --reload 

    