from fastapi import APIRouter, HTTPException
from database import get_db_connection

router = APIRouter(prefix="/categorias", tags=["Categorías"])

@router.get("")
def obtener_categorias():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM categorias")
            categorias = cursor.fetchall()
        return categorias
    finally:
        conn.close()

@router.post("")
def crear_categoria(nombre: str):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO categorias (nombre) VALUES (%s)", (nombre,))
            nuevo_id = cursor.lastrowid
        conn.commit()
        return {"mensaje": "Categoría creada", "id": nuevo_id, "nombre": nombre}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()
