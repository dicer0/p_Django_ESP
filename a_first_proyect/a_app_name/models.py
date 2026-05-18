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


#Clase donde primero se crea con una tabla, se añade a la base de datos y luego se 
#debe actualizar, debido a que se agregó otra columna.
class Car(models.Model):
    #Cada uno de los atributos que se agreguen a la clase, representarán una 
    #columna en la tabla de la base de datos.
    #models.TextField(): Clase o campo para decarar strings, recibe como parámetros:
    # - max_length: El número máximo de caracteres que puede recibir.
    # - null: Llena de valores NULL la DB cuando sea creada una nueva columna con 
    #   este tipo de dato.
    #Si queremos ver todos los campos disponibles que tenemos en Django para 
    #declarar distintos tipos de datos en los modelos, podemos acceder a este enlace: 
    #https://docs.djangoproject.com/en/5.0/ref/models/fields/
    title = models.TextField(max_length = 250)
    #Cada vez que se quiera hacer un cambio a una database existente con el 
    #archivo models.py, debemos ejecutar el comando python manage.py makemigrations 
    #y luego python manage.py migrate para que este se aplique a la base de datos, 
    #pero aquí vale la pena mencionar, que cada vez que se haga un cambio a una DB 
    #previamente creada, se le debe asignar un valor por defecto, para que este se 
    #asigne a las filas de datos anteriores a que esta nueva columna se agregara, 
    #ya sea NULL o un valor por específico por default y esto se muestra cuando se 
    #quiera agregar la migración. Para ello se utiliza el parámetro null = True.
    #Al crear la nueva migración, se creará otro archivo dentro de la carpeta 
    #migrations, que indicará todos los cambios hechos a la tabla en la DB.
    year = models.TextField(max_length = 4, null = True)

    #def __str__(self): El concepto de String en los modelos es un método cuya 
    #función es definir cómo se representa un objeto como texto cuando se imprime 
    #o se muestra en pantalla.
    def __str__(self):
        return f"{self.title} - {self.year}"
        #Para poder observar lo que este método está imprimiendo, debemos correr 
        #este código en consola después de haber ejecutado el comando:
        #       python manage.py shell
        #Y luego ejecutar el siguiente código Python para insertar datos a una DB:
        #from a_app_name.models import Car
        #my_car = Car(title="BMW", year="2023")
        #print(my_car) #Función __str__(): Se imprimirá en consola: BMW - 2023
        #my_car.save() #Método para guardar los datos del objeto en la DB.
        #my_car.title  #Así se accede al atributo actual del objeto.
        #my_car.title = "Mazda"  #Así se edita un atributo.
        #my_car.title  #Así se accede al atributo actual del objeto.
        #my_car.save()  #Método para actualizar los datos del objeto en la DB.
        #my_car.delete()#Método para borrar un objeto en la DB.
#Para que podamos escribir fácilmente código Python en consola, permitiéndonos 
#añadir, eliminar y modificar datos en la DB a través de objetos, debemos 
#instalar la librería iPython con el comando: pip install ipython y luego abrir 
#la consola con: python manage.py shell.



#Dos clases relacionadas entre ellas con llaves foráneas: Relación de uno a muchos, 
#muchos a muchos y de uno a uno.
class Publisher(models.Model):
    #Atributos (Columnas en la base de datos) de la clase (Tabla en la DB).
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)
    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.TextField(max_length=200)
    #models.DateField(): Clase para decarar timestamps, recibe como parámetros:
    # - auto_now: Hace que se guarde la hora y fecha de cuando se cree el objeto.
    birth_date = models.DateField()
    def __str__(self):
        return self.name
class Profile(models.Model): #Esta es información que se quiere añadir al Autor.
    #Relación de uno a uno: Al hacer esta conexión, solo la tabla que sea opcional 
    #de llenar, tendrá el métoodo OneToOneField() y dentro de su paréntesis recibirá 
    #la tabla principal de la relación.
    # - on_delete: Lo que se hace en este parámetro es indicar que es lo que va a 
    #   pasar en esta tabla, cuando la otra deje de existir.
    #       - models.DO_NOTHING: Esta opción hace que no le pase nada a esta tabla 
    #         cuando la otra sea borrada.
    #       - models.PROTECT: Esta opción lanza un error al intentar borrar la otra 
    #         tabla, evitando que esta pueda ser eliminada.
    #       - models.CASCADE: Esta opción elimina la tabla actual, cuando la otra 
    #         sea borrada.
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    #models.URLField(): Clase para decarar URLs.
    website = models.URLField()
    biography = models.TextField(max_length=500)
