# 🐳 Proyecto 1.1: Basic Dockerfile

## 🎯 Objetivo del Proyecto
El objetivo de este proyecto es escribir un `Dockerfile` muy básico para crear una imagen de Docker. Al ejecutar esta imagen, debe imprimir el mensaje `"Hola Capitán"` en la consola antes de finalizar su ejecución. Ad   emás, incluimos la mejora propuesta ("Bonus") para permitir pasar tu nombre como variable y que imprima `"Hola, [tu nombre]!"`.

> **Fuente:** Proyecto práctico para dominar los fundamentos extraído del roadmap de Docker de https://roadmap.sh/projects/basic-dockerfile

---

## 🛠️ Requisitos Cumplidos
- [x] El archivo se llama `Dockerfile`.
- [x] Está ubicado en el directorio raíz de la carpeta del proyecto.
- [x] La imagen base es `alpine:latest`.
- [x] Contiene una única instrucción que imprime `"Hola Capitán"` al ejecutarse.
- [x] *(Mejora)* Permite inyectar el nombre a través de variables de entorno de forma dinámica.

---

## 📝 Explicación Paso a Paso (Cómo se hizo)

### 1. La Imagen Base
Un `Dockerfile` es el plano de construcción de un contenedor. Todo plano necesita unos cimientos, y eso es la imagen base:
```dockerfile
FROM alpine:latest
```
*Anotación:* Usamos `alpine:latest` porque es el estándar de facto para imágenes ligeras. Pesa a penas 5MB, en comparación con los cientos de MB de distribuciones como Ubuntu.

### 2. La Variable de Entorno (El Toque Dinámico)
Para no tener quemado (hardcodeado) el texto "Capitán" y poder personalizarlo, declaramos una variable:
```dockerfile
ENV NAME="Capitán"
```
*Anotación:* `ENV` nos permite establecer valores por defecto. Si el usuario no proporciona nada, la imagen no fallará y saludará al "Capitán".

### 3. El Comando de Ejecución
Por último, indicamos qué tiene que hacer el contenedor una vez esté corriendo:
```dockerfile
CMD sh -c "echo Hola, $NAME!"
```
*Anotación:* 
- `CMD` es la instrucción que se ejecuta cuando levantas el contenedor.
- Usamos `sh -c` para iniciar el procesador de comandos (*shell*) integrado de Alpine, de manera que pueda leer y procesar correctamente la variable `$NAME`.

---

## 🚀 Guía de Ejecución

### Paso 1: Construir (Build) la imagen
Abre la terminal en esta carpeta y dile a Docker que cocine la imagen y la empaquete con el nombre de etiqueta (`-t`) **"hola-capitan"**.
```bash
docker build -t hola-capitan .
```
*(Ojo: no te olvides del `.` al final, eso le dice a Docker "busca el Dockerfile en la carpeta actual")*

### Paso 2: Ejecutar el contenedor (Modo Normal)
Levanta el contenedor basado en tu nueva imagen:
```bash
docker run --rm hola-capitan
```
> **Output esperado:** `Hola, Capitán!`
*(Tip: El parámetro `--rm` se encarga de eliminar el contenedor de tu disco en cuanto termina de ejecutar el `echo`. ¡Ideal para no acumular basura!)*

### Paso 3: Ejecutar el contenedor (Modo Personalizado)
Inyecta tu nombre usando el parámetro de variables de entorno (`-e`):
```bash
docker run --rm -e NAME="Izan" hola-capitan
```
> **Output esperado:** `Hola, Izan!`

---

## 🧠 Conclusión y Notas Personales

- Un contenedor no tiene por qué ser un servidor que corre indefinidamente. Puede ser una simple tarea efímera (ejecuta un comando y muere, como en este caso).

- Utilizar variables de entorno (`ENV`) desde el principio es una muy buena práctica para desacoplar el código de los datos dinámicos.
