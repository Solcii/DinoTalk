from django.shortcuts import render
from django.template import loader

from cursos.forms import FormularioContacto
from .models import Contacto, Curso, Profesor
from django.db.models import Q, query


def home(request):
    return render(request, 'index.html')


def cursos(request):
    cursos = Curso.objects.all()

    print(Profesor.objects.all())

    queryset = request.GET.get('buscar')

    if queryset:
        cursos = Curso.objects.filter(Q(titulo__icontains=queryset))

    idioma_seleccionado = request.GET.get('idioma')
    if idioma_seleccionado and idioma_seleccionado != 'Seleccionar...':
        cursos = cursos.filter(idioma=idioma_seleccionado)

    nivel_seleccionado = request.GET.get('nivel')
    if nivel_seleccionado and nivel_seleccionado != 'Seleccionar...':
        cursos = cursos.filter(nivel=nivel_seleccionado)

    print(cursos)

    return render(request, 'cursos.html', {'cursos': cursos})


def contacto(request):
    if request.method == 'POST':
        formulario_contacto = FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            info_formulario = formulario_contacto.cleaned_data
            datos_contacto = Contacto()

            datos_contacto.asunto = info_formulario['asunto']
            datos_contacto.nombre = info_formulario['nombre']
            datos_contacto.email = info_formulario['email']
            datos_contacto.mensaje = info_formulario['mensaje']
            datos_contacto.save()

            return render(request, 'mensaje_recibido.html', {'respuestasFormulario': info_formulario})
    else:
        formulario_contacto = FormularioContacto()
        return render(request, 'contacto.html', {'form': formulario_contacto})
