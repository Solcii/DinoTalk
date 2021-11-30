from django.contrib import admin
from .models import Profesor
from .models import Curso

admin.site.register(Profesor)
admin.site.register(Curso)
