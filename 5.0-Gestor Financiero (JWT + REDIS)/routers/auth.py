from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import pymysql

from database import get_db_connection
from security import hash_password, verify_password, create_access_token

router = APIRouter(tags=["Autenticación"])

@router.post("/registro")
def registrar_usuario(username: str, password: str):
    password_hash = hash_password(password)
    
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (username, password_hash) VALUES (%s, %s)", 
                (username, password_hash)
            )
        conn.commit()
    except pymysql.err.IntegrityError:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    finally:
        conn.close()
        
    return {"mensaje": "Usuario creado con éxito. Ya puedes iniciar sesión."}

@router.post("/login")
def iniciar_sesion(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE username = %s", (form_data.username,))
            usuario = cursor.fetchone()
    finally:
        conn.close()

    if not usuario or not verify_password(form_data.password, usuario['password_hash']):
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")

    token = create_access_token(data={"sub": usuario['username']})
    return {"access_token": token, "token_type": "bearer"}
