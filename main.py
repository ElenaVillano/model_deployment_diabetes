from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

lista_pythonistas = ['elena','pablo','hola','chido']

class Pythonista(BaseModel):
    nombre: str
    ciudad: str
    edad: Optional[int] = None
    perfil: str

class PythonistaOut(BaseModel):
    nombre: str
    fecha_creacion: datetime

@app.get('/')
def index():
    return {'mensaje': 'Hola, great world!'}

@app.get('/pythonistas')
def obtener_pythonistas(skip: int=0, limit: int=3):
    return lista_pythonistas[skip: skip + limit]


@app.get('/pythonistas/{pythonista_id}')
def obtener_pythonista_by_id(pythonista_id: int):
    return {'pythonista': pythonista_id}

@app.post('/pythonistas', status_code = 201, response_model=PythonistaOut)
def crear_pythonista(pythonista: Pythonista):
    print(Pythonista)

    out = PythonistaOut(nombre=pythonista.nombre,
                        fecha_creacion=datetime.now())
    return out



# comando para correr esto
# uvicorn main:app --reload