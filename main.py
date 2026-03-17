from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from metodos import rutas

app = FastAPI()

app.include_router(rutas.router)

@app.get("/")
def root():
    return RedirectResponse(url="/productos")