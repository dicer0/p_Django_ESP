#Podemos seleccionar el entorno virtual que esté utilizando VSCode, del lado inferior 
#derecho, para después resetear el editor de código con CTRL+SHIFT+P y ejecutando la 
#opción de Developer: Reload Window, esto solamente cuando VSCode esté mostrando errores 
#o warnings erróneos de dependencias instaladas en nuestro entorno virtual.
from django.db import models

# Create your models here.
class Product(models.Model):
    #Cada uno de los atributos que se agreguen a la clase, representarán una 
    #columna en la tabla de la base de datos.
    #models.TextField(): Clase o campo para decarar strings, recibe como parámetros:
    # - max_length: El número máximo de caracteres que puede recibir.
    # - null: Llena de valores NULL la DB cuando sea creada una nueva columna con 
    #   este tipo de dato.
    # - verbose_name: Sirve para asgnar un nombre más claro, bonito o traducido a un 
    #   campo (atributo) cuando se enseñe en formularios, tablas o el admin de Django.
    #Si queremos ver todos los campos disponibles que tenemos en Django para 
    #declarar distintos tipos de datos en los modelos, podemos acceder a este enlace: 
    #https://docs.djangoproject.com/en/5.0/ref/models/fields/
    name = models.TextField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descripción")
    #models.DecimalField(): Atributo o campo para decarar números decimales, recibe 
    #como parámetros:
    # - max_digits: Número máximo de dígitos en el número.
    # - decimal_places: Número máximo de decimales que aparecen.
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    #models.BooleanField(): Campo para decarar valores booleanos True o False, recibe 
    #como parámetros:
    # - default: Este define cual es el valor inicial que contiene el campo, ya sea 
    #   True o False
    available = models.BooleanField(default=True)
    #models.ImageField(): Campo para decarar una imagen, recibe como parámetros:
    # - default: Este define donde se ha subido la imagen.
    photo = models.ImageField(upload_to="logos")