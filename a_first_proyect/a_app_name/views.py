#render: La librería render de django.shortcuts sirve para cargar datos 
#dinámicos en una página HTML, para ello se utiliza un contexto, que es un 
#diccionario de Python con información cambiante de la base de datos, la 
#cual puede incluir datos como usuarios, fechas, etc. y los inserta en el 
#template (UI).  
from django.shortcuts import render

# •	View (V): Esta se refiere a un conector entre el modelo que tiene 
# acceso a los datos y el template (UI) que los está pidiendo para saber si 
# los puede proporcionar o no, esta parte es la encargada de controlar el 
# flujo de peticiones SQL de la interfaz gráfica hacia la base de datos y 
# respuestas del backend hacia el frontend.
#   →: La vista entrega al template las estructuras de datos recibidas del 
#      modelo en otro tipo de estructura llamada contexto para que se pueda 
#      mostrar al usuario en la UI (user interface).
#   ←: La vista recibe una petición (id, request y query) del template del 
#      template y se conectará al modelo para encontrar el dato.


def my_view(request):
    #Datos a mandar de la vista hacia el template, lo que después se 
    #traerá desde el modelo (base de datos), hacia la vista y luego el 
    #template.
    car_list = [
        {"title": "BMW"},
        {"title": "Mazda"},
    ]
    #Contexto: Es un diccionario de Python con información cambiante de la 
    #base de datos, es como un diccionario de listas de estructuras de datos
    #que vienen de la database.
    context = {
        "car_list": car_list
    }


    #render: Renderizar es tomar datos dinámicos del modelo y asignarlos a 
    #una template HTML para construir la página final que el usuario ve.
    #Para que Django encuentre el template que recibirá el resultado de la 
    #request se debe registrar la aplicación en el archivo: 
    #a_first_proyect/a_first_proyect/settings.py 
    #Aquí se buscará el array INSTALLED_APPS para agregar el nombre de 
    #nuestra app. En este caso, tras agregarla, el array quedará así:
    #INSTALLED_APPS = [
    #     'django.contrib.admin',
    #     'django.contrib.auth',
    #     'django.contrib.contenttypes',
    #     'django.contrib.sessions',
    #     'django.contrib.messages',
    #     'django.contrib.staticfiles',
    #     'a_app_name',
    #]
    #Posteriormente, deberemos crear la carpeta y archivo de 
    #a_first_proyect/a_app_name/templates/a_app_name/car_list.html
    return render(request, "a_app_name/car_list.html", context)