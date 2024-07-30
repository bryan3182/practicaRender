from django.contrib import admin
from .models import Genero 
# Register your models here.
admin.site.register(Genero)

from .models import Director
admin.site.register(Director)

from.models import Pais
admin.site.register(Pais)

from.models import Pelicula
admin.site.register(Pelicula)