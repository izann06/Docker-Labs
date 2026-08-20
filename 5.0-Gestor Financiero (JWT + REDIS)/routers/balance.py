from fastapi import APIRouter, Depends
from database import get_db_connection, get_redis_connection
from security import get_current_user

router = APIRouter(prefix="/balance", tags=["Balance"])

@router.get("")
def obtener_balance(usuario_actual: str = Depends(get_current_user)):
    redis_client = get_redis_connection()
    
    # 1. Intentar leer el balance desde Redis (Caché RAM)
    balance_cacheado = redis_client.get("balance_total")
    
    if balance_cacheado is not None:
        return {
            "balance": float(balance_cacheado), 
            "origen": "⚡ Redis (Caché ultrarrápida)",
            "usuario": usuario_actual
        }
    
    # 2. Si Redis está vacío, hacer el cálculo en MySQL
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT SUM(cantidad) as total FROM transacciones WHERE tipo = 'ingreso'")
            ingresos = cursor.fetchone()['total'] or 0
            
            cursor.execute("SELECT SUM(cantidad) as total FROM transacciones WHERE tipo = 'gasto'")
            gastos = cursor.fetchone()['total'] or 0
            
        balance_real = float(ingresos) - float(gastos)
    finally:
        conn.close()
    
    # 3. Guardar el cálculo en Redis (expira en 3600 segundos)
    redis_client.setex("balance_total", 3600, balance_real)
    
    return {
        "balance": balance_real, 
        "origen": "🐢 MySQL (Cálculo original)",
        "usuario": usuario_actual
    }
