# Generated by Django 3.2.6 on 2021-11-30 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo del curso')),
                ('idioma', models.CharField(choices=[('I', 'Inglés'), ('A', 'Alemán'), ('F', 'Frances'), ('P', 'Portugués')], default='I', max_length=1)),
                ('nivel', models.CharField(choices=[('P', 'Principiante'), ('I', 'Intermedio'), ('A', 'Avanzado')], default='P', max_length=1)),
                ('duracion', models.PositiveIntegerField(default=30)),
                ('modalidad', models.CharField(choices=[('P', 'Presencial'), ('V', 'Virtual')], default='P', max_length=1)),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.profesor')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
    ]