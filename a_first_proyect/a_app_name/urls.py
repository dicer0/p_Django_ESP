#django.urls: Librería para crear rutas o URLs dentro de una aplicación 
#Django. La función path() se utiliza para conectar una dirección web (URL) 
#con una función o vista (view) del backend, permitiendo que cuando un 
#usuario entre a una URL específica, Django sepa qué código ejecutar y qué 
#contenido mostrar.
from django.urls import path

def mi_view():
    return ""

urlpatterns = [
    #El path que se declare aquí, será el interno que está contenido en 
    #el endpoint que se declare en el archivo urls.py del proyecto que se 
    #encuentra en a_first_project/a_first_project/urls.py
    path("/listado/", mi_view),
    path("/detalle/", mi_view),
]