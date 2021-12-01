from django.shortcuts import render
from django.template import loader

def home(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'cursos.html')

def contacto(request):
    return render(request, 'contacto.html')