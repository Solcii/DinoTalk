from django.shortcuts import render
from django.template import loader
from .models import Curso

def home(request):
    return render(request, 'index.html')

def cursos(request):
    cursos = Curso.objects.filter()
    return render(request, 'cursos.html', {'cursos': cursos} )

def contacto(request):
    return render(request, 'contacto.html')