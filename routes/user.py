from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import	users #carpeta.archivo imports nombreTabla
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)

#Listar 
@user.get('/users', response_model=list[User], tags=["Users"])
def get_users():
    return conn.execute(users.select()).fetchall()

# Listar por id
@user.get('/users/{id}', response_model=User, tags=["Users"])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()

# Guardar
@user.post('/users',  response_model=User, tags=["Users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    
    # result = conn.execute(users.insert().values(new_user))  
    # return conn.execute(users.select().where( users.c.id == result.lastrowid )).first() # users.c.id  -> tabla.columna.campo

    result = conn.execute(users.insert().values(new_user))
    inserted_row = conn.execute(users.select().where(users.c.id == result.lastrowid)).fetchone()
    inserted_user = dict(zip(inserted_row.keys(), inserted_row))
    return inserted_user

# Actualizar
@user.put('/users/{id}', response_model=User, tags=["Users"])
def update_user(id: str, user: User):
    conn.execute(users.update().values(name=user.name, email=user.email, password=f.encrypt(user.password)).where(users.c.id==id))
    return "usuario actualizado"

# Eliminar
@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def detele_user(id: str):
    result = conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)