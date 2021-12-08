from django.contrib import admin
from .models import Profesor
from .models import Curso
from .models import Contacto

class ProfesorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido']
    list_display = ('nombre', 'apellido', 'email',)

class CursoAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','idioma','nivel', 'modalidad',)
    list_filter = ('idioma', 'nivel', 'modalidad','inscripciones_abiertas',)

class ContactoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'email']
    list_display = ('asunto', 'nombre', 'email',)
    list_filter = ('info_enviada',)

admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Contacto, ContactoAdmin)
