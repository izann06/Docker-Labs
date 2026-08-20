# 🐳 Docker Labs & Playground

Este repositorio es mi laboratorio personal para aprender y practicar Docker y Docker Compose de forma incremental.

Abarca desde empaquetar una aplicación básica con un `Dockerfile` hasta la orquestación de arquitecturas multicontenedor con APIs (Node.js y FastAPI), bases de datos relacionales (PostgreSQL y MySQL), volúmenes persistentes, redes internas y paneles de administración (pgAdmin y Adminer).

---

## 🛠️ Tecnologías y Conceptos Clave

- **Herramientas de Contenedores:** Docker, Dockerfiles, Docker Compose.
- **Runtimes & Frameworks:** Node.js (HTTP nativo y Express.js), Python (FastAPI, PyMySQL).
- **Bases de Datos & GUIs:** PostgreSQL + pgAdmin, MySQL + Adminer.
- **Conceptos de Arquitectura:**
  - **Networking Interno:** Comunicación aislada entre contenedores mediante la red interna de Docker y resolución DNS por nombre de servicio.
  - **Persistencia de Datos:** Uso de *Named Volumes* para la persistencia de datos en bases de datos y *Bind Mounts* para la sincronización de código local en tiempo real durante el desarrollo.
  - **Gestión de Configuración:** Inyección de variables de entorno directamente en Compose o mediante archivos `.env`.

---

## 📂 Estructura del Laboratorio

| Directorio Real | Tecnologías | Descripción / Concepto Clave |
| :--- | :--- | :--- |
| `1.0-API de Tareas (Node.js + PostgreSQL) DockerFile` | Node.js | Empaquetado básico de una API usando un `Dockerfile` nativo. |
| `2.0-API de Tareas (Node.js + PostgreSQL) DockerCompose` | Node.js, Docker Compose | Orquestación inicial con Compose y montaje de volúmenes en vivo (*Bind Mounts*). |
| `3.0-API de Tareas + PostgreSQL + pgAdmin` | Express.js, PostgreSQL, pgAdmin | Arquitectura de 3 servicios, comunicación en red interna y persistencia con *Named Volume*. |
| `4.0-API REST (FastAPI) + MySql + Adminer` | FastAPI, MySQL, Adminer | API RESTful CRUD completa en Python, inyección de variables `.env` y gestor Adminer. |
| `5.0-Gestor Financiero (JWT + REDIS)` | FastAPI, MySQL 8.0, Redis, Adminer, JWT, Bcrypt | Arquitectura modular multicontenedor con autenticación JWT, hashing seguro y caché en memoria con Redis e invalidación automática. |

---

## 🔬 Detalle y Ejecución de los Proyectos

### 1.0 API de Tareas (Node.js + PostgreSQL) DockerFile
- **Directorio:** `1.0-API de Tareas (Node.js + PostgreSQL) DockerFile`
- **Tecnologías:** Node.js (HTTP nativo), Docker CLI.
- **Concepto clave:** Construcción manual de una imagen ligera basada en `node:20-alpine`, definición del directorio de trabajo (`WORKDIR /app`) y exposición del puerto 3000.
- **Cómo ejecutar:**
  ```bash
  cd "1.0-API de Tareas (Node.js + PostgreSQL) DockerFile"
  docker build -t api-node-dockerfile .
  docker run -d -p 3000:3000 --name api-node-container api-node-dockerfile
  ```
- **Acceso:** `http://localhost:3000`

---

### 2.0 API de Tareas (Node.js + PostgreSQL) DockerCompose
- **Directorio:** `2.0-API de Tareas (Node.js + PostgreSQL) DockerCompose`
- **Tecnologías:** Node.js, Docker Compose.
- **Concepto clave:** Automatización del build y despliegue usando `docker-compose.yml`. Introduce *Bind Mounts* (`- .:/app`) para sincronizar cambios en el código local con el contenedor sin necesidad de reconstruir la imagen.
- **Cómo ejecutar:**
  ```bash
  cd "2.0-API de Tareas (Node.js + PostgreSQL) DockerCompose"
  docker compose up -d --build
  ```
