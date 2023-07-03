# Utiliza una imagen base de Node con la versión más reciente
FROM node:16

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos package.json y package-lock.json al directorio de trabajo
COPY package*.json ./

# Instala Angular CLI de forma global
RUN npm install -g @angular/cli

# Instala los módulos de Node requeridos por tu aplicación
RUN npm install

# Instala Angular Material
RUN npm install @angular/material@latest --save

# Instala Bootstrap
RUN npm install bootstrap@latest --save

# Copia todo el contenido del directorio frontend a la carpeta de trabajo del contenedor
COPY . .

# Expone el puerto 4200 que utiliza ng serve para el servidor de desarrollo de Angular
EXPOSE 4200

# Ejecuta el comando para levantar el servidor de desarrollo de Angular
CMD ng serve --host 0.0.0.0
