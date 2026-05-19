#django.urls: Librería para crear rutas o URLs dentro de una aplicación 
#Django. La función path() se utiliza para conectar una dirección web (URL) 
#con una función o vista (view) del backend, permitiendo que cuando un 
#usuario entre a una URL específica, Django sepa qué código ejecutar y qué 
#contenido mostrar.
from django.urls import path
#django.http: Librería para crear y enviar respuestas HTTP desde el backend 
#hacia el navegador cuando este acceda a una URL. Es la forma más básica de 
#devolver contenido desde una vista, en vez de usar templates o render().
from django.http import HttpResponse
#VISTAS PROPIAS: Cuando se quiera agregar un nuevo endpoint interno de Django, 
#se debe hacer referencia al archivo de views.py y a la vista creada dentro 
#de este archivo, el cual se conectará a la base de datos para mostrar cierto 
#valor dinámico en un template, el cual de igual forma se menciona dentro del 
#archivo views.py, específicamente a través de la función render().
from .views import CarListView

#Cuando se trabaja con endpoints dinámicos (que incluyen variables), la 
#función que define una vista recibe más de un solo parámetro, no solo el 
#request, sino también un tipo de parámetros especiales llamados *args y 
#**kargs, donde el primero es una tupla y el segundo es un diccionario 
#donde se imprimirá el valor de la variable dinámica incluida en la URL.
def mi_view(request, *args, **kargs):
    print(args)     #args: Tupla 
    print(kargs)    #kargs: Diccionario con el valor del endpoint dinámico.
    return HttpResponse("Holis mundo")
#Las views nunca deben ir dentro del archivo de URLs.py, pero en este caso
#se hizo así para denotar cierta funcionalidad de args y kargs con 
#endpoints dinámicas y de igual forma, recordemos que estas se pueden 
#declarar en forma de función o en forma de clase, como se denotará a 
#continuación.

urlpatterns = [
    #El path que se declare aquí, será el interno que está contenido en 
    #el endpoint que se declare en el archivo urls.py del proyecto que se 
    #encuentra en a_first_project/a_first_project/urls.py
    #path("listado/", mi_view),      #View en forma de función.
    path("listado/", CarListView.as_view()),  #View en forma de Clase.
    #Cuando se quiera crear un endpoint dinámico donde se utilizará el 
    #valor de una variable dentro del endpoint, como una id, se deben 
    #utilizar los símmbolos de menor que y mayor que y en medio poner la 
    #variable: "endpoint/<tipo_de_dato : nombre_variable>/"
    path("detalle/<int:id>", mi_view),
    path("marcas/<str:brand>", mi_view),
    #Los tipos de datos que se pueden recibir a través de URLs dinámicas:
    # - int: Numéricos enteros.
    # - str: Cadenas de caracteres.
    # - slug: Números o letras conformados por el código ASCII.
    # - uuid (Universally Unique Identifier): Código de 128 bits para ids.
]