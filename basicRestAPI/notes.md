**mi clave generica**

**crear un proyecto nuevo**
django-admin startproject myproject

**sincronizar db por primera vez**
python manage.py migrate

**crear nuevo usuario en db**
python manage.py createsuperuser --email admin@example.com --username admin

para cambiar la ruta del codigo fuente cambiar el source route del projecto para poder asi acceder a todos los modulos
sin problema

# necesita ser añadido para una restAPI

**'rest_framework',** dentro del array **INSTALLED_APPS** dentro del archivo settings.py

# añadir una nueva app al proyecto

añadir el nombre de la app dentro **INSTALLED_APPS** en settings.py

**se necesita realizar una migracion inicial para nuestro modelo de snippet y sincronizar la base de datos por primera
vez**
python manage.py makemigrations snippets python manage.py migrate snippets

# crear una clase serializada

permite añadir validaciones y valores por default a una clase nueva

**serializar a python**
traducir la instancia del modelo en una estructura nativa de python y posteriormente llevarlo a formato json

primero importar:

`from snippets.models import Snippet`

`from snippets.serializers import SnippetSerializer`

`from rest_framework.renderers import JSONRenderer`

`from rest_framework.parsers import JSONParser`

despues serializar la respuesta

`serializer = SnippetSerializer(snippet)`

`content = JSONRenderer().render(serializer.data)`

**deserializar**

`import io`

`stream = io.BytesIO(content)`

`data = JSONParser().parse(stream)`


