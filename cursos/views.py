from django.shortcuts import render
from django.template import loader
from .models import Curso
from django.db.models import Q

def home(request):
    return render(request, 'index.html')

def cursos(request):
    queryset = request.GET.get('buscar')
    cursos = Curso.objects.all()
    if queryset:
        cursos = Curso.objects.filter(Q(titulo__icontains = queryset))
    return render(request, 'cursos.html', {'cursos': cursos} )

def contacto(request):
    return render(request, 'contacto.html')