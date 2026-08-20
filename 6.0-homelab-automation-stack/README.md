Markdown
# 🛡️ Proyecto 6.0: Homelab Automation Stack 

## 🎯 Objetivo del Proyecto
Este proyecto deja de lado la programación de código puro para centrarse en la **Arquitectura de Sistemas y DevOps**.

 El objetivo es levantar un servidor de automatización (Homelab) en local utilizando Docker, aplicando estándares profesionales de ciberseguridad: bases de datos aisladas, variables de entorno ocultas, redes privadas y chequeos de salud automatizados.

## 🛠️ Tecnologías y Servicios Utilizados
El ecosistema orquesta 4 contenedores que se comunican entre sí:
*   **🐳 Docker & Docker Compose:** El motor principal para crear y gestionar la infraestructura.
*   **🐘 PostgreSQL (16-alpine):** Base de datos robusta utilizada como bóveda de almacenamiento.
*   **🤖 n8n:** Motor de automatización visual (alternativa a Zapier) para crear flujos de trabajo.
*   **🚢 Portainer:** Interfaz gráfica web para gestionar los contenedores, redes y volúmenes sin tocar la terminal.
*   **🏠 Homepage:** Panel de control centralizado y estético para agrupar los accesos rápidos y monitorizar widgets.

---

## 🏗️ Arquitectura y Ciberseguridad (La Magia del Proyecto)

Este proyecto no expone servicios a lo loco. Utiliza tres conceptos clave de DevOps:

1.  **Redes Aisladas (Zero Trust):** Se han creado dos redes virtuales (`red_frontend` y `red_backend`). PostgreSQL vive **solo** en la red de backend y no tiene expuesto ningún puerto (`ports`) hacia el PC anfitrión (Windows). Es totalmente invisible desde el exterior. Solo n8n puede hablar con la base de datos.

2.  **Healthchecks (Semáforos de encendido):** Docker arranca rapidísimo, pero las bases de datos tardan en estar listas. Hemos configurado un `healthcheck` que lanza el comando `pg_isready` cada 10 segundos. n8n está configurado con `depends_on: condition: service_healthy`, por lo que espera pacientemente a que PostgreSQL dé luz verde antes de arrancar.

3.  **Variables de Entorno (`.env`):** Ninguna contraseña está escrita en el archivo `docker-compose.yml`. Se inyectan de forma segura desde un archivo oculto.

4.  **Políticas de Reinicio:** Se utiliza `restart: unless-stopped`. Si el PC se reinicia o un servicio colapsa, Docker lo levantará automáticamente, a menos que el administrador lo haya apagado manualmente.

---

## 📂 Estructura de Archivos

Para que el proyecto funcione, la carpeta debe tener exactamente esta estructura:

```text
/homelab-automation-stack
│
├── .env                  # (OBLIGATORIO) Credenciales seguras
├── docker-compose.yml    # El orquestador de la infraestructura
└── /homepage_config      # (Autogenerado) Archivos de personalización del panel
    ├── services.yaml
    ├── widgets.yaml
    └── settings.yaml


💻 Comandos Clave (Manual de Supervivencia)
Levantar toda la infraestructura (en segundo plano):

Bash
docker compose up -d
Ver el estado y la salud de los contenedores:

Bash
docker ps
Leer los logs (chivatos) de un contenedor específico:

Bash
docker logs <nombre_del_contenedor>
Destruir la infraestructura y borrar volúmenes corruptos (Borrón y cuenta nueva):

Bash
docker compose down -v

⚙️ Casos de Uso y Configuraciones Implementadas
1. Automatización con n8n y PostgreSQL
Se diseñó un flujo de trabajo para extraer datos de una API pública (https://dummyjson.com/quotes/random) y guardarlos de forma autónoma en la base de datos blindada.

Creación de tabla vía consola de Portainer:

Bash
psql -U izan_admin -d n8n_database
SQL
CREATE TABLE citas_celebres (
    id SERIAL PRIMARY KEY,
    autor VARCHAR(100),
    frase TEXT
);
En n8n se utilizó el nodo HTTP Request para obtener el JSON y el nodo PostgreSQL (configurado mediante Expresiones como {{ $json.author }}) para mapear e insertar los datos.

2. Personalización Avanzada de Homepage
Mediante un Bind Mount (./homepage_config:/app/config), conectamos una carpeta local al contenedor para aplicar cambios en tiempo real sin reiniciar.

services.yaml (Accesos Rápidos):

YAML
- Mi Infraestructura:
    - Portainer:
        icon: portainer.png
        href: http://localhost:9000
        description: Gestión visual de contenedores
    - n8n:
        icon: n8n.png
        href: http://localhost:5678
        description: Motor de automatización de flujos
widgets.yaml (Meteorología Local sin API Key):

YAML
- openmeteo:
    label: Villafranqueza
    latitude: 38.3789
    longitude: -0.5019
    timezone: Europe/Madrid
    units: metric
    format: "%t - %d"
settings.yaml (Estética DevOps):

YAML
background:
  image: "[https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=2070&auto=format&fit=crop](https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=2070&auto=format&fit=crop)"
  blur: sm
  brightness: 50
  saturate: 75
theme: dark