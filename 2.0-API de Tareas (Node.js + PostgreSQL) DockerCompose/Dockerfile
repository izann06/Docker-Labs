#1. Usar Node.js
FROM node:20-alpine

#2. Carpeta de Trabajo que se crea dentro del contenedor (aislado del PC)
# Sirve para no tirar nuestros archivos en la raíz del sistema operativo Linux.
WORKDIR /app

#3. Copiar solo nuestro archivo al contenedor, al ser uno ponemos su nombre
# Si hubiera más archivos, usaríamos COPY . . para copiarlos TODOS
COPY server.js .

#4. Abrir el puerto 3000 (Puerto del Contenedor)
# Luego con -p 3001:3000 lo "engancharemos" al PC
EXPOSE 3000

#5 Ejecutar el código
CMD ["node", "--watch", "server.js"]