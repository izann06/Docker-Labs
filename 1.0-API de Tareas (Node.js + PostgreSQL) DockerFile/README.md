# 📦 Proyecto 1.0: API de Tareas (Node.js) — Dockerfile

## 🎯 Objetivo del Proyecto
Primer contacto con Docker. El objetivo es **empaquetar manualmente** una aplicación Node.js sencilla dentro de un contenedor usando un `Dockerfile` escrito a mano, sin Docker Compose.

Se aprende a construir la imagen con `docker build` y a ejecutar el contenedor con `docker run`, comprendiendo el ciclo de vida básico de un contenedor Docker.

---

## 🛠️ Tecnologías Utilizadas

- **Node.js 20 (Alpine):** Runtime JavaScript ligero basado en Alpine Linux.
- **Docker CLI:** Construcción y ejecución manual de contenedores sin Compose.

---

## 📂 Estructura de Archivos

```text
1.0-API de Tareas (Node.js + PostgreSQL) DockerFile/
├── Dockerfile    # Definición de la imagen Docker
└── server.js     # Servidor HTTP básico con Node.js nativo
```

---

## 🏗️ Conceptos Clave Aprendidos

1. **`FROM node:20-alpine`:** Selección de la imagen base. Alpine reduce drásticamente el tamaño final de la imagen respecto a `node:20`.
2. **`WORKDIR /app`:** Define el directorio de trabajo dentro del sistema de archivos del contenedor, evitando ensuciar la raíz `/`.
3. **`COPY server.js .`:** Copia únicamente el archivo necesario desde el host al contenedor.
4. **`EXPOSE 3000`:** Documentación del puerto que el contenedor escucha internamente (no abre el puerto solo, es `docker run -p` quien lo mapea).
5. **`CMD ["node", "server.js"]`:** Comando que se ejecuta cuando el contenedor arranca.

---

## 🌐 Servicios y Puertos

| Servicio | Puerto Host | Puerto Contenedor | Acceso |
| :--- | :--- | :--- | :--- |
| Node.js API | `3000` | `3000` | `http://localhost:3000` |

---

## 💻 Comandos para Ejecutar

```bash
cd "1.0-API de Tareas (Node.js + PostgreSQL) DockerFile"

# 1. Construir la imagen a partir del Dockerfile
docker build -t api-node-dockerfile .

# 2. Ejecutar el contenedor mapeando puertos
docker run -d -p 3000:3000 --name api-node-container api-node-dockerfile

# 3. Comprobar que está corriendo
docker ps

# 4. Detener y eliminar el contenedor
docker stop api-node-container
docker rm api-node-container
```

**Acceso:** `http://localhost:3000`
