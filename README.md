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

---

## 👨‍💻 Autor y Licencia

Creado como laboratorio personal de aprendizaje de Docker y orquestación de sistemas. ¡Siéntete libre de clonarlo, probarlo y mejorarlo! 🚀
