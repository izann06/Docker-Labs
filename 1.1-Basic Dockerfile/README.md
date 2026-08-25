# 🐳 Proyecto 1.1: Basic Dockerfile

## 🎯 Objetivo del Proyecto
El objetivo de este proyecto es escribir un `Dockerfile` muy básico para crear una imagen de Docker. Al ejecutar esta imagen, debe imprimir el mensaje `"Hola Capitán"` en la consola antes de finalizar su ejecución. Además, incluimos la mejora propuesta ("Bonus") para permitir pasar tu nombre como variable de entorno y que imprima `"Hola, [tu nombre]!"`.

> **Fuente:** Proyecto práctico para dominar los fundamentos extraído del roadmap de Docker de [Roadmap.sh](https://roadmap.sh/projects/basic-dockerfile)

---

## 🛠️ Requisitos Cumplidos
- [x] El archivo se llama `Dockerfile`.
- [x] Está ubicado en el directorio raíz de la carpeta del proyecto.
- [x] La imagen base es `alpine:latest`.
- [x] Contiene una instrucción que imprime `"Hola Capitán"` al ejecutarse.
- [x] *(Mejora)* Permite inyectar el nombre a través de variables de entorno de forma dinámica.

---

## 📝 Las Dos Formas de Hacerlo

Para entender bien Docker, vamos a ver cómo se haría de la forma más básica (directa) y luego cómo se hace con la mejora de la variable de entorno.

### Forma 1: Directa (Texto quemado / Hardcodeado)

Si solo quisiéramos imprimir "Hola Capitán" siempre, sin posibilidad de cambiar el nombre, nuestro **Dockerfile** sería así de sencillo:

```dockerfile
# 1. Imagen base
FROM alpine:latest

# 2. Comando directo
CMD ["echo", "Hola Capitán"]
```

> **¿Cómo funciona `CMD ["echo", "Hola Capitán"]`?** 
> Al usar los corchetes `["comando", "argumento"]`, Docker coge el programa `echo` y le pasa literalmente el texto que pongas. Es la forma más rápida y directa.

### Forma 2: Dinámica (Con Variable de Entorno - Recomendada)

Si queremos poder inyectar un nombre distinto al arrancar el contenedor (el "Bonus"), necesitamos usar una variable. El **Dockerfile** quedaría así (este es el que tenemos guardado en tu archivo):

```dockerfile
# 1. Imagen base
FROM alpine:latest

# 2. Variable de entorno por defecto
ENV NAME="Capitán"

# 3. Comando ejecutado a través de una terminal (shell)
CMD ["sh", "-c", "echo Hola, $NAME!"]
```

> ⚠️ **El problema de las variables y el `CMD`**
> Te preguntarás, ¿por qué no pusimos simplemente `CMD ["echo", "Hola $NAME"]`? 
> Si haces eso, Docker no sabe qué es `$NAME`. Al no haber una terminal de por medio, Docker imprime el texto literal "$NAME". 
> Por eso usamos `["sh", "-c", "..."]`: esto obliga a Docker a abrir una pequeña terminal (`sh`) de fondo, la cual **sí sabe** interpretar variables, traduciendo `$NAME` a "Capitán" o a "Izan".

---

## 🚀 Guía de Ejecución

Para probar nuestro proyecto (la Forma 2 que está en tu `Dockerfile`), sigue estos pasos en la terminal:

### Paso 1: Construir (Build) la imagen
Abre la terminal en esta carpeta y dile a Docker que cocine la imagen y la empaquete con el nombre de etiqueta (`-t`) **"hola-capitan"**.

```bash
docker build -t hola-capitan .
```
*(Ojo: no te olvides del `.` al final, eso le dice a Docker "busca el Dockerfile en la carpeta actual").*

> 🚨 **REGLA DE ORO (El error más común):** 
> Cada vez que modifiques el código de tu `Dockerfile` (aunque solo sea cambiar una letra), **tienes que volver a ejecutar el comando `docker build`**. Si no lo haces, Docker ignorará tus cambios y seguirá ejecutando la versión antigua que construiste la primera vez.

### Paso 2: Ejecutar el contenedor (Valor por defecto)
Levanta el contenedor basado en la imagen que acabas de construir:

```bash
docker run --rm hola-capitan
```
> **Output esperado:** `Hola, Capitán!`

### Paso 3: Ejecutar el contenedor inyectando tu nombre (Bonus)
Usa el parámetro `-e` para sobrescribir la variable de entorno `NAME`:

```bash
docker run --rm -e NAME="Izan" hola-capitan
```
> **Output esperado:** `Hola, Izan!`

---

## 👻 El Misterio de los Contenedores Fantasma

Si ejecutas el contenedor y luego haces un `docker ps` para ver tus contenedores, te darás cuenta de que **no sale nada**. ¿Por qué?

Un contenedor no tiene por qué ser un servidor que corre indefinidamente. Este contenedor nace, imprime el saludo y **muere inmediatamente** al terminar su trabajo (es una tarea efímera).
- El comando `docker ps` solo muestra los contenedores vivos y trabajando actualmente.
- Si haces `docker ps -a` (el flag `-a` significa "all"), verás el historial con tu contenedor muerto (estado `Exited`).

**¿Y para qué sirve el `--rm`?**
Como el contenedor se muere en un segundo, si no ponemos `--rm`, se quedaría ocupando espacio inútilmente en tu disco como contenedor "zombie" muerto. El flag `--rm` le dice a Docker: *"Cuando termines de ejecutar y te mueras, bórrate automáticamente de mi ordenador para no dejar basura"*.
