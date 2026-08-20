# 🐍 Proyecto 4.0: API REST (FastAPI) + MySQL + Adminer

## 🎯 Objetivo del Proyecto
Implementar una **API RESTful CRUD completa** para una Biblioteca Personal, usando Python y FastAPI como alternativa al stack Node.js. Se introduce la gestión profesional de credenciales mediante archivos `.env` y el uso de Adminer como panel de administración web para MySQL.

---

## 🛠️ Tecnologías Utilizadas

- **FastAPI (Python):** Framework web moderno y de alto rendimiento para APIs REST.
- **PyMySQL:** Conector Python para comunicación con MySQL.
- **MySQL 8.0:** Motor de base de datos relacional.
- **Adminer:** Panel de administración web ligero y universal para bases de datos.
- **Docker Compose:** Orquestación de los 3 servicios.

---

## 📂 Estructura de Archivos

```text
4.0-API REST (FastAPI) + MySql + Adminer/
├── .env             # Variables de entorno reales (ignorado en Git)
├── .env.example     # Plantilla de variables de entorno para nuevos desarrolladores
├── Dockerfile       # Definición de la imagen de la API Python
├── docker-compose.yml
├── main.py          # API FastAPI con endpoints CRUD para /libros
└── requirements.txt # Dependencias Python (fastapi, pymysql, uvicorn)
```

---

## 🏗️ Conceptos Clave Aprendidos

1. **Gestión de Secretos con `.env`:** Ninguna contraseña está escrita en `docker-compose.yml`. Se definen en `.env` e inyectan con la sintaxis `${VARIABLE}`. El archivo `.env.example` documenta las variables sin exponer valores reales.
2. **API CRUD completa:** Implementación de los 4 verbos HTTP principales:
   - `GET /libros`: Lista todos los libros.
   - `POST /libros`: Crea un nuevo libro.
   - `PUT /libros/{id}`: Actualiza un libro existente.
   - `DELETE /libros/{id}`: Elimina un libro.
3. **`restart: always` como solución a Race Conditions:** MySQL tarda unos segundos en arrancar. Con `restart: always`, si la API falla al conectarse porque MySQL aún no está listo, Docker la reinicia automáticamente hasta que la conexión sea exitosa.
4. **Documentación Automática (Swagger UI):** FastAPI genera automáticamente una interfaz web interactiva en `/docs` para probar todos los endpoints sin necesidad de Postman u otro cliente HTTP externo.
5. **Bind Mount para Desarrollo (`.:/app`):** Los cambios en el código Python se sincronizan en tiempo real con el contenedor, sin necesidad de reconstruir la imagen.

---

## ⚙️ Variables de Entorno (`.env`)

Copia `.env.example` y ajusta los valores:

```bash
cp .env.example .env
```

| Variable | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `MYSQL_ROOT_PASSWORD` | Contraseña del usuario root de MySQL | `root` |
| `DB_DATABASE` | Nombre de la base de datos | `biblioteca` |
| `DB_USER` | Usuario de la base de datos | `usuario` |
| `DB_PASSWORD` | Contraseña del usuario | `1234` |
| `DB_PORT` | Puerto de conexión a MySQL | `3306` |

---

## 🌐 Servicios y Puertos

| Servicio | Puerto Host | Puerto Contenedor | Acceso |
| :--- | :--- | :--- | :--- |
| FastAPI | `8000` | `8000` | `http://localhost:8000` |
| Swagger UI (Docs) | `8000` | `8000` | `http://localhost:8000/docs` |
| MySQL 8.0 | `3306` | `3306` | `localhost:3306` |
| Adminer | `8080` | `8080` | `http://localhost:8080` |

---

## 💻 Comandos para Ejecutar

```bash
cd "4.0-API REST (FastAPI) + MySql + Adminer"

# 1. Crear el archivo de entorno
cp .env.example .env

# 2. Construir y levantar todos los servicios
docker compose up -d --build

# 3. Ver logs de la API
docker compose logs -f api

# 4. Detener
docker compose down
```

### Conectar Adminer a MySQL

1. Accede a `http://localhost:8080`
2. Sistema: `MySQL`, Servidor: `db`, Usuario y contraseña según tu `.env`
