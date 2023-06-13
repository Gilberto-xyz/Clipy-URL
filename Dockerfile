# Imagen base de Python
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3-dev python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Agregar repositorio de phpmyadmin
RUN add-apt-repository ppa:phpmyadmin/ppa

# Actualizar lista de paquetes
RUN apt-get update

# Instalar MySQL y PHPMyAdmin
RUN apt-get install -y mysql-server phpmyadmin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Copiar el archivo de configuración de PHPMyAdmin
COPY config.inc.php /etc/phpmyadmin/config.inc.php

# Exponer los puertos de la aplicación y de PHPMyAdmin
EXPOSE 5000 80

# Iniciar la aplicación y PHPMyAdmin
CMD service mysql start && \
    service apache2 start && \
    python clipy_app.py

