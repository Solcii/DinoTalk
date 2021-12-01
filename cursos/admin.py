from django.contrib import admin
from .models import Profesor
from .models import Curso

class ProfesorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido']
    list_display = ('nombre', 'apellido', 'email',)

class CursoAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','idioma','nivel', 'modalidad',)
    list_filter = ('idioma', 'nivel', 'modalidad','inscripciones_abiertas',)

admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Curso, CursoAdmin)
