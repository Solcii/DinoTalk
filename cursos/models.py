from django.db import models

class Profesor(models.Model):
    dni = models.CharField('DNI', max_length=8, primary_key=True)
    apellido = models.CharField('Apellido', max_length=50, null=False, blank=False)
    nombre = models.CharField('Nombre', max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    email = models.EmailField('Correo electrónico', null=False, blank=False)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo del curso', max_length=100, null=False, blank=False)
    idiomas = [
        ('I', 'Inglés'),
        ('A', 'Alemán'),
        ('F', 'Frances'),
        ('P', 'Portugués')
    ]
    idioma = models.CharField(max_length=1, choices=idiomas, default='I')
    niveles = [
        ('P', 'Principiante'),
        ('I', 'Intermedio'),
        ('A', 'Avanzado')
    ]
    nivel = models.CharField(max_length=1, choices=niveles, default='P')
    duracion = models.PositiveIntegerField('Duración (días)', default=30)
    modalidades = [
        ('P', 'Presencial'),
        ('V', 'Virtual')
    ]
    modalidad = models.CharField(max_length=1, choices=modalidades, default='P')
    profesor = models.ForeignKey(Profesor, null=False, blank=False, on_delete=models.CASCADE)
    inscripciones_abiertas = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f'{self.titulo}'


class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=50 ,null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    mensaje = models.CharField(max_length=800, null=False, blank=False)
    info_enviada = models.BooleanField('Solicitud respondida', default=False)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return f'Mensaje de: {self.nombre} - {self.email}'

