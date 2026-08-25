# 🐳 Docker Labs & Playground

Este repositorio es mi laboratorio personal para aprender y practicar Docker y Docker Compose de forma incremental.

Abarca desde empaquetar una aplicación básica con un `Dockerfile` hasta la orquestación de arquitecturas multicontenedor con APIs (Node.js y FastAPI), bases de datos relacionales (PostgreSQL y MySQL), automatización, redes Zero-Trust y paneles de administración.

---

## 🛠️ Tecnologías y Conceptos Clave

- **Herramientas de Contenedores:** Docker, Dockerfiles, Docker Compose.
- **Runtimes & Frameworks:** Node.js (HTTP nativo y Express.js), Python (FastAPI, PyMySQL).
- **Bases de Datos & GUIs:** PostgreSQL + pgAdmin, MySQL + Adminer.
- **Seguridad & Automatización:** JWT, Bcrypt, Redis, n8n, Portainer CE, Homepage.
- **Conceptos de Arquitectura:**
  - **Networking Interno:** Comunicación aislada entre contenedores mediante la red interna de Docker y resolución DNS por nombre de servicio.
  - **Persistencia de Datos:** Uso de *Named Volumes* para la persistencia de datos en bases de datos y *Bind Mounts* para la sincronización de código local en tiempo real durante el desarrollo.
  - **Gestión de Configuración:** Inyección de variables de entorno directamente en Compose o mediante archivos `.env`.
  - **Zero-Trust Networking:** Redes privadas de backend aisladas del host para servicios sensibles.
  - **Healthchecks:** Control de condiciones de carrera en el arranque de servicios dependientes.

---

## 📂 Estructura del Laboratorio

| Directorio | Tecnologías | Concepto Principal |
| :--- | :--- | :--- |
| [`1.0-API de Tareas (Node.js + PostgreSQL) DockerFile`](./1.0-API%20de%20Tareas%20%28Node.js%20+%20PostgreSQL%29%20DockerFile) | Node.js, Docker CLI | Construcción manual de imagen con `Dockerfile`. |
| [`2.0-API de Tareas (Node.js + PostgreSQL) DockerCompose`](./2.0-API%20de%20Tareas%20%28Node.js%20+%20PostgreSQL%29%20DockerCompose) | Node.js, Docker Compose | Orquestación con Compose y *Bind Mounts* en vivo. |
| [`3.0-API de Tareas + PostgreSQL + pgAdmin`](./3.0-API%20de%20Tareas%20+%20PostgreSQL%20+%20pgAdmin) | Express.js, PostgreSQL, pgAdmin | Stack de 3 servicios con red interna y *Named Volume*. |
| [`4.0-API REST (FastAPI) + MySql + Adminer`](./4.0-API%20REST%20%28FastAPI%29%20+%20MySql%20+%20Adminer) | FastAPI, MySQL 8.0, Adminer | API CRUD completa en Python con variables `.env`. |
| [`5.0-Gestor Financiero (JWT + REDIS)`](./5.0-Gestor%20Financiero%20%28JWT%20+%20REDIS%29) | FastAPI, MySQL 8.0, Redis, JWT, Bcrypt | Autenticación JWT, hashing seguro y caché en Redis. |
| [`6.0-homelab-automation-stack`](./6.0-homelab-automation-stack) | PostgreSQL 16, n8n, Portainer CE, Homepage | Homelab DevOps con Zero-Trust, healthchecks y dashboard. |

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
| **5.0** | FastAPI (JWT + Redis) | `8000` | `8000` | `http://localhost:8000/docs` |
| **5.0** | MySQL 8.0 | `3306` | `3306` | `localhost:3306` |
| **5.0** | Redis (Alpine) | `6379` | `6379` | `localhost:6379` |
| **5.0** | Adminer | `8080` | `8080` | `http://localhost:8080` |
| **6.0** | Portainer CE | `9000` | `9000` | `http://localhost:9000` |
| **6.0** | n8n | `5678` | `5678` | `http://localhost:5678` |
| **6.0** | Homepage Dashboard | `3000` | `3000` | `http://localhost:3000` |
| **6.0** | PostgreSQL 16 | *Ninguno* | `5432` | `postgres:5432` *(Red privada)* |

---

## 🗺️ Roadmap de Docker (Roadmap.sh)

De forma complementaria, estoy siguiendo la ruta de proyectos oficiales para validar mis conocimientos y escalar la dificultad poco a poco.

Proyectos: https://roadmap.sh/docker/projects

### 🟢 Nivel Básico
- [x] **Basic Dockerfile**
  > 🔗 **Reto:** https://roadmap.sh/projects/basic-dockerfile
  > 🏆 **Solución:** [Ver en GitHub](https://github.com/izann06/Docker-Labs/tree/main/Roadmap/Basico/1.1-Basic%20Dockerfile)

### 🟡 Nivel Intermedio
- [ ] 🚧 *Aún no he llegado a este nivel.*

### 🔴 Nivel Avanzado
- [ ] 🚧 *Aún no he llegado a este nivel.*

---

## 👨‍💻 Autor y Licencia

Creado como laboratorio personal de aprendizaje de Docker y orquestación de sistemas. ¡Siéntete libre de clonarlo, probarlo y mejorarlo! 🚀
