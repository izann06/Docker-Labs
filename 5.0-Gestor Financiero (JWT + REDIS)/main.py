from fastapi import FastAPI
from database import init_db
from routers import auth, categorias, transacciones, balance

app = FastAPI(title="Gestor de Finanzas API")

@app.on_event("startup")
def startup():
    init_db()

# Registro de routers por módulo
app.include_router(auth.router)
app.include_router(categorias.router)
app.include_router(transacciones.router)
app.include_router(balance.router)