# APP Salones de capacitación

Esta aplicación se utiliza en las tablets que se encuentran en la puerta de los salones de capacitación para mostrar el curso o reunión del salón.

# Configuración

La aplicación esta desarrollada en Python 3.x y Flask

## Dependencias
Estas se encuentran dentro del archivo requeriment.txt

 - Flask
 - uwsgi
 - mysql-connector-python

## Variables de ambiente.

Definir las variables de ambiente para conectarse a la base de datos de reserva de salones.

 - DATABASE_IP
 - DATABASE_NAME
 - DATABASE_USER
 - DATABASE_PASSWORD

# Run

## Develop

    python app.py

## Prod

Configurar previamente los parámetros necesarios en uwsgi.ini

    uwsgi --ini uwsgi.ini

