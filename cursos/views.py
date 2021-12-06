from django.shortcuts import render
from django.template import loader
from .models import Curso
from django.db.models import Q, query

def home(request):
    return render(request, 'index.html')

def cursos(request):
    cursos = Curso.objects.all()

    queryset = request.GET.get('buscar')
    if queryset:
        cursos = Curso.objects.filter(Q(titulo__icontains = queryset))

    idioma_seleccionado = request.GET.get('idioma')
    if idioma_seleccionado and idioma_seleccionado != 'Seleccionar...':
        cursos = cursos.filter(idioma=idioma_seleccionado)

    nivel_seleccionado = request.GET.get('nivel')
    if nivel_seleccionado and nivel_seleccionado != 'Seleccionar...':
        cursos = cursos.filter(nivel=nivel_seleccionado)

    return render(request, 'cursos.html', {'cursos': cursos} )

def contacto(request):
    return render(request, 'contacto.html')