from fastapi import APIRouter, HTTPException
from database import get_db_connection, get_redis_connection

router = APIRouter(prefix="/transacciones", tags=["Transacciones"])

@router.post("")
def crear_transaccion(concepto: str, cantidad: float, tipo: str, categoria_id: int):
    if tipo not in ["ingreso", "gasto"]:
        raise HTTPException(status_code=400, detail="El tipo debe ser 'ingreso' o 'gasto'")

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO transacciones (concepto, cantidad, tipo, categoria_id) 
                VALUES (%s, %s, %s, %s)
            """, (concepto, cantidad, tipo, categoria_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()

    # REDIS: Al añadir un gasto/ingreso, eliminamos el caché del balance
    redis_client = get_redis_connection()
    redis_client.delete("balance_total")
    
    return {"mensaje": "Transacción registrada con éxito"}
