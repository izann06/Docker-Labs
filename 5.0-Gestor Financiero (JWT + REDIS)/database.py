import os
import time
import pymysql
import redis

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        cursorclass=pymysql.cursors.DictCursor,
    )

def get_redis_connection():
    # decode_responses=True convierte los bytes de Redis a strings normales de Python
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=6379,
        decode_responses=True
    )

def init_db():
    conn = None
    retries = 10
    while retries > 0:
        try:
            conn = get_db_connection()
            break
        except Exception as e:
            print(f"Esperando conexión con la base de datos... ({e})")
            retries -= 1
            time.sleep(2)

    if not conn:
        raise Exception("No se pudo conectar a la base de datos MySQL tras varios intentos.")

    with conn.cursor() as cursor:
        # 1. Tabla de Categorías (Tabla Padre)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL UNIQUE
            )
        """)
        
        # 2. Tabla de Transacciones (Tabla Hija)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                concepto VARCHAR(255) NOT NULL,
                cantidad DECIMAL(10, 2) NOT NULL,
                tipo ENUM('ingreso', 'gasto') NOT NULL,
                categoria_id INT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE SET NULL
            )
        """)

        # 3. Tabla de Usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL
            )
        """)
    conn.commit()
    conn.close()
