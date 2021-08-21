from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'mensaje': 'Hola, great world!'}

@app.get('/pythonistas')
def obtener_pythonistas():
    return ['elena','pablo','hola','chido']


# comando para correr esto
# uvicorn main:app --reload