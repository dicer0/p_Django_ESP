#models: La librería models de django.db nos da acceso al sistema de modelos 
#ORM, que es la forma en que Django representa y maneja la base de datos 
#usando Python.
from django.db import models

# •	Model (M): Esta es la capa de datos de la arquitectura, que indica como 
# se guardan los datos, donde se procesan, que tipo de datos son, donde va 
# la lógica de negocio, etc.
#   →: El modelo entrega estructuras de datos del backend hacia la vista.
#   ←: El modelo recibe una petición de la vista y entrega hacia el template 
#      el dato que está buscando.


class Car(models.Model):
    #models.TextField: Clase para decarar strings.
    title = models.TextField(max_length = 250)