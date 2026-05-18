"""
URL configuration for a_first_proyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#django.urls: Librería para crear rutas o URLs dentro de una aplicación 
#Django. La función path() se utiliza para conectar una dirección web (URL) 
#con una función o vista (view) del backend, permitiendo que cuando un 
#usuario entre a una URL específica, Django sepa qué código ejecutar y qué 
#contenido mostrar.
from django.urls import path, include
#VISTAS PROPIAS: Cuando se quiera agregar un nuevo endpoint interno de Django, 
#se debe hacer referencia al archivo de views.py y a la vista creada dentro 
#de este archivo, el cual se conectará a la base de datos para mostrar cierto 
#valor dinámico en un template, el cual de igual forma se menciona dentro del 
#archivo views.py, específicamente a través de la función render().
from a_app_name.views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car-list/', my_view),
    path('app_endpoint/', include('a_app_name.urls')),
]
