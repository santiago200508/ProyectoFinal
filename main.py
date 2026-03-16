from fastapi import FastAPI
from metodos import rutas

app = FastAPI()

app.include_router(rutas.router)