- **Acceso:** `http://localhost:3001` (puerto host 3001 mapeado al 3000 interno del contenedor).

---

### 3.0 API de Tareas + PostgreSQL + pgAdmin
- **Directorio:** `3.0-API de Tareas + PostgreSQL + pgAdmin`
- **Tecnologías:** Express.js, PostgreSQL 16, pgAdmin 4.
- **Concepto clave:** Orquestación de 3 servicios (`api`, `db`, `pgadmin`). La API Express conecta a la base de datos mediante la resolución DNS interna de Docker (`DB_HOST=db`). Los datos de la base de datos se persisten en el volumen nombrado `pgdata`.
- **Variables de Entorno (definidas en docker-compose.yml):**
  - PostgreSQL (`db`): `POSTGRES_USER=usuario`, `POSTGRES_PASSWORD=1234`, `POSTGRES_DB=base_tareas`
  - pgAdmin (`pgadmin`): `PGADMIN_DEFAULT_EMAIL=user@user.com`, `PGADMIN_DEFAULT_PASSWORD=root`
- **Cómo ejecutar:**
  ```bash
  cd "3.0-API de Tareas + PostgreSQL + pgAdmin"
  docker compose up -d --build
  ```
- **Acceso y Servicios:**
  - **API Express:** `http://localhost:3000`
  - **pgAdmin Web UI:** `http://localhost:5050` (Email: `user@user.com`, Contraseña: `root`, Host de conexión a BD: `db`)

---

### 4.0 API REST (FastAPI) + MySql + Adminer
- **Directorio:** `4.0-API REST (FastAPI) + MySql + Adminer`
- **Tecnologías:** Python, FastAPI, PyMySQL, MySQL 8.0, Adminer.
- **Concepto clave:** API RESTful CRUD de Biblioteca Personal (`GET`, `POST`, `PUT`, `DELETE` `/libros`). Persistencia de datos en el volumen `dbBiblioteca`, montaje *Bind Mount* para desarrollo en Python y panel de administración gráfica Adminer.
- **Configuración de Variables de Entorno (`.env`):**
  Este proyecto lee la configuración desde un archivo `.env`. Las variables configuradas son:
  - `MYSQL_ROOT_PASSWORD`: Contraseña del usuario root de MySQL (ej. `root`).
  - `DB_DATABASE`: Nombre de la base de datos (ej. `biblioteca`). En `docker-compose.yml`, se asigna a `MYSQL_DATABASE` en el servicio de MySQL y a `DB_NAME` en la API FastAPI.
  - `DB_USER`: Usuario de la base de datos (ej. `usuario`).
  - `DB_PASSWORD`: Contraseña del usuario (`1234` en `.env` / `password` en `.env.example`).
  - `DB_PORT`: Puerto de conexión a MySQL (`3306`).
- **Cómo ejecutar:**
  ```bash
  cd "4.0-API REST (FastAPI) + MySql + Adminer"

  # Crear el archivo .env si aún no existe
  cp .env.example .env

  docker compose up -d --build
  ```
- **Acceso y Servicios:**
  - **API FastAPI:** `http://localhost:8000`
  - **Documentación Interactiva (Swagger UI):** `http://localhost:8000/docs`
  - **Adminer (Gestor Web MySQL):** `http://localhost:8080` (Sistema: `MySQL`, Servidor: `db`, Usuario y Contraseña según tu `.env`)

---

### 5.0 Gestor Financiero (JWT + REDIS)
- **Directorio:** `5.0-Gestor Financiero (JWT + REDIS)`
- **Tecnologías:** Python (FastAPI), MySQL 8.0, Redis (Alpine), Adminer, JWT (PyJWT), Bcrypt, Docker Compose.
- **Objetivo del Proyecto:** 
  Diseñar una arquitectura backend profesional y escalable de 4 servicios orquestados en Docker. Permite gestionar categorías, registrar transacciones financieras (ingresos y gastos), proteger rutas mediante tokens JWT y optimizar el cálculo del balance global utilizando una **capa de memoria ultrarrápida con Redis** para evitar consultas pesadas a la base de datos.
