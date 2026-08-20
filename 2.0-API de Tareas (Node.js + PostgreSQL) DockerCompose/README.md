# 🐳 Proyecto 2.0: API de Tareas (Node.js) — Docker Compose

## 🎯 Objetivo del Proyecto
Dar el salto de los comandos manuales de Docker CLI a la **orquestación declarativa con Docker Compose**. El mismo servidor Node.js del proyecto 1.0 se despliega ahora a través de un `docker-compose.yml`, simplificando radicalmente el proceso de arranque.

Además, se introduce el concepto de **Bind Mount** para sincronizar el código local con el contenedor en tiempo real, eliminando la necesidad de reconstruir la imagen con cada cambio.

---

## 🛠️ Tecnologías Utilizadas

- **Node.js 20 (Alpine):** Runtime JavaScript ligero.
- **Docker Compose:** Orquestación declarativa mediante `docker-compose.yml`.

---

## 📂 Estructura de Archivos

```text
2.0-API de Tareas (Node.js + PostgreSQL) DockerCompose/
├── Dockerfile          # Definición de la imagen Docker
├── docker-compose.yml  # Orquestador del servicio
└── server.js           # Servidor HTTP básico con Node.js nativo
```

---

## 🏗️ Conceptos Clave Aprendidos

1. **`docker-compose.yml`:** Archivo declarativo que sustituye el largo comando `docker run` con todas sus flags por un fichero legible y versionable.
2. **`build: .`:** Le indica a Compose que construya la imagen desde el `Dockerfile` en la carpeta actual, en lugar de descargar una imagen preexistente.
3. **Bind Mount (`- .:/app`):** Monta la carpeta actual del host directamente dentro del contenedor en `/app`. Cualquier cambio en el código local se refleja de forma inmediata sin necesidad de reconstruir la imagen.
4. **Puerto diferente (`3001:3000`):** El servidor escucha en el puerto `3000` interno del contenedor, pero se expone al host en el `3001` para evitar conflictos con el proyecto 1.0.
5. **`restart: always`:** Política de reinicio que garantiza que el contenedor se levante automáticamente si el sistema se reinicia o el proceso falla.

---

## 🌐 Servicios y Puertos

| Servicio | Puerto Host | Puerto Contenedor | Acceso |
| :--- | :--- | :--- | :--- |
| Node.js API | `3001` | `3000` | `http://localhost:3001` |

---

## 💻 Comandos para Ejecutar

```bash
cd "2.0-API de Tareas (Node.js + PostgreSQL) DockerCompose"

# Construir la imagen y levantar el servicio en segundo plano
docker compose up -d --build

# Ver los logs del servicio
docker compose logs -f

# Detener y eliminar el contenedor
docker compose down
```

**Acceso:** `http://localhost:3001`