class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    #Relación de uno a muchos: Al hacer esta relación, debemos identificar cual de 
    #las tablas conectadas es la que tendrá la ForeignKey y esta es la que dependerá 
    #de la otra, en otras palabras, un libro puede tener una sola editorial 
    #(publisher), pero una editorial puede tener varios libros.
    #models.ForeignKey(): Clase para relacionar dos tablas entre ellas, para ello 
    #debe recibir entre paréntesis cual es la clase a la que se está relacionando.
    # - on_delete: Lo que se hace en este parámetro es indicar que es lo que va a 
    #   pasar en esta tabla, cuando la otra deje de existir.
    #       - models.DO_NOTHING: Esta opción hace que no le pase nada a esta tabla 
    #         cuando la otra sea borrada.
    #       - models.PROTECT: Esta opción lanza un error al intentar borrar la otra 
    #         tabla, evitando que esta pueda ser eliminada.
    #       - models.CASCADE: Esta opción elimina la tabla actual, cuando la otra 
    #         sea borrada.
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    #Relación de muchos a muchos: Al hacer esta conexión, ambas tablas relacionadas 
    #poseerán una ForeignKey de tipo ManyToManyField, ya que ambas dependen de la 
    #otra, en otras palabras, un libro puede tener varios autores y un autor puede 
    #tener varios libros.
    #models.ManyToManyField(): Clase para relacionar dos tablas entre ellas, para 
    #ello debe recibir entre paréntesis cual es la clase a la que se está 
    #relacionando.
    # - related_name: Hace referencia al nombre del atributo con el que se hace 
    #   referencia a esta tabla dentro de la otra.
    authors = models.ManyToManyField(Author, related_name="authors")
    #Managers: Son métodos que nos permiten ejecutar acciones en las listas de datos 
    #de una database (DB), a las cuales Django denomina como QuerySets, como contar, 
    #ver el primer y último elemento, etc. Imprimiendo en consola el valor que se 
    #haya declarado en la función string __str()__ de la clase:
    # - Clase.objects: El atributo objects es la forma en la que se puede aplicar un 
    #   manager hacia un objeto que sea instancia de una clase o tabla de una DB.
    #   A través del operador .objects se pueden utilizar distintos métodos para 
    #   ejecutar acciones específicas con las listas de datos que sacamos de las 
    #   filas de nuestras tablas de las bases de datos:
    #    - Clase.objects.count(): Cuenta todos los datos de la tabla "Clase".
    #    - Clase.objects.first(): Accede al primer dato de la tabla "Clase" en la DB.
    #    - Clase.objects.last(): Accede al último dato de la tabla "Clase" en la DB.
    #    - Clase.objects.all(): Accede al todos los datos de la tabla "Clase".
    #       - Clase.objects.all().order_by('columna'): Ordena de menor a mayor los 
    #         elementos de la tabla, en función del atributo dado en el paréntesis.
    #    - Clase.objects.filter(columna="valor"): Accede al dato de la tabla "Clase" 
    #      que cumpla con la condición dada en el paréntesis.
    #      -  Clase.objects.filter(columna="valor").detele(): Borra el registro de 
    #         la base de datos que cumpla con la condición descrita en el paréntesis.
    #    - Clase.objects.create(columna="valor"): Inserta un nuevo dato en la tabla.
    #        - Clase??: Este operador nos deja ver la clase para saber que datos se 
    #          deben introducir en las columnas de la tabla al crear un nuevo 
    #          registro (fila).
    #objeto = Clase.objects.first(): Este es un manager, el cual nos permite traer 
    #los datos de una clase en específico en la DB hacia nuestra terminal shell y 
    #guardarlo en una variable.
    #book.authors.set(List): Cuando se quiera añadir en la terminal shell de Django 
    #varios autores a un libro, primero se deberán introucir a una lista y luego 
    #utilizar el método set para añadirlos a su campo de authors. 
    def __str__(self):
        return self.title