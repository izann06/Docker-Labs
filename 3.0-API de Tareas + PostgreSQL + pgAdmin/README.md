# 🐘 Proyecto 3.0: API de Tareas + PostgreSQL + pgAdmin

## 🎯 Objetivo del Proyecto
Escalar la arquitectura a un **stack multicontenedor real** de 3 servicios: una API Express.js conectada a una base de datos PostgreSQL, con un panel de administración gráfico pgAdmin accesible desde el navegador.

El objetivo central es entender la **comunicación interna entre contenedores** a través de la red de Docker (resolución DNS por nombre de servicio) y la **persistencia de datos** mediante Named Volumes.

---

## 🛠️ Tecnologías Utilizadas

- **Express.js (Node.js):** Framework web para la API.
- **PostgreSQL 16 (Alpine):** Base de datos relacional.
- **pgAdmin 4:** Panel de administración gráfica web para PostgreSQL.
- **Docker Compose:** Orquestación de los 3 servicios.

---

## 📂 Estructura de Archivos

```text
3.0-API de Tareas + PostgreSQL + pgAdmin/
├── dockerfile          # Definición de la imagen de la API
├── docker-compose.yml  # Orquestación de los 3 servicios
├── package.json        # Dependencias de Node.js
└── server.js           # API Express.js con conexión a PostgreSQL
```

---

## 🏗️ Conceptos Clave Aprendidos

1. **Networking Interno de Docker:** Los contenedores del mismo `docker-compose.yml` se ven entre sí por su nombre de servicio. La API se conecta a la base de datos usando `DB_HOST=db` (no una IP), ya que Docker actúa como DNS interno.
2. **Named Volumes (`pgdata`):** A diferencia de los Bind Mounts, los Named Volumes son gestionados por Docker y persisten los datos de PostgreSQL aunque el contenedor se elimine con `docker compose down`.
3. **`depends_on`:** Garantiza el orden de arranque: la API y pgAdmin esperan a que el servicio `db` esté iniciado antes de arrancar.
4. **Variables de Entorno inline:** Las credenciales de PostgreSQL y pgAdmin se definen directamente en el `docker-compose.yml` (práctica introductoria, mejorada en proyectos posteriores con `.env`).

---

## ⚙️ Variables de Entorno

Las credenciales están definidas directamente en `docker-compose.yml`:

| Variable | Valor | Servicio |
| :--- | :--- | :--- |
| `POSTGRES_USER` | `usuario` | PostgreSQL |
| `POSTGRES_PASSWORD` | `1234` | PostgreSQL |
| `POSTGRES_DB` | `base_tareas` | PostgreSQL |
| `PGADMIN_DEFAULT_EMAIL` | `user@user.com` | pgAdmin |
| `PGADMIN_DEFAULT_PASSWORD` | `root` | pgAdmin |

---

## 🌐 Servicios y Puertos

| Servicio | Puerto Host | Puerto Contenedor | Acceso |
| :--- | :--- | :--- | :--- |
| API Express | `3000` | `3000` | `http://localhost:3000` |
| PostgreSQL | `5432` | `5432` | `localhost:5432` |
| pgAdmin 4 | `5050` | `80` | `http://localhost:5050` |

---

## 💻 Comandos para Ejecutar

```bash
cd "3.0-API de Tareas + PostgreSQL + pgAdmin"

# Construir y levantar todos los servicios
docker compose up -d --build

# Ver el estado de los contenedores
docker compose ps

# Detener y eliminar (los datos del volumen pgdata se conservan)
docker compose down

# Detener eliminando también el volumen (borrón y cuenta nueva)
docker compose down -v
```

### Conectar pgAdmin a PostgreSQL

1. Accede a `http://localhost:5050`
2. Login: `user@user.com` / `root`
3. Clic derecho en "Servers" → "Register" → "Server"
4. En la pestaña **Connection**: Host `db`, Puerto `5432`, Usuario `usuario`, Contraseña `1234`
