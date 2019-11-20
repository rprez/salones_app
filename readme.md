# APP Salones de capacitación

Esta aplicación se utiliza en la puerta de los salones de capacitación para mostrar que materia o reunión se encuentra en determinado salón.

# Configuración

La aplicación esta desarrollada en Python 3.x y Flask

## Dependencias
Estas se encuentran dentro del archivo requeriment.txt

 - Flask
 - uwsgi
 - mysql-connector-python

## Variables de ambiente.

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