- **Estructura Modular del Código:**
  - `main.py`: Punto de entrada y montaje de enrutadores (`app.include_router(...)`).
  - `database.py`: Conexiones a MySQL (`pymysql`), cliente Redis e inicialización de tablas (`categorias`, `transacciones`, `usuarios`).
  - `security.py`: Lógica de hashing de contraseñas (`bcrypt`), generación y validación de tokens JWT (`PyJWT`) y dependencia de autenticación (`get_current_user`).
  - `routers/`: Separación de endpoints por dominio (`auth.py`, `categorias.py`, `transacciones.py`, `balance.py`).

- **Configuración de Variables de Entorno (`.env`):**
  ```env
  MYSQL_ROOT_PASSWORD=root
  MYSQL_DATABASE=finanzas
  MYSQL_USER=izan
  MYSQL_PASSWORD=1234
  ```

- **Cómo ejecutar:**
  ```bash
  cd "5.0-Gestor Financiero (JWT + REDIS)"
  docker compose up -d --build
  ```

- **Endpoints Principales:**
  - `POST /registro`: Crea un nuevo usuario hasheando la contraseña con bcrypt.
  - `POST /login`: Valida credenciales y genera un Token JWT Bearer.
  - `GET /categorias` & `POST /categorias`: Lista y crea categorías financieras.
  - `POST /transacciones`: Registra ingresos o gastos e invalida la caché en Redis.
  - `GET /balance` *(Protegido con JWT)*: Retorna el balance total calculado mediante agregación en MySQL o servido instantáneamente desde la memoria de Redis.

---

### 🧠 Errores Comunes, Diagnósticos y Aprendizajes Clave (Proyecto 5.0)

Durante el desarrollo e integración de este laboratorio surgieron situaciones y errores reales muy formativos:

#### 1. Peticiones `POST` vs `GET` y el error `405 Method Not Allowed`
* **Qué ocurría:** Al escribir `http://localhost:8000/transacciones` en la barra del navegador, aparecía `{"detail": "Method Not Allowed"}`.
* **Causa:** La barra de direcciones del navegador realiza **exclusivamente peticiones `GET`**. Si un endpoint solo está programado para `POST` (como crear transacciones), FastAPI rechaza la petición con código 405.
* **Aprendizaje:** Para enviar datos por `POST` se debe usar una interfaz interactiva como **Swagger UI** (`http://localhost:8000/docs`), un cliente HTTP (`cURL`, `Postman`) o un Frontend (`fetch` / `axios`). En el navegador directo solo funcionan los endpoints `GET`.

#### 2. Rutas Protegidas con JWT y el error `401 Not Authenticated`
* **Qué ocurría:** Al acceder a `http://localhost:8000/balance` salía `{"detail": "Not authenticated"}`.
* **Causa:** Los navegadores no adjuntan por defecto cabeceras de autorización (`Authorization: Bearer <token>`).
* **Por qué no se puede pasar el usuario en la URL (`?username=...`):** Permitir autenticación por nombre en la URL sería una vulnerabilidad grave (cualquiera podría consultar el saldo de otro usuario cambiando el nombre). El token JWT garantiza de forma cifrada que el usuario conoce la contraseña.
* **Solución en Swagger UI:**
  1. Ejecutar `POST /login` y copiar el `access_token`.
  2. Pulsar el botón verde superior **`Authorize 🔓`**, pegar el token y cerrar la modal.
  3. El candado pasa a estar cerrado **🔒** y Swagger inyectará el token Bearer en todas las peticiones posteriores.

