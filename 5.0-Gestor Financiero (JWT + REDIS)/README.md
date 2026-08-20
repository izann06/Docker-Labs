# 💰 Proyecto 5.0: Gestor Financiero (JWT + Redis)

## 🎯 Objetivo del Proyecto
Diseñar una **arquitectura backend profesional y escalable** de 4 servicios orquestados en Docker para gestionar finanzas personales. Implementa los dos pilares de seguridad de cualquier API de producción: **autenticación con tokens JWT** y **hashing seguro de contraseñas con Bcrypt**, junto con una **capa de caché ultrarrápida en Redis** para optimizar consultas costosas.

---

## 🛠️ Tecnologías Utilizadas

- **FastAPI (Python):** Framework web moderno y de alto rendimiento.
- **MySQL 8.0:** Motor de base de datos relacional para persistencia.
- **Redis (Alpine):** Base de datos en memoria para caché de resultados.
- **Adminer:** Panel de administración web para MySQL.
- **JWT (PyJWT):** Generación y validación de tokens de autenticación.
- **Bcrypt:** Hashing seguro e irreversible de contraseñas.
- **Docker Compose:** Orquestación de los 4 servicios.

---

## 📂 Estructura de Archivos

```text
5.0-Gestor Financiero (JWT + REDIS)/
├── .env                 # Variables de entorno reales (ignorado en Git)
├── dockerfile           # Definición de la imagen de la API
├── docker-compose.yml   # Orquestación de los 4 servicios
├── main.py              # Punto de entrada, montaje de routers
├── database.py          # Conexiones MySQL y Redis, inicialización de tablas
├── security.py          # Hashing Bcrypt, generación/validación JWT
├── requirements.txt     # Dependencias Python
└── routers/
    ├── auth.py          # POST /registro, POST /login
    ├── categorias.py    # GET /categorias, POST /categorias
    ├── transacciones.py # POST /transacciones
    └── balance.py       # GET /balance (protegido con JWT + caché Redis)
```

---

## 🏗️ Conceptos Clave Aprendidos

### 1. Autenticación con JWT
- `POST /registro` hashea la contraseña con **Bcrypt** antes de guardarla en MySQL. Nunca se almacena la contraseña en texto plano.
- `POST /login` verifica la contraseña y genera un **token JWT Bearer** firmado con `SECRET_KEY`. El token lleva el `username` codificado y caduca en 30 minutos.
- Las rutas protegidas usan la dependencia `get_current_user` que decodifica y valida el JWT en cada petición.

### 2. Caché con Redis e Invalidación Automática
- **1ª consulta a `GET /balance`:** Redis está vacío → la API ejecuta `SUM(ingresos) - SUM(gastos)` en MySQL, guarda el resultado en Redis y responde con `"origen": "🐢 MySQL"`.
- **2ª consulta a `GET /balance`:** El dato existe en RAM → Redis responde en microsegundos con `"origen": "⚡ Redis"` sin tocar la base de datos.
- **Invalidación:** Cada `POST /transacciones` ejecuta `redis_client.delete("balance_total")` para garantizar que el próximo cálculo sea fresco.

### 3. Arquitectura Modular con Routers
Separación de endpoints por dominio usando `app.include_router(...)`. Cada router es un módulo independiente, mejorando la mantenibilidad y escalabilidad del código.

---

## ⚙️ Variables de Entorno (`.env`)

```env
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=finanzas
DB_USER=izan
DB_PASSWORD=1234
SECRET_KEY=clave_super_secreta_para_jwt
```

---

## 🌐 Servicios y Puertos

| Servicio | Puerto Host | Puerto Contenedor | Acceso |
| :--- | :--- | :--- | :--- |
| FastAPI (JWT + Redis) | `8000` | `8000` | `http://localhost:8000` |
| Swagger UI (Docs) | `8000` | `8000` | `http://localhost:8000/docs` |
| MySQL 8.0 | `3306` | `3306` | `localhost:3306` |
| Redis (Alpine) | `6379` | `6379` | `localhost:6379` |
| Adminer | `8080` | `8080` | `http://localhost:8080` |

---

## 💻 Comandos para Ejecutar

```bash
cd "5.0-Gestor Financiero (JWT + REDIS)"

# Construir y levantar los 4 servicios
docker compose up -d --build

# Ver logs de la API
docker compose logs -f api

# Detener
docker compose down
```

---

## 🔀 Flujo de Uso (desde Swagger UI en `/docs`)

1. **`POST /registro`** → Crear cuenta (contraseña se hashea con Bcrypt).
2. **`POST /login`** → Obtener `access_token` JWT.
3. Pulsar **`Authorize 🔓`** en Swagger UI y pegar el token.
4. **`POST /categorias`** → Crear categoría (ej: "Nómina", "Alquiler").
5. **`POST /transacciones`** → Registrar ingresos/gastos (invalida caché Redis).
6. **`GET /balance`** *(protegido)* → Consultar balance total (1ª vez desde MySQL, siguientes desde Redis).

---

## 🧠 Errores Comunes y Aprendizajes

### `405 Method Not Allowed` en el navegador
La barra de direcciones solo hace peticiones `GET`. Para endpoints `POST` hay que usar Swagger UI (`/docs`), Postman o cURL.

### `401 Not Authenticated` en rutas protegidas
El navegador no adjunta cabeceras `Authorization`. Hay que autenticarse mediante el botón **`Authorize 🔓`** de Swagger UI antes de llamar a rutas JWT.

### Race Conditions entre MySQL y la API
MySQL tarda unos segundos en arrancar. Se implementó un bucle de reintentos en el evento `startup()` de FastAPI para esperar a que la base de datos esté lista antes de ejecutar migraciones.

### Fuga de Conexiones (`Lock wait timeout exceeded`)
Si una consulta falla sin cerrar la conexión, MySQL retiene bloqueos que congelan las siguientes peticiones. Solución: proteger **todas** las operaciones con `try ... finally: conn.close()`.

### Incompatibilidad `passlib` + `bcrypt 4.x`
Las versiones recientes de `bcrypt` eliminaron atributos internos que `passlib` usaba. Solución: usar directamente `bcrypt.hashpw` y `bcrypt.checkpw` sin `passlib`.
