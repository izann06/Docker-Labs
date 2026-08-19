import pymysql
import os
from fastapi import FastAPI, HTTPException


app = FastAPI(title="API de Biblioteca Personal")

# Obtener conexión a la base de datos
def get_db_connection():
  return pymysql.connect(
      host=os.getenv("DB_HOST", "db"),
      user=os.environ["DB_USER"],  # Lanza KeyError si no existe la variable
      password=os.environ["DB_PASSWORD"],
      database=os.environ["DB_NAME"],
      port=int(os.getenv("DB_PORT", "3306")),
      cursorclass=pymysql.cursors.DictCursor,
  )

# GET, para obtener todos los libros
@app.get("/libros")
def obtener_libros():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()
    conn.close()
    return libros

# POST, para crear libros
@app.post("/libros")
def crear_libro(nombre: str, autor: str):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO libros (nombre, autor) VALUES (%s, %s)", (nombre, autor))
        nuevo_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"mensaje": "Libro añadido con éxito", "id": nuevo_id, "nombre": nombre}

# PUT, para actualizar libros
@app.put("/libros/{libro_id}")
def marcar_leido(libro_id: int, leido: bool):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE libros SET leido = %s WHERE id = %s", (leido, libro_id))
        filas_afectadas = cursor.rowcount
    conn.commit()
    conn.close()
    
    if filas_afectadas == 0:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"mensaje": f"Libro {libro_id} actualizado"}

# DELETE, para borrar libros
@app.delete("/libros/{libro_id}")
def borrar_libro(libro_id: int):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
        filas_afectadas = cursor.rowcount
    conn.commit()
    conn.close()

    if filas_afectadas == 0:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"mensaje": "Libro eliminado correctamente"}