#### 3. Cómo funciona la Caché de Redis y su Invalidación
* **1ª Consulta a `GET /balance`:** Redis está vacío. La API consulta a MySQL (`SUM(ingresos) - SUM(gastos)`), guarda el resultado en Redis y responde indicando `"origen": "🐢 MySQL (Cálculo original)"`.
* **2ª Consulta a `GET /balance`:** El dato existe en la RAM de Redis. Responde de inmediato `"origen": "⚡ Redis (Caché ultrarrápida)"` sin tocar la base de datos.
* **Invalidación Automática:** Cada vez que se registra una nueva transacción con `POST /transacciones`, la API ejecuta `redis_client.delete("balance_total")`. Así se garantiza que el siguiente cálculo del balance refleje los datos actualizados.

#### 4. Espera al Arranque de MySQL (Race Conditions en Docker)
* **Qué ocurría:** En el primer arranque, MySQL tarda unos segundos en inicializar el catálogo de tablas. La API intentaba conectarse inmediatamente al arrancar y se apagaba por excepción no controlada.
* **Solución:** Se implementó un bucle de reintentos (`retries`) en el evento `startup()` de FastAPI para esperar hasta que MySQL acepte conexiones antes de lanzar las migraciones iniciales.

#### 5. Fuga de Conexiones y Bloqueo de Tablas (`1205 Lock wait timeout exceeded`)
* **Qué ocurría:** Tras un error en una transacción, las siguientes llamadas se quedaban congeladas 50 segundos hasta fallar por timeout de bloqueo.
* **Causa:** Si una consulta falla y la conexión a MySQL no se cierra, la transacción queda abierta reteniendo bloqueos (*locks*) a nivel de tabla/fila en InnoDB.
* **Solución:** Proteger **todas** las operaciones de base de datos con bloques `try ... finally: conn.close()` y `conn.rollback()` en caso de excepción.

#### 6. Incompatibilidad entre `passlib` y `bcrypt 4.x`
* **Qué ocurría:** Al registrar un usuario salía `ValueError: password cannot be longer than 72 bytes` y `AttributeError: module 'bcrypt' has no attribute '__about__'`.
* **Causa:** Versiones recientes de `bcrypt` (4.x) eliminaron atributos internos que la librería `passlib` utilizaba para auto-detección.
* **Solución:** Utilizar directamente la librería oficial `bcrypt` (`bcrypt.hashpw` y `bcrypt.checkpw`), mejorando el rendimiento y eliminando dependencias obsoletas.

---

## 🌐 Resumen de Puertos y Servicios

| Proyecto | Servicio | Puerto Host | Puerto Contenedor | Acceso |
| :--- | :--- | :--- | :--- | :--- |
| **1.0** | Node.js API | `3000` | `3000` | `http://localhost:3000` |
| **2.0** | Node.js API | `3001` | `3000` | `http://localhost:3001` |
| **3.0** | API Express | `3000` | `3000` | `http://localhost:3000` |
| **3.0** | PostgreSQL | `5432` | `5432` | `localhost:5432` |
| **3.0** | pgAdmin 4 | `5050` | `80` | `http://localhost:5050` |
| **4.0** | FastAPI | `8000` | `8000` | `http://localhost:8000/docs` |
| **4.0** | MySQL 8.0 | `3306` | `3306` | `localhost:3306` |
| **4.0** | Adminer | `8080` | `8080` | `http://localhost:8080` |
| **5.0** | FastAPI (JWT + Redis API) | `8000` | `8000` | `http://localhost:8000/docs` |
| **5.0** | MySQL 8.0 | `3306` | `3306` | `localhost:3306` |
| **5.0** | Redis (Alpine) | `6379` | `6379` | `localhost:6379` |
| **5.0** | Adminer | `8080` | `8080` | `http://localhost:8080` |

---

## 👨‍💻 Autor y Licencia

Creado como laboratorio personal de aprendizaje de Docker y orquestación de sistemas. ¡Siéntete libre de clonarlo, probarlo y mejorarlo! 🚀

