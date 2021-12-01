from django.urls import path
from .views import home
from .views import cursos
from .views import contacto

urlpatterns = [
    path('', home, name='index'),
    path('cursos', cursos, name='cursos'),
    path('contacto', contacto, name='contacto'),
